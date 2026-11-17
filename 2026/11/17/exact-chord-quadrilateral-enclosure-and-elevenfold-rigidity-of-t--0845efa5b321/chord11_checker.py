"""Exact rational interval certificate for regular hendecagon chord quadrilateral."""
from fractions import Fraction
from itertools import combinations
from math import factorial

S=10**28

def ceildiv(a,b): return -((-a)//b)
class I:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None): self.lo=lo;self.hi=lo if hi is None else hi
    @staticmethod
    def rat(x):
        x=Fraction(x);a=x.numerator*S;b=x.denominator
        return I(a//b,ceildiv(a,b))
    def __add__(a,b):
        if not isinstance(b,I):b=I.rat(b)
        return I(a.lo+b.lo,a.hi+b.hi)
    __radd__=__add__
    def __neg__(a):return I(-a.hi,-a.lo)
    def __sub__(a,b):return a+(-b if isinstance(b,I) else -I.rat(b))
    def __mul__(a,b):
        if not isinstance(b,I):b=I.rat(b)
        vals=[x*y for x in (a.lo,a.hi) for y in (b.lo,b.hi)]
        return I(min(vals)//S,ceildiv(max(vals),S))
    __rmul__=__mul__
    def __truediv__(a,b):
        if not isinstance(b,I):b=I.rat(b)
        assert b.lo>0
        if a.lo>=0: return I((a.lo*S)//b.hi,ceildiv(a.hi*S,b.lo))
        if a.hi<=0:return I((a.lo*S)//b.lo,ceildiv(a.hi*S,b.hi))
        return I((a.lo*S)//b.lo,ceildiv(a.hi*S,b.lo))

def atan_bounds(z,m):
    x=Fraction(0)
    for j in range(m):x+=Fraction((-1)**j,(2*j+1)*z**(2*j+1))
    y=x+Fraction((-1)**m,(2*m+1)*z**(2*m+1))
    return min(x,y),max(x,y)
a,b=atan_bounds(5,31);c,d=atan_bounds(239,31)
pi_lo=16*a-4*d;pi_hi=16*b-4*c
pi=I(pi_lo.numerator*S//pi_lo.denominator,ceildiv(pi_hi.numerator*S,pi_hi.denominator))

def trig(x,kind):
    term=I.rat(1) if kind=='cos' else x
    res=term
    z=x*x
    for j in range(1,35):
        term=-(term*z)/((2*j-1)*(2*j) if kind=='cos' else (2*j)*(2*j+1))
        res=res+term
    # sin first omitted |x|^71/71!, cos first omitted |x|^70/70!
    k=70 if kind=='cos' else 71
    err=I.rat(Fraction(7**k,factorial(k)))
    return I(res.lo-err.hi,res.hi+err.hi)
cs=[trig(pi*k/11,'cos') for k in range(11)]
ss=[trig(pi*k/11,'sin') for k in range(11)]
h=[I.rat(1) if j%2==0 else cs[1] for j in range(22)]

def area(ix):
    v=I.rat(0)
    for j in range(len(ix)):
        k=ix[j];l=ix[(j+1)%len(ix)];g=(l-k)%22
        v=v+(h[k]*h[l] - ((h[k]*h[k]+h[l]*h[l])/2)*cs[g])/ss[g]
    return v

def gaps(ix):return [(ix[(j+1)%len(ix)]-ix[j])%22 for j in range(len(ix))]
def redundant(ix):
    ids=set(ix)
    return any(k%2==0 and (k-1)%22 in ids and (k+1)%22 in ids for k in ids)

winner=(1,5,11,17)
opt=area(winner)
all_ok=0;three_ok=0;excluded=0;winners=[];second=None;second_combo=None;minmargin=None
for ix in combinations(range(22),4):
    if max(gaps(ix))>=11:continue
    if redundant(ix):excluded+=1;continue
    ar=area(ix)
    if ar.hi < opt.lo:raise AssertionError(('counterexample',ix))
    if ar.lo<=opt.hi:
        if ar.lo >opt.hi:raise AssertionError('impossible')
        winners.append(ix)
    else:
        gap=ar.lo-opt.hi
        if minmargin is None or gap<minmargin:minmargin=gap
        if second is None or ar.hi<second.lo:second=ar;second_combo=ix
    all_ok+=1
for ix in combinations(range(22),3):
    if max(gaps(ix))>=11:continue
    ar=area(ix)
    if ar.lo<=opt.hi:raise AssertionError(('bad triangle',ix))
    three_ok+=1
expected={tuple(sorted((k+2*r)%22 for k in (1,5,11,17))) for r in range(11)}
assert set(winners)==expected,(winners,expected)
assert minmargin > S//125, 'Nonwinner separation too small'
print('pi width',pi.hi-pi.lo,'trig cosine1',cs[1].lo/S,cs[1].hi/S)
print('winner',round(opt.lo/S,14),round(opt.hi/S,14),'winners',len(winners))
print('winner list',winners)
print('checked essential quadrilaterals',all_ok,'redundant',excluded,'bounded triangles',three_ok)
print('next representative',second_combo, round(second.lo/S,14),round(second.hi/S,14),'certified gap ≥',minmargin/S)
print('Certificate PASS')
