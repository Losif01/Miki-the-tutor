# Miki the Tutor - RAG App with Ollama's Phi3 Model

<img width="852" height="317" alt="Screenshot From 2025-08-21 13-32-31" src="https://github.com/user-attachments/assets/5ba6ba80-2b3d-49c9-98ac-814ad75de4d4" />

Miki the Tutor is a Retrieval-Augmented Generation (RAG) application that uses Ollama's Phi3 model to provide intelligent tutoring based on the "Grokking Algorithms" book. The application is designed to work with PDF textbooks, with the current implementation focused on the popular algorithms book but easily extensible to other educational materials.

<img width="1920" height="1200" alt="Screenshot From 2025-08-21 13-29-53" src="https://github.com/user-attachments/assets/5c7974d8-ab62-45e8-97ab-53d1f89c4902" />

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
note that phi3's size is 2GB, which is why this project couldn't be hosted easily, i may consider API calls but this costs money you know
4. Place your PDF textbooks in the `/Data` directory

## Usage

1. Run the application:
   ```bash
   python -c "from ingestion.build_index import build_vector_index; build_vector_index()"    
   python main.py
   ```
   If you encounter any issues, run `debug_index.py` and it will show diagnosis and where exactly is the issue

2. The system will:
   - Process PDFs in the `/Data` directory
   - Create vector embeddings for semantic search
   - Launch the RAG interface

3. Ask questions about the textbook content through the interface

## Extending to Other Books

To use Miki with another textbook:
1. Place the PDF in the `/Data` directory
2. Re-run the application to process the new book

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
