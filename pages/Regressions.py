import streamlit as st  # pip install streamlit
import pandas as pd  # pip install pandas
import numpy as np 
from streamlit_option_menu import option_menu


hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: red;'> REGRESSION ANALYSIS </h1>", unsafe_allow_html=True) 


uploaded_file = st.file_uploader('Choose a XLSX file', type='csv')
#uploaded_file ="./Dashboard.xlsx";
 
if uploaded_file:
   st.markdown('---')
   df = pd.read_csv(uploaded_file,sep="|")
   df=df.fillna('') 
   df.index = np.arange(1, len(df) + 1)
   modulecol,ownercol = st.columns(2)
   try:
       owner_ph = ownercol.empty()
       owner_cntnr = owner_ph.container()
       module_ph = modulecol.empty()
       module_cntnr = modulecol.container()
       module_opts = ["ALL"] + list(set(df['module']))
       owner_opts = ["ALL"] + list(set(df['owner']))
       with modulecol:
           module = module_cntnr.selectbox(label="Module",options=module_opts,key="MODULE")
       with ownercol:
           owner = owner_cntnr.selectbox(label="Owner",options=owner_opts,key="Owner")

       owner_opts = ["ALL"] + list(set(df['owner']))
   
       
       if module != "ALL":
           df =df.loc[df['module'].isin([module])]
           owner_opts = ["ALL"] + list(set(df['owner']))
           owner_cntnr = owner_ph.empty()
           with ownercol:
               owner = owner_cntnr.selectbox(label="Owner",options=owner_opts,key=module+owner)
           
       if owner != "ALL" and  module != "ALL" :
           df = df[(df['module']==module) & (df['owner']==owner)]
       if module == "ALL" and  owner != "ALL" :
           df =df.loc[df['owner'].isin([owner])]
   except Exception as e:
       pass
  

   st.table(df)
    


   #st.empty()
   #st.dataframe(df,width=800)