is_urgent = True
is_verified = False
is_assigned = None

if is_urgent :
    print("This ticket is urgent!")


if is_verified:
    print("Customer verified. Proceed")
else:
    print("Customer not verified. Ask for ID")


priority = "medium"

if priority == "high":
    print("respond within 1 hour")
elif priority == "medium":
    print ("respond within 2 hour")
elif priority == "low":
    print ("respond within 24 hours")
else:
    print("unknown priority")