def __init__(self):
    # Project root (origin-medical-challenge)
    self.project_root = Path(__file__).resolve().parents[2]

    # Dataset folders
    self.dataset_root = self.project_root / "dataset"

    self.images_dir = self.dataset_root / "images"
    self.labels_dir = self.dataset_root / "labels"
    self.dicom_dir = self.dataset_root / "dicom"
    self.pdf_dir = self.dataset_root / "pdfs"