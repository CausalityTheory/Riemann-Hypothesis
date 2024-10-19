import numpy as np

# Hecke operator action on a modular form
def hecke_operator(f, n):
    return sum(f(k) for k in range(1, n + 1) if n % k == 0)

# Define a simple modular form
def modular_form(x):
    return np.exp(2 * np.pi * 1j * x)

# Apply Hecke operator to the modular form
if __name__ == "__main__":
    result = hecke_operator(modular_form, 5)
    print(f"Hecke operator result: {result}")
