from pathlib import Path
import csv

import numpy as np
from PIL import Image

from config import MASK_CSV
from src.analysis.dataset_loader import DatasetLoader
from logger_config import get_logger

logger = get_logger()

class MaskAnalyzer:

    def __init__(self, loader):
        self.loader = loader
        self.labels = self.loader.load_png_labels()


    def analyze(self):

        results = []

        for label_path in self.labels:

            mask = Image.open(label_path)
            mask_array = np.array(mask)

            total_pixels = mask_array.size
            foreground_pixels = np.count_nonzero(mask_array)

            foreground_percentage = round(
                float((foreground_pixels / total_pixels) * 100),
                2
            )

            results.append({
                "filename": label_path.name,
                "width": mask.width,
                "height": mask.height,
                "foreground_pixels": int(foreground_pixels),
                "background_pixels": int(total_pixels - foreground_pixels),
                "foreground_percentage": foreground_percentage
            })

        return results



    def save_csv(self, results, output_path=MASK_CSV):

        output_path = Path(output_path)

        with open(output_path, "w", newline="") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=results[0].keys()
            )

            writer.writeheader()
            writer.writerows(results)
        logger.info(
            f"Mask CSV saved successfully: {output_path}"
        )



if __name__ == "__main__":

    loader = DatasetLoader()

    analyzer = MaskAnalyzer(loader)

    results = analyzer.analyze()


    analyzer.save_csv(results)


    print("\n========== MASK ANALYSIS ==========\n")


    for item in results[:5]:
        print(item)


    logger.info(f"Mask CSV saved successfully: {output_path}")