#!/usr/bin/env python3
"""Recompute the six-state antisymmetric characteristic polynomial exactly."""
import sympy as s

q,lam=s.symbols('q lam')
columns=[(a,b) for a in (0,1) for b in (0,1)]
states=[(p,r) for p in columns for r in columns]
swap=lambda p:(p[1],p[0])
reflection=lambda state:(swap(state[0]),swap(state[1]))
reps=[v for v in states if v<reflection(v)]
idx={v:i for i,v in enumerate(states)}

def local_weight(p,r,t):
    ans=s.Integer(1)
    for k in (0,1):
        c=int(r[k]!=p[k])+int(r[k]!=t[k])+int(r[k]!=r[1-k])
        if not c:return s.Integer(0)
        ans*=q**(3 if r[k] else 3-c)*sum(q**j for j in range(c))
    return s.expand(ans)

T=s.zeros(16)
for i,(p,r) in enumerate(states):
    for k,(u,t) in enumerate(states):
        if r==u:T[i,k]=local_weight(p,r,t)
N=s.Matrix([[T[idx[i],idx[j]]-T[idx[i],idx[reflection(j)]] for j in reps] for i in reps])
a=q**3*(1+q)**2
b=q**5*(1+q)**2
expected=(lam**2-q**10)*(lam**2+a*lam-q**8)*(lam**2+b*lam-q**12)
assert s.expand(N.charpoly(lam).as_expr()-expected)==0
print('characteristic factorization: PASS')
print('minus representatives:',reps)
print('factor:',s.factor(expected))

def lucas(a,b,n):
    if n==0:return s.Integer(2)
    u,v=s.Integer(2),a
    for k in range(2,n+1):u,v=v,s.expand(a*v+b*u)
    return v
for n in range(3,9):
    d=s.expand(s.trace(N**n))
    formula=s.expand((1+(-1)**n)*q**(5*n)+(-1)**n*(lucas(a,q**8,n)+lucas(b,q**12,n)))
    assert s.expand(d-formula)==0,(n,s.factor(d-formula))
    poly=s.Poly(d,q)
    assert all(((-1)**n)*int(poly.coeff_monomial(q**k))>0 for k in range(3*n,7*n+1)),n
    assert all(not poly.coeff_monomial(q**k) for k in range(3*n)),n
    print(f'n={n}: trace identity PASS, signed coefficients={4*n+1}')
print('all exact symbolic checks: PASS')
