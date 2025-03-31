# Crop Yield Prediction

## Project Overview
This project aims to predict crop yield based on environmental and agricultural factors such as temperature, rainfall, irrigation and fertilizer usage, etc.

---

## ✅ Current Progress

### **1. Data Analysis**
- Identified a **positive correlation** between yield and:
  - Temperature
  - Rainfall
  - Irrigation used
  - Fertilizer used
- However, extreme values of temperature and rainfall may negatively affect yield. (This did not reflect in the Linear Regression model)

### **2. Feature Engineering**
- Added interaction terms:
  - **Temperature × Rainfall** (captures combined effects)
  - **Irrigation Used AND Fertilizer Used** (captures agricultural intervention effects)

### **3. Model Development**
- Trained the following models:
  - **Linear Regression** (highest accuracy but poor generalization for non-linear effects)
  - **Random Forest** (captures non-linearity but needs testing)
  - **LinearSVR** (needs testing)
  - **Gradient Boosting** (needs testing)

### **4. Testing and Evaluation**
- **Linear Regression performed poorly** in modeling non-linear effects such as:
  - Crop-specific responses
  - Optimal temperature and rainfall ranges
  - Effects of new interaction features
- Other models (**Random Forest, LinearSVR, Gradient Boosting**) **have not been tested yet**.

---

## 📌 Work to be Done

### **🔬 1. Test Alternative Models**
- Evaluate **Random Forest, LinearSVR, and Gradient Boosting** on:
  - **Root Mean Squared Error (RMSE)**
  - **Mean Absolute Error (MAE)**
  - **R² Score**
- Compare against Linear Regression and identify the best-performing model.

### **📊 2. Improve Model Performance**
- **Hyperparameter tuning** for tree-based models (Random Forest, Gradient Boosting) to optimize performance.
- Feature Engineering: Consider polynomial terms: `Temperature^2` and Rainfall^2
- Experiment with **Polynomial Regression (degree=2)** to capture quadratic relationships.
- Try **XGBoost**, which often performs well in structured data problems.
- Consider using **Neural Networks** for deeper feature interactions.

### **🚀 3. Final Deployment**
- Select the best-performing model and deploy it using **Flask/FastAPI**.
- Integrate a **frontend UI** for users to input crop parameters and receive yield predictions.
- Optimize API for real-time predictions.

---


---

### **🔎 Next Steps**
- 📌 **Test remaining models** (Random Forest, LinearSVR, Gradient Boosting)
- 📌 **Fine-tune hyperparameters** for better performance
- 📌 **Deploy best model** using Flask or FastAPI

**Stay tuned for updates!**
