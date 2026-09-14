from oop_proj import ChatBook


# <=================> Encapsulation <=================> 
# print(obj._ChatBook__name) # <--------- We can access hidden attribute like this

# Gatter and Setter # # <--------- We can also access hidden attribute using [Getter and Setter]
# print(obj.get_name())
# obj.set_name("Kashif")
# print(obj.get_name())

user1 = ChatBook()
print(user1.id)

# Using Static method directly from class rather than object
ChatBook.set_id(10)

user2 = ChatBook()
print(user2.id)

user3 = ChatBook()
print(user3.id)

