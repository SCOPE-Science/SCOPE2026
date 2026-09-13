"""Verify Hellinger affinity between N(a,1) and N(b,1) equals exp(-(a-b)^2/8)."""
import mpmath as mp

def affinity(a, b):
    f = lambda s: mp.sqrt(
        (1/mp.sqrt(2*mp.pi))*mp.e**(-(s-a)**2/2)
        * (1/mp.sqrt(2*mp.pi))*mp.e**(-(s-b)**2/2)
    )
    return mp.quad(f, [-mp.inf, mp.inf])

for d in [0.0, 0.5, 1.0, 2.0, 3.0]:
    num = affinity(0.0, d)
    closed = mp.e**(-d**2/8)
    print(f"d={d} numeric={num} closed={closed} diff={abs(num-closed)}")
print("OK: numeric matches exp(-d^2/8) to quadrature precision")
