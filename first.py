# 引入 tkinter 模組
import tkinter as tk

# 自訂函數
def hello():
    print("Hello, world.")

# 建立主視窗 Frame
window = tk.Tk()

# 設定視窗標題
window.title('Hello World')

# 設定視窗大小為 300x100，視窗（左上角）在螢幕上的座標位置為 (250, 150)
window.geometry("300x100+250+150")

# 建立按鈕
button = tk.Button(window,          # 按鈕所在視窗
                   text = 'Hello',  # 顯示文字
                   command = hello) # 按下按鈕所執行的函數

# 以預設方式排版按鈕
button.pack()

# 執行主程式
window.mainloop()