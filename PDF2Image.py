from pdf2image import convert_from_path

# PDF 文件的路徑
pdf_path = r"C:\Users\pearl\OneDrive\文件\備課相關資料\Projects100\LV2\FileConverter\Example_2.pdf"

# 將 PDF 文件轉換為圖片
# 使用 convert_from_path 函數將 PDF 文件的每個頁面轉換為圖片
images = convert_from_path(pdf_path)

# 保存每個頁面為單獨的圖片檔
# 遍歷轉換後的每個圖片頁面，並保存為 PNG 格式
for i, image in enumerate(images):
    # 使用 save 方法儲存圖片
    # 檔名為 page_頁碼.png，例如 page_1.png，page_2.png
    image.save(f"page_{i + 1}.svg", "svg")
