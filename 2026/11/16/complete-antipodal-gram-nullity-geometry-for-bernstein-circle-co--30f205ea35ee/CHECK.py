"""Independent finite symbolic checks for the Bernstein-circle Gram-nullity theorem.

Requires SymPy.  The universal statements are proved analytically in RESULT.md;
finite tests here detect mistakes in constants, parity, and boundary cases.
"""
from math import comb, cos, pi
import sympy as s

t=s.symbols('t',real=True)
checks=0

def Q(n,m):
    return s.expand(sum(s.binomial(n,j)*t**j*(1-t)**(n-j)*s.cos(s.pi*m*j/n) for j in range(n+1)))

def cosine_coefficient(P,k):
    ans=s.Integer(0)
    for r in range(1,s.degree(P,t)+1,2):
        term=(((-1)**k)*s.diff(P,t,r).subs(t,1)-s.diff(P,t,r).subs(t,0))
        ans+=2*((-1)**((r-1)//2))*term/(s.pi*k)**(r+1)
    return s.simplify(ans)

for n in range(1,7):
    for m in range(1,2*n+1):
        P=Q(n,m)
        assert s.simplify(P.subs(t,0)-1)==0
        assert s.simplify(P.subs(t,1)-(-1)**m)==0
        assert s.simplify(P.subs(t,1-t)-(-1)**m*P)==0
        checks+=3
        assert s.simplify(s.diff(P,t).subs(t,0)-n*(s.cos(s.pi*m/n)-1))==0
        checks+=1
        for k in range(1,21):
            a=cosine_coefficient(P,k)
            if (m+k)%2 or m%(2*n)==0:
                assert s.simplify(a)==0,(n,m,k,a)
            else:
                assert float(s.N(a,35))>=-1e-28,(n,m,k,a)
            checks+=1
        for parity in (0,1):
            k=10000+parity
            a=cosine_coefficient(P,k)
            lim=4*n*(1-s.cos(s.pi*m/n))/s.pi**2 if m%2==parity else 0
            assert abs(float(s.N(k*k*a-lim,30)))<1e-4,(n,m,k)
            checks+=1

# Exact Gram-nullspace checks for examples.
points=[s.Integer(0),s.pi/2,s.pi,3*s.pi/2]
def gram(P):
    entries=[]
    for a in points:
        row=[]
        for b in points:
            d=s.Min(s.Abs(a-b),2*s.pi-s.Abs(a-b))
            row.append(s.simplify(P.subs(t,d/s.pi)))
        entries.append(row)
    return s.Matrix(entries)

Pboth=Q(2,1)+Q(2,2)
Podd=s.Integer(1)+Q(2,1)
Peven=Q(2,2)
assert gram(Pboth).rank()==4
assert gram(Podd).rank()==3
assert gram(Peven).rank()==2
checks+=3
v=s.Matrix([1,-1,1,-1]) # sorted points [0,pi/2,pi,3pi/2], pair differences
assert gram(Podd)*v==s.zeros(4,1)
checks+=1
# Four-point zero mode under one odd harmonic and a positive constant:
w=s.Matrix([1,-1,1,-1]); assert gram(Podd)*w==s.zeros(4,1)
checks+=1
# Exact spectral eigenvalue at two antipodal pairs with separation pi/2.
lam=s.symbols('lam', positive=True)
Gt=gram(Podd+lam*Peven)
assert s.simplify(Gt*w-2*lam*w)==s.zeros(4,1)
checks+=1
# Formula for 2 finite-atom polynomial features: rank loss at 2 antipodal pairs only.
assert gram(Q(2,1)).rank()==2
checks+=1
print('PASS',checks,'exact finite checks')
# General four-node antipodal geometry at degree 2, all rational separations.
u=s.symbols('u',real=True,positive=True)
D=1-2*u
Q0=2+lam
Qpi=lam
Qnear=2-2*u+lam*D**2
Qfar=2*u+lam*D**2
GG=s.Matrix([[Q0,Qpi,Qnear,Qfar],[Qpi,Q0,Qfar,Qnear],
             [Qnear,Qfar,Q0,Qpi],[Qfar,Qnear,Qpi,Q0]])
eigs=[(s.Matrix([1,1,1,1]),4+2*lam*(1+D**2)),
      (s.Matrix([1,1,-1,-1]),2*lam*(1-D**2)),
      (s.Matrix([1,-1,1,-1]),4*(1-u)),
      (s.Matrix([1,-1,-1,1]),4*u)]
for vec,eig in eigs:
    assert all(s.simplify(v)==0 for v in GG*vec-eig*vec)
    checks+=1
for v0 in (s.Rational(1,7),s.Rational(1,4),s.Rational(1,2),s.Rational(3,4),s.Rational(6,7)):
    for ell in (s.Rational(1,10),s.Rational(1,2),s.Integer(1),s.Integer(3),s.Integer(5)):
        actual=sorted(float(s.N(x,20)) for x in GG.subs({u:v0,lam:ell}).eigenvals().keys())
        predicted=sorted(float(s.N(eig.subs({u:v0,lam:ell}),20)) for _,eig in eigs)
        assert len(actual)==len(set(predicted)) or len(actual)==len(set(actual))
        assert set(round(x,10) for x in actual)==set(round(x,10) for x in predicted)
        checks+=1
print('PASS',checks,'including complete symbolic four-site spectrum')
