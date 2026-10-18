from fractions import Fraction as F

# Exact cyclic Lorenz-96 energy cancellation.
x = [F(2, 3), F(-5, 4), F(7, 6), F(9, 5), F(-4, 7), F(11, 8), F(3, 2), F(-2, 5)]
N = len(x)

def A(i):
    return (x[(i+1) % N] - x[(i-2) % N]) * x[(i-1) % N]

cancel = sum(x[i] * A(i) for i in range(N))
assert cancel == 0

# Classical stationary site-time relation.
forcing = F(8)
m = F(3)
EX2 = forcing * m
varX = EX2 - m*m
assert varX == m * (forcing - m)
assert varX == F(15)

# Abstract conditional-residual algebra A = X-F+V.
varV = F(7, 3)
covXV = F(0)
varA = varX + varV + 2*covXV
covXA = varX + covXV
assert varA == varX + varV
assert covXA == varX

# Exact squared-correlation formula.
corr2 = covXA * covXA / (varX * varA)
assert corr2 == varX / (varX + varV)
assert F(0) < corr2 < F(1)

print("VERIFY_OK")
