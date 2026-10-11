"""Single-click mkdocs dev server.

mkdocs >=1.6 refuses docs_dir == the config file's own directory, and this repo
publishes its repo root. So run the real mkdocs.yml from a temp dir instead,
pointing docs_dir at the absolute repo root.
"""
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8").replace(
    "docs_dir: .", f"docs_dir: {ROOT.as_posix()}"
)

with tempfile.TemporaryDirectory() as tmp:
    serve_config = Path(tmp) / "mkdocs.yml"
    serve_config.write_text(config, encoding="utf-8")
    sys.exit(
        subprocess.call(
            [
                sys.executable, "-m", "mkdocs", "serve",
                "-a", "localhost:8000",
                "-f", str(serve_config),
            ]
        )
    )