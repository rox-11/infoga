
#   _____    __    __   ______    __     __
#  /   . \  /  \  /  \ /      \  /  \   /  \   configured by (@snom)
#  |  ___/`~|   \ |  | |  []  |  |   \ /   |
#  | |____  |  \ \|  | |  ||  |  |         |
#  |____  | |  |\    | |  ||  |  |  |\_/|  |
#   ____| | |  | \   | |  []  |  |  |   |  |
#  |______| \__/  \__/ \______/  \__/   \__/
# 
# snom info gatharinct tool V 1.0
# sample version 
# version 1.1 gools: 
#       * add more and exact info li (addres , phone, email ...)
#       * add tool user password in requests to have more accses to info




from tkinter import *
from tkinter import messagebox
from bs4 import BeautifulSoup as bs
import requests
from tkinter import ttk





# varaibles

myFont= ('times',11,'bold')


#-------------------------------------------------------------------------------------------#

#fonctions
def undo():
    
   
    mFram.place(height=300,width=600)
    # secFram.place(x=1000)
    secFram.pack(side='bottom',fill="none",expand=False)
   



def found():
    window.configure(bg='#ffffff')
    backBtn = Button(secFram,text='back',fg='black', bg='red',font=myFont,bd=False,command=undo)
    backBtn.place(x=480,y=250,width=100)

    global a
    a = mFram.pack_forget()
    secFram.place(height=300,width=600)
    try:
        if igtitle == 'Instgram' :
            textElm.insert('end',' >> ACCONT LINC [ig]: not found \n', )
        
        else:
            
            textElm.insert('end',' >> ACCONT LINC [ig]:', 'orange')
            textElm.insert('end',f'{igtitle} \n')
    except:
        pass
    try:

        if fbtitle == 'Facebook':
            textElm.insert('end',' >> ACCONT LINC [fb]: not found \n')
        
        else:
            
            textElm.insert('end',' >> ACCONT LINC [fb]:', 'blue')
            textElm.insert('end',f'{fbtitle} \n')
    except:
        pass



    

    

def infget():


    name = infoEntry.get()
    fbCheck = ivone.get()
    istgCheck = ivtwo.get()
    xCheck = ivtree.get()
    
    def facebook():

        if fbCheck == 1:
            
            facebookUrl = 'https://www.facebook.com/'
            request = requests.get(facebookUrl+name)
            soup = bs(request.content,'html.parser')
            global fbtitle
            title1 = soup.find('title')
            fbtitle = title1.string

            # if fbtitle == 'Facebook':
            #         messagebox.showwarning(title='notfound', message='notfound')
            # else:
            #         print(f"facebook",titleOf)

                     
                    
        else:
        
                pass
            # ----------------------------
        
    
    facebook()


    def instgrame():

        if istgCheck == 1:
    
            instgramUrl = 'https://www.instagram.com/'
        #     https://www.instagram.com/   
            request = requests.get(instgramUrl+name)
            soup = bs(request.content,'html.parser')
            global igtitle
            title1 = soup.find('title')
            igtitle = title1.string

            # if titleOf == 'Instagram':
            #         messagebox.showwarning(title='notfound', message='notfound')
            # else:
            #         print(f"instgrame",titleOf)
                    
                    
        else:
        
        #     
                pass
    instgrame()

                #-----------------------------
    def twitter():


        print('not working yet in this verssion')
    # twitter()    


# -----------------------------------------------------------------------------------------------------------------#


window = Tk()
window.config(bg='black')
window.geometry('600x300')

# main fram

mFram = Frame(window,bg='#000000')
mFram.place(height=300,width=600)

# top label for search message

searchLabel= Label(mFram,text='search',fg='white',bg='black').pack(side='top', pady= 10)

# info entry

infoEntry = Entry(mFram,border=0, bg='white',width=30)
infoEntry.pack()

# check button

ivone = IntVar()
ivtwo = IntVar()
ivtree = IntVar()
fb = Checkbutton(mFram,text='facebook',bg='black',fg='#0165E1',font=myFont,variable=ivone)
fb.place(x=100,y=100)
istg = Checkbutton(mFram,text='instgram',bg='black',fg='#FCAF45',font=myFont,variable=ivtwo)
istg.place(x=250,y=100)
x = Checkbutton(mFram,text='twitter',bg='black',fg='#1D9BF0',font=myFont, variable=ivtree )
x.place(x=400,y=100)

# click button for search about the target

mainClickBtn = Button(mFram,text='click',fg='black', bg='red',font=myFont,bd=False,command=infget)
mainClickBtn.place(x=240,y=180,width=100)

# down button

downBtn = Button(mFram,text='down',fg='black', bg='red',font=myFont,bd=False,command=found)
downBtn.place(x=480,y=250,width=100)

# second frame
secFram = Frame(window,bg='#ffffff')
secFram.pack_forget()

# text field

textElm = Text(secFram)
textElm.tag_config('blue',background='blue',foreground='white')    
textElm.tag_config('orange',background='orange',foreground='white')
textElm.tag_config('red',foreground='red')
textElm.insert('end','''
   _____    __    __   ______    __     __
  /   . \  /  \  /  \ /      \  /  \   /  \   configured by (@snom)
  |  ___/`~|   \ |  | |  []  |  |   \ /   |
  | |____  |  \ \|  | |  ||  |  |         |
  |____  | |  |\    | |  ||  |  |  |\_/|  |
   ____| | |  | \   | |  []  |  |  |   |  |
  |______| \__/  \__/ \______/  \__/   \__/ \n''','red')
textElm.insert('end','\n')

textElm.place(x=0,y=0)
scr = Scrollbar(secFram,orient="vertical",command=textElm.yview)
scr.pack(side='right',fill='y')
textElm.config(yscrollcommand=scr.set)

window.mainloop()
