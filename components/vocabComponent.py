import tkinter
import tkinter.messagebox
import customtkinter
import vocab

class VocabComponent(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid(row=0, column=1, padx=(5, 0), pady=(5, 0), rowspan=4,sticky="nsew")

        self.button0 = customtkinter.CTkButton(self, command=self.button_click("0"))
        self.button0.grid(row=0, column=0, padx=20, pady=10)


        self.button1 = customtkinter.CTkButton(self, command=self.button_click("1"))
        self.button1.grid(row=0, column=1, padx=20, pady=10)

        self.button2 = customtkinter.CTkButton(self, command=self.button_click("2"))
        self.button2.grid(row=1, column=0, padx=20, pady=10)

        self.button3 = customtkinter.CTkButton(self, command=self.button_click("3"))
        self.button3.grid(row=1, column=1, padx=20, pady=10)

    def button_click(self, buttonNum):
        print(buttonNum)