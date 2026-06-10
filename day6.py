def greet_customer():
    print("Welcome to Deskmate AI")
    print("How can I help you")

greet_customer()
greet_customer()
greet_customer()


def greet_customer(name):
    print("Welcome " +name + " to Deskmate AI")
    print("How can I help you")

greet_customer("priya")
greet_customer("wilson")


def check_priority(priority):
    if priority == "high" :
        return "respond within an hour"
    elif priority == "medium" :
        return "respond within 4 hour"
    elif priority == "low" :
        return "respond within 24 hours"
    else :
        return "unknown priority"

result1 = check_priority("low")
print(result1)

result2 = check_priority("medium")
print(result2)

result3 = check_priority("high")
print(result3)


