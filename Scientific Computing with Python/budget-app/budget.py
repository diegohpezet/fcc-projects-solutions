class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount: float, description = ""):
        self.ledger.append({
            'amount': amount,
            'description': description
        })

    def withdraw(self, amount: float, description = ""):
        if self.check_funds(amount):
            self.ledger.append({
                'amount': -amount,
                'description': description
            })
            return True
        else: 
            return False

    def get_balance(self):
        total = 0
        for element in self.ledger:
            total += element['amount']
        return total

    def transfer(self, amount, budget):
        if self.check_funds(amount):
            budget.deposit(amount, f"Transfer from {self.name}")
            self.withdraw(amount, f"Transfer to {budget.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else: 
            return True

    def __str__(self):
        category_string = ""
        # Build title
        amount_of_asterisks = 30 - len(self.name)
        half_line = '*' * int((amount_of_asterisks/2))
        title = half_line + self.name + half_line

        ledger_txt = ""
        total = 0

        # Append items to text
        for element in self.ledger:
            ledger_txt += f'\n{element["description"][:23]}{str("{:.2f}".format(element["amount"])).rjust(len(title) - len(element["description"][:23]))}'
            total += element["amount"]
        ledger_txt += f'\nTotal: {total}'

        # Build final text
        category_string = title + ledger_txt

        return category_string


def create_spend_chart(categories):
    # Get withdrawals by category
    spent_values = {}
    for category in categories:
        category_total = 0
        for item in category.ledger:
            category_total += -item['amount'] if item['amount'] < 0 else 0
            spent_values[category.name] = category_total
    
    # Get withdrawals total
    total_withdrawals = sum(spent_values.values())

    # Get percentage by category
    percentages = []
    for price in spent_values.values():
        amount = (price * 100)/total_withdrawals
        percentages.append(amount)

    # Build chart
    spend_chart_title = "Percentage spent by category"
    spend_chart = ""
    for i in range(100, -1, -10):
        spend_chart += f"\n{' ' * (3-len(str(i)))}{i}|"
        for item in percentages:
            spend_chart += ' o ' if int(item) >= i else '   '
        spend_chart += ' '
    spend_chart_line = f"\n    {'-' * (3 * len(percentages) + 1) }"

    # Add category titles on bottom of the chart
    vertical_category_display = ''
    max_length = max(len(category) for category in spent_values)
    # Transpose the list of strings, replacing missing characters with empty strings
    transposed_list = [
    tuple(category[i] if i < len(category) else ' ' for category in spent_values)
    for i in range(max_length)
    ]
    for index in transposed_list:
        vertical_category_display += "\n     "
        for letter in index:
            vertical_category_display += f"{letter}  "

    result = spend_chart_title + spend_chart + spend_chart_line + vertical_category_display

    return result


# Food
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(50, "groceries")
# Clothing
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(50)
# Auto
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(50)

print(create_spend_chart([food, clothing, auto]))