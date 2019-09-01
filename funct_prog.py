# Functional Programming assignment for DAT/210 - Data programming Languages at University of Phoenix

class cost():
    def __init__(self, label='none', val=0):
        self.label = label
        self.value = val
    
    def to_aud(self):
        return '${:,.2f}'.format(self.value * 1.43470)

    def to_usd(self):
        return '${:,.2f}'.format(self.value)
    
    def print_vals(self):
        print(self.label + ': ' + self.to_usd())
    
    def print_aud(self):
        print(self.label + ': ' + self.to_aud())

# Write a function to convert the costs from United States dollar (USD) to Australian dollar (AUD). Note: Look up the current USD to AUD exchange rate to use in your function
list_of_items = ['Travel Cost', 'Hotel Cost', 'Rental Car Cost', 'Labor Cost']
list_of_costs = []

for item in list_of_items:
    item_cost = float(input('Enter cost for ' + item + ' in USD:\n'))
    new_cost = cost(item, item_cost)
    list_of_costs.append(new_cost)

print('\nItems in USD:')
for cost_obj in list_of_costs:
    cost_obj.print_vals()

print('\nItems in AUD:')
for cost_obj in list_of_costs:
    cost_obj.print_aud()