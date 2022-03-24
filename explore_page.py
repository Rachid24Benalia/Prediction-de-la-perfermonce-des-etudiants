import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


@st.cache
def load_data():
    df_train = pd.read_csv('student-mat.csv')

    
    df_train['famsup'] = df_train['famsup'].replace({'yes':1, 'no':0})
    df_train['activities'] = df_train['activities'].replace({'yes':1, 'no':0})
    df_train['higher'] = df_train['higher'].replace({'yes':1, 'no':0})
    df_train['romantic'] = df_train['romantic'].replace({'yes':1, 'no':0})

    return df_train

df_train = load_data()

def show_explore_page():
    st.title("Explore Student Grade")

    
    st.write(
        """
    #### Mean final grade Based On weekly study time 
    """
    )
    st.write(
        """
    ###### weekly study time |1(<2h)| and |2(2h to 5h)|and | 3(5h to 10h)| and|4(10h to 20h)|
    """
    )

    
    data = df_train.groupby(["studytime"])["G3"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write(
        """
    #### Mean final grade Based On romantic relationship 
    """
    )
    st.write(
        """
    ###### 0 : NONE  -1 : yes but not in same shool -2 : yes, in same chool
    """
    )
    dat = df_train.groupby(["romantic"])["G3"].mean().sort_values(ascending=True)
    st.bar_chart(dat)
    

    
