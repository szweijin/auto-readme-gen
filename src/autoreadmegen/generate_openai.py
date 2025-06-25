import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv() # Load environment variables

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

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

def generate_readme_openai_content(project_summary, project_name, model_name="gpt-3.5-turbo"): # Renamed for clarity
    """
    Generates README.md content using OpenAI API.
    """
    if not OPENAI_API_KEY:
        print("Error: OpenAI API Key not set. Please check your .env file.")
        return None

    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
    except Exception as e:
        print(f"Error initializing OpenAI client: {e}")
        print("Please ensure 'openai' is installed and your API key is valid.")
        return None

    prompt = f"""
    請為這個 GitHub 專案生成一份**繁體中文**的完整 README.md。
    專案名稱是 '{project_name}'。
    這是專案結構與部分檔案內容的摘要：

    {project_summary}

    README 應包含以下項目：
    1.  清晰簡潔的標題。
    2.  簡短的專案描述。
    3.  主要功能。
    4.  安裝指南。
    5.  使用說明。
    6.  專案結構概述。
    7.  功能概述。
    8.  技術棧。
    9.  貢獻指南（簡要說明）。
    10.  版權宣告（例如 MIT 或類似的通用範本）。
    請使用 Markdown 格式。確保內容結構良好且易於閱讀。
    """
    print(f"Generating README using OpenAI API ({model_name})...")
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant for generating GitHub README files."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating README with OpenAI: {e}")
        return None

def run_openai_cli(): # This will be the entry point
    parser = argparse.ArgumentParser(description="Generate a README.md for a GitHub project using OpenAI API.")
    parser.add_argument("project_path", type=str, help="Path to the GitHub project directory.")
    parser.add_argument("--output", type=str, default="README.md",
                        help="Output file name for the README.md (e.g., README.md or my_readme.md).")
    parser.add_argument("--model", type=str, default="gpt-3.5-turbo",
                        help="Specify OpenAI model (e.g., 'gpt-4', 'gpt-3.5-turbo').")

    args = parser.parse_args()

    project_path = os.path.abspath(args.project_path)
    if not os.path.isdir(project_path):
        print(f"Error: Project path '{project_path}' is not a valid directory.")
        return

    project_name = os.path.basename(project_path)
    print(f"Scanning project: {project_name} at {project_path}")
    project_summary = summarize_project_structure(project_path)

    readme_content = generate_readme_openai_content(project_summary, project_name, args.model)

    if readme_content:
        output_path = os.path.join(project_path, args.output)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(readme_content)
        print(f"\nSuccessfully generated {args.output} at: {output_path}")
    else:
        print("\nFailed to generate README.md.")