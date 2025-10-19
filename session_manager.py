import gradio as gr
import nest_asyncio
from pyngrok import ngrok
from aibot import Aibot

nest_asyncio.apply()

class GradioSessionsManager:
    "class for geenrating simultaneous user sessions for financial chatbot"

    def __init__(self):

        self.aibot = Aibot()
        self.sessions = {}
        self.interfaces = []
        self.servers = []


    def get_session(self, session_id:str):
        """
        for generating new session params

        Parameters
        ----------
        session_id : str
            session id for which session param would be generated if not
            already exists.
            
        """

        if session_id not in self.sessions:
            chat_history = self.aibot.initiate_chat_history(session_id)
            self.sessions[session_id] = {"history": chat_history,
                                        "messages":[]}


    def get_gradio_setup(self):
        """
        for gradio setup of interface for a single session
        """

        new_session_id = f'Session_{len(self.sessions)+1}'
        self.get_session(new_session_id)
        demo = gr.Interface(
            fn=self.aibot.get_response,
            inputs=[
                gr.Textbox(label="enter query"),
                gr.State(value=self.sessions[new_session_id])
            ],
            outputs=[
                gr.Textbox(label="Chat", lines=15),
                gr.State()
            ],
            title=f"Financial_Chatbot_{new_session_id}",
            allow_flagging="never"
        )
        server = demo.launch(server_port=None, share=False, quiet=True)
        self.interfaces.append(demo)
        self.servers.append(server)


    def create_setups(self, no_of_sessions:int):
        """
        wrapper for generating sessions and interfaces for n no of users

        Parameters
        ----------
        no_of_sessions : int
            number of users for which sessions would need to be generated
            
        """

        for session in range(no_of_sessions):

            self.get_gradio_setup()