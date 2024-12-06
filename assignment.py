#does not seem to work for some reason 
num_iterations = int(input("Enter the number of iterations: "))
pi_value = 0
for n in range(num_iterations):
    term = 4 / (2 * n + 1)
    if n % 2 == 0:
        term = term
    else:
        term = -term
        pi_value += term
print("The value of pi is:",pi_value)
