import streamlit as st
#import streamlit.components.v1 as com
 
# from streamlit_lottie import st_lottie  
 
def Home_page():
 
   
   
    st.title("Integrating Machine Learning into a GUI with Streamlit")
   # com.iframe("https://lottie.host/embed/1d9c7726-8312-4477-ae0b-7efc13a12654/WKcl6YhXxL.json")
    st.title("Telco Churn Classification App :telephone:")
 
 
    st.markdown("""
        This app predicts whether a customer will churn or not using Machine Learning.
    """)
 
    st.subheader("Instructions")
    st.markdown("""
                - Upload a CSV file :o:
                - Select features for classififcation :star:
                - Choose a Machine Learning (ML) model from the dropdown :mag_right:
                - Click on Predict to get the predicted results :magic_wand:
                - The app gives you a report on the performance of the ML model :chart_with_downwards_trend:
                - The app provides a performance report with metrics such as accuracy, precision, recall, f1-score, etc. :chart_with_upwards_trend:
    """)
   
    st.header("App features")
    st.markdown("""
 
        - **Data View**: View the uploaded data
        - **Predict View**: Get the predicted results from the ML model
        - **Dashboard**: View the performance of the ML model
    """)    
 
    st.subheader("User Benefits")
    st.markdown("""
                **Data Driven Approach**: Informed decision making based on the data
 
                **Streamlined Process**: Streamlined process for churn prediction
               
                **Real-time Predictions**: Allows users to input customer data and instantly receive churn predictions, enabling quick interventions to retain customers.
               
                **Interactive Insights**: Explore interactive visualizations and dashboards, helping to analyze trends, customer behaviors, and key churn drivers intuitively.
               
                **User-friendly Customization**: Provides options to adjust input parameters, filters, and thresholds, tailoring predictions and insights to specific business needs without requiring technical expertise.
               
                **Cost-Effective**: Streamlined process and cost-effective approach to churn prediction
     """)
   
 
    st.divider()
   #  st.subheader("Author: David Zodanu")
   #  st.markdown("""
   #      "Welcome to My Streamlit App! :wave:
 
   #   Hi, I'm a passionate data analyst and aspiring AI expert. I specialize in leveraging data-driven solutions to uncover insights and drive impactful decisions.
   #   I enjoy working on projects that blend analytics with real-world applications. Explore this app to learn more about my work and how I can help you unlock the potential of your data.
   #   """ )
   
   
# Rating the App
 
    st.header("RATE THIS APP")
 
    rating = st.radio("Rate the app",("1","2","3","4","5"))
   
    if rating == "1":
        st.write("I'm sorry. You have bad taste!😀")    
    elif rating == "2":
        st.write("Good but You can do better!👏🏽")    
    elif rating == "3":
        st.write("You are getting there!🥳")    
    elif rating == "4":
        st.write("You have good taste!🥂")    
    elif rating == "5":
        st.write("You are amazing!🎉:champagne:")
 
 
    st.divider()
   
    st.write('NEED HELP:question:')
    st.write('Email: david.zodanu@azubiafrica.org :email:')
   #  st.write('GitHub: https://github.com/Asi9128 :cat:')
    st.write('LinkedIn: https://www.linkedin.com/in/david-zodanu-904751105:link:')
    st.write('Phone: 0535560023')
 
 
 
