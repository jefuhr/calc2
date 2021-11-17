from calculator.calculations.calculation import Calculation

class Division(Calculation):

    def get_result(self):

        result = 1.0
        for value in self.values:
            result =  value / result
        return result