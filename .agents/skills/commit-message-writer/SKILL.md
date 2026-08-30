---
name: commit-message-writer
description: >
  Genera mensajes de commit con formato Conventional Commits. Úsame cuando
  quieras escribir un commit, hacer commit de tus cambios, resumir tu diff
  staged, hacer "haz commit", crear un commit message o generar el mensaje
  para git commit. Produce una línea de asunto, cuerpo opcional y footer.
---

# Commit Message Writer

Inspecciona primero `git diff --staged`. Si no existe ningún cambio staged,
responde exactamente: `No hay cambios staged para generar un commit.`

## Formato de output

Usa la especificación Conventional Commits:

```text
type(scope): descripción corta

[cuerpo opcional]

[footer opcional]
```

## Tipos permitidos

- `feat` — nueva funcionalidad
- `fix` — corrección de bug
- `docs` — cambios en documentación
- `refactor` — refactorización sin cambio de comportamiento
- `test` — agregar o corregir tests
- `chore` — tareas de mantenimiento

## Reglas

1. Escribe la descripción corta en modo imperativo, por ejemplo `add`, no `added`.
2. Limita la primera línea a 72 caracteres.
3. Genera el mensaje directamente, sin hacer preguntas ni ejecutar el commit.
4. Nunca uses lenguaje vago como `update stuff` o `fix things`.
5. Si hay cambios no relacionados, propone mensajes separados y agrúpalos por tipo.
6. Basa el mensaje únicamente en el diff staged, no en archivos sin seguimiento ni cambios sin stage.

## Ejemplos

Correcto:

```text
feat(auth): add JWT token refresh endpoint
```

Incorrecto:

- `Updated the auth stuff` — es vago y no usa Conventional Commits.
- `feat: added new feature for authentication` — usa tiempo pasado y no tiene scope.
