import tkinter
from tkinter import *
import subprocess



# Layer 7
''' GET, POST, OVH BYPASS, STRESS, OSTRESS, DYN, SLOW, HEAD, HIT, NULL, COOKIE, BRUST, CFB'''
# Layer 4
''' TCP, UDP, SYN '''
# Layer 3
'''ICMP, POD'''


def get():
    #subprocess.call(['cd', 'Desktop'])
    #window.destroy()
    subprocess.call(['python', 'dos_get_method.py', 'http://pmgrz.net])    # url (tuk izliza nqkvo stranno ddz )
    # Tuk samo edno neshto trqbva da se napravi i to e, da smesnish imeto na faila.
    ''' 'dos_get_method.py' trqbva da se smeni primerno s tvoq OVH Bypass '''


    #dos.mainloop()


def icmp():
    subprocess.call(['ping', '1.1.1.1'])


def MainWindow():
    window = Tk()
    window.geometry('800x500-200-100')
    window.title('DDoS Tool')
    window.configure(bg='Gray15')
    window.minsize(800,500)
    window.maxsize(800,500)
    EmptyLabel = Label(window, text="", bg='Gray15')
    EmptyLabel.grid(row=0, column=1)
    EmptyLabel1 = Label(window, text="\t", bg='Gray15')  #'\t\t\t\t               '
    EmptyLabel1.grid(row=1, column=0)
    EmptyLabelABC = Label(window, text="      ", bg='Gray15')
    EmptyLabelABC.grid(row=1, column=1)
    # Layer 7
    Layer7 = Label(window, text="    Layer 7 ", bg='Gray15')
    Layer7.grid(row=1, column=2, sticky='w')

    EmptyLabel2 = Label(window, text="", bg='Gray15')
    EmptyLabel2.grid(row=2, column=3)
    EmptyL = Label(window, text="\t\t", bg='Gray15')
    EmptyL.grid(row=3, column=0)
    Get = Button(window, text='    GET    ', bg='Gray13', command=lambda: get())
    Get.grid(row=3, column=1, sticky='w')
    Post = Button(window, text='   POST   ', bg='Gray13')
    Post.grid(row=3, column=2, sticky='w')
    Ovh = Button(window, text='    OVH    ', bg='Gray13')
    Ovh.grid(row=3, column=3, sticky='w')

    Stress = Button(window, text=' STRESS ', bg='Gray13')
    Stress.grid(row=4, column=1)
    Slow = Button(window, text='   SLOW  ', bg='Gray13')
    Slow.grid(row=4, column=2)
    Dyn = Button(window, text='    DYN    ', bg='Gray13')
    Dyn.grid(row=4, column=3)

    Hit = Button(window, text='    HIT    ', bg='Gray13')
    Hit.grid(row=5, column=1)
    Cookie = Button(window, text=' COOKIE ', bg='Gray13')
    Cookie.grid(row=5, column=2)
    Cfb = Button(window, text='CFBypass', bg='Gray13')
    Cfb.grid(row=5, column=3)
    # Layer 4
    EmptyLabelCol3 = Label(window, text="\t\t", bg='Gray15')
    EmptyLabelCol3.grid(row=1, column=4)
    Layer4 = Label(window, text="    Layer 4 ", bg='Gray15')
    Layer4.grid(row=1, column=5, sticky='w')
    Tcp = Button(window, text='    TCP    ', bg='Gray13')
    Tcp.grid(row=3, column=4, sticky='e')
    Udp = Button(window, text='    UDP    ', bg='Gray13')
    Udp.grid(row=3, column=5)
    Syn = Button(window, text='    SYN    ', bg='Gray13')
    Syn.grid(row=3, column=6)
    # Layer 3
    EmptyLabelRow6 = Label(window, text="", bg='Gray15')
    EmptyLabelRow6.grid(row=6, column=0)
    EmptyLabelRow7 = Label(window, text="\t", bg='Gray15')
    EmptyLabelRow7.grid(row=7, column=0)
    EmptyLabelRow7Col1 = Label(window, text="      ", bg='Gray15')
    EmptyLabelRow7Col1.grid(row=7, column=1)
    Layer3 = Label(window, text="  Layer 3 ", bg='Gray15')
    Layer3.grid(row=7, column=2)
    Icmp = Button(window, text='   ICMP   ', bg='Gray13', command=lambda: icmp())
    Icmp.grid(row=8, column=1)
    Pod = Button(window, text='    POD    ', bg='Gray13')
    Pod.grid(row=8, column=3)
    # Deautification Attack
    EmptyLabelXYZ = Label(window, text='\t\t', bg='Gray15')
    EmptyLabelXYZ.grid(row=7, column=4)
    DefAtt = Label(window, text=' Def Attack ', bg='Gray15')
    DefAtt.grid(row=7, column=5)
    options = Button(window, text="Options",bg='Gray13')
    options.grid(row=8, column=5)

    window.mainloop()


MainWindow()