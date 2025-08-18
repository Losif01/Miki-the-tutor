# Miki the Tutor - RAG App with Ollama's Phi3 Model

![RAG Architecture](https://miro.medium.com/v2/resize:fit:1400/1*6hFST5QNsc9kOn2q0oVt_w.png)

Miki the Tutor is a Retrieval-Augmented Generation (RAG) application that uses Ollama's Phi3 model to provide intelligent tutoring based on the "Grokking Algorithms" book. The application is designed to work with PDF textbooks, with the current implementation focused on the popular algorithms book but easily extensible to other educational materials.

## Features

- **PDF Document Processing**: Extracts and indexes text from PDF textbooks
- **Vector Embeddings**: Uses state-of-the-art embeddings for semantic search
- **Ollama Integration**: Leverages the lightweight Phi3 model for efficient local inference
- **RAG Architecture**: Combines retrieval of relevant passages with generative AI
- **Extensible Design**: Can be adapted to work with any PDF textbook in the `/Data` directory

## Requirements

- Python 3.8+
- Ollama (with Phi3 model installed)
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Losif01/Miki-the-tutor.git
   cd Miki-the-tutor
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up Ollama and pull the Phi3 model:
   ```bash
   ollama pull phi3
   ```

4. Place your PDF textbooks in the `/Data` directory

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. The system will:
   - Process PDFs in the `/Data` directory
   - Create vector embeddings for semantic search
   - Launch the RAG interface

3. Ask questions about the textbook content through the interface

## Configuration

Modify `config.py` to adjust:
- Chunk size for document processing
- Embedding model parameters
- Retrieval settings (number of passages to retrieve)
- Generation parameters (temperature, max tokens)

## Extending to Other Books

To use Miki with another textbook:
1. Place the PDF in the `/Data` directory
2. Update the book title in `config.py`
3. Re-run the application to process the new book

## Roadmap

- [ ] Add web interface
- [ ] Support for multiple books simultaneously
- [ ] Conversation history
- [ ] Citation of page numbers
- [ ] Performance optimizations

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

MIT License (see LICENSE file)