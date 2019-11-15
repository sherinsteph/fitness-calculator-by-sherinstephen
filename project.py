from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Fitness Calculator")
root.geometry('730x630')
image2 = PhotoImage(file="fs.png")
#print(image2)
frame1 = Frame(root,bg="blue",height = 6)
label1 = Label(frame1,text = "",image = image2,fg = "white",bg = "blue",height = "100",font=("Helvetica", 16))
label1.pack()
frame1.pack(fill = 'x')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
def fetch():
   # appHighlightFont = font.Font(family='Helvetica', size=12, weight='bold')
    fetcher = Tk()
    fetcher.title("Enter your id")
    fetcher.geometry("500x200")
    Label(fetcher,text = "ENTER YOUR ID HERE",).pack(pady=20)
    id_ftch = Entry(fetcher)
    id_ftch.pack()
    btntofetchit = Button(fetcher, text="FETCH DETAILS", command=lambda: id_validator(id_ftch))
    btntofetchit.pack(pady=50)
    fetcher.mainloop()
def id_validator(id_ftch):
    try:
        import sqlite3
        idgetter = id_ftch.get()
        conn = sqlite3.connect("ftscalc.db")
        data = conn.execute(f'SELECT * FROM FITCAL WHERE ID ={idgetter}')
        list = []
        for row in data:
            for j in range(14):
                list.append(str(row[j]))

        print(list)
        if len(list) == 0:
            messagebox.showerror("Not Found", "Please Enter a Valid ID")
        else:
            fetchit(list)
    except:
        messagebox.showerror("incomplete value","please enter the value !")


def fetchit(list):

    report = Tk()
    report.geometry("400x590")
    report.title("FETCHED REPORT")
    frame6 = Frame(report,bg="blue")
    #frame6.place(relx=0.5, rely=0.5, anchor=CENTER)
    frame6.pack(fill="x")
    fet1 = Label(frame6,text="Name  :",fg = "white",bg = "blue",height = "0",font=("Helvetica", 18),padx =50)
    #fet1.place(relx=0.5, rely=0.5, anchor=CENTER)
    fet1.grid(column=0,row=0,sticky = "w")
    fett1 =Label(frame6,text=list[1],fg = "white",bg = "blue",height = "0",font=("Helvetica", 18))
    fett1.grid(column=1,row=0,sticky = "w")
    fet2 = Label(frame6,text = "Age  :",fg = "white",bg = "blue",height = "0",font=("Helvetica", 12),padx =50)
    fet2.grid(column=0,row=1,sticky = "w")
    fett2 = Label(frame6,text = list[3],fg = "white",bg = "blue",height = "0",font=("Helvetica", 12))
    fett2.grid(column=1,row=1,sticky = "w")
    fet3 = Label(frame6,text = "Gender  :",fg = "white",bg = "blue",height = "0",font=("Helvetica", 12),padx =50)
    fet3.grid(column=0,row=2,sticky = "w")
    fett3 = Label(frame6,text = list[2],fg = "white",bg = "blue",height = "0",font=("Helvetica", 12))
    fett3.grid(column=1,row=2,sticky = "w")
    fet4 = Label(frame6,text="ID   :",fg = "white",bg = "blue",height = "0",font=("Helvetica", 12),padx =50)
    fet4.grid(column=0,row=3,sticky = "w")
    fett4 =Label(frame6,text=list[0],fg = "white",bg = "blue",height = "0",font=("Helvetica", 12))
    fett4.grid(column=1,row=3,sticky = "w")



    frame5 = Frame(report, pady=50)
    frame5.pack(pady = 30)

    Label(frame5, text="BMI(BODY MASS INDEX):").grid(column=0, row=0, sticky='w')
    rep_bmientry = Entry(frame5)
    rep_bmientry.grid(column=1, row=0)

    Label(frame5, text="BP(High/Medium/Low):").grid(column=0, row=1, sticky='w')
    rep_bpentry = Entry(frame5)
    rep_bpentry.grid(column=1, row=1)

    Label(frame5, text="Pulse Rate(High/Medium/Low):").grid(column=0, row=2, sticky='w')
    rep_pulseentry = Entry(frame5)
    rep_pulseentry.grid(column=1, row=2)

    Label(frame5, text="RBC Count(High/Medium/Low):").grid(column=0, row=3, sticky='w')
    rep_rbcenrty = Entry(frame5)
    rep_rbcenrty.grid(column=1, row=3)

    Label(frame5, text="WBC Count(High/Medium/Low):").grid(column=0, row=4, sticky='w')
    rep_wbcentry = Entry(frame5)
    rep_wbcentry.grid(column=1, row=4)

    Label(frame5, text="Platelets(High/Medium/Low):").grid(column=0, row=5, sticky='w')
    rep_plateletsentry = Entry(frame5)
    rep_plateletsentry.grid(column=1, row=5)

    Label(frame5, text="HB(High/Medium/Low):").grid(column=0, row=6, sticky='w')
    rep_hbentry = Entry(frame5)
    rep_hbentry.grid(column=1, row=6)

    Label(frame5, text="Uric Acid(High/Medium/Low):").grid(column=0, row=7, sticky='w')
    rep_uricacidentry = Entry(frame5)
    rep_uricacidentry.grid(column=1, row=7)

    Label(frame5, text="Cholesterol(High/Medium/Low):").grid(column=0, row=8, sticky='w')
    rep_cholesterolentry = Entry(frame5)
    rep_cholesterolentry.grid(column=1, row=8)


    rep_bmientry.insert(0, list[4])
    rep_bpentry.insert(0, list[5])
    rep_pulseentry.insert(0, list[6])
    rep_rbcenrty.insert(0, list[7])
    rep_wbcentry.insert(0, list[8])
    rep_plateletsentry.insert(0, list[9])
    rep_hbentry.insert(0, list[10])
    rep_uricacidentry.insert(0, list[11])
    rep_cholesterolentry.insert(0, list[12])
    bottomframe = Frame(report)
    bottomframe.pack()
    saved_datetime_fetch = Label(bottomframe, text=f'saved on {list[13]}')
    saved_datetime_fetch.pack()


    report.mainloop()





#---------------------------------------------------------------ID GEN Using Time-----------------------------------------------------------------------------------
def idgen():
    import time
    c = time.time()
    time_str = str(c)
    indexdot = time_str.find(".")
    #print(indexdot)
    time_id = time_str[:indexdot]
    return  time_id
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
#database saving
def save(a,b,c,d,e,f,g,h,i,gender,age_s,idgenerated,saved_datetime):

    #print("working")
    import sqlite3
    import time
    seconds = time.time()
    localtime = time.ctime(seconds)
    conn = sqlite3.connect("ftscalc.db")
    id = int(idgen())
    if gender == 1:
        gendata ="Male"
    else:
        gendata ="Female"
    name = name_entry.get()
    parms = [id,name,gendata,age_s,str(a),b,c,d,e,f,g,h,i,str(localtime)]
    conn.execute("""CREATE TABLE IF NOT EXISTS FITCAL(
    ID INT PRIMARY KEY,
    NAME CHAR(50),
    GENDER CHAR(20),
    AGE INT,
    BMI TEXT,
    BP TEXT,
    PULSERATE TEXT,
    RBC TEXT,
    WBC TEXT,
    PLATELETS TEXT,
    HB TEXT,
    URICACID TEXT,
    CHOLESTEROL TEXT,
    DAYTIME TEXT
    )
    """)

    sql_insertion ="INSERT INTO FITCAL VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)"

    conn.execute(sql_insertion,parms)
    conn.commit()

    messagebox.showinfo("Successfull",f'Data saved sucessfully and your unique ID is - {id}')
    idgenerated.configure(text = f'your ID is {id}')
    import time
    seconds = time.time()
    local = time.ctime(seconds)
    #ids = id
    saved_datetime.configure(text = f'saved data sucessfully on {localtime}')


#-------------------------------functions-----------------------------------------
def report():
    #from tkinter import PhotoImage
    report = Tk()
    report.title('REPORT')
    report.geometry('430x700')

    frame4 = Frame(report, bg="blue")
    lab = Label(frame4,text = "Report",fg = "white",bg = "blue",height = "5",font=("Helvetica", 16))
    lab.pack()

    frame4.pack(fill='x')
    #-----------------------operations--------------------------------------------
    gender = v.get()
    age=age_entry.get()
    height = height_entry.get()
    weight = weight_entry.get()
    bplow =bplow_entry.get()
    bphigh = bphigh_entry.get()
    pulserate=pulserate_entry.get()
    rbc = rbc_entry.get()
    wbc = wbc_entry.get()
    platelets = platelets_entry.get()
    hb = hb_entry.get()
    uricacid = uricacid_entry.get()
    cholesterol = cholesterol_entry.get()

    a=bmi(int(height),int(weight))
    b=bpcheck(int(bplow),int(bphigh))
    c=pulserate_check(gender,int(age),int(pulserate))
    d=rbc_check(gender,float(rbc))
    e=wbc_check(int(wbc))
    f=Platelets_check(int(platelets))
    g=hb_check(gender,float(hb))
    h=uricacid_check(gender,float(uricacid))
    i=cholesterol_check(int(cholesterol))
    #
    # print(a,b,c,d,e,f,g,h,i)
    #save to database function












    #------------------------------------


    frame5 = Frame(report,pady =50)
    frame5.pack()
    Label(frame5, text="BMI(BODY MASS INDEX):").grid(column=0, row=0, sticky='w')
    rep_bmientry = Entry(frame5)
    rep_bmientry.grid(column=1, row=0)

    Label(frame5, text="BP(High/Medium/Low):").grid(column=0, row=1, sticky='w')
    rep_bpentry = Entry(frame5)
    rep_bpentry.grid(column=1, row=1)

    Label(frame5, text="Pulse Rate(High/Medium/Low):").grid(column=0, row=2, sticky='w')
    rep_pulseentry = Entry(frame5)
    rep_pulseentry.grid(column=1, row=2)

    Label(frame5, text="RBC Count(High/Medium/Low):").grid(column=0, row=3, sticky='w')
    rep_rbcenrty = Entry(frame5)
    rep_rbcenrty.grid(column=1, row=3)

    Label(frame5, text="WBC Count(High/Medium/Low):").grid(column=0, row=4, sticky='w')
    rep_wbcentry = Entry(frame5)
    rep_wbcentry.grid(column=1, row=4)

    Label(frame5, text="Platelets(High/Medium/Low):").grid(column=0, row=5, sticky='w')
    rep_plateletsentry = Entry(frame5)
    rep_plateletsentry.grid(column=1, row=5)

    Label(frame5, text="HB(High/Medium/Low):").grid(column=0, row=6, sticky='w')
    rep_hbentry = Entry(frame5)
    rep_hbentry.grid(column=1, row=6)

    Label(frame5, text="Uric Acid(High/Medium/Low):").grid(column=0, row=7, sticky='w')
    rep_uricacidentry = Entry(frame5)
    rep_uricacidentry.grid(column=1, row=7)

    Label(frame5, text="Cholesterol(High/Medium/Low):").grid(column=0, row=8, sticky='w')
    rep_cholesterolentry = Entry(frame5)
    rep_cholesterolentry.grid(column=1, row=8)

    rep_bmientry.insert(0,a)
    rep_bpentry.insert(0,b)
    rep_pulseentry.insert(0,c)
    rep_rbcenrty.insert(0,d)
    rep_wbcentry.insert(0,e)
    rep_plateletsentry.insert(0,f)
    rep_hbentry.insert(0,g)
    rep_uricacidentry.insert(0,h)
    rep_cholesterolentry.insert(0,i)






    #image3 = PhotoImage(file="fs1.png")
    #Label(report, image=image3).pack()
    saveframe = Frame(report)
    saveframe.pack()


    lstframe = Frame(report)
    lstframe.pack()
    saved_datetime = Label(lstframe, text="Not Yet Saved !")
    saved_datetime.pack()
    idgenerated = Label(lstframe, text="ID will be generated after you save the file")
    idgenerated.pack()
    try:
        save_btn = Button(saveframe, text="SAVE", command=lambda: save(a, b, c, d, e, f, g, h, i, gender, age,idgenerated,saved_datetime))
        save_btn.grid(column=0, row=10)
    except:
        messagebox.showerror("something went wrong !","data already exists")
    #print("this id from report ,", ids)


    report.mainloop()


def check():

    if weight_entry.get()=="" or height_entry.get() == "" or bplow_entry.get() == "" or bphigh_entry.get() =="" or pulserate_entry.get() =="" or rbc_entry.get()=="" or wbc_entry.get()=="" or platelets_entry.get()=="" or hb_entry.get()=="" or uricacid_entry.get()=="" or cholesterol_entry.get() == "":
        messagebox.showwarning("Warning","All values Required")
    else:
        report()

def bmi(height,weight):
    height_mtrs = (height/100)
    rbmi=(weight//height_mtrs**2)
    #print("bmi is",rbmi)
    return rbmi

def bpcheck(lower,upper):
    if lower <= 60 or upper<=90:
        return "Low"
    elif lower<=80 or upper<=120:
        return "Medium"
    else:
        return "High"
def pulserate_check(gender,age,pulse):
    #An optimal blood pressure level is a reading under 120/80 mmHg. Readings over 120/80mmHg and up to 139/89mmHg
    # are in the normal to high range.
    #------
    if gender == 1:
        if age < 18:
            if pulse >63:
                return "High"
            elif pulse <61:
                return "Low"
            else:
                return "Medium"
        elif age<35:
            if pulse > 65:
                return "High"
            elif pulse < 62:
                return "Low"
            else:
                return "Medium"
        elif age <45:
            if pulse > 66:
                return "High"
            elif pulse < 63:
                return "Low"
            else:
                return "Medium"
        elif age <=65:
            if pulse > 67:
                return "High"
            elif pulse < 62:
                return "Low"
            else:
                return "Medium"
        elif age >65:
            if pulse > 65:
                return "High"
            elif pulse < 62:
                return "Low"
            else:
                return "Medium"
    else:
        if age < 18:
            if pulse >63:
                return "High"
            elif pulse <61:
                return "Low"
            else:
                return "Medium"
        elif age<35:
            if pulse > 68:
                return "High"
            elif pulse < 65:
                return "Low"
            else:
                return "Medium"
        elif age <45:
            if pulse > 66:
                return "High"
            elif pulse < 63:
                return "Low"
            else:
                return "Medium"
        elif age <=65:
            if pulse > 68:
                return "High"
            elif pulse < 65:
                return "Low"
            else:
                return "Medium"
        elif age >65:
            if pulse > 65:
                return "High"
            elif pulse < 62:
                return "Low"
            else:
                return "Medium"


def rbc_check(gender,rbc):
    #Normal red blood cell counts vary from around 4.7 to 6.1 million cells per microliter (µL)
    #for men and 4.2 to 5.4 million cells per µL for women. The normal count in children
    #is 4.0 to 5.5 million cells per µL
    #----
    if gender == 1:
        if rbc < 4.7:
            return "Low"
        elif rbc > 6.1:
            return "High"
        else:
            return "Medium"
    else :
        if rbc < 4.2:
            return "Low"
        elif rbc >5.4:
            return "High"
        else:
            return "Medium"


def wbc_check(wbc):
    #normal range is usually between 4,000 and 11,000 per microliter of blood.
    #----
    if wbc < 4000:
        return "Low"
    elif wbc > 11000:
        return "High"
    else :
        return "Medium"

def Platelets_check(platelets):
    #A normal platelet count ranges from 150,000 to 450,000 platelets per microliter of blood.
    #----
    if platelets < 150000:
        return "Low"
    elif platelets > 450000:
        return "High"
    else:
        return "Medium"
def hb_check(gender,hemoglobin):
    #The normal range for hemoglobin is: For men, 13.5 to 17.5 grams per deciliter.
    #  For women, 12.0 to 15.5 grams per deciliter.
    #---
    if gender == 1:
        if hemoglobin < 13.5:
            return "Low"
        elif hemoglobin > 17.5:
            return "High"
        else:
            return"Medium"
    else:
        if hemoglobin < 12.0:
            return "Low"
        elif hemoglobin > 15.5:
            return "High"
        else:
            return "Medium"

def uricacid_check(gender,uricacid):

    #Normal Uric acid levels are 2.4-6.0 mg/dL (female) and 3.4-7.0 mg/dL (male)
    #-----
    if gender == 1:
        if uricacid < 3.4:
            return "Low"
        elif uricacid > 7.0:
            return "High"
        else:
            return "Medium"
    else:
        if uricacid < 2.4:
            return "Low"
        elif uricacid > 7.0:
            return "High"
        else:
            return "Medium"

def cholesterol_check(cholesterol):
    #less than 200 milligrams per deciliter (mg/dL) are considered desirable for adults.
    # A reading between 200 and 239 mg/dL is considered borderline high
    # and a reading of 240 mg/dL and above is considered high.
    #-----
    if cholesterol <200:
        return "Low"
    elif cholesterol >240:
        return "High"
    else:
        return "Medium"



#------------------------------------------------------------------------
frame2 = Frame(root,height=200,width=200)
frame2.pack(padx = 100,pady=20)
name_label = Label(frame2,text = "Name")
name_label.grid(column = 0, row = 0)
name_entry = Entry(frame2,bd = 2)
name_entry.grid(column = 1,row = 0,pady = 10)
age_label = Label(frame2,text = "Age")
age_label.grid(column = 2,row = 0,pady = 10,)
age_entry = Entry(frame2,bd = 2)
age_entry.grid(column = 3,row = 0,pady = 10)

v= IntVar()
frame3 = Frame(root)
frame3.pack(padx=20,pady=10)
gender_label = Label(frame3,text = "Gender :",padx= 20).grid(column=0,row=0)
r1=Radiobutton(frame3,text = "Male",variable =v,value = 1)
r1.grid(column = 1,row =0)
r2=Radiobutton(frame3,text = "Female",variable =v,value = 2)
r2.grid(column = 2,row =0)
#-------------------------------------------------

frame4=Frame(root)
frame4.pack()


weight_label = Label(frame4,text = "Weight (kgs):").grid(column = 0,row =0,sticky = 'w')
weight_entry = Entry(frame4,bd=2)
weight_entry.grid(column = 2,row =0,sticky = 'e')


height_label = Label(frame4,text = "Height (cm):").grid(column = 0,row =2,sticky = 'w')
height_entry = Entry(frame4,bd=2)
height_entry.grid(column = 2,row =2,sticky = 'e')


bplow_label = Label(frame4,text = "BP low (mmHg):").grid(column = 0,row =3,sticky = 'w')
bplow_entry = Entry(frame4,bd=2)
bplow_entry.grid(column = 2,row =3,sticky = 'e')


bphigh_label = Label(frame4,text = "BP high (mmHg):").grid(column = 0,row =4,sticky = 'w')
bphigh_entry = Entry(frame4,bd=2)
bphigh_entry.grid(column = 2,row =4,sticky = 'e')


pulserate_label = Label(frame4,text = "Pulse Rate (bpm):").grid(column = 0,row =5,sticky = 'w')
pulserate_entry = Entry(frame4,bd=2)
pulserate_entry.grid(column = 2,row =5,sticky = 'e')


rbc_label = Label(frame4,text = "RBC Count (million/mm3):").grid(column = 0,row =6,sticky = 'w')
rbc_entry = Entry(frame4,bd=2)
rbc_entry.grid(column = 2,row =6,sticky = 'e')


wbc_label =Label(frame4,text = "WBC Count (cells/mm3):").grid(column = 0,row =7,sticky = 'w')
wbc_entry = Entry(frame4,bd=2)
wbc_entry.grid(column = 2,row =7,sticky = 'e')


platelets_label = Label(frame4,text = "Platelets (billion/L):").grid(column = 0,row =8,sticky = 'w')
platelets_entry = Entry(frame4,bd=2)
platelets_entry.grid(column = 2,row =8,sticky = 'e')


hb_label = Label(frame4,text = "HB (g/dl):").grid(column = 0,row =9,sticky = 'w')
hb_entry = Entry(frame4,bd=2)
hb_entry.grid(column = 2,row =9,sticky = 'e')


uricacid_label = Label(frame4,text = "Uric Acid (mg/dL):").grid(column = 0,row =10,sticky = 'w')
uricacid_entry = Entry(frame4,bd=2)
uricacid_entry.grid(column = 2,row =10,sticky = 'e')


Cholesterol_label = Label(frame4,text = "Cholesterol (mg/dL):").grid(column = 0,row =11,sticky = 'w')
cholesterol_entry = Entry(frame4,bd=2)
cholesterol_entry.grid(column = 2,row =11,sticky = 'e')

image3 = PhotoImage(file="btn1.png")
generate = Button(root,text = "Generate Report",image = image3,command = check,height = 25,width =100)
generate.pack(pady = 20)
image4 = PhotoImage(file="btn2.png")
fetchdata=Button(root,text = 'Fetch Data',image=image4,command = fetch,height = 25,width =100)
fetchdata.pack()

#Label(root,image = image3).pack()
#print(str(image3))



root.mainloop()