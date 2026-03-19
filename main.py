import darkdetect

from kivy.core.text import LabelBase
from kivy.metrics import sp
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.lang import Builder

from label import MainScreen
from interactive import SecondScreen


class WindowManager(MDScreenManager):
    pass


class MainApp(MDApp):
    
    textStyle = StringProperty()
    
    # On créé une variable vide pour stocker le nom de l'utilisateur
    userNameStored = StringProperty("Utilisateur")
    
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
    
        Builder.load_file("label.kv")
        Builder.load_file("interactive.kv")
    
        self.theme_cls.primary_palette = "Orange"
        
        # On récupère le theme de notre système (darkdetect = pc, _get_theme_style = smartphone)
        if darkdetect.isDark() or self.theme_cls._get_theme_style == "Dark":
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"
        
        # On envoi le thème utilisé
        self.textStyle = "Sombre" if self.theme_cls.theme_style == "Dark" else "Claire"
        
        # On créé l'animation du changement de theme style
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.5
        
        sm = WindowManager()
        sm.add_widget(MainScreen(name="ecran_principal"))
        sm.add_widget(SecondScreen(name="ecran_interaction"))
        
        return sm
    
    # On va changer le theme style qui prendra en compte l'animation
    def switchThemeStyle(self):
        
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )
        
        self.textStyle = "Sombre" if self.theme_cls.theme_style == "Dark" else "Claire"
    

if __name__ == "__main__":
    MainApp().run()
