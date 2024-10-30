import os
import time
import tkinter
import webbrowser

import PIL
import PIL.Image
import plyer
import plyer.facades.notification
import customtkinter


customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()


        self.title("RegularNotifications")
        self.iconphoto(False, tkinter.PhotoImage(f"{os.path.dirname(__file__)}/icon.png"))
        self.minsize(800, 600)


        self.grid_columnconfigure(
            index = 1,
            weight = 1
        )
        self.grid_columnconfigure(
            index = (2, 3),
            weight = 0
        )
        self.grid_rowconfigure(
            index = (0, 1, 2),
            weight = 1
        )


        self.sidebar_frame = customtkinter.CTkFrame(
            master = self,
            height = 600,
            corner_radius = 0
        )
        self.sidebar_frame.grid(
            row = 0,
            column = 0,
            rowspan = 4,
            sticky = "nsew"
        )

        self.title_label = customtkinter.CTkLabel(
            master = self.sidebar_frame,
            text = "RegularNotifications",
            font = customtkinter.CTkFont(
                size = 24,
                weight = "bold"
            )
        )
        self.title_label.grid(
            row = 0,
            column = 0,
            padx = 24,
            pady = 24
        )

        self.description_label = customtkinter.CTkLabel(
            master = self.sidebar_frame,
            text = "An app for sending customizable notifications\nevery X minutes/hours/days etc\n\nMade by Serriox",
            font = customtkinter.CTkFont(
                size = 16
            )
        )
        self.description_label.grid(
            row = 1,
            column = 0
        )


        self.main_frame = customtkinter.CTkFrame(
            master = self
        )
        self.main_frame.grid(
            row = 0,
            column = 1,
            rowspan = 4,
            padx = 16,
            pady = 16,
            sticky = "nsew"
        )


        self.settings_label = customtkinter.CTkLabel(
            master = self.main_frame,
            width = 420,
            text = "Settings",
            font = customtkinter.CTkFont(
                size = 16
            )
        )
        self.settings_label.grid(
            row = 0,
            column = 0,
            padx = 8,
            pady = 8,
            sticky = "ew"
        )


        self.notification_title = customtkinter.CTkEntry(
            master = self.main_frame,
            width = 420,
            placeholder_text = "Notification title",
            font = customtkinter.CTkFont(
                size = 16
            )
        )
        self.notification_title.grid(
            row = 1,
            column = 0,
            padx = 8,
            pady = 8,
            sticky = "ew"
        )

        self.notification_description = customtkinter.CTkEntry(
            master = self.main_frame,
            width = 420,
            placeholder_text = "Notification description",
            font = customtkinter.CTkFont(
                size = 16
            )
        )
        self.notification_description.grid(
            row = 2,
            column = 0,
            padx = 8,
            pady = 8,
            sticky = "ew"
        )

        self.notification_icon = customtkinter.CTkEntry(
            master = self.main_frame,
            width = 420,
            placeholder_text = "Notification icon (absolute path to icon)",
            font = customtkinter.CTkFont(
                size = 16
            )
        )
        self.notification_icon.grid(
            row = 3,
            column = 0,
            padx = 8,
            pady = 8,
            sticky = "ew"
        )

        self.notification_interval = customtkinter.CTkEntry(
            master = self.main_frame,
            width = 420,
            placeholder_text = "Notification interval (in seconds)",
            font = customtkinter.CTkFont(
                size = 16
            )
        )
        self.notification_interval.grid(
            row = 4,
            column = 0,
            padx = 8,
            pady = 8,
            sticky = "ew"
        )


        self.start_button = customtkinter.CTkButton(
            master = self.main_frame,
            text = "START",
            font = customtkinter.CTkFont(
                size = 16
            ),
            command = lambda: self.start(
                title = self.notification_title.get(),
                description = self.notification_description.get(),
                icon = self.notification_icon.get(),
                interval = self.notification_interval.get()
            )
        )
        self.start_button.grid(
            row = 5,
            column = 0,
            padx = 8,
            pady = 8
        )


        self.github = customtkinter.CTkButton(
            master = self.sidebar_frame,
            height = 40,
            corner_radius = 0,
            hover_color = (
                "gray50",
                "gray50"
            ),
            text = "Serriox on GitHub",
            font = customtkinter.CTkFont(
                size = 16
            ),
            image = customtkinter.CTkImage(
                light_image = PIL.Image.open(f"{os.path.dirname(__file__)}/github.png"),
                dark_image = PIL.Image.open(f"{os.path.dirname(__file__)}/github.png"),
                size = (24, 24)
            ),
            command = lambda: webbrowser.open("https://github.com/serriox/")
        )
        self.github.grid(
            row = 2,
            column = 0,
            pady = (400, 0),
            sticky = "ew"
        )
    

    def start(self, title: str, description: str, icon: str, interval: int | float):
        self.destroy()


        if title == "":
            title_ = "RegularNotifications"
        else:
            title_ = title
        
        if description == "":
            description_ = "New notification"
        else:
            description_ = description

        if icon == "":
            icon_ = f"{os.path.dirname(__file__)}/icon.png"
        else:
            icon_ = icon

        if interval == "":
            interval_ = 600
        else:
            interval_ = interval


        while True:
            self.notification = plyer.notification

            self.notification.notify(
                title = title_,
                message = description_,
                app_name = "RegularNotifications",
                app_icon = icon_
            )

            time.sleep(float(interval_))


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
