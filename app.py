from flask import Flask, request, jsonify, render_template
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.llms import Ollama
from langchain.document_loaders import PyPDFLoader, DirectoryLoader

app = Flask(__name__)

# Configuração do Ollama
OLLAMA_BASE_URL = "http://localhost:11434"
MODELO_OLLAMA = "mistral"


# Carregar e processar PDFs
def carrega_e_processa_pdfs():
    loader = DirectoryLoader('dados/', glob="**/*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    embeddings = SentenceTransformerEmbeddings(model_name="all-mpnet-base-v2")
    db = FAISS.from_documents(texts, embeddings)
    return db


# Banco de dados vetorial
db = carrega_e_processa_pdfs()


@app.route("/testarconexao", methods=["GET"])
def testar_conexao():
    return jsonify({"status": "Servidor Flask ativo e funcional!"})


@app.route("/chat", methods=["GET"])
def chat():
    return render_template("index.html")  # Página do chat


@app.route("/ask", methods=["POST"])
def ask():
    try:
        user_question = request.json.get("question")
        if not user_question:
            return jsonify({"error": "A pergunta está vazia!"}), 400

        llm = Ollama(base_url=OLLAMA_BASE_URL, model=MODELO_OLLAMA)
        qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=db.as_retriever())
        resposta = qa.run(user_question)

        return jsonify({"response": resposta})
    except Exception as e:
        return jsonify({"error": f"Erro: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
