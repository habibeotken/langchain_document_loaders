import os
import gradio as gr
from dotenv import load_dotenv

# LangChain bileşenleri
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain

# Gemini entegrasyonu için özel paket
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI

# .env dosyasından API anahtarını yükle
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Embedding ve LLM modelini tanımla
embedding = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=api_key
)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key
)

# Dokümanı yükleyip vektör veritabanına dönüştür
def process_document(file_path):
    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(documents)
    vectorstore = FAISS.from_documents(split_docs, embedding)
    return vectorstore

# Soru-cevap işlemi
def ask_question(file, question):
    vectorstore = process_document(file.name)
    docs = vectorstore.similarity_search(question)
    chain = load_qa_chain(llm, chain_type="stuff")
    result = chain.run(input_documents=docs, question=question)
    return result

# Gradio arayüzü
interface = gr.Interface(
    fn=ask_question,
    inputs=[
        gr.File(label="Belge (TXT)", file_types=[".txt"]),
        gr.Textbox(label="Sorunuz")
    ],
    outputs="text",
    title="Gemini 2.5 ile Dokümana Soru Sor",
    description="Bir metin dosyası yükleyin ve doğal dilde sorular sorun. Yanıtlar Gemini 2.5 Flash tarafından üretilir."
)

# Uygulamayı başlat
if __name__ == "__main__":
    interface.launch()
