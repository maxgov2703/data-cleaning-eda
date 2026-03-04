# Data Cleaning and Exploratory Data Analysis (EDA)

This project demonstrates the process of cleaning and analyzing raw data using Python.  
The dataset used is the Titanic passenger dataset.

The goal of the project is to simulate a real analytical workflow:  
working with messy data, detecting problems in the dataset, cleaning it, and performing exploratory data analysis.

---

## Dataset

The dataset contains information about Titanic passengers, including:

- Passenger class
- Name
- Gender
- Age
- Ticket price
- Cabin
- Port of embarkation
- Survival status

The raw dataset contains missing values and requires preprocessing before analysis.

---

## Project Goals

The main objectives of this project were:

- Identify missing values
- Detect duplicated records
- Explore the structure of the dataset
- Visualize important variables
- Prepare a cleaned dataset for further analysis

---

## Data Cleaning

During the cleaning stage the following steps were performed:

- Checked dataset structure using `df.info()`
- Identified missing values with `df.isnull()`
- Visualized missing data using a heatmap
- Handled missing values in the **Age** column by replacing them with the median
- Removed the **Cabin** column due to a large number of missing values
- Filled missing values in **Embarked**
- Checked for duplicated rows

A cleaned dataset was then saved for further use.

---

## Exploratory Data Analysis

Several visualizations were created to explore the dataset.

### Missing Values Heatmap
Shows the distribution of missing values across all columns.

### Ticket Price Distribution
Displays the distribution of ticket prices and highlights the presence of high-value outliers.

### Survival Rate by Gender
Shows that female passengers had a significantly higher survival rate compared to male passengers.

### Survival Rate by Passenger Class
Illustrates how survival probability varied by passenger class.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Key Takeaways

The analysis revealed several insights:

- Passenger **gender** had a strong impact on survival probability
- Passengers in **first class** had significantly higher survival rates
- Ticket prices showed a highly skewed distribution with several high-value outliers

This project demonstrates the fundamental workflow of preparing and exploring real-world data before performing deeper statistical analysis or building predictive models.
