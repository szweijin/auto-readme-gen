import os
import argparse
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv() # Load environment variables

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def summarize_project_structure(project_path):
    """
    Scans the project directory and summarizes its structure and key files.
    """
    structure_summary = []
    ignore_dirs = [".git", "__pycache__", "node_modules", ".venv", ".env"]
    ignore_files = ["README.md", ".gitignore", "LICENSE"]

    for root, dirs, files in os.walk(project_path):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]

        level = root.replace(project_path, '').count(os.sep)
        indent = ' ' * 4 * level
        structure_summary.append(f"{indent}{os.path.basename(root)}/")

        for f in files:
            if f not in ignore_files:
                file_path = os.path.join(root, f)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                        content_preview = file.read(200).strip()
                    structure_summary.append(f"{indent}    - {f} (Preview: '{content_preview[:50]}...')")
                except Exception:
                    structure_summary.append(f"{indent}    - {f} (Binary or unreadable)")

    return "\n".join(structure_summary)

def generate_readme_gemini_content(project_summary, project_name): # Renamed for clarity within the module
    """
    Generates README.md content using Gemini API.
    """
    if not GEMINI_API_KEY:
        print("Error: Gemini API Key not set. Please check your .env file.")
        return None

    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
    except Exception as e:
        print(f"Error configuring Gemini API or model: {e}")
        print("Please ensure 'google-generativeai' is installed and your API key is valid.")
        return None

    prompt = f"""
    Please generate a comprehensive README.md for a GitHub project.
    The project name is '{project_name}'.
    Here is a summary of the project structure and some file contents:

    {project_summary}

    The README should include:
    1.  A clear, concise title.
    2.  A brief project description.
    3.  Features.
    4.  Installation instructions (assuming Python/pip requirements).
    5.  Usage examples.
    6.  Project structure overview.
    7.  Contributing guidelines (brief).
    8.  License (MIT or similar, general placeholder).
    Use Markdown formatting. Ensure the content is well-structured and easy to read.
    """
    print("Generating README using Gemini API...")
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error generating README with Gemini: {e}")
        return None

def run_gemini_cli(): # This will be the entry point
    parser = argparse.ArgumentParser(description="Generate a README.md for a GitHub project using Gemini API.")
    parser.add_argument("project_path", type=str, help="Path to the GitHub project directory.")
    parser.add_argument("--output", type=str, default="README.md",
                        help="Output file name for the README.md (e.g., README.md or my_readme.md).")

    args = parser.parse_args()

    project_path = os.path.abspath(args.project_path)
    if not os.path.isdir(project_path):
        print(f"Error: Project path '{project_path}' is not a valid directory.")
        return

    project_name = os.path.basename(project_path)
    print(f"Scanning project: {project_name} at {project_path}")
    project_summary = summarize_project_structure(project_path)

    readme_content = generate_readme_gemini_content(project_summary, project_name)

    if readme_content:
        output_path = os.path.join(project_path, args.output)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(readme_content)
        print(f"\nSuccessfully generated {args.output} at: {output_path}")
    else:
        print("\nFailed to generate README.md.")