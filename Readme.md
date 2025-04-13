# Summarizer

The **Summarizer** is a Python-based project designed to efficiently summarize text data. It provides tools and algorithms to extract meaningful summaries from large volumes of text, making it ideal for applications like document summarization, news processing, and more.

---

## Features

- **Efficient Text Summarization**: Quickly generates summaries for input text using advanced algorithms.
- **Customizable**: Supports parameter tuning for personalized summarization results.
- **Extensible Framework**: Can be integrated with other applications or services for automated workflows.
- **Makefile Integration**: Simplifies setup, testing, and other common tasks.

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Usage](#usage)
5. [Makefile Commands](#makefile-commands)
6. [Contributing](#contributing)
7. [License](#license)

---

## Getting Started

This section will guide you through setting up the project on your local machine.

---

## Installation

1. **Clone the Repository**  
   Clone the repository to your local machine:
   ```bash
   git clone https://github.com/news-on-blockchain/summarizer.git
   cd summarizer
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**  
   Create a virtual environment to isolate dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**  
   Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

1. **Custom Settings**  
   Modify the `config.py` or relevant configuration files to adjust settings such as summarization parameters or model paths.

---

## Usage

1. **Run the Summarizer**  
   Use the main script to summarize text:
   ```bash
   python main.py --input input.txt --output summary.txt
   ```

2. **Example Commands**  
   - Summarize a text from api endpoint:
     endpoint: `http://localhost:8000`
     method: `POST`
     type: `JSON`
     sample input:
     ```json
     {"text": "LangChain is a framework designed to simplify the creation of applications using large language models (LLMs). It provides modular components for managing prompts, interfacing with models, chaining sequences of calls, adding memory, and enabling agents. FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. Combining them allows developers to quickly deploy LLM-powered web services. Llama 3.1 is the latest iteration of Meta AI large language models, known for its improved performance and reasoning capabilities compared to its predecessors. Using Llama 3.1 via Ollama provides a way to run powerful models locally." }
    ```
3. **Output**  
   ```json
    {summary: "text summary"}
   ```

---

## Makefile Commands

This repository includes a `Makefile` to simplify common tasks. Below are the available commands:

- **Install Dependencies**:
  ```bash
  make install
  ```
- **Run Tests**:
  ```bash
  make test
  ```
- **Lint Code**:
  ```bash
  make lint
  ```
- **Clean Build Files**:
  ```bash
  make clean
  ```

---

## Contributing

We welcome contributions to improve the Summarizer! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to your forked repository:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request in the main repository.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements

- Thanks to the contributors who made this project possible.
