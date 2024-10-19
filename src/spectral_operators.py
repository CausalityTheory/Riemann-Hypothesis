import numpy as np
from scipy.special import zeta, gamma

# Riemann Zeta function definition
def riemann_zeta(s):
    return zeta(s)

# Define a spectral operator for s in the complex plane
def spectral_operator(s):
    return (1/2) * s * (s - 1) * np.pi**(-s / 2) * gamma(s / 2) * riemann_zeta(s)

# Example calculation
if __name__ == "__main__":
    t = 14.134725  # First non-trivial zero
    s = 1/2 + 1j * t
    result = spectral_operator(s)
    print(f"Spectral operator evaluated at s = 1/2 + {t}i: {result}")
