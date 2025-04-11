
---

## 📘 🔑 Important Terms in Linear Regression

Here are the key terms you should know — with simple definitions and examples!

---

### 1. **Dependent Variable (Y)**  
👉 The **output** we are trying to predict.  
🧠 Think: It's the "result".

**Example:** Marks, Price, Salary

---

### 2. **Independent Variable (X)**  
👉 The **input** or feature used to predict Y.  
🧠 Think: It's the "reason" or "cause".

**Example:** Study hours, House size, Experience

---

### 3. **Regression Line (Best Fit Line)**  
👉 The straight line that best represents the data.

Its equation is:  
\[
Y = aX + b
\]

Where:
- \( a \) = slope
- \( b \) = intercept

---

### 4. **Slope (a)**  
👉 Tells you **how much Y changes** when X increases by 1.  
🧠 Steep slope = big change; Flat slope = small change

**Example:**  
If slope = 10, then every extra hour of study = 10 more marks

---

### 5. **Intercept (b)**  
👉 The value of Y when X = 0 (where the line crosses the Y-axis)

**Example:**  
If intercept = 30, that’s the base value (like marks without studying)

---

### 6. **Prediction**  
👉 Using the regression line to find Y for a given X.

**Example:**  
If \( Y = 10X + 20 \), and X = 4,  
then prediction = \( Y = 10(4) + 20 = 60 \)

---

### 7. **Residual (Error)**  
👉 The difference between actual value and predicted value.

\[
\text{Residual} = Y_{\text{actual}} - Y_{\text{predicted}}
\]

**Example:**  
If predicted marks = 70 but actual = 65,  
then residual = -5

---

### 8. **Loss Function**  
👉 A formula that calculates the **total error**.  
In linear regression, we use:

\[
\text{Loss} = \sum (Y_i - (aX_i + b))^2
\]

We try to **minimize** this error.

---

### 9. **R-squared ( \( R^2 \) )**  
👉 A score that tells us how well the model fits the data.

- \( R^2 = 1 \): perfect prediction
- \( R^2 = 0 \): bad prediction

---

### 10. **Underfitting**  
👉 When your model is too simple and **misses** the trend.

---

### 11. **Overfitting**  
👉 When your model is too complex and **fits noise**, not the real trend.

---

## ✅ Summary Table

| Term           | Meaning                              | Example                      |
|----------------|---------------------------------------|-------------------------------|
| Y              | Output we predict                     | Marks, Salary                |
| X              | Input we use to predict               | Hours, Size, Experience      |
| Slope (a)      | Change in Y per 1 unit of X           | +10 marks per study hour     |
| Intercept (b)  | Y value when X = 0                    | Base score = 30              |
| Line           | Equation: \( Y = aX + b \)            | Predicts new values          |
| Residual       | Error = Actual Y - Predicted Y        | -5                           |
| Loss Function  | Total error of all predictions        | We want this minimum         |
| R-squared      | Accuracy of the model (0 to 1)        | Closer to 1 = better         |
| Underfitting   | Too simple, misses pattern            | Flat line                    |
| Overfitting    | Too complex, follows noise            | Wiggly line                  |

---
