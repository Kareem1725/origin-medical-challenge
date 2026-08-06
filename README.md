# Medical Image Analysis Pipeline

## Overview

This project implements an automated medical image analysis pipeline for ultrasound image datasets.

The pipeline performs:
- Dataset loading
- Dataset validation
- Image statistical analysis
- Mask/segmentation analysis
- Visualization generation
- Automated report generation

The goal is to analyze medical images and their corresponding segmentation masks before further machine learning model development.

---

# Project Workflow

Dataset
|
|
Dataset Loader
|
|
Dataset Validation
|
|
Image Analysis
|
|
Mask Analysis
|
|
Visualization
|
|
Reports & Logs


---

# Dataset Structure

The input dataset contains:


dataset/

├── images/
│ └── Ultrasound PNG images
│
├── labels/
│ └── Segmentation mask PNG images
│
├── dicom/
│ └── DICOM medical image files
│
└── pdfs/
└── Supporting documents


---

# Project Structure


origin-medical-challenge/

│
├── dataset/
│
├── src/
│ │
│ ├── analysis/
│ │ ├── dataset_loader.py
│ │ ├── image_analysis.py
│ │ ├── mask_analysis.py
│ │ └── visualization.py
│ │
│ └── validation/
│ └── dataset_validator.py
│
├── figures/
│ ├── image_mean_distribution.png
│ ├── mask_foreground_distribution.png
│ ├── image_dimensions.png
│ └── sample_mask_overlay.png
│
├── logs/
│ └── pipeline.log
│
├── image_analysis.csv
├── mask_analysis.csv
├── dataset_validation.csv
│
├── main.py
├── config.py
├── logger_config.py
├── requirements.txt
└── README.md


---

# Features

## 1. Dataset Validation

The validation module checks dataset quality before analysis.

Validation includes:

- Image count verification
- Mask count verification
- Missing image-mask pair detection
- Image and mask dimension consistency
- Empty segmentation mask detection

Example output:


Image count : PASS
Mask count : PASS
Dimension mismatch : PASS
Empty masks : PASS


Generated report:


dataset_validation.csv


---

# 2. Image Analysis

The image analysis module extracts statistical information from ultrasound images.

For every image, the pipeline calculates:

- Filename
- Image width
- Image height
- Image mode
- Minimum pixel intensity
- Maximum pixel intensity
- Mean pixel intensity
- Pixel standard deviation


Generated report:


image_analysis.csv


Example:


filename width height mean_pixel

003_HC.png 800 540 45.55
005_HC.png 800 540 63.01


---

# 3. Mask Analysis

The mask analysis module evaluates segmentation annotations.

For every mask, it calculates:

- Mask dimensions
- Foreground pixel count
- Background pixel count
- Foreground percentage


Generated report:


mask_analysis.csv


Example:


filename foreground_percentage

003_HC_Annotation.png 55.92
005_HC_Annotation.png 37.33


---

# 4. Visualization

The visualization module creates graphical summaries from generated CSV reports.

Generated visualizations:

## Image Mean Pixel Distribution

Shows the intensity distribution across ultrasound images.

Output:


image_mean_distribution.png


---

## Mask Foreground Distribution

Shows the distribution of segmentation coverage percentages.

Output:


mask_foreground_distribution.png


---

## Image Dimension Distribution

Checks image resolution consistency.

Output:


image_dimensions.png


---

## Mask Overlay Visualization

Creates image-mask overlays to verify segmentation alignment visually.

Output:


sample_mask_overlay.png


---

# Logging System

The pipeline includes a logging system for execution tracking.

Logs include:

- Pipeline start
- Dataset validation status
- Analysis completion
- Visualization completion
- Errors and warnings


Generated log:


logs/pipeline.log


Example:


INFO - PIPELINE STARTED
INFO - Dataset validation completed
INFO - Image analysis completed
INFO - Visualization completed successfully


---

# Installation

## Clone Repository

```bash
git clone <repository-url>

Navigate into the project:

cd origin-medical-challenge
Create Virtual Environment
python -m venv .venv

Activate environment:

Windows:

.venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Running the Pipeline

Execute:

python main.py

The complete pipeline will automatically execute:

Dataset loading
Dataset validation
Image analysis
Mask analysis
Visualization generation
Logging
Generated Outputs

After successful execution:

origin-medical-challenge/

├── image_analysis.csv
│
├── mask_analysis.csv
│
├── dataset_validation.csv
│
├── figures/
│
└── logs/
Technologies Used
Python
NumPy
Pandas
Pillow (PIL)
Matplotlib
CSV Processing
Logging
Dataset Validation Observation

The provided dataset was analyzed without modifying the original files.

During validation, one unmatched image-mask pair was detected:

Missing Mask:
230_2HC

Missing Image:
231_HC

The issue is reported through validation logs and CSV reports.

Future Improvements

Possible future extensions:

DICOM metadata extraction
Automated PDF report generation
Data augmentation pipeline
Deep learning segmentation model integration
U-Net based segmentation training
Evaluation metrics:
Dice Score
IoU
Precision
Recall
