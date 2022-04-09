import unittest


class CA_One_Employee:
    def __init__(self,StaffID,LastName, FirstName, RegHours, HourlyRate, OTMultiple, TaxCredit, StandardBand):
        if (RegHours < 0 or StaffID < 0 or OTMultiple < 0 or HourlyRate < 0 or TaxCredit < 0 or StandardBand < 0):
            raise ValueError("This values cannot be negative.")

        self.__StaffID = StaffID
        self.__LastName = LastName
        self.__FirstName = FirstName
        self.__RegHours = RegHours
        self.__HourlyRate = HourlyRate
        self.__OTMultiple = OTMultiple
        self.__TaxCredit = TaxCredit
        self.__StandardBand = StandardBand

    def computePayment(self, HoursWorked, date):

        if (self.__RegHours > HoursWorked):
            raise ValueError("Regular Hours Worked cannot exceed worked hours")
        else:
            OverTimeWorked = HoursWorked - self.__RegHours
            print(OverTimeWorked)

        # if(OverTimeWorked < 0):
        #     raise ValueError('OverTimeWorked cannot be negative!')


        OverTimeRate = self.__HourlyRate*self.__OTMultiple

        print(OverTimeRate)

        RegularPay = self.__RegHours * self.__HourlyRate
        print(RegularPay)

        OverTimepay = OverTimeRate * OverTimeWorked
        if (OverTimepay < 0):
            raise ValueError('OverTimePay cannot be negative!')
        print(OverTimepay)

        GrossPay = RegularPay + OverTimepay
        print(GrossPay)

        HigherRatePay = GrossPay - self.__StandardBand
        print(HigherRatePay)

        # 20% Standard Tax
        StdTax = GrossPay * 0.2
        rndStdTax = round(StdTax)
        print(rndStdTax)


        # HigherTax = HigherRatePay*0.4
        if (HigherRatePay < 0):
            raise ValueError("Higher Tax cannot be negative")
        else:
            HigherTax = HigherRatePay * 0.4
        print(HigherTax)


        TotalTax = rndStdTax + HigherTax
        print(TotalTax)

        NetTax = TotalTax - self.__TaxCredit
        print(NetTax)

        # PRSI (at 4%)
        PRSI = GrossPay * 0.04
        print(PRSI)

        NetDeduction = NetTax + PRSI
        print(NetDeduction)

        if(NetDeduction > GrossPay):
          raise ValueError("Net Pay cannot be negative")
        else:
             NetPay = GrossPay - NetDeduction
        print(NetPay)

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


# e=CA_One_Employee(12345,'Green','Joe', 37, 16, 1.5, 72, 710)
# e.computePayment(42, '31/10/2021')

class testCA_One_Employee(unittest.TestCase):

    # Testing class thoroughly
    def testNegativeStaffID(self):
        emp = CA_One_Employee(-12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        self.assertRaises(ValueError)

    def testNegativeRegHours(self):
        emp = CA_One_Employee(12345, 'Green', 'Joe', -37, 16, 1.5, 72, 710)
        self.assertRaises(ValueError)

    def testNegativeHourlyRate(self):
        emp = CA_One_Employee(12345, 'Green', 'Joe', 37, -16, 1.5, 72, 710)
        self.assertRaises(ValueError)

    def testNegativeOTMultiple(self):
        emp = CA_One_Employee(12345, 'Green', 'Joe', 37, 16, -1.5, 72, 710)
        self.assertRaises(ValueError)

    def testNegativeTaxCredit(self):
        emp = CA_One_Employee(12345, 'Green', 'Joe', 37, 16, 1.5, -72, 710)
        self.assertRaises(ValueError)

    def testNegativeStandardBand(self):
        emp = CA_One_Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, -710)
        self.assertRaises(ValueError)


    # Net pay cannot exceed gross pay
    def testNetPayCannotExceedGrosspay(self):
        emp = CA_One_Employee(12345,'Green','Joe', 37, 16, 1.5, 72, 710)
        cal = emp.computePayment(42, '31/10/2021')
        self.assertLessEqual(cal['Net Pay'], cal['Gross Pay'])

        # Overtime pay cannot be negative.

    def testOverTimePayCannotBeNegative(self):
        emp = CA_One_Employee(12345, 'Green', 'Joe', 37, -16, 1.5, 72, 710)
        pi = emp.computePayment(42, '31/10/2021')
        self.assertLessEqual(0, pi["Overtime Pay"])

        # Regular Hours cannot be greater than the Hours worked

    def testRegHoursNotGreaterThanHoursWorked(self):
        emp = CA_One_Employee(12345, 'Green', 'Joe', 73, 16, 1.5, 72, 710)
        pi = emp.computePayment(42, '31/10/2021')
        self.assertLessEqual(pi["Regular Hours Worked"], pi["Hours Worked"])

        # Higher Tax cannot be negative.

    def testHigherTaxCannotBeNegative(self):
        e = CA_One_Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 715)
        pi = e.computePayment(42, '31/10/2021')
        self.assertLessEqual(0, pi["Higher Tax"])

        # Net Pay cannot be negative

    def testNetPayCannotBeNegative(self):
        e = CA_One_Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        calc = e.computePayment(42, '31/10/2021')
        self.assertLessEqual(calc["Net Pay"], 0)


unittest.main(argv=['ignored'],exit=False)