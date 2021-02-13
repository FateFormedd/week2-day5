class Ticket:

    def __init__(self):
        self.tickets = []
        self.current = {}

    def sell(self):
        x = self.tickets.pop(0)
        self.current[x] = 'Unpaid'
        return f"Here's your ticket {x}"

    def pay(self):
        x = input("which ticket is yours? ")
        self.current[x] = 'Paid'
        return f"You're all paid up!"


        # for key, value:
        #     key = i
        #     value = j
        # self.tickets.append(i)
        # self.spaces.append(j)
        # self.current.del[i] = j
        # return

    def leave(self):
        x = input("What ticket are you returning? ")
        self.tickets.append(x)
        del self.current[x]
        return "Have a great drive!"


class Test:

    def main(self):
        user_input = input()
        ticket = Ticket()
        ticket.sell()


test = Test()
# test.main()
Ticket()
myticket = Ticket()
myticket.pay()