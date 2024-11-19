from langchain_openai import ChatOpenAI
import os
from langchain_core.messages import SystemMessage, HumanMessage
from custom_prompts import sys_ev_plnner_prompt, event_extract_sys_prompt


llm = ChatOpenAI(temperature=0.5, model_name="gpt-4", api_key=os.environ["OPENAI_API_KEY"])

def get_event_plan(event_details):
    messages = [
        SystemMessage(content=sys_ev_plnner_prompt),
        HumanMessage(content=f"Event details: {event_details}"),
    ]
    response = llm.invoke(messages)
    return response.content


def extract_event_details(transcription):
    messages = [
        SystemMessage(content=event_extract_sys_prompt),
        HumanMessage(content=f"Transcription: {transcription}"),
    ]
    response = llm.invoke(messages)
    return response.content
    
