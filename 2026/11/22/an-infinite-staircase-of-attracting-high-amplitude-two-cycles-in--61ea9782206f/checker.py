"""Standalone diagnostic checks for the antipodal period-two staircase.
The complete infinite-orbit claims rest on the proof, not these finite tests.
Requires Python 3, numpy, scipy, sympy.
"""
import math
import numpy as np
import sympy as sp
from scipy.optimize import brentq

x,y,z,p,a,g=sp.symbols('x y z p a g',real=True)
F=sp.Matrix([y,sp.sin(z),p*x+a*y-g*sp.sin(z)])
J=F.jacobian([x,y,z])
q=sp.symbols('q')
assert sp.simplify(J.det()-p*sp.cos(z))==0
print('symbolic det J =',sp.factor(J.det()))
assert sp.simplify(J.charpoly(q).as_expr()-(q**3+g*sp.cos(z)*q**2-a*sp.cos(z)*q-p*sp.cos(z)))==0
# Fixed A=a-g and B=a+g on p=0. Check antipodal period-2 identities.
B,d,A=sp.symbols('B d A',real=True)
sub={p:0,a:(B+A)/2,g:(B-A)/2}
P=sp.Matrix([sp.sin(d),-sp.sin(d),d]); Q=-P
FP=sp.simplify(F.subs({x:P[0],y:P[1],z:P[2]}).subs(sub))
assert sp.simplify((FP-Q).subs(B,d/sp.sin(d)))==sp.zeros(3,1)
Jd=J.subs({z:d,p:0}).subs(sub)
assert sp.factor(Jd.charpoly(q).as_expr())==sp.factor(q*(q*q+(B-A)*sp.cos(d)*q/2-(B+A)*sp.cos(d)/2))
assert sp.simplify((Jd.subs(d,-d)-Jd))==sp.zeros(3,3)
print('symbolic orbit and characteristic polynomial: PASS')

def thresholds(A,k):
    m=(2*k+0.5)*math.pi
    q=0 if k==0 else brentq(lambda t:t/math.tan(t)-1,2*k*math.pi+1e-6,m-1e-6)
    r=brentq(lambda t:t/math.tan(t)+A*math.cos(t)+2,m+1e-6,(2*k+1)*math.pi-1e-6)
    return (q/(math.sin(q)) if k else 1),r/math.sin(r),q,r

def Fnum(v,a,g,p=0):
    x,y,z=v
    return np.array([y,math.sin(z),p*x+a*y-g*math.sin(z)])

def check(A,k):
    lo,hi,q,r=thresholds(A,k)
    B=(lo+hi)/2; a=(B+A)/2;g=(B-A)/2
    d=brentq(lambda v:v/math.sin(v)-B, max(2*k*math.pi+1e-8,q+1e-7), (2*k+1)*math.pi-1e-6)
    P=np.array([math.sin(d),-math.sin(d),d]);Q=-P
    assert np.linalg.norm(Fnum(P,a,g)-Q)<1e-11
    assert np.linalg.norm(Fnum(Q,a,g)-P)<1e-11
    jac=np.array([[0,1,0],[0,0,math.cos(d)],[0,a,-g*math.cos(d)]])
    assert max(abs(np.linalg.eigvals(jac)))<1
    # Branch to left of fold, when present, has B cos(d)>1.
    if k>=1:
        dleft=brentq(lambda v:v/math.sin(v)-B,2*k*math.pi+1e-7,q-1e-7)
        assert B*math.cos(dleft)>1
    # Above upper threshold the right solution has |a cos(d)|>1.
    Bout=hi+min(.1, (2*k+1)*math.pi/10)
    dend=brentq(lambda v:v/math.sin(v)-Bout,r+1e-7,(2*k+1)*math.pi-1e-7)
    assert ((Bout+A)/2)*math.cos(dend)<-1
    return lo,hi

for A in (-.75,0,.75):
    ws=[]
    for k in range(1,31):
        lo,hi=check(A,k);ws.append((k,lo,hi,hi-lo))
    for k in (0,1,2,5,10):check(A,k)
    assert all(ws[i][2]<ws[i+1][1] for i in range(len(ws)-1))
    for k,lo,hi,w in ws[-5:]:
        m=(2*k+.5)*math.pi
        assert abs(m*w-4.5)<.05
    print('A=',A,'windows for k=1,2,10,30:',[tuple(round(v,6) for v in ws[i][1:]) for i in (0,1,9,29)])
print('all finite diagnostics PASS')
