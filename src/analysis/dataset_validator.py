from pathlib import Path
from PIL import Image

from dataset_loader import DatasetLoader


class DatasetValidator:

    def __init__(self):
        self.loader = DatasetLoader()

        self.images = self.loader.load_png_images()
        self.labels = self.loader.load_png_labels()

    def check_image_label_pairs(self):
        # Compare image and label names after removing common suffixes
        image_names = {
            image.stem.replace("_HC", "").replace("_2HC", "")
            for image in self.images
        }

        label_names = {
            label.stem.replace("_Annotation", "").replace("_HC", "").replace("_2HC", "")
            for label in self.labels
        }

        missing_labels = image_names - label_names
        missing_images = label_names - image_names

        print("\nImage / Label Validation")
        print("-" * 40)

        if not missing_labels and not missing_images:
            print("✓ Every image has a matching label.")
            return

        if missing_labels:
            print("\nImages without labels:")
            for name in sorted(missing_labels):
                print(f"  - {name}")

        if missing_images:
            print("\nLabels without images:")
            for name in sorted(missing_images):
                print(f"  - {name}")

    def check_image_sizes(self):
        print("\nChecking image dimensions...")

        mismatch = 0

        for image_path, label_path in zip(self.images, self.labels):

            image = Image.open(image_path)
            label = Image.open(label_path)

            if image.size != label.size:
                mismatch += 1

        if mismatch == 0:
            print("✓ All image and label sizes match.")
        else:
            print(f"Found {mismatch} size mismatches.")

    def check_corrupt_files(self):
        print("\nChecking for corrupt images...")

        corrupt = 0

        for image_path in self.images:
            try:
                Image.open(image_path).verify()
            except Exception:
                corrupt += 1
                print(image_path.name)

        if corrupt == 0:
            print("✓ No corrupt image files found.")
        else:
            print(f"Found {corrupt} corrupt images.")

    def run(self):
        print("=" * 50)
        print("DATASET VALIDATION")
        print("=" * 50)

        self.check_image_label_pairs()
        self.check_image_sizes()
        self.check_corrupt_files()

        print("\nValidation Complete.")


if __name__ == "__main__":
    validator = DatasetValidator()
    validator.run()

    """During dataset validation, one unmatched image (230.png) and one unmatched label (231.png) were identified.
     This appears to be a dataset inconsistency. The remaining image-label pairs were successfully validated."""