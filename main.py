import random
import customtkinter as ctk



app = ctk.CTk()
app.title("Slot")
app.geometry("400x400")

ans = []
i = 0
s = []

# ฟังก์ชั่นไว้ใช้สำหรับกดปุ่ม
# เมื่อกดจะเปลียนค่า stop_label ตามลำดับตัวที่กด
def click():
    global i
    stop_b = stop_button.cget("text")
    # ทำเงื่อนไขตรวจสอบข้อความบนปุ่ม
    # ถ้าข้อความบนปุ่มเป็น Reset
    # จะทำการเปลี่ยนข้อความบน stop_label เป็น stop0
    # แล้วก็เปลี่ยนข้อความบน stop_button เป็น Start เพื่อใช้เป็นข้อความอ้างอิงในการตรวจสอบเงือนไข
    if stop_b == "Reset":
        text = "stop0"
        stop_label.configure(text=text)
        score_label.configure(text=" ")
        stop_button.configure(text="Start")
    elif stop_b == "stop" or stop_b == "Start": 
        stop_button.configure(text="stop")
        i += 1
        if i > 3:
            i = 0
        text = "stop" + str(i)
        #print(s[-1][0], s[-1][1], s[-1][2])
        stop_label.configure(text=text)        

def slot():
    global s
    number = [0,1,2,3,4,5,6,7,8,9,"@","#"]
    stop = stop_label.cget("text") # ดึข้อความจาก stop_label เพื่อใช้อ้างอิง

    if stop == "stop0": 
        random1 = random.choice(number)
        random2 = random.choice(number)
        random3 = random.choice(number)
    elif stop == "stop1" or "stop1" in ans:
        random1 = s[-1][0]
        random2 = random.choice(number)
        random3 = random.choice(number)        
    elif stop == "stop2" or "stop2" in ans:
        random1 = s[-1][0]
        random2 = s[-1][1]
        random3 = random.choice(number) 
    elif stop == "stop3" or "stop3" in ans:
        random1 = s[-1][0]
        random2 = s[-1][1]
        random3 = s[-1][2]
        if random1 and random2 == random3:
            score_label.configure(text="Win",text_color="#FFDE59")
            stop_button.configure(text="Reset")
            i=1
            
        else:
            score_label.configure(text="Lose",text_color="#737373")
            stop_button.configure(text="Reset")
            i=1
            
    text = [str(random1), str(random2), str(random3)]
    s.append(text)        
    label.configure(text=text)
    label.after(500, slot)




label = ctk.CTkLabel(app, text="",
                     width=20,
                     height=20,
                     corner_radius=20,
                     fg_color="#7DFAB6",
                     font=('Arial', 40),
                     padx=30, pady=30)
label.pack()


stop_label = ctk.CTkLabel(app, text="stop0",
                          font=('Arial', 20),
                          pady=30)
stop_label.pack()

stop_button = ctk.CTkButton(app, text="stop", command=click,
                            font=('Arial', 20), fg_color="#7DFAB6",
                            corner_radius=30, border_width=2,
                            text_color="#007074")
stop_button.pack()

score_label = ctk.CTkLabel(app, text="",
                           font=('Arial', 60),
                           text_color="#FFDE59",
                           pady=20)
score_label.pack()

slot()
app.mainloop()
