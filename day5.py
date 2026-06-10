tickets = ["billing issue", "login problem", "slow performance"]

for ticket in tickets:
    print(ticket)


print("---checking priorities ---")

for ticket in tickets:
    if ticket == "billing issue" :
        print(ticket + "->Ticket is of financial priority")
    else:
        print(ticket + "-> Support team")


count =1
while count<= 3:
     print("Checking ticket number " + str(count))
     count=count + 1