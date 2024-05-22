# main.py
from fastapi import FastAPI
from pydantic import BaseModel
#from text_processor import process_text
import bot


chain  = bot.rag_chain

def generate_response(text):
    print(f"Received text: {text}")  # Debug print
    response = chain.invoke(text)
    print(f"Generated response: {response}")  # Debug print
    return response


app= FastAPI()

class TextRequest(BaseModel):
    text: str

class TextResponse(BaseModel):
    processed_text: str

@app.post("/process_text", response_model=TextResponse)
def process_text_endpoint(request: TextRequest):
    output_text = generate_response(request.text)
    return TextResponse(processed_text=output_text)



if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))  # Default to 8000 if PORT is not set
    uvicorn.run(app, host="0.0.0.0", port=port)

# # main.py
# from fastapi import FastAPI
# from pydantic import BaseModel
# import bot

# chain = bot.rag_chain

# def generate_response(text):
#     print(f"Received text: {text}")  # Debug print
#     response = chain.invoke(text)
#     print(f"Generated response: {response}")  # Debug print
#     return response

# app = FastAPI()

# class TextRequest(BaseModel):
#     text: str

# class TextResponse(BaseModel):
#     processed_text: str

# @app.post("/process_text", response_model=TextResponse)
# def process_text_endpoint(request: TextRequest):
#     output_text = generate_response(request.text)
#     return TextResponse(processed_text=output_text)





























# import bot

# import io

# from fastapi import FastAPI , File , UploadFile
# from fastapi.middleware.cors import CORSMiddleware


# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.post("/app/{question}")
# async def get_answer(question: str):
#     print(question + " received")
#     return generate_response(question)




# chain  = bot.rag_chain

# def generate_response(text):
#     response = chain.invoke(text)
#     return response
