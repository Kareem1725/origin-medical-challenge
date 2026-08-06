from pathlib import Path


# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent


# Output directories
FIGURES_DIR = PROJECT_ROOT / "figures"


# CSV output paths
IMAGE_CSV = PROJECT_ROOT / "image_analysis.csv"

MASK_CSV = PROJECT_ROOT / "mask_analysis.csv"


# Create folders if missing
FIGURES_DIR.mkdir(exist_ok=True)