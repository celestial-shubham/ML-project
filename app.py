 
import pickle
import streamlit as st
import warnings
warnings.filterwarnings('ignore')
# loading the trained model
pickle_in = open('heart_disease.pkl','rb') 
classifier = pickle.load(pickle_in)

# @st.cache()

# defining the function which will make the prediction using the data which the user inputs 
def prediction(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
    #preprocessing user input
    
    if sex == 'Male':
        sex = 1
    else:
        sex =0
        
    if fbs == "true":
        fbs = 1
    else:
        fbs = 0
    
    if exang == "true":
        exang = 1
    else:
        exang = 0
    
   # Making predictions 
    prediction = classifier.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    
    if prediction == 0:
        pred = 'No Heart Issue!! You are Healthy :)'
    else:
        pred = 'Heart Issue Detected !! See Your Doctor'
    return pred


# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    st.title("Heart-Disease Detector")
    html_temp = """ 
    <div style ="background-color:tomato;padding:13px"> 
    <h2 style ="color:white;text-align:center;"> Heart-disease Classifier </h2> 
    </div> 
    """
    with st.sidebar:
      if st.button("About"):
          st.text("Visit [Github](https://github.com/celestial-shubham/ML-project)!!")
          st.text("By Shubham Verma")
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    age = st.number_input("Enter Your Age :", min_value=1, max_value=100, value=50, step=1)
    sex = st.selectbox('sex',("Male","Female"))
    exang = st.selectbox('Do you Feel Exercise induced Anigma ?',("true","false")) 
    fbs = st.selectbox('is your fasting blood sugar > 120 mg/dl ?',("true","false")) 
    cp = st.number_input("chest pain type : \n Enter 0: Typical angina: chest pain related decrease blood supply to the heart \n Enter 1: Atypical angina: chest pain not related to heart\nEnter 2: Non-anginal pain: typically esophageal spasms (non heart related)\nEnter 3: Asymptomatic: chest pain not showing signs of disease", min_value=1, max_value=3, value=1, step=1)
    trestbps = st.number_input("resting blood pressure (in mm Hg on admission to the hospital) anything above 130-140 is typically cause for concern", min_value=50, max_value=200, value=90, step=1)
    chol = st.number_input("cholestoral in mg/dl \n above 200 is cause for concern",min_value = 120,max_value = 250,value = 210,step =2)
    restecg = st.number_input("Resting Electrocardiographic results:: \n Enter 0 :Nothing to note \n Enter 1:ST-T Wave abnormality \n Enter 2:Possible or definite left ventricular hypertroph", min_value=0, max_value=2, value=0, step=1)
    thalach = st.number_input("Maximum heart rate achieved", min_value=20, max_value=200, value=60, step=1)
    oldpeak = st.number_input('ST depression induced by exercise',min_value = 0.1 ,max_value =7.0,value=1.0,step=0.2)
    slope = st.number_input('the slope of the peak exercise ST segment:: \n Enter 0: Upsloping: better heart rate with excercise (uncommon)\n Enter 1: Flatsloping: minimal change (typical healthy heart) \n Enter 2: Downslopins: signs of unhealthy heart', min_value=0, max_value=2, value=0, step=1)
    ca = st.number_input('number of major vessels (0-3) colored by flourosopy', min_value=0, max_value=3, value=1, step=1)
    thal = st.number_input('thalium stress result \n Enter (1-3): normal \n Enter 6: fixed defect: used to be defect but ok now \n Enter 7: reversable defect: no proper blood movement when excercising', min_value=1, max_value=7, value=1, step=1)
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Report"): 
        result = prediction(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal) 
        st.success('Your Report Says {}'.format(result))
        st.balloons()
     
if __name__=='__main__':
    main()
