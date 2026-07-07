import json
import os

class LensParser:
    def __init__(self, lens_path: str):
        self.lens_path = lens_path
        self.config = self._load()

    def _load(self):
        if not os.path.exists(self.lens_path):
            raise FileNotFoundError(f"Lens contract not found at {self.lens_path}")
        with open(self.lens_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    @property
    def bullshit_filter(self):
        return self.config.get("bullshit_filter", [])

    @property
    def deep_keywords(self):
        return self.config.get("deep_keywords", [])

    @property
    def target_sources(self):
        return self.config.get("target_sources", {})

    @property
    def drop_path(self):
        # We need to expand $ATLAS_ROOT if present
        path = self.config.get("delivery_protocol", {}).get("path", "./inbox")
        atlas_root = os.environ.get("ATLAS_ROOT", "")
        if atlas_root:
            path = path.replace("$ATLAS_ROOT", atlas_root)
        # Normaliza la ruta según el SO, elimina diagonales mixtas
        return os.path.normpath(path)
