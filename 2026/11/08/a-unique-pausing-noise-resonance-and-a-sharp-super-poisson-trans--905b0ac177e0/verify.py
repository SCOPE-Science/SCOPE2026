"""Exact two-site paused-exclusion count statistics and sign certificates.
Run: python verify.py   (requires SymPy and NumPy).
The analytical statements follow from rational polynomial identities and Descartes' rule.
"""
from itertools import product
import sympy as S
import numpy as np

p, q = S.symbols('p q', positive=True)
labels = tuple(product(range(3), repeat=2))  # 0=vacant, 1=active, 2=paused
ix = {z:i for i,z in enumerate(labels)}
n = len(labels)
Q, C = S.zeros(n), S.zeros(n)

def transition(src,dst,rate,is_exit=False):
    i,j=ix[src],ix[dst]
    Q[j,i] += rate
    Q[i,i] -= rate
    if is_exit: C[j,i] += rate

for st in labels:
    x,y=st
    if x==0: transition(st,(1,y),1)
    if x==1 and y==0: transition(st,(0,1),1)
    if y==1: transition(st,(x,0),1,True)
    if x==1: transition(st,(2,y),p)
    if x==2: transition(st,(1,y),q)
    if y==1: transition(st,(x,2),p)
    if y==2: transition(st,(x,1),q)
assert Q.shape == (9,9) and all(S.simplify(z)==0 for z in Q.T*S.ones(n,1))

B=Q.copy(); B[-1,:]=S.ones(1,n)
normal=S.zeros(n,1); normal[-1]=1
pi=B.inv()*normal
current=S.factor((S.ones(1,n)*C*pi)[0])
rhs=current*pi-C*pi;rhs[-1]=0
h=B.inv()*rhs
fano=S.cancel(1+2*(S.ones(1,n)*C*h)[0]/current)
A,den=S.fraction(fano)
P=4*p**4+20*p**3*q+12*p**3+38*p**2*q**2+40*p**2*q+7*p**2+32*p*q**3+47*p*q**2+15*p*q+10*q**4+20*q**3+10*q**2
assert S.expand(den-P**2)==0
assert S.simplify(current-q*(p+2*q+2)*(2*p**2+4*p*q+p+2*q**2+2*q)/P)==0
assert all(z>0 for _,z in S.Poly(P,p,q).terms())
assert all(z>0 for _,z in S.Poly(A,p,q).terms())
assert S.simplify(fano.subs(p,0)-S.Rational(9,25))==0
assert S.limit(fano,p,S.oo)==S.Rational(1,2)
assert S.limit(p*(fano-S.Rational(1,2)),p,S.oo)==S.Rational(1,2)

# Exact rational derivative numerator for F. Denominator is positive for p,q>0.
Up=S.Poly(S.expand(S.diff(A,p)*den-A*S.diff(den,p)),p)
Uq=S.Poly(S.expand(S.diff(A,q)*den-A*S.diff(den,q)),p,q)
assert Up.degree()==14
assert all(z<0 for _,z in Uq.terms())
assert all(z<0 for _,z in S.Poly(S.expand(S.diff(S.fraction(current)[0],p)*S.fraction(current)[1]-S.fraction(current)[0]*S.diff(S.fraction(current)[1],p)),p,q).terms())

# In p order 0..14 the coefficient signs are +...+ -...-.
# For k=3..13 each coefficient has precisely one positive q-root; the
# rational isolators are strictly ordered from k=3 to k=13.
root_boxes = {
    3:(81,82),4:(332,333),5:(616,617),6:(881,882),
    7:(1114,1115),8:(1328,1329),9:(1545,1546),
    10:(1802,1803),11:(2167,2168),12:(2835,2836),
    13:(4761,4762),
}
for k in range(15):
    ck=S.Poly(Up.nth(k),q)
    if k<=2: assert all(c>0 for c in ck.all_coeffs() if c!=0)
    elif k==14: assert ck.as_expr()==-128
    else:
        # The polynomial in q has exactly one positive sign variation.
        seq=[S.sign(z) for z in ck.all_coeffs() if z!=0]
        assert sum(seq[i]!=seq[i+1] for i in range(len(seq)-1))==1
        lo,hi=root_boxes[k]
        assert ck.eval(S.Rational(lo,1000))<0
        assert ck.eval(S.Rational(hi,1000))>0
assert all(root_boxes[k][1]<root_boxes[k+1][0] for k in range(3,13))
assert S.simplify(S.diff(fano,p).subs(p,0)-2*(q**3+21*q**2+85*q+50)/(125*q**2*(q+1)**2))==0

# A 1-site controlled comparison, derived from its three-state tilted generator.
F1=(p**2+2*p*q+2*p+2*q**2)/(p+2*q)**2
assert S.simplify(S.diff(F1,p)-2*(p*q-p+2*q)/(p+2*q)**3)==0

# Super-Poisson transition bracket: below q=0.33645 at p=0.36467,
# F>1; above q=0.33646, den-A has no positive roots, and its
# value at p=0 is positive. Root counts use exact rational Sturm chains.
qlow=S.Rational(33645,100000);qhigh=S.Rational(33646,100000)
ptest=S.Rational(36467,100000)
assert fano.subs({p:ptest,q:qlow})>1
polynomial=S.Poly((den-A).subs(q,qhigh),p)
assert polynomial.count_roots(0,S.oo)==0 and polynomial.eval(0)>0

# Scaling limits: rare unpausing q->0, fast unpausing q->infinity.
t,z=S.symbols('t z',positive=True)
Fl=S.cancel(fano.subs(p,q*t))
low=S.factor(S.limit(q*Fl,q,0,dir='+'))
assert S.simplify(low-4*t*(9*t**2+30*t+20)/(7*t**2+15*t+10)**2)==0
assert S.simplify(S.diff(low,t)+4*(63*t**4+285*t**3+150*t**2-300*t-200)/(7*t**2+15*t+10)**3)==0
Fh=S.cancel(fano.subs({p:t/z**2,q:1/z}, simultaneous=True))
high=S.factor(S.limit((Fh-S.Rational(1,2))/z**2,z,0,dir='+'))
assert S.simplify(high-(t-2)/(2*t**2))==0
assert S.simplify(S.diff(high,t)+(t-4)/(2*t**3))==0

# Independent floating-point tilted-eigenvalue cross-check.
# The two derivatives of the dominant eigenvalue are evaluated by
# central differences, independent of the stationary Poisson solve.
Fnum=S.lambdify((p,q),fano,'numpy')
checks=0
for pv in (0.05,0.3,1.0,7.0):
    for qv in (0.08,0.34,1.0,5.0):
        G=np.array(Q.subs({p:pv,q:qv})).astype(float)
        E=np.array(C).astype(float)
        def root(s):
            H=G+(np.exp(s)-1)*E
            return max(np.linalg.eigvals(H).real)
        delta=0.0005
        k1=(root(delta)-root(-delta))/(2*delta)
        k2=(root(delta)+root(-delta)-2*root(0))/(delta*delta)
        assert abs(k2/k1-float(Fnum(pv,qv)))<4e-5, (pv,qv,k2/k1,float(Fnum(pv,qv)))
        checks+=1
print('PASS: exact 9-state tilted-generator identities, 11 ordered root certificates,')
print('      nonpositive current and Fano-q derivative coefficients, two scaling limits,')
print('      sharp super-Poisson threshold bracket and',checks,'independent spectral comparisons.')
