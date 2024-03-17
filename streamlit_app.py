import streamlit as st
import pandas as pd
import joblib
# Function to load the model
@st.cache_data
def load_model():
    with open('calories_model', 'rb') as file:
        loaded_model = joblib.load(file)
    return loaded_model

# Load your model
loaded_model = load_model()


# Sidebar for navigation
st.sidebar.title('Navigation')
options = st.sidebar.selectbox('Select a page:', 
                           ['Prediction', 'Code', 'About'])

if options == 'Prediction': # Prediction page
    st.title('Calories Burnt Prediction Web App')

    # Index(['gender', 'age', 'height', 'weight', 'duration', 'heart_rate','body_temp'],
    # User inputs
    gender = st.selectbox('Gender', ['Male','Female'])
    age = st.number_input('Age', 1, 100, 25)
    height = st.number_input('Height in cm', 100, 250, 170)
    weight = st.number_input('Weight in kg', 30, 200, 70)
    duration = st.number_input('Duration in minutes', 1, 180, 60)
    heart_rate = st.number_input('Heart Rate', 60, 200, 100)
    body_temp = st.number_input('Body Temperature in Celsius', 35.0, 43.0, 37.0)

    user_inputs = {
        'gender': 0 if gender == 'Male' else 1,
        'age': age,
        'height': height,
        'weight': weight,
        'duration': duration,
        'heart_rate': heart_rate,
        'body_temp': body_temp
    }
    
    if st.button('Predict'):
        st.write(pd.DataFrame(user_inputs, index=[0]))
        # prediction = loaded_model.predict(pd.DataFrame(user_inputs, index=[0]))
        # st.markdown(f'**The predicted Calories Burnt is: {prediction[0]:,.2f}**')  # Display prediction with bold
        
        with st.expander("Show more details"):
            st.write("Details of the prediction:")
            # You can include more details about the prediction
            # For example, display the parameters of the loaded model
            st.json(loaded_model.get_params())
            st.write('Model used: Random Forest Regressor')
            
elif options == 'Code':
    st.header('Code')
    # Add a button to download the Jupyter notebook (.ipynb) file
    notebook_path = 'calories_burnt_prediction.ipynb'
    with open(notebook_path, "rb") as file:
        btn = st.download_button(
            label="Download Jupyter Notebook",
            data=file,
            file_name="calories_burnt_prediction.ipynb",
            mime="application/x-ipynb+json"
        )
    st.write('You can download the Jupyter notebook to view the code and the model building process.')
    st.write('--'*50)

    st.header('Data')
    # Add a button to download your dataset
    data_path = 'calories_data.csv'
    with open(data_path, "rb") as file:
        btn = st.download_button(
            label="Download Dataset",
            data=file,
            file_name="calories_data.csv",
            mime="text/csv"
        )
    st.write('You can download the dataset to use it for your own analysis or model building.')
    st.write('--'*50)

    st.header('GitHub Repository')
    st.write('You can view the code and the dataset used in this web app from the GitHub repository:')
    st.write('[GitHub Repository](https://github.com/gokulnpc/Calories-Burnt-Prediction)')
    st.write('--'*50)
    
elif options == 'About':
    st.title('About')
    st.write('This web app is created to predict the calories burnt based on the user inputs such as gender, age, height, weight, duration, heart rate, and body temperature.')
    st.write('The model used in this web app is a Random Forest Regressor model trained on the dataset with 15000 samples.')
    st.write('The dataset used in this web app is collected from the Kaggle dataset: [Dataset](https://www.kaggle.com/datasets/fmendes/fmendesdat263xdemos).')
    
    st.write('The web app is open-source. You can view the code and the dataset used in this web app from the GitHub repository:')
    st.write('[GitHub Repository](https://github.com/gokulnpc/Calories-Burnt-Prediction)')
    st.write('--'*50)

    st.header('Contact')
    st.write('You can contact me for any queries or feedback:')
    st.write('Email: gokulnpc@gmail.com')
    st.write('LinkedIn: [Gokuleshwaran Narayanan](https://www.linkedin.com/in/gokulnpc/)')
    st.write('--'*50)
