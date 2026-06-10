tickets = ["billing issue", "login problem", "slow performance"]

for ticket in tickets:
    print(ticket)


print("---checking priorities ---")

for ticket in tickets:
    if ticket == "billing issue" :
        print(ticket + "->Ticket is of financial priority")
    else:
        print(ticket + "-> Support team")