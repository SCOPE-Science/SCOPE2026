"""Auxiliary algebraic checks for a discrete generalized Cesaro norm-gap theorem."""
from fractions import Fraction
import math

def q(v,t):
    return sum((v[j]-t*(v[j-1] if j else 0))**2 for j in range(len(v)+1) for _ in [0] if j<len(v)+1 and (j<len(v) or (j==len(v) and len(v)>0)))

def padded(v,k):
    return v[k] if 0<=k<len(v) else 0

for t in [Fraction(1,4),Fraction(1,2),Fraction(9,10),Fraction(1,1)]:
    for v in [(Fraction(1),), (Fraction(1),Fraction(-2),Fraction(3)), (Fraction(2),Fraction(0),Fraction(7),Fraction(-4))]:
        a=sum((padded(v,j)-t*padded(v,j-1))**2 for j in range(len(v)+1))
        b=t*sum((padded(v,j)-padded(v,j-1))**2 for j in range(len(v)+1))+(1-t)**2*sum(x*x for x in v)
        assert a==b,(t,v,a,b)

for v in ([1.,2.,-3.,4.], [3.,-1.,1.,1.,-5.], [0.2,0.4,0.6]):
    f=[v[j]/math.sqrt(j+1) for j in range(len(v))]
    left=sum((padded(v,j)-padded(v,j-1))**2 for j in range(len(v)+1)) - 0.25*sum(v[j]**2/(j+1)**2 for j in range(len(v)))
    kinetic=sum(math.sqrt(j*(j+1))*(padded(f,j)-padded(f,j-1))**2 for j in range(1,len(f)+1))
    rem=0.
    for j in range(len(f)):
        h=1/(j+1)
        r=(7/4-math.sqrt(2)) if j==0 else 2-math.sqrt(1-h)-math.sqrt(1+h)-h*h/4
        assert r>=-1e-13
        rem+=(j+1)*r*f[j]**2
    assert abs(left-kinetic-rem)<1e-10,(v,left,kinetic,rem)
print('PASS: 12 exact rational inverse identities and 3 numerical ground-state identities')
