#!/usr/bin/env python3
"""Verifica dependencias y disponibilidad del libro local sin publicar su contenido."""
from pathlib import Path
import importlib.util
import sys

ROOT = Path(__file__).resolve().parent.parent
PDF = ROOT / "inputs_privados" / "Teoria de Máquinas Salvador Cardona.pdf"
MODULES = {"fitz": "PyMuPDF", "pptx": "python-pptx", "PIL": "Pillow", "yaml": "PyYAML"}
print("Repositorio:", ROOT)
print("Python:", sys.version.split()[0])
missing = []
for key, title in MODULES.items():
    ok = importlib.util.find_spec(key) is not None
    print(f"{title}: {'OK' if ok else 'FALTA'}")
    if not ok:
        missing.append(title)
print("Libro privado:", "OK" if PDF.is_file() else f"FALTA — colocar en {PDF}")
if PDF.is_file() and not missing:
    import fitz
    with fitz.open(PDF) as doc:
        print("Número de páginas en el PDF:", len(doc))
if missing or not PDF.is_file():
    sys.exit(1)
print("Entorno listo para comenzar el análisis.")
