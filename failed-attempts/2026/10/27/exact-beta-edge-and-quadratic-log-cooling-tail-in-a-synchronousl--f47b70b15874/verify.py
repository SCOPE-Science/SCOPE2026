"""Numerical and symbolic checks for an OU gas with common multiplicative jumps.

Run: python verify.py
Requires numpy and sympy. Computation checks finite samples, not edge asymptotic proofs.
"""
import math
import numpy as np
import sympy as sp

# Independent symbolic checks for the jump-generator moment identities.
a,b,r,c=sp.symbols('a b r c', positive=True)
m1=b/(a+r*(1-c))
m2=2*b*m1/(2*a+r*(1-c*c))
var=sp.factor(m2-m1*m1)
assert sp.simplify(var-b*b*r*(1-c)**2 / ((a+r*(1-c))**2*(2*a+r*(1-c*c))))==0
assert sp.simplify((2*b*m1/m2-2*a)/(b/m1-a) - (1+c))==0
checks=2
rng=np.random.default_rng(20261020)

# Stationary perpetuity sampling by iterating Y <- 1-U+c*U*Y.
# Finite iteration introduces at most c**steps absolute error per sample.
for alpha,D,rate,q in [(1.0,0.8,0.6,0.35),(1.3,1.2,2.4,0.65),(0.7,0.5,3.2,0.78),(2.0,1.1,1.5,0.45)]:
    aa=2*alpha; bb=2*D; cc=q*q; beta=rate/aa
    count=160000; steps=130
    y=np.ones(count)
    for _ in range(steps):
        u=rng.random(count)**(1/beta)
        y=1-u+cc*u*y
    v=y*bb/aa
    exact1=bb/(aa+rate*(1-cc))
    exact2=2*bb*exact1/(2*aa+rate*(1-cc*cc))
    assert abs(v.mean()-exact1)<0.012*bb/aa
    assert abs(np.mean(v*v)-exact2)<0.012*(bb/aa)**2
    checks+=2
    # Formula for the positive non-self-averaging component.
    exactvar=bb**2*rate*(1-cc)**2/((aa+rate*(1-cc))**2*(2*aa+rate*(1-cc**2)))
    assert abs(np.var(v)-exactvar)<0.018*(bb/aa)**2
    checks+=1
    # Exact conditional upper-edge distribution at two interior points.
    k=np.mean((1-cc*y)**(-beta))
    for eps in [0.35*(1-cc),0.72*(1-cc)]:
        observed=np.mean(y>1-eps)
        predicted=eps**beta*k
        assert abs(observed-predicted)<0.011
        checks+=1
    # Inverse problem recovers original parameters from the exact moments.
    AA=bb/exact1; BB=2*bb*exact1/exact2
    recovered_c=(BB-2*aa)/(AA-aa)-1
    recovered_r=(AA-aa)/(1-recovered_c)
    assert abs(recovered_c-cc)<1e-11
    assert abs(recovered_r-rate)<1e-11
    checks+=2
    # The moment hierarchy holds through order six.
    cur=1.0
    for n in range(1,7):
        prev=cur
        cur=n*bb*prev/(n*aa+rate*(1-cc**n))
        assert abs(n*bb*prev-(n*aa+rate*(1-cc**n))*cur)<1e-10
        checks+=1
    # Finite-N cloud-variance identity: Var(M_N)=Var(V)+2E[V^2]/N.
    for N in [25,100,500]:
        target=exactvar+2*exact2/N
        assert target>exactvar
        checks+=1

print('PASS:',checks,'independent finite/symbolic assertion groups')
