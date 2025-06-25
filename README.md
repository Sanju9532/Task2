Introduction:
          In the Titanic dataset, Performing several preprocessing steps, including imputing null values with the median and mode, checking whether all columns are in the correct data types, 
examining correlations, identifying outliers, conducting statistical analysis, and applying standard scaling. Also perform Principal Component Analysis (PCA) and visualize outliers using 
box plots and histograms. Next, we will connect Python with MySQL to identify trends and patterns, and finally, visualize the results of SQL queries in Streamlit.

Handling Missing Data: 
        In three columns, there is missing data. The "Cabin" column has more than 50% missing values, so I dropped this column. The "Age" column has some missing values, which were imputed 
using the median. The "Embarked" column has very few missing values, which were imputed using the mode.

Encoding: 
        There are some categorical columns, and I performed encoding for only two of them. For the 'Sex' column, I used One-Hot Encoding, and for the 'Embarked' column, I applied One-Hot 
Encoding to create separate binary columns for each category.

Standardizing and Visualizing Outliers:
        Except for the target variable, "Name," and the "Ticket" column, I standardized the other columns. There are no outliers in the target column, but the "Age" column and some other 
columns contain many outliers. If I were to remove these outliers, nearly half of the data would be lost, so I decided not to remove them.

Creating MySQL queries and visualizing the results in Streamlit:
		Connecting Python with MySQL to create a database named 'Titanic2' and a table also named 'Titanic2', and then inserting the values from the DataFrame into the MySQL table. Connecting 
MySQL to Streamlit to visualize the query results.

Conclusion: 
        This analysis of the Titanic dataset involved preprocessing steps such as dropping the 'Cabin' column due to missing data and imputing missing values for 'Age' and 'Embarked' 
Categorical variables were transformed using one-hot encoding, and numerical features were standardized, except for outliers in the 'Age' column, which were retained to maintain data 
integrity. Using MySQL and Streamlit, an interactive querying and visualization system was built to explore the dataset dynamically.
