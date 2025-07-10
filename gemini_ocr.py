import os
import sys
import pathlib
import google.generativeai as genai
from PIL import Image
import docx
from dotenv import load_dotenv

def perform_ocr(image_path, model):
    """
    使用 Gemini API 對指定的圖片檔案進行 OCR。

    Args:
        image_path (pathlib.Path): 圖片檔案的路徑物件。
        model (genai.GenerativeModel): 已初始化的 Gemini 模型。

    Returns:
        str: 辨識出來的文字，如果失敗則返回 None。
    """
    try:
        print(f"  - 正在開啟圖片檔案: {image_path.name}")
        img = Image.open(image_path)

        prompt = "請對這張圖片進行OCR，提取所有可辨識的文字。請直接輸出文字內容，不要包含任何額外的說明或標題。"

        print("  - 正在呼叫 Gemini API 進行辨識...")
        response = model.generate_content([prompt, img])
        
        if response.prompt_feedback.block_reason:
            print(f"  - 錯誤：由於 {response.prompt_feedback.block_reason.name}，請求被阻擋。")
            return None

        print("  - 辨識成功。")
        return response.text

    except Exception as e:
        print(f"  - 處理檔案 {image_path.name} 時發生錯誤：{e}")
        return None

def save_results(text_content, txt_path, docx_path):
    """
    將文字內容儲存為 .txt 和 .docx 檔案。
    """
    try:
        print(f"  - 正在儲存 TXT 檔案至: {txt_path}")
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(text_content)
    except Exception as e:
        print(f"  - 儲存 TXT 檔案時發生錯誤: {e}")

    try:
        print(f"  - 正在儲存 Word 檔案至: {docx_path}")
        doc = docx.Document()
        doc.add_paragraph(text_content)
        doc.save(docx_path)
        print("  - 檔案儲存成功。")
    except Exception as e:
        print(f"  - 儲存 Word 檔案時發生錯誤: {e}")

def main():
    """
    主執行函式。
    """
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "YOUR_API_KEY_HERE":
        print("錯誤：找不到或尚未設定 GEMINI_API_KEY。")
        print("請在 .env 檔案中設定您的 API 金鑰後再執行此腳本。")
        sys.exit(1)
    
    try:
        print("正在設定 Gemini API...")
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-pro')
        print("Gemini API 設定成功。")
    except Exception as e:
        print(f"初始化 Gemini API 時發生錯誤: {e}")
        sys.exit(1)

    script_dir = pathlib.Path(__file__).parent
    input_folder_path = script_dir / 'input'
    output_folder_path = script_dir / 'output'

    for folder_path in [input_folder_path, output_folder_path]:
        if not folder_path.is_dir():
            print(f"未找到 '{folder_path.name}' 資料夾，正在建立中...")
            folder_path.mkdir()
            print(f"資料夾已建立於: {folder_path}")

    if not any(input_folder_path.iterdir()):
         print("請將您要辨識的圖片檔案放入 'input' 資料夾，然後重新執行此腳本。")
         sys.exit(0)

    supported_extensions = ['.png', '.jpg', '.jpeg', '.webp', '.bmp', '.gif']
    image_files = [f for f in input_folder_path.iterdir() if f.is_file() and f.suffix.lower() in supported_extensions]

    if not image_files:
        print(f"在 '{input_folder_path}' 資料夾中找不到任何支援的圖片檔案。")
        sys.exit(0)

    print(f"\n在資料夾 {input_folder_path.name} 中找到 {len(image_files)} 張圖片，開始批次處理...\n")

    for file_path in image_files:
        print(f"正在處理檔案: {file_path.name}")
        ocr_result = perform_ocr(file_path, model)

        if ocr_result:
            output_stem = output_folder_path / file_path.stem
            txt_output_path = output_stem.with_suffix('.txt')
            docx_output_path = output_stem.with_suffix('.docx')
            
            save_results(ocr_result, txt_output_path, docx_output_path)
            print(f"檔案 {file_path.name} 處理完成.\n")
        else:
            print(f"無法取得檔案 {file_path.name} 的 OCR 辨識結果.\n")

    print("所有圖片處理完畢.")

if __name__ == "__main__":
    main()