class Ticket:

    def __init__(self, tickets):
        self.tickets = [x + 1 for x in range(10)]
        self.current = {}

    def sell(self, tickes):
        tickets = self.tickets.pop(0)
        self.current[tickets] = 'Unpaid'
        return f"Here's your ticket {tickets}"

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

    def leave(self, tickets):
        self.tickets = tickets
        self.tickets.append(self.tickets)
        del self.current[self.tickets]
        return "Have a great drive!"


class Test:

    def main(self):

        def leave(self, tickets):
            self.tickets = input("What ticket are you returning? ")
        user_input = input()
        ticket = Ticket()
        ticket.sell()


test = Test()
# test.main()
Ticket()
myticket = Ticket()
myticket.pay()