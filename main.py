from kivy.core.text import LabelBase
from kivy.metrics import sp
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class MainScreen(MDScreen):
    
    # On créé une variable pour changer le texte de notre label
    textLabel = StringProperty("Maîtrise des bases")
    # On ajoute une variable pour la police
    policeLabel = StringProperty("comfortaa")
    
    # On crée la fonction pour afficher le texte dans le terminal
    def clickButton(self):
        
        print("Bonjour, le bouton fonctionne")
        
    # On change le texte de notre label
    def changeTextLabel(self):
        
        self.textLabel = "Les bases sont maîtrisées, !!! BRAVO !!!"
        
    # On change la police
    def changePoliceLabel(self):
        
        self.policeLabel = "tomorrow" if self.policeLabel == "comfortaa" else "comfortaa"
        
        
class MainApp(MDApp):
    
    textStyle = StringProperty()
    
    # La fonction pour construire la fenêtre de l'application
    def build(self):
        
        # On enregistre les police personnalisées sans oublier l'import de "LabelBase"
        LabelBase.register(name="hackPolice", fn_regular="assets/fonts/hack.ttf")
        LabelBase.register(name="3270Police", fn_regular="assets/fonts/3270.ttf")
        LabelBase.register(name="comfortaaPolice", fn_regular="assets/fonts/comfortaa.ttf")
        LabelBase.register(name="tomorrowPolice", fn_regular="assets/fonts/tomorrow.ttf")
        
        # On update le dictionnaire "font_style"
        self.theme_cls.font_styles.update({
            "3270": {
                "large": {"line-height": 1.64, "font-name": "3270Police", "font-size": sp(57)},
                "medium": {"line-height": 1.52,"font-name": "3270Police","font-size": sp(45)},
                "small": {"line-height": 1.44, "font-name": "3270Police", "font-size": sp(36)}
                },
            "hack": {
                "large": {"line-height": 1.64, "font-name": "hackPolice", "font-size": sp(57)},
                "medium": {"line-height": 1.52,"font-name": "hackPolice","font-size": sp(45)},
                "small": {"line-height": 1.44, "font-name": "hackPolice", "font-size": sp(36)}
                ,},
            "comfortaa": {
                "large": {"line-height": 1.64, "font-name": "comfortaaPolice", "font-size": sp(57)},
                "medium": {"line-height": 1.52,"font-name": "comfortaaPolice","font-size": sp(45)},
                "small": {"line-height": 1.44, "font-name": "comfortaaPolice", "font-size": sp(36)}
                ,},
            "tomorrow": {
                "large": {"line-height": 1.64, "font-name": "tomorrowPolice", "font-size": sp(57)},
                "medium": {"line-height": 1.52,"font-name": "tomorrowPolice","font-size": sp(45)},
                "small": {"line-height": 1.44, "font-name": "tomorrowPolice", "font-size": sp(36)}
                ,}
            ,})
        
        # On choisi un thème de couleur
        self.theme_cls.primary_palette = "SeaGreen"
        
        # Cette ligne permet de récupérer le style du système (PC ou Smartphone)
        self.theme_cls.theme_style = "Dark" if self.theme_cls._get_theme_style == "Dark" else "Light"
        self.textStyle = "Sombre" if self.theme_cls.theme_style == "Dark" else "Claire"
        
        # On créé l'animation du changement de theme style
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.5
        
        # On renvoi l'écran
        return MainScreen()
    
    # On va changer le theme style qui prendra en compte l'animation
    def switchThemeStyle(self):
        
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )
        
        self.textStyle = "Sombre" if self.theme_cls.theme_style == "Dark" else "Claire"
    
    
    
if __name__ == "__main__":
    
    # On lance le programme
    MainApp().run()
