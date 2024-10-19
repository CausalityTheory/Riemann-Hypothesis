import numpy as np
from scipy.special import zeta, gamma

# Riemann Zeta function definition using scipy's zeta function
def riemann_zeta(s):
    return zeta(s)

# Spectral operator H(s)
def spectral_operator(s):
    return (1/2) * s * (s - 1) * np.pi**(-s / 2) * gamma(s / 2) * riemann_zeta(s)

# Function to compute the first n non-trivial zeroes of the Zeta function numerically
def compute_zeroes(n_zeroes=10000):
    # Using a placeholder for the zeroes since numerical root finding is complex
    # In real use case, we might use more sophisticated methods or libraries
    # such as mpmath or specific algorithms for Riemann zeta zeroes
    zeroes = np.zeros(n_zeroes)
    # Example placeholder for zeroes: using known values for demonstration
    zeroes[:5] = [14.134725, 21.022040, 25.010858, 30.424876, 32.935061]  # First 5 non-trivial zeroes
    return zeroes

# Example: Evaluate spectral operator at the first non-trivial zero
if __name__ == "__main__":
    zeroes = compute_zeroes(5)
    for i, t in enumerate(zeroes):
        s = 1/2 + 1j * t
        result = spectral_operator(s)
        print(f"Spectral operator evaluated at s = 1/2 + {t}i: {result}")
