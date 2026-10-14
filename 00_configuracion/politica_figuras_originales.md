# Política de figuras del libro — v1
**Decisión del proyecto:** usar recortes directos del PDF para toda figura tomada de Cardona; no pedir a Gemini que la redibuje.

1. Registrar sección, página impresa y número de figura.
2. Extraer usando `scripts/extraer_figuras.py` y la caja normalizada de `04_recursos_graficos/recortes.json`.
3. Inspeccionar el PNG: ningún eje, etiqueta o borde relevante puede quedar cortado.
4. El documento maestro debe identificar el archivo PNG exacto que se adjunta a Gemini. Si Gemini no permite adjuntos, debe reservar espacio y permitir inserción posterior.
5. Mejoras permitidas: recorte, escalado proporcional, contraste moderado; no modificar la construcción mecánica original.
6. Las imágenes PNG **no son editables por piezas**; el resto de los elementos de la diapositiva sí deben procurarse editables.
7. No publicar el PDF completo ni asumir libre redistribución de las figuras: comprobar los derechos del material para cada uso.
