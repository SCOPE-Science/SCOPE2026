#!/usr/bin/env python3
"""Coefficientwise integer-polynomial certificate for the six-variable identity.

Uses only the Python standard library. Equality is exact for all complex (hence
all positive real) values of the named variables, not an interpolation test.
"""
class Poly:
    def __init__(self, terms=None):
        self.v={m:c for m,c in (terms or {}).items() if c}
    def __add__(self,other):
        other=coerce(other); result=self.v.copy()
        for m,c in other.v.items(): result[m]=result.get(m,0)+c
        return Poly(result)
    __radd__=__add__
    def __neg__(self): return Poly({m:-c for m,c in self.v.items()})
    def __sub__(self,other): return self+-coerce(other)
    def __rsub__(self,other): return coerce(other)+-self
    def __mul__(self,other):
        other=coerce(other); result={}
        for m,c in self.v.items():
            for n,d in other.v.items():
                k=tuple(x+y for x,y in zip(m,n));result[k]=result.get(k,0)+c*d
        return Poly(result)
    __rmul__=__mul__
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        out=coerce(1)
        for _ in range(n):out=out*self
        return out
    def __eq__(self,other):return self.v==coerce(other).v

def coerce(x):
    if isinstance(x,Poly):return x
    assert isinstance(x,int)
    return Poly({(0,)*6:x})

onehot=lambda i:tuple(int(j==i) for j in range(6))
a,b,c,d,p,q=(Poly({onehot(i):1}) for i in range(6))
k=p+q
K1=a*b+a*q+b*p
K2=c*d+c*q+d*p
K12=(a+c)*(b+d)+(a+c)*q+(b+d)*p
N=(a*b+a*d+a*p+2*a*q+b*c+2*b*p+b*q+c*d+c*p+2*c*q+
   2*d*p+d*q+2*k**2)
L=(k*(q*(b+d+k)*((d+k)*K1+(b+k)*K2)
       +p*(a+c+k)*((c+k)*K1+(a+k)*K2))
   -(q*b+p*a+k**2)*(q*d+p*c+k**2)*K12)
R=p*q*(a-b)*(c-d)*N
assert L==R
print('PASS: polynomial identity,',len(L.v),'exact monomial coefficients,')
print('       factor expansion,',len(R.v),'exact monomial coefficients')
