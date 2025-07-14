# Credit Risk System

A machine learning-powered web application built with Streamlit that predicts credit risk based on various financial and personal factors.

## Overview

The Credit Risk System is designed to assess the creditworthiness of loan applicants by analyzing multiple features including personal information, employment details, loan characteristics, and credit history. The system uses a pre-trained Decision Tree Classifier to make predictions.

## Dataset Information

The model was trained using a credit risk dataset sourced from **Kaggle**. The dataset contains historical loan data with various features that help predict whether a loan applicant is likely to default or not.

### Dataset Details:
- **Source**: Kaggle
- **Dataset Type**: Credit Risk/Loan Default Prediction
- **Features**: 15 key features including demographic, financial, and loan-specific variables
- **Target Variable**: Binary classification (0 = No Default/Low Risk, 1 = Default/High Risk)
- **Use Case**: Financial risk assessment and loan approval decision support

### Data Preprocessing:
The dataset underwent standard preprocessing steps including:
- Handling missing values
- Feature encoding for categorical variables
- Data normalization/scaling where necessary
- Train-test split for model validation

## Features

- **Interactive Web Interface**: User-friendly Streamlit interface with sliders for input parameters
- **Real-time Predictions**: Instant credit risk assessment based on input data
- **Comprehensive Feature Analysis**: Evaluates 15 different features including:
  - Personal demographics (age, income, home ownership)
  - Employment information (employment length)
  - Loan details (amount, grade, interest rate, purpose)
  - Credit history (default history, credit length)

## Prerequisites

Before running the application, ensure you have the following installed:

```bash
Python 3.7+
streamlit
pickle
numpy
scikit-learn
```

## Installation

1. Clone or download the project files
2. Install the required packages:
   ```bash
   pip install streamlit numpy scikit-learn
   ```
3. Ensure you have the trained model file (`model_selection.pkl`) in the correct path
4. **Note**: The original Kaggle dataset is not included in this repository due to size constraints. You can download the dataset from Kaggle if you want to retrain the model.

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run model.py
   ```

2. Open your web browser and navigate to the displayed local URL (typically `http://localhost:8501`)

3. Use the sliders to input the following information:
   - **Person Age**: Age of the applicant (15-100 years)
   - **Person Income**: Annual income ($25,000-$100,000)
   - **Person Home Ownership**: Home ownership status (0-1)
   - **Person Employment Length**: Length of employment (15-100)
   - **Loan Grade**: Credit grade (282-1080)
   - **Loan Amount**: Requested loan amount ($15,000-$200,000)
   - **Loan Interest Rate**: Interest rate (9.99%-24%)
   - **Loan Percent Income**: Loan amount as percentage of income (9.99%-24%)
   - **CB Person Default on File**: Previous default history (2-30)
   - **CB Person Credit History Length**: Length of credit history (2-30 years)
   - **Loan Intent Categories**: Purpose of loan (Education, Home Improvement, Medical, Personal, Venture)

4. Click the "Predict" button to get the credit risk assessment

## Model Information

- **Algorithm**: Decision Tree Classifier
- **Library**: scikit-learn 1.6.1
- **Features**: 15 input features
- **Output**: Binary classification (0 = Low Risk, 1 = High Risk)
- **Training Data**: Kaggle Credit Risk Dataset
- **Model Performance**: Trained and validated on thousands of real-world loan records

### Model Development Process:
1. **Data Collection**: Downloaded credit risk dataset from Kaggle
2. **Data Exploration**: Analyzed feature distributions and correlations
3. **Data Preprocessing**: Cleaned and prepared data for training
4. **Model Training**: Used Decision Tree Classifier with optimized hyperparameters
5. **Model Validation**: Evaluated performance using cross-validation
6. **Model Serialization**: Saved trained model using pickle for deployment

## Data Source

### Kaggle Dataset
This project utilizes a credit risk dataset obtained from Kaggle, a popular platform for machine learning datasets and competitions. The dataset provides real-world financial data that has been anonymized and processed for machine learning applications.

**Why Kaggle?**
- High-quality, curated datasets
- Community-validated data sources
- Comprehensive feature sets
- Real-world applicability
- Extensive documentation and community support

### Dataset Characteristics:
- **Size**: Multiple thousands of loan records
- **Features**: 15 carefully selected predictive features
- **Quality**: Clean, preprocessed data suitable for machine learning
- **Relevance**: Current financial market conditions and lending practices
- **Diversity**: Represents various loan types, demographics, and risk profiles

## File Structure

```
credit_risk_system/
├── model.py                    # Main Streamlit application
├── model_selection.pkl         # Pre-trained machine learning model
├── dataset/                    # Kaggle dataset files (not included in repo)
│   ├── train.csv              # Training data
│   └── test.csv               # Testing data
└── README.md                  # Project documentation
```

## Model Features

The system evaluates the following features:

1. **person_age**: Age of the loan applicant
2. **person_income**: Annual income of the applicant
3. **person_home_ownership**: Home ownership status
4. **person_emp_length**: Employment length
5. **loan_grade**: Credit grade assigned to the loan
6. **loan_amnt**: Loan amount requested
7. **loan_int_rate**: Interest rate of the loan
8. **loan_percent_income**: Loan amount as percentage of income
9. **cb_person_default_on_file**: Whether person has defaults on file
10. **cb_person_cred_hist_length**: Length of credit history
11. **loan_intent_EDUCATION**: Education loan indicator
12. **loan_intent_HOMEIMPROVEMENT**: Home improvement loan indicator
13. **loan_intent_MEDICAL**: Medical loan indicator
14. **loan_intent_PERSONAL**: Personal loan indicator
15. **loan_intent_VENTURE**: Business venture loan indicator

## Important Notes

- **Model Path**: Update the model file path in `model.py` to match your local directory structure
- **Data Validation**: The current implementation uses slider inputs with predefined ranges
- **Prediction Output**: The system outputs a binary prediction (0 or 1) representing risk level

## Potential Improvements

- Add data validation and error handling
- Implement feature scaling/normalization
- Add confidence scores for predictions
- Include model performance metrics
- Add data visualization for better insights
- Implement database connectivity for storing predictions
- Add user authentication and session management

## Troubleshooting

**Common Issues:**

1. **File Not Found Error**: Ensure the `model_selection.pkl` file path is correct
2. **Import Errors**: Install all required packages using pip
3. **Model Loading Issues**: Verify the pickle file is not corrupted and was created with a compatible scikit-learn version

## Contributing

Feel free to contribute to this project by:
- Improving the user interface
- Adding new features
- Optimizing the model
- Adding comprehensive testing
- Improving documentation
- Working with additional Kaggle datasets for model enhancement
- Implementing ensemble methods or other ML algorithms

### Working with the Dataset:
If you want to retrain the model or experiment with different algorithms:
1. Download the original dataset from Kaggle
2. Create a `dataset/` folder in your project directory
3. Place the CSV files in the dataset folder
4. Modify the training script to use your preferred ML algorithm
5. Retrain and save the new model

## Acknowledgments

- **Kaggle Community**: For providing high-quality datasets and fostering machine learning research
- **Dataset Contributors**: Original data providers who made this analysis possible
- **Open Source Libraries**: scikit-learn, Streamlit, NumPy, and Pandas communities

## License

This project is open source and available under the MIT License.

## Support

For questions or issues, please check the troubleshooting section or create an issue in the project repository.
