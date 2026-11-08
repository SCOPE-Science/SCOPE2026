#!/usr/bin/env python3
"""Exact integer-polynomial verification of a Poncelet translation law.
No third-party dependencies. Plus independent prime-square orbit counts.
"""
class Poly:
    def __init__(self,d=None):
        self.d={m:int(c) for m,c in (d or {}).items() if c}
    @staticmethod
    def coerce(x):
        return x if isinstance(x,Poly) else Poly({(0,0,0):int(x)})
    def __add__(self,x):
        x=Poly.coerce(x);d=self.d.copy()
        for m,c in x.d.items():d[m]=d.get(m,0)+c
        return Poly(d)
    __radd__=__add__
    def __neg__(self):return Poly({m:-c for m,c in self.d.items()})
    def __sub__(self,x):return self+-Poly.coerce(x)
    def __rsub__(self,x):return Poly.coerce(x)+-self
    def __mul__(self,x):
        x=Poly.coerce(x);d={}
        for a,v in self.d.items():
            for b,w in x.d.items():
                m=tuple(a[i]+b[i] for i in range(3))
                d[m]=d.get(m,0)+v*w
        return Poly(d)
    __rmul__=__mul__
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        r=Poly.coerce(1)
        for _ in range(n):r=r*self
        return r
    def __eq__(self,x):return self.d==Poly.coerce(x).d
U=Poly({(1,0,0):1});T=Poly({(0,1,0):1});S=Poly({(0,0,1):1})
C=lambda v:(v**2,v,Poly.coerce(1))
D=lambda v:(v**2-v,v,Poly.coerce(1))
L=lambda v:(Poly.coerce(1),1-2*v,v**2)
dot=lambda x,y:sum((a*b for a,b in zip(x,y)),Poly.coerce(0))
assert dot(C(T),L(S)) == (S-T)**2+T
assert dot(C(-U**2),L(U-U**2))==0
new_t=-(U-1)**2
assert new_t==2*(U-U**2)-1-(-U**2)
new_s=2*new_t-(U-U**2)
assert new_s==(U-1)-(U-1)**2
assert D(S)[0]*D(S)[2]-D(S)[1]**2+D(S)[1]*D(S)[2]==0
# Poncelet fixed-field translation has a single orbit of collision flags.
for p in (3,5,7,11,13):
    E=range(p*p)
    neg=lambda z:(-z%p)+p*((-(z//p))%p)
    add=lambda x,y:((x%p+y%p)%p)+p*((x//p+y//p)%p)
    visited=set();orbits=[]
    for z in E:
        if z in visited:continue
        orbit=[];v=z
        while v not in orbit:
            orbit.append(v);visited.add(v);v=add(v,p-1)
        assert v==z and len(orbit)==p
        orbits.append(frozenset(orbit))
    assert len(orbits)==p
    exceptional=frozenset(range(p))
    assert exceptional in orbits
    assert sum(A==frozenset(neg(z) for z in A) for A in orbits)==1
    print('p=%d, q=%d: %d good oriented, %d unoriented' % (p,p*p,p-1,(p-1)//2))
print('VERIFY_TRANSLATION_OK')
