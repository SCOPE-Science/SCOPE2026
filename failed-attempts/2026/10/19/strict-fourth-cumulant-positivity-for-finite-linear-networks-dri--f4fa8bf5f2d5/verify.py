"""Exact moment checks for a linearly filtered Brownian resetting reservoir.

Only symbolic rational arithmetic is used; no numerical sampling certifies the theorem.
"""
import sympy as s
from functools import lru_cache
from math import comb

r, k, D = s.symbols('r k D', positive=True)
checks = 0

def check(expr, expected=0):
    global checks
    assert s.cancel(expr-expected) == 0, (expr, expected)
    checks += 1

# Generator of (Y,X): dY=(-kY+X)dt; X is Brownian of diffusivity D
# reset to zero at rate r; all stationary monomial moments are recursive.
@lru_cache(None)
def moment(i,j):
    if i == j == 0:
        return s.Integer(1)
    assert (i+j) % 2 == 0
    numer = s.Integer(0)
    if i:
        numer += i*moment(i-1,j+1)
    if j>=2:
        numer += D*j*(j-1)*moment(i,j-2)
    return s.factor(numer/(i*k + (r if j else 0)))

for deg in (2,4):
    for i in range(deg+1):
        j=deg-i
        lhs=(i*k+(r if j else 0))*moment(i,j)
        rhs=(i*moment(i-1,j+1) if i else 0)+(D*j*(j-1)*moment(i,j-2) if j>=2 else 0)
        check(lhs-rhs)

m2=moment(2,0)
m4=moment(4,0)
k4=s.factor(m4-3*m2**2)
excess=s.factor(k4/m2**2)
check(m2,2*D/(k*r*(k+r)))
check(k4,24*D**2*(3*k+7*r)/(k*r**2*(k+r)**2*(2*k+r)*(3*k+r)))
check(excess,6*k*(3*k+7*r)/((2*k+r)*(3*k+r)))
# The scalar check is previously implied by published low moments,
# and is not independently advanced as a discovery.
z=s.symbols('z',positive=True)
f=s.factor(excess.subs(r,z*k))
q=3*(s.sqrt(22)-1)/7
check(s.diff(f,z).subs(z,q))
check(f.subs(z,q), 174-36*s.sqrt(22))
check(s.factor(f-3), -3*z*(z-9)/((z+2)*(z+3)))

# Second independent calculation by the Poisson-clock conditional
# Gaussian variance perpetuity V = Q(A)+exp(-2kA)V', A~Exp(r).
# Here Q(A) = (2D/k^2)[A-3/(2k)+2 exp(-kA)/k-exp(-2kA)/(2k)].
# Represent Q as a linear combination of A^p exp(-a k A).
terms = [((2*D/k**2),1,0),(-3*D/k**3,0,0),(4*D/k**3,0,1),(-D/k**3,0,2)]
def ea(power, exp_coeff):
    return s.factor(r*s.factorial(power)/(r+exp_coeff*k)**(power+1))
EQ=s.factor(sum(c*ea(p,e) for c,p,e in terms))
EQ2=s.factor(sum(c*d*ea(p+u,e+v) for c,p,e in terms for d,u,v in terms))
EQe=s.factor(sum(c*ea(p,e+2) for c,p,e in terms))
mu=s.factor(EQ/(1-ea(0,2)))
sec=s.factor((EQ2+2*EQe*mu)/(1-ea(0,4)))
varV=s.factor(sec-mu**2)
check(mu,m2)
check(3*varV,k4)

# A signed two-exponential impulse response from a stable two-mode
# linear system; positive fourth cumulant is verified independently.
@lru_cache(None)
def mm(i,j,p):
    if i==j==p==0:
        return s.Integer(1)
    assert (i+j+p)%2 ==0
    num=s.Integer(0)
    if i: num+=i*mm(i-1,j,p+1)
    if j: num+=j*mm(i,j-1,p+1)
    if p>=2:num+=p*(p-1)*mm(i,j,p-2)
    return s.cancel(num/(i+2*j+(1 if p else 0)))

def z_moment(n):
    return s.factor(sum(comb(n,j)*(-2)**j*mm(n-j,j,0) for j in range(n+1)))
z2=z_moment(2)
z4=z_moment(4)
z_k4=s.factor(z4-3*z2**2)
assert z_k4 > 0
checks += 1
# All nonzero coefficient vectors must have positive conditional variance;
# verifying finitely many particular vectors does not prove that statement.
for a,b in [(1,0),(0,1),(1,-2),(2,3),(-3,4)]:
    x2=s.factor(sum(comb(2,j)*a**(2-j)*b**j*mm(2-j,j,0) for j in range(3)))
    x4=s.factor(sum(comb(4,j)*a**(4-j)*b**j*mm(4-j,j,0) for j in range(5)))
    kval=s.factor(x4-3*x2**2)
    assert kval>0,(a,b,kval)
    checks+=1

if __name__=='__main__':
    print('exact assertions:',checks)
    print('scalar variance:',m2)
    print('scalar fourth cumulant:',k4)
    print('scalar excess kurtosis:',excess)
    print('signed filter h(s)=exp(-s)-2 exp(-2s), r=D=1')
    print('variance:',z2,'fourth cumulant:',z_k4)
