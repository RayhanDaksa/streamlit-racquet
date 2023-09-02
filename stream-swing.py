import pickle
import streamlit as st

# Load the trained model
swing_model = pickle.load(open('swing_model.sav', 'rb'))

# Function to describe swing weight
def describe_swing_weight(swing_weight):
    if swing_weight > 89:
        return 'Head Heavy - Great For Power / Attacking Player'
    elif 83 < swing_weight <= 89:
        return 'Balance - Great For All Around / Hybrid Player'
    else:
        return 'Head Light - Great For Speed / Defensive Player'

# Title of the web app
st.title('Swing Weight Calculator')

# Input fields for Weight and Balance
Weight = st.text_input('Input Weight of Racquet (in gram): ')
Balance = st.text_input('Input Balance Point of Racquet (in mm): ')

swing_weight = None
swing_weight_rounded = None  # Define the variable here

# Add a button to trigger the prediction
if st.button('Predict Swing Weight'):
    if Weight and Balance:
        try:
            Weight = float(Weight)
            Balance = float(Balance)
            
            # Make the prediction
            swing_weight = swing_model.predict([[Weight, Balance]])[0]
            
            # Round the prediction to the nearest 0.5 kg
            swing_weight_rounded = round(swing_weight * 2) / 2
        except ValueError:
            st.error("Please enter valid numerical values for Weight and Balance.")

# Display the rounded prediction (if available)
if swing_weight_rounded is not None:
    st.write(f"Predicted Swing Weight (Rounded to nearest 0.5 kg): {swing_weight_rounded:.2f} kg")

    # Describe the swing weight
    swing_weight_description = describe_swing_weight(swing_weight_rounded)
    st.write(f"Description: {swing_weight_description}")


