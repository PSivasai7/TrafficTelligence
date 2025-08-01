
# TrafficTelligence 🚦
### Advanced Traffic Volume Estimation with Machine Learning

TrafficTelligence is a predictive system designed to estimate and forecast traffic volumes using machine learning. By analyzing historical traffic data, weather patterns, and other external factors, the system provides actionable insights for dynamic traffic control, urban development planning, and commuter guidance.

---

## 🚀 Features

- 📊 **Traffic Volume Forecasting** using ML models
- 🌦️ **Integration of Weather & Event Data**
- 🧠 **Pre-trained Models** with `model.pkl` and `encoder.pkl`
- 💡 **Real-time Traffic Estimation** and Decision Support
- 🛣️ **Scenarios**:
  - Dynamic Traffic Management
  - Urban Development Planning
  - Intelligent Commuter Navigation

---

## 🧠 Tech Stack

- **Python**, **Flask** (for API + Web Integration)
- **Pandas**, **Scikit-learn** (Data Processing & ML)
- **Joblib** or **Pickle** (for model serialization)
- **Jupyter Notebook** (for experimentation and training)
- **CSV** for data storage

---

## 🗂️ Project Structure

```
├── Flask/
│   ├── templates/
│   ├── app.py                  # Flask backend
│   ├── encoder.pkl             # Encoded categorical features
│   ├── model.pkl               # Trained ML model
|   ├── scale.pkl
|
├── Requirements.txt            # Project dependencies
├── traffic volume.ipynb        # Jupyter Notebook (Model Dev)
├── traffic volume.csv          # Dataset
├── Traffic volume estimation.docx
└── README.md                   # Project documentation
```

---

## 🧪 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/TrafficTelligence.git
cd TrafficTelligence
```

### 2. Install Dependencies

```bash
pip install -r Requirements.txt
```

### 3. Start Flask App

```bash
cd Flask
python app.py
```

Then open your browser and go to: `http://localhost:5000/`

---

## 📁 Data

- `traffic volume.csv`: Contains traffic data used for training and predictions.
- Make sure data is clean and formatted correctly before use.

---

## 📌 Scenarios Implemented

### ✅ Scenario 1: Dynamic Traffic Management
Helps traffic departments adjust signal timings and routing dynamically.

### ✅ Scenario 2: Urban Development Planning
Assists planners in understanding future congestion and optimizing road infrastructure.

### ✅ Scenario 3: Commuter Navigation
Provides smart travel time predictions and route suggestions.

---

## 🔒 Model Files

- `model.pkl`: Trained machine learning regression model
- `encoder.pkl`: Fitted encoder for categorical variable transformation

---

## 📊 Jupyter Notebooks

- `traffic volume.ipynb`: Exploratory Data Analysis + Model Building
- `traffic_volume_lbm_scoring_end_point.ipynb`: IBM Watson endpoint integration for scoring

---

## 📄 License

This project is licensed under the MIT License. Feel free to use, modify, and contribute!

---

## 🙋‍♂️ Author

Developed by **Sivasai Pepakayala**  
📧 [sivasaipepakayala07@gmail.com]  
🌐 [https://www.linkedin.com/in/psivasai/]
