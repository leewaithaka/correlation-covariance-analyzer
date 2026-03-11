# 📊 Correlation & Covariance Analyzer

## Project Overview
This project analyzes relationships between variables using **covariance and correlation matrices** in Python.

It demonstrates important statistical concepts used in **data analysis, machine learning, and statistical modeling**.

The project reads a dataset, calculates statistical relationships between variables, and visualizes them using scatter plots.

---

## 🛠 Tools & Technologies

- Python
- pandas
- matplotlib

---

## 📂 Project Structure

```
correlation-covariance-analyzer
│
├── analyzer.py
├── visualize.py
├── dataset.csv
└── README.md
```

---

## 📈 Features

- Calculate **covariance matrix**
- Calculate **correlation matrix**
- Analyze relationships between variables
- Visualize variable relationships using **scatter matrix plots**

---

## 📊 Example Dataset

The dataset contains the following variables:

| Variable | Description |
|---------|-------------|
| Hours_Studied | Number of hours spent studying |
| Sleep_Hours | Average sleep hours |
| Exam_Score | Student exam score |

Example data:

```
Hours_Studied,Sleep_Hours,Exam_Score
2,6,50
3,7,55
4,6,60
5,7,65
6,8,70
7,7,75
8,8,80
9,7,85
10,8,90
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

```
git clone https://github.com/leewaithaka/correlation-covariance-analyzer.git
```

### 2️⃣ Navigate to the project folder

```
cd correlation-covariance-analyzer
```

### 3️⃣ Install required libraries

```
pip install pandas matplotlib
```

### 4️⃣ Run the analyzer

```
python analyzer.py
```

### 5️⃣ Generate visualization

```
python visualize.py
```

---

## 📉 Statistical Concepts Used

### Covariance

Covariance measures how two variables change together.

Cov(X,Y) = Σ((xi - x̄)(yi - ȳ)) / n

Positive covariance → variables increase together  
Negative covariance → one increases while the other decreases  

---

### Correlation

Correlation measures the **strength and direction of a relationship between variables**.

r = Cov(X,Y) / (σx σy)

Correlation values range between:

+1 → strong positive relationship  
0 → no relationship  
-1 → strong negative relationship  

---

## 📷 Visualization Output

The project generates a **scatter matrix** to show relationships between variables.

After running `visualize.py`, the following plot will be generated:

![Scatter Matrix](scatter_matrix.png)

---

## 🎓 Author

Lee Waithaka Komu
BSc Applied Statistics with Programming  

🔗 LinkedIn  
https://www.linkedin.com/in/lee-komu-674459283  

📧 Email  
leekomu4@gmail.com
