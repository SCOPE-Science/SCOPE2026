"""Exact checks for cycle Chebyshev covariance and the four-cycle cutoff transition.

Usage: python verify.py  (requires sympy >=1.12)
All critical continuum claims are proved analytically in RESULT.md;
this checks exact algebra, Sturm isolations, and independent finite enumeration.
"""
import itertools
import sympy as sp

r = sp.symbols('r', positive=True)
U = 1-2*r**2
R = -48*r**6-16*r**4+28*r**2-1
P = sp.Poly(sp.expand(R**2-48*r**4*U**2*(2+4*r**2)), r)
assert P.as_expr() == (2304*r**12 + 768*r**10 - 2048*r**8
                           -608*r**6 +720*r**4-56*r**2+1)
assert P.count_roots(0,1)==4
intervals=[(sp.Rational(164,1000),sp.Rational(165,1000)),
           (sp.Rational(237,1000),sp.Rational(238,1000)),
           (sp.Rational(751,1000),sp.Rational(752,1000)),
           (sp.Rational(809,1000),sp.Rational(810,1000))]
sgns=[]
for a,b in intervals:
    assert P.count_roots(a,b)==1
    RL=-48*b**6-16*b**4+28*a**2-1
    RH=-48*a**6-16*a**4+28*b**2-1
    UL=1-2*b**2; UH=1-2*a**2
    assert (RL>0 and RH>0) or (RL<0 and RH<0)
    assert (UL>0 and UH>0) or (UL<0 and UH<0)
    sgns.append((sp.sign(RL),sp.sign(UL)))
assert sgns==[(-1,1),(1,1),(1,-1),(-1,-1)]

def g1(x):return 1+x*sp.sqrt(3*(2+x*x))
def g2(x):return sp.sqrt(2+4*x*x)+sp.sqrt(3)*x*x
for a,b in [intervals[1],intervals[3]]:
    # Genuine cutoffs have opposite original objective ordering at their ends.
    assert (g2(a)-g1(a) > 0) != (g2(b)-g1(b)>0)
assert g2(sp.Rational(1,100))-g1(sp.Rational(1,100))>0
assert g2(sp.Rational(1,2))-g1(sp.Rational(1,2))<0
assert g2(sp.Rational(99,100))-g1(sp.Rational(99,100))>0

# The following finite computations cross-check the general covariance identity.
for n in range(3,9):
    S=sp.zeros(n,n)
    for i in range(n): S[i,(i+1)%n]=1
    A=(S+S.T)/2
    Tk=[sp.eye(n),A]
    for k in range(2,n):Tk.append(sp.expand(2*A*Tk[-1]-Tk[-2]))
    for k in range(n):
        assert Tk[k]==(S**k+(S.T)**k)/2
    # Compare the covariance to its Rademacher fourth-moment calculation.
    def cov(M,N):
        return 2*sum(M[i,j]*N[i,j] for i in range(n) for j in range(n) if i!=j)
    half=(n-1)//2
    for j in range(1,n):
        for k in range(1,n):
            expected=(2*n if n%2==0 and j==k==n//2 else
                      n if (j==k or j+k==n) else 0)
            assert cov(Tk[j],Tk[k])==expected
    # Independent enumeration of sign-vector quadratic-form variance.
    if n<=7:
        for k in [1,n-1]:
            M=Tk[k]
            out=[]
            for z in itertools.product((-1,1),repeat=n):
                v=sp.Matrix(z)
                out.append((v.T*M*v)[0])
            mean=sum(out)/len(out)
            variance=sum((t-mean)**2 for t in out)/len(out)
            assert variance==cov(M,M)

# Four-cycle exact variance and continuous-work expressions.
x=sp.symbols('x', positive=True)
v1a=4*x**2;v2a=8*x**4+4*x**6
v1b=4*x**2+8*x**4;v2b=4*x**6
assert sp.simplify((sp.sqrt(v1a)+sp.sqrt(3*v2a)) - 2*x*g1(x))==0
assert sp.simplify((sp.sqrt(2*v1b)+sp.sqrt(3*v2b)) - 2*x*g2(x))==0
# Existence and sharpness of both transitions in the open interval.
roots=sorted(float(sp.re(z)) for z in sp.nroots(P.as_expr(),n=30,maxsteps=200)
             if abs(float(sp.im(z)))<1e-20 and 0<float(sp.re(z))<1)
assert len(roots)==4
assert abs(roots[1]-0.23718071382399833)<1e-12
assert abs(roots[3]-0.8095480401540004)<1e-12
print('PASS: 4 Sturm-isolated polynomial roots, exactly 2 admissible cutoffs')
print('cutoff transition roots:',roots[1],roots[3])
print('PASS: exact cycle covariance in n=3,...,8 and independent enumeration in n<=7')
