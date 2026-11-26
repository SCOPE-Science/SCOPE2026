"""Standalone exact-arithmetic checks for an RK4 graph-heat kernel on weighted stars.
Run: python verify.py (requires sympy >= 1.12).
"""
from fractions import Fraction
from itertools import product
import sympy as S

h=S.symbols('h',real=True)

def matrices(weights):
    weights=list(map(S.Rational,weights))
    n=len(weights)+1
    L=S.zeros(n)
    for i,w in enumerate(weights,1):
        L[0,0]+=w; L[i,i]+=w
        L[0,i]-=w; L[i,0]-=w
    P=S.eye(n)
    power=S.eye(n)
    for k in range(1,5):
        power=power*L
        P+=(-h)**k*power/S.factorial(k)
    return L,P

def polynomial_coefficients(weights):
    ws=list(map(S.Rational,weights))
    A=sum(ws); B=sum(w*w for w in ws); C=sum(w**3 for w in ws)
    def F(w):
        T=A+w
        U=A*A+B+A*w+w*w
        V=A**3+2*A*B+C+(A*A+B)*w+A*w*w+w**3
        return 1-T*h/2+U*h*h/6-V*h**3/24
    def G(u,v):
        W=A*A+B+A*(u+v)+u*u+u*v+v*v
        return S.Rational(1,2)-(A+u+v)*h/6+W*h*h/24
    return F,G

checks=0
# Independent symbolic direct matrix expansion, including non-equivalent weights.
u,v,w=S.symbols('u v w',positive=True)
L=S.Matrix([[u+v+w,-u,-v,-w],[-u,u,0,0],[-v,0,v,0],[-w,0,0,w]])
P=S.eye(4); Q=S.eye(4)
for k in range(1,5):
    Q=Q*L; P+=(-h)**k*Q/S.factorial(k)
A=u+v+w; B=u*u+v*v+w*w; C=u**3+v**3+w**3
for i,wi in enumerate([u,v,w],1):
    T=A+wi; U=A*A+B+A*wi+wi*wi
    V=A**3+2*A*B+C+(A*A+B)*wi+A*wi**2+wi**3
    expected=h*wi*(1-T*h/2+U*h*h/6-V*h**3/24)
    assert S.expand(P[0,i]-expected)==0
    checks+=1
for i,wi in enumerate([u,v,w],1):
    for j,wj in enumerate([u,v,w],1):
        if j<=i:continue
        W=A*A+B+A*(wi+wj)+wi*wi+wi*wj+wj*wj
        expected=h*h*wi*wj*(S.Rational(1,2)-(A+wi+wj)*h/6+W*h*h/24)
        assert S.expand(P[i,j]-expected)==0
        checks+=1
x,t,c=S.symbols('x t c',nonnegative=True)
P_d=S.expand(9*(1+x)*(1+2*t+c+(1+t)*x+x*x+x**3)-4*(1+t+x+x*x)**2)
P_cert=9*c*(1+x)-4*t**2+t*(x*x+19*x+10)+5*x**4+10*x**3+6*x*x+10*x+5
assert S.expand(P_d-P_cert)==0
checks+=1

for n in range(1,6):
    configs=list(product([S.Rational(1,2),S.Rational(1),S.Rational(3,2),S.Rational(3)],repeat=n))
    if n==5:configs=configs[::17]
    for ws in configs:
        LL,PP=matrices(ws)
        FF,GG=polynomial_coefficients(ws)
        for i in range(n):
            assert S.expand(PP[0,i+1]-h*ws[i]*FF(ws[i]))==0
            checks+=1
            for j in range(i+1,n):
                assert S.expand(PP[i+1,j+1]-h*h*ws[i]*ws[j]*GG(ws[i],ws[j]))==0
                checks+=1
        assert LL*S.ones(n+1,1)==S.zeros(n+1,1)
        assert PP*S.ones(n+1,1)==S.ones(n+1,1)
        checks+=2
        maxw=max(ws)
        root=float(S.nroots(FF(maxw),maxsteps=100)[0]) if False else None
        # Find the unique positive root from the cubic numerically; monotonic proof is analytic.
        cand=S.nroots(FF(maxw),maxsteps=100)
        roots=[float(S.re(z)) for z in cand if abs(float(S.im(z)))<1e-9 and float(S.re(z))>0]
        assert len(roots)==1
        threshold=roots[0]
        for scale in [S.Rational(1,4),S.Rational(3,4),S.Rational(5,4),S.Rational(2)]:
            hh=threshold*float(scale)
            vv=[float(S.N(PP[a,b].subs(h,hh),18)) for a in range(n+1) for b in range(n+1)]
            expected=scale<=1
            assert (min(vv)>=-1e-9)==expected, (ws,scale,min(vv),threshold)
            checks+=1
print('VERIFY_OK',checks,'symbolic polynomial and exact rational graph identities, numerical sign spotchecks')
