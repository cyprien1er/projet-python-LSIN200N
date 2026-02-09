"""

"""
from tkinter import *
class puissance_4(Frame):
    def __init__(self,boss=None):
        Frame.__init__(self,boss,background='#c3c3c3')
        self.pack()
        self.dernier=[]
        self.li = []
        self.grille = []
        self.color_dict = {'R': '#ff0000', 'J': '#ffff00', 'V': '#ffffff'}
        self.can = Canvas(self, width=450, height=350,background='#0000ff')
        self.can.grid(row=2, column=0, columnspan=9, rowspan=6)
        self.choixligne=IntVar()
        self.tour=0
        Button(self,text='quitter',command=self.master.quit).grid(row=8, column=2)
        Button(self,text='rejouer',command=self.rejouer).grid(row=8, column=6)
        Button(self, text='annuler', command=self.annuler).grid(row=8, column=4)
        for line in range(7):
            l2 = []
            l3 = []
            for p in range(6):
                l2[0:0]=[self.can.create_oval(24+57 * line,50+50 * p,74 + 57 * line,100 + 50 * p, fill=self.color_dict['V'])]
                l3[0:0]=['V']
            self.li.append(l2)
            self.grille.append(l3)
            Radiobutton(self, text='', variable=self.choixligne, value=line,background='#c3c3c3').grid(row=1, column=1+line)
        Button(self, text='Jouer', command=self.placer).grid(row=0, column=4)
    def annuler(self):
        if self.dernier!=[]:
            self.grille[self.dernier[-1][0]][self.dernier[-1][1]] = 'V'
            self.can.itemconfig(self.li[self.dernier[-1][0]][self.dernier[-1][1]], fill=self.color_dict['V'])
            self.tour=not(self.tour)
            self.dernier[-1:len(self.dernier)]=[]
    def rejouer(self):
        self.dernier=[]
        for colonne in range(7):
            for l in range(6):
                self.grille[colonne][l] ='V'
                self.can.itemconfig(self.li[colonne][l], fill=self.color_dict[self.grille[colonne][l]])
    def placer_pion(self,couleur, colonne, grille):
        ok=False
        r=grille
        for l in range(6):
            if grille[colonne][l]== 'V'and not(ok):
                ok=True
                r[colonne][l]=couleur
                self.can.itemconfig(self.li[colonne][l],fill=self.color_dict[self.grille[colonne][l]])
                self.dernier.append((colonne,l))
        return ((ok,r))
    def placer(self):
        if self.tour:
            a,self.grille=self.placer_pion('R',self.choixligne.get(),self.grille)
            if a:
                self.tour = 0
        else:
            a,self.grille=self.placer_pion('J',self.choixligne.get(),self.grille)
            if a:
                self.tour = 1
        g=self.gagnant(self.grille)
        if g!=None:
            if g=='R':
                print('le joueur rouge a gagné!')
                f_2=Tk()
                Label(f_2, text='bravo au joueur rouge!').pack(side=TOP)
                Button(f_2, text='quitter', command=f_2.quit).pack(side=BOTTOM)
            else:
                print('bravo au joueur jaune !')
                f_2 = Tk()
                Label(f_2, text='le joueur jaune a gagné!').pack(side=TOP)
                Button(f_2, text='quitter', command=f_2.quit).pack(side=BOTTOM)
    def gagnant(self,grille):
        def test_g(grille,c,x,y,dx,dy):
            test=0
            for step in range(1,4):
                try:
                    if grille[y+dy*step][x+dx*step]==c:
                        test=test+1
                except:
                    pass
            return test==3
        y=0
        for l in grille:
            x=0
            for p in l:
                if p!='V':
                    g=x>2
                    d=x<4
                    for a in range(g*-1,d+1):
                        if y>2:
                            if test_g(grille,p,x,y,a,-1):
                                return p
                        else:
                            if test_g(grille,p,x,y,a,1):
                                return p
                    if g:
                        if test_g(grille, p, x, y, -1, 0):
                            return p
                    if d:
                        if test_g(grille, p, x, y, 1, 0):
                            return p
                x=x+1
            y=y+1
        return None
if __name__ == '__main__':
    f=Tk()
    f.resizable(width=0, height=0)
    puissance_4(f)
    f.mainloop()