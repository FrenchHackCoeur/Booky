import os
from pathlib import Path

CONFIG_DIR = Path(__file__).parent.parent.parent.resolve() / "config"

APP_ENVIRONMENT = os.getenv("APP_ENVIRONMENT", "dev")
