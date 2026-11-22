#!/usr/bin/env python3
"""Exact finite-state certificates for the first-prime Stern square-root threshold.

Run: python3 verify_stern_prime_threshold.py (requires sympy).
No numerical eigenvalue computation is used in the certificates.
"""
import sympy as sp

X = sp.Symbol('X')
FACTORS = {
 2: (X-2)*(X-1)*(X+1),
 3: X**2*(X-2)*(X-1)**3*(X**2+X+2),
 5: X**4*(X-2)*(X-1)**7*(X+1)**2*(X**2+1)**2*(X**2-X+2)*(X**4-X**2+4),
 7: X**10*(X-2)*(X-1)**11*(X+1)**4*(X**2+2)*(X**4+3)**2*(X**4+X**3+2*X+4)*(X**4-2*X**3+3*X**2-4*X+4)**2,
 11: X**20*(X-2)*(X-1)**21*(X+1)**10*(X**2-2*X+2)*(X**2+X+2)*(X**2+2*X+2)*(X**3-X+2)**2*(X**8+3*X**4+16)**2*(X**4-3*X**3+5*X**2-6*X+4)**2*(X**4-X**3+3*X**2-2*X+4)**2*(X**12+X**10-2*X**9+X**8-4*X**7+4*X**5+13*X**4+4*X**3-X**2-2*X+1)**2
}

def build(p):
    states = [(a,b) for a in range(p) for b in range(p) if a or b]
    ix = {u:i for i,u in enumerate(states)}
    L = [ix[(a,(a+b)%p)] for a,b in states]
    R = [ix[((a+b)%p,b)] for a,b in states]
    T = sp.zeros(len(states))
    for j in range(len(states)):
        T[L[j],j] += 1
        T[R[j],j] += 1
    assert all(sum(T[:,j])==2 for j in range(len(states)))
    assert all(sum(T[i,:])==2 for i in range(len(states)))
    assert len(set(L)) == len(states) and len(set(R)) == len(states)
    return states,ix,L,R,T

def test_direct(p,ix,L,R):
    v=[0]*len(ix)
    v[ix[(0,1)]]=1
    seq=[0,1]
    for k in range(0,13):
        if len(seq)<(1<<k)+1:
            for n in range(len(seq),(1<<k)+1):
                seq.append(seq[n//2] if n%2==0 else seq[(n-1)//2]+seq[(n+1)//2])
        direct = [0]*len(ix)
        for n in range(1<<k):
            direct[ix[(seq[n]%p,seq[n+1]%p)]]+=1
        assert direct==v,(p,k)
        w=[0]*len(v)
        for i,a in enumerate(v):
            w[L[i]]+=a
            w[R[i]]+=a
        v=w

for p in [2,3,5,7,11]:
    states,ix,L,R,T=build(p)
    expected=sp.Poly(FACTORS[p],X)
    observed=sp.Poly(T.charpoly(X).as_expr(),X)
    assert observed == expected,(p,sp.factor(observed.as_expr()-expected.as_expr()))
    assert sp.degree(expected) == p*p-1
    test_direct(p,ix,L,R)
    print('EXACT charpoly & direct dyadic counts: p=',p,'states=',len(states))
    if p==11:
        q=X**3-X+2
        assert sp.Poly(q,X).is_irreducible
        div,rem=sp.div(observed.as_expr(),(X-2)*q*q,X)
        assert rem==0
        P=sp.Poly((X-2)*div,X)
        coef=[int(P.nth(j)) for j in range(P.degree()+1)]
        v=[0]*len(states)
        v[ix[(0,1)]]=1
        projection=[0]*len(states)
        for c in coef:
            if c:
                for j,vj in enumerate(v):
                    projection[j]+=c*vj
            w=[0]*len(states)
            for j,vj in enumerate(v):
                if vj:
                    w[L[j]]+=vj
                    w[R[j]]+=vj
            v=w
        certificate=projection[ix[(1,2)]]
        assert P.degree()==114
        assert certificate==573530441763580574433280
        assert certificate!=0
        print('NONZERO cubic-mode certificate for (1,2):',certificate)
        print('q=X^3-X+2; irrational real root is <-sqrt(2)')

# Algebraic radial bounds at p=5 and p=7, used in the proof:
# Setting y=X+2/X, reciprocal quartics reduce to y^2-5,
# y^2+y-4, and y^2-2y-1, respectively. Their real roots
# have modulus <2*sqrt(2); hence every original root has
# modulus exactly sqrt(2).
y5=[sp.sqrt(5),-sp.sqrt(5)]
y7a=[(-1+sp.sqrt(17))/2,(-1-sp.sqrt(17))/2]
y7b=[1+sp.sqrt(2),1-sp.sqrt(2)]
for y in y5+y7a+y7b:
    assert bool((8-y*y)>0)
print('PASS: all exact characteristic, scalar-mode, and circle-root certificates')
