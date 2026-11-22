#!/usr/bin/env python3
"""Exact degree-two stationary moment verification for a finite inclusion network.
Run: python CHECK.py; requires Python 3 and sympy.
"""
import itertools
import sympy as sp


def check(n, kappa, gamma, coupling, rho_a, rho_b):
    k, g, v, ra, rb = map(sp.Rational, (kappa, gamma, coupling, rho_a, rho_b))
    N=2*n
    z=sp.symbols('z0:'+str(N))
    rho=[ra]*n+[rb]*n
    terms=[(1,)]
    # E monomials of degree <=2 as exponent tuples.
    monoms=[sp.Integer(1)]+list(z)+[z[i]*z[j] for i in range(N) for j in range(i,N)]
    exponents=[sp.Poly(m,*z).monoms()[0] for m in monoms]
    ei={exp:i for i,exp in enumerate(exponents)}
    def transition_polynomial(f):
        total=sp.Integer(0)
        # Indirect substitution via polynomial variable shift; independent of covariance identities.
        for i in range(n):
            for j in range(n,N):
                move_ij=f.subs({z[i]:z[i]-1,z[j]:z[j]+1}, simultaneous=True)-f
                move_ji=f.subs({z[i]:z[i]+1,z[j]:z[j]-1}, simultaneous=True)-f
                total+=v/n*(z[i]*(k+z[j])*move_ij+z[j]*(k+z[i])*move_ji)
        for i in range(N):
            rate=g*rho[i]/k
            total+=rate*(k+z[i])*(f.subs(z[i],z[i]+1)-f)
            total+=(g+rate)*z[i]*(f.subs(z[i],z[i]-1)-f)
        return sp.Poly(sp.expand(total),*z)
    A=sp.zeros(len(monoms)-1)
    b=sp.zeros(len(monoms)-1,1)
    for index,m in enumerate(monoms[1:]):
        poly=transition_polynomial(m)
        for term,coeff in poly.terms():
            col=ei[term]
            if col==0:b[index]=-coeff
            else:A[index,col-1]=coeff
    raw=list(sp.linsolve((A,b)))[0]
    raw=[sp.factor(t) for t in raw]
    means=[raw[i] for i in range(N)]
    pairs={}
    offset=N
    for i in range(N):
        for j in range(i,N):
            pairs[i,j]=raw[offset];offset+=1
    def cov(i,j):return sp.factor(pairs[min(i,j),max(i,j)]-means[i]*means[j])
    pred_cross=sp.factor(g*v*(g+k*v)*(ra-rb)**2/(2*(g+2*k*v)**2*(g*n+2*k*n*v+v)))
    pred_same=sp.factor(k*v/(g+k*v)*pred_cross)
    assert all(means[i] == sp.factor((ra+rb)/2 + g*(ra-rb)/(2*(g+2*k*v))) for i in range(n))
    assert all(means[i] == sp.factor((ra+rb)/2 - g*(ra-rb)/(2*(g+2*k*v))) for i in range(n,N))
    assert all(cov(i,j)==pred_cross for i in range(n) for j in range(n,N))
    assert all(cov(i,j)==pred_same for a in (range(n),range(n,N)) for i,j in itertools.combinations(a,2))
    print(f'n={n} kappa={k} gamma={g} v={v} rho_A={ra} rho_B={rb}: PASS, all {len(monoms)-1} exact stationarity equations, cov_A_B={pred_cross}, cov_same={pred_same}')

if __name__=='__main__':
    check(2,1,2,3,1,4)
    check(2,3,2,1,sp.Rational(1,2),sp.Rational(5,3))
    check(3,2,3,sp.Rational(1,2),sp.Rational(5,4),sp.Rational(11,4))
    check(3,1,1,2,4,4)
    print('All full-site exact-rational checks passed.')
