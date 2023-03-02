import streamlit as st 

st.set_page_config(
        page_title="CISCO REPORT ANALYSIS",
        page_icon="chart_with_upwards_trend",
        layout="wide",
        initial_sidebar_state="collapsed")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: red;'> MOC ANALYSIS </h1>", unsafe_allow_html=True) 
ft = """
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 0;
top:230px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: left; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p> <img src="https://www.icegif.com/wp-content/uploads/icegif-5453.gif"   height= "30"/><a style='display: inline; text-align: left;'  target="_blank"> LAST MODIFIED TSTAMP</a></p>
</div>

</div>
"""
import os.path, time
get_time = str(time.ctime(os.path.getmtime("Home.py")))
ft = ft.replace("TSTAMP",get_time)
st.write(ft, unsafe_allow_html=True) 