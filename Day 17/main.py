
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0 


        print("new user being created....")

user_1 = User("0001", "shiro")
print(user_1.username)
print(user_1.follower)

user_2 = User("002", "seneca")
print(user_2.id)


user_1.follower += 100000 

print(user_1.follower)