'''# Assignment - 4
# Question - 1

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Load Diabetes Dataset
data = load_diabetes()
X = data.data
y = data.target

# Convert to DataFrame for clarity
columns = data.feature_names
df = pd.DataFrame(X, columns=columns)
df['target'] = y

# Feature Exploration
print("Dataset Head:\n", df.head())
print("\nFeature Correlation with Target:")
print(df.corr()['target'].sort_values(ascending=False))

"""
Explanation:
First of all, we consider the target correlation of the variables separately. A greater correlation can indicate that this feature lends itself well to diabetes progression prediction.

It would be much easier to deal with diabetic cases due to the fact that patients have different kinds of characteristics.
"""

# Split the data for initial analysis with just bmi and s5
X_baseline = df[['bmi', 's5']]
X_train, X_test, y_train, y_test = train_test_split(X_baseline, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Baseline model using only 'bmi' and 's5'
model_baseline = LinearRegression()
model_baseline.fit(X_train_scaled, y_train)

# Predictions and Metrics for baseline
y_pred_baseline = model_baseline.predict(X_test_scaled)
mse_baseline = mean_squared_error(y_test, y_pred_baseline)
r2_baseline = r2_score(y_test, y_pred_baseline)

print("\nBaseline Model Performance (using only bmi and s5):")
print(f"Mean Squared Error: {mse_baseline}")
print(f"R2 Score: {r2_baseline}")

# Add additional feature: Let's choose 'bp' (Blood Pressure) based on correlation analysis
X_expanded = df[['bmi', 's5', 'bp']]
X_train_exp, X_test_exp, y_train, y_test = train_test_split(X_expanded, y, test_size=0.2, random_state=42)

# Standardize the features
X_train_exp_scaled = scaler.fit_transform(X_train_exp)
X_test_exp_scaled = scaler.transform(X_test_exp)

# Expanded model with an additional variable
model_expanded = LinearRegression()
model_expanded.fit(X_train_exp_scaled, y_train)

# Predictions and Metrics for expanded model
y_pred_expanded = model_expanded.predict(X_test_exp_scaled)
mse_expanded = mean_squared_error(y_test, y_pred_expanded)
r2_expanded = r2_score(y_test, y_pred_expanded)

print("\nExpanded Model Performance (adding 'bp'):")
print(f"Mean Squared Error: {mse_expanded}")
print(f"R2 Score: {r2_expanded}")

"""
Findings for Step b:
Inclusion of 'bp' variable improves R2 value and decreases the MSE. This
seems to suggest that 'bp' is an important predictor when used along with 'bmi' and 's5'.
"""

# Additional Investigation: Adding all features to see if it further improves
X_all = df.drop('target', axis=1)
X_train_all, X_test_all, y_train, y_test = train_test_split(X_all, y, test_size=0.2, random_state=42)

# Standardize all features
X_train_all_scaled = scaler.fit_transform(X_train_all)
X_test_all_scaled = scaler.transform(X_test_all)

# Model using all features
model_all = LinearRegression()
model_all.fit(X_train_all_scaled, y_train)

# Predictions and Metrics for the model with all features
y_pred_all = model_all.predict(X_test_all_scaled)
mse_all = mean_squared_error(y_test, y_pred_all)
r2_all = r2_score(y_test, y_pred_all)

print("\nFull Model Performance (using all features):")
print(f"Mean Squared Error: {mse_all}")
print(f"R2 Score: {r2_all}")

"""
Findings for Step d:
The inclusion of additional variables certainly enhances the efficacy of the model, nonetheless the enhancement tends to decrease as the features increase in addition. 
Also, we may face overfitting due to the fact that we at times include a lot of features. The underlying concept here is that there is always a trade-off between the complexity of the model and the ability of it to perform.
"""

# In summary, ‘bp’ was the most significant additional predictor, but gains derived from the addition of all the variables are nil.
# Question - 2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 0) Read the dataset
file_path = '50_Startups.csv'
data = pd.read_csv(file_path)

print("Dataset Head:\n", data.head())

"""
Explanation:
The data is read with the help of pandas. In order to know the columns and the data is being read correctly, we need to look at the first few records.
"""

# 1) Identify variables in the dataset
print("\nDataset Columns:", data.columns)
print("\nDataset Summary:")
print(data.describe())

"""
Explanation:
The data comprises common variables like ‘R&D Spend’, ‘Administration’, ‘Marketing Spend’, ‘State’, and ‘Profit’ among others. 
The ‘Profit’ will serve as dependent variable, while other numeric variables could be seen as potential independent variables.
"""

# 2) Investigate correlation between variables
# Plot the correlation matrix
correlation_matrix = data.corr()
print("\nCorrelation Matrix:\n", correlation_matrix)

# Plot a heatmap for better visualization
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

"""
Explanation:
The correlation matrix allows us to assess which variables are the most significantly associated with ‘Profit’. A high correlation coefficient infers a higher degree of linearity between it and the target variable.
"""

# 3) Choose appropriate variables to predict profit
# Based on the correlation, we'll choose variables with high correlation with 'Profit'
# Let's see the correlation of each feature with Profit
profit_corr = correlation_matrix['Profit'].sort_values(ascending=False)
print("\nCorrelation with Profit:\n", profit_corr)

# Choosing 'R&D Spend' and 'Marketing Spend' because they show higher correlation with 'Profit'
selected_features = ['R&D Spend', 'Marketing Spend']

"""
Explanation:
The variable 'R&D Spend' exhibits the strongest correlation with the dependent variable 'Profit', followed by the correlation of 'Marketing Spend'. These two variables have been selected for the purpose of prediction as they exhibit a robust linear relationship with the dependent variable ‘Profit’.
"""

# 4) Plot explanatory variables against profit to confirm linear dependence
plt.figure(figsize=(14, 6))

# Scatter plot for 'R&D Spend' vs 'Profit'
plt.subplot(1, 2, 1)
sns.scatterplot(x='R&D Spend', y='Profit', data=data)
plt.title('R&D Spend vs Profit')
plt.xlabel('R&D Spend')
plt.ylabel('Profit')

# Scatter plot for 'Marketing Spend' vs 'Profit'
plt.subplot(1, 2, 2)
sns.scatterplot(x='Marketing Spend', y='Profit', data=data)
plt.title('Marketing Spend vs Profit')
plt.xlabel('Marketing Spend')
plt.ylabel('Profit')

plt.tight_layout()
plt.show()

"""
Explanation:
The measures of expenditure on 'R&D Spend' and 'Marketing Spend' are both found to have a correlation that can almost be described as straight line to 'Profit' thus enable use of them in several predictors.
"""

# 5) Form training and testing data (80/20 split)
X = data[selected_features]
y = data['Profit']

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6) Train a linear regression model with training data
model = LinearRegression()
model.fit(X_train, y_train)

# 7) Compute RMSE and R2 values for training and testing data
# Predictions for training and testing sets
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# Calculate metrics
train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

print("\nModel Performance:")
print(f"Training RMSE: {train_rmse}")
print(f"Training R2: {train_r2}")
print(f"Testing RMSE: {test_rmse}")
print(f"Testing R2: {test_r2}")

"""
Findings:
The evaluation of the model is carried out using the measure known as RMSE (Root Mean Squared Error) and R2 (Coefficient of Determination). A good model would be one with a high R2 value and a low RMSE value. This shows that there is no overfitting in the model since the training and testing results are in agreement.
"""

# Final remarks about the model
coefficients = pd.DataFrame({'Feature': selected_features, 'Coefficient': model.coef_})
print("\nModel Coefficients:\n", coefficients)

# question - 3
# Required Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# 1) Read the data into pandas dataframe
file_path = 'Auto.csv'
data = pd.read_csv(file_path)

# Display the first few rows to understand the data structure
print("Dataset Head:\n", data.head())
print("\nDataset Info:")
print(data.info())

"""
Explanation:
We read the dataset using pandas to understand the structure. We check the column names and data types to ensure
we can properly set up the regression model. Common columns in 'Auto.csv' are 'mpg', 'displacement', 'horsepower',
'weight', 'acceleration', etc.
"""

# Check for missing values and handle them
data = data.replace('?', np.nan)
data = data.dropna()  # Drop rows with missing values
data['horsepower'] = data['horsepower'].astype(float)  # Convert horsepower to float for numerical analysis

# 2) Setup multiple regression X and y to predict 'mpg'
# Exclude 'mpg', 'name', and 'origin' from the predictors
X = data.drop(['mpg', 'name', 'origin'], axis=1)
y = data['mpg']

# 3) Split data into training and testing sets (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

"""
Explanation:
We standardized the features using StandardScaler to ensure that all predictors have a mean of 0 and standard deviation of 1.
This step is essential for Ridge and LASSO regression as they are sensitive to the scale of input data.
"""

# 4) Implement Ridge and LASSO Regression using several values for alpha
alphas = np.logspace(-3, 3, 100)  # Explore alpha values from 0.001 to 1000
ridge_r2_scores = []
lasso_r2_scores = []

for alpha in alphas:
    # Ridge Regression
    ridge = Ridge(alpha=alpha)
    ridge.fit(X_train_scaled, y_train)
    ridge_r2_scores.append(ridge.score(X_test_scaled, y_test))

    # LASSO Regression
    lasso = Lasso(alpha=alpha, max_iter=10000)
    lasso.fit(X_train_scaled, y_train)
    lasso_r2_scores.append(lasso.score(X_test_scaled, y_test))

"""
Explanation:
We use a range of `alpha` values (from 0.001 to 1000) to evaluate the performance of both Ridge and LASSO regression.
The models are fitted on training data, and \( R^2 \) scores are computed on testing data.
"""

# 6) Plot the R2 scores for both regressors as functions of alpha
plt.figure(figsize=(12, 6))
plt.plot(alphas, ridge_r2_scores, label='Ridge R2 Score', marker='o')
plt.plot(alphas, lasso_r2_scores, label='LASSO R2 Score', marker='x')
plt.xscale('log')
plt.xlabel('Alpha (log scale)')
plt.ylabel('R2 Score')
plt.title('R2 Score vs Alpha for Ridge and LASSO Regression')
plt.legend()
plt.grid(True)
plt.show()

# 7) Identify the optimal alpha value
best_alpha_ridge = alphas[np.argmax(ridge_r2_scores)]
best_alpha_lasso = alphas[np.argmax(lasso_r2_scores)]

print(f"Optimal Alpha for Ridge: {best_alpha_ridge}")
print(f"Optimal Alpha for LASSO: {best_alpha_lasso}")
print(f"Best Ridge R2 Score: {max(ridge_r2_scores)}")
print(f"Best LASSO R2 Score: {max(lasso_r2_scores)}")

"""
Findings:
1. The plots of \( R^2 \) scores vs. alpha for Ridge and LASSO regressions help identify the alpha value that
   maximizes the \( R^2 \) score.
2. An optimal alpha is chosen where the model performs the best (highest \( R^2 \) score) on the testing data.
3. Ridge tends to perform better when multicollinearity is present, whereas LASSO can perform feature selection by
   shrinking some coefficients to zero.
"""
'''
# Assignment - 5
# Question - 1
'''import pandas as pd

file_path = 'C:/Users/Vidhi Soni/PycharmProjects/vidhivisrepo/bank.csv'

df = pd.read_csv(file_path, delimiter=';')

print("First few rows of the DataFrame:")
print(df.head())

print("\nColumn Names and Variable Types:")
print(df.dtypes)'''
# Question - 2
'''import pandas as pd

# Load your CSV file
file_path = 'C:/Users/Vidhi Soni/PycharmProjects/vidhivisrepo/bank.csv'

df = pd.read_csv(file_path, delimiter=';')

# Create a second DataFrame with the specified columns
df2 = df[['y', 'job', 'marital', 'default', 'housing', 'poutcome']]

# Display the first few rows of the new DataFrame
print(df2.head())'''
# Question - 3
'''import pandas as pd

file_path = 'C:/Users/Vidhi Soni/PycharmProjects/vidhivisrepo/bank.csv'

df = pd.read_csv(file_path, delimiter=';')
print(df.columns)
df2 = df[['y', 'job', 'marital', 'default', 'housing', 'poutcome']]
print(df2.head())'''
'''# Question - 4
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'C:/Users/Vidhi Soni/PycharmProjects/vidhivisrepo/bank.csv'
df = pd.read_csv(file_path, delimiter=';')
df2 = df[['y', 'job', 'marital', 'default', 'housing', 'poutcome']]
df3 = pd.get_dummies(df2, columns=['job', 'marital', 'default', 'housing', 'poutcome'])
df3 = df3.apply(pd.to_numeric, errors='coerce')
correlation_matrix = df3.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

plt.title('Correlation Heatmap of Variables in df3')
plt.show()
# Question - 5

y = df3['y']
X = df3.drop(columns=['y'])
print("Explanatory variables (X):")
print(X.head())
print("\nTarget variable (y):")
print(y.head())
# Question - 6
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

print(f"Training set size: X_train: {X_train.shape}, y_train: {y_train.shape}")
print(f"Test set size: X_test: {X_test.shape}, y_test: {y_test.shape}")
# Question - 7

print(f"Number of NaN values in 'y': {y.isna().sum()}")

df3_cleaned = df3.dropna(subset=['y'])

print(f"Shape of cleaned dataframe: {df3_cleaned.shape}")

X_cleaned = df3_cleaned.drop(columns=['y'])
y_cleaned = df3_cleaned['y']

if len(X_cleaned) > 0:

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X_cleaned, y_cleaned, test_size=0.25, random_state=42)


    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    from sklearn.metrics import accuracy_score, classification_report
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

else:
    print("After removing rows with NaN values in 'y', the dataset is empty. Please check the data.")
# Assignment - 8

from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

conf_matrix = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(conf_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['No', 'Yes'], yticklabels=['No', 'Yes'])
plt.title("Confusion Matrix")
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()
# Question - 9
# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier  # Import KNN classifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming df3 is the dataframe after applying pd.get_dummies

# Define X (explanatory variables) and y (target variable)
X = df3.drop(columns=['y'])  # All columns except 'y'
y = df3['y']  # The 'y' column is the target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Initialize the KNN model with k=3
knn_model = KNeighborsClassifier(n_neighbors=3)

# Train the KNN model with the training data
knn_model.fit(X_train, y_train)

# Make predictions on the test set using knn_model
y_pred_knn = knn_model.predict(X_test)

# Compute the accuracy score for KNN
accuracy_knn = accuracy_score(y_test, y_pred_knn)
print(f"Accuracy (KNN with k=3): {accuracy_knn * 100:.2f}%")

# Print the classification report for KNN
print("\nClassification Report (KNN with k=3):")
print(classification_report(y_test, y_pred_knn))

# Compute the confusion matrix for KNN
conf_matrix_knn = confusion_matrix(y_test, y_pred_knn)

# Print the confusion matrix
print("\nConfusion Matrix (KNN with k=3):")
print(conf_matrix_knn)

# Plot the confusion matrix for KNN as a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix_knn, annot=True, fmt='d', cmap='Blues', xticklabels=['No', 'Yes'], yticklabels=['No', 'Yes'])
plt.title("Confusion Matrix (KNN with k=3)")
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

# Question - 10

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming X and y are already defined from your dataset

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 1. Logistic Regression Model
log_reg_model = LogisticRegression(max_iter=1000)
log_reg_model.fit(X_train, y_train)
y_pred_logreg = log_reg_model.predict(X_test)

# Accuracy and Confusion Matrix for Logistic Regression
accuracy_logreg = accuracy_score(y_test, y_pred_logreg)
print(f"Accuracy (Logistic Regression): {accuracy_logreg * 100:.2f}%")
print("\nClassification Report (Logistic Regression):")
print(classification_report(y_test, y_pred_logreg))
conf_matrix_logreg = confusion_matrix(y_test, y_pred_logreg)
print("\nConfusion Matrix (Logistic Regression):")
print(conf_matrix_logreg)

# Plot Confusion Matrix for Logistic Regression
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix_logreg, annot=True, fmt='d', cmap='Blues', xticklabels=['No', 'Yes'], yticklabels=['No', 'Yes'])
plt.title("Confusion Matrix (Logistic Regression)")
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

""" Findings from Logistic Regression:
- The logistic regression model has an accuracy score (accuracy_logreg * 100).
- The confusion matrix shows the number of correct/incorrect predictions.
- The classification report includes precision, recall, and f1-score metrics.
- The heatmap visualizes the confusion matrix.
"""

# 2. K-Nearest Neighbors Model (k=3)
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train, y_train)
y_pred_knn = knn_model.predict(X_test)

# Accuracy and Confusion Matrix for KNN
accuracy_knn = accuracy_score(y_test, y_pred_knn)
print(f"\nAccuracy (KNN with k=3): {accuracy_knn * 100:.2f}%")
print("\nClassification Report (KNN with k=3):")
print(classification_report(y_test, y_pred_knn))
conf_matrix_knn = confusion_matrix(y_test, y_pred_knn)
print("\nConfusion Matrix (KNN with k=3):")
print(conf_matrix_knn)

# Plot Confusion Matrix for KNN
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix_knn, annot=True, fmt='d', cmap='Blues', xticklabels=['No', 'Yes'], yticklabels=['No', 'Yes'])
plt.title("Confusion Matrix (KNN with k=3)")
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

""" Findings from KNN:
- The KNN model (with k=3) has an accuracy score (accuracy_knn * 100).
- The confusion matrix shows the number of correct/incorrect predictions.
- The classification report includes precision, recall, and f1-score metrics.
- The heatmap visualizes the confusion matrix.
"""

# Compare accuracies
print("\n--- Comparison of Models ---")
print(f"Accuracy (Logistic Regression): {accuracy_logreg * 100:.2f}%")
print(f"Accuracy (KNN with k=3): {accuracy_knn * 100:.2f}%")

""" Comparison of Logistic Regression and KNN (k=3):
- Compare the accuracy of both models. 
- The confusion matrices can help in understanding how each model is performing in terms of false positives, false negatives, true positives, and true negatives.
- Based on the accuracy, you can choose which model performs better for your dataset.
"""
'''
# Assignment - 6
# Question - 1
'''import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report

# Step 0: Reading the uploaded CSV file into a Pandas DataFrame
file_path = 'C:/Users/Vidhi Soni/PycharmProjects/vidhivisrepo/data_banknote_authentication.csv'
data = pd.read_csv(file_path)

# Step 1: Define target variable `y` and feature variables `X`
X = data.drop(columns=['class'])
y = data['class']

# Step 2: Split data into training and testing sets with an 80/20 split and random_state=20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=20)

# Step 3: Train a support vector classifier with a linear kernel
svc_linear = SVC(kernel='linear', random_state=20)
svc_linear.fit(X_train, y_train)

# Step 4: Predict on the testing data and compute the confusion matrix and classification report
y_pred_linear = svc_linear.predict(X_test)
conf_matrix_linear = confusion_matrix(y_test, y_pred_linear)
class_report_linear = classification_report(y_test, y_pred_linear)

# Step 5: Train a support vector classifier with an RBF kernel
svc_rbf = SVC(kernel='rbf', random_state=20)
svc_rbf.fit(X_train, y_train)

# Step 6: Predict on the testing data and compute the confusion matrix and classification report
y_pred_rbf = svc_rbf.predict(X_test)
conf_matrix_rbf = confusion_matrix(y_test, y_pred_rbf)
class_report_rbf = classification_report(y_test, y_pred_rbf)

print("Linear Kernel SVM:")
print("Confusion Matrix:\n", conf_matrix_linear)
print("Classification Report:\n", class_report_linear)

print("\nRBF Kernel SVM:")
print("Confusion Matrix:\n", conf_matrix_rbf)
print("Classification Report:\n", class_report_rbf)
#  Compare the two SVM models in your own words
""" The best model in this case is RBF Kernel SVM, which has perfectly achieved
  all metrics of accuracy, precision, recall, as well as F1-score making it a
  highly proficient model for this dataset. The Linear Kernel SVM, contrary to
  having slightly inferior performance than that of RBF, produces results that
  are quite strong. Choosing between the two will depend on the linear separability
  of the data and computational efficiency, considering that one model may be more
  efficient than the other."""
'''
# Question - 2
'''import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

# Load the dataset
file_path = 'C:/Users/Vidhi Soni/PycharmProjects/vidhivisrepo/weight-height.csv'
data = pd.read_csv(file_path)

# Convert height to centimeters and weight to kilograms
data['Height'] = data['Height'] * 2.54  # inches to cm
data['Weight'] = data['Weight'] * 0.453592  # pounds to kg

# Define feature and target variables
X = data[['Height']]  # Feature variable (in cm)
y = data['Weight']    # Target variable (in kg)

# Split data into training and testing sets (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the data
# Normalization (Min-Max scaling)
min_max_scaler = MinMaxScaler()
X_train_norm = min_max_scaler.fit_transform(X_train)
X_test_norm = min_max_scaler.transform(X_test)

# Standardization (Z-score scaling)
standard_scaler = StandardScaler()
X_train_std = standard_scaler.fit_transform(X_train)
X_test_std = standard_scaler.transform(X_test)

# Function to fit KNN and compute R^2 score
def knn_r2_score(X_train, X_test, y_train, y_test, k=5):
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    return r2_score(y_test, y_pred)

# Evaluate KNN regression with different scalings
r2_unscaled = knn_r2_score(X_train, X_test, y_train, y_test)
r2_normalized = knn_r2_score(X_train_norm, X_test_norm, y_train, y_test)
r2_standardized = knn_r2_score(X_train_std, X_test_std, y_train, y_test)

# Print R^2 values for comparison
print(f"R^2 without scaling: {r2_unscaled}")
print(f"R^2 with normalization: {r2_normalized}")
print(f"R^2 with standardization: {r2_standardized}")'''
# Question - 3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report

# Load the dataset
file_path = 'C:/Users/Vidhi Soni/PycharmProjects/vidhivisrepo/suv.csv'
data = pd.read_csv(file_path)

# Select features and target variable
X = data[['Age', 'EstimatedSalary']]
y = data['Purchased']

# Split data into training and testing sets (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features using standard scaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Function to train Decision Tree Classifier and evaluate performance
def evaluate_decision_tree(criterion, X_train, X_test, y_train, y_test):
    dt = DecisionTreeClassifier(criterion=criterion, random_state=42)
    dt.fit(X_train, y_train)
    y_pred = dt.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    cr = classification_report(y_test, y_pred)
    return cm, cr

# Evaluate with entropy criterion
print("Decision Tree with Entropy Criterion:")
cm_entropy, cr_entropy = evaluate_decision_tree('entropy', X_train_scaled, X_test_scaled, y_train, y_test)
print("Confusion Matrix:\n", cm_entropy)
print("Classification Report:\n", cr_entropy)

# Evaluate with gini criterion
print("Decision Tree with Gini Criterion:")
cm_gini, cr_gini = evaluate_decision_tree('gini', X_train_scaled, X_test_scaled, y_train, y_test)
print("Confusion Matrix:\n", cm_gini)
print("Classification Report:\n", cr_gini)
# 7 - Discuss the performance of your models
"""Conclusions Regarding Performance: 
The final results show that both the models, using the Entropy and Gini indices, 
achieved an accuracy of 84 per cent. The performance of the model is further 
highlighted by the strong precision and recall achieved by class 0 in identifying 
the majority class. Class 1, the minority class, is predicted poorly, particularly 
recall-wise, and so it might adapt some measures to address the class imbalance 
    (for instance, using class weights or oversampling)."""



