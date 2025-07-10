
# Gemini OCR 腳本

這是一個 Python 腳本，使用 Google Gemini Pro Vision API 對圖片進行光學字元辨識 (OCR)，並將結果儲存為 `.txt` 和 `.docx` 檔案。

## ✨ 功能

- 使用強大的 Gemini Pro Vision 模型進行高準確率的文字辨識。
- 支援多種常見圖片格式 (PNG, JPEG, WEBP 等)。
- 自動將辨識結果儲存為純文字 (`.txt`) 檔案。
- 自動將辨識結果儲存為 Word (`.docx`) 檔案，方便後續編輯。
- 透過命令列介面操作，簡單易用。

## 🚀 事前準備

在執行此腳本之前，請確保您已完成以下設定。

### 1. 取得 Google Gemini API 金鑰

- 前往 [Google AI for Developers](https://makersuite.google.com/app/apikey) 網站。
- 點擊 **"Create API key"** 來產生您的專屬金鑰。

### 2. 安裝 Python 函式庫

開啟您的終端機或命令提示字元，然後執行以下指令來安裝必要的 Python 套件：

```bash
pip install google-generativeai pillow python-docx python-dotenv
```

### 3. 設定 API 金鑰

1.  在專案資料夾中，您會找到一個名為 `.env` 的檔案。
2.  用文字編輯器打開 `.env` 檔案。
3.  將 `YOUR_API_KEY_HERE` 替換成您在步驟 1 中取得的真實 Gemini API 金鑰，然後儲存檔案。

    ```
    GEMINI_API_KEY="替換成您的API金鑰"
    ```

## 🛠️ 如何使用

1.  **準備圖片**
    -   在 `gemini_ocr.py` 所在的目錄下，找到 (或建立) 一個名為 `input` 的資料夾。
    -   將所有您想要辨識的圖片檔案 (如 `.png`, `.jpg` 等) 放入 `input` 資料夾中。

2.  **執行腳本**
    -   開啟終端機或命令提示字元。
    -   使用 `cd` 指令切換到 `gemini_ocr.py` 所在的目錄。
    -   直接執行以下指令，不需要再提供任何路徑：
        ```bash
        python gemini_ocr.py
        ```

3.  **檢查結果**
    -   腳本會自動處理 `input` 資料夾中的所有圖片。
    -   辨識完成後，對應的 `.txt` 和 `.docx` 檔案會被儲存到 `output` 資料夾內。

## 📄 輸出

腳本執行成功後，會在原始圖片所在的資料夾中，產生兩個新檔案：

- `[原始檔名].txt`
- `[原始檔名].docx`

例如，若您辨識的檔案是 `invoice.png`，則會產生 `invoice.txt` 和 `invoice.docx`。
