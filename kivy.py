from kivy.app import App
from kivy.uix.button import Button
import sys
import phonenumbers
from phonenumbers import geocoder
from tkinter import *
from opencage.geocoder import OpenCageGeocode



class MainApp(App):
    def build(self):


        root = Tk()
        root.title("Corexital Phone Tracer")
        root.configure(bg='black')


        value = str(StringVar())
        enternum = Label(root, text="Phone Tracer", font="comicsanms 20 bold", fg="yellow", bg="black")

        prompt = Label(root, text="Enter phone number with country code +1 US/CA", font="comicsanms 10", fg="white", bg="black")
        prompt.grid(column=1, row=4)
        enternum.grid(row=2, column=1)
        numenter = Entry(root, textvariable=value, fg="black")

        numenter.config(highlightthickness=2, highlightbackground="lime", width=30)

        numenter.grid(row=5, column=1)

        def center_window(width=350, height=500):
            # get screen width and height
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            # calculating the position of x and y coordinate
            x = (screen_width / 2) - (width / 2)
            y = (screen_height / 2) - (height / 2)
            root.geometry('%dx%d+%d+%d' % (width, height, x, y))


        center_window()



        def Mainfunc():
            try:
                print(numenter.get())
                pepnumber = phonenumbers.parse(numenter.get())
                location = phonenumbers.geocoder.description_for_number(pepnumber, "en")

                print("LOCATION:")
                print(location)

                key = '7b5057c5d0594b948600eaf3affa261d'

                geocoder = OpenCageGeocode(key)
                query = str(location)
                results = geocoder.geocode(query)


                lat = results[0]['geometry']['lat']
                lng = results[0]['geometry']['lng']
                print("GPS COORDINATES:")
                print(lat,lng)
                print("END OF REPORT")
                print("Corexital Data 2023")

            except:
                print("INVALID INPUT!!")


        Button(root, text="Get Location", font="comicsanms 10 bold ", fg="black", bg="white", command=Mainfunc).grid(padx=40,
                                                                                                                     pady=10,
                                                                                                                     column=1)


        class Redirect():

            def __init__(self, widget):
                self.widget = widget
                widget.place(x=0, y=220)
            def write(self, text):
                self.widget.insert('end', text)
                # self.widget.see('end') # autoscroll



        text =Text(root)

        old_stdout = sys.stdout

        # assing Redirect with widget Text
        sys.stdout = Redirect(text)

        root.mainloop()

        # assign back original stdout (if you need it)
        sys.stdout = old_stdout
MainApp().run()
