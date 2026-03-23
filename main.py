from pyscript import document, display

class Dog:
    def __init__(self, breed, age, name, owner):
        self.breed = document.getElementById("breed").value #Attribute
        self.age = document.getElementById("age").value #Attribute
        self.name = document.getElementById("name").value #Attribute
        self.owner = document.getElementById("owner").value #Attribute

def Submit(self):
        breed = document.getElementById("breed").value
        age = document.getElementById("age").value
        name = document.getElementById("name").value
        owner = document.getElementById("owner").value
        document.getElementById('output1').innerHTML = ' '

         # Displaying the attributes of the object
        display(f'{name} is a {age} year old {breed} owned by {owner}', target="output1")