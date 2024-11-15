# Assignment - 4
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
