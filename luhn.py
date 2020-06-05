class Luhn:
    def __init__(self, card_num):
        self.card = card_num

    def valid(self):        
        num = self.card.replace(' ', '')        
        
        if len(num) < 2:
            return False
        if not num.isnumeric():
            return False
        total = sum(int(i) for i in num[-1::-2])
        
        for i in num[-2::-2]:
            i = 2 * int(i)
            total += i if i < 9 else i - 9
        return total % 10 == 0