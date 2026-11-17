from fractions import Fraction as F
from mpmath import mp
import sympy as S
A,X,Y,Z=S.symbols('A X Y Z', real=True)
x0=A+((1-A)*X-2*A*Y)*Z
x1=1-A+(A*Y-2*(1-A)*X)*Z
x2=(A*Y+(1-A)*X)*Z
u=(1-A)*X+A*Y
r=2*A*(1-A)
assert S.expand(x0+x1+x2-1).subs(Y,1-X-Z)==0
assert S.simplify(((1-A)*x0+A*x1-x2-r*(1-S.Rational(3,2)*Z*(1-Z))).subs(Y,1-X-Z))==0
assert S.simplify(x2-u*Z)==0
print('symbolic transition and barycentric identities PASS')

def iterate(a, ini, N):
    x0,x1,x2=map(mp.mpf,ini)
    out=[x2]
    for k in range(N):
        n0=a+((1-a)*x0-2*a*x1)*x2
        n1=1-a+(a*x1-2*(1-a)*x0)*x2
        n2=(a*x1+(1-a)*x0)*x2
        x0,x1,x2=n0,n1,n2
        out.append(x2)
    return out
mp.dps=500
initial=['0.4','0.1','0.5'];q=mp.mpf('0.2');c=mp.mpf('1.7')
for N in (3,4,5,6,7):
    r=c*q**(2**(N-1))
    a=(1-mp.sqrt(1-2*r))/2
    ss=iterate(a, initial,N+5)
    pred=1/c**2+1/c
    a0=ss[N]/(r/c)
    a1=ss[N+1]/(r*r)
    a2=ss[N+2]/(r*r*r)
    print('N=',N,'sN/(r/c)=',mp.nstr(a0,13),'sN+1/r2=',mp.nstr(a1,13),'sN+2/r3=',mp.nstr(a2,13),'limit=',mp.nstr(pred,13))
    if N>=5:
        assert abs(a0-1)<mp.mpf('0.01')
        assert abs(a1-pred)<mp.mpf('0.01')
        assert abs(a2-pred)<mp.mpf('0.01')
print('moving parameter checks PASS')
for a0 in (mp.mpf('0.1'),mp.mpf('0.3'),mp.mpf('0.7')):
    rr=2*a0*(1-a0)
    arr=iterate(a0,initial,120)
    assert abs(arr[-1]/arr[-2]/rr -1)<mp.mpf('1.e-15')
print('fixed positive mixing ratio checks PASS')
