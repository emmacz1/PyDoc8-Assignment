class RentalProperty:
    def __init__(self, rental_income, laundry_income, taxes, insurance, utilities=None, vacancy=None, repairs=None, mortgage=None, property_management=None):
        self.rental_income = rental_income
        self.laundry_income = laundry_income
        self.expenses = Expenses(taxes, insurance, utilities, vacancy, repairs, mortgage, property_management)

    def calculate_cash_flow(self):
        total_income = self.rental_income + self.laundry_income
        total_expenses = sum(vars(self.expenses).values())  # Summing all expenses
        return total_income - total_expenses

    def calculate_roi(self, initial_investment):
        cash_flow = self.calculate_cash_flow()
        return (cash_flow * 12) / initial_investment * 100

class Expenses:
    def __init__(self, taxes, insurance, utilities=None, vacancy=None, repairs=None, mortgage=None, property_management=None):
        self.taxes = taxes
        self.insurance = insurance
        self.utilities = utilities or 0
        self.vacancy = vacancy or 0
        self.repairs = repairs or 0
        self.mortgage = mortgage or 0
        self.property_management = property_management or 0

# Input data
property_data = {
    "rental_income": 2000.00,
    "laundry_income": 390.00,
    "taxes": 150.00,
    "insurance": 100.00,
    "utilities": 0,
    "vacancy": 100.00,
    "repairs": 100.00,
    "mortgage": 860.00,
    "property_management": 200.00
}

initial_investment = 50000.00  # Total initial investment

# Create rental property object
rental_property = RentalProperty(**property_data)

# Calculate ROI
roi = rental_property.calculate_roi(initial_investment)
print("Cash on Cash ROI: {:.2f}%".format(roi))