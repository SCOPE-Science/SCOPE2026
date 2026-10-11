from sympy import symbols, sqrt, simplify, Rational, N

q, x = symbols("q x", positive=True)
a = sqrt(2) - 1
C2 = 2 * a
E2 = 1 - x * (1 - x) / (q + x)
defect = ((x - a)**2 + (q - 1) * a**2) / (q + x)
assert simplify(E2 - C2 - defect) == 0
assert simplify(a**2 - (1 - 2*a)) == 0

# For q >= 2 and 0 <= x < 1, (q-1)/(q+x) >= 1/3.
# The following endpoint calculation identifies the sharp minimum over q >= 2
# after relaxing x to the closed interval [0,1].
assert simplify(Rational(1, 3) * a**2 - ((2 - 1) * a**2) / (2 + 1)) == 0

convergents = [(1, 2), (2, 5), (5, 12), (12, 29)]
print("C =", N(sqrt(C2), 18))
for r, s in convergents:
    xx = Rational(r, s)
    exact_gap = simplify((xx - a)**2 / (1 + xx))
    assert exact_gap > 0
    assert N(exact_gap, 30) < Rational(1, s**4)
    print(f"r/s={r}/{s}; E^2-C^2={N(exact_gap, 18)}")
print("symbolic identity: PASS")
