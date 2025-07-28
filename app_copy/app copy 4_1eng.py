import streamlit as st
import random
import pandas as pd

# Simulated data for demonstration
mock_expressions = ["happy", "sad", "anxious", "calm"]
mock_tones = ["cheerful", "low", "nervous", "steady"]
mock_activities = ["sitting", "walking", "still", "active"]
mock_reactions = ["positive", "neutral", "negative"]

# Simulated emotion classification based on inputs
def classify_emotion(expression, tone, activity):
    if expression == "sad" or tone == "low" or activity == "still":
        return "lonely"
    elif expression == "anxious" or tone == "nervous":
        return "anxious"
    elif expression == "happy" and tone == "cheerful" and activity == "active":
        return "happy"
    else:
        return "calm"

# Simulated care action recommendation
def recommend_action(emotion):
    actions = {
        "lonely": ["Start a conversation", "Play music"],
        "anxious": ["Call caregiver", "Suggest rest"],
        "happy": ["Encourage activity", "Play music"],
        "calm": ["Maintain routine", "Offer a book"]
    }
    return random.choice(actions.get(emotion, ["Monitor"]))

# Simulated reinforcement learning reward
def get_reward(action, reaction):
    if reaction == "positive":
        return 1
    elif reaction == "negative":
        return -1
    else:
        return 0

# Streamlit app
st.title("AI Elderly Care Simulator for Students")

# Tutorial Section
st.header("Tutorial: How to Use This App")
st.markdown("""
Welcome to the AI Elderly Care Simulator! This app helps you understand how AI can analyze an elderly person's emotions and suggest caring actions. Here's how it works:

1. **Choose Inputs**: Use the dropdown menus to select an expression, voice tone, and activity for a simulated elderly person.
2. **See AI Analysis**: The app will analyze these inputs and guess the person's emotion (e.g., happy, lonely).
3. **Get Recommendations**: Based on the emotion, the app suggests a caring action (e.g., play music, call a caregiver).
4. **Simulate Reaction**: Choose how the person reacts to the action, and the app will give a 'reward' score to show if the action worked well.
5. **Learn and Explore**: Try different combinations to see how the AI makes decisions and how reactions affect future suggestions!

This app is a simplified version to help you learn about AI, emotions, and caring for others.
""")

# Input Section
st.header("Step 1: Input the Elderly Person's Data")
expression = st.selectbox("Select Facial Expression", mock_expressions)
tone = st.selectbox("Select Voice Tone", mock_tones)
activity = st.selectbox("Select Activity", mock_activities)

# Analyze and Recommend
if st.button("Analyze and Recommend"):
    emotion = classify_emotion(expression, tone, activity)
    action = recommend_action(emotion)
    
    st.header("Step 2: AI Analysis Results")
    st.write(f"**Detected Emotion**: {emotion}")
    st.write(f"**Recommended Action**: {action}")
    
    # Reaction Simulation
    st.header("Step 3: Simulate the Elderly Person's Reaction")
    reaction = st.selectbox("How does the person react?", mock_reactions)
    
    if st.button("Submit Reaction"):
        reward = get_reward(action, reaction)
        st.write(f"**Reaction**: {reaction}")
        st.write(f"**Reward Score**: {reward} (Positive = +1, Neutral = 0, Negative = -1)")
        
        # Display data in a table for educational purposes
        st.header("Step 4: Data Summary")
        data = {
            "Expression": [expression],
            "Tone": [tone],
            "Activity": [activity],
            "Detected Emotion": [emotion],
            "Recommended Action": [action],
            "Reaction": [reaction],
            "Reward": [reward]
        }
        df = pd.DataFrame(data)
        st.table(df)
        
        st.markdown("""
        **What does this mean?**
        - The AI uses your inputs to guess the person's feelings.
        - It suggests an action to help them feel better.
        - The reward score helps the AI learn if the action was good or not.
        Try different inputs to see how the AI changes its suggestions!
        """)

# Additional Educational Note
st.header("Why This Matters")
st.markdown("""
This app shows how AI can help care for people by understanding their emotions and actions. For example, if someone is lonely, the AI might suggest talking to them. In real life, AI could use cameras or sensors to collect this data, but we used simple choices here to make it easy to understand. Caring for others involves both technology and kindness, and this app helps you think about both!
""")