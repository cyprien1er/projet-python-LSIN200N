"""

"""
from tkinter import *
class pendu(Frame):
    def __init__(self,boss=None):
        Frame.__init__(self,boss)
        self.pack()
        self.rates = 0
        self.start=1
        self.lettre=Entry(self)
        self.lettre.grid(row=0, column=0)
        self.lettre.bind('<Return>', self.essai)
    def essai(self,event):
        if self.lettre.get()=='':
            return
        if self.start:
            self.can = Canvas(self)
            self.can.grid(row=2, column=0)
            self.reponce = self.lettre.get()
            self.affiche_bons = Label(self, text='_ ' * len(self.reponce))
            self.affiche_bons.grid(row=1, column=0)
            self.affichage = '_ ' * len(self.reponce)
            self.start = 0
            self.lettre.delete(0, END)
            return
        self.fin=0
        if self.lettre.get()[0] in self.reponce:
            i = 0
            for l in self.reponce:
                if l==self.lettre.get()[0]:
                    self.affichage = self.affichage[:i * 2] + self.lettre.get()[0] + ' ' + self.affichage[i * 2 + 2:]
                    mem=''
                    prec=''
                    for c in self.affichage:
                        if c!=' ' or prec=='_':
                            mem=mem+c
                        prec=c
                    self.affiche_bons.configure(text=mem)
                i+=1
            mem = ''
            prec = ''
            for c in self.affichage:
                if c != ' ' or prec == '_':
                    mem = mem + c
                prec = c
            if mem==self.reponce:
                self.lettre.destroy()
                Label(Tk(),text='gagné!').pack()
                self.fin=1
        else:
            self.rate()
        if not(self.fin):
            self.lettre.delete(0,END)
        else:
            self.replay=Button(self, text='rejouer', command=self.rejouer)
            self.replay.grid(row=3, column=0)
    def rate(self):
        self.rates+=1
        if self.rates == 1:
            self.can.create_line(100,200,200,200)
        if self.rates == 2:
            self.can.create_line(100,200,100,100)
        if self.rates == 3:
            self.can.create_line(100, 100, 200, 100)
        if self.rates == 4:
            self.can.create_line(100,125, 125,100)
        if self.rates == 5:
            self.can.create_line(200, 100, 200, 125)
        if self.rates == 6:
            self.can.create_oval(187.5, 125,212.5, 150)
        if self.rates == 7:
            self.can.create_line(200, 150,200, 162.5)
        if self.rates == 8:
            self.can.create_line(200, 162.5,187.5, 175)
        if self.rates == 9:
            self.can.create_line(200, 162.5, 212.4, 175)
        if self.rates == 10:
            self.can.create_line(200, 156.25,187.5,156.25)
        if self.rates == 11:
            self.can.create_line(200, 156.25, 212.4,156.25)
            self.lettre.destroy()
            self.fin=1
            Label(Tk(),text="perdu!\nc'était : "+self.reponce).pack()
    def rejouer(self):
        self.rates = 0
        self.start = 1
        self.lettre = Entry(self)
        self.lettre.grid(row=0, column=0)
        self.lettre.bind('<Return>', self.essai)
        self.can.destroy()
        self.replay.destroy()
        self.affiche_bons.destroy()
if __name__ == '__main__':
    f=Tk()
    f.resizable(width=0,height=0)
    f.title('pendu')
    pendu(f)
    f.mainloop()