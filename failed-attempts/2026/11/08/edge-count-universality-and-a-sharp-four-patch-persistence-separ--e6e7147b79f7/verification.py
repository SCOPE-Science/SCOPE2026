"""Exact, reproducible finite-contact-process extinction checks.

Requires Python 3.10+ and SymPy >= 1.12. Execute: python verification.py
"""
from fractions import Fraction
import sympy as sp

x=sp.Symbol('x')
STAR=[(0,1),(0,2),(0,3)]
PATH=[(0,1),(1,2),(2,3)]

def exact_time(edges):
    n=4
    M=sp.zeros(2**n-1)
    b=sp.ones(2**n-1,1)
    for S in range(1,2**n):
        j=S-1
        occupied=S.bit_count()
        total=sp.Integer(occupied)
        for v in range(n):
            if S>>v&1:
                R=S^(1<<v)
                if R: M[j,R-1]-=1
            else:
                neighbors=sum(1 for a,c in edges if (v==a and S>>c&1) or (v==c and S>>a&1))
                if neighbors:
                    total+=neighbors*x
                    M[j,(S|(1<<v))-1]-=neighbors*x
        M[j,j]=total
    return sp.factor(M.inv()[-1,:].dot(b))

def taylor(n,edges,order=2):
    nei=[0]*n
    for a,b in edges:
        nei[a]|=1<<b; nei[b]|=1<<a
    a=[[Fraction(0) for _ in range(1<<n)] for _ in range(order+1)]
    for j in range(order+1):
        for S in range(1,1<<n):
            k=S.bit_count()
            death=sum((a[j][S^(1<<v)] for v in range(n) if S>>v&1),Fraction(0))
            colon=Fraction(0)
            if j:
                colon=sum(((nei[v]&S).bit_count()*(a[j-1][S|1<<v]-a[j-1][S]) for v in range(n) if not (S>>v&1)),Fraction(0))
            a[j][S]=(Fraction(int(j==0),1)+death+colon)/k
    return [a[j][-1] for j in range(order+1)]

s=exact_time(STAR)
p=exact_time(PATH)
expected_s=(9*x**6+60*x**5+193*x**4+439*x**3+554*x**2+331*x+75)/(6*(x+1)*(3*x+2)*(4*x+3))
expected_p=(12*x**8+100*x**7+427*x**6+1280*x**5+2628*x**4+3527*x**3+2961*x**2+1424*x+300)/(2*(4*x**2+9*x+6)*(12*x**3+31*x**2+32*x+12))
assert sp.cancel(s-expected_s)==0
assert sp.cancel(p-expected_p)==0
numer=324*x**8+2595*x**7+8941*x**6+17676*x**5+22477*x**4+19319*x**3+11195*x**2+4032*x+684
assert sp.cancel((s-p)-x**2*numer/(6*(x+1)*(3*x+2)*(4*x+3)*(4*x**2+9*x+6)*(12*x**3+31*x**2+32*x+12)))==0
assert taylor(4,STAR)==[Fraction(25,12),Fraction(29,24),Fraction(11,16)]
assert taylor(4,PATH)==[Fraction(25,12),Fraction(29,24),Fraction(61,144)]
for n in range(4,8):
    ed=[(0,1)]
    c1=taylor(n,ed)[1]
    cm=taylor(n,[(0,1),(1,2)])[1]
    cd=taylor(n,[(0,1),(2,3)])[1]
    assert cm==cd==2*c1
for k in [sp.Rational(1,10),sp.Rational(1,2),sp.Integer(1),sp.Integer(2),sp.Integer(10)]:
    assert (s-p).subs(x,k)>0
print('PASS: two exact rational-time formulae, strictly positive all-rate numerator, independent Taylor coefficients, structural checks.')
print('At rate 1, star time =',s.subs(x,1),'path time =',p.subs(x,1),'difference =',(s-p).subs(x,1))
