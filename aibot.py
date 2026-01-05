import os
import base64
from langchain_groq.chat_models import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

class Aibot:
  "class for utilising llm and prompt creation modules"

  def __init__(self):

      self.chatmodel = ChatGroq(
                        model = 'meta-llama/llama-4-scout-17b-16e-instruct',
                        temperature = 0
                    )


  def initiate_chat_history(self, id:str)-> list:
    """
    class method for instantiating agent and its parameters.

    Parameters
    ----------
    id : str
        session id for which chat history needs to be initiated.
        
    Returns
    ----------
    list -> initiated history list of the session chat
    """

    global DOC_PATHS

    print(DOC_PATHS)
    
    chat_history = [SystemMessage(content="You are a helpful financial assistant.")]


    message_content = [
                {"type": "text", "text": "Below is a financial statement of a company on which you would need to answer future questions"},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{self.execute_DATA_LOADER(DOC_PATHS[id])}"},
                },
            ]

    chat_history.append(HumanMessage(content=message_content))

    return chat_history


  def get_response(self, user_input:str, session:dict)->tuple:
    """
    get response for a query based on previous context.

    Parameters
    ----------
    user_input : str
        user query.
        
    Returns
    ----------
    tuple (str, dict): tuple of ai response and updated session params 
    """

    history = session['history']
    history.append(HumanMessage(content=user_input))
    response = self.chatmodel.invoke(history)
    history.append(AIMessage(content=response.content))

    if user_input:
        session["messages"].append(f"USER INPUT: - {user_input}")
        session["messages"].append(f"AI RESPONSE: - {response.content}")
        session["history"].extend(history)

    return "\n".join(session["messages"]), session


  def execute_DATA_LOADER(self, file_path:str) -> str:
    """
    function for converting image to loadable base64 str
    
    Parameters
    ----------
    file_path : str
        path of financial document.
        
    Returns
    ----------
    str: base64 converted document image
    """
    

    #based on user input convert the file into base64
    with open(file_path, "rb") as image_file:
      encoded_str = base64.b64encode(image_file.read()).decode('utf-8')

    return encoded_str
