#!/usr/bin/env python3
"""Reproducible exact checks for two pinned leaders on unit clique coronas.

Requires SymPy. Finite checks corroborate, but do not replace, the all-size proof.
"""
import itertools
import sympy as s

N, z = s.symbols('n z', integer=True, positive=True)
A = N + (N + 2)*z + z*z
B = N + 1 + z
factors = {
    'CC': [(1+z,2),(A,N-3),(A-(N-2)*(1+z),1)],
    'CLsame': [(A,N-2),(A-(N-1)*(1+z),1)],
    'CLdiff': [(1+z,1),(A,N-3),(A*B-(N-2)*(1+z)*B-A,1)],
    'LL': [(A,N-3),(B,1),(A*B-(N-2)*(1+z)*B-2*A,1)],
}
J2 = {
    'CC': (N+2)*(N*N+2*N-6)/N**2,
    'CLsame': (N-1)*(N*N+8*N+8)/N**2,
    'CLdiff': (N**5+11*N**4+14*N**3-20*N**2-56*N-48)/(N**2*(N+2)**2),
    'LL': (N**6+4*N**5+2*N**4-6*N**3-18*N**2-26*N-12)/(N**2*(N+1)**2),
}
J1 = {
    'CC': (N*N+3*N-6)/N,
    'CLsame': (N-1)*(N+4)/N,
    'CLdiff': (N**3+5*N*N-2*N-12)/(N*(N+2)),
    'LL': (2*N**3+2*N*N-5*N-6)/(N*(N+1)),
}
for key, fs in factors.items():
    d1 = sum(k*s.diff(f,z).subs(z,0)/f.subs(z,0) for f,k in fs)
    d2 = sum(k*((s.diff(f,z).subs(z,0)/f.subs(z,0))**2 - s.diff(f,z,2).subs(z,0)/f.subs(z,0)) for f,k in fs)
    assert s.cancel(d1-J1[key]) == 0, ('J1',key)
    assert s.cancel(d2-J2[key]) == 0, ('J2',key)
assert s.cancel(J2['CC']-J2['CLdiff']+(3*N*N-4*N-16)/(N+2)**2) == 0
assert s.cancel(J2['CLsame']-J2['CC']-(3*N*N+2*N+4)/N**2) == 0
assert s.cancel(J2['LL']-J2['CC']-(N**4+3*N**3-4*N*N-13*N-6)/(N+1)**2) == 0
assert s.cancel(J2['CLsame']-J2['CLdiff']-2*(9*N**3+20*N*N+12*N+8)/(N*N*(N+2)**2)) == 0
assert s.cancel(J1['CC']-J1['CLdiff']-2/(N+2)) == 0
x=s.symbols('x', nonnegative=True)
assert s.expand((N**4+3*N**3-4*N**2-13*N-6).subs(N,x+3)) == x**4+15*x**3+77*x*x+152*x+81

def graph_laplacian(n):
    L = s.zeros(2*n)
    for i in range(n):
        for j in range(i+1,n):
            L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
        L[i,i]+=1; L[n+i,n+i]+=1;L[i,n+i]-=1;L[n+i,i]-=1
    return L

def orbit(pair,n):
    a,b = sorted(pair)
    if b<n: return 'CC'
    if a>=n: return 'LL'
    if a==b-n: return 'CLsame'
    return 'CLdiff'

checks=0
for n in range(3,9):
    L=graph_laplacian(n)
    for S in itertools.combinations(range(2*n),2):
        # Exhaustive for n up to 6, representative orbits for n=7 and 8.
        if n>=7 and S not in [(0,1),(0,n),(0,n+1),(n,n+1)]: continue
        follower=[v for v in range(2*n) if v not in S]
        Q=L.extract(follower,follower)
        inv=Q.inv()
        label=orbit(S,n)
        assert s.trace(inv)==s.cancel(J1[label].subs(N,n)),(n,S,label,'J1')
        assert s.trace(inv*inv)==s.cancel(J2[label].subs(N,n)),(n,S,label,'J2')
        if n<=6:
            assert s.factor(Q.charpoly().as_expr().subs(s.Symbol('lambda'),-z)*(-1)**len(follower)-s.prod(f.subs(N,n)**k.subs(N,n) if hasattr(k,'subs') else f.subs(N,n)**k for f,k in factors[label]))==0,(n,S,label,'det')
        checks+=1
    vals={k:s.cancel(v.subs(N,n)) for k,v in J2.items()}
    winners=[k for k,v in vals.items() if v==min(vals.values())]
    assert winners==(['CLdiff'] if n==3 else ['CC']), (n,winners)
print('PASS: 8 symbolic derivative/comparison identities; '+str(checks)+' exact grounded-matrix comparisons; all tested optimizer regimes.')
