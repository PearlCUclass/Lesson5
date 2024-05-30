# 從 Python Imaging Library (PIL) 庫中匯入 Image 模組，用於圖片的處理及操作
from PIL import Image

# 圖片的路徑列表
# 這裡列出了要轉換為 PDF 的圖片路徑
image_paths = ["image1.png", "image2.jpg", "image3.bmp"]

# 創建一個空列表來存放 Image 物件
# 用來存儲打開並轉換後的圖片物件
images = []

# 遍歷圖片路徑，打開每個圖片並轉換為 RGB 模式，然後添加到列表中
# 對於每個圖片路徑，打開圖片並轉換為 RGB 模式（因為 PDF 不支持透明度），然後添加到 images 列表中
for image_path in image_paths:
    # 打開圖片並轉換為 RGB 模式
    img = Image.open(image_path).convert("RGB")
    # 將轉換後的圖片添加到列表中
    images.append(img)

# 設置輸出 PDF 文件的路徑
# 指定輸出 PDF 文件的名稱和路徑
output_pdf_path = "combined_output.pdf"

# 使用第一張圖片作為基礎，並將其他圖片附加到 PDF 文件中
# 檢查 images 列表是否有圖片，如果有，將第一張圖片保存為 PDF，並將其他圖片附加到同一 PDF 文件中
if images:
    # 保存為 PDF 並附加其他圖片
    images[0].save(output_pdf_path, save_all=True, append_images=images[1:])
else:
    # 如果沒有圖片，印出錯誤訊息
    print("沒有找到任何圖片。")
