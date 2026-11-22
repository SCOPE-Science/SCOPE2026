"""Exact arithmetic diagnostics for cubic planar jet rotation; not an infinite proof."""
from fractions import Fraction as Q
from math import comb

def multiply(a, b):
    out = {}
    for (i,j), x in a.items():
        for (k,l), y in b.items():
            out[(i+k,j+l)] = out.get((i+k,j+l), Q(0)) + x*y
    return out

def power(a,n):
    v={(0,0):Q(1)}
    for _ in range(n):v=multiply(v,a)
    return v

def matrix(k,c,s):
    mx = {}
    for out in range(k+1):
        p=multiply(power({(1,0):c,(0,1):s},k-out),power({(1,0):-s,(0,1):c},out))
        for inp in range(k+1):mx[out,inp]=p.get((k-inp,inp),Q(0))
    return mx

n=0
for a in range(3,79):
    for b in range(1,a):
        if b*5>a*2:continue
        c=Q(a*a-b*b,a*a+b*b)
        s=Q(2*a*b,a*a+b*b)
        if s>c:continue
        r=s/c
        m={k:matrix(k,c,s) for k in (0,1,2,3)}
        vals={k:[sum(abs(m[k][out,inp]) for out in range(k+1)) for inp in range(k+1)] for k in (0,1,2,3)}
        v2=(c*c-s*s)+4*c*s
        assert max(vals[2]) == v2
        v3=3*c*c*s+abs(c*(c*c-2*s*s))+s*(2*c*c-s*s)+3*c*s*s
        assert max(vals[3]) == v3
        assert v3>=max(vals[2])>=max(vals[1])>=max(vals[0])
        assert vals[3][1]==vals[3][2]==v3
        if 2*r*r<=1:
            assert v3*c**(-3) == (1+5*r+r*r-r*r*r)
        else:
            assert v3*c**(-3) == (-1+5*r+5*r*r-r*r*r)
        assert (v3*v3) <= 8
        n+=1
# Exact rational sign and a strict analytic bound on the first-branch maximum.
z=Q(57,100);w=Q(29,50)
q=lambda r: 5-r-13*r*r-r*r*r
p=lambda r: 1+5*r+r*r-r*r*r
assert q(z)>0 and q(w)<0
assert p(w)**2 * 9 < 64*(1+z*z)**3
print('CUBIC_ROTATION_EXACT_DIAGNOSTICS_OK',n)
