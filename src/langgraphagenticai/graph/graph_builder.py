from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode

class GraphBuilder:
    def __init__(self, model):
        self.model = model
        self.graph_builder= StateGraph(State)

    def basic__chatbot_build_graph(self):
        self.basic_chatbot_node = BasicChatbotNode(self.model)
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot",END)

