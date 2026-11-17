"""Supplementary exact-arithmetic checks for the endpoint radial-rescaling lemma.

The arbitrary-norm result is proved analytically in RESULT.md; these are finite examples.
Run: python CHECK.py
"""
from fractions import Fraction as Q
from itertools import product

def add(u,v): return (u[0]+v[0],u[1]+v[1])
def neg(u): return (-u[0],-u[1])
def sub(u,v): return add(u,neg(v))
def mul(a,u): return (a*u[0],a*u[1])
def ratio(n,u,v): return n(u)/n(v)
def n1(v): return abs(v[0])+abs(v[1])
def ni(v): return max(abs(v[0]),abs(v[1]))
def nh(v):
    s,t=v
    return max(abs(2*s-t),abs(2*t-s),abs(s+t))/2

def build(V,n):
    a=[n(v) for v in V]
    ds=[n(sub(V[(i+1)%3],V[(i+2)%3])) for i in range(3)]
    choices=[i for i in range(3) if ds[i]>Q(3,2)*a[i]]
    if choices:
        i=choices[0]; j=(i+1)%3; k=(i+2)%3
        t=(Q(2,3)*ds[i]/a[i]-1)/2
        assert t>0
        val=ratio(n, sub(add(V[j],V[k]),mul(2*t,V[i])), sub(V[j],V[k]))
        assert val==Q(2,3),(V,n.__name__,val)
        return 'strict'
    assert all(ds[i]==Q(3,2)*a[i] for i in range(3))
    assert a[0]==a[1]==a[2]
    i,j,k=0,1,2
    numerator=add(mul(2,V[i]),V[j]); denominator=sub(mul(2,V[i]),V[j])
    assert ratio(n,numerator,denominator)<=Q(3,5)
    # r(0)<=3/5; r(t) -> infinity, so positive t exists exactly at 2/3.
    T=Q(1)
    while ratio(n,sub(numerator,mul(2*T,V[k])),denominator)<=Q(2,3): T*=2
    assert ratio(n,sub(numerator,mul(2*T,V[k])),denominator)>Q(2,3)
    return 'saturated'

counts={'strict':0,'saturated':0}
for n in [n1,ni,nh]:
    for x,y,z,w in product(range(-3,4),repeat=4):
        if x*w-y*z==0:continue
        v1=(Q(x),Q(y));v2=(Q(z),Q(w));v3=neg(add(v1,v2))
        branch=build((v1,v2,v3),n)
        counts[branch]+=1
# An exact endpoint witness in the equality case (hexagonal norm).
v=((Q(1),Q(0)),(Q(0),Q(1)),(Q(-1),Q(-1)))
assert all(nh(x)==1 for x in v)
assert all(nh(sub(v[(i+1)%3],v[(i+2)%3]))==Q(3,2) for i in range(3))
t=Q(1,12)
b1,b2,b3=mul(2,v[0]),v[1],mul(t,v[2])
assert nh(sub(add(b1,b2),mul(2,b3)))==Q(2,3)*nh(sub(b1,b2))
print('PASS',counts,'total',sum(counts.values()),'and exact exceptional witness t=1/12')
