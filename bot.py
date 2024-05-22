import os 
import retrieval
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
google_api_key = os.getenv('GOOGLE_API_KEY')


ret = retrieval.retriever


llm = ChatGoogleGenerativeAI(model = 'gemini-1.5-pro-latest', google_api_key=google_api_key)

template = """
You are a medical chatbot. First respond to greetings only if the user is greeting with you like hi , hello etc. Provide comprehensive suggestions based on the context. If context is not enough, ask for more information or search if you dont know , only provide factually correct information and suggestion. The chats need to be professional and helpful.
Context: {context}
Question: {question}

1. Lifestyle Changes:
2. Food Recommendations:
3. Exercise Suggestions:
4. Potential Medicines:

Helpful Answer:
"""
prompt_template = PromptTemplate.from_template(template=template)

set_ret = RunnableParallel(
    {"context": ret, "question": RunnablePassthrough()} 
)

rag_chain = set_ret |  prompt_template | llm | StrOutputParser()



