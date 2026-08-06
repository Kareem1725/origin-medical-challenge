from src.analysis.dataset_loader import DatasetLoader
from src.analysis.image_analysis import ImageAnalyzer
from src.analysis.mask_analysis import MaskAnalyzer
from src.analysis.visualization import Visualization

from src.Validation.dataset_validator import DatasetValidator

from config import IMAGE_CSV, MASK_CSV
from logger_config import get_logger


logger = get_logger()



def main():

    logger.info(
        "========== PIPELINE STARTED =========="
    )


    # -----------------------------
    # Load Dataset
    # -----------------------------

    logger.info(
        "Loading dataset"
    )

    loader = DatasetLoader()



    # -----------------------------
    # Dataset Validation
    # -----------------------------

    logger.info(
        "Running dataset validation"
    )


    validator = DatasetValidator(loader)


    validation_results = validator.validate()


    validator.save_csv(
        validation_results,
        "dataset_validation.csv"
    )


    logger.info(
        "Dataset validation completed"
    )



    # -----------------------------
    # Image Analysis
    # -----------------------------

    logger.info(
        "Running image analysis"
    )


    image_analyzer = ImageAnalyzer(loader)


    image_results = image_analyzer.analyze()


    image_analyzer.save_csv(
        image_results,
        IMAGE_CSV
    )


    logger.info(
        "Image analysis completed"
    )



    # -----------------------------
    # Mask Analysis
    # -----------------------------

    logger.info(
        "Running mask analysis"
    )


    mask_analyzer = MaskAnalyzer(loader)


    mask_results = mask_analyzer.analyze()


    mask_analyzer.save_csv(
        mask_results,
        MASK_CSV
    )


    logger.info(
        "Mask analysis completed"
    )



    # -----------------------------
    # Visualization
    # -----------------------------

    logger.info(
        "Generating visualizations"
    )


    viz = Visualization()


    viz.load_data(
        IMAGE_CSV,
        MASK_CSV
    )


    viz.generate_all()



    logger.info(
        "Visualization completed"
    )



    logger.info(
        "========== PIPELINE COMPLETED SUCCESSFULLY =========="
    )



if __name__ == "__main__":

    main()