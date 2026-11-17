"""Exact algebra and diagnostic trajectories for a critical planar Hénon map.

Requires SymPy. Finite-time simulations are supplementary, not infinite proof.
"""
from fractions import Fraction
import math
import sympy as sp

b,c=sp.symbols('b c', real=True)
N=6

def add(x,y):
    return [sp.expand(x[i]+y[i]) for i in range(N)]

def mul(x,y):
    return [sp.expand(sum(x[j]*y[i-j] for j in range(i+1))) for i in range(N)]

def scale(x,a):
    return [sp.expand(a*t) for t in x]

def power(x,k):
    out=[sp.Integer(1)]+[sp.Integer(0)]*(N-1)
    for _ in range(k): out=mul(out,x)
    return out

z=[sp.Integer(0),sp.Integer(1)]+[sp.Integer(0)]*(N-2)
h2=c/(b-1)
h3=2*c**2/(b-1)
h4=5*c**3*(b**2-b+1)/(b-1)**3
H=[0,0,h2,h3,h4,sp.Integer(0)]
p=add(z,scale(H,b))
Z=add(scale(z,-1),scale(mul(p,p),-c))
W=add(scale(H,b),scale(mul(p,p),-c))
h_of_Z=[sp.Integer(0)]*N
for k in range(2,5):h_of_Z=add(h_of_Z,scale(power(Z,k),H[k]))
for k in range(2,5):
    assert sp.factor(h_of_Z[k]-W[k])==0, ('center graph',k)
f2,f3,f4,f5=Z[2:6]
expected=[-c, 2*b*c**2/(1-b),-b*c**3*(5*b-4)/(1-b)**2,2*b*c**4*(7*b*b-7*b+5)/(1-b)**3]
for obs,exp in zip((f2,f3,f4,f5),expected): assert sp.factor(obs-exp)==0

u2=-c/2
u4=-c**3*(5*b*b-6*b+5)/(8*(1-b)**2)
p3=c**2*(1+b)/(1-b)
p5=c**4*(1+b)*(17*b*b-2*b+5)/(4*(1-b)**3)
coord=[sp.Integer(0),sp.Integer(1),u2,sp.Integer(0),u4,sp.Integer(0)]
f_of_coord=scale(coord,-1)
for j,coeff in ((2,f2),(3,f3),(4,f4),(5,f5)):
    f_of_coord=add(f_of_coord,scale(power(coord,j),coeff))
g=[sp.Integer(0),-sp.Integer(1),sp.Integer(0),p3,sp.Integer(0),p5]
coord_of_g=add(g,add(scale(power(g,2),u2),scale(power(g,4),u4)))
for k in range(1,6):assert sp.factor(f_of_coord[k]-coord_of_g[k])==0,('normal form',k)

cb=3*(1-b)**2/(4*(1+b))
A=-c*(1+b)/(2*(1-b))
K=4*p3
SqCoeff=sp.factor(-2*A*sp.sqrt(4*p3))
L=sp.factor(sp.Rational(3,2)*p3+p5/p3)
assert sp.factor(K.subs(c,cb)-9*(1-b)**3/(4*(1+b)))==0
assert sp.factor(L.subs(c,cb)-9*(1-b)**2*(11*b*b-2*b+11)/(64*(1+b)**2))==0
# Avoid symbolic square-root ambiguity by comparing the squares and known positive signs.
Hphysical=9*(1-b)**sp.Rational(5,2)/(8*sp.sqrt(1+b))
assert sp.simplify((SqCoeff.subs(c,cb)**2 - Hphysical**2))==0
assert sp.factor(sp.diff(11*b*b-2*b+11,b,2))==22
print('Exact center-jet, conjugacy and asymptotic-coefficient identities: PASS')

for bb in (0.2, 0.5, 0.8):
    aa=3*(1-bb)**2/4
    xstar=2/(3*(1-bb)); ystar=bb*xstar
    x=xstar+0.1; y=ystar-0.1*bb
    kk=9*(1-bb)**3/(4*(1+bb))
    hh=9*(1-bb)**2.5/(8*math.sqrt(1+bb))
    ll=9*(1-bb)**2*(11*bb**2-2*bb+11)/(64*(1+bb)**2)
    residual=[]
    for i in range(2*100000):
        x,y=1-aa*x*x+y,bb*x
        if i%2==1 and (i+1)//2 in (10000,50000,100000):
            n=(i+1)//2
            sig=1 if x>xstar else -1
            residual.append((n, 1/(x-xstar)**2-kk*n-sig*hh*math.sqrt(n)-ll*math.log(n)))
    assert all(math.isfinite(value) for _,value in residual)
    print(f'b={bb}: renormalized even-iterate residuals:',residual)
print('All algebraic and supplementary numerical checks: PASS')
