import unittest


class CA_One_Employee:
    def __init__(self,StaffID,LastName, FirstName, RegHours, HourlyRate, OTMultiple, TaxCredit, StandardBand):

        self.__StaffID = StaffID
        self.__LastName = LastName
        self.__FirstName = FirstName
        self.__RegHours = RegHours
        self.__HourlyRate = HourlyRate
        self.__OTMultiple = OTMultiple
        self.__TaxCredit = TaxCredit
        self.__StandardBand = StandardBand

    # Compute Payment Method
    def computePayment(self, HoursWorked, date):
        
        # OverTime calculation
        if (self.__RegHours > HoursWorked):
            raise ValueError("Regular Hours Worked cannot exceed worked hours")
        else:
            OverTimeWorked = HoursWorked - self.__RegHours
            # print(OverTimeWorked)

        # OverTimeRate Calculation
        OverTimeRate = self.__HourlyRate*self.__OTMultiple
        # print(OverTimeRate)
        
        # RegularPay Calculation
        RegularPay = self.__RegHours * self.__HourlyRate
        # print(RegularPay)
        
        # OverTimepay Calculation
        OverTimepay = OverTimeRate * OverTimeWorked
        if (OverTimepay < 0):
            raise ValueError('OverTimePay cannot be negative')
        # print(OverTimepay)
        
        # GrossPay Calculation
        GrossPay = RegularPay + OverTimepay
        # print(GrossPay)
        
        # HigherRatePay Calculation
        HigherRatePay = GrossPay - self.__StandardBand
        # print(HigherRatePay)

        # 20% Standard Tax
        StdTax = GrossPay * 0.2
        rndStdTax = round(StdTax)
        # print(rndStdTax)

        # HigherTax Calculation
        HigherTax = HigherRatePay*0.4
        if (HigherTax < 0):
            raise ValueError("Higher Tax cannot be negative")
        
        # print(HigherTax)

        # TotalTax Calculation
        TotalTax = rndStdTax + HigherTax
        # print(TotalTax)
        
        # NetTax Calculation
        NetTax = TotalTax - self.__TaxCredit
        # print(NetTax)

        # PRSI (at 4%)
        PRSI = GrossPay * 0.04
        # print(PRSI)
        
        # NetDeduction Calculation
        NetDeduction = NetTax + PRSI
        # print(NetDeduction)

        if (NetDeduction > 0):
            raise ValueError("Net Pay cannot be negative")
        else:
            NetPay = GrossPay - NetDeduction
            if(NetDeduction < 0):
               raise ValueError("Net Pay cannot exceed Gross pay")
        # print(NetPay)

        dict = {
            "name": self.__FirstName + " " + self.__LastName,
            "Date": date,
            "Hours Worked": HoursWorked,
            "Regular Hours Worked": self.__RegHours,
            "Overtime Hours Worked": OverTimeWorked,
            "Regular Rate": self.__HourlyRate,
            "Overtime Rate": OverTimeRate,
            "Regular Pay": RegularPay,
            "Overtime Pay": OverTimepay,
            "Gross Pay": GrossPay,
            "Standard Rate Pay": self.__StandardBand,
            "Higher Rate Pay": HigherRatePay,
            "Standard Tax": StdTax,
            "Higher Tax": HigherTax,
            "Total Tax": TotalTax,
            "Tax Credit": self.__TaxCredit,
            "Net Tax": NetTax,
            "PRSI": PRSI,
            "Net Deductions": NetDeduction,
            "Net Pay": NetPay
        }
        print(dict)

        return dict


# emp=CA_One_Employee(12345,'Green','Joe', 37, 16, 1.5, 72, 710)
# emp.computePayment(42, '31/10/2021')

# creating a class 'CA_One_Employee' for the testing purpose:
class testCA_One_Employee(unittest.TestCase):

    # Net pay cannot exceed gross pay
    def testNetPayCannotExceedGrosspay(self):
        emp = CA_One_Employee(12345,'Green','Joe', 37, 16, 1.5, 600, 710)
        cal = emp.computePayment(42, '31/10/2021')
        self.assertLessEqual(cal['Net Pay'], cal['Gross Pay'])

        
    # Overtime pay cannot be negative.
    def testOverTimePayCannotBeNegative(self):
        emp = CA_One_Employee(12345, 'Green', 'Joe', 37, -16, 1.5, 72, 710)
        calc = emp.computePayment(42, '31/10/2021')
        self.assertLessEqual(0, calc["Overtime Pay"])

        
    # Regular Hours cannot be greater than the Hours worked
    def testRegHoursNotGreaterThanHoursWorked(self):
        emp = CA_One_Employee(12345, 'Green', 'Joe', 73, 16, 1.5, 72, 710)
        calc = emp.computePayment(42, '31/10/2021')
        self.assertLessEqual(calc["Regular Hours Worked"], calc["Hours Worked"])

        
    # Higher Tax cannot be negative. 
    def testHigherTaxCannotBeNegative(self):
        emp = CA_One_Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 715)
        calc = emp.computePayment(42, '31/10/2021')
        self.assertLessEqual(0, calc["Higher Tax"])

        
    # Net Pay cannot be negative
    def testNetPayCannotBeNegative(self):
        emp = CA_One_Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        calc = emp.computePayment(42, '31/10/2021')
        self.assertLessEqual(0, calc["Net Pay"])


unittest.main(argv=['ignored'],exit=False)