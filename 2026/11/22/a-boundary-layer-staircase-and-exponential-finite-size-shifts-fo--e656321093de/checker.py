"""Independent finite arithmetic and high-precision checks of path Green landmark theorem.
Run: python checker.py  (requires SymPy and mpmath). No data files required.
"""
from fractions import Fraction
from math import exp, log
import sympy as sp
import mpmath as mp

assertions=0
for n in range(2,13):
    L=sp.zeros(n)
    for i in range(n-1):
        L[i,i]+=1; L[i+1,i+1]+=1
        L[i,i+1]-=1; L[i+1,i]-=1
    for qq in (sp.Rational(1,5),sp.Rational(1,2),sp.Rational(2,3),sp.Rational(9,10)):
        mu=(1-qq)**2/qq
        G=(L+mu*sp.eye(n)).inv()
        common=qq/((1-qq**2)*(1-qq**(2*n)))
        f=lambda a:a*qq**a/(1+qq**a)
        F=[]; captures=[]
        for j in range(n):
            aa=2*j+1;bb=2*n-2*j-1
            formula=common*(1+qq**aa)*(1+qq**bb)
            assert G[j,j]==formula, (n,qq,j,'diag')
            assertions+=1
            cap=(G*G)[j,j]/G[j,j]
            captures.append(cap)
            F.append(f(aa)+f(bb))
        for j in range(n):
            for h in range(j+1,n):
                sign=sp.sign(captures[j]-captures[h]);sgn2=sp.sign(F[j]-F[h]);assert sign==sgn2,(n,qq,j,h,sign,sgn2)
                assertions+=1
        assert max(captures)==captures[max(range(n),key=lambda j:F[j])]
        assertions+=1

for a in range(1,102,2):
    p=lambda q:a-(a+2)*q*q-2*q**(a+2)
    assert p(sp.Rational(1,100))>0 and p(1)<0
    assertions+=1

mp.mp.dps=65
c=1+mp.lambertw(1/mp.e)
roots=[]
for a in range(1,100,2):
    p=lambda q:a-(a+2)*q*q-2*q**(a+2)
    q=mp.findroot(p, (mp.mpf('.2'),mp.mpf('.9999')))
    assert 0<q<1
    assert not roots or q>roots[-1]
    b=-mp.log(q)
    assert c/(a+2)<b<c/a
    roots.append(q)
    assertions+=4
assert abs(roots[0]-mp.mpf('.5'))<mp.mpf('1e-60');assertions+=1

# At the half-line threshold beta_0=log 2, verify the leading finite-size shift.
b=mp.log(2)
fn=lambda a,B:mp.mpf(a)/(1+mp.exp(a*B))
for n in (8,10,12,14,16,20,24):
    z=2*n-1
    diff=lambda B:fn(1,B)+fn(z,B)-fn(3,B)-fn(z-2,B)
    zz=mp.findroot(diff,(b+mp.mpf('1e-13'),b+mp.mpf('.05')))
    mu_n=2*(mp.cosh(zz)-1)
    asym=mp.mpf(27)*z*2**(-z)/4
    assert mu_n>mp.mpf('.5')
    assert 0<(mu_n-mp.mpf('.5'))/asym<2
    assertions+=2

print('PASS:',assertions,'exact symbolic/rational and high-precision assertions')
print('first 4 beta / mu thresholds:')
for i in range(4):
    q=roots[i];print(2*i+1,mp.nstr(-mp.log(q),16),mp.nstr(q+1/q-2,16))
print('c=1+W(exp(-1)):',mp.nstr(c,20))
