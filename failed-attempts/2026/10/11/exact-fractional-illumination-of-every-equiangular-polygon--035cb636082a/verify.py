#!/usr/bin/env python3
import math
from fractions import Fraction

def adiff(a,b):
    return abs((a-b+math.pi)%(2*math.pi)-math.pi)

# Exact integer incidence certificate for all n in range.
for n in range(3,501):
    r=(n-1)//2
    assert r>=1
    # A direction can illuminate at most r equally spaced vertex cones:
    # r centers fit strictly, while r+1 would span r spacings, which is
    # not shorter than the illumination-arc length.
    # Verify the equivalent exact integer inequalities without floating point.
    assert 2*(r-1) < n-2
    assert 2*r >= n-2

    loads=[Fraction(0,1) for _ in range(n)]
    for j in range(n):
        for k in range(r):
            loads[(j+k)%n]+=Fraction(1,r)
    assert all(x==1 for x in loads)
    assert sum(Fraction(1,r) for _ in range(n))==Fraction(n,r)
    assert Fraction(n,r)==(Fraction(2*n,n-1) if n%2 else Fraction(2*n,n-2))

# Independent geometric sampling of every combinatorial cell for small/medium n.
for n in range(3,61):
    delta=2*math.pi/n
    alpha=math.pi-delta
    r=(n-1)//2
    centers=[2*math.pi*j/n for j in range(n)]
    events=sorted([(b+s*alpha/2)%(2*math.pi) for b in centers for s in (-1,1)])
    probes=[]
    for i,a in enumerate(events):
        b=events[(i+1)%len(events)]
        probes.append((a+((b-a)%(2*math.pi))/2)%(2*math.pi))
    assert max(sum(adiff(u,b)<alpha/2-1e-10 for b in centers) for u in probes)==r

special={3:Fraction(3,1),4:Fraction(4,1),5:Fraction(5,2),6:Fraction(3,1),8:Fraction(8,3)}
for n,v in special.items():
    assert Fraction(n,(n-1)//2)==v

print('VERIFY_OK')
print('exact_integer_range = 3..500')
print('geometric_cell_sweep = 3..60')
print('cyclic_equal_weight_cover = exact')
print('special_values = passed')
