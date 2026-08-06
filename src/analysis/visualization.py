from pathlib import Path

import numpy as np
from PIL import Image


import pandas as pd
import matplotlib.pyplot as plt

from config import FIGURES_DIR
from src.analysis.dataset_loader import DatasetLoader

from logger_config import get_logger

logger = get_logger()
class Visualization:

    def __init__(self):

        self.output_dir = FIGURES_DIR

        self.output_dir.mkdir(exist_ok=True)


    def load_data(self, image_csv, mask_csv):

        if not Path(image_csv).exists():
            raise FileNotFoundError(
                f"{image_csv} not found"
            )

        if not Path(mask_csv).exists():
            raise FileNotFoundError(
                f"{mask_csv} not found"
            )


        self.image_df = pd.read_csv(image_csv)
        self.mask_df = pd.read_csv(mask_csv)


        logger.info("CSV files loaded successfully")



    def plot_image_intensity(self):

        plt.figure(figsize=(8, 5))

        plt.hist(
            self.image_df["mean_pixel"],
            bins=30
        )

        plt.title(
            "Image Mean Pixel Distribution"
        )

        plt.xlabel(
            "Mean Pixel Value"
        )

        plt.ylabel(
            "Number of Images"
        )


        plt.savefig(
            self.output_dir / "image_mean_distribution.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

    def plot_mask_overlay(self):

        loader = DatasetLoader()

        images = loader.load_png_images()
        masks = loader.load_png_labels()

        image_path = images[0]
        mask_path = masks[0]

        image = Image.open(image_path).convert("L")
        mask = Image.open(mask_path).convert("L")

        image_array = np.array(image)
        mask_array = np.array(mask)

        plt.figure(figsize=(8, 5))

        plt.imshow(
            image_array,
            cmap="gray"
        )

        plt.imshow(
            mask_array,
            cmap="jet",
            alpha=0.35
        )

        plt.title(
            "Ultrasound Image with Mask Overlay"
        )

        plt.axis("off")

        plt.savefig(
            self.output_dir / "sample_mask_overlay.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        logger.info(
            "Mask overlay visualization generated successfully"
        )

    def plot_mask_foreground_ratio(self):

        plt.figure(figsize=(8, 5))

        plt.hist(
            self.mask_df["foreground_percentage"],
            bins=30
        )

        plt.title(
            "Mask Foreground Percentage Distribution"
        )

        plt.xlabel(
            "Foreground %"
        )

        plt.ylabel(
            "Number of Masks"
        )


        plt.savefig(
            self.output_dir / "mask_foreground_distribution.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()



    def plot_image_dimensions(self):

        plt.figure(figsize=(8, 5))

        plt.scatter(
            self.image_df["width"],
            self.image_df["height"]
        )

        plt.title(
            "Image Dimension Distribution"
        )

        plt.xlabel(
            "Width"
        )

        plt.ylabel(
            "Height"
        )


        plt.savefig(
            self.output_dir / "image_dimensions.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

    def generate_all(self):

        self.plot_image_intensity()

        self.plot_mask_foreground_ratio()

        self.plot_image_dimensions()

        self.plot_mask_overlay()

        logger.info("Visualization completed successfully")

if __name__ == "__main__":

    from config import IMAGE_CSV, MASK_CSV

    viz = Visualization()

    viz.load_data(
        IMAGE_CSV,
        MASK_CSV
    )

    viz.generate_all()