from fractions import Fraction
# Exact stall lemma: 16x16 proxy, p=1/2, cell v=(8,0), canonical component-revealing
# vertical-interface exploration with uniform start row U in {0..15}.
# P[query v] >= (1/16) * sum_u (p^L+(1-p)^L), L=|u-8|+1.
p = Fraction(1,2)
S = sum(p**(abs(u-8)+1) + (1-p)**(abs(u-8)+1) for u in range(16))
bound = S / 16
print("S =", S, "=", float(S))
print("bound =", bound, "=", float(bound))
print("cap = 1/10 =", 0.1)
assert bound == Fraction(765,4096), bound
assert bound > Fraction(1,10)
print("margin =", bound - Fraction(1,10), "=", float(bound-Fraction(1,10)))
print("VERIFY_OK")
