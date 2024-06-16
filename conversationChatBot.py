###################################################################
# Aim:
# 1. Integrate code with an LLM API (eg OpenAI, anthropic or local Olama)
# 2. Create a conversational Q&A chatpot with Open AI (official) and key using streamlit session
# 3. Control system, human and AI message schema
###################################################################

###################################################################
# Load packages
###################################################################
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama

###################################################################
# Declare parameters
###################################################################
load_dotenv()
open_api_key = os.getenv('OPEN_API_KEY')

###################################################################
# Set up streamlit framework
###################################################################
st.header('Langchain Demo - Q&A Bot')
user_input = st.text_input('Hey, lets chat! ')

###################################################################
# Main
###################################################################
def main():

    ###################################################################
    # 1. Set up Session state to remember the conversations
    ###################################################################
    if 'flowmessages' not in st.session_state:
        st.session_state['flowmessages'] = [
            SystemMessage(content = 'You are an AI assistant.')
        ]
    st.session_state['flowmessages'].append(HumanMessage(content = user_input))

    ###################################################################
    # 2. Set up LLM 
    ###################################################################
    llm=Ollama(model = 'llama2')
    #or ChatOpenAI(openai_api_key = open_api_key)

    ###################################################################
    # 3. Run the LLM
    ###################################################################
    response = llm.invoke(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content = response))
    st.write(response)
    

###################################################################
# Driver
###################################################################
if __name__ == '__main__':
    
    if len(user_input)>0:
        main()

