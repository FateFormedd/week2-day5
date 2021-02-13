def tickets():
    ticket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    myticket = []
    paid = []
    t = input("Would you like to take a ticket, pay for your ticket, or leave? ")
    if t.lower == 'take':
        ticket.pop(0) = x
        myticket.append(x)
    elif t.lower == 'pay':
        num = input("What's your ticket number? ")
        if num in myticket:
            paid.append(num)
            myticket.remove(num)
            return "You're all paid up!"
    elif t.lower == 'leave':
        num = input("What's your ticket number? ")
        if num in paid:
            return "Have a great drive!"
        else:
            return "Please pay for your ticket before you leave."

tickets()
