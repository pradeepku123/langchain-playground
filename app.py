import getpass
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage

os.environ["LANGCHAIN_TRACING_V2"] = "true"
# Load environment variables from a .env file
load_dotenv()

# Get the LANGCHAIN_API_KEY from the environment variables
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
print("LANGCHAIN_API_KEY Key is set to", os.environ["LANGCHAIN_API_KEY"])

os.environ["GROQ_API_KEY"] =os.getenv("GROQ_API_KEY")
print("GROQ_API_KEY Key is set to", os.environ["GROQ_API_KEY"])


model = ChatGroq(model="llama3-8b-8192")

print(model.invoke([HumanMessage(content="i am pradeep")]).content)



