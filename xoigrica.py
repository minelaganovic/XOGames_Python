from tkinter import *
from tkinter import messagebox
import random

trenutni_igrac=random.choice(['x','o'])
igra_aktivna=True
pobednik=None

def zamrzni_dugmad():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def deaktiviraj_igru():
    global igra_aktivna
    igra_aktivna=False
    pobednik=trenutni_igrac
    messagebox.showinfo('XO Igra', f'Pobedio je {pobednik}')
    zamrzni_dugmad()

def igraj_XO(gumb):
    global igra_aktivna, trenutni_igrac
    if igra_aktivna:
        igra_igrac(gumb, trenutni_igrac)

def igra_igrac(gumb, igrac):
    if gumb['text']=='':
        gumb.config(text=igrac)
        proveri_kraj_igre()
        promeni_igraca()
    else:
        messagebox.showerror('XO Igra','To nije dozvoljeno polje. Probaj ponovo.! ')

def proveri_kraj_igre():
    proveri_pobedu()
    proveri_nereseno()

def proveri_pobedu():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    if b1['text'] == b2['text']== b3['text']!='':
        deaktiviraj_igru()
    elif b4['text'] == b5['text']== b6['text']!='':
        deaktiviraj_igru()
    elif b7['text'] == b8['text']== b9['text']!='':
        deaktiviraj_igru()
    elif b1['text'] == b4['text']== b7['text']!='':
        deaktiviraj_igru()
    elif b2['text'] == b5['text']== b8['text']!='':
        deaktiviraj_igru()
    elif b3['text'] == b6['text']== b9['text']!='':
        deaktiviraj_igru()
    elif b1['text'] == b5['text']== b9['text']!='':
        deaktiviraj_igru()
    elif b3['text'] == b5['text']== b7['text']!='':
        deaktiviraj_igru()

def proveri_nereseno():
    global igra_aktivna
    kliknuta_sva_dugmad=b1['text']!='' and b2['text']!=''and b3['text']!=''and b4['text']!='' and b5['text']!='' and b6['text']!='' and b7['text']!='' and b8['text']!='' and b9['text']!=''
    if pobednik==None and kliknuta_sva_dugmad:
        igra_aktivna=False
        zamrzni_dugmad()
        messagebox.showinfo('XO Igra','Nereseno je!')

def promeni_igraca():
    global trenutni_igrac
    if trenutni_igrac=='x':
        trenutni_igrac='o'
    elif trenutni_igrac=='o':
        trenutni_igrac='x'   

root=Tk()
root.title('XO Igra!')

b1=Button(root, text='', font=('Helvetica,20'), height=3, width=6, bg='white',command=lambda:igraj_XO(b1) )
b2=Button(root, text='', font=('Helvetica,20'), height=3, width=6, bg='white',command=lambda:igraj_XO(b2) )
b3=Button(root, text='', font=('Helvetica,20'), height=3, width=6, bg='white',command=lambda:igraj_XO(b3) )

b4=Button(root, text='', font=('Helvetica,20'), height=3, width=6, bg='white',command=lambda:igraj_XO(b4) )
b5=Button(root, text='', font=('Helvetica,20'), height=3, width=6, bg='white',command=lambda:igraj_XO(b5) )
b6=Button(root, text='', font=('Helvetica,20'), height=3, width=6, bg='white',command=lambda:igraj_XO(b6) )

b7=Button(root, text='', font=('Helvetica,20'), height=3, width=6, bg='white',command=lambda:igraj_XO(b7) )
b8=Button(root, text='', font=('Helvetica,20'), height=3, width=6, bg='white',command=lambda:igraj_XO(b8) )
b9=Button(root, text='', font=('Helvetica,20'), height=3, width=6, bg='white',command=lambda:igraj_XO(b9) )

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

root.mainloop()