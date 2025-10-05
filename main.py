#-importing the libraries
from typing_extensions import TypedDict
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph,START,END
import os
from dotenv import load_dotenv
load_dotenv()
#loading the environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

#-Defining the LLM
llm=ChatGroq(model="llama-3.1-8b-instant",api_key=groq_api_key)
#-Creating_State (Data-Validation)
class State(TypedDict):
    user_message:str
    bot_message:str

#-Defining_Function_Node1
def user_input(state:State):
    print("USER",state['user_message'])
    return {'user_message':state['user_message']}
#-Defining_Function_Node2
def groq_response(state:State):
    response=llm.invoke(state['user_message'])
    return {'bot_message': response.content}
#Building_the_StateGraph
graph=StateGraph(State)
#-i-adding_the_nodes
graph.add_node("USER_MESSAGE",user_input)
graph.add_node("MODEL_RESPONSE",groq_response)
#-ii-adding_the_edges
graph.add_edge(START,'USER_MESSAGE')
graph.add_edge('USER_MESSAGE',"MODEL_RESPONSE")
graph.add_edge("MODEL_RESPONSE",END)
#-executing the graph
compiled_graph=graph.compile()
#-Running The Chatbot
if __name__ == "__main__":
    user_message = input("You: ")
    output = compiled_graph.invoke({"user_message": user_message})
    print("GroqBot:", output["bot_message"])

#-this helps us to load it in 'app.py'
__all__ = ["compiled_graph"]