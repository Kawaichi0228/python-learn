"""クラスのコンストラクタ的な役割を関数で行う"""
# クラスでのやり方
class UserProfile:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

user = UserProfile("佐藤", "35", "男")
print(user.name)
 
 
# test
# 関数をコンストラクタのように使う
def userProfile(name, age, gender):
    user_profile = {}
    user_profile["name"] = name
    user_profile["age"] = age
    user_profile["gender"] = gender
    return user_profile
 
user = userProfile("佐藤", "35", "男")
print(user["name"])
