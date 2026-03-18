from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

class MainScreen(MDScreen):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.app = MDApp.get_running_app()
    
    def on_pre_enter(self):
        if self.app.userNameStored != "Utilisateur":
            self.textLabel = f"Les bases sont maîtrisées, !!! BRAVO {self.app.userNameStored} !!!"
    
    # On créé une variable pour changer le texte de notre label
    textLabel = StringProperty("Maîtrise des bases")
    # On ajoute une variable pour la police
    policeLabel = StringProperty("comfortaa")
    
    # On crée la fonction pour afficher le texte dans le terminal
    def clickButton(self):
        
        print("Bonjour, le bouton fonctionne")
        
    # On change le texte de notre label
    def changeTextLabel(self):
        
        if self.app.userNameStored != "Utilisateur":
            self.textLabel = f"Les bases sont maîtrisées, !!! BRAVO {self.app.userNameStored} !!!"
        else:
            self.textLabel = "Les bases sont maîtrisées, mais il reste un écran !"
        
    # On change la police
    def changePoliceLabel(self):
        
        self.policeLabel = "tomorrow" if self.policeLabel == "comfortaa" else "comfortaa"
