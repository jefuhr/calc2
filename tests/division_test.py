from calculator.calculations.division import Division


def test_calculation_division():
    #Arrange
    mynumbers = (2.0,4.0)
    division = Division(mynumbers)
    #Act
    #Assert
    assert division.get_result() == 2.0
