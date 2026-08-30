# Evidencias del laboratorio

Las imágenes listas para pegar se guardan en `images/`, numeradas en el mismo
orden del documento de entregables.

| Entregable | Archivo | Estado |
|---|---|---|
| Skill en `~/.agents/skills` y `~/.claude/skills` | `images/01-skill-directories.png` | Pendiente de generar |
| Skill invocado desde Copilot CLI | `images/02-copilot-cli.png` | Pendiente de generar |
| Skill invocado desde VS Code + Copilot Chat | `images/03-vscode-copilot.png` | Pendiente de generar |
| Skill invocado desde Cursor | `images/04-cursor.png` | Pendiente de generar |
| Skill invocado desde Gemini CLI (opcional) | — | No realizado: opcional |
| Skill invocado desde Codex (opcional) | `images/05-codex.png` | Pendiente de generar |
| Skill invocado desde Antigravity (opcional) | — | No realizado: opcional |

## Validaciones solicitadas

- Invocación directa: `/commit-message-writer`.
- Lenguaje natural: `genera el mensaje de commit para mis cambios staged`.
- Sin cambios staged: debe indicar que no hay cambios staged.
- Cambios no relacionados: debe proponer mensajes separados por tipo.

Los pasos opcionales no son necesarios para completar los entregables
obligatorios. No se instaló Gemini CLI ni Antigravity.
