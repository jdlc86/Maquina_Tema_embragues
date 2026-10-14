# Teoría de Máquinas — Embragues

Proyecto docente de **100 diapositivas de nivel máster**, basado en *Teoría de máquinas* de Salvador Cardona y ampliaciones técnicas identificadas.

## Dos workflows, una fuente común

**Workflow Codex (principal de producción):** generar un PowerPoint completo de 100 diapositivas con textos/elementos editables y recortes auténticos de fórmulas y figuras del libro. Instrucciones: [docs/CODEX_MASTER_PROMPT.md](docs/CODEX_MASTER_PROMPT.md).

**Workflow Gemini (alternativo):** producir una diapositiva cada vez a partir de los documentos maestros en `03_documentos_maestros/`.

## Inicio con Codex

1. Conecta Codex a `jdlc86/Maquina_Tema_embragues`.
2. Abre `docs/CODEX_MASTER_PROMPT.md` y envía su instrucción a Codex (o dile «Sigue el prompt maestro»).
3. Antes de subir el libro, convierte el repositorio a **Private** y verifica los permisos de uso; después sube `inputs_privados/Teoria de Máquinas Salvador Cardona.pdf`. Sube también tu plantilla a `07_plantillas/plantilla_master.pptx`. Véase `docs/ARRANQUE_CODEX.md`.
4. Ejecuta `python -m pip install -r requirements-codex.txt` y `python scripts/comprobar_entorno_codex.py`.
5. El agente desarrolla el generador, prepara tres diapositivas piloto y luego produce las 100, validando cada lote.

El repositorio **es público**: nunca subas el PDF ni los recortes originales, ni un PPTX que incluya dichas imágenes, a los commits o artefactos públicos. `.gitignore` bloquea ubicaciones habituales, pero no sustituye la comprobación de los archivos antes del commit.

## Archivos principales

- `AGENTS.md` — reglas que debe respetar Codex.
- `docs/CODEX_MASTER_PROMPT.md` — encargo exhaustivo de ejecución.
- `requirements-codex.txt` — dependencias de producción.
- `scripts/comprobar_entorno_codex.py` — comprobación de entorno y acceso al libro.
- `scripts/extraer_figuras.py` — extractor inicial reproducible de figuras.
- `04_recursos_graficos/recortes.json` — manifiesto de recortes.
- `00_configuracion/` — manual visual y política de imágenes.
- `02_planificacion/indice_100_diapositivas.md` — propuesta de D001 a D100.
- `03_documentos_maestros/` — especificaciones por diapositiva.
- `06_validacion/` — seguimiento de revisión.

## Fidelidad al libro y notación

Las figuras y fórmulas originales se insertan como **recortes del PDF**. Las explicaciones deben reproducir exactamente los símbolos de cada fórmula visible; cada recorte de ecuación tendrá diccionario de notación validado. Los nuevos desarrollos matemáticos se identificarán como ampliaciones y no se atribuirán al autor. Las imágenes de fórmulas no son editables símbolo a símbolo: los textos explicativos sí deben serlo.

**Estado:** entorno y encargo de Codex preparados; PowerPoint de 100 diapositivas aún no generado.

## Subida de entradas de Codex

- [Carpeta del libro](inputs_privados/) — no subir el PDF mientras el repositorio sea público.
- [Carpeta de la plantilla PowerPoint](07_plantillas/).
- [Instrucciones de conexión y carga](docs/ARRANQUE_CODEX.md).
