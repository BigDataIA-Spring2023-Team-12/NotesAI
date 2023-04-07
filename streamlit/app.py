import streamlit as st
from datetime import datetime
from Functions.auth_functions import login_user, register_user
from Functions.db_functions import log_data, user_data
from prompt.api.organizer import organize_context
from prompt.api.summarizer import summarize_text


with st.sidebar:
    # options menu  
    selected = st.selectbox("Menu", ["Log In", 'Sign Up'])
    
    # log in form
    if 'login' not in st.session_state:
        st.session_state['login'] = False

   


    if selected == "Log In":
        
        st.write('## Log In')
        login_username = st.text_input('Email')
        login_password = st.text_input('Password', type='password')
        # authentication status update
        if st.button('Log In!'):
            # send login request 
            st.session_state['login'] = login_user(login_username,login_password)

        if st.session_state['login'] == True:
            if st.button("Logout"):
                st.session_state['login'] = False

    # # Sign-up form 
    if selected == "Sign Up":
        st.write('## Sign up')
        name = st.text_input('Name')
        username = st.text_input('Email',key='signup_username')
        plan = st.selectbox(
                    "Select Plan",
                ["free", "gold","platinum"]
                )

        password = st.text_input('Password', type='password',key='signup_pass')
        confirm_password = st.text_input('Confirm Password', type='password')

        
        if st.button('Sign up'):
            if password != confirm_password:
                st.write("Passwords don't Match!")
            else:
                # send register request 
                signup_status = register_user(name,username,password,plan)
                if signup_status:
                    st.success("User Registered Successfully! Sign-in to continue...")
                else:
                    st.error("Email already exists! Sign in to continue...")


if  st.session_state['login'] == True:
    st.title("Welcome to the Chatbox")


    with st.form("my_form"):
        message = st.text_area("Type message to remember")
        submit = st.form_submit_button("Send")

    if submit:
        log_data(login_username, datetime.now(),message)


   

    df = user_data(login_username)
    df = df.drop(columns="username")
    st.dataframe(data=df,use_container_width=True)
    context_list = df["message"].tolist()
    context_str = ' '.join(context_list)

    st.write("## Sumarize the Data")
    if st.button("Summarize"):
            summarize = summarize_text(context_str)
            st.write(summarize)

    
    st.write("## Organize the Data")
    if st.button("Organize"):
            organize = organize_context(context_str)
            st.write(organize)


    