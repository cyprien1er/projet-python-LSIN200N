"""

"""
from tkinter import *
import random
class mastermind(Frame):
    def __init__(self,boss=None):
        Frame.__init__(self,boss)
        self.pack()
        self.couleurs=['#ffffff','#000000','#ff0000','#00ff00','#0000ff','#ffff00']
        self.nb_emplacements=4
        self.emplacements=[]
        self.emplacement_actif=0
        self.essais = -1
        self.prec_essai = []
        i=0
        self.dico_reponce = {0:'#ffffff',1: '#000000'}
        self.emplacements_prec_essai=[]
        self.master.title('codage')
        for e in range(self.nb_emplacements):
            self.emplacements_prec_essai.append(Frame(self, height=75))
            self.emplacements_prec_essai[-1].grid(row=1, column=e + 1, sticky=NSEW)
        for c in self.couleurs:
            Button(self, background=c,width=10,height=2,command=lambda couleur=i:self.jouer(couleur)).grid(row=2, column=i)
            i=i+1
        for e in range(self.nb_emplacements):
            self.emplacements.append(Frame(self,height=75,bg='#553823'))
            self.emplacements[-1].grid(row=0,column=e+1,sticky=EW)
        if len(self.couleurs)%2:
            Button(self,text='annuler', command=self.annuler).grid(row=3, column=int((len(self.couleurs)-1)/2))
        else:
            Button(self,text='annuler', command=self.annuler).grid(row=3, column=int((len(self.couleurs)-1)/2),columnspan=2)
        Button(self, text='rejouer', command=self.rejouer).grid(row=3, column=0)
        Button(self, text='quiter', command=self.quit).grid(row=3, column=len(self.couleurs)-1)
        self.ale=Button(self,text='code aléatoire', command=self.rand)
        self.ale.grid(row=4,column=0, columnspan=len(self.couleurs))
    def jouer(self,couleur):
        self.emplacements[self.emplacement_actif].configure(bg=self.couleurs[couleur])
        self.emplacement_actif+=1
        self.prec_essai.append(couleur)
        if self.emplacement_actif==len(self.emplacements):
            self.emplacement_actif=0
            self.essais+=1
            if self.essais:
                for e in range(self.nb_emplacements):
                    self.emplacements_prec_essai[e].configure(bg=self.couleurs[self.prec_essai[e]])
                if self.reponce==self.prec_essai:
                    Label(Tk(),text='gagné en '+str(self.essais)+' essais').pack()
                rep=[None]*self.nb_emplacements
                i=0
                for e in self.prec_essai:
                    if self.reponce[i]==e:
                        ok=1
                        while ok:
                            ok=random.randint(0,self.nb_emplacements-1)
                            if rep[ok]==None:
                                rep[ok]=1
                                ok=0
                            else:
                                ok=1
                    elif e in self.reponce:
                        ok = 1
                        while ok:
                            ok = random.randint(0, self.nb_emplacements - 1)
                            if rep[ok] == None:
                                rep[ok] = 0
                                ok=0
                            else:
                                ok=1
                    i+=1
                self.can.delete(ALL)
                i=0
                coins=[10,55]
                for p in rep:
                    if p!=None:
                        self.can.create_oval(coins[i%2],coins[i//2],coins[i%2]+10,coins[i//2]+10,fill=self.dico_reponce[p])
                    i+=1
            else:
                self.master.title('jeu')
                self.reponce=self.prec_essai
                self.can = Canvas(self, height=75, bg='#aaaaaa', width=75)
                self.can.grid(row=1, column=-1 + int((len(self.couleurs) - self.nb_emplacements) / 2), sticky=EW)
                self.ale.destroy()
            for e in self.emplacements:
                e.configure(bg='#553823')
            self.prec_essai=[]
    def annuler(self):
        if self.emplacement_actif:
            self.emplacement_actif -= 1
            self.emplacements[self.emplacement_actif].configure(bg='#553823')
            self.prec_essai[-1:len(self.prec_essai)]=[]
    def rejouer(self):
        if self.essais+1:
            self.emplacement_actif = 0
            self.essais = -1
            self.prec_essai = []
            self.master.title('codage')
            self.can.destroy()
            self.ale = Button(self, text='code aléatoire', command=self.rand)
            self.ale.grid(row=4, column=0, columnspan=len(self.couleurs))
            for e in range(self.nb_emplacements):
                self.emplacements_prec_essai[e].configure(bg='#eeeeee')
                self.emplacements[e].configure(bg='#553823')
    def rand(self):
        self.master.title('jeu')
        self.reponce = [random.randint(0,len(self.couleurs)-1) for _ in range(len(self.emplacements))]
        self.can = Canvas(self, height=75, bg='#aaaaaa', width=75)
        self.can.grid(row=1, column=-1 + int((len(self.couleurs) - self.nb_emplacements) / 2), sticky=EW)
        self.ale.destroy()
        for e in self.emplacements:
            e.configure(bg='#553823')
        self.prec_essai = []
        self.essais = 0
if __name__ == '__main__':
    f = Tk()
    f.resizable(width=0,height=0)
    mastermind(f)
    f.mainloop()