# Auto README Generator (自動 README 生成器)

## 專案簡介

`Auto README Generator` 是一個強大且易於使用的 Python 工具，旨在自動化 GitHub 專案的 `README.md` 檔案生成過程。它能掃描您的專案目錄結構和部分文件內容，並利用 Google Gemini API 或 OpenAI API 的強大能力，為您的專案生成一份清晰、專業且格式良好的 README 文件。

此工具特別適合開發者：

  * 快速為新專案建立基礎 README。
  * 為現有專案更新或補充 README 內容。
  * 節省手動撰寫 README 的時間和精力。


## 主要功能

  * **智慧掃描**：自動分析專案目錄結構、檔案名稱及部分內容，以提供 AI 模型豐富的上下文。
  * **多模型支援**：
      * **Gemini API**：利用 Google 最新的生成式 AI 模型。
      * **OpenAI API**：支援 GPT 系列模型，提供高品質的內容生成。
  * **命令行介面 (CLI)**：提供簡潔的命令行指令，方便整合到您的開發工作流程中。
  * **自訂輸出檔名**：您可以指定生成的 README 檔案名稱，例如 `README.md` 或 `my_project_readme.md`。


## 安裝指南

本工具可透過 `pip` 安裝，強烈建議在**虛擬環境**中進行安裝。

1.  **建立虛擬環境** (如果尚未建立)：
    開啟您的終端機或命令提示字元，並導航到您希望放置此工具的目錄（例如 `~/Projects/`）。然後執行以下指令：

    ```bash
    python3 -m venv .venv
    ```

    這將在當前目錄下創建一個名為 `.venv` 的虛擬環境資料夾。

2.  **啟動虛擬環境**：

      * **macOS / Linux (Bash/Zsh)**:
        ```bash
        source ./.venv/bin/activate
        ```
      * **Windows (PowerShell)**:
        ```powershell
        .\.venv\Scripts\activate
        ```

    成功啟動後，您的終端機提示符號前面會顯示 `(.venv)`，表示您已進入虛擬環境。


3.  **安裝工具**：
    在虛擬環境**已啟動**的狀態下，執行以下指令來安裝本工具。

      * **從本地檔案安裝 [(從 GitHub 下載了 `.whl` 或 `.tar.gz` 檔案)](https://github.com/szweijin/auto-readme-gen/releases/tag/v0.1.0)**：
        
        假設您已下載 `auto_readme_gen-0.1.0-py3-none-any.whl` 到您的 `~/Downloads` 目錄：
        ```bash
        pip install ~/Downloads/auto_readme_gen-0.1.0-py3-none-any.whl
        ```
      * **開發模式安裝 (如果您從 GitHub 克隆了原始碼)**：
        導航到 `auto-readme-gen` 專案的根目錄（即 `setup.py` 所在的目錄），然後執行：
        ```bash
        pip install -e .
        ```
        這種模式允許您修改原始碼而無需重新安裝。


## API 金鑰設定

本工具需要您的 Gemini 或 OpenAI API 金鑰才能運作。請將您的 API 金鑰設定為環境變數。**強烈建議您在您要生成 README 的 GitHub 專案根目錄下建立一個 `.env` 檔案來存放這些金鑰。**

在您的專案根目錄下建立一個名為 `.env` 的檔案，並填入以下內容（請替換為您實際的金鑰）：

```
# .env (放在您要生成 README 的專案根目錄下，例如 `my-awesome-project/.env`)
GEMINI_API_KEY="您的Gemini API 金鑰"
OPENAI_API_KEY="您的OpenAI API 金鑰"
```

**重要提示**：**請將 `.env` 檔案加入您專案的 `.gitignore` 中，確保您的 API 金鑰不會被上傳到 GitHub！**


## 使用方式

在您的虛擬環境中，您可以使用以下指令來生成 README：

### 使用 Gemini API 生成 README

```bash
gen-readme-gemini <您的專案路徑> [--output <輸出檔名>]
```

  * `<您的專案路徑>`：必填，您希望生成 README 的 GitHub 專案的根目錄路徑。
      * **範例 (在 macOS/Linux 上，生成當前目錄的 README)**：
        ```bash
        gen-readme-gemini . --output README.md
        ```
      * **範例 (在 Windows 上，生成指定路徑的 README)**：
        ```bash
        gen-readme-gemini "C:\Users\YourUser\Documents\my-awesome-project" --output README.md
        ```
  * `--output <輸出檔名>`：可選，預設為 `README.md`。您可以指定不同的輸出檔名。

### 使用 OpenAI API 生成 README

```bash
gen-readme-openai <您的專案路徑> [--output <輸出檔名>] [--model <OpenAI 模型名稱>]
```

  * `<您的專案路徑>`：必填，同上。

  * `--output <輸出檔名>`：可選，預設為 `README.md`。

  * `--model <OpenAI 模型名稱>`：可選，預設為 `gpt-3.5-turbo`。您可以指定其他模型，例如 `gpt-4`。

      * **範例 (生成當前目錄的 README)**：
        ```bash
        gen-readme-openai . --output README.md
        ```
      * **範例 (指定 GPT-4 模型)**：
        ```bash
        gen-readme-openai "/path/to/your/project" --output README.md --model gpt-4
        ```


## 專案結構概述

```
auto-readme-gen/
├── src/
│   └── autoreadmegen/
│       ├── __init__.py           # 套件初始化文件
│       ├── generate_gemini.py    # Gemini API 整合及命令行邏輯
│       └── generate_openai.py    # OpenAI API 整合及命令行邏輯
├── .env.example                  # 環境變數範本
├── setup.py                      # Python 套件設定及打包文件
└── requirements.txt              # 專案依賴套件列表
```


## 貢獻指南

歡迎任何形式的貢獻！如果您有任何改進建議、功能請求或發現 Bug，請隨時透過 GitHub Issues 或 Pull Requests 提出。


## 版權宣告

本專案採用 MIT 授權協議 - 詳情請見 `LICENSE` 檔案。
