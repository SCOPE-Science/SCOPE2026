"""[5,3,3,3] Coxeter simplex: Chiswell orbifold Euler char (terms r=0..4 only; full group infinite)."""
import itertools
from fractions import Fraction
import math

def parabolic_order(T):
    if not T: return 1
    if len(T)==5: return None
    nodes=sorted(T); comps=[]; cur=[nodes[0]]
    for n in nodes[1:]:
        if n==cur[-1]+1: cur.append(n)
        else: comps.append(cur); cur=[n]
    comps.append(cur)
    o=1
    for c in comps:
        k=len(c)
        if 0 in c and 1 in c:
            o *= {2:10,3:120,4:14400}[k]
        else:
            o*=math.factorial(k+1)
    return o

tot=Fraction(0)
for r in range(5):
    sub=Fraction(0)
    for T in itertools.combinations(range(5),r):
        o=parabolic_order(T)
        sub += Fraction((-1)**r, o)
    print(f"rank {r}: {sub} = {float(sub):.12f}")
    tot+=sub
print("chi_orb =", tot, "=", float(tot))
print("index for chi=16:", Fraction(16,1)/tot)
