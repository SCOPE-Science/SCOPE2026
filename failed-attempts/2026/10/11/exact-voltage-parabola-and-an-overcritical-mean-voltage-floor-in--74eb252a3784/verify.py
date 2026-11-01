from fractions import Fraction as F

I = F(3, 2)
gamma = F(2, 3)
m = F(2)

Ev2 = I * m / gamma
varv = Ev2 - m*m
assert Ev2 == F(9, 2)
assert varv == m * (I/gamma - m)
assert varv == F(1, 2)

lower = (I*I - 1) / (I*gamma)
upper = I / gamma
assert lower == F(5, 4)
assert upper == F(9, 4)
assert lower < m < upper

# Abstract residual algebra: S = I - gamma V - R,
# with E[R]=0 and Cov(V,R)=0.
varR = F(7, 20)
varS = gamma*gamma*varv + varR
covVS = -gamma*varv
assert varS == gamma*gamma*varv + varR
assert covVS == -gamma*varv

# The strict-floor derivation at the test mean.
meanS = I - gamma*m
assert gamma*gamma*varv < 1 - meanS*meanS
assert I*gamma*m > I*I - 1

print("VERIFY_OK")
