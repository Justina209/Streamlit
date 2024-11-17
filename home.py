import streamlit as st
#import streamlit.components.v1 as com
 
# from streamlit_lottie import st_lottie  
 
def Home_page():
    # uploaded_file = st.file_uploader(r"C:\Users\JUSTINA\Downloads\telco image.pptx", type="pptx")
    
    # if uploaded_file is not None:
    # # Display the uploaded image
    #  st.image(uploaded_file)

    st.title("Integrating Machine Learning into a GUI with Streamlit")
   
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
  
 
    #Adding a clickable link
    st.markdown("[Watch a Demo](https://www.youtube.com/watch?v=1nKOVQyrUqI)")
    
  
   
   
# Rating the App
 
    st.header("RATE THIS APP")
 
    rating = st.radio("Rate the app",("1","2","3","4","5"))
   
    if rating == "1":
        st.write("OOpsy. What could have gone wrong?😀")    
    elif rating == "2":
        st.write("Not too bad!👏🏽")    
    elif rating == "3":
        st.write("Glad you are making progress!🥳")    
    elif rating == "4":
        st.write("We are doing much better!🥂")    
    elif rating == "5":
        st.write("Excellent!🎉:champagne:")
 
    # st.image(r"C:\Users\JUSTINA\Documents\justina pic.jpg")
    st.divider()
   
    st.write('NEED HELP:question:')
    st.write('Email: justina.owusua@azubiafrica.org :email:')
   #  st.write('GitHub: https://github.com/Justina209 :cat:')
    st.write('LinkedIn: https://www.linkedin.com/in/justina-abena-owusua:')
    st.write('Phone: 0535560023')
 
 
 
