 def ukaz_hvezdy(self, pocet):
        self.hvezdy_label.config(text="⭐" * pocet)
        self.root.after(2000, lambda: self.hvezdy_label.config(text=""))