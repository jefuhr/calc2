from calculator.calculations.multiplication import multiplcation

def test_calculation_multiplication():
    #Arrange
    mynumbers = (1.0,2.0)
    addition = Multiplication(mynumbers)
    #Act
    #Assert
    assert addition.get_result() == 3.0