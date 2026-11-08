"""Exact and numerical reproducibility checks for complement-block sampling."""
from itertools import product
from math import sqrt
import numpy as np
import sympy as sp

checks=0
def check(condition,desc):
    global checks
    assert bool(condition), desc
    checks+=1

s=sp.symbols('s',positive=True)
c=s/sp.sqrt(1+s*s)
H=sp.Matrix([[1,c,c],[c,1,0],[c,0,1]])
Hi=sp.simplify(H.inv())
G=sp.Matrix(3,3,lambda i,j:sp.simplify(Hi[i,j]/sp.sqrt(Hi[i,i]*Hi[j,j])))
# A sign change of the center normal makes the inverse-Hessian Gram nonnegative.
D=sp.diag(-1,1,1)
Gpositive=sp.simplify(D*G*D).subs(sp.Abs(s*s-1),1-s*s)
reference=sp.Matrix([[1,s,s],[s,1,s*s],[s,s*s,1]])
for i,j in product(range(3),repeat=2):
    check(sp.simplify(Gpositive[i,j]-reference[i,j])==0,f'Gram {i},{j}')
r=sp.simplify(reference.inv()*sp.ones(3,1))
check(sp.simplify(r[0]-(1-s)/(1+s))==0,'r center')
for i in [1,2]:check(sp.simplify(r[i]-1/(1+s))==0,f'r leaf {i}')
S=sp.simplify(sum(r))
check(sp.simplify(S-(3-s)/(1+s))==0,'sum inverse rows')
q=sp.simplify(r/S)
check(sp.simplify(q[0]-(1-s)/(3-s))==0,'optimal center')
for i in [1,2]:check(sp.simplify(q[i]-1/(3-s))==0,'optimal leaf')
check(sp.simplify(1/S-(1+s)/(3-s))==0,'optimal risk')

# On concrete positive-definite rational star Hessians, verify exact equality
# between expected post-update energy and complement-vector projector Gram.
for c0 in [sp.Rational(1,5),sp.Rational(3,5),sp.Rational(2,3)]:
    A=sp.Matrix([[1,c0,c0],[c0,1,0],[c0,0,1]])
    K=A.inv(); check(A.det()>0,'SPD example')
    R=[]
    for omitted in range(3):
        idx=[i for i in range(3) if i!=omitted]
        E=sp.eye(3)[:,idx]
        T=sp.eye(3)-E*(E.T*A*E).inv()*E.T*A
        R.append(sp.simplify(T.T*A*T))
        ee=sp.eye(3)[:,omitted]
        # Exact energy-residual identity: rank one along A^{-1}e_j.
        expected=ee*ee.T/K[omitted,omitted]
        check(sp.simplify(R[-1]-expected)==sp.zeros(3),'rank-one residual identity')
    t=float(c0)/sqrt(1-float(c0)**2)
    for law in [[1/3]*3,[(1-t)/(3-t),1/(3-t),1/(3-t)],
                [(1+t*t)/(3+t*t),1/(3+t*t),1/(3+t*t)]]:
        B=np.array(sum([float(law[i])*R[i] for i in range(3)],sp.zeros(3))).astype(float)
        Aarr=np.array(A).astype(float)
        vals=np.linalg.eigvalsh(np.linalg.solve(np.linalg.cholesky(Aarr),np.eye(3))@B@np.linalg.solve(np.linalg.cholesky(Aarr),np.eye(3)).T)
        # Equivalent by generalized eigenvalues A^{-1/2} B A^{-1/2}.
        Gnum=np.array([[float(K[i,j]/sp.sqrt(K[i,i]*K[j,j])) for j in range(3)] for i in range(3)])
        qD=np.diag(np.sqrt(law))
        vg=np.linalg.eigvalsh(qD@Gnum@qD)
        check(abs(max(vals)-max(vg))<1e-11,'weighted Gram equivalence')
        if abs(law[1]-law[2])<1e-12 and abs(law[0]-(1-t)/(3-t))<1e-9:
            check(abs(max(vg)-(1+t)/(3-t))<1e-11,'optimal formula')

# Symmetry reduction, exact discriminant and stationary point identities.
p=sp.symbols('p',positive=True)
b=s*s
q0=1-2*p
Delta=sp.expand((q0-p*(1+b))**2+8*b*p*q0)
check(sp.expand(Delta-(1-(3+b)*p)**2-8*b*p*(1-2*p))==0,'radicand')
check(sp.factor(sp.diff(Delta,p)-2*(1-b)*((9-b)*p-3))==0,'radicand derivative')
check(sp.simplify((((9-b)*p-3)**2-Delta) / (p-1/(3-s)) / (p-1/(3+s)) - 8*(9-s*s))==0,'derivative threshold factor')
for t in [sp.Rational(1,4),sp.Rational(1,2),sp.Rational(3,4),sp.Rational(9,10)]:
    qstar=[(1-t)/(3-t),1/(3-t),1/(3-t)]
    qvol=[(1+t*t)/(3+t*t),1/(3+t*t),1/(3+t*t)]
    qunif=[sp.Rational(1,3)]*3
    GG=reference.subs(s,t)
    evals={}
    for name,law in [('star',qstar),('uniform',qunif),('volume',qvol)]:
        M=sp.diag(*[sp.sqrt(z) for z in law])*GG*sp.diag(*[sp.sqrt(z) for z in law])
        evals[name]=float(max([sp.re(e.evalf()) for e in M.eigenvals().keys()]))
    check(evals['star']<evals['uniform']<evals['volume'],f'strict chain t={t}')
    check(abs(evals['star']-float((1+t)/(3-t)))<1e-10,'closed form')
    lamvol=(1+t*t+sp.sqrt(2)*t*sp.sqrt(1+t*t))/(3+t*t)
    check(abs(evals['volume']-float(lamvol))<1e-10,'volume closed form')

# General Perron minimax formula tested on irreducible positive Gram matrices.
for eta in [sp.Rational(1,8),sp.Rational(1,3),sp.Rational(2,3)]:
    GG=sp.Matrix([[1,eta,eta],[eta,1,eta],[eta,eta,1]])
    rr=GG.inv()*sp.ones(3,1); ss=sum(rr); pp=rr/ss
    Mat=sp.diag(*[sp.sqrt(x) for x in pp])*GG*sp.diag(*[sp.sqrt(x) for x in pp])
    spec=[float(x) for x in Mat.eigenvals()]
    check(abs(max(spec)-float(1/ss))<1e-12,'Perron optimum')
    check(abs(sum(pp)-1)<1e-12,'probabilities sum 1')

print(f'PASS: {checks} exact/spectral checks; analytic argument establishes all-parameter inequalities.')
