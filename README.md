# 📚 PDF-Conv 💬

Welcome to **PDF-Conv**, a Streamlit-based application that allows you to upload multiple PDF files and interact with them through a conversational interface. 🚀

## 🌟 Features

- Upload multiple PDF documents 📄
- Extract text from PDFs and split into manageable chunks 🧩
- Create vector store from text chunks using Google Palm embeddings 🔍
- Conversational retrieval chain for interacting with PDF content 🤖
- Beautiful and user-friendly interface 🎨

## 📋 Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or later 🐍
- Streamlit
- PyPDF2
- Langchain
- Google Generative AI
- FAISS

## 🛠️ Installation

1. Clone the repo
    ```sh
    git clone https://github.com/silentkiller18/pdf-conv.git
    ```
2. Navigate to the project directory
    ```sh
    cd pdf-conv
    ```
3. Install required packages
    ```sh
    pip install -r requirements.txt
    ```

## 🚀 Usage

1. Set up your Google API key
    ```python
    os.environ['GOOGLE_API_KEY'] = 'YOUR_GOOGLE_API_KEY'
    ```
2. Run the Streamlit application
    ```sh
    streamlit run app.py
    ```

3. Open your web browser and go to `http://localhost:8501`

4. Upload your PDF files and start interacting with the content! 🗂️

## 🌐 Deployment on AWS EC2

1. **Launch an EC2 Instance**
    - Go to the EC2 Dashboard and click "Launch Instance".
    - Choose an Amazon Machine Image (AMI), such as the latest Ubuntu Server.
    - Select an instance type, like t2.micro for free tier.
    - Configure instance details, add storage, and configure security groups to allow HTTP (port 80) and HTTPS (port 443).
    - Review and launch the instance.

2. **Connect to Your Instance**
    - Use SSH to connect to your instance.
    ```sh
    ssh -i /path/to/your-key-pair.pem ubuntu@your-ec2-public-dns
    ```

3. **Install Dependencies**
    - Update package lists and install Python, pip, and git.
    ```sh
    sudo apt-get update
    sudo apt-get install python3-pip git
    ```

4. **Clone the Repository and Install Python Packages**
    ```sh
    git clone https://github.com/silentkiller18/pdf-conv.git
    cd pdf-conv
    pip3 install -r requirements.txt
    ```

5. **Set Up Environment Variable**
    - Add your Google API key to the environment.
    ```sh
    echo "export GOOGLE_API_KEY='YOUR_GOOGLE_API_KEY'" >> ~/.bashrc
    source ~/.bashrc
    ```

6. **Run the Streamlit Application**
    ```sh
    streamlit run app.py --server.port 80
    ```

7. **Access Your Application**
    - Open your web browser and navigate to `http://your-ec2-public-dns`

## 📸 Screenshots

![Screenshot 1]![image](https://github.com/silentkiller18/PDF-Conv/assets/89922781/0a087bf8-6321-45ab-b0fc-e49407aa68a8)



## 💡 How It Works

1. **Upload PDFs**: Users can upload multiple PDF files through the sidebar.
2. **Text Extraction**: Extracts text from each PDF file.
3. **Text Splitting**: Splits the extracted text into chunks for better processing.
4. **Vector Store Creation**: Creates a vector store using Google Palm embeddings.
5. **Conversational Interface**: Users can ask questions about the PDF content and receive responses.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/silentkiller18/pdf-conv/issues).

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgements

- [Streamlit](https://streamlit.io/)
- [PyPDF2](https://pypdf2.readthedocs.io/)
- [Langchain](https://github.com/langchain-ai/langchain)
- [Google Generative AI](https://cloud.google.com/ai-platform/generative-ai)
- [FAISS](https://github.com/facebookresearch/faiss)

## 📬 Contact

adarshraj@duck.com

Project Link: [https://github.com/silentkiller18/pdf-conv](https://github.com/silentkiller18/pdf-conv)

---

⭐️ Don't forget to give the project a star if you found it useful! ⭐️
