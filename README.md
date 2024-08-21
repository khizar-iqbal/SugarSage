# SugarSage

SugarSage is an AI-powered Diet Recommendation System designed to help diabetic patients in Pakistan manage their dietary needs. With diabetes affecting 31% of the population, SugarSage offers personalized diet recommendations based on individual preferences, sugar levels, energy needs, and locally available foods. The system also tracks physical activity and sleep patterns, providing a comprehensive solution for diabetes management.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Models](#models)
- [Docker Setup](#docker-setup)

## Introduction

SugarSage addresses the challenges of diabetes management by using two machine learning models:

- **Model 1: XGBoost Regressor**
  - **Input:** User's dietary profile (age, gender, activity level, dietary habits).
  - **Output:** Predicts the optimal percentage of carbohydrates, fats, and proteins in the diet to maintain balanced sugar levels.

- **Model 2: XGBoost Classifier**
  - **Input:** User health metrics and food item data.
  - **Output:** Scores each food item (1 to 10) based on its suitability for the user's diet.

## Features

- **XGBoost Regressor and Classifier:** Implementation of XGBoost for both regression and classification tasks.
- **Comprehensive Pipeline:** Combines various preprocessing and model training steps into a single, streamlined process.
- **Docker Integration:** The project is Dockerized for easy deployment and scalability.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/khizar-iqbal/SugarSage-Models.git
   cd SugarSage-Models
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. For Docker setup:
   ```bash
   docker build -t sugarsage .
   docker run -p 5000:5000 sugarsage
   ```

## Project Structure

Here's an overview of the project's directory structure:

```plaintext
SugarSage-Models/
│   About This Directory.txt
│   Book_Food_Composition_Table_for_Pakistan_.pdf
│   food exchange list.pdf
│
├───Docker Setup
│   │   app.py
│   │   Dockerfile
│   │   Model 01 Pipeline.pkl
│   │   Model 02 Pipeline.pkl
│   │   requirements.txt
│   │
│   ├───Model 02 Dependencies
│   │       Target Encoder.pkl
│   │
│   └───Payload
│       │   Payload Maker.ipynb
│       │
│       ├───Dependencies
│       │   │   User Profile.csv
│       │   │
│       │   └───Categories
│       │           1. Cereal and Cereal Products.xlsx
│       │           2. Legumes.xlsx
│       │           3. Vegetables.xlsx
│       │           4. Fruits.xlsx
│       │           5. Nuts and Dry Fruits.xlsx
│       │           6. Dairy Products.xlsx
│       │           7. Meat and Meat Products.xlsx
│       │           8. Fish.xlsx
│       │           9. Eggs.xlsx
│       │           10. Sugar - Sweets and Beverages.xlsx
│       │           11. Dishes.xlsx
│       │
│       └───Outputs
│               Payload.json
│
└───Models Combined
    │   Model 01 Final.ipynb
    │   Model 02 Final.ipynb
    │
    ├───Model 01 Dependencies
    │       Model 01 Pipeline.pkl
    │
    └───Model 02 Dependencies
        │   Model 02 Pipeline.pkl
        │   Target Encoder.pkl
        │   User Profile.csv
        │
        └───Categories
                1. Cereal and Cereal Products.xlsx
                2. Legumes.xlsx
                3. Vegetables.xlsx
                4. Fruits.xlsx
                5. Nuts and Dry Fruits.xlsx
                6. Dairy Products.xlsx
                7. Meat and Meat Products.xlsx
                8. Fish.xlsx
                9. Eggs.xlsx
                10. Sugar - Sweets and Beverages.xlsx
                11. Dishes.xlsx
```

## Models

### Model 01: XGBoost Regressor
- **Task:** Regression
- **Purpose:** Predict the values of carbs, fats, and proteins as a percentage of the entire diet for a specific user based on the provided features.
- **Algorithm:** XGBoost Regressor

### Model 02: XGBoost Classifier
- **Task:** Classification
- **Purpose:** Given user information and food information, this model provides a score for each food item for that user, ranging from 1 to 10.
- **Algorithm:** XGBoost Classifier

## Docker Setup

The project includes a Docker setup to facilitate easy deployment. The Docker container runs the predictive models as a REST API.

1. **Build the Docker Image:**
   ```bash
   docker build -t sugarsage .
   ```

2. **Run the Docker Container:**
   ```bash
   docker run -p 5000:5000 sugarsage
   ```
