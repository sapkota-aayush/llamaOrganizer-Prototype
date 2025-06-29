# LlamaOrganizer-Prototype

> ⚠️ **Prototype Status**: This is a working prototype demonstrating core concepts for my main project. The full, production-ready LlamaOrganizer application is under active development and will be released soon.

A local AI-powered file organization assistant that converts natural language commands into structured JSON instructions, enabling automated file operations like listing, moving, copying, and deleting files.

## 🚀 Project Overview

This prototype demonstrates a system where:

- A local LLaMA-based AI model (via [Ollama](https://ollama.com)) runs entirely offline on your machine
- Users send natural language commands (e.g., "List all images in Pictures folder")
- The AI parses these commands into machine-readable JSON format
- The JSON response can be used to perform file operations programmatically

## 🛠️ Features Implemented

- **Local Ollama Integration**: `core/ollama_client.py` - Connects to local Ollama models for AI processing
- **REST API**: `api/server.py` - FastAPI server with `/parse` endpoint for command processing
- **File Operations**: `core/file_operator.py` - Scaffold for file management functions (list, move, copy, delete)
- **Testing Support**: Easy testing via Postman, curl, or any HTTP client

## 📂 Project Structure

```
llamaOrganizer-Prototype/
├── api/
│   └── server.py              # FastAPI application
├── core/
│   ├── ollama_client.py       # Ollama API client wrapper
│   └── file_operator.py       # File operation utilities
├── cli/
│   └── cli_app.py             # CLI interface (planned)
├── tests/
│   └── test_file_operator.py  # Unit tests (planned)
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com) installed and running locally
- A compatible LLaMA model (e.g., phi3, llama2, etc.)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/sapkota-aayush/llamaOrganizer-Prototype.git
   cd llamaOrganizer-Prototype
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # On Windows PowerShell:
   venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start Ollama model**
   ```bash
   ollama run phi3  # or your preferred model
   ```

5. **Start the FastAPI server**
   ```bash
   uvicorn api.server:app --reload --port 8080
   ```

## 🧪 Testing the API

### Using curl

```bash
curl -X POST http://127.0.0.1:8080/parse \
  -H "Content-Type: application/json" \
  -d '{"command": "List all images in Pictures folder"}'
```

### Using Postman

1. Create a new POST request
2. URL: `http://127.0.0.1:8080/parse`
3. Headers: `Content-Type: application/json`
4. Body (raw JSON):
   ```json
   {
     "command": "List all images in Pictures folder"
   }
   ```

### Example Commands to Test

- "List all images in Pictures folder"
- "Move all PDF files from Downloads to Documents"
- "Copy all text files from Desktop to Backup folder"
- "Delete all temporary files in Temp directory"

## 🔮 Next Steps & Roadmap

This prototype serves as the foundation for the main LlamaOrganizer project. Planned improvements include:

- **Enhanced JSON Parsing**: Improved prompt templates for more accurate command interpretation
- **File Operations Integration**: Connect parsed JSON to actual file management functions
- **CLI Interface**: Command-line tool for direct interaction
- **GUI Application**: User-friendly graphical interface
- **Advanced Features**: File deduplication, smart organization, batch operations
- **Production Features**: Error handling, logging, configuration management

## 🤝 Contributing

This is currently a prototype for my main project. However, if you're interested in the concept or have suggestions, feel free to:

- Open issues with feature requests or bug reports
- Fork the repository for your own experiments
- Reach out with questions or feedback

## 📝 License

This prototype is provided as-is for educational and demonstration purposes.

## 👨‍💻 Author

**Aayush Sapkota**

- Building the next generation of AI-powered file organization tools
- This prototype is part of a larger project in development
- Stay tuned for the complete, production-ready LlamaOrganizer application!

---

> **Note**: This prototype demonstrates the core architecture and AI integration concepts. The full LlamaOrganizer application will include comprehensive file management capabilities, improved AI models, and a polished user experience. 