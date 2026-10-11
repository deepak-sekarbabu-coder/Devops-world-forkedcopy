# AGENTS.md

## Windows shell — read the glossary first (all agents, every session)

Canonical command reference for this machine:
`C:\Users\deepa\.config\opencode\windows-command-glossary.md`
— syntax, quoting rules, and failure log for PowerShell 5.1 / `cmd.exe`.

Before ANY terminal command:

1. Read the glossary's Quick reference + Failure log; reuse the closest documented syntax.
2. Shell is PowerShell 5.1 (`dir` = `Get-ChildItem`; no `&&`, no `sudo`, no GNU utils). Use `cmd /c "..."` only for CMD-only flags.
3. Validate quoting/paths (`-LiteralPath`, quote spaces), execute, inspect output.
4. On failure, record it: append `command | error | cause | fix` to the glossary's Failure log, then retry with the corrected syntax.
