class Ticket:
    
    def __init__(self):
        self.tickets = [x + 1 for x in range(10)]
        self.current = {}
    def sell(self):
        x = self.tickets.pop(0)
        self.current[x] = 'unpaid'
#         show available spaces

    def paid(self):
        for key, value:
            key = i
            value = j
            self.tickets.append(i)
            self.spaces.append(j)
            self.current.del[i] = j


    def leave():
        pass
        
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - Update tickets list to increase by 1 (meaning add to the tickets list)        
# class Garage:
#     def __init__(self):
       
class Spaces:
    def __init__(self):
        self.spaces = []

class Test:
    
    def main():
        ticket = Ticket()
        ticket.sell()
    
test=Test()
test.main()