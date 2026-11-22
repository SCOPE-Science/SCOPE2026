"""Exact reproducibility checks for a branching-genealogy sampling design."""
from fractions import Fraction as F
from math import log

# Strings encode depth-five binary paths from a single depth-zero ancestor.
# Individuals with different chosen depth-two prefixes have distance >=8.
families = {
    'a': ['00000', '00100'],
    'b': ['01000', '01001', '01100', '01101', '01110'],
    'c': ['10000', '10001', '10010', '10100'],
    'd': ['11000', '11001'],
}
leaves = sum(families.values(), [])
focals = ['00000','01000','10000','11000']
assert len(leaves) == len(set(leaves))
# All internal nodes have <= 2 child labels, by binary path construction.
assert all(len(x)==5 for x in leaves)

def genealogical_distance(a,b):
    shared = 0
    for x,y in zip(a,b):
        if x!=y: break
        shared+=1
    return len(a)+len(b)-2*shared

def counts(a):
    return tuple(sum(genealogical_distance(a,b)==d for b in leaves if b!=a)
                 for d in (2,4,6))

C = tuple(counts(a) for a in focals)
assert C == ((0,0,1),(1,0,3),(1,1,1),(1,0,0)), C

def det3(M):
    (a,b,c),(d,e,f),(g,h,i) = M
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
assert det3(C[:3]) == 1

def g(t,counts):
    return sum(F(count)*t**j for j,count in enumerate(counts,1))

def eta(t,b0,b1,design):
    return tuple(b0+b1*g(t,row) for row in design)

def alternate(t):
    s=(1-2*t)/(2*(1+t))
    b1=t*(1+2*t*t)/(s*(1+2*s*s))
    b0=t**3-b1*s**3
    return s,b0,b1

t=F(1,5)
s,b0p,b1p=alternate(t)
assert (s,b0p,b1p)==(F(1,4),-F(1,250),F(96,125))
assert eta(t,F(0),F(1),C[:3]) == (F(1,125),F(28,125),F(31,125))
assert eta(t,F(0),F(1),C[:3]) == eta(s,b0p,b1p,C[:3])
assert eta(t,F(0),F(1),C)[3] != eta(s,b0p,b1p,C)[3]
assert eta(t,F(0),F(1),C)[3]-eta(s,b0p,b1p,C)[3] == F(3,250)

for numer in range(1,50):
    t=F(numer,100)
    s,b0p,b1p=alternate(t)
    assert 0<s<F(1,2)
    assert eta(t,F(0),F(1),C[:3]) == eta(s,b0p,b1p,C[:3])
    assert b1p>0
    # The (s,t) pair coincides only at an irrational stationary point.
    assert s!=t
    assert eta(t,F(0),F(1),C)[3] != eta(s,b0p,b1p,C)[3]

# Strict monotonicity of (1-t^2)/(1+2*t^2) can be checked
# by the exact cross-multiplied positive difference for all 0<s<t<1.
for a in range(1,20):
    for b in range(a+1,20):
        s,t=F(a,20),F(b,20)
        assert (1-s*s)/(1+2*s*s) > (1-t*t)/(1+2*t*t)

print('PASS: rooted binary family realization; determinant; exact alias; 49 rational aliases; fourth-individual separation; monotone reconstruction.')
