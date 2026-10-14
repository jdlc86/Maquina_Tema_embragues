# PROMPT MAESTRO PARA CODEX — Embragues, 100 diapositivas

## Rol y objetivo
Actúa como **ingeniero de contenidos de Teoría de Máquinas**, **desarrollador Python/PowerPoint** y **auditor de calidad visual y matemática**. Tu misión es construir una presentación PowerPoint **completa, profesional y de nivel máster, exactamente de 100 diapositivas**, utilizando el repositorio `jdlc86/Maquina_Tema_embragues`.

No debes limitarte a escribir un plan: desarrolla el generador, completa los documentos maestros pendientes, crea el PowerPoint, renderiza y valida el resultado. Trabaja por hitos verificables y reporta bloqueos objetivos.

## Entrada y fuentes
1. Repositorio: `jdlc86/Maquina_Tema_embragues`.
2. Fuente principal: *Teoría de máquinas* de Salvador Cardona, proporcionado **privadamente** en `inputs_privados/Teoria de Máquinas Salvador Cardona.pdf`. El usuario prevé subir el libro a `inputs_privados/` en GitHub **solo después de cambiar el repositorio a privado y comprobar los permisos de uso**. Si falta, solicita adjuntarlo o montarlo privadamente en esa ruta y no atribuyas al libro contenidos que no puedas verificar.
3. Índice inicial: `02_planificacion/indice_100_diapositivas.md`. Contiene D001–D100; considera títulos y anclajes **provisionales** y conserva la distinción entre contenido Cardona y ampliación.
4. Manual de diseño: `00_configuracion/manual_visual.md`.
5. Política de imágenes: `00_configuracion/politica_figuras_originales.md`.
6. Plantilla de documentos maestros: `00_configuracion/plantilla_documento_maestro.md`.
7. Herramienta inicial para recortes: `scripts/extraer_figuras.py` y `04_recursos_graficos/recortes.json`.
8. Pilotos existentes: `03_documentos_maestros/D001.md`, `D028.md`, `D043.md` (necesitan adaptación/validación). No tomes los pilotos como correctos por defecto.
9. **Plantilla PPTX**: buscar primero `07_plantillas/plantilla_master.pptx`, que el usuario subirá a GitHub. Si está presente, úsala; en otro caso crea una plantilla programática en estilo técnico-profesional, 16:9, fondo claro, azul grafito, tipografía legible. Todos los elementos del sistema de diseño han de ser reproducibles desde código.

## Puntos críticos y controles obligatorios

### I. Fuente científica
- Inspecciona las páginas del PDF necesarias para cada diapositiva. Lee texto y comprueba visualmente imágenes y expresiones matemáticas.
- Cada diapositiva debe tener una ficha con: ID, título, objetivo didáctico, referencias bibliográficas (página impresa, sección y figura/ecuación si procede), contenido exacto, hipótesis, notación, recortes requeridos, instrucciones de composición y estado de verificación.
- No inventes fuentes, páginas o numeraciones; si no se pueden verificar, marca `pendiente_fuente` y bloquea la publicación final como validada.
- El libro tiene un tratamiento concentrado de embragues en §7.5 y principios de rozamiento en §7.4. Para completar 100 diapositivas de máster se requieren ampliaciones técnicas. Márcalas como **ampliaciones** y justifícalas rigurosamente.
- No sustituyas por terminología tuya la del libro de forma silenciosa; cualquier variable nueva o equivalencia debe documentarse.

### II. Figuras y fórmulas: política no negociable
- Toda **figura tomada del libro** debe insertarse como **recorte directo del PDF**, nunca como recreación generativa.
- Toda **fórmula del libro** que se muestre gráficamente debe insertarse como **recorte directo del PDF**.
- Recortar a resolución legible, preservar proporción, márgenes mínimos adecuados y procedencia.
- Extender el extractor para admitir entradas de tipo `figure` y `equation`, asociadas a diapositivas.
- Crear para cada fórmula un **diccionario exacto de símbolos visibles**, que incluya forma Unicode/LaTeX solo como apoyo, significado y unidades, y estado de inspección. No completar símbolos a partir de suposiciones.
- **Los textos que explican fórmulas deben utilizar los mismos símbolos, mayúsculas, índices y subíndices que aparecen en el recorte**. Añade una comprobación automática de las explicaciones contra el diccionario y una revisión humana para confusiones visuales.
- Cuando hagas una deducción matemática NUEVA para una ampliación, puedes crear una ecuación nativa PowerPoint si es técnicamente verificable, pero no atribuirla al libro ni presentarla como recorte original.
- En el archivo final, el recorte de ecuación es una imagen no editable carácter a carácter; los textos de su explicación sí deben ser editables. No afirmes editabilidad integral.

### III. Construcción PowerPoint
- Implementa un generador **reproducible** preferentemente con Python (`python-pptx`, `PyMuPDF`, `Pillow`), o alternativa argumentada, que produzca `build/embragues_master_100.pptx`.
- Debe soportar composición por plantillas, reutilización de estilos y registro de objetos vinculados a cada diapositiva.
- Estilo profesional, sin exceso de texto. Equilibrar carga cognitiva y nivel técnico mediante desarrollo gradual, ejemplos, derivaciones y síntesis.
- Guardar imagen en calidad suficiente para proyección; nunca deformar su proporción.
- Nombres coherentes de diapositivas: D001…D100, con notas de procedencia (metadatos o fichero de trazabilidad).
- Cuando sea técnicamente útil, crear ilustraciones propias solo para contenido **complementario**, diferenciadas de figuras de Cardona.

### IV. Pruebas automáticas y visuales
Crear scripts de QA para:
1. **Número = 100** y orden correcto.
2. Presencia de títulos, componentes obligatorios y vínculos de procedencia.
3. Existencia y resolución mínima práctica de los recortes según tamaño en el lienzo.
4. Integridad de todas las imágenes, sin distorsión y sin páginas recortadas erróneamente.
5. Límites geométricos, textos sobrepuestos o fuera del lienzo, fuentes legibles; los controles automáticos no sustituyen inspección visual.
6. Concordancia de notación: símbolos originales frente a explicación textual.
7. Informe final con incidencias por DNNN; cualquier incidencia crítica mantiene estado NO APROBADO.

Renderizar diapositivas a PNG/PDF, crear mosaicos por lotes de 10 y revisar visualmente pilotos + lotes. No entregar como completo algo sin inspección real. Para ejecutar LibreOffice o render, comprobar que el entorno dispone de las herramientas.

### V. Desarrollo incremental y entregables
**Fase A. Preparación:** verifica dependencias, integridad del PDF y las reglas existentes; implementa generador y extractor de fórmulas.
**Fase B. Piloto:** D001 (conceptual), D028 (figura original cónica 7.18), D043 (geometría/ecuaciones de ampliación). Renderizar, revisar, corregir estilos y registrar resultado.
**Fase C. Producción:** generar fichas y diapositivas D001–D100 en bloques de diez; testear cada bloque; mantener registro de decisiones y de incidencias.
**Fase D. Integración:** construir `build/embragues_master_100.pptx`, ejecutar todas las pruebas y redactar `build/QA_REPORT.md`, `build/SLIDE_SOURCES.csv` y galería de previsualizaciones.
**Fase E. Entrega:** facilitar el PowerPoint final como artefacto de trabajo por canal autorizado (no exponer recortes protegidos públicamente); subir código, metadatos **sin imágenes protegidas** y documentación al repositorio mediante una PR.

## Restricciones de flujo GitHub
- El repositorio es público hasta su conversión explícita a privado. NO subir el libro ni recortes de ecuaciones/figuras a un repositorio, PR, issue, artefacto o Pages público. Si el usuario transforma el repositorio a privado y tiene autorización, el libro puede estar versionado en `inputs_privados/`, accesible a Codex por checkout autenticado.
- No publicar el PPTX con recortes originales en GitHub público. Entregarlo mediante la sesión/archivo privado habilitado. Verificar visibilidad efectiva del repositorio antes de cualquier subida de material de terceros.
- El material bibliográfico privado solo reside en directorios ignorados por Git (`inputs_privados/` y `04_recursos_graficos/recortes/`).
- No crear 100 diapositivas ficticias si no está disponible el libro. Detenerse y pedirlo; no inventar evidencia.

## Comunicación y control de cambios
Trabaja con PR para el generador y los documentos maestros. Documenta lo ejecutado, las pruebas y sus resultados reales. Mantén una lista breve de tareas pendientes. Si una fase falla, resuélvela antes de avanzar. La revisión posterior a los pilotos es obligatoria.

**Comienza ahora:** inspecciona el repositorio y comprueba si existe `inputs_privados/Teoria de Máquinas Salvador Cardona.pdf`. Si no existe, indica cómo proporcionarlo en privado. Si existe, ejecuta Fase A y continúa hasta el PowerPoint final con las puertas de calidad establecidas.
