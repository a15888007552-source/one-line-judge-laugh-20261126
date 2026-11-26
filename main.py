"""Write the one-line entry to the output directory."""
import os
from pathlib import Path

# 140 characters, limit 200, one line.
LINE = 'I told my AI assistant to be more human, so now it sighs, says "per my last email," and schedules meetings it has no intention of attending.'

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(LINE, encoding="utf-8")
# Second pass: verified the line reads cleanly on its own, no setup needed.
