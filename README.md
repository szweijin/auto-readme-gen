# auto-readme-gen

A command-line tool for automatically generating README files using Gemini and OpenAI APIs.

## Description

`auto-readme-gen` simplifies the process of creating README files.  It leverages the power of Gemini and OpenAI's large language models to generate comprehensive and informative README content based on your project's structure and code.  This saves you valuable time and ensures consistency across your projects.

## Features

* **Gemini API Support:** Generate README content using Google's Gemini API.
* **OpenAI API Support:** Generate README content using OpenAI's API. (Requires API key)
* **Flexible Configuration:** Easily configure API keys and other settings via environment variables.
* **Command-line Interface:** Simple and intuitive command-line usage.
* **Automated README generation:**  Reduces manual effort in creating README files.


## Installation

Ensure you have Python 3.7+ installed. Then, install `auto-readme-gen` using pip:

```bash
pip install -r requirements.txt
```

Alternatively, you can install directly from the source code:

```bash
git clone <repository_url>
cd auto-readme-gen
pip install .
```

## Usage

Before running the tool, set your API keys in a `.env` file (refer to `.env.example` for the correct format).  The tool supports two modes:

**Using Gemini:**

```bash
gen-readme-gemini
```

**Using OpenAI:**

```bash
gen-readme-openai
```

The generated README file will be output to the console. You can then redirect the output to a file if desired:

```bash
gen-readme-gemini > README.md
```


## Project Structure

```
auto-readme-gen/
├── .env              # API keys and environment variables (DO NOT COMMIT)
├── .env.example      # Example .env file
├── requirements.txt   # Project dependencies
├── setup.py          # Setup script
└── src/
    └── autoreadmegen/
        ├── generate_gemini.py  # Gemini API interaction
        ├── generate_openai.py  # OpenAI API interaction
        └── __init__.py         # Package initialization
    └── auto_readme_gen.egg-info/  # Build artifacts
```

`.idea` directory contains IDE-specific settings and is usually ignored in version control.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your changes.  Ensure your code follows PEP 8 style guidelines.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  (This license placeholder needs to be created in the actual repository).
