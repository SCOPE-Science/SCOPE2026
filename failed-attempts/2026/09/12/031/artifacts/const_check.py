from mpmath import mp, mpf, pi, sqrt, zeta, hurwitz
mp.dps = 50
c0 = 1/(2*sqrt(2*pi))
a_star = sqrt(2*pi)/3
print("c0 =", c0)
print("a_star =", a_star)
# Dirichlet beta via Hurwitz: beta(s) = 4^-s (zeta(s,1/4)-zeta(s,3/4))
s = mpf(1)/4
beta = (mpf(4)**(-s))*(hurwitz(s, mpf(1)/4) - hurwitz(s, mpf(3)/4))
print("zeta(1/4) =", zeta(s))
print("beta(1/4) =", beta)
Z = 4*zeta(s)*beta
print("Z(1/4) =", Z)
print("a0 = c0*Z =", c0*Z)
