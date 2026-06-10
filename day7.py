tickets = ["billing issue", "login problem", "slow performance"]

print(tickets[-2])
print(tickets[0])

print("original:")
print(tickets)

tickets.append("password reset")
print("After append:")
print(tickets)

print("total tickets:", len(tickets))

tickets.remove("login problem")
print("after remove:")
print(tickets)

tickets.sort()
print("after sort:")
print(tickets)

tickets.pop()
print("after pop")
print(tickets)