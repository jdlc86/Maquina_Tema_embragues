#!/usr/bin/env python3
"""Recorta figuras de PDF usando coordenadas normalizadas y un manifiesto JSON.

Uso:
 python scripts/extraer_figuras.py --pdf "libro.pdf" --manifest 04_recursos_graficos/recortes.json --all
 python scripts/extraer_figuras.py --pdf "libro.pdf" --id fig7_18_conico
Requiere: pip install pymupdf
"""
import argparse
import hashlib
import json
from pathlib import Path
import fitz

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", required=True, type=Path)
    parser.add_argument("--manifest", type=Path, default=Path("04_recursos_graficos/recortes.json"))
    parser.add_argument("--out", type=Path, default=Path("04_recursos_graficos/recortes"))
    choose = parser.add_mutually_exclusive_group(required=True)
    choose.add_argument("--all", action="store_true")
    choose.add_argument("--id")
    choose.add_argument("--list", action="store_true")
    parser.add_argument("--dpi", type=int, default=300)
    args = parser.parse_args()
    figures = json.loads(args.manifest.read_text(encoding="utf-8"))["figures"]
    if args.list:
        for e in figures:
            print(f"{e['id']}: PDF p.{e['pdf_page']}, figura {e['figure']}, archivo {e['file']}")
        return
    if not 72 <= args.dpi <= 900:
        parser.error("--dpi debe estar entre 72 y 900")
    selected = figures if args.all else [f for f in figures if f["id"] == args.id]
    if not selected:
        parser.error(f"Figura no encontrada: {args.id}")
    args.out.mkdir(parents=True, exist_ok=True)
    with fitz.open(args.pdf) as doc:
        for entry in selected:
            idx = entry["pdf_page"] - 1
            if not 0 <= idx < len(doc):
                raise ValueError(f"{entry['id']}: página PDF fuera de rango")
            x0, y0, x1, y1 = entry["bbox_norm"]
            if not (0 <= x0 < x1 <= 1 and 0 <= y0 < y1 <= 1):
                raise ValueError(f"{entry['id']}: coordenadas inválidas")
            page = doc[idx]
            r = page.rect
            rect = fitz.Rect(r.x0 + x0*r.width, r.y0 + y0*r.height,
                             r.x0 + x1*r.width, r.y0 + y1*r.height)
            pix = page.get_pixmap(matrix=fitz.Matrix(args.dpi / 72, args.dpi / 72),
                                  clip=rect, alpha=False)
            filename = entry["file"]
            if Path(filename).name != filename or not filename.endswith(".png"):
                raise ValueError(f"{entry['id']}: nombre de archivo inválido")
            destination = args.out / filename
            pix.save(destination)
            sha = hashlib.sha256(destination.read_bytes()).hexdigest()
            print(f"{entry['id']}: {destination} ({pix.width}x{pix.height}; sha256={sha[:16]}...)")

if __name__ == "__main__":
    main()
