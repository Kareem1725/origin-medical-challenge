from pathlib import Path
import csv

import numpy as np
from PIL import Image

from config import IMAGE_CSV
from src.analysis.dataset_loader import DatasetLoader

from logger_config import get_logger

logger = get_logger()


class ImageAnalyzer:

    def __init__(self, loader):
        self.loader = loader
        self.images = self.loader.load_png_images()


    def analyze(self):

        results = []

        for image_path in self.images:

            image = Image.open(image_path)
            image_array = np.array(image)

            results.append({
                "filename": image_path.name,
                "width": image.width,
                "height": image.height,
                "mode": image.mode,
                "min_pixel": int(image_array.min()),
                "max_pixel": int(image_array.max()),
                "mean_pixel": round(float(image_array.mean()), 2),
                "std_pixel": round(float(image_array.std()), 2)
            })

        return results



    def save_csv(self, results, output_path=IMAGE_CSV):

        output_path = Path(output_path)

        with open(output_path, "w", newline="") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=results[0].keys()
            )

            writer.writeheader()
            writer.writerows(results)

        logger.info(f"Image CSV saved successfully: {output_path}")



if __name__ == "__main__":

    loader = DatasetLoader()

    analyzer = ImageAnalyzer(loader)

    image_stats = analyzer.analyze()


    analyzer.save_csv(image_stats)


    print("\n========== IMAGE ANALYSIS ==========\n")


    for image in image_stats[:5]:
        print(image)


    print(f"\nTotal Images : {len(image_stats)}")