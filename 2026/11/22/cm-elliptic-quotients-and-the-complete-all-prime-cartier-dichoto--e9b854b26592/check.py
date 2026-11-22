"""Exact checks for the genus-two Chebyshev quintic arithmetic claim.
Requires Python 3 and SymPy. Finite-field tests corroborate, not prove, the universal classification.
"""
from sympy import symbols, Poly, factor, rem, together, primerange

x,u,d = symbols('x u d')
rel=d**4-5
f=x**5-5*x**3+5*x
K=5+2*d**2
U=x+d**2/x
for sgn in (1,-1):
    e=(u+2*sgn*d)*(u**2-K)
    v2=f*(x+sgn*d)**2/x**4
    num=together(v2-e.subs(u,U)).as_numer_denom()[0]
    assert rem(num,rel,d)==0, ('elliptic quotient identity failed',sgn)
# j=c4^3/Delta with b-invariants for y^2 = u^3 + a2*u^2 + a4*u + a6
cubic=(u+2*d)*(u**2-K)
_,a2,a4,a6=Poly(cubic,u).all_coeffs()
b2,b4,b6,b8=4*a2,2*a4,4*a6,4*a2*a6-a4*a4
c4=b2*b2-24*b4
Delta=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
j=c4**3/Delta
assert rem(together(j-(632000+282880*d**2)).as_numer_denom()[0],rel,d)==0
J=symbols('J')
assert (632000+282880*d**2)**2-1264000*(632000+282880*d**2)-681472000 != 0 # simplify modulo relation below
assert rem((632000+282880*d**2)**2-1264000*(632000+282880*d**2)-681472000,rel,d)==0

def coefficient(p,m):
    n=(p-1)//2
    if (m-n)%2: return 0
    s=(m-n)//2
    if s<0 or s>2*n: return 0
    factorial=[1]*(n+1)
    for a in range(1,n+1):factorial[a]=factorial[a-1]*a%p
    total=0
    for a in range(max(0,s-n),min(n,s//2)+1):
        b=s-2*a;c=n-a-b
        if c>=0:
            multinomial=factorial[n]*pow(factorial[a]*factorial[b]*factorial[c]%p,-1,p)%p
            total=(total+multinomial*pow(-5,b,p)*pow(5,c,p))%p
    return total

def square_symbol(a,p):
    return 1 if pow(a%p,(p-1)//2,p)==1 else -1

for p in primerange(3,200):
    if p==5: continue
    a,b,c,dd=[coefficient(p,i) for i in (p-1,p-2,2*p-1,2*p-2)]
    det=(a*dd-b*c)%p
    inert = square_symbol(-5,p)==-1
    if inert: assert (a,b,c,dd)==(0,0,0,0),(p,'expected superspecial',a,b,c,dd)
    else: assert det,(p,'expected ordinary',a,b,c,dd)
print('PASS: both quotient identities, CM j polynomial, and Hasse-Witt rank for primes 3 <= p < 200, p !=5')
