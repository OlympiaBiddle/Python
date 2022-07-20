lucky_numbers = [4, 8, 15, 16, 23, 42]
lucky_numbers.reverse()
print(lucky_numbers)

friends = ["Kevin", "Keya", "Walter", "Sofia", "Sofia", "Candace"]

print(friends)
print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[1:3])
friends[0] = "John"
print(friends)

#friends.extend(lucky_numbers)
print(friends)
friends.append("Creed")
print(friends)

friends.insert(1, "Kelly")
print(friends)
friends.remove("Walter")
print(friends)

#friends.clear
#print(friends)
friends.pop()
print(friends)
print(friends.count("Sofia"))
friends.sort()
friends2 = friends.copy()
print(friends2)

