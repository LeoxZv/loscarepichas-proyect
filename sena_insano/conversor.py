#crea un programa que convierta una temperatura dada en grados celcius a fahrenheit y kelvin

celcius = float(input("Digite sus grados celcius:"))

conversor_a_F = (celcius * 1.8) + 32
conversor_a_K = (celcius + 273.15)
print("De celcius a fahrenheit es:",conversor_a_F, "y de celcius a kelvin es:",conversor_a_K)