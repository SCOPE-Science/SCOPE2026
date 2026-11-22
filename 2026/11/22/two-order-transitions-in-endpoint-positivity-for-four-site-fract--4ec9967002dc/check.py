"""Supplementary numerical and symbolic spot checks for a four-node spectral heat identity.
Run with Python 3, sympy, and mpmath: python check.py.
The analytic proof, not these finite tests, establishes the statements for all parameters.
"""
import math
import sympy as sp
import mpmath as mp

L = sp.Matrix([[1,-1,0,0],[-1,2,-1,0],[0,-1,2,-1],[0,0,-1,1]])
r = sp.sqrt(2)
a, b, c = 2-r, sp.Integer(2), 2+r
q, p = 1+1/r, 1-1/r
assert L.charpoly().as_expr().factor() == sp.Symbol('lambda')*(sp.Symbol('lambda')-2)*(sp.Symbol('lambda')**2-4*sp.Symbol('lambda')+2)
for lam, coef in [(0, sp.Rational(1,4)), (a,-q/4), (b,sp.Rational(1,4)), (c,-p/4)]:
    proj=sp.eye(4)
    for other in [0,a,b,c]:
        if other != lam:
            proj=proj*(L-other*sp.eye(4))/(lam-other)
    assert sp.simplify(proj[0,3]-coef)==0
assert (L**2)[0,3]==0
assert (L**3)[0,3]==-1
assert (L**4)[0,3]==-6
D1=sp.simplify((b*sp.log(b)-q*a*sp.log(a)-p*c*sp.log(c))/4)
assert sp.simplify(sp.logcombine(sp.expand(D1-sp.log(2)/4), force=True))==0
D2=(b*b*sp.log(b)-q*a*a*sp.log(a)-p*c*c*sp.log(c))/4
mp.mp.dps=60
am=2-mp.sqrt(2); bm=mp.mpf(2); cm=2+mp.sqrt(2)
qm=1+1/mp.sqrt(2); pm=1-1/mp.sqrt(2)
def F(alpha,t):
    return (1+mp.exp(-(bm**alpha)*t)-qm*mp.exp(-(am**alpha)*t)-pm*mp.exp(-(cm**alpha)*t))/4

def crossings(alpha):
    A,B,C=am**alpha,bm**alpha,cm**alpha
    pts=[mp.mpf('1e-12')*(mp.mpf('1.05')**j) for j in range(780)]
    pts += [mp.mpf(j)/20 for j in range(1,401)]
    pts=sorted(set(pts))
    roots=[]
    for x,y in zip(pts,pts[1:]):
        if F(alpha,x)*F(alpha,y)<0:
            low,high=x,y
            for _ in range(150):
                mid=(low+high)/2
                if F(alpha,low)*F(alpha,mid)<=0: high=mid
                else:low=mid
            root=(low+high)/2
            if not roots or abs(root-roots[-1])>mp.mpf('1e-8'):roots.append(root)
    return roots

for alpha,expected in [('0.5',0),('1',0),('1.01',1),('1.1',1),('1.5',1),('1.75',1),('2',1),('2.01',2),('2.25',2),('2.5',2),('3',2),('4',2)]:
    roots=crossings(mp.mpf(alpha))
    assert len(roots)==expected, (alpha,roots)
    if expected:
        for root in roots:assert abs(F(mp.mpf(alpha),root))<mp.mpf('1e-45')

for eps in ['1e-4','1e-5','1e-6']:
    e=mp.mpf(eps)
    rr=crossings(1+e)[0]
    limit=mp.sqrt(mp.mpf(3)*mp.log(2)/2)
    assert abs(rr/mp.sqrt(e)/limit-1) < mp.mpf('0.08')
    rr2=crossings(2+e)[0]
    K=-mp.mpf(str(sp.N(D2,55)))/3
    assert abs(rr2/e/K-1)<mp.mpf('0.015')

# A fixed-time strict witness used in the theorem, including for high powers.
for alpha in [2,3,4,8,20]:
    assert F(mp.mpf(alpha),1/bm**alpha)<0
print('PASS: exact projectors, endpoint powers, phase patterns, and onset asymptotics')
