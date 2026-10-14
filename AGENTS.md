# Instrucciones para Codex — proyecto Embragues

## Misión
Producir una presentación PowerPoint profesional de **100 diapositivas**, nivel máster, sobre **embragues**, basada en el libro *Teoría de máquinas* de Salvador Cardona y en el índice de `02_planificacion/indice_100_diapositivas.md`. El producto principal es `build/embragues_master_100.pptx` acompañado de registros de trazabilidad y QA.

## No modificar silenciosamente la fuente
- Leer primero `docs/CODEX_MASTER_PROMPT.md`, `00_configuracion/manual_visual.md`, `00_configuracion/politica_figuras_originales.md`, `00_configuracion/plantilla_documento_maestro.md` y `01_fuentes/trazabilidad_libro.md`.
- Para contenido derivado del libro, comprobar el PDF **real**, no confiar solo en la extracción textual cuando haya fórmulas o imágenes.
- Identificar explícitamente cada contenido de **Cardona** frente a cada **ampliación técnica**; nunca atribuirle a Cardona una ecuación o una figura nueva.
- Ecuaciones y figuras del libro: **recortes nítidos del PDF**. No redibujar por IA ni transcribir a mano sin verificación.
- Explicaciones: símbolos, índices y subíndices deben coincidir exactamente con la fórmula visible en el recorte. Crear un registro de símbolos por fórmula. No inventar símbolos ni equivalencias.
- Evitar que la presión/desgaste uniforme, par de fricción/enlace o número de superficies activas se confundan en las deducciones.

## Privacidad
Este repositorio es público. No subir el libro PDF ni sus recortes, imágenes o derivados extensivos al repositorio público. Utilizar `inputs_privados/` como ubicación local ignorada por Git. No insertar las imágenes en Markdown versionado. El archivo PPTX final puede contener material protegido: distribuir solo por un canal permitido.

## Formato, alcance y calidad
- **Exactamente 100 diapositivas** y orden D001–D100; no 99, 101 ni slides de relleno.
- Texto, títulos, anotaciones y formas complementarias como objetos PowerPoint editables.
- Figuras y fórmulas procedentes del libro serán **imágenes PNG**: editables solo como imágenes (no editables carácter por carácter).
- 16:9; consistencia visual, legibilidad y ausencia de solapes/cortes.
- Las ampliaciones tienen que contar con derivación física consistente y referencias externas bien identificadas o marcarse pendientes y NO presentarse como hechos verificados.
- No afirmar que QA pasó si no se ejecutó; detener entrega final cuando falten datos esenciales de una diapositiva.
- Hacer 3 pilotos D001, D028, D043 y validarlos visual/técnicamente antes de producir las 100.

## Comportamiento autónomo de Codex
Puedes añadir código, tests, documentos maestros, plantillas y scripts de render/QA. Ejecuta pruebas y genera informes. No hagas deploy. No elimines material del repositorio sin justificación. Proponer PR antes de integrar cambios amplios. Si falta el PDF, informar de la ruta exacta esperada y detener el análisis dependiente del libro, sin sustituirlo por información inventada.
