from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class MainScreen(MDScreen):
    
    # On crée la fonction pour afficher le texte dans le terminal
    def clickButton(self):
        
        print("Bonjour, le bouton fonctionne")
        
        
class MainApp(MDApp):
    
    # La fonction pour construire la fenêtre de l'application
    def build(self):
        
        # On choisi un thème de couleur
        self.theme_cls.primary_palette = "SeaGreen"
        
        # On choisi un style
        self.theme_cls.theme_style = "Dark"  # Ou "Light"
        
        # On renvoi l'écran
        return MainScreen()
    
    
if __name__ == "__main__":
    
    # On lance le programme
    MainApp().run()
