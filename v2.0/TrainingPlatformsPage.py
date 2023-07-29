from gi.repository import Gtk
import webbrowser
from Page import Page

class TrainingPlatformsPage(Page):
    def __init__(self, back_label):
        super().__init__(back_label)

        self.grid = Gtk.Grid()
        self.append(self.grid)

        platforms = {
            "TryHackMe": "🏁 TryHackMe",
            "Hack The Box": "📦 Hack The Box",
            "PortSwigger": "🌐 PortSwigger",
            "Let's Defend": "🛡️ Let's Defend",
            "Cyberary": "📚 Cyberary",
            "Pentester Academy": "🎓 Pentester Academy",
            "Secure Code Warrior": "⚔️ Secure Code Warrior",
            "Codecademy": "📖 Codecademy",
            "Pluralsight": "🎥 Pluralsight",
            "LinkedIn Learning": "🔗 LinkedIn Learning"
        }

        for i, platform in enumerate(platforms):
            btn = Gtk.Button(label=platforms[platform])
            btn.get_style_context().add_class("circular")
            btn.connect("clicked", self.open_page, platform)
            self.grid.attach(btn, i % 3, i // 3, 1, 1)
            btn.set_size_request(200, 200)

            btn.set_hexpand(True)
            btn.set_vexpand(True)
            btn.set_halign(Gtk.Align.CENTER)
            btn.set_valign(Gtk.Align.CENTER)

    def open_page(self, button, page_name):
        button.get_style_context().add_class('clicked')

        urls = {
            "TryHackMe": "https://tryhackme.com/",
            "Hack The Box": "https://www.hackthebox.eu/",
            "PortSwigger": "https://portswigger.net/",
            "Let's Defend": "https://letsdefend.io/",
            "Cyberary": "https://www.cybrary.it/",
            "Pentester Academy": "https://www.pentesteracademy.com/",
            "Secure Code Warrior": "https://www.securecodewarrior.com/",
            "Codecademy": "https://www.codecademy.com/",
            "Pluralsight": "https://www.pluralsight.com/",
            "LinkedIn Learning": "https://www.linkedin.com/learning/"
        }

        if page_name in urls:
            webbrowser.open(urls[page_name])
        else:
            print(f"No URL found for {page_name}")
