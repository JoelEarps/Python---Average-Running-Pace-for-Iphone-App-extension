#!/usr/bin/env python
# coding: utf-8

# In[340]:


#Python file for app extension of the app to give average times per interval
import datetime
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import pandas as pd
mins2secs = 0
avlist = []


# In[341]:

# In[343]:


def testret():
    resultString = entry1.get()
    #print(resultString)
    averageFunc(resultString)
    
# the function that gets the average of the times - 
def averageFunc(inputString):
    global times
    times = inputString.split(", ")
    #convert time values from a string to a float
    for x in (range(len(times))):
        templist = times[x].split(".")
        templist[0] = (int(templist[0])*60)
        tempres = templist[0]+int(templist[1])
        avlist.append(tempres)
    #get average times    
    avg = sum(avlist)/len(avlist)
    avg = datetime.timedelta(seconds=avg)
    print(avg)
    label1 = tk.Label(results_frame, text= avg, font=('helvetica', 9, 'bold'))
    label1.place(rely=0.4, relx=0.4)
    displayLaps(times)

def displayLaps(intervaltimes):
    df = pd.DataFrame(data=intervaltimes)
    df.index +=1
    df['Lap Number'] = df.index
    df=df.rename(columns = {0:'Lap Time'})
    col_name = "Lap Number"
    first_col = df.pop("Lap Number")
    df.insert(0, col_name, first_col)
    print(df)
    clear_data()
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column)
        
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        tv1.insert("","end", values=row)
    return df
     
        

def clear_data():
    tv1.delete(*tv1.get_children())
	
	
root = tk.Tk() #widget with a title bar - intialised
root.geometry("550x500") #root starting geometry, 500 by 500 pixels
root.pack_propagate(False) #don't repack yourself based on the things that are placed in there
root.resizable(0,0) #don't resize


# In[342]:


frame1 = tk.LabelFrame(root, text = "Interval Data", font=('helvetica', 10, 'bold'))
frame1.place(height=250, width=550)

time_frame = tk.LabelFrame(root, text="Enter Times", font=('helvetica', 10, 'bold'))
time_frame.place(height=100, width = 550, rely=0.6,relx=0)
button1 = tk.Button(time_frame, text="Upload you times", command = testret, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
entry1 = tk.Entry(time_frame) 
label1 = tk.Label(time_frame, text= "Enter your interval times, seperated with a comma and a space e.g. 3.45, 3.45, 3.50", font=('helvetica', 9, 'bold'))
label1.place(rely=0.1, relx=0.05)
entry1.place(rely=0.3, relx=0.4)
button1.place(rely=0.6, relx=0.4)
results_frame = tk.LabelFrame(root, text = "Average Pace", font=('helvetica', 10, 'bold'))
results_frame.place(height=100, width = 550, rely=0.8,relx=0)

#tree view widget - how to visualise dataframe
tv1 = ttk.Treeview(frame1)
tv1.place(relheight = 1, relwidth = 1) #place inside frame_1 as the conatiner and fill the whole conatiner

#now add a scroll bar
treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview)
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview)
tv1.configure(xscrollcommand =treescrollx.set, yscrollcommand = treescrolly.set)
treescrollx.pack(side="bottom", fill="x")
treescrolly.pack(side ="right", fill="y")





# In[344]:


root.mainloop() # main loop starts the GUI - won't appear till this is called


# In[ ]:





# times = "3.45, 3.45, 3.55"
# times = times.split(", ")
# print(times)
# df = pd.DataFrame(data=times)
# df.index +=1
# df['Lap Number'] = df.index
# df=df.rename(columns = {0:'Lap Time'})
# col_name = "Lap Number"
# first_col = df.pop("Lap Number")
# df.insert(0, col_name, first_col)
# print(df)

# In[ ]:




