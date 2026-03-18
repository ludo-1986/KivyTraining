from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class SecondScreen(MDScreen):
    
    textHello = StringProperty("Bonjour, entrez votre nom dans le champ")
    
    def validateName(self):
        
        # On récupère le nom de l'utilisateur
        userName = self.ids.fieldName.text.capitalize()
        userAge = int(self.ids.fieldAge.text) if self.ids.fieldAge.text else 0
        
        if userName:
            
            # On récupère l'application qui tourne et on change sa variable
            app = MDApp.get_running_app()
            app.userNameStored = userName
            
            # On change directement
            # ecran_accueil = self.manager.get_screen("ecran_principal")
            # ecran_accueil.changeTextLabel()
            
            self.textHello = f"Bonjour {userName}, ravis de te rencontrer"
        else:
            self.textHello = "Bonjour utilisateur, comment vous appelez vous ?"
            
        if userAge:
            self.textHello += f"\nVous avez {userAge} ans,"
            if userAge >= 60:
                self.textHello += "vous êtes senior"
            elif userAge < 18:
                self.textHello += "vous êtes mineur"
            else:
                self.textHello += "vous êtes majeur"
        else:
            self.textHello += "\nNous n'avons pas reçu votre age"
