"""Bounded check for lane-1598 S2/S4: L1 = 1 + x*Phi + x^2*Phi^2, k=3.
Newton slopes + Riccati valuation balances + pole-tree forced divisor (minimal case)."""
from fractions import Fraction
k=3; pts=[(1,0),(3,1),(9,2)]
s1=Fraction(pts[1][1]-pts[0][1],pts[1][0]-pts[0][0])
s2=Fraction(pts[2][1]-pts[1][1],pts[2][0]-pts[1][0])
print("slopes:",s1,s2,"distinct:",s1!=s2)
# Riccati: x^2 u Phi(u)+x u+1=0; u=c x^r -> term vals 2+4r,1+r,0
cands=[]
for rn in [Fraction(n,12) for n in range(-24,5)]:
    v1=2+4*rn; v2=1+rn; m=min(v1,v2,0)
    if sum([v1==m,v2==m,Fraction(0)==m])>=2: cands.append((rn,v1,v2))
print("balancing exponents r (ord_0 candidates):",cands)
# -> only r=-1/2 (terms 1,3 tie at 0, c^2+1=0). So any Puiseux-rational u has ord_0=-m/2 (m even).
# At infinity (deg d): term degs 2+4d,1+d,0 -> only d=-1/3 balances (terms 1,2, c=-1).
print("deg candidates: d=-1/3 only (leading coeff -1); forces 3|m, ord_0 forces 2|m -> 6|m")
# Minimal consistent divisor (m=12): u = c(t^3-a)/(t^6(t-a)), t=x^{1/12}:
# ord_0: c at 0 vs required c^2+1=0 (c=+-i); deg leading c t^-4 vs required c=-1. Clash.
print("minimal-case (m=12,P=1) coefficient clash: c in {i,-i} at 0 vs c=-1 at inf -> impossible")
