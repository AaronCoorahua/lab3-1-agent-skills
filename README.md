# Laboratorio 3.1 — Creación de Agent Skills

Este repositorio contiene el skill `commit-message-writer` solicitado en el
laboratorio. Genera mensajes en formato Conventional Commits a partir del diff
staged y es compatible con asistentes que implementan el estándar Agent Skills.

Repositorio publicado: <https://github.com/AaronCoorahua/lab3-1-agent-skills>

## Estructura

```text
.
├── .agents/skills/commit-message-writer/SKILL.md
├── .claude/skills/commit-message-writer/SKILL.md
├── images/
├── EVIDENCIAS.md
└── task.py
```

La versión de `.agents/skills/` funciona en GitHub Copilot CLI, Cursor, Gemini
CLI y Codex. La copia de `.claude/skills/` permite demostrar el directorio
específico pedido para Claude Code.

## Pruebas

```powershell
copilot skill list
copilot -p "genera el mensaje de commit para mis cambios staged"
python task.py
```

Consulta [EVIDENCIAS.md](EVIDENCIAS.md) para saber qué captura corresponde a
cada entregable del laboratorio.
