# Inicio del trabajo en Codex

## Estructura de entrada ya preparada

- `inputs_privados/` — libro `Teoria de Máquinas Salvador Cardona.pdf`. **No subir mientras el repositorio sea público.**
- `07_plantillas/` — `plantilla_master.pptx`, archivo que subirá el usuario.
- `docs/CODEX_MASTER_PROMPT.md` — encargo completo de 100 diapositivas.
- `AGENTS.md` — reglas y controles de producción.

## Cómo preparar GitHub

1. En el repositorio `jdlc86/Maquina_Tema_embragues`, ve a **Settings → General → Danger Zone → Change repository visibility** y cámbialo a privado **antes de subir el libro**, siempre que tengas permiso para compartirlo en ese entorno.
2. Abre `inputs_privados/` y sube el PDF del libro mediante **Add file → Upload files** con el nombre exacto esperado.
3. Abre `07_plantillas/` y sube el PPTX con el nombre `plantilla_master.pptx`.
4. Conecta Codex con acceso al repositorio privado; Codex debe realizar checkout o clonar el repositorio en su propio entorno antes de trabajar.
5. Instruye a Codex: «Lee AGENTS.md y docs/CODEX_MASTER_PROMPT.md; comprueba las dos entradas y ejecuta el proyecto».
6. El PPTX de salida con las imágenes del libro no se debe publicar en un repositorio público o artefacto accesible a terceros.

## Nota sobre .gitignore
GitHub Web permite subidas que no están sujetas al `.gitignore` de una copia local. Para subir el libro desde una copia local con Git habría que decidir conscientemente cómo incorporarlo; no elimines protecciones mientras el repositorio siga público.

## Salida esperada
`build/embragues_master_100.pptx` y documentación de QA. El entorno de Codex es independiente de la biblioteca de ChatGPT, por lo que no ve el libro allí de forma automática.
