#! /usr/bin/python3

print("this is python file 4")

users = ['val', 'bob', 'mia', 'ron', 'ned']
num_users = len(users)
print("We have " + str(num_users) + " users.")

print(users.sort())
print(users.sort(reverse=True))
print(sorted(users))
print(sorted(users, reverse=True))
print(users.reverse())

for user in users:
print(user)

for user in users:
print("Welcome, " + user + "!")
print("Welcome, we're glad to see you all!")