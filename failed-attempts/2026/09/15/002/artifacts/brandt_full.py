"""Full Brandt matrix computation for disc 109 via O/lO ≅ M2(F_l) neighbor enumeration + class identification."""
from fractions import Fraction
from itertools import product
import json

def mulm_factory(l, c109=109):
    def mulm(a,b):
        a0,a1,a2,a3=a; b0,b1,b2,b3=b
        return (
          (a0*b0 -2*a1*b1 -c109*a2*b2 -218*a3*b3)%l,
          (a0*b1 + a1*b0 +c109*a2*b3 -c109*a3*b2)%l,
          (a0*b2 + a2*b0 -2*a1*b3 +2*a3*b1)%l,
          (a0*b3 + a3*b0 + a1*b2 - a2*b1)%l)
    return mulm

def matrix_units(l):
    mulm = mulm_factory(l)
    def iszero(a): return all(v==0 for v in a)
    one=(1,0,0,0)
    prop=[a for a in product(range(l),repeat=4) if mulm(a,a)==a and not iszero(a) and a!=one]
    e=prop[0]
    f=tuple((one[i]-e[i])%l for i in range(4))
    e12=[a for a in product(range(l),repeat=4) if mulm(e,a)==a and iszero(mulm(a,e)) and not iszero(a)]
    e21=[a for a in product(range(l),repeat=4) if mulm(a,e)==a and iszero(mulm(e,a)) and not iszero(a)]
    x=e12[0]
    for y in e21:
        if mulm(x,y)==e: break
    return {"e11":e,"e12":x,"e21":y,"e22":mulm(y,x)}

for l in [3,5,7]:
    mu = matrix_units(l)
    print(l, mu, flush=True)
