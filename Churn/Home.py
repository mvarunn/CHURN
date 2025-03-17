import streamlit as st

# # Create a sidebar with navigation
# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to", ["Introduction", "Prediction"])

st.write("# Customer Churn Prediction App")
st.write("Welcome to the Customer Churn Prediction app!")
st.write("This application helps predict whether a customer is likely to churn (leave) based on the details you provide. It uses machine learning models to make predictions based on user data.")

image_path = "https://blog.xoxoday.com/content/images/2024/05/corporate-perks-at-work.webp"
st.image(image_path)

st.markdown("""**👈 Select an app from the sidebar** to get started""")

# if page == "Introduction":
#     st.write("# Customer Churn Prediction App")
#     st.write("Welcome to the Customer Churn Prediction app!")
#     st.write("This application helps predict whether a customer is likely to churn (leave) based on the details you provide. It uses machine learning models to make predictions based on user data.")
#     st.markdown("""**👈 Select an app from the sidebar** to get started""")

# elif page == "Prediction":
#     st.write("# Predict Customer Churn")
#     st.write("Fill in the details below to predict the likelihood of customer churn.")
    
#     # Link to prediction page
#     st.write("[Go to Prediction Page](predict.py)")
