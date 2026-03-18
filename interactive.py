from kivy.metrics import dp
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogButtonContainer,
    MDDialogContentContainer,
)
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.textfield import MDTextField, MDTextFieldHintText
from kivymd.uix.screen import MDScreen


class SecondScreen(MDScreen):
    
    textHello = StringProperty("Bonjour, entrez votre nom dans le champ")
    # On prépare une variable pour le dialogue
    dialogName = None
    dialogAge = None
    
    def openAgeDialog(self):
        """Ouvre le dialogue si le champ principal est vide"""
        if not self.dialogAge:
            # Création du champ interne pour pouvoir y accéder facilement
            self.age_input_field = MDTextField(
                MDTextFieldHintText(text="Entrez votre age"),
                input_filter="int",
            )

            self.dialogAge = MDDialog(
                MDDialogHeadlineText(text="Âge manquant"),
                MDDialogContentContainer(self.age_input_field),
                MDDialogButtonContainer(
                    MDButton(
                        MDButtonText(text="Valider l'âge"),
                        style="text",
                        # On appelle une fonction dédiée au clic
                        on_release=self.process_dialog_age 
                    ),
                ),
            )
        self.dialogAge.open()

    def process_dialog_age(self, *args):
        """Récupère l'âge du dialogue et ferme la boîte"""
        age_text = self.age_input_field.text
        if age_text:
            # On met à jour le champ de l'écran principal pour rester synchro
            self.ids.fieldAge.text = age_text
            self.dialogAge.dismiss()
            # On relance la validation globale
            self.validateName()
    
    def validateName(self):
        
        # 1. On récupère les TEXTES bruts (pas de int() ici pour éviter le crash)
        userName = self.ids.fieldName.text.strip().capitalize()
        age_text = self.ids.fieldAge.text.strip()

        # 2. VERIFICATION : Si l'âge manque, on STOPPE et on ouvre le dialogue
        if not age_text:
            self.openAgeDialog()
            return # On quitte la fonction, elle sera relancée par le dialogue

        # 3. Maintenant qu'on est SÛR d'avoir un âge, on peut convertir
        userAge = int(age_text)
        
        if userName:
            
            # On crée le dialogue s'il n'existe pas encore
            if not self.dialogName:
                self.dialogName = MDDialog(
                    MDDialogHeadlineText(text="validation réussie"),
                    MDDialogSupportingText(
                        text=f"Bonjour {userName}, votre visite à été enregistrée"
                        ),
                    MDDialogButtonContainer(
                        MDButton(
                            MDButtonText(text="OK"),
                            style="text",
                            on_release=lambda x: self.dialogName.dismiss()
                            ),
                        spacing=dp(8),
                    ),
                )
            
            # On affiche le dialogue
            self.dialogName.open()
            
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
