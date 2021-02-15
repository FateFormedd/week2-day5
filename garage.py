class Garage:
    ticket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    myticket = []
    paid = []

    def tickets(self):
        t = input("Would you like to take a ticket, pay for your ticket, or leave? ")
        if t.lower == 'take':
            num = self.ticket.pop(0)
            Garage.myticket.append(num)
        elif t.lower == 'pay':
            num = input("What's your ticket number? ")
            if num in Garage.myticket:
                Garage.paid.append(num)
                Garage.myticket.remove(num)
                return "You're all paid up!"
        elif t.lower == 'leave':
            num = input("What's your ticket number? ")
            if num in Garage.paid:
                return "Have a great drive!"
            else:
                return "Please pay for your ticket before you leave."

t=Garage()
t.tickets()
