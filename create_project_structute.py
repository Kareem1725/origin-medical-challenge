from pathlib import Path

# Project Root
ROOT = Path(".")

# Folder Structure
folders = [
    "dataset",
    "dataset/images",
    "dataset/labels",
    "dataset/dicom",
    "dataset/pdfs",

    "src",
    "src/analysis",
    "src/deidentify",
    "src/utils",

    "notebooks",
    "reports",
    "figures",

    "logs",
    "config",
    "tests",
]

# Files to Create
files = [
    "main.py",
    "README.md",
    "requirements.txt",
    "Dockerfile",
    "docker-compose.yml",
    ".gitignore",
    "config/config.yaml",

    "src/__init__.py",
    "src/analysis/__init__.py",
    "src/deidentify/__init__.py",
    "src/utils/__init__.py",

    "src/analysis/dataset_loader.py",
    "src/analysis/dataset_validator.py",
    "src/analysis/image_analysis.py",
    "src/analysis/mask_analysis.py",
    "src/analysis/visualization.py",
    "src/analysis/statistics.py",

    "src/deidentify/dicom_processor.py",
    "src/deidentify/pdf_processor.py",
    "src/deidentify/metadata_extractor.py",
    "src/deidentify/pipeline.py",

    "src/utils/logger.py",
    "src/utils/helpers.py",
]

# Create folders
for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)

# Create files
for file in files:
    path = Path(file)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch(exist_ok=True)

print("=" * 50)
print("✅ Origin Medical Challenge structure created!")
print("=" * 50)