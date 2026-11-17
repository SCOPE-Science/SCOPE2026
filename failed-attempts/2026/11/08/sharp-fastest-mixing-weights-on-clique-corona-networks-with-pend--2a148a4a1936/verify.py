"""Symbolic and finite-matrix checks of a corona-graph mixing formula.

Requires Python 3, SymPy, NumPy. The accompanying proof, not finite sampling,
establishes the result for all integer parameters and all feasible matrices.
"""
import math
import random
import numpy as np
import sympy as sp

s, q, a, b = sp.symbols('s q a b', positive=True)
t = sp.sqrt(q) * (1+s)
T = 1+q*(1+s)**2
ast = s*(1+s)/T
bst = (s*s-1)*(1+q*(1+s))/T
rho = 1-s*s/T
v = sp.Matrix([1,t])
Mst=sp.Matrix([[-bst,sp.sqrt(q)*ast],[sp.sqrt(q)*ast,1-ast]])
assert all(sp.simplify(x)==0 for x in Mst*v-rho*v)
assert sp.factor((1-q*ast)/(1/(s*s-1))-bst)==0
bmax=(s*s-1)*(1-q*a)
Mmax=sp.Matrix([[-bmax,sp.sqrt(q)*a],[sp.sqrt(q)*a,1-a]])
assert sp.simplify((v.T*Mmax*v)[0]/(v.T*v)[0]-rho)==0
assert sp.simplify(1-q*ast-(1/(s*s-1))*bst)==0 # core holding is zero
mexpr=s*s/(s*s-1)
assert sp.simplify(ast-bst-(mexpr-1-q)*(1+s)/((mexpr-1)*T))==0


def build(m,q,a,b):
    """The actual stochastic matrix in core/leaf coordinate order."""
    n=m*(q+1)
    P=np.zeros((n,n))
    for i in range(m):
        c=i*(q+1)
        for j in range(m):
            if i!=j:
                P[c,j*(q+1)]=b
        for z in range(q):
            w=c+z+1
            P[c,w]=P[w,c]=a
            P[w,w]=1-a
        P[c,c]=1-q*a-(m-1)*b
    return P

rng=random.Random(17423)
tests=0
competitors=0
for m in range(2,9):
    for q0 in range(1,8):
        sigma=math.sqrt(m/(m-1))
        den=1+q0*(1+sigma)**2
        aopt=sigma*(1+sigma)/den
        bopt=(1-q0*aopt)/(m-1)
        opt=1-sigma**2/den
        P=build(m,q0,aopt,bopt)
        assert np.allclose(P,P.T,atol=1e-13)
        assert P.min()>=-1e-13
        assert np.max(np.abs(P.sum(axis=1)-1))<1e-13
        eig=np.linalg.eigvalsh(P)
        mu=max(abs(eig[:-1]))
        assert abs(eig[-1]-1)<2e-12
        assert abs(mu-opt)<3e-12,(m,q0,mu,opt)
        # Check 2x2 block matches the full graph's eigenvalues.
        transverse=np.array([[-bopt,math.sqrt(q0)*aopt],[math.sqrt(q0)*aopt,1-aopt]])
        eb=np.linalg.eigvalsh(transverse)
        assert abs(eb[-1]-opt)<2e-12
        tests+=1
        for j in range(6):
            ar=rng.random()/q0
            br=rng.random()*(1-q0*ar)/(m-1)
            C=build(m,q0,ar,br)
            ee=np.linalg.eigvalsh(C)
            value=max(abs(ee[:-1]))
            assert value>=opt-3e-12,(m,q0,ar,br,opt,value)
            competitors+=1
# At fixed q, m->infinity: gap -> 1/(1+4q); at fixed m, q->infinity:
# q times the gap -> (sqrt(m/(m-1))/(1+sqrt(m/(m-1))))**2.
for m in (2,3,5,19):
    for qq in (10**5,10**7):
        ss=math.sqrt(m/(m-1))
        gap=ss**2/(1+qq*(1+ss)**2)
        assert abs(qq*gap-(ss/(1+ss))**2)<1e-4
print('SYMBOLIC_IDENTITIES_OK')
print('FULL_GRAPH_CASES',tests)
print('RANDOM_FEASIBLE_COMPETITORS',competitors)
print('VERIFICATION_OK')
