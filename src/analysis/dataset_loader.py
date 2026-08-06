from pathlib import Path
from typing import Dict, List


class DatasetLoader:
    """

Loads all datasets required for the Origin Medical Challenge.
This function iterates through all directories and returns the
appropriate datasets for downstream processing.
"""

    def __init__(self):
        # Get the project root automatically
        self.project_root = Path(__file__).resolve().parents[2]

        # Dataset folder
        self.dataset_root = self.project_root / "dataset"

        self.images_dir = self.dataset_root / "images"
        self.labels_dir = self.dataset_root / "labels"
        self.dicom_dir = self.dataset_root / "dicom"
        self.pdf_dir = self.dataset_root / "pdfs"
    def load_png_images(self) -> List[Path]:
        return sorted(self.images_dir.rglob("*.png"))

    def load_png_labels(self) -> List[Path]:
        return sorted(self.labels_dir.rglob("*.png"))

    def load_dicom_files(self) -> List[Path]:
        return sorted(self.dicom_dir.rglob("*.dcm"))

    def load_pdf_reports(self) -> List[Path]:
        return sorted(self.pdf_dir.glob("*.pdf"))

    def summary(self) -> Dict[str, int]:
        return {
            "Images": len(self.load_png_images()),
            "Labels": len(self.load_png_labels()),
            "DICOM Files": len(self.load_dicom_files()),
            "PDF Reports": len(self.load_pdf_reports()),
        }


if __name__ == "__main__":

    loader = DatasetLoader()

    print("\n========== DATASET SUMMARY ==========\n")

    summary = loader.summary()

    for key, value in summary.items():
        print(f"{key:<20}: {value}")

    print("\n=====================================\n")