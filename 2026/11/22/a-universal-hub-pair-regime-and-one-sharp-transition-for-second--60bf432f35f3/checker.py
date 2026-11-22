#!/usr/bin/env python3
"""Reproduce exact two-leader inverse-square coherence comparisons for weighted quadrilateral books.
Requires SymPy and NumPy. No network access or external data files are needed.
"""
import itertools
import sympy as sp
import numpy as np

m, t, h, u = sp.symbols('m t h u', positive=True)
Dpair = sp.Matrix([[1+t, -t], [-t, 1+t]])
# A pair (multiplicity, (retain_top, retain_bottom)) encodes leaf columns.
ORBIT = {
 'HH':((),[(m,(True,True))]),
 'HS':((1,),[(m-1,(True,True)),(1,(False,True))]),
 'HO':((1,),[(m-1,(True,True)),(1,(True,False))]),
 'LLs':((0,1),[(m-2,(True,True)),(2,(False,True))]),
 'LLc':((0,1),[(m-1,(True,True)),(1,(False,False))]),
 'LLd':((0,1),[(m-2,(True,True)),(1,(False,True)),(1,(True,False))]),
}

def schur_cost(hubs, columns):
    k=len(hubs)
    H=sp.Matrix(k,k,lambda i,j:(m+1 if i==j else -1)) if k else sp.zeros(0)
    M=[sp.zeros(k) for _ in range(3)]
    leaf_cost=sp.Integer(0)
    for count, status in columns:
        loc=[j for j in range(2) if status[j]]
        if not loc:continue
        inv=Dpair.extract(loc,loc).inv()
        B=sp.Matrix(len(loc),k,lambda i,j:int(loc[i]==hubs[j]))
        for r in range(3):M[r]+=count*(B.T*inv**(r+1)*B)
        leaf_cost+=count*sp.trace(inv**2)
    if not k:return sp.factor(leaf_cost)
    X=(H-M[0]).inv()
    return sp.factor(sp.trace(X**2)+2*sp.trace(X**2*M[1])+leaf_cost+
                     2*sp.trace(X*M[2])+sp.trace(X*M[1]*X*M[1]))

C={name:schur_cost(*shape) for name,shape in ORBIT.items()}
assert sp.simplify(C['HH']-2*m*(2*t*t+2*t+1)/(2*t+1)**2)==0
checks=0
# Denominators of each rational difference have positive factorizations for m>=2,t>0.
for name in ['HS','HO','LLs','LLc','LLd']:
    num,den=sp.fraction(sp.factor(C[name]-C['HH']))
    poly=sp.Poly(sp.expand(num.subs(m,h+3)),h,t)
    assert poly.terms() and all(c>0 for _,c in poly.terms()),name
    # Each factor of the denominator is manifestly positive in the relevant domain.
    assert all(c>=0 for c in sp.Poly(sp.expand(den),m,t).coeffs()),name
    checks+=len(poly.terms())

q=54*t**4+126*t**3+37*t**2-48*t-23
assert sp.simplify((C["LLd"]-C["HH"]).subs(m,2)+2*q/((2*t+1)**2*(4*t+3)**2))==0
assert q.subs(t,sp.Rational(3,5)) < 0 < q.subs(t,sp.Rational(7,10))
# Descending nonzero coefficient signs in q: + + + - -. Descartes gives a unique positive root.
assert [sp.sign(c) for c in sp.Poly(q,t).all_coeffs()]==[1,1,1,-1,-1]
for name in ['HS','LLs','LLc']:
    num,den=sp.fraction(sp.factor((C[name]-C['LLd']).subs(m,2)))
    assert all(c>0 for c in sp.Poly(sp.expand(num),t).coeffs()),name
    assert all(c>=0 for c in sp.Poly(sp.expand(den),t).coeffs()),name
    checks+=len(sp.Poly(sp.expand(num),t).terms())
# HO can be eliminated on the two overlapping parameter intervals.
Q, dQ=sp.fraction(sp.factor((C['HO']-C['HH']).subs(m,2)))
R, dR=sp.fraction(sp.factor((C['HO']-C['LLd']).subs(m,2)))
qpoly=sp.Poly(sp.cancel(Q.subs(t,sp.Rational(3,5)*u/(1+u))*(5*(1+u))**6),u)
assert all(c>0 for _,c in qpoly.terms())
rpoly=sp.Poly(sp.expand(R.subs(t,u+sp.Rational(3,5))),u)
assert all(c>0 for _,c in rpoly.terms())
assert all(c>=0 for c in sp.Poly(sp.expand(dQ),t).coeffs())
assert all(c>=0 for c in sp.Poly(sp.expand(dR),t).coeffs())
checks+=len(qpoly.terms())+len(rpoly.terms())

# Independently build the full weighted Laplacian and exhaustively enumerate all pairs.
def full_laplacian(M, T):
    N=2*M+2
    L=np.zeros((N,N))
    edges=[(0,1,1.)]
    for j in range(M):
        a,b=2+2*j,3+2*j
        edges.extend([(0,a,1.),(1,b,1.),(a,b,T)])
    for i,j,w in edges:
        L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
    return L

def cls(pair):
    a,b=pair
    if a<2 and b<2:return 'HH'
    if a<2 or b<2:
        hub,leaf=(a,b) if a<2 else (b,a)
        return 'HS' if hub==(leaf-2)%2 else 'HO'
    col1,col2=(a-2)//2,(b-2)//2
    if col1==col2:return 'LLc'
    return 'LLs' if a%2==b%2 else 'LLd'

for M in range(2,9):
    for T in (0.02,0.4,0.6,0.625,1.,4.,100.):
        L=full_laplacian(M,T)
        vals={}
        for pair in itertools.combinations(range(2*M+2),2):
            F=[i for i in range(2*M+2) if i not in pair]
            ev=np.linalg.eigvalsh(L[np.ix_(F,F)])
            assert ev[0]>0
            val=float(np.sum(ev**-2))
            name=cls(pair)
            expected=float(C[name].subs({m:M,t:T}))
            assert abs(val-expected)<2e-5*(1+expected),(M,T,pair,name,val,expected)
            vals[pair]=val
            checks+=1
        best=min(vals.values())
        tol=1e-7*(1+best)
        found={pair for pair,v in vals.items() if abs(v-best)<tol}
        if M>=3 or T<0.6:
            assert found=={(0,1)}
        elif T>0.7:
            assert found=={(2,5),(3,4)}

root=float(sp.nroots(q,maxsteps=100)[1]) if False else float([r for r in sp.nroots(q) if abs(sp.im(r))<1e-10 and sp.re(r)>0][0])
assert 0.6<root<0.7
print('PASS: exact symbolic certificates and independent full-matrix comparisons:',checks,'checks; threshold=',format(root,'.14f'))
