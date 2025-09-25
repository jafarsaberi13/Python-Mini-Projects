class Person:
    def __init__(self, firstName, lastName, email, income = 0, expense = 0, total = 0):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.income = income
        self.expense = expense
        self.total = total

    def __str__(self):
        return f"===>>>    Your deteils    <<<+===\n", f"Name: {self.firstName}\n", f"LastName: {self.lastName}\n", f"email: {self.email}\n", f"income: {self.income}\n", f"expense: {self.expense}\n", f"total: {self.total}"


