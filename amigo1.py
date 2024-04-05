class YearEndOverview:
    def __init__(self,initial_deposit):
        self.sales=initial_deposit
        self.transaction=[]
    def profit(sales,expenses):
        profit=sales-expenses
        return profit
    sales=float(input("Enter sales for the month: "))
    expenses=float(input("Enter expenses for the month: "))
match profit:
    case 4000:
        print("New margins need to be implemented")
    case 5000:
        print("We're doing great,but we can do better")
    case 6000:
        print("We're smashing it! Consider investing in other markets.")   


    
        
        