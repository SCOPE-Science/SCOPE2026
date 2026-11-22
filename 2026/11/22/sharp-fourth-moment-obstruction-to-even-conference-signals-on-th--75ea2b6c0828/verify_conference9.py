"""Standalone exact autocorrelation and numerical DFT checks for nine-cycle even phases.

Uses only the Python standard library; this is supporting verification, not a proof of
infinite statements or originality.
"""
from collections import defaultdict
from math import cos, sin, pi
import cmath

# Laurent monomials z^k with conjugation z -> z^-1 on |z|=1.
def mon(k, s=1):
    return {k: s} if s else {}

def add(*args):
    out = defaultdict(int)
    for a in args:
        for k, v in a.items(): out[k] += v
    return {k: v for k,v in out.items() if v}

def mul(a,b):
    out=defaultdict(int)
    for k,v in a.items():
        for l,w in b.items(): out[k+l]+=v*w
    return {k: v for k,v in out.items() if v}

def conj(a): return {-k:v for k,v in a.items()}

def correlation(f,s): return add(*(mul(f[j],conj(f[(j-s)%9])) for j in range(9)))

z=mon(1); one=mon(0); neg=lambda a:{k:-v for k,v in a.items()}
patterns={
    'I':[one,neg(one),z,neg(z)],
    'II':[one,z,neg(one),neg(z)],
    'III':[one,z,neg(z),neg(one)]
}
# t=(z+z^-1)/2. Each listed polynomial represents c_s+1.
twot=add(z,mon(-1))
expected={
 'I':[add(mon(0,-2),neg(twot)),mul(mon(0,2),twot),{},add(mon(0,2),neg(twot))],
 'II':[add(mon(0,2),twot),add(mon(0,-2),twot),{},neg(mul(mon(0,2),twot))],
 'III':[mul(mon(0,2),twot),add(mon(0,2),neg(twot)),{},add(mon(0,-2),neg(twot))]
}
checks=0
for name, params in patterns.items():
    a,b,c,d=params
    f=[{},a,b,c,d,d,c,b,a]
    assert add(a,b,c,d)=={}, name
    assert correlation(f,0)=={0:8},name
    for s in range(1,5):
        got=add(correlation(f,s),one)
        assert got==expected[name][s-1],(name,s,got,expected[name][s-1])
        checks+=1
        assert correlation(f,9-s)==correlation(f,s)
        checks+=1
    # defect: 2 * sum of squares over four distinct positive shifts.
    defect={}
    for u in expected[name]: defect=add(defect,mul(mon(0,2),mul(u,u)))
    # 16 + 48 t^2 = 16 + 12(z+z^-1)^2
    assert defect==add(mon(0,16),mul(mon(0,12),mul(twot,twot))),(name,defect)
    checks+=1
    for j in range(13):
        angle=2*pi*j/13
        zz=complex(cos(angle),sin(angle))
        vals=[sum(coef*zz**exp for exp,coef in v.items()) for v in f]
        assert abs(sum(vals))<1e-12
        assert max(abs(abs(x)-1) for x in vals[1:])<1e-12
        spec=[sum(vals[x]*cmath.exp(-2j*pi*k*x/9) for x in range(9)) for k in range(9)]
        m4=sum(abs(zv)**4 for zv in spec[1:])
        t=cos(angle)
        assert abs(m4-(792+432*t*t))<1e-8,(name,j,m4,t)
        checks+=1
assert checks==3*(9+13)
print('PASSED: 27 exact Laurent-polynomial identities and 39 independent numerical DFT checks.')
