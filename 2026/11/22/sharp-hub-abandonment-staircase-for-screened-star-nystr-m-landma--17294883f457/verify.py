"""Exact arithmetic checks for screened-star Nyström landmark theorem.
Run: python verify.py
Requires sympy; no network or external datasets.
"""
from fractions import Fraction
from itertools import combinations
import sympy as sp

x, m, k = sp.symbols('x m k', positive=True)
Z = x * (x+m+1) + k
EH = (m-k+1)/(x+1)
EL = (m-k)/(x+1) + ((x+1)**2 + m-k)/((x+1)*Z)
DELTA = (m+1-2*k-(m-1)*x)/((x+1)*Z)
assert sp.factor(EL-EH-DELTA) == 0
DH = (x+1)**(2-k)/(x*(x+m+1))
DL = Z/((x+1)**k*x*(x+m+1))
assert sp.factor(DH/DL - (x+1)**2/Z) == 0
# Identity relating trace reduction and logarithmic principal determinant.
assert sp.factor(-sp.diff(sp.log(DH/DL),x)-DELTA) == 0

checks=3
shifts=(sp.Rational(1,10),sp.Rational(1,3),sp.Rational(1,2),sp.Rational(3,4),sp.Integer(1),sp.Integer(2),sp.Integer(5))
for leaves in range(2,13):
    n=leaves+1
    L=sp.zeros(n,n)
    for j in range(1,n):
        L[0,0]+=1; L[j,j]+=1; L[0,j]=L[j,0]=-1
    for mu in shifts:
        A=mu*sp.eye(n)+L
        G=A.inv()
        for budget in range(1,n):
            hub_set=[0]+list(range(1,budget))
            leaf_set=list(range(1,budget+1))
            vals=[]
            for S in (hub_set,leaf_set):
                W=G.extract(S,S)
                Gs=G[:,S]
                N=G-Gs*W.inv()*Gs.T
                val=sp.trace(N)
                det=W.det()
                vals.append((val,det))
            assert vals[0][0]==EH.subs({x:mu,m:leaves,k:budget})
            assert vals[1][0]==EL.subs({x:mu,m:leaves,k:budget})
            assert vals[0][1]==DH.subs({x:mu,m:leaves,k:budget})
            assert vals[1][1]==DL.subs({x:mu,m:leaves,k:budget})
            assert sp.sign(vals[1][0]-vals[0][0])==sp.sign(DELTA.subs({x:mu,m:leaves,k:budget}))
            assert vals[1][1]>vals[0][1]
            checks+=6

# All subsets for small stars: symmetry-class values and precise counts.
for leaves in range(2,9):
    n=leaves+1
    L=sp.zeros(n,n)
    for j in range(1,n):
        L[0,0]+=1;L[j,j]+=1;L[0,j]=L[j,0]=-1
    for mu in (sp.Rational(1,5),sp.Rational(1,2),sp.Integer(1)):
        A=mu*sp.eye(n)+L
        G=A.inv()
        for budget in range(1,n):
            errors=[]; dets=[]
            for S in combinations(range(n),budget):
                W=G.extract(S,S); C=G[:,list(S)]
                # verify with principal complement inverse rather than full matrix product
                U=[j for j in range(n) if j not in S]
                err=sp.trace(A.extract(U,U).inv())
                errors.append((err,S)); dets.append((W.det(),S))
            optimum=min(v for v,_ in errors)
            predicted=min(EH.subs({x:mu,m:leaves,k:budget}), EL.subs({x:mu,m:leaves,k:budget}))
            assert optimum==predicted
            pred_d=DL.subs({x:mu,m:leaves,k:budget})
            assert max(v for v,_ in dets)==pred_d
            optsets={S for v,S in errors if v==optimum}
            want={(tuple(S)) for S in combinations(range(1,n),budget)} if predicted==EL.subs({x:mu,m:leaves,k:budget}) else set()
            if predicted==EH.subs({x:mu,m:leaves,k:budget}):
                want|={tuple((0,)+S) for S in combinations(range(1,n),budget-1)}
            assert optsets==want
            checks+=3

# Check one nonsubsumed nonnesting interval, as well as the growing near-full-budget ratio.
leaves=10;mu=sp.Rational(1,2)
assert DELTA.subs({x:mu,m:leaves,k:3})>0
assert DELTA.subs({x:mu,m:leaves,k:4})<0
for leaves in (10,20,40,100,400):
    mu=sp.Rational(1,2);budget=leaves
    ratio=sp.factor(EH.subs({x:mu,m:leaves,k:budget})/EL.subs({x:mu,m:leaves,k:budget}))
    assert ratio==(mu+leaves)/(mu+1)
    checks+=1
print('PASS:',checks,'exact symbolic, subset, and matrix assertions')
