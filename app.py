from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from dbhelper import DBHelper
import shutil


class Tinder:

    def __init__(self):

        self.db = DBHelper()
        # Load GUI
        self.load_login_window()

    def load_login_window(self):
        self._root = Tk()
        self._root.iconbitmap(r'C:\Users\WIN8\PycharmProjects\Tinder\tinder.ico')
        self._root.title("Finderr | Find. Propose. Match")
        self._root.minsize(400, 650)
        self._root.maxsize(400, 650)
        self._root.config(background="#FE3C72")

        self._image = PhotoImage(file='logo.png')
        self._label1 = Label(self._root, fg="#fff", bg="#FE3C72",image=self._image, compound=LEFT)
        self._label1.config(font=("Monsterrat", 30))
        self._label1.pack(pady=(10,0))

        self._label2 = Label(self._root, text="finderr", fg="#fff", bg="#FE3C72")
        self._label2.config(font=("Monsterrat", 40))
        self._label2.pack(pady=(10,0))

        self._label4 = Label(self._root, text="One step destination to find LOVED ONES", fg="#fff", bg="#FE3C72")
        self._label4.pack(pady=(0,20))

        self._email = Label(self._root, text="Email", fg="#fff", bg="#FE3C72")
        self._email.config(font=("Monsterrat", 16))
        self._email.pack(pady=(5, 5))

        self._emailInput = Entry(self._root)
        self._emailInput.pack(pady=(5, 10), ipady=5, ipadx=15)

        self._password = Label(self._root, text="Password", fg="#fff", bg="#FE3C72")
        self._password.config(font=("Monsterrat", 16))
        self._password.pack(pady=(5, 5))

        self._passwordInput = Entry(self._root, show="*")
        self._passwordInput.pack(pady=(5, 20), ipady=5, ipadx=15)

        self._img=PhotoImage(file='login.png')
        self._img=self._img.subsample(2,2)
        self._login = Button(self._root, text="Login", bg="#fff", fg="#FE3C72", font=('Monsterrat',10,'bold'), image=self._img, compound=LEFT, relief=RIDGE, width=150, height=35,
                             command=lambda: self.check_login())
        self._login.pack(pady=(10,5))

        self._lab=Label(self._root,text="---------------OR----------------",fg="#fff", bg="#FE3C72")
        self._lab.pack()

        self._img1 = PhotoImage(file='signup.png')
        self._img1 = self._img1.subsample(2, 2)
        self._reg = Button(self._root, text="Sign Up", bg="#fff", fg="#FE3C72", font=('Monsterrat',10,'bold'),image=self._img1, compound=LEFT, relief=RIDGE, width=150, height=35,
                             command=lambda: self.regWindow())
        self._reg.pack(pady=(5,10))
        self._label3=Label(self._root, text="""By clicking Sign Up, you agree to our Terms. Learn how we 
    process your data in our Privacy Policy and Cookie Policy.""", fg="#fff", bg="#FE3C72")
        self._label3.pack(pady=(10,10))

        self._root.mainloop()

    def check_login(self):
        email = self._emailInput.get()
        password = self._passwordInput.get()

        data = self.db.check_login(email, password)

        # print(data)
        if len(data) == 0:
            # print("Invalid Credentials")
            messagebox.showerror("Error", "Invalid Credentials")
        else:
            self.user_id = data[0][0]
            self.gender = data[0][5]
            self.is_logged_in = 1
            self.login_handler()

    def regWindow(self):
        self.clear()
        self._name = Label(self._root, text="Name", fg="#fff", bg="#FE3C72")
        self._name.config(font=("Monsterrat", 16))
        self._name.pack(pady=(5, 5))
        self._nameInput = Entry(self._root)
        self._nameInput.pack(pady=(5, 5), ipady=5, ipadx=20)

        self._email = Label(self._root, text="Email", fg="#fff", bg="#FE3C72")
        self._email.config(font=("Monsterrat", 16))
        self._email.pack(pady=(5, 5))
        self._emailInput = Entry(self._root)
        self._emailInput.pack(pady=(5, 5), ipady=5, ipadx=20)

        self._password = Label(self._root, text="Password", fg="#fff", bg="#FE3C72")
        self._password.config(font=("Monsterrat", 16))
        self._password.pack(pady=(5, 5))

        self._passwordInput = Entry(self._root, show='*')
        self._passwordInput.pack(pady=(5, 5), ipady=5, ipadx=20)

        self._age = Label(self._root, text="Age", fg="#fff", bg="#FE3C72")
        self._age.config(font=("Monsterrat", 16))
        self._age.pack(pady=(5, 5))
        self._ageInput = Entry(self._root)
        self._ageInput.pack(pady=(5,5), ipady=5, ipadx=20)

        self._gender = Label(self._root, text="Gender", fg="#fff", bg="#FE3C72")
        self._gender.config(font=("Monsterrat", 16))
        self._gender.pack(pady=(5, 5))
        self._genderInput = Entry(self._root)
        self._genderInput.pack(pady=(5,5), ipady=5, ipadx=20)

        self._city = Label(self._root, text="City", fg="#fff", bg="#FE3C72")
        self._city.config(font=("Monsterrat", 16))
        self._city.pack(pady=(5, 5))
        self._cityInput = Entry(self._root)
        self._cityInput.pack(pady=(5, 5), ipady=5, ipadx=20)

        self._dp = Button(self._root,fg="#fff",bg="#FE3C72",text="Selct a Profile Picture",font=('Monsterrat',10,'bold'),relief=RIDGE,command = lambda : self._selct_dp())
        self._dp.pack(pady=(10,5), ipady=5, ipadx=10)

        self.dp_filename=Label(self._root,bg="#FE3C72")
        self.dp_filename.pack()

        self._img2 = PhotoImage(file='back.png')

        self._back = Button(self._root, text="  Back", bg="#fff", fg="#FE3C72", font=('Monsterrat',10,'bold'),image=self._img2, compound=LEFT, relief=RIDGE, width=150, height=35,
                             command=lambda: self.back())
        self._back.pack(padx=20,pady=10,side=LEFT)

        self._signup = Button(self._root, text="Sign Up", bg="#fff", fg="#FE3C72", font=('Monsterrat',10,'bold'),image=self._img1, compound=LEFT, relief=RIDGE, width=150, height=35,
                             command=lambda: self.reg_handler())
        self._signup.pack(padx=10,pady=10,side=LEFT)

    def _selct_dp(self):

        self.filename = filedialog.askopenfilename(initialdir="/images", title="something")
        self.dp_filename.config(text=self.filename)

    def back(self):
        self._root.destroy()
        self.load_login_window()

    def reg_handler(self):
        self.actual_filename = self.filename.split("/")[-1]
        flag=self.db.register(self._nameInput.get(),self._emailInput.get(),self._passwordInput.get(),self._ageInput.get(),self._genderInput.get(),self._cityInput.get(),self.actual_filename)
        if flag == 1:

            self.destination = "C:\\Users\\WIN8\\PycharmProjects\\Tinder\\Images\\" + self.actual_filename
            shutil.copyfile(self.filename,self.destination)
            messagebox.showinfo("Sucess!","Registered Sucessfully! Login Now.")
            self._root.destroy()
            self.load_login_window()
        else:
            messagebox.showerror("Error", "Try Again")


    def mainWindow(self, data, flag=0, index=0):

        name = "Name: " + str(data[index][1])
        email = "Email: " + str(data[index][2])
        age = "Age: " + str(data[index][4])
        gender = "Gender: " + str(data[index][5])
        city = "City: " + str(data[index][6])
        dp = data[index][7]

        try:
            imageUrl = "images/{}".format(data[index][7])

            load = Image.open(imageUrl)
            load = load.resize((300, 300), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)

            img = Label(image=render)
            img.image = render
            img.pack()
        except:
            image_label = Label(self._root, text="No Image found", fg="#fff", bg="#FE3C72")
            image_label.config(font=("Arial", 16))
            image_label.pack(pady=(20, 10))

        # Display remaining info about the user

        name_label = Label(self._root, text=name, fg="#fff", bg="#FE3C72")
        name_label.config(font=("Arial", 16))
        name_label.pack(pady=(20, 10))


        age_label = Label(self._root, text=age, fg="#fff", bg="#FE3C72")
        age_label.config(font=("Arial", 12))
        age_label.pack(pady=(5, 10))

        gender_label = Label(self._root, text=gender, fg="#fff", bg="#FE3C72")
        gender_label.config(font=("Arial", 12))
        gender_label.pack(pady=(5, 10))

        city_label = Label(self._root, text=city, fg="#fff", bg="#FE3C72")
        city_label.config(font=("Arial", 12))
        city_label.pack(pady=(5, 10))

        if flag == 1:
            frame = Frame(self._root, bg="#FE3C72")
            frame.pack()

            previous = Button(frame, text="Previous", command=lambda: self.view_others(index - 1))
            previous.pack(side=LEFT, padx=5, ipadx=10)
            propose = Button(frame, text="Propose", command=lambda: self.propose(self.user_id, data[index][0]))
            propose.pack(side=LEFT, padx=5, ipadx=10)
            next = Button(frame, text="Next", command=lambda: self.view_others(index + 1))
            next.pack(side=LEFT, padx=5, ipadx=20)
        elif flag==2:
            frame = Frame(self._root, bg="#FE3C72")
            frame.pack()

            previous = Button(frame, text="Previous", command=lambda: self.view_proposals(index - 1))
            previous.pack(side=LEFT, padx=5, ipadx=10)
            propose = Button(frame, text="Propose", command=lambda: self.propose(self.user_id, data[index][0]))
            propose.pack(side=LEFT, padx=5, ipadx=10)
            next = Button(frame, text="Next", command=lambda: self.view_proposals(index + 1))
            next.pack(side=LEFT, padx=5, ipadx=20)
        elif flag==3:
            frame = Frame(self._root, bg="#FE3C72")
            frame.pack()

            previous = Button(frame, text="Previous", command=lambda: self.view_requests(index - 1))
            previous.pack(side=LEFT, padx=5, ipadx=10)
            next = Button(frame, text="Next", command=lambda: self.view_requests(index + 1))
            next.pack(side=LEFT, padx=5, ipadx=20)
        elif flag==4:
            frame = Frame(self._root, bg="#FE3C72")
            frame.pack()

            previous = Button(frame, text="Previous", command=lambda: self.view_matches(index - 1))
            previous.pack(side=LEFT, padx=5, ipadx=10)
            next = Button(frame, text="Next", command=lambda: self.view_matches(index + 1))
            next.pack(side=LEFT, padx=5, ipadx=20)



    def propose(self, romeo, juliet):
        flag = self.db.insert_proposal(romeo, juliet)
        if flag == 1:
            messagebox.showinfo("Congrats", "Proposal Sent. Fingers Crossed!")
        elif flag == 2:
            messagebox.showerror("Sorry!", "Proposal already sent!")
        else:
            messagebox.showerror("Sorry!", "Unable to sent Request!")

    def login_handler(self):
        # To load user's profile
        # clear screen
        self.clear()
        self.headerMenu()
        data = self.db.fetch_userdata(self.user_id)
        self.mainWindow(data, flag=0)

    def clear(self):
        for i in self._root.pack_slaves():
            i.destroy()

    def view_others(self, index=0):

        # fetch data of all other users from db
        data = self.db.fetch_otheruserdata(self.user_id, self.gender)
        if index == 0:
            self.clear()
            self.mainWindow(data, flag=1, index=0)
        else:
            if index < 0:
                messagebox.showerror("No User Found", "Click on Next")
            elif index == len(data):
                messagebox.showerror("No User Left", "Click on Previous")
            else:
                self.clear()
                self.mainWindow(data, flag=1, index=index)

    def logout(self):
        self.is_logged_in = 0
        self._root.destroy()
        self.load_login_window()

    def headerMenu(self):
        menu = Menu(self._root)
        self._root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Home", menu=filemenu)
        filemenu.add_command(label="My Profile", command = lambda : self.login_handler())
        filemenu.add_command(label="Edit Profile", command = lambda : self.edit_profile())
        filemenu.add_command(label="View Profile", command=lambda: self.view_others())
        filemenu.add_command(label="LogOut", command=lambda: self.logout())

        helpmenu = Menu(menu)
        menu.add_cascade(label="Proposals", menu=helpmenu)
        helpmenu.add_command(label="My Proposals", command = lambda : self.view_proposals())
        helpmenu.add_command(label="My Requests", command = lambda : self.view_requests())
        helpmenu.add_command(label="My Matches", command = lambda : self.view_matches())


    def edit_profile(self):

        data = self.db.fetch_userdata(self.user_id)


        self.clear()
        self._password = Label(self._root, text="Password", fg="#fff", bg="#FE3C72")
        self._password.config(font=("Monsterrat", 16))
        self._password.pack(pady=(5, 5))

        self._passwordInput = Entry(self._root, show='*')
        self._passwordInput.insert(0,data[0][3])
        self._passwordInput.pack(pady=(5, 5), ipady=5, ipadx=20)
        self._age = Label(self._root, text="Age", fg="#fff", bg="#FE3C72")
        self._age.config(font=("Monsterrat", 16))
        self._age.pack(pady=(5, 5))
        self._ageInput = Entry(self._root)
        self._ageInput.insert(0, data[0][4])
        self._ageInput.pack(pady=(5, 5), ipady=5, ipadx=20)
        self._city = Label(self._root, text="City", fg="#fff", bg="#FE3C72")
        self._city.config(font=("Monsterrat", 16))
        self._city.pack(pady=(5, 5))
        self._cityInput = Entry(self._root)
        self._cityInput.insert(0, data[0][6])
        self._cityInput.pack(pady=(5, 5), ipady=5, ipadx=20)

        self._update = Button(self._root, fg="#fff", bg="#FE3C72", text="Update Info",
                          font=('Monsterrat', 10, 'bold'), relief=RIDGE, command=lambda: self.update_info())
        self._update.pack(pady=(10, 5), ipady=5, ipadx=10)



    def update_info(self):

        flag = self.db.update_info(self._passwordInput.get(), self._ageInput.get(), self._cityInput.get(), self.user_id)
        if flag == 1:
            messagebox.showinfo("Success", "Profile Updated")
        else:
            messagebox.showerror("Error","Some Error Occured. Try Again")


    def view_proposals(self,index=0):
        try:
            data=self.db.fetch_proposals(self.user_id)

            new_data=[]
            for i in data:
                new_data.append(i[3:])

            if index==0:
                self.clear()
                self.mainWindow(new_data,flag=2,index=0)
            else:
                if index < 0:
                    messagebox.showerror("No User Found", "Click on Next")
                elif index == len(new_data):
                    messagebox.showerror("No User Left", "Click on Previous")
                else:
                    self.clear()
                    self.mainWindow(new_data, flag=2, index=index)
        except:
            messagebox.showerror("Sorry!", "No Proposals Found")

    def view_requests(self, index=0):
        try:
            data = self.db.fetch_requests(self.user_id)

            new_data = []
            for i in data:
                new_data.append(i[3:])

            if index == 0:
                self.clear()
                self.mainWindow(new_data, flag=3, index=0)
            else:
                if index < 0:
                    messagebox.showerror("No User Found", "Click on Next")
                elif index == len(new_data):
                    messagebox.showerror("No User Left", "Click on Previous")
                else:
                    self.clear()
                    self.mainWindow(new_data, flag=3, index=index)
        except:
            messagebox.showerror("Sorry!", "No Requests Sent")

    def view_matches(self, index=0):
        try:
            data = self.db.fetch_matches(self.user_id)

            new_data = []
            for i in data:
                new_data.append(i[3:])

            if index == 0:
                self.clear()
                self.mainWindow(new_data, flag=4, index=0)
            else:
                if index < 0:
                    messagebox.showerror("No User Found", "Click on Next")
                elif index == len(new_data):
                    messagebox.showerror("No User Left", "Click on Previous")
                else:
                    self.clear()
                    self.mainWindow(new_data, flag=4, index=index)
        except:
            messagebox.showerror("Sorry!", "No Matches Found")

obj = Tinder()
