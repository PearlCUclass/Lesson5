# 匯入 pdfplumber 模組，用於處理 PDF檔
import pdfplumber


# 定義一個從 PDF檔中提取文字的函數
def extract_text_from_pdf(file_path):
    # 初始化一個空字串，用於儲存提取的文字
    text = ""
    # 使用 pdfplumber.open 方法打開指定路徑的 PDF檔，並將其命名為 pdf_file。
    # 當使用 pdfplumber.open() 方法打開一個 PDF檔時，會創建並返回一個 PDF() 類別的實例化物件。
    with pdfplumber.open(file_path) as pdf_file:
        # 使用PDF()物件的pages屬性取得PDF檔的所有頁面物件之列表，並遍歷 PDF檔中的每一頁
        for page in pdf_file.pages:
            # 使用 page.extract_text 方法提取頁面上的文字，並將其添加到 text 字串中
            text += page.extract_text()
    # 返回提取的完整文字內容
    return text


if __name__ == "__main__":
    # 指定PDF檔的路徑
    file_path = r"C:\Projects100\LV2\FileConverter\Example.pdf"
    # 呼叫 extract_text_from_pdf 函數，提取文字內容
    pdf_text = extract_text_from_pdf(file_path)
    # 輸出提取的文字
    print(pdf_text)
    # 將轉換後的文字寫入到一個新的文字檔中
    with open("LV2/FileConverter/Example.txt", "w", encoding="utf-8") as file:
        file.write(pdf_text)
