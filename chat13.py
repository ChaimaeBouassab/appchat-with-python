class Chat:
    def __init__(self):
        self.users_file = "users.txt"
        self.user=None
    def Inscription(self):
        liste=[]
        while True:
          nom=input("Entrez le nom : ")
          password = input("Entrez le mot de passe : ")
          liste.append(nom + "," + password)
          r=int(input("Voulez-vous continuer Tapez 0 pour arreter ou autre nombre pour continuer : "))
          if r==0:
            break
          print("Liste des utilisateurs :")
          for l in liste:
            print(l)
          with open(self.users_file,'w') as file:
            for items in liste:
              file.write("%s \n " % items)
          file.close()

    def connexion(self):
        utilisateur = input("Entrez le nom d'utilisateur : ")
        password = input("Entrez le mot de passe : ")
        with open(self.users_file, "r") as file:
            for line in file:
                ancien_username, ancien_password = line.strip().split(",")
                if ancien_username == utilisateur and ancien_password == password:
                    print("Connexion réussie.")
                    return True
                return False
    def envoie_message(self):
        destinataire = input("Entrez le nom de destinataire : ")
        contenue = input("Entrez le contenu de message : ")
        with open("users.txt", "r") as file:
            users = file.readlines()
            if self.user == destinataire:
                print("Vous ne pouvez pas vous envoyer un message à vous-même.")
                return
            user_exists = False
            for user in users:
                username, _ = user.strip().split(',')
                if username == destinataire:
                    user_exists = True
                    break
            if not user_exists:
                print("Le destinataire n'existe pas.")
                return
        with open("messages.txt", "a") as file:
            file.write(f"{self.user},{destinataire},{contenue}\n")
        print("Message envoyé.")

    def lire_messages(self):
        with open("messages.txt", "r") as file:
            messages = file.readlines()
        user_messages = []
        for message in messages:
            sender, recipient, content = message.strip().split(',')
            if recipient == self.user:
                user_messages.append(f"De : {sender}  Contenu : {content}")
    def afficher_utilisateurs(self):
        with open("users.txt", "r") as file:
            users = file.readlines()
            print("Liste des utilisateurs :")
            for user in users:
                username, _ = user.strip().split(',')
                print(username)


chat_app = Chat()
chat_app.Inscription()
chat_app.connexion()
chat_app.envoie_message()
chat_app.lire_messages()
chat_app.afficher_utilisateurs()