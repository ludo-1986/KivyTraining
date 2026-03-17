from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class SecondScreen(MDScreen):
    
    textHello = StringProperty("Bonjour, entrez votre nom dans le champ")
    
    def validateName(self):
        
        # On récupère le nom de l'utilisateur
        userName = self.ids.fieldName.text.capitalize()
        userAge = self.ids.fieldAge.text
        
        if userName:
            self.textHello = f"Bonjour {userName}, ravis de te rencontrer"
        else:
            self.textHello = "Bonjour utilisateur, comment vous appelez vous ?"
            
        if userAge:
            self.textHello += f"\nVous avez {userAge} ans,"
            if int(userAge) >= 60:
                self.textHello += "vous êtes senior"
            elif int(userAge) < 18:
                self.textHello += "vous êtes mineur"
            else:
                self.textHello += "vous êtes majeur"
        else:
            self.textHello += "\nNous n'avons pas reçu votre age"
            
        
        
class InteractiveApp(MDApp):
    
    # La fonction pour construire la fenêtre de l'application
    def build(self):
        
        # On choisi un thème de couleur
        self.theme_cls.primary_palette = "SeaGreen"
        
        # Cette ligne permet de récupérer le style du système (PC ou Smartphone)
        self.theme_cls.theme_style = "Dark" 
        self.textStyle = "Sombre" if self.theme_cls.theme_style == "Dark" else "Claire"
        
        # On renvoi l'écran
        return SecondScreen()
    
    
    
if __name__ == "__main__":
    
    # On lance le programme
    InteractiveApp().run()
