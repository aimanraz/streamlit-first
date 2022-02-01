
# import necessary packages
import streamlit as st
import pandas as pd
import numpy as np
from function import *
from PIL import Image
st.set_option('deprecation.showPyplotGlobalUse', False)
sns.set_theme(style='dark',palette="deep")

# set the page title
st.set_page_config(page_title='Datama')
# import banner image
image = Image.open("Banner.png")
st.image(image)

# loading function
@st.cache(suppress_st_warning=True)
def load_file(file):
    if file is not None:
        try:
            df = pd.read_csv(file)
        except Exception as e:
            print(e)
            df = pd.read_excel(file)
        return(df)

# the main application
def main():
    selection = ['EDA','Machine learning','About Us']
    option = st.sidebar.selectbox('Main options:',selection)

    if option == "EDA":
        uploaded_file = st.file_uploader("Choose a file (Preferred cleaned dataset)", type = ['csv', 'xlsx'])
        data = load_file(uploaded_file)
        if data is not None:
            st.success("Successfully loaded")
        else:
            st.warning("Please load the dataset")

        st.subheader("Exploratory Data Analysis")
        sub_option = ['About Data','Visualisation']
        sub_option = st.sidebar.selectbox('Sub options:',sub_option)

        if sub_option == 'About Data':
            st.markdown("""
            #####
            ###### Displayed the basic information about the dataset

            """)
            if st.button('Generate report'):
                if data is not None:
                    about_data(data)
                else:
                    st.error('There is no dataset')

        elif sub_option == 'Visualisation':
            st.markdown("""
            #####
            ###### Visualisation features

            """)
            if data is not None:
                viz(data)
            else:
                st.error('There is no dataset')

    elif option == "Machine learning":
        st.subheader("Coming soon")

    else:
        st.markdown("""
        ## About Datama

        ##### Datama is web application used to perform EDA, and visualization for any given dataset. This web application eases the stakeholder's access to any crucial task of every data analytic project.
        ###### Developed by Aiman Raziq


        """)


if __name__ == '__main__':
	main()
