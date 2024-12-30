str1 = "Subhash"
int_1 = 152

print(type(str1))
print(type(int_1))

# import class from chatter
# example of code resuability

# from oops_project_1 import chatter

# use1 = chatter()

# function v/s method

# # function
# a = len(str1)
# print(a)

# # method

# use1.my_post()

# getter and setter
'''
from oops_project_1 import chatter

user1 = chatter()
print(user1.get_name())
user1.set_name("Agent Y")
print(user1.get_name())
'''


# static method
'''
from oops_project_1 import chatter
# first person user id
user1 = chatter()
print(user1.id)

# second person user id
user2 = chatter()
print(user2.id)

## third person user id
user3 = chatter()
print(user3.id)
'''
from oops_project_1 import chatter
# first person user id
user1 = chatter()
print(user1.id)

chatter.set_id(10)
user2 = chatter()
print(user2.id)

user3 = chatter()
print(user3.id)