"""Independently enumerate idempotent additive maps and Takasaki-quandle retractions.
No external packages. Counts by two isomorphism-type ranks (free p^2, p).
"""
from itertools import product
from math import prod


def group_data(p,a,b):
    mods=(p*p,)*a+(p,)*b
    elems=list(product(*[range(m) for m in mods]))
    return mods,elems

def generators(mods):
    return [tuple(1 if j==i else 0 for j in range(len(mods))) for i in range(len(mods))]

def apply(cols,x,mods):
    return tuple(sum(x[j]*cols[j][i] for j in range(len(mods)))%mods[i] for i in range(len(mods)))

def subtract(x,y,mods):
    return tuple((u-v)%m for u,v,m in zip(x,y,mods))

def add(x,y,mods):
    return tuple((u+v)%m for u,v,m in zip(x,y,mods))

def hom_generator_choices(mods,p):
    all_elem=list(product(*[range(m) for m in mods]))
    torsion=[v for v in all_elem if all((p*c)%m==0 for c,m in zip(v,mods))]
    return [all_elem if m==p*p else torsion for m in mods]

def rank_type(p,mods,im):
    # Absent a full image subgroup enumeration: |p im|=p^r; |im|=p^(2r+s).
    r=0
    powers={tuple(p*x % m for x,m in zip(v,mods)) for v in im}
    k=len(powers)
    while k>1:
        assert k%p==0
        r+=1;k//=p
    t=len(im);n=0
    while t>1:
        assert t%p==0
        n+=1;t//=p
    return r,n-2*r

def brute(p,a,b):
    mods,elems=group_data(p,a,b)
    zero=tuple(0 for m in mods)
    totals={}
    aff={}
    for cols in product(*hom_generator_choices(mods,p)):
        if any(apply(cols,cols[j],mods)!=cols[j] for j in range(len(cols))): continue
        images={apply(cols,x,mods) for x in elems}
        typ=rank_type(p,mods,images)
        totals[typ]=totals.get(typ,0)+1
        kern=len(elems)//len(images)
        aff[typ]=aff.get(typ,0)+kern
    return totals,aff

def aut(p,a,b):
    # Aut(C_(p^2)^a + C_p^b) = p^(a^2+2ab) GL_a(p) GL_b(p).
    # avoid fractional: |GL_n(p)| * p^{(a+b)^2+a^2 -a^2 - b^2}
    def gl(n): return prod(p**n-p**i for i in range(n))
    return p**(a*a+2*a*b)*gl(a)*gl(b)

def predicted(p,a,b):
    d={};q={}
    whole=aut(p,a,b)
    for r in range(a+1):
        for s in range(b+1):
            v=whole//(aut(p,r,s)*aut(p,a-r,b-s))
            assert whole%(aut(p,r,s)*aut(p,a-r,b-s))==0
            d[(r,s)]=v
            q[(r,s)]=v*p**(2*(a-r)+(b-s))
    return d,q

def main():
    for p,a,b in [(3,0,2),(3,2,0),(3,1,1),(5,1,1),(3,1,2)]:
        x,y=brute(p,a,b)
        u,v=predicted(p,a,b)
        assert x==u,(p,a,b,x,u)
        assert y==v,(p,a,b,y,v)
        print('verified',p,a,b,'group size',p**(2*a+b),'linear',sum(x.values()),'quandle',sum(y.values()),'types',x,'affine_by_type',y)
    # Verify actual quandle equation and idempotence for every affine map at group order 27.
    p,a,b=3,1,1
    mods,elems=group_data(p,a,b)
    def qop(x,y):return tuple((2*y[i]-x[i])%mods[i] for i in range(len(mods)))
    checked=0
    for cols in product(*hom_generator_choices(mods,p)):
        for c in elems:
            f=lambda x:add(apply(cols,x,mods),c,mods)
            if any(f(qop(x,y))!=qop(f(x),f(y)) for x in elems for y in elems):
                raise AssertionError('not a quandle morphism')
            if all(f(f(x))==f(x) for x in elems):checked+=1
    assert checked==sum(predicted(p,a,b)[1].values())
    print('all 6561 affine maps preserve quandle identity; idempotents',checked)
    print('MIXED_TAKASAKI_CHECKS_PASSED')
if __name__=='__main__':main()
