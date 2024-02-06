import streamlit as st
import hydralit_components as hc
import home
import predict_page

st.set_page_config(page_title='Pneumonia Detection', 
                   page_icon=':bar_chart:', layout='wide',
                   )

    
# atur menu untuk app
menu_data = [
    {'icon': "far fa-chart-bar", 'label':"Predict"},
]

over_theme = {'txc_inactive': '#FFFFFF','menu_background':'purple'}
menu_id = hc.nav_bar(  
    menu_definition=menu_data,
    override_theme=over_theme,
    home_name='Home',
    # login_name='Logout',
    hide_streamlit_markers=True, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
)

# Check if the Home menu item is clicked
if menu_id == 'Home':
    home.home_page()

    
if menu_id == 'Predict':
    predict_page.main()
   