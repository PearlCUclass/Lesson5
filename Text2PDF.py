# 導入 FPDF 類別從 fpdf 模組中
from fpdf import FPDF

# 指定要轉換的文本檔案路徑
file_path = r"LV2/FileConverter/text_file.txt"

# 創建一個新的 FPDF 對象
pdf = FPDF()

# 打開文本文件並讀取其內容
with open(file_path, "r") as file:
    text = file.read()

# 添加一個新頁到 PDF 中
pdf.add_page()

# 設定字型和字型大小
pdf.set_font("Arial", "B", 12)

# Write the text to the PDF
pdf.write(6, text)

# 儲存 PDF
pdf.output(r"LV2/FileConverter/text_file.pdf")
