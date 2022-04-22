import math

class IncomeAmount:
    """ValueObject"""
    def __init__(self, income_amount):
        if not self.isValid(income_amount): raise ValueError("Argument Out of Range")
        income_amount_after_rounddown = self.roundDownSenenMiman(income_amount)
        self.income_amount = income_amount_after_rounddown
    
    @staticmethod
    def isValid(income_amount):
        return True if 0 <= int(income_amount) <= 1000000000 else False
    
    @staticmethod
    def roundDownSenenMiman(amount):
        decimal = -3
        return int(math.floor(amount * 10 ** decimal) / (10 ** decimal))


class IncomeTax:
    """ValueObject"""
    TAXRATE1 = 0.05
    TAXRATE2 = 0.1
    TAXRATE3 = 0.2
    TAXRATE4 = 0.23
    TAXRATE5 = 0.33
    TAXRATE6 = 0.4
    TAXRATE7 = 0.45
    
    def __init__(self, income_amount):
        self.income_amount = income_amount
        
        tax_rate = self.calclateTaxRate()
        self.tax_rate = tax_rate
        
        income_tax = self.calclateIncomeTax()
        self.income_tax = income_tax
    
    def calclateTaxRate(self):
        if 1000 <= self.income_amount <= 1949000: return self.TAXRATE1
        if 1950000 <= self.income_amount <= 3299000: return self.TAXRATE2
        if 3300000 <= self.income_amount <= 6949000: return self.TAXRATE3
        if 6950000 <= self.income_amount <= 8999000: return self.TAXRATE4
        if 9000000 <= self.income_amount <= 17999000: return self.TAXRATE5
        if 18000000 <= self.income_amount <= 39999000: return self.TAXRATE6
        if 40000000 <= self.income_amount: return self.TAXRATE7
        raise ValueError("Argument Out of Range")
        
    def calclateIncomeTax(self):
        """所得税を計算(所得税額×税率 -> 千円未満切捨)"""
        return self.roundDownSenenMiman(self.income_amount * self.tax_rate)

    @staticmethod
    def roundDownSenenMiman(amount):
        return IncomeAmount.roundDownSenenMiman(amount)
    
    @staticmethod
    def formatAmount(num):
        return f"{num:,}"
    
    @staticmethod
    def formatRate(num, digits=0):
        d = str(digits)
        return f"{num:.{d}%}"


class ApplicationService:
    @staticmethod
    def run():
        user_input_income_amount = int(input("所得金額を入力してください"))
        incm_amount = IncomeAmount(user_input_income_amount)
        incm_tax = IncomeTax(incm_amount.income_amount)
        
        print("-------------------------------")
        print("あなたの所得金額")
        print(incm_tax.formatAmount(incm_tax.income_amount))
        
        print("-------------------------------")
        print("あなたの所得税率")
        print(incm_tax.formatRate(incm_tax.tax_rate))

        print("-------------------------------")
        print("あなたの所得税額")
        print(incm_tax.formatAmount(incm_tax.income_tax))


if __name__ == "__main__":
    app = ApplicationService()
    app.run()
