
# Customer Churn Prediction Model

𝗣𝗿𝗼𝗷𝗲𝗰𝘁 𝗢𝘃𝗲𝗿𝘃𝗶𝗲𝘄

This project aims to predict customer churn in the banking sector using a machine learning approach. The model is trained on a dataset containing various customer attributes. The objective is to accurately classify customers as either likely to churn or not, allowing the bank to take proactive measures.

𝗣𝗿𝗼𝗷𝗲𝗰𝘁 𝗦𝘁𝗿𝘂𝗰𝘁𝘂𝗿𝗲

Customer_Churn_Prediction.ipynb: Jupyter notebook with comprehensive data exploration, preprocessing, model training, evaluation, and selection processes.
app.py: Streamlit web application script enabling users to input customer data and predict the likelihood of churn using the trained model.
customer_churn_data.csv: The dataset used for training and evaluating the models.
best_model.pkl: The saved machine learning model (using joblib) that provides predictions in the Streamlit app.

Tasks Performed
Data Exploration and Statistical Analysis:

Explored the dataset, addressed missing values, and calculated statistical measures.
Algorithm Selection:

Selected and applied various machine learning algorithms, including Logistic Regression, K-Nearest Neighbors (KNN), Decision Tree, Random Forest, Gradient Boosting, and XGBoost.
Data Preprocessing:

Encoded categorical variables, normalized numerical features, and split the dataset into training and testing sets.
Model Training:

Trained multiple models and evaluated their performance based on accuracy, precision, recall, and F1 score.
Model Evaluation:

Compared models using precision, recall, and F1 score. Chose the best-performing model based on a balance of these metrics.
Model Saving:

Saved the best-performing model using joblib for future deployment.
Streamlit Web Application:

Developed a Streamlit app (app.py) allowing users to predict customer churn based on input features.
Deployment on GitHub:

Uploaded the Jupyter notebook, trained model, Streamlit app, and dataset to GitHub for public access.
Conclusion
This project showcases a robust approach to predicting customer churn using machine learning. The Streamlit app provides a user-friendly interface for predicting churn likelihood based on customer data. The project includes various visualizations such as pie charts, bar plots, and box plots to help understand the data and model performance.
