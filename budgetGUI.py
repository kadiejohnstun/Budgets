import tkinter as tk

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1000x600')
        self.root.resizable(width=False, height=False)
        self.root.title('Automated Budgeting Tool')
        self.style = ('Helvetica', 18)
        self.draw('   Hello! Welcome to the Johnstud Budget App!\n   Where everyone can be a stud at budgeting!')
        self.buttons()
        self.root.mainloop()

    def draw(self, msg):
        self.frameText = tk.Frame(self.root, height=20, width=50)
        self.textBox = tk.Text(self.frameText, height=20, width=50, relief='flat', bg='light blue', font=self.style)
        self.textBox.insert(1.0, msg)
        self.textBox.config(state='disabled')
        self.frameText.grid(row=0, column=0)
        self.textBox.pack(padx=3, pady=3)

    def buttons(self):
        self.frame = tk.Frame(self.root, height=20, width=50)
        self.frame.grid(row=0, column=1)
        self.label = tk.Label(self.frame, text='How much is your monthly Budget?')
        self.entry = tk.Entry(self.frame, font=14)
        self.kadieBudget = tk.Button(self.frame, text='Calculate Budget', command=self.calculateBudget, width=20)
        self.viewSpending = tk.Button(self.frame, text='View your Spending Budget', command=self.popUp, width=20)
        self.viewOverallBudget = tk.Button(self.frame, text='View your Overall Budget', command=self.viewOverallBudgetPlan, width=20)
        items = [self.label, self.entry, self.kadieBudget, self.viewOverallBudget, self.viewSpending]
        for item in items: item.pack(padx=10,pady=5)

    def popUp(self):
        self.popUp = tk.Tk()
        self.popUp.geometry("220x190")
        self.popUp.title("Bills")
        self.popUp.resizable(width=False, height=False)
        self.rentLabel = tk.Label(self.popUp, text="Mortgage/Rent:")
        self.rentEntry = tk.Entry(self.popUp, width=25)
        self.billsLabel = tk.Label(self.popUp, text="Total Monthly Expenditures:")
        self.billsEntry = tk.Entry(self.popUp, width=25)
        # self.savingsLabel = tk.Label(self.popUp, text="How much will you Save:")
        # self.savingsEntry = tk.Entry(self.popUp, width=25)
        self.done = tk.Button(self.popUp, text='Done', command=self.calculateSpending)
        items = [self.rentLabel, self.rentEntry, self.billsLabel, self.billsEntry, self.done]
        for item in items: item.pack(pady=5)

    def calculateBudget(self):
        self.budget=float(self.entry.get() or 0)
        self.spending = self.budget * 0.5
        self.draw(f" Total Budget\t\t: ${'{:.2f}'.format(self.budget)}\n Spending Budget\t\t: ${'{:.2f}'.format(self.spending)}")

    def viewOverallBudgetPlan(self):
        self.budget = float(self.entry.get() or 0)
        self.spending = self.budget * 0.5
        self.savings = self.budget * 0.3
        self.extra = self.budget - self.spending - self.savings
        self.draw(f"Total Budget\t\t: ${'{:.2f}'.format(self.budget)}\nSpending Budget\t\t: ${'{:.2f}'.format(self.spending)}\nSavings\t\t: ${'{:.2f}'.format(self.savings)}\nPlay Money\t\t: ${'{:.2f}'.format(self.extra)}")

    def calculateSpending(self):
        self.rent = float(self.rentEntry.get() or 0)
        self.bills = float(self.billsEntry.get() or 0)
        self.popUp.destroy()
        self.budget = float(self.entry.get() or 0)
        self.food = (self.budget * 0.5) - self.rent - self.bills
        self.draw(f"       **- Total Budget -** \n Total\t\t: ${'{:.2f}'.format(self.budget)}\n Spending Budget\t\t: ${'{:.2f}'.format(self.budget*0.5)}\n\n       **- Expenditures -** \n Mortage/Rent\t\t: ${'{:.2f}'.format(self.rent)}\n Bills\t\t: ${'{:.2f}'.format(self.bills)}\n Food\t\t: ${'{:.2f}'.format(self.food)}")

if __name__ == '__main__':
    MainWindow()