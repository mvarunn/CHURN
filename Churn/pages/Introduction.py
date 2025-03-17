import streamlit as st

st.title("Introduction to Features")

st.write("""
#### Here's an explanation of each feature you need to fill out:

1. **City**: Choose the city where the customer resides.
   
2. **Latitude and Longitude**: Provide the latitude and longitude coordinates of the customer’s location. 

3. **Gender**: Select the customer's gender.

4. **Senior Citizen**: Select whether the customer is a senior citizen.
   
5. **Partner**: Select if the customer has a partner.

6. **Dependents**: Indicate if the customer has dependents.

7. **Tenure (Months)**:  This represents how long the customer has been with the service in months. Longer tenure typically correlates with lower churn.

8. **Phone Service**: Whether the customer has phone service or not. This could influence churn predictions.

9. **Multiple Lines**: Whether the customer has multiple phone lines. Having multiple lines may reduce the likelihood of churn.

10. **Internet Service**: Whether the customer has internet service, and if so, what type.

11. **Online Security, Online Backup, Device Protection, Tech Support**: These fields represent the type of services the customer uses.

12. **Streaming TV, Streaming Movies**: Whether the customer uses streaming services (TV or movies). These services may indicate a higher level of engagement with the service provider.

13. **Contract**: Indicates the type of contract the customer has. Longer contracts may lead to lower churn.

14. **Paperless Billing**: Whether the customer uses paperless billing, which may affect customer retention.

15. **Payment Method**: The payment method used by the customer.

16. **Monthly Charges**: The customer's monthly bill for using the service. Higher charges may indicate higher value customers.

17. **Total Charges**: The total amount spent by the customer over the course of their subscription.
         
18. **Churn Score**: The chances/score predicting their likelihood to churn
         
19. **CLTV**: Cutomer Life Time Value
""")
