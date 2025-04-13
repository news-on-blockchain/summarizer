import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from langchain_community.llms.ollama import Ollama
from langchain.chains.summarize import load_summarize_chain
from langchain_core.prompts import PromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
import uvicorn

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

LLM_PROVIDER = Ollama(
    model="llama3.1",
    base_url="http://localhost:11434",
)
MODEL_NAME = "Llama 3.1 via Ollama" 

TEXT_SPLITTER = RecursiveCharacterTextSplitter(
    chunk_size=4000,
    chunk_overlap=200
)

class TextInput(BaseModel):
    """Request model for text input."""
    text: str = Field(..., min_length=1, description="The text to be summarized.")

class SummaryOutput(BaseModel):
    """Response model for the summary."""
    summary: str = Field(description="The generated summary.")
    model_used: str = Field(description="The name of the model used for summarization.")

app = FastAPI(
    title="LangChain Text Summarization API",
    description="API to summarize text using Llama 3.1 via LangChain.",
    version="1.0.0",
)

@app.post("/summarize", response_model=SummaryOutput)
async def summarize_text(request: TextInput):
    """
    Summarizes the input text using the configured Llama 3.1 model.

    Handles text splitting for longer inputs.
    """
    logger.info(f"Received summarization request with text length: {len(request.text)}")

    try:
        texts = TEXT_SPLITTER.split_text(request.text)
        docs = [Document(page_content=t) for t in texts]
        logger.info(f"Split text into {len(docs)} documents/chunks.")

        prompt_template = """Write a concise summary of the following text:

        "{text}"

        CONCISE SUMMARY:"""
        prompt = PromptTemplate.from_template(prompt_template)
        chain = load_summarize_chain(
            llm=LLM_PROVIDER,
            chain_type="stuff",
            prompt=prompt,
            verbose=False 
        )
        logger.info(f"Using summarization chain type: {chain._chain_type}")

        summary_result = await chain.ainvoke({"input_documents": docs})

        final_summary = summary_result.get("output_text", "Error: Could not extract summary.")
        logger.info(f"Successfully generated summary of length: {len(final_summary)}")

        return SummaryOutput(summary=final_summary, model_used=MODEL_NAME)

    except Exception as e:
        logger.error(f"Error during summarization: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred during processing: {e}"
        )

@app.get("/", summary="Root Endpoint", description="Basic API health check.")
async def read_root():
    """Provides a simple welcome message."""
    return {"message": "Welcome to the LangChain Summarization API with Llama 3.1!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)