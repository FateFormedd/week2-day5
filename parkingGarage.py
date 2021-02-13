class Ticket:

    def __init__(self):
        self.tickets = [x + 1 for x in range(11)]
        self.current = {}

    def sell(self):
        tickets = []
        tickets.append(self.tickets.pop(0))
        if self.tickets != None:
            for i in range(len(tickets)):
                self.current[tickets[i]] = 'Unpaid'
            return f"Here's your ticket {tickets}"
        else:
            return "No more room in this lot."
        sorted(self.tickets)

    def pay(self):
        x = input("which ticket is yours? ")
        self.current[x] = 'Paid'
        return f"You're all paid up!"


    def leave(self, tickets):
        self.tickets = tickets
        self.tickets.append(self.tickets)
        del self.current[self.tickets]
        return "Have a great drive!"


class Test:

    def main():
        t.sell()
        print(t.tickets)
        print(t.current)


    def leave(self):
        pass
        self.tickets = input("What ticket are you returning? ")
        
        



t = Ticket()
Test.main()