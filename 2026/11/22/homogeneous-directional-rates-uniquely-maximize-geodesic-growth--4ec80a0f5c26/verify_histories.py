"""Independent exhaustive event-history test with Fraction arithmetic.
Run: python verify_histories.py (Python standard library only).
"""
from fractions import Fraction
from collections import defaultdict

N3 = (3616,26912,82162,137585,139614,88714,35054,8229,1035,54)
N5 = (448,1728,3076,3334,2814,2428,1851,890,213,18)
N7 = (16,8,1,4,16,21,9)

def poly(c,x):
    return sum((v*x**i for i,v in enumerate(c)),Fraction(0))

def formula(x):
    d = 8*(x+1)**2*(x+2)**3*(x+4)**2*(3*x+2)**2
    return (poly(N3,x)/d, poly(N5,x)/d, (x+2)*poly(N7,x)/d)

def enumerate_histories(x):
    rates = (Fraction(1),Fraction(1),x)
    output = defaultdict(Fraction)
    count = 0
    def walk(mask, parents, weight):
        nonlocal count
        if mask & 128:
            count += 1
            length=0
            v=7
            while v != 0:
                v = parents[v]
                length += 1
            output[length] += weight
            return
        cut=[]
        for u in range(8):
            if mask >> u & 1:
                for i in range(3):
                    v = u ^ (1<<i)
                    if not (mask >> v & 1):
                        cut.append((u,v,rates[i]))
        total = sum((r for _,_,r in cut),Fraction(0))
        for u,v,r in cut:
            nxt = list(parents)
            nxt[v] = u
            walk(mask | (1 << v), tuple(nxt), weight*r/total)
    walk(1, tuple([-1]*8), Fraction(1))
    assert count == 7368
    assert set(output) == {3,5,7}
    assert sum(output.values()) == 1
    return tuple(output[i] for i in (3,5,7))

for x in (Fraction(1,4),Fraction(1,2),Fraction(1),Fraction(2),Fraction(5),Fraction(10)):
    actual = enumerate_histories(x)
    assert actual == formula(x), (x, actual, formula(x))
    print('PASS rate=',x,'law=',actual)
print('PASS: 7368 genealogical edge-event histories per rate, six rational rates')
