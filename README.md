# Chatbot de Vendedor de Peças de Informática

Este é um projeto de chatbot desenvolvido para atender clientes de uma loja de peças de informática. O bot utiliza inteligência artificial para responder perguntas com base em dados extraídos de documentos PDF e interagir por meio de uma interface web personalizada.

## Funcionalidades

- Respostas precisas com base em dados extraídos de arquivos PDF.
- Interface web amigável para comunicação com os clientes.
- Integração com o modelo **Mistral 7B** da Ollama para processamento de linguagem natural.
- Configuração utilizando **Flask** para o backend e **HTML/CSS** para o frontend.

## Tecnologias Utilizadas

- **Python**
- **Flask**: Framework para criação do backend.
- **LangChain**: Biblioteca para orquestração de modelos de IA e gerenciamento de dados.
- **Mistral 7B**: Modelo de linguagem natural utilizado para processar perguntas.
- **WSL Ubuntu 24**: Ambiente de desenvolvimento.
- **HTML/CSS**: Para a interface web.

## Requisitos de Instalação

1. **WSL (Windows Subsystem for Linux)** com Ubuntu 24 configurado.
2. **Python 3.9+**
3. **Ollama** instalado para rodar o modelo Mistral 7B.
4. Dependências do projeto (instaladas via `pip`).

## Como Executar o Projeto

1. Clone este repositório:

   ```bash
   git clone https://github.com/joaopaulomts/flask_chatbot_v1
   cd flask_chatbot_v1
   ```

2. Crie um ambiente virtual e ative-o:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

4. Inicie o servidor Flask:

   ```bash
   python app.py
   ```

5. Acesse a interface web no navegador:

   ```
   http://localhost:5000
   ```

## Estrutura do Projeto

```
.
├── app.py               # Arquivo principal do Flask
├── static/              # Arquivos estáticos (CSS, JS, imagens)
├── templates/           # Templates HTML
├── data/                # Diretório para armazenar os PDFs
├── requirements.txt     # Lista de dependências Python
└── README.md            # Documentação do projeto
```

## Extração de Dados de PDFs

Os dados relevantes para as respostas do chatbot são extraídos dos PDFs usando o LangChain, que estrutura as informações para o modelo Mistral 7B responder com precisão.
