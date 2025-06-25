from setuptools import setup, find_packages

setup(
    name="auto-readme-gen", # 套件名稱
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool to automatically generate README.md using Gemini or OpenAI APIs.",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/auto-readme-gen", # 替換為您的 GitHub 專案 URL
    package_dir={"": "src"}, # 指示 setuptools 在 src 目錄中尋找套件
    packages=find_packages(where="src"), # 自動尋找 src/ 下的所有套件
    install_requires=[
        "google-generativeai",
        "openai",
        "python-dotenv",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "gen-readme-gemini=autoreadmegen.generate_gemini:run_gemini_cli",
            "gen-readme-openai=autoreadmegen.generate_openai:run_openai_cli",
        ],
    },
)