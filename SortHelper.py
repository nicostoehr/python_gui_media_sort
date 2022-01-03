import tkinter
import os
import tkinter.messagebox

class GUI(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.master = master

        self.sortopt = tkinter.IntVar(value=0)

        self.pngopt = tkinter.IntVar(value=1)
        self.webpopt = tkinter.IntVar(value=1)
        self.jpgopt = tkinter.IntVar(value=1)
        self.jpegopt = tkinter.IntVar(value=1)

        self.l2 = tkinter.Label(master, text="What media should be sorted:", height=1, width=50)

        self.cb1 = tkinter.Checkbutton(master, text=".png", variable=self.pngopt, offvalue=0, onvalue=1)
        self.cb2 = tkinter.Checkbutton(master, text=".webp", variable=self.webpopt, offvalue=0, onvalue=1)
        self.cb3 = tkinter.Checkbutton(master, text=".jpg", variable=self.jpgopt, offvalue=0, onvalue=1)
        self.cb4 = tkinter.Checkbutton(master, text=".jpeg", variable=self.jpegopt, offvalue=0, onvalue=1)

        self.l1 = tkinter.Label(master, text="Input path to folder to sort:", height=1, width=50)
        self.t1 = tkinter.Text(master, height=1, width=50)

        self.l3 = tkinter.Label(master, text="How should the media be sorted:", height=1, width=50)
        self.rb1 = tkinter.Radiobutton(master, text="Name", variable=self.sortopt, value=1)
        self.rb2 = tkinter.Radiobutton(master, text="Name Rev", variable=self.sortopt, value=2)
        self.rb3 = tkinter.Radiobutton(master, text="Date", variable=self.sortopt, value=3)
        self.rb4 = tkinter.Radiobutton(master, text="Date Rev", variable=self.sortopt, value=4)
        self.rb5 = tkinter.Radiobutton(master, text="Size", variable=self.sortopt, value=5)
        self.rb6 = tkinter.Radiobutton(master, text="Size Rev", variable=self.sortopt, value=6)

        self.l4 = tkinter.Label(master, text="(optinal) Choose a name for the media", height=1, width=50)
        self.t2 = tkinter.Text(master, height=1, width=50)

        self.b1 = tkinter.Button(master, text="Sort!", height=3, width=56)
        self.b1["command"] = self.mediasort

        self.l2.pack(anchor="w")
        self.cb1.pack(anchor="w")
        self.cb2.pack(anchor="w")
        self.cb3.pack(anchor="w")
        self.cb4.pack(anchor="w")
        self.l1.pack(anchor="w")
        self.t1.pack(anchor="w")
        self.l3.pack(anchor="w")
        self.rb1.pack(anchor="w")
        self.rb2.pack(anchor="w")
        self.rb3.pack(anchor="w")
        self.rb4.pack(anchor="w")
        self.rb5.pack(anchor="w")
        self.rb6.pack(anchor="w")
        self.l4.pack(anchor="w")
        self.t2.pack(anchor="w")

        self.b1.pack(anchor="w")

    def rbdeselct(self):
        print("d")

    def mediasort(self):
        if self.sortopt.get() == 0: tkinter.messagebox.askokcancel(title="No option chosen", message="Please choose one of the sorting options")
        else:
            dir = self.t1.get("0.0","end")[0:-1]
            if dir != "":
                folder = os.listdir(dir)
                fcont = []
                for i in folder:
                    if self.pngopt.get() and i.endswith(".png"):
                        print(i)
                        fcont.append([i, os.path.getsize(dir + "\\" + i), os.path.getctime(dir + "\\" + i), ".png"])
                    elif self.webpopt.get() and i.endswith(".webp"):
                        print(i)
                        fcont.append([i, os.path.getsize(dir + "\\" + i), os.path.getctime(dir + "\\" + i), ".webp"])
                    elif self.jpgopt.get() and i.endswith(".jpg"):
                        print(i)
                        fcont.append([i, os.path.getsize(dir + "\\" + i), os.path.getctime(dir + "\\" + i), ".jpg"])
                    elif self.jpegopt.get() and i.endswith("jpeg"):
                        print(i)
                        fcont.append([i, os.path.getsize(dir + "\\" + i), os.path.getctime(dir + "\\" + i), ".jpeg"])

                tsort = self.sortopt.get()
                if tsort < 3:
                    if tsort == 1:
                        fcont.sort(key=lambda x: x[0])
                    else:
                        fcont.sort(key=lambda x: x[0], reverse=True)
                elif tsort < 5:
                    if tsort == 3:
                        fcont.sort(key=lambda x: x[1])
                    else:
                        fcont.sort(key=lambda x: x[1], reverse=True)
                else:
                    if tsort == 5:
                        fcont.sort(key=lambda x: x[2])
                    else:
                        fcont.sort(key=lambda x: x[2], reverse=True)

                tname = ""
                if self.t2.get("0.0","end").strip() != "": tname = self.t2.get("0.0","end").strip() + "_"

                len(fcont)
                for d in range(0, len(fcont)):
                    print(str(d))
                    print(tname)
                    print(tname+str(d))
                    os.replace(dir + "\\" + fcont[d][0], dir + "\\" + tname + str(d+1) + fcont[d][3])

            else: tkinter.messagebox.askokcancel(title="No path input", message="Please input a correct path")

root = tkinter.Tk()
root.title("SortHelper")
gui = GUI(root)
root.mainloop()
