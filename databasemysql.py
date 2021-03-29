from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import colorchooser
import mysql.connector
import datetime
from PIL import ImageTk, Image

root= Tk()
root.title("Blood Bank System")
root.geometry("1024x686+-8+-8")
root.configure(background='white')
root.bind("<Return>")

my_menu= Menu(root)
root.config(menu=my_menu)
root.iconbitmap("blood.ico")
now= datetime.datetime.now()

conn= mysql.connector.connect(
		host="localhost",
		user="username",
		passwd="password",
		database="blood")

c=conn.cursor()

def color():
	global my_color
	global buttn_edit
	global buttn_delete
	my_color= colorchooser.askcolor()
	root.config(menu=my_menu,background=my_color[1])
	buttn_submit.config(bg=my_color[1], activebackground=my_color[1])
	search_buttn.config(bg=my_color[1], activebackground=my_color[1])
	buttn_show.config(bg=my_color[1])
	buttn_delete.config(bg=my_color[1])
	buttn_edit.config(bg=my_color[1])

def admin_login():
	global command1
	global command2
	global entry1
	global entry2
	global top
	global bttn1

	top= Toplevel()
	top.title("Login Screen")
	top.geometry("500x500")
	top.bind("<Return>")
	top.configure(background="white")

	global admin_img
	admin_img= PhotoImage(file="12.png")

	label3= Label(top, image=admin_img, bg="white")
	label3.pack()
	global entry1
	global entry2
	label1= Label(top, text="Username", font=('Halvetica',25),bg='white')
	label1.pack()
	entry1= Entry(top, bd=5)
	entry1.pack()
	label2= Label(top, text="Password", font=('Halvetica',25),bg='white')
	label2.pack()
	entry2= Entry(top, show="*")
	entry2.pack()
	entry2.bind("<Return>", command1)
	global bttn_login
	bttn_login= PhotoImage(file="login.png")
	bttn1= Button(top, text="Login", image=bttn_login, command= lambda: command1(1), bd=0, bg="white")
	bttn1.pack()
	bttn1.bind("<Return>", command1)
	global bttn_close
	bttn_close= PhotoImage(file="close.png")
	bttn2= Button(top, text="Close", image=bttn_close, command=open_admin_panel, bd=0, bg="white")
	bttn2.pack()

	root.withdraw()

def logout():
	global buttn_edit
	global edit
	global buttn_delete
	global delete
	global	select_id_label
	global buttn_show

	buttn_edit.destroy()
	buttn_delete.destroy()
	buttn_show.destroy()
	select_id_label.destroy()
	select_id.destroy()

	global tools_menu
	tools_menu.entryconfig("Admin Login", state=NORMAL)
	tools_menu.delete("Logout")

def edit_root_window():
		#Creating buttons
		global buttn_edit
		global edit
		global buttn_delete
		global delete

		global	select_id_label
		select_id_label= Label(root,text="Select Id                  ",font=('Halvetica',10), bg="white")
		select_id_label.grid(row=10,column=0, stick=W,pady=2)

		global select_id
		select_id = Entry(root,bd=5,bg="white",font=('Halvetica',10))
		select_id.grid(row=10,column=1, stick=W+E+N+S,pady=2, padx=3)	

		global bttn_edit_img
		bttn_edit_img= PhotoImage(file='3.png')
		global buttn_edit
		buttn_edit= Button(root, text="Update Record",image=bttn_edit_img,command=lambda: edit(1), pady=5, bd=0, bg="white",font=('Halvetica',10))
		buttn_edit.grid(row=11,column=0,columnspan=2, stick=W+E+N+S, padx=3)
		buttn_edit.bind("<Return>", edit)

		global bttn_delete_img
		bttn_delete_img= PhotoImage(file='2.png')
		global buttn_delete
		buttn_delete= Button(root, text="Delete Record",image=bttn_delete_img,command=lambda: delete(1), pady=5, bd=0, bg="white",font=('Halvetica',10))
		buttn_delete.grid(row=12,column=0,columnspan=2, stick=W+E+N+S, padx=3)
		buttn_delete.bind("<Return>", delete)

		global sort
		sortby=["Sort By..",
				"Name",
				"Gender",
				"Blood Group",
				"Date Update"
					]

		sort= ttk.Combobox(root, value=sortby)
		sort.set("Sort By..")
		sort.grid(row=13,column=1, stick=W+E+N+S,pady=2)
		
		global sort_label
		sort_label= Label(root,text="Sort By                   ",font=('Halvetica',10), bg="white")
		sort_label.grid(row=13,column=0, stick=W,pady=2, padx=3)

		global enter_name
		enter_name = Entry(root, bd=5, bg="white",font=('Halvetica',10))
		enter_name.grid(row=14, column=0, columnspan=2, stick=W+E+N+S, pady=2, padx=3)

		global bttn_show
		bttn_show= PhotoImage(file='5.png')
		global buttn_show
		buttn_show= Button(root, text="Show All", image=bttn_show, command=lambda:show(1), pady=5, bd=0, bg="white",font=('Halvetica',10))
		buttn_show.grid(row=15,column=0,columnspan=2, stick=W+E+N+S, padx=3)
		buttn_show.bind("<Return>", show)

		global tools_menu
		tools_menu.entryconfig("Admin Login", state=DISABLED)

		tools_menu.add_cascade(label='Logout', command=logout)

		if my_color:
			buttn_show.config(bg=my_color[1])
			buttn_delete.config(bg=my_color[1])
			buttn_edit.config(bg=my_color[1])

def command1(e):
	if entry1.get()=="admin" and entry2.get()== "admin" or entry1.get()=="root" and entry2.get()== "root":
		root.deiconify()
		top.destroy()

		edit_root_window()

	else:
		messagebox.showerror("Error", "Please Enter Valid Username or Password")
		entry1.delete(0, END)
		entry2.delete(0, END)

def open_admin_panel():
	root.deiconify()
	top.destroy()

def new_file():
	pass

def find():
	pass

def find_next():
	pass

def next_file():
	pass

def previous_file():
	pass

def contact_us():
	pass

def read_tnc():
	pass

def submit(e):
	# Label(root,text=full_name.get() +gender.get()+address.get()+city.get()+state.get()+zip_code.get()).grid(row=7,column=0)
	if full_name.get() =="" or drop.get() == "Select gender" or drop_blood.get()== "Select Blood Group" or address.get() =="" or contact.get()== "" or city.get() =="" or state.get()== "Select State" or zip_code.get() =="":
		messagebox.showinfo("Error", "Enter Valid Details !!!! ")
			
	else:
		try:
			conn= mysql.connector.connect(
			host="localhost",
			user="username",
			passwd="password",
			database="blood"

			)

			decide=messagebox.askyesno("Confirmation","You Want To Save These Details")
			if decide == 1:
				c=conn.cursor()	
				c.execute("INSERT INTO donors(name, gender, blood_group, address, contact, city, state, zip_code, date_updated) VALUES  ('"+full_name.get().title()+"','"+drop.get()+"','"+drop_blood.get()+"','"+address.get().title()+"','"+contact.get()+"','"+city.get().title()+"','"+state.get()+"','"+zip_code.get()+"', '"+now.strftime("%Y/%m/%d")+"')")
				
				messagebox.showinfo("Success", "Record Submitted Successfully")
				full_name.delete(0, END)
				drop.set("Select gender")
				drop_blood.set("Select Blood Group")
				address.delete(0, END)
				contact.delete(0, END)
				city.delete(0, END)
				state.set("Select State")
				zip_code.delete(0, END)

			conn.commit()
			conn.close()	
		except Exception as e:
			print(e)
			messagebox.showinfo("Error", "Enter Correct zip Code or contact no. !!! ")				

def exit(e):
	root.destroy()

def show(e):
	try:
		
		conn= mysql.connector.connect(
			host="localhost",
			user="username",
			passwd="password",
			database="blood"

			)
		
		c=conn.cursor()
		
		global result
		if sort.get()=="Sort By..":
			c.execute("SELECT * FROM donors")
			result=c.fetchall()
			
		elif sort.get()=="Name":
			if enter_name.get()=="":
				c.execute("SELECT * FROM donors order by name")
				result=c.fetchall()
				
			else:
				c.execute("SELECT * FROM donors WHERE name=('"+enter_name.get().title()+"')")
				result=c.fetchall()

		elif sort.get()=="Date Update":
			c.execute("SELECT * FROM donors order by date_updated desc")
			result=c.fetchall()
			

		elif sort.get()=="Gender":
			c.execute("SELECT * FROM donors order by gender")
			result=c.fetchall()
			
		elif sort.get()=="Blood Group":
			c.execute("SELECT * FROM donors order by blood_group")
			result=c.fetchall()

		conn.commit()
		conn.close()

		sort.set("Sort By..")
		enter_name.delete(0,END)
		
		if len(result) ==0:
			messagebox.showerror("Error", "No Record Found")

		else:
			show_windows()

	except Exception as e:
		messagebox.showerror("Error", "Error Occured")

def show_windows():
	global show_window
	show_window= Toplevel()
	show_window.title("Show records")
	show_window.geometry("1024x686+-8+-8")
	show_window.config(bg='white')
	
	main_frame= Frame(show_window)
	main_frame.pack(fill=BOTH, expand=1)

	my_canvas= Canvas(main_frame,bg='white')
	my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

	my_scrollbar= ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
	my_scrollbar.pack(side=RIGHT, fill=Y)

	my_canvas.configure(yscrollcommand=my_scrollbar.set)
	my_canvas.bind('<Configure>' , lambda e: my_canvas.configure(scrollregion= my_canvas.bbox("all")))

	second_frame = Frame(my_canvas,bg='white')

	my_canvas.create_window((0,0), window=second_frame, anchor="nw")


	global label_show
	label_list=[
			"Id",
			"Name",
			"Gender",
			"Blood Group",
			"Address",
			"Contact",
			"City",
			"State",
			"Zip Code",
			"Date Updated"
	]

	for ind, k in enumerate(label_list):
		top_label= Label(second_frame,text=k,bg="white")
		top_label.grid(row=0,column=ind,stick=W, padx=5)

	for index, i in enumerate(result):
		num=0
		for j in i:
			label_show=Label(second_frame,text=j,bg="white")
			label_show.grid(row=index+1,column=num, stick=W, padx=5)
			num+=1
		
def delete(e):
	if select_id.get()== "":
		messagebox.showinfo("Caution", "Enter Valid Id")
		select_id.delete(0, END)
	else:
		try:
			conn= mysql.connector.connect(
			host="localhost",
			user="username",
			passwd="password",
			database="blood"

			)

			c=conn.cursor()
			c.execute("SELECT * FROM donors WHERE iddonors=('"+select_id.get()+"')")
			global res
			res=c.fetchall()
			conn.commit()
			conn.close()

			if len(res) == 0:
				messagebox.showinfo("Error","Record Not Found")
				select_id.delete(0, END)

			else:
				conn= mysql.connector.connect(
				host="localhost",
				user="username",
				passwd="password",
				database="blood"

				)

				c=conn.cursor()
				
				c.execute("DELETE FROM donors WHERE iddonors=('"+select_id.get()+"')")

				conn.commit()

				conn.close()

				show()

				messagebox.showinfo("Success","Successfully Deleted Record")
				select_id.delete(0, END)


		except Exception as e:
			messagebox.showinfo("Error", "Enter Valid Id")
			select_id.delete(0, END)

def update(e):
	if full_name_editor.get() =="" or dro.get() == "Select gender" or dro_blood.get()== "Select Blood Group" or address_editor.get() =="" or contact_editor.get()== "" or city_editor.get() =="" or dro_state.get()== "Select State" or zip_code_editor.get() =="":
		messagebox.showinfo("Error", "Enter Valid Details !!!! ")
	else:
		try:

			conn= mysql.connector.connect(
					host="localhost",
					user="username",
					passwd="password",
					database="blood")

			c=conn.cursor()

			c.execute("UPDATE donors SET name=('"+full_name_editor.get().title()+"'), gender=('"+dro.get()+"'), blood_group=('"+dro_blood.get()+"'), address=('"+address_editor.get().title()+"'), contact=('"+contact_editor.get()+"'), city=('"+city_editor.get().title()+"'), state=('"+dro_state.get()+"'), zip_code=('"+zip_code_editor.get()+"'), date_updated=('"+now.strftime("%Y/%m/%d")+"') WHERE iddonors=('"+select_id.get()+"')") 

			conn.commit()
			conn.close()

			messagebox.showinfo("Success!", "Successfully Updated Record !")
			editor.destroy()
			select_id.delete(0, END)
			show(e)
		except Exception as e:
			print(e)
			messagebox.showinfo("Error", "Error Occured...")

def edit(e):
	if select_id.get()=="":
		messagebox.showinfo("Caution", "Enter Valid Id")
		select_id.delete(0, END)

	else:
		try:
			global editor
			editor= Toplevel()
			editor.title("Edit Record")
			
			global full_name_editor
			global gender_editor
			global blood_group_editor
			global address_editor
			global contact_editor
			global city_editor
			global state_editor
			global zip_code_editor
			global dro
			global dro_blood
			global dro_state

			dro= StringVar()
			dro_state= StringVar()
			dro_blood= StringVar()
			

			full_name_editor= Entry(editor,bd=5)
			full_name_editor.grid(row=0,column=1, stick=W+E)
			gender_editor=OptionMenu(editor,dro, "Select gender", "Male", "Female", "Other")
			gender_editor.grid(row=1,column=1, stick=W+E)
			blood_group_editor= OptionMenu(editor,dro_blood, *bloodgroups)
			blood_group_editor.grid(row=2,column=1, stick=W+E)
			address_editor= Entry(editor,bd=5)
			address_editor.grid(row=3,column=1, stick=W+E)
			contact_editor= Entry(editor,bd=5)
			contact_editor.grid(row=4,column=1, stick=W+E)
			city_editor= Entry(editor,bd=5)
			city_editor.grid(row=5,column=1, stick=W+E)
			state_editor= OptionMenu(editor,dro_state, *states)
			state_editor.grid(row=6,column=1, stick=W+E)
			zip_code_editor= Entry(editor,bd=5)
			zip_code_editor.grid(row=7,column=1, stick=W+E)	

			full_name_label_editor= Label(editor,text="Full Name")
			full_name_label_editor.grid(row=0,column=0, stick=W+E)
			gender_label_editor=Label(editor,text="Gender")
			gender_label_editor.grid(row=1,column=0, stick=W+E)
			blood_group_label_editor= Label(editor,text="Enter Blood Group")
			blood_group_label_editor.grid(row=2,column=0, stick=W+E)
			address_label_editor= Label(editor,text="Address")
			address_label_editor.grid(row=3,column=0, stick=W+E)
			contact_label_editor= Label(editor, text="Contact No.")
			contact_label_editor.grid(row=4,column=0, stick=W+E)
			city_label_editor= Label(editor,text="City")
			city_label_editor.grid(row=5,column=0, stick=W+E)
			state_label_editor= Label(editor,text="State")
			state_label_editor.grid(row=6,column=0, stick=W+E)
			zip_code_label_editor= Label(editor,text="Zip Code")
			zip_code_label_editor.grid(row=7,column=0, stick=W+E)
			
			buttn_save= Button(editor, text="Save",command=lambda: update(1), pady=5,bg="green")
			buttn_save.grid(row=8,column=0,columnspan=2, stick=W+E, pady=5)
			buttn_save.bind("<Return>", update)

			conn= mysql.connector.connect(
			host="localhost",
			user="username",
			passwd="password",
			database="blood"

			)	
			c=conn.cursor()
			

			c.execute("SELECT * FROM donors WHERE iddonors=('"+select_id.get()+"')")
			result= c.fetchall()

			for rslt in result:
				full_name_editor.insert(0, rslt[1])
				dro.set(rslt[2])
				dro_blood.set(rslt[3])
				address_editor.insert(0, rslt[4])
				contact_editor.insert(0, rslt[5])
				city_editor.insert(0, rslt[6])
				dro_state.set(rslt[7])
				zip_code_editor.insert(0, rslt[8])
				

			conn.commit()

			conn.close()
			
			editor.mainloop()

		except Exception as e:
			messagebox.showinfo("Error","Please Enter Valid Id")

def search(e):

	global select_blood
	if select_blood.get() == "Select Blood Group":
		messagebox.showinfo("Caution", "Enter Valid Blood Group")
		select_blood.delete(0, END)
	else:
		conn= mysql.connector.connect(
			host="localhost",
			user="username",
			passwd="password",
			database="blood")

		c= conn.cursor()
		c.execute("SELECT name, gender,blood_group,contact,city,state,date_updated FROM donors WHERE blood_group=('"+select_blood.get()+"') order by date_updated desc")
		re=c.fetchall()

		conn.commit()
		conn.close()

		if len(re) ==0:
			messagebox.showinfo("Error", "NO Record Found")

		else:
			search_window= Toplevel()
			search_window.title("Search Result")
			search_window.config(bg="white")
			search_window.geometry("1024x686+-8+-8")

			main_frame= Frame(search_window)
			main_frame.pack(fill=BOTH, expand=1)

			my_canvas= Canvas(main_frame,bg='white')
			my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

			my_scrollbar= ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
			my_scrollbar.pack(side=RIGHT, fill=Y)

			my_canvas.configure(yscrollcommand=my_scrollbar.set)
			my_canvas.bind('<Configure>' , lambda e: my_canvas.configure(scrollregion= my_canvas.bbox("all")))

			second_frame = Frame(my_canvas,bg='white')

			my_canvas.create_window((0,0), window=second_frame, anchor="nw")
			global label_show
			label_list=[
					"Name",
					"Gender",
					"Blood Group",
					"Contact",
					"City",
					"State",
					"Date Updated"
			]

			for ind, k in enumerate(label_list):
				top_label= Label(second_frame,text=k,bg="white")
				top_label.grid(row=0,column=ind,stick=W, padx=5)
			
			for index, i in enumerate(re):
				num=0
				for j in i:
					label_show=Label(second_frame,text=j,bg="white")
					label_show.grid(row=index+1,column=num, stick=W, padx=5)
					num+=1
		select_blood.set("Select Blood Group")

def menus():
	# Creating menus
	global file_menu
	global my_menu
	global edit_menu
	global tools_menu
	global help_menu

	file_menu= Menu(my_menu, tearoff=False)
	my_menu.add_cascade(label='File', menu=file_menu)
	file_menu.add_cascade(label='New...', command=new_file)
	file_menu.add_separator()
	file_menu.add_cascade(label='Exit', command=root.quit)

	edit_menu= Menu(my_menu, tearoff=False)
	my_menu.add_cascade(label='Edit', menu=edit_menu)
	edit_menu.add_cascade(label='Find', command=find)
	edit_menu.add_cascade(label='Find next', command=find_next)

	tools_menu= Menu(my_menu, tearoff=False)
	my_menu.add_cascade(label='Tools', menu=tools_menu)
	tools_menu.add_cascade(label='Next', command=next_file)
	tools_menu.add_cascade(label='Previous', command=previous_file)
	tools_menu.add_cascade(label='Background Color', command=color)
	tools_menu.add_cascade(label='Admin Login', command=admin_login)

	help_menu= Menu(my_menu, tearoff=False)
	my_menu.add_cascade(label='Help', menu=help_menu)
	help_menu.add_cascade(label='Contact Us', command=contact_us)
	help_menu.add_cascade(label='Read T&C..', command=read_tnc)

def button_label():
	# Creating main heading label
	global head
	head= Label(root,text= "Blood Donation Portal", font=('Halvetica',25),bg='white')
	head.grid(row=0,column=0,columnspan=2)

	global states
	global bloodgroups
	# States Lists
	states = [
			"Select State",
			 "Andhra Pradesh",
			 "Arunachal Pradesh ",
			 "Assam",
			 "Bihar",
			 "Chhattisgarh",
			 "Goa",
			 "Gujarat",
			 "Haryana",
			 "Himachal Pradesh",
			 "Jammu and Kashmir",
			 "Jharkhand",
			 "Karnataka",
			 "Kerala",
			 "Madhya Pradesh",
			 "Maharashtra",
			 "Manipur",
			 "Meghalaya",
			 "Mizoram",
			 "Nagaland",
			 "Odisha",
			 "Punjab",
			 "Rajasthan",
			 "Sikkim",
			 "Tamil Nadu",
			 "Telangana",
			 "Tripura",
			 "Uttar Pradesh",
			 "Uttarakhand",
			 "West Bengal",
			 "Andaman and Nicobar Islands",
			 "Chandigarh",
			 "Dadra and Nagar Haveli",
			 "Daman and Diu",
			 "Lakshadweep",
			 "National Capital Territory of Delhi",
			 "Puducherry"
		]
	# Blood Groups Lists
	bloodgroups=[
				"Select Blood Group",
				"A+",
				"A-",
				"B+",
				"B-",
				"O+",
				"O-",
				"AB+",
				"AB-"

			]

	# Creating entry widgets
	global full_name
	global drop
	global gender
	global drop_blood
	global blood_group
	global address
	global contact
	global city
	global state
	global zip_code
	full_name= Entry(root,bd=5,bg="white",font=('Halvetica',10))
	full_name.grid(row=1,column=1, stick=W+E+N+S,pady=2)
	drop= StringVar()
	gender=OptionMenu(root,drop, "Select gender", "Male", "Female", "Other")
	drop.set("Select gender")
	gender.grid(row=2,column=1, stick=W+E+N+S,pady=2)
	drop_blood= StringVar()
	blood_group= OptionMenu(root,drop_blood, *bloodgroups)
	drop_blood.set("Select Blood Group")
	blood_group.grid(row=3,column=1, stick=W+E+N+S,pady=2)
	address= Entry(root,bd=5,bg="white",font=('Halvetica',10))
	address.grid(row=4,column=1, stick=W+E+N+S,pady=2)
	contact= Entry(root,bd=5,bg="white",font=('Halvetica',10))
	contact.grid(row=5,column=1, stick=W+E+N+S,pady=2)
	city= Entry(root,bd=5,bg="white",font=('Halvetica',10))
	city.grid(row=6,column=1, stick=W+E+N+S,pady=2)
	state= ttk.Combobox(root, value=states)
	state.set("Select State")
	state.grid(row=7,column=1, stick=W+E+N+S,pady=2)
	zip_code= Entry(root,bd=5,bg="white",font=('Halvetica',10))
	zip_code.grid(row=8,column=1, stick=W+E+N+S,pady=2)

	# Creating submit and show buttons
	global bttn_submit
	bttn_submit= PhotoImage(file='1.png')
	global buttn_submit
	buttn_submit= Button(root, text="Submit", image=bttn_submit, command=lambda: submit(1), bd=0, pady=5, bg="white",font=('Halvetica',10))
	buttn_submit.grid(row=9,column=0,columnspan=2, stick=W+E+N+S, pady=(5,0), padx=3)
	buttn_submit.bind("<Return>", submit)


	# creating labels
	global full_name_label
	global gender_label
	global blood_group_label
	global address_label
	global contact_label
	global city_label
	global state_label
	global zip_code_label
	full_name_label= Label(root,text="Full Name               ",font=('Halvetica',10), bg="white")
	full_name_label.grid(row=1,column=0, stick=W,pady=2, padx=3)
	gender_label=Label(root,text="Gender                   ",font=('Halvetica',10), bg="white")
	gender_label.grid(row=2,column=0, stick=W,pady=2, padx=3)
	blood_group_label= Label(root,text="Enter Blood Group   ",font=('Halvetica',10), bg="white")
	blood_group_label.grid(row=3,column=0, stick=W,pady=2, padx=3)
	address_label= Label(root,text="Address                  ",font=('Halvetica',10), bg="white")
	address_label.grid(row=4,column=0, stick=W,pady=2, padx=3)
	contact_label= Label(root, text="Contact No.             ",font=('Halvetica',10), bg="white")
	contact_label.grid(row=5,column=0, stick=W,pady=2, padx=3)
	city_label= Label(root,text="City                        ",font=('Halvetica',10), bg="white")
	city_label.grid(row=6,column=0, stick=W,pady=2, padx=3)
	state_label= Label(root,text="State                      ",font=('Halvetica',10), bg="white")
	state_label.grid(row=7,column=0, stick=W,pady=2, padx=3)
	zip_code_label= Label(root,text="Zip Code                 ",font=('Halvetica',10), bg="white")
	zip_code_label.grid(row=8,column=0, stick=W,pady=2, padx=3)

	# global bttn_exit
	# bttn_exit= PhotoImage(file='exit.png')
	# buttn_exit= Button(root, text="Exit",image=bttn_exit, command=lambda: exit(1), pady=5, bd=5, bg="red",font=('Halvetica',10))
	# buttn_exit.grid(row=14,column=0,columnspan=2, stick=W+E+N+S)
	# buttn_exit.bind("<Return>", exit)


	# Creating Labels for search
	global head_1
	head_1 = Label(root,text= "Search For Donor", font=('Halvetica',25),bg='white')
	head_1.grid(row=0, column=2,columnspan=2,stick=W+E+N+S, padx=50)

	global label_blood
	label_blood= Label(root,text="Select Blood Group       ",font=('Halvetica',10), bg="white")
	label_blood.grid(row=1, column=2, stick=W, pady=2, padx=50)

	global select_blood
	select_blood= ttk.Combobox(root, value=bloodgroups)
	select_blood.set("Select Blood Group")
	select_blood.grid(row=1, column=3, stick=W, pady=2, padx=50)


	# Creating Search Button to search donors
	global bttn_search
	bttn_search= PhotoImage(file='4.png')
	global search_buttn
	search_buttn= Button(root, text="Search For Donors",image=bttn_search, command=lambda: search(1), bg="white", pady=2, bd=0, font=('Halvetica',10))
	search_buttn.grid(row=2, column=2, columnspan=2, stick=W+E+N+S, padx=50)
	search_buttn.bind("<Return>", search)

menus()
button_label()


conn.commit()

conn.close()


root.mainloop()