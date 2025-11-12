# 🏏 IPL Win Predictor
This project is a machine learning-based web application built using Streamlit. It predicts the winning probability of an IPL (Indian Premier League) team during a live match based on key match parameters like target, score, overs completed, and more.

---

## 🎯 Live Demo

1. Visit the [Live Site](https://ipl-win-predictorgit-hlahvvso8zydckesw2ttql.streamlit.app/)
   
---

## ✅ Features

- Predicts win probability based on live match inputs  
- Dynamic team selection with validation (batting ≠ bowling)  
- Selectable venue from official IPL stadiums  
- Inputs for target, score, overs completed, and wickets fallen  
- Responsive and clean user interface using Streamlit  

---

## 🛠 Technologies Used

- **Python** – Core programming language  
- **Streamlit** – For building the web UI  
- **Pandas** – Data manipulation  
- **Scikit-learn** – Machine learning pipeline  
- **Pickle** – Model serialization  

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/EndravathKrishna/IPL-Win-Predictor.git
cd IPL-Win-Predictor

# 2. (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install required Python packages
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py
