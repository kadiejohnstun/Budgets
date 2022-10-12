import os

# limit_1 = 10275
# limit_2 = 41775
# limit_3 = 89075
# limit_4 = 170050
# limit_5 = 215950
# limit_6 = 539900

# rate_1 = 0.1
# rate_2 = 0.12
# rate_3 = 0.22
# rate_4 = 0.24
# rate_5 = 0.32
# rate_6 = 0.35
# rate_7 = 0.37

#  if (self.budget * 12) < limit_1:
#             self.net = self.budget * rate_1
#         elif (self.budget * 12) < limit_2:
#             self.net = rate_1 * limit_1 + (rate_2 * ((self.budget * 12) - limit_1))
#         elif (self.budget * 12) < limit_3:
#             self.net = rate_1 * limit_1 + (rate_2 * (limit_2 - limit_1)) + (rate_3 * ((self.budget * 12) - limit_2))
#         elif (self.budget * 12) < limit_4:
#             self.net = rate_1 * limit_1 + (rate_2 * (limit_2 - limit_1)) + (rate_3 * (limitF_3 - limit_2)) + (rate_4 * ((self.budget * 12) - limit_3))
#         elif (self.budget * 12) < limit_5:
#             self.net = rate_1 * limit_1 + (rate_2 * (limit_2 - limit_1)) + (rate_3 * (limit_3 - limit_2)) + (rate_4 * (limit_3 - limit_4)) + (rate_5 * ((self.budget * 12) - limit_4))
#         elif (self.budget * 12) < limit_6:
#             self.net = rate_1 * limit_1 + (rate_2 * (limit_2 - limit_1)) + (rate_3 * (limit_3 - limit_2)) + (rate_4 * (limit_3 - limit_4)) + (rate_5 * (limit_4 - limit_5)) + (rate_6 * ((self.budget * 12) - limit_5))
#         else:
#             self.net = rate_1 * limit_1 + (rate_2 * (limit_2 - limit_1)) + (rate_3 * (limit_3 - limit_2)) + (rate_4 * (limit_3 - limit_4)) + (rate_5 * (limit_4 - limit_5)) + (rate_6 * (limit_5 - limit_6)) + (rate_7 * ((self.budget * 12) - limit_6))




class Budget(object):
    def __init__(self):
        os.system('cls')
        self.budget = float(input("How much is your monthly Gross Pay?\n Budget: $ "))
        self.spending = self.budget * 0.5
        self.main()

    def main(self):
        os.system('cls')
        print("This calculator follows the 50-20-30 budget rule.\n")
        print("Your total budget is\n$", '{:.2f}'.format(self.budget))
        main_option = int(input('\nWhich budget do you want to view?\n 1. View over all budget?\n 2. View spending budget?\n 3. View budget breakdown?\n Option 1, 2, or 3: '))
        if main_option == 1:
            self.overall_budget()
        elif main_option == 2:
            self.spending_budget()
        elif main_option == 3:
            self.breakdown_budget()
        else: 
            quit
    
    def overall_budget(self):
        os.system('cls')
        option = int(input("How much do you want to invest?\n 1. 20%\n 2. 30%\n Option 1 or 2: "))
        if option == 1:
            self.saving = 0.2
        elif option == 2:
            self.saving = 0.3
        else:
            print('Error: Please select 1 or 2!')
        self.final_saving = self.budget * self.saving
        self.extra = self.budget - self.final_saving - self.spending
        print('\nSpending: $', '{:.2f}'.format(self.spending),'\nTo save: $', '{:.2f}'.format(self.final_saving), '\nExtra: $', '{:.2f}'.format(self.extra))
        os.system('pause')
        self.main()

    def spending_budget(self):
        os.system('cls')
        print('Spending Budget: $','{:.2f}'.format(self.spending))
        rent = float(input('\nHow much is your monthly rent?\n'))
        bills = float(input('\nHow much are your monthly bills?\n'))
        food = self.spending - rent - bills
        print('\nExpenses:\n  Rent: $','{:.2f}'.format(rent),'\n  Bills: $','{:.2f}'.format(bills), '\n  Food: $','{:.2f}'.format(food))
        os.system('pause')
        self.main()

    def breakdown_budget(self):
        os.system('cls')
        print('Spending Budget: $','{:.2f}'.format(self.spending))
        rent = float(input('\nHow much is your monthly rent?\n'))
        bills = float(input('\nHow much are your monthly bills?\n'))
        food = self.spending - rent - bills
        option = int(input("How much do you want to invest?\n1. 20%\n2. 30%\nOption 1 or 2: "))
        if option == 1:
            self.saving = 0.2
        elif option == 2:
            self.saving = 0.3
        else:
            print('Error: Please select 1 or 2!')
        self.final_saving = self.budget * self.saving
        self.extra = self.budget - self.final_saving - self.spending
        print('\nExpenses:\n  Rent: $','{:.2f}'.format(rent),'\n  Bills: $','{:.2f}'.format(bills), '\n  Food: $','{:.2f}'.format(food), '\n  Savings: $ ', '{:.2f}'.format(self.final_saving), '\n  Extra: $', '{:.2f}'.format(self.extra))
        os.system('pause')
        self.main()



Budget()