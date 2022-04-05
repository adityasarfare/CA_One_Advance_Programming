class Employee:
    def __init__(self,StaffID,LastName, FirstName, RegHours, HourlyRate, OTMultiple, TaxCredit, StandardBand):
        self.__StaffID = StaffID
        self.__LastName = LastName
        self.__FirstName = FirstName
        self.__RegHours = RegHours
        self.__HourlyRate = HourlyRate
        self.__OTMultiple = OTMultiple
        self.__TaxCredit = TaxCredit
        self.__StandardBand = StandardBand

    def computePayment(self, HoursWorked, date):

        OverTimeWorked = HoursWorked - self.__RegHours
        print(OverTimeWorked)

        Over_Time_Rate = self.__HourlyRate*self.__OTMultiple
        print(Over_Time_Rate)

        Regular_Pay = self.__RegHours * self.__HourlyRate
        print(Regular_Pay)


        e=Employee(12345,'Green','Joe', 37, 16, 1.5, 72, 710)
        e.computePayment(42, '31/10/2021')