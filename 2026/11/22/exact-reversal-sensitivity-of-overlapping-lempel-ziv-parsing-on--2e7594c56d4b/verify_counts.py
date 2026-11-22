"""Independent finite-length census of reversal defects for positive four-run compositions."""
from collections import Counter
from fractions import Fraction


def length_gap(a,b,c,d):
    z = 3+int(a>1)+int(b>1)+int(c>a)+int(c>2*a)+int(d>b)
    zr = 3+int(d>1)+int(c>1)+int(b>d)+int(b>2*d)+int(a>c)
    return z-zr

first = None
for n in range(4, 31):
    ctr = Counter()
    extremal = []
    for a in range(1,n-2):
        for b in range(1,n-a-1):
            for c in range(1,n-a-b):
                d = n-a-b-c
                g = length_gap(a,b,c,d)
                assert abs(g)<=3
                ctr[g] += 1
                if abs(g)==3:
                    extremal.append((a,b,c,d,g))
    if first is None and extremal:
        first = (n,sorted(extremal))
    assert ctr[-3]==ctr[3], (n,ctr)
    assert ctr[-2]==ctr[2] and ctr[-1]==ctr[1], (n,ctr)
print('First length with |defect|=3:', first)
assert first == (12, [(2,2,5,3,3),(3,5,2,2,-3)])
prob = Counter()
a_mass = {-1:Fraction(1,2),1:Fraction(1,6),2:Fraction(1,3)}
b_mass = {-2:Fraction(1,3),-1:Fraction(1,6),1:Fraction(1,2)}
for x,p in a_mass.items():
    for y,q in b_mass.items():
        prob[x+y] += p*q
assert sorted(prob)==[-3,-2,-1,0,1,2,3]
assert sum(prob.values())==1
assert prob[0]==Fraction(7,18)
assert sum(abs(k)*p for k,p in prob.items())==Fraction(13,9)
print('Limit distribution:', [(k,str(prob[k])) for k in sorted(prob)])
print('Limit E[absolute defect]:', sum(abs(k)*p for k,p in prob.items()))
print('PASS: all positive four-run compositions through total length 30, exact reversal symmetry, sharp cutoff, and limiting-law algebra')
