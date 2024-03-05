import pymongo

myclient = pymongo.MongoClient("mongodb+srv://admin:admin@cluster1.c9arx6y.mongodb.net/")

mydb = myclient["todo_database"]
mycol = mydb["todo_collection"]



def add(s):
    todo_item = {"task": s}
    mycol.insert_one(todo_item) #je pense qu'il rentre les informations dans le ma collection sur mongodb
    print("Added todo: {s}")

def raj():
    try:
        todos = mycol.find()
        for todo in todos:
            print(todo)  # Vous pouvez personnaliser l'affichage selon vos besoins
    except Exception as e:
        raise e

def delete(task):
    mycol.delete_one({"task": task}) #il va aller dans ma collection pour chercher les taches (task) et va les supprimer quand je lui demanderai de le supprimer
    print("Deleted todo: {task}")

# Ajout de la fonctionnalité de suppression
def delete_task():
    task = input("Entrez la tâche à supprimer : ")
    delete(task)

# Test des fonctions
todo = input("Rajoutez à la todo list: ")
add(todo)
raj()

# Suppression d'une tâche
delete_task()
raj()
