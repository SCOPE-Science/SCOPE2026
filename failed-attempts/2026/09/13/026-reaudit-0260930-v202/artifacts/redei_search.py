"""Hand-checkable certificate for the explicit Rédei triple {5,29,181}.
This repaired artifact intentionally performs no census and makes no minimality claim.
"""
import itertools, math

def legendre(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

def poly_eval(c,x,p):
    y=0
    for a in c: y=(y*x+a)%p
    return y

# Pairwise splitting.
assert legendre(5,29)==1 and legendre(5,181)==1 and legendre(29,181)==1

# Normalized conic solution for base pair (5,29).
x,y,z=7,2,1
assert x*x-5*y*y-29*z*z==0 and math.gcd(math.gcd(x,y),z)==1
assert y%2==0 and (x-y)%4==1

# f(T)=T^4-14T^2+29 is irreducible modulo 3.
p=3
f=[1,0,-14,0,29]
assert all(poly_eval(f,r,p)!=0 for r in range(p))
# Exhaust all monic quadratic divisors T^2+aT+b.
for a,b in itertools.product(range(p),repeat=2):
    # divide f mod p by q using sympy-free long division on coefficient lists
    q=[1,a,b]
    rem=[v%p for v in f]
    for i in range(3):
        lead=rem[i]%p
        if lead:
            for j in range(3): rem[i+j]=(rem[i+j]-lead*q[j])%p
    assert rem[-2:] != [0,0]

# The cubic resolvent R(Z)=Z(Z^2+28Z+80) has exactly one rational root.
# Its nonzero quadratic factor has discriminant 28^2-4*80=464, not a square.
assert 28*28-4*80 == 464
assert int(464**0.5)**2 != 464

# A factorization pattern 1+1+2 modulo 11 then excludes the cyclic quartic C4 case.
# f=(T-2)(T+2)(T^2+1) mod 11.
for r in (2,9): assert poly_eval(f,r,11)==0
assert all((r*r+1)%11!=0 for r in range(11))

# Frobenius witness at 181.
r=27
assert r*r%181==5
vals=((x+y*r)%181,(x-y*r)%181)
assert vals==(61,134)
assert pow(vals[0],90,181)==180 and pow(vals[1],90,181)==180

# Reciprocity/order cross-check conics.
assert 11*11-29*2*2-5==0
assert 35*35-29*6*6-181==0
print('pairwise Legendre symbols: +1')
print('normalized solution (5,29):', (7,2,1))
print('cubic resolvent: exactly one rational root')
print('mod-11 factorization pattern: 1+1+2 (excludes C4)')
print('beta conjugates mod 181:', vals, 'both nonsquares')
print('Redei symbol [5,29,181] = -1')
print('CERTIFICATE CHECKS PASSED')
