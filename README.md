# auto-readme-gen：自動生成 README 檔案

本專案 `auto-readme-gen` 旨在自動化生成 README 檔案，讓您能更輕鬆地維護您的專案文件。  透過整合 Gemini 和 OpenAI 等大型語言模型，您可以快速生成結構清晰、內容完整的 README，節省大量時間和精力。


## 主要功能

* 自動生成 README 檔案，包含標題、描述、功能、安裝指南、使用說明、專案結構、技術棧等資訊。
* 支援 Gemini 和 OpenAI API，提供多種選擇。
* 可自定義模板，滿足不同專案的需求。
* 簡潔易用的命令列介面。


## 安裝指南

1. **複製本專案:**  您可以透過 Git 將本專案複製到您的本地機器：

   ```bash
   git clone https://github.com/[YourGitHubUsername]/auto-readme-gen.git
   ```

2. **安裝依賴項:**  使用 pip 安裝必要的套件：

   ```bash
   cd auto-readme-gen
   pip install -r requirements.txt
   ```

3. **設定 API 金鑰:**  在 `.env` 檔案中填寫您的 Gemini 和 OpenAI API 金鑰。請參考 `.env.example` 檔案。


## 使用說明

1. **執行指令:** 使用以下指令執行程式，並指定要使用的 API（gemini 或 openai）：

   ```bash
   python -m autoreadmegen.generate_gemini  # 使用 Gemini API
   python -m autoreadmegen.generate_openai  # 使用 OpenAI API
   ```

2. **輸出:** 程式會在當前目錄下生成一個 `README.md` 檔案。


## 專案結構概述

```
auto-readme-gen/
├── README.md             (此檔案)
├── requirements.txt      (專案依賴項)
├── setup.py              (安裝腳本)
├── .env                  (API 金鑰設定)
├── .env.example          (API 金鑰設定範例)
└── src/
    └── autoreadmegen/
        ├── generate_gemini.py (Gemini API 生成器)
        ├── generate_openai.py (OpenAI API 生成器)
        └── __init__.py        (套件初始化)
```


## 功能概述

`generate_gemini.py` 和 `generate_openai.py` 分別使用 Gemini 和 OpenAI API 生成 README 檔案內容。

這些檔案會根據您專案的程式碼結構和設定檔，自動生成不同的區段。


## 技術棧

* Python
* google-generativeai (適用於 Gemini API)
* openai (適用於 OpenAI API)
* python-dotenv (環境變數管理)


## 貢獻指南

歡迎貢獻程式碼！請提交 pull request，並確保您的程式碼符合 PEP 8 程式碼風格指南。


## 版權宣告

MIT License

Copyright (c) [Your Name/Organization]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
