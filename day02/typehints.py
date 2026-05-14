class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age



user: User = User("Rahul", 21)

print(user.name)
print(user.age)