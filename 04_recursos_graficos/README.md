# Extracción reproducible de figuras

El proyecto utiliza los **recortes exactos del PDF original**, sin recreación por IA. Los recortes están definidos en `recortes.json`. La numeración de `pdf_page` empieza en 1, no en 0.

## Requisitos
- Python 3.10 o superior
- `pip install pymupdf`

## Instrucciones
Coloca el libro PDF en tu equipo (no se incluye en este repositorio), luego ejecuta desde la raíz:

```bash
python scripts/extraer_figuras.py --pdf "Teoria de Máquinas Salvador Cardona.pdf" --manifest 04_recursos_graficos/recortes.json --list
python scripts/extraer_figuras.py --pdf "Teoria de Máquinas Salvador Cardona.pdf" --manifest 04_recursos_graficos/recortes.json --all --dpi 300
```

Para extraer solo el embrague cónico:

```bash
python scripts/extraer_figuras.py --pdf "Teoria de Máquinas Salvador Cardona.pdf" --id fig7_18_conico
```

Los archivos se guardan por defecto en `04_recursos_graficos/recortes/`.

## Editar un recorte
Cada `bbox_norm` contiene las fracciones `[izquierda, arriba, derecha, abajo]` de la página del PDF (de 0 a 1). Las cajas actuales se revisaron sobre la página 178. Se puede añadir una entrada por cada figura o subfigura. **Es necesario inspeccionar cada resultado visualmente** y corregir la caja si corta ejes, rótulos o flechas.

## Procedencia y limitaciones
Fuente: Salvador Cardona, *Teoría de máquinas*, página impresa 178, figura 7.18. Los recortes se utilizan como imágenes del libro (PNG); **no** son dibujos desagrupables. El uso y distribución de las imágenes debe respetar los derechos de autor y el contexto docente. El PDF completo no se publica.
