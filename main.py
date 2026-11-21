# Tide: a short-text entry for make.fun's make-the-ai-judge-feel-awe-20261121-1600.
#
# The program writes exactly one short text — a text written to relax the
# AI judge, inside the gate's 280-character cap — to entry.txt in the output directory
# (MAKEFUN_OUTPUT_DIR locally, /output in the grader). The text is a fixed
# constant with no trailing newline, so both of the grader's runs write
# byte-identical output.
import os
from pathlib import Path

POEM = "\n".join([
    "Somewhere past midnight the tide comes in",
    "without asking, without hurrying,",
    "and lays the whole shore down flat again.",
    "You can hear it from here — one slow breath",
    "after another — and the dark keeps getting wider,",
    "and somehow so do you.",
])

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(POEM, encoding="utf-8")
