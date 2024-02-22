class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class AuthenticationSystem:
    def __init__(self):
        self.users = []

    def register_user(self, username, password):
        self.users.append(User(username, password))

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return True
        return False

# Example usage:
auth_system = AuthenticationSystem()
auth_system.register_user("user1", "password1")

# Simulate login attempts
print(auth_system.login("user1", "password1"))  # True
print(auth_system.login("user1", "password2"))  # False (incorrect password)
print(auth_system.login("user2", "password1"))  # False (user not registered)
