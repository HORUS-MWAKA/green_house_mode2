import pickle
import joblib
import streamlit as st
from streamlit_option_menu import option_menu

def show_entry_fields():
    p1=float(e1.get())
    p2=int(e2.get())
    p3=float(e3.get())
    p4=int(e4.get())
    
    model = joblib.load('model_green_house')
    result=model.predict([[p1,p2,p3,p4]])

    if result == 0:
        Label(master, text="No Aeration").grid(row=6)

    else:
        Label(master, text="Aeration Needed").grid(row=6)

master = Tk()
master.title("Greenhouse Predictive Model")

label = Label(master,text = "Greenhouse Predictive Model"
               , bg = "black", fg = "white"). \
                    grid(row=0,columnspan=2)

Label(master, text="Enter Temperature Value").grid(row=1)
Label(master, text="Enter Humidity Value").grid(row=2)
Label(master, text="Enter Soil Moisture Value").grid(row=3)
Label(master, text="Enter Aeration State Value").grid(row=4)

e1=Entry(master)
e2=Entry(master)
e3=Entry(master)
e4=Entry(master)

e1.grid(row=1,column=1)
e2.grid(row=2,column=1)
e3.grid(row=3,column=1)
e4.grid(row=4,column=1)

Button(master,text='Predict', command=show_entry_fields).grid()

mainloop()
