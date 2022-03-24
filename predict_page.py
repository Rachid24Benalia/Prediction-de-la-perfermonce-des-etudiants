import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
L = data["model"]




def show_predict_page():
    st.title("Final Grade Prediction")
    st.write("""### We need some information to predict your final grade""")
    
    """
    reason = (
        "course",
        "home",
        "reputation",
        "other",
    )
    """
    G=(
        "class prepa",
        "GM",
        "GIAI",
        "GI",

    )
    famrel=(
        "yes",
        "no",
    )
    Prel=(
        "yes",
        "no",
    )
    famsup = (
        "yes",
        "No",
    )
    
    activities = (
        "yes",
        "No",
    )
    higher = (
        "yes",
        "No",
    )
    
    #tzdt mais maghat2tr
    G=st.selectbox("your field:",G)

    famrel = st.selectbox("do you love your field? ",famrel)
    traveltime = st.slider(" Home to school travel time : 1 si (<15min)- 2 (15 to 30min)- 3 (30min to 1h)- 4 (>1h)", 1, 4, 1)
    Studytime = st.slider("weekly study time:1 si (<2h) 2-(2h to 5h) 3-(5h to 10h)4-(10h to 20h)  ", 1, 4, 1)
    famsup = st.selectbox("family educional support", famsup)
    paid = st.slider("Nbr of extra paid classes", 0,6,1)
    #reason = st.selectbox("reason u chose this shool", reason)
    activities = st.selectbox("activités parascolaires", activities)
    higher = st.selectbox("visant à être un entrepreneur ou Non?", higher)
    romantic = st.slider("with a romantic relationship( 0 : NONE  -1 : yes but not in same shool -2 : yes, in same chool", 0,2,1)

    goout = st.slider("quality of Classmates relationships ( 1 - very low to 5 - very high ) ",1, 5, 1)
    health = st.slider("current health status(sport,healthy food ,sleep weel) ( 1 - very bad to 5 - very good )", 1, 5, 1)

    #tzado mais bla dat
    Prel=st.selectbox("majorité d prof know u",Prel)
    lkra=st.slider("kari ou nn :0(kari solo),1(kari m3a drari),2(makarich) ", 0, 2, 1)

    ok = st.button("Calculate final note")
    if ok:
        X = np.array([ famsup,
        activities,higher,famrel,Prel,romantic ,paid,Studytime,traveltime,goout,health,lkra])
        

        for i in range(5):
            
            if X[i] == "yes":
                X[i]=1
            else:
                X[i]=0
        X=[int(X[j]) for j in range(12)]
        X = np.array(X)
        X=X.reshape(1,-1)

        salary = L.predict(X)
        st.subheader(f"The Final Grade is {salary[0]:.2f}")
