from guizero import App, Text, Box, Picture

app = App(title = "Self-introduction")
header_box = Box(app, align = "top", width = "fill")
text = Text(header_box, text = "Họ và tên: Hoàng Đức Bảo Lâm \n"
                                "Tuổi: 16", color = "blue")

self_pic = Picture(app, image = "gifts_lmao.png")
self_pic.resize(300, 300)

bottom_box = Box(app, align = "bottom", width = "fill")
newer_text = Text(bottom_box, text = "Giới tính: Nam \n"
                                    "Trường : Trường THPT Lý Tự Trọng", color = "red")

app.display()