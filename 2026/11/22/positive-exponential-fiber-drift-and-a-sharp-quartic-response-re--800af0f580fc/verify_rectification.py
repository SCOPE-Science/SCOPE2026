"""Reproducible algebraic and numerical checks for exponential Duffing fiber drift.

Run: python3 verify_rectification.py.  Only the Python standard library is used.
Finite numerical checks supplement, but do not establish, the analytic theorem.
"""
from fractions import Fraction as Q
from math import pi, cos, exp


def add(a,b):return (a[0]+b[0], a[1]+b[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def inv(a):
    d=a[0]*a[0]+a[1]*a[1]
    return (a[0]/d,-a[1]/d)
def scale(a,s):return (s*a[0],s*a[1])
Z=(Q(0),Q(0))
def prod(p,q):
    out={}
    for j,a in p.items():
        for k,b in q.items():out[j+k]=add(out.get(j+k,Z),mul(a,b))
    return out

def algebraic_case(kappa,delta,B,omega,alpha,beta):
    vals=[Q(x) for x in (kappa,delta,B,omega,alpha,beta)]
    k,d,b,w,A,bet=vals
    D=(k-w*w)**2+d*d*w*w
    H=inv((k-w*w,d*w))
    u={1:scale(H,Q(1,2)),-1:scale((H[0],-H[1]),Q(1,2))}
    u2=prod(u,u);u3=prod(u2,u);u4=prod(u2,u2)
    v={n:scale(mul(coeff,inv((k-n*n*w*w,d*n*w))),-b) for n,coeff in u3.items()}
    uv=prod(u,v)
    assert u2[0][1]==u4[0][1]==uv[0][1]==0
    q2=A*bet*u2[0][0]
    q4=2*A*bet*uv[0][0]+A*bet**3*Q(1,6)*u4[0][0]
    predicted2=A*bet/(2*D)
    predicted4=A*bet/D**3*(bet**2*D/Q(16)-Q(3,4)*b*(k-w*w))
    assert q2==predicted2 and q4==predicted4
    return q2,q4

cases=[(Q(2),Q(1,2),Q(1),Q(1),Q(1),Q(1)),
       (Q(2),Q(1,2),Q(1),Q(1),Q(1),Q(4)),
       (Q(1),Q(1,2),Q(1,10),Q(1),Q(1),Q(1)),
       (Q(1,2),Q(3,5),Q(1),Q(1),Q(2),Q(1))]
for params in cases:
    q2,q4=algebraic_case(*params)
    print('EXACT',tuple(map(str,params)),'q2=',q2,'q4=',q4)
assert algebraic_case(*cases[0])[1]<0<algebraic_case(*cases[1])[1]

# Explicit RK4 quadrature of the local attracting base cycle and z increment.
def numeric_case(beta,epsilon):
    delta=0.5;kappa=2.0;B=1.0;omega=1.0;alpha=1.0
    T=2*pi/omega; N=4096; h=T/N
    def F(t,s):
        x,y,z=s
        return (y,-delta*y-kappa*x-B*x**3+epsilon*cos(omega*t),alpha*x*exp(beta*x))
    def step(t,s):
        k1=F(t,s)
        k2=F(t+h/2,tuple(s[i]+h*k1[i]/2 for i in range(3)))
        k3=F(t+h/2,tuple(s[i]+h*k2[i]/2 for i in range(3)))
        k4=F(t+h,tuple(s[i]+h*k3[i] for i in range(3)))
        return tuple(s[i]+h*(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6 for i in range(3))
    s=(0.0,0.0,0.0)
    for period in range(30):
        begin=s; halfway=None
        for j in range(N):
            s=step((period*N+j)*h,s)
            if j+1==N//2:halfway=s
    drift=(s[2]-begin[2])/T
    anti=max(abs(begin[i]+halfway[i]) for i in (0,1))
    D=(kappa-omega**2)**2+(delta*omega)**2
    q2=alpha*beta/(2*D)
    q4=alpha*beta/D**3*(beta*beta*D/16-3*B*(kappa-omega**2)/4)
    scaled=(drift-q2*epsilon**2)/epsilon**4
    assert drift>0 and anti<1e-6
    assert abs(scaled-q4)<0.045
    return drift,scaled,q4,anti
for beta in (1.0,4.0):
    for eps in (0.08,0.04):
        d,r,p,a=numeric_case(beta,eps)
        print('NUMERIC beta=',beta,'eps=',eps,'drift=',format(d,'.12g'),
              'quartic estimate=',format(r,'.9g'),'exact=',format(p,'.9g'),
              'antiperiod residual=',format(a,'.4g'))
print('VERIFY_OK')
