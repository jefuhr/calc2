from calculator.calculations.multiplication import Multiplication


def test_calculation_multiplication():
    #Arrange
    mynumbers = (1.0,2.0)
    multiplication = Multiplication(mynumbers)
    #Act
    #Assert
    assert multiplication.get_result() == 2.0
