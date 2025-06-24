import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.gorqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
def load_langgraph_agenticai_app():
    """"
    
    """
    # LOAD ui
    ui=LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load your input from the UI")
        return
    user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            obj_llm_config = GroqLLM(user_control_input=user_message)
            model = obj_llm_config.get_llm_model()


            if not model:
                st.error("Error: LLM not found")
                return
            usecase= user_input.get("selected_usecase")
            if not usecase:
                st.error("Error: No use case selected.")
                return
            graph_builder= GraphBuilder(model)
            try:
                graph= graph_builder.setup_graph(usecase)

        except Exception as e:
