import streamlit as st
import pickle
import pandas as pd

# Load trained model pipeline
pipe = pickle.load(open('pipe.pkl', 'rb'))

# Team and venue data
teams = [
    'Chennai Super Kings', 'Delhi Capitals', 'Gujarat Titans', 'Kolkata Knight Riders',
    'Lucknow Super Giants', 'Mumbai Indians', 'Punjab Kings', 'Rajasthan Royals',
    'Royal Challengers Bengaluru', 'Sunrisers Hyderabad'
]

venues = [
    'M. Chinnaswamy Stadium, Bengaluru',
    'Punjab Cricket Association IS Bindra Stadium, Mohali',
    'Arun Jaitley Stadium, Delhi', 'Wankhede Stadium, Mumbai',
    'Sawai Mansingh Stadium, Jaipur', 'M. A. Chidambaram Stadium, Chennai',
    'Eden Gardens, Kolkata', 'Narendra Modi Stadium, Ahmedabad',
    'Himachal Pradesh Cricket Association Stadium, Dharamsala',
    'Rajiv Gandhi International Stadium, Hyderabad',
    'Barsapara Cricket Stadium, Guwahati',
    'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam',
    'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow',
    'Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur'
]

# UI Title
st.title('🏏 IPL Win Predictor')

# Team selection
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team', sorted(teams))

with col2:
    # Filter out batting team from bowling team options
    bowling_options = [team for team in teams if team != batting_team]
    bowling_team = st.selectbox('Select the bowling team', sorted(bowling_options))

# Venue
selected_venue = st.selectbox('Select host Stadium', sorted(venues))

# Match target
target = st.number_input('Target Score', min_value=1, step=1, format="%d")

# Match state inputs
col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input('Current Score', min_value=0, step=1, format="%d")

with col4:
    overs = st.number_input('Overs Completed', min_value=0.0, max_value=20.0, step=0.1, format="%.1f")

with col5:
    wickets = st.number_input('Wickets Fallen', min_value=0, max_value=10, step=1, format="%d")

# Prediction
if st.button('Predict Probability'):
    if overs == 0:
        st.error("Overs cannot be zero for calculation.")
    elif score > target:
        st.warning("Score is already greater than target. Match likely won!")
    else:
        runs_left = target - score
        balls_left = 120 - int(overs * 6)
        wickets_left = 10 - wickets
        crr = score / overs
        rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

        # Create input dataframe
        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'venue': [selected_venue],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets_left': [wickets_left],
            'target_runs': [target],
            'crr': [crr],
            'rrr': [rrr]
        })

        # Predict win probabilities
        result = pipe.predict_proba(input_df)
        loss = result[0][0]
        win = result[0][1]

        # Display
        st.success(f"🏏 {batting_team} Win Probability: **{round(win * 100)}%**")
        st.error(f"🎯 {bowling_team} Win Probability: **{round(loss * 100)}%**")
