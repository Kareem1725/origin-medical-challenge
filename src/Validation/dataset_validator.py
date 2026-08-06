from pathlib import Path
import csv

from PIL import Image

from src.analysis.dataset_loader import DatasetLoader
from logger_config import get_logger


logger = get_logger()


class DatasetValidator:

    def __init__(self, loader):

        self.loader = loader

        self.images = self.loader.load_png_images()
        self.masks = self.loader.load_png_labels()



    def validate(self):

        results = []


        logger.info("Starting dataset validation")


        # -----------------------------
        # Image and Mask Count Check
        # -----------------------------

        results.append({
            "check": "Image count",
            "value": len(self.images),
            "status": "PASS"
        })


        results.append({
            "check": "Mask count",
            "value": len(self.masks),
            "status": "PASS"
        })



        # -----------------------------
        # Image-Mask Pair Validation
        # -----------------------------

        image_names = {
            img.stem
            for img in self.images
        }


        mask_names = {
            mask.stem.replace("_Annotation", "")
            for mask in self.masks
        }


        missing_masks = image_names - mask_names

        missing_images = mask_names - image_names



        # Log actual filenames

        logger.info(
            f"Missing masks: {missing_masks}"
        )

        logger.info(
            f"Missing images: {missing_images}"
        )



        results.append({
            "check": "Missing masks",
            "value": len(missing_masks),
            "status": "PASS"
            if len(missing_masks) == 0
            else "FAIL"
        })


        results.append({
            "check": "Missing images",
            "value": len(missing_images),
            "status": "PASS"
            if len(missing_images) == 0
            else "FAIL"
        })



        # -----------------------------
        # Dimension Validation
        # -----------------------------

        dimension_errors = 0


        for image_path, mask_path in zip(
                self.images,
                self.masks
        ):

            image = Image.open(image_path)

            mask = Image.open(mask_path)


            if image.size != mask.size:
                dimension_errors += 1



        results.append({
            "check": "Dimension mismatch",
            "value": dimension_errors,
            "status": "PASS"
            if dimension_errors == 0
            else "FAIL"
        })



        # -----------------------------
        # Empty Mask Validation
        # -----------------------------

        empty_masks = 0


        for mask_path in self.masks:

            mask = Image.open(mask_path)


            if not any(mask.get_flattened_data()):
                empty_masks += 1



        results.append({
            "check": "Empty masks",
            "value": empty_masks,
            "status": "PASS"
            if empty_masks == 0
            else "WARNING"
        })



        logger.info(
            "Dataset validation completed"
        )


        return results



    def save_csv(
            self,
            results,
            output_path="dataset_validation.csv"
    ):

        project_root = Path(__file__).resolve().parents[2]

        output_path = project_root / output_path



        with open(
                output_path,
                "w",
                newline=""
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=results[0].keys()
            )

            writer.writeheader()

            writer.writerows(results)



        logger.info(
            f"Validation report saved: {output_path}"
        )



if __name__ == "__main__":


    loader = DatasetLoader()


    validator = DatasetValidator(loader)


    results = validator.validate()



    print("\n========== DATASET VALIDATION ==========\n")


    for result in results:
        print(result)



    validator.save_csv(results)