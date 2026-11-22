"""Reproducible finite checks for a closed-form triangular-flow correction.

Uses only the Python standard library. Finite tests support, but do not replace,
the analytical proof of the uniform and all-dimensional assertions.
"""
from math import exp, expm1, sqrt, isfinite
import random


def phi(x):
    if abs(x) < 1e-7:
        return 1 - x / 2 + x*x / 6 - x*x*x / 24 + x**4 / 120
    return -expm1(-x)/x


def coeffs(a, s, T):
    assert a >= 0 and s > 0 and s >= a and T > 0
    p = 1.0 / (exp(-2*a*T)/s + 2*T*phi(2*a*T))
    ell = sqrt(p)
    return p, T*ell*phi(a*T), T*ell*phi(p*T)


def ode_rk4(a,s,T,N=5000):
    h=T/N
    L=sqrt(s)
    G=0.
    def rhs(l,g):
        return l*(a-l*l), l*(1-l*g)
    for _ in range(N):
        u,v=rhs(L,G)
        uu,vv=rhs(L+h*u/2,G+h*v/2)
        uuu,vvv=rhs(L+h*uu/2,G+h*vv/2)
        uuuu,vvvv=rhs(L+h*uuu,G+h*vvv)
        L+=h*(u+2*uu+2*uuu+uuuu)/6
        G+=h*(v+2*vv+2*vvv+vvvv)/6
    return L,G


def minor_nonnegative(M, tol=1e-8):
    n=len(M)
    for bit in range(1,1<<n):
        ix=[j for j in range(n) if (bit>>j)&1]
        if len(ix)==1: det=M[ix[0]][ix[0]]
        elif len(ix)==2:
            i,j=ix
            det=M[i][i]*M[j][j]-M[i][j]*M[j][i]
        elif len(ix)==3:
            i,j,k=ix
            a,b,c=M[i][i],M[i][j],M[i][k]
            d,e,f=M[j][i],M[j][j],M[j][k]
            g,h,z=M[k][i],M[k][j],M[k][k]
            det=a*(e*z-f*h)-b*(d*z-f*g)+c*(d*h-e*g)
        else:raise ValueError('Only dimensions <=3 tested')
        assert det>=-tol,(ix,det,M)


def corrected_factor(M,T):
    n=len(M)
    L=[[0.]*n for _ in range(n)]
    for k in range(n):
        a=M[k][k]-sum(L[k][j]**2 for j in range(k))
        assert a >= -2e-9
        a=max(a,0.)
        p,g,_=coeffs(a,max(1.,a),T)
        L[k][k]=sqrt(p)
        for i in range(k+1,n):
            r=M[i][k]-sum(L[i][j]*L[k][j] for j in range(k))
            if a==0.: assert abs(r)<1e-8
            L[i][k]=g*r
        S=[[M[i][j]-sum(L[i][h]*L[j][h] for h in range(k+1)) for j in range(k+1,n)] for i in range(k+1,n)]
        if S: minor_nonnegative(S)
    return L


def run():
    q=2*(-expm1(-0.5))
    checks=0
    cases=[(a,s,t) for a in (0,.001,.1,.75,1.,3.,10.)
           for s in (max(1.,a),max(1.,a)*2)
           for t in (.01,.1,1.,2.,10.,100.)]
    for a,s,T in cases:
        p,g,gf=coeffs(a,s,T)
        assert p>=a*(1-1e-10) and p*T <=a*T+.5+1e-9
        assert q-1e-12 <= gf/g <= 1+1e-12
        assert a*g*g < 1+1e-12
        checks+=4
    for a,s,T in ((0,1,1),(.1,1,2),(1,2,1),(2,3,.3),(5,5,.5)):
        p,g,_=coeffs(a,s,T)
        ln,gn=ode_rk4(a,s,T)
        assert abs(ln-sqrt(p))<2e-8,(a,s,T,ln,sqrt(p))
        assert abs(gn-g)<2e-8,(a,s,T,gn,g)
        checks+=2
    for T in (1e3,1e4,1e5):
        a=1/(T*T)
        p,g,gf=coeffs(a,1.,T)
        assert gf/g>=q-1e-10 and gf/g <q+2/T
        checks+=2
    rng=random.Random(1422)
    for _ in range(80):
        V=[[rng.uniform(-1,1) for j in range(3)] for i in range(3)]
        A=[[sum(V[h][i]*V[h][j] for h in range(3)) for j in range(3)] for i in range(3)]
        L=corrected_factor(A,T=10**rng.uniform(-2,2))
        assert all(isfinite(L[i][j]) for i in range(3) for j in range(3))
        checks+=1
    for a in (1e-6, .001, .5, 1, 5):
        for T in (.001,.1,10,100):
            r=sqrt(a)
            A=[[a,r],[r,1.]]
            corrected_factor(A,T)
            checks+=1
    print('VERIFY_OK',checks,'finite_checks','q=',format(q,'.17g'))

if __name__=='__main__':run()
