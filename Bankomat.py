from tkinter import *
import os
import tkinter as tk


def main():

    liczba = 0
    pin=[]
    goodpin=[1,1,1,1]
    twojesaldo=1000000
    kwota = 0
    wyplacanakwota=""
    wyplacanakwotatablica=[]
    zmiennaiteracyjnapin=3


    class Bankomat():

        def __init__(self):


            #OKNO GLOWNE
            self.oknoglowe=Tk()
            self.oknoglowe.geometry("500x500")
            self.oknoglowe.title("Bankomat-interface")
            self.pinpad = []  # tablica przyciskow do wprowadzenia PIN

            #KOMUNIKAT
            self.Label1=Label(text="Podaj pin: ", borderwidth="5", relief="raised", background="silver")
            self.Label1.config(font=("Arial", 22))
            self.Label1.place(x=180, y=20)


            #WPISANY PIN

            self.Label2=Label(text='', background="white", width=20)
            self.Label2.place(x=130, y=80)
            self.Label2.config(font=("Arial", 16))

            for wiersz in range(1, 4):
                # Przyciski wiersza 'wiersz'
                min_wiersz, max_wiersz = 3 * (wiersz-1) + 1, 3 * wiersz + 1
                for i in range(min_wiersz, max_wiersz):
                    przycisk = Button(text="%d"%i, width="6", height="3", background="silver", command=lambda j=i: self.Nacisnij(j))
                    przycisk.place(x=150+((i-1)%3)*70, y=150+(wiersz-1)*70)
                    self.pinpad.append(przycisk)

            #Przycisk 0
            self.przycisk0 = Button(text="0", width="6", height="3", background="silver", command=lambda j=0: self.Nacisnij(j))
            self.przycisk0.place(x=150, y=360)

            #Przycisk *
            self.przyciskgw = Button(text="*", width="6", height="3", background="silver")
            self.przyciskgw.place(x=220, y=360)

            #Przycisk #
            self.przyciskhash = Button(text="#", width="6", height="3", background="silver")
            self.przyciskhash.place(x=290, y=360)


            #PrzyciskZatwierdz
            self.przyciskzatwierdz = Button(text="Zatwierdź", width="10", height="2", background="silver", command=self.Zatwierdz)
            self.przyciskzatwierdz.place(x=80, y= 430)

            #PrzyciskBackspace
            self.przyciskbackspace = Button(text="<---", width="10", height="2", background="silver", command=self.cofnij)
            self.przyciskbackspace.place(x=350, y=430)

            self.oknoglowe.mainloop()


#Funkcje przycisków klawiatury - wpisywanie pinu
        def Nacisnij(self, cyfra):
            nonlocal liczba
            liczba=liczba+1
            pin.append(cyfra)
            self.Label2.configure(text=liczba*'*')

        def Nacisnij0(self):
            nonlocal liczba
            liczba=liczba+1
            pin.append(0)
            self.Label2.configure(text=liczba * '*')


        ##############SPRAWDZANIE POPRAWNOŚCI PINU############################################

        def Zatwierdz(self):
            if pin==goodpin:
                self.Wybierzoperacje()

            else:
                nonlocal zmiennaiteracyjnapin
                nonlocal liczba
                zmiennaiteracyjnapin=zmiennaiteracyjnapin-1
                self.Label2.configure(text=" ")
                pin.clear()
                liczba=0
                if zmiennaiteracyjnapin <= 0:
                    try:
                        self.Zlypin()
                    except:
                        pass
                    #self.Zlypintrzy()



        def Zlypin(self):
            for widget in self.oknoglowe.winfo_children():
                widget.destroy()

        def Zlypintrzy(self):
            self.Label10 = Label(text="Podałeś nieprawidłowy PIN trzy razy, koniec, nie ma kasy :-)", borderwidth="5", relief="raised", background="silver")
            self.Label10.config(font=("Arial", 22))
            self.Label10.place(x=180, y=20)



        ########PRZYCISK BACKSPACE - FUNKCJA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        def cofnij(self):
            nonlocal liczba
            pin.remove(pin[-1])
            liczba=liczba-1
            if liczba==0 and pin==[]:
                self.Label2.configure(text="")
            self.Label2.configure(text=liczba*'*')


        def Wybierzoperacje(self):

            for widget in self.oknoglowe.winfo_children():
                widget.destroy()

            self.Label1 = Label(text="Wybierz operację, którą chcesz wykonać: ", borderwidth="5", relief="raised", background="silver")
            self.Label1.config(font=("Arial", 16))
            self.Label1.place(x=60, y=20)



            #PRZYCISK SALDO
            self.saldo = Button(text="Saldo", width="15", height="2", background="silver", font=("Arial", 16), command=self.Saldokonta)
            self.saldo.place(x=50, y=80)

            #PRZYCISK WYPLATA
            self.wyplata = Button(text="Wypłata gotówki", width="15", height="2", background="silver", font=("Arial", 16), command=self.wyplatagot)
            self.wyplata.place(x=50, y=155)



        def Saldokonta(self):
            self.Label1.configure(text="Saldo Twojego konta wynosi:")
            self.saldo.destroy()
            self.wyplata.destroy()

            self.Twojesaldo=Label(text=twojesaldo, background="silver", width="20", height="2", font=("Arial", 16))
            self.Twojesaldo.place(x=50, y=100)

            self.TwojesaldoPLN = Label(text="PLN", background="silver", width="3", height="2", font=("Arial", 16))
            self.TwojesaldoPLN.place(x=250, y=100)

            self.Pytanie = Label(text="Czy chcesz wykonać jeszcze jakąś operację?", borderwidth="5", background="silver")
            self.Pytanie.config(font=("Arial", 16))
            self.Pytanie.place(x=50, y=220)

            #PRZYCISK TAK
            self.tak = Button(text="Tak", width="3", height="1", background="silver", font=("Arial", 14), command=self.tak)
            self.tak.place(x=90, y=270)

            #PRZYCISK NIE
            self.nie = Button(text="Nie", width="3", height="1", background="silver", font=("Arial", 14), command=self.koniec)
            self.nie.place(x=90, y=320)

        def koniec(self):
            for widget in self.oknoglowe.winfo_children():
                widget.destroy()
            self.Label4 = Label(text="Dziekujemy i zapraszamy ponownie", borderwidth="5", relief="raised",
                                background="silver")
            self.Label4.config(font=("Arial", 16))
            self.Label4.place(x=80, y=30)


        def tak(self):
            self.tak.destroy()
            self.nie.destroy()
            self.Twojesaldo.destroy()
            self.TwojesaldoPLN.destroy()
            self.Pytanie.destroy()
            self.Wybierzoperacje()


        def wyplatagot(self):
            self.Label1.configure(text="Ile pieniędzy chcesz wypłacić?")
            self.Label1.place(x=100, y=30)
            self.saldo.destroy()
            self.wyplata.destroy()

            self.Label3 = Label(text='', background="white", width=20)
            self.Label3.place(x=130, y=80)
            self.Label3.config(font=("Arial", 16))
            
            # Zmiane tej serii przyciskow pozostawiam jako cwiczenie
            
            # Przycisk 1
            self.przycisk1 = Button(text="1", width="6", height="3", background="silver", command=self.Na1)
            self.przycisk1.place(x=150, y=150)

            # Przycisk 2
            self.przycisk2 = Button(text="2", width="6", height="3", background="silver", command=self.Na2)
            self.przycisk2.place(x=220, y=150)

            # Przycisk 3
            self.przycisk3 = Button(text="3", width="6", height="3", background="silver", command=self.Na3)
            self.przycisk3.place(x=290, y=150)

            # Przycisk 4
            self.przycisk4 = Button(text="4", width="6", height="3", background="silver", command=self.Na4)
            self.przycisk4.place(x=150, y=220)

            # Przycisk 5
            self.przycisk5 = Button(text="5", width="6", height="3", background="silver", command=self.Na5)
            self.przycisk5.place(x=220, y=220)

            # Przycisk 6
            self.przycisk6 = Button(text="6", width="6", height="3", background="silver", command=self.Na6)
            self.przycisk6.place(x=290, y=220)

            # Przycisk 7
            self.przycisk7 = Button(text="7", width="6", height="3", background="silver", command=self.Na7)
            self.przycisk7.place(x=150, y=290)

            # Przycisk 8
            self.przycisk8 = Button(text="8", width="6", height="3", background="silver", command=self.Na8)
            self.przycisk8.place(x=220, y=290)

            # Przycisk 9
            self.przycisk9 = Button(text="9", width="6", height="3", background="silver", command=self.Na9)
            self.przycisk9.place(x=290, y=290)

            # Przycisk 0
            self.przycisk0 = Button(text="0", width="6", height="3", background="silver", command=self.Na0)
            self.przycisk0.place(x=150, y=360)

            # Przycisk *
            self.przyciskgw = Button(text="*", width="6", height="3", background="silver")
            self.przyciskgw.place(x=220, y=360)

            # Przycisk #
            self.przyciskhash = Button(text="#", width="6", height="3", background="silver")
            self.przyciskhash.place(x=290, y=360)

            # PrzyciskZatwierdz
            self.przyciskzatwierdz = Button(text="Zatwierdź", width="10", height="2", background="silver",
                                            command=self.Zatwierdz2)
            self.przyciskzatwierdz.place(x=80, y=430)

            # PrzyciskBackspace
            self.przyciskbackspace = Button(text="<---", width="10", height="2", background="silver",
                                            command=self.cofnij2)
            self.przyciskbackspace.place(x=350, y=430)

#Funkcje klawiatura wyplacanie kwoty
        def Na1(self):
            nonlocal wyplacanakwota
            wyplacanakwota=wyplacanakwota+"1"
            wyplacanakwotatablica.append(1)
            self.Label3.configure(text=wyplacanakwota)

        def Na2(self):
            nonlocal wyplacanakwota
            wyplacanakwota=wyplacanakwota+"2"
            wyplacanakwotatablica.append(2)
            self.Label3.configure(text=wyplacanakwota)

        def Na3(self):
            nonlocal wyplacanakwota
            wyplacanakwota=wyplacanakwota+"3"
            wyplacanakwotatablica.append(3)
            self.Label3.configure(text=wyplacanakwota)

        def Na4(self):
            nonlocal wyplacanakwota
            wyplacanakwota=wyplacanakwota+"4"
            wyplacanakwotatablica.append(4)
            self.Label3.configure(text=wyplacanakwota)

        def Na5(self):
            nonlocal wyplacanakwota
            wyplacanakwota=wyplacanakwota+"5"
            wyplacanakwotatablica.append(5)
            self.Label3.configure(text=wyplacanakwota)

        def Na6(self):
            nonlocal wyplacanakwota
            wyplacanakwota=wyplacanakwota+"6"
            wyplacanakwotatablica.append(6)
            self.Label3.configure(text=wyplacanakwota)

        def Na7(self):
            nonlocal wyplacanakwota
            wyplacanakwota=wyplacanakwota+"7"
            wyplacanakwotatablica.append(7)
            self.Label3.configure(text=wyplacanakwota)

        def Na8(self):
            nonlocal wyplacanakwota
            wyplacanakwota=wyplacanakwota+"8"
            wyplacanakwotatablica.append(8)
            self.Label3.configure(text=wyplacanakwota)

        def Na9(self):
            nonlocal wyplacanakwota
            wyplacanakwota = wyplacanakwota + "9"
            wyplacanakwotatablica.append(9)
            self.Label3.configure(text=wyplacanakwota)

        def Na0(self):
            nonlocal wyplacanakwota
            wyplacanakwota = wyplacanakwota + "0"
            wyplacanakwotatablica.append(0)
            self.Label3.configure(text=wyplacanakwota)

        def cofnij2(self):
            nonlocal wyplacanakwota
            self.b = []
            for i in wyplacanakwota:
                self.b.append(i)
            self.b.remove(self.b[-1])
            wyplacanakwota = ""
            for v in self.b:
                wyplacanakwota=wyplacanakwota+v

            wyplacanakwotatablica.remove(wyplacanakwotatablica[-1])
            a=""
            for i in wyplacanakwotatablica:
                a=a+str(i)
                self.Label3.configure(text=a)

        def Zatwierdz2(self):
            nonlocal wyplacanakwota
            nonlocal wyplacanakwotatablica
            wyplacanakwotatablica=[]
            wyplacanakwota=""
            self.f=self.Label3.cget("text")
            self.f=int(self.f)
            nonlocal twojesaldo
            twojesaldo=twojesaldo-self.f

            for widget in self.oknoglowe.winfo_children():
                widget.destroy()
            self.Wybierzoperacje()


    Bankomat()
    return 0
if __name__== '__main__':
    main()
