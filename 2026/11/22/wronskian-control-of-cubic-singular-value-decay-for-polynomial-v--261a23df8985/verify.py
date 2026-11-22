"""Reproducible finite checks for polynomial Volterra-commutator identities.

This program is supplementary: the infinite singular-value theorem is proved
analytically and is not certified by finite matrices.
"""
from fractions import Fraction
from math import pi
from cmath import exp


def symbol(g,h):
    out={}
    for m,am in g.items():
        for n,bn in h.items():
            if m and n:
                L=m+n
                out[L]=out.get(L,0)+m*n*(m-n)*am*bn
    return {L:v for L,v in out.items() if v}


def comm_coefficient(g,h,k,L):
    z=Fraction(0)
    for m,a in g.items():
        n=L-m
        if m and n in h and n:
            z+=Fraction(a*h[n]*m*n*(m-n),(k+m)*(k+n)*(k+L))
    return z


def via_matrix(g,h,k,L):
    a=Fraction(0)
    b=Fraction(0)
    for m,gm in g.items():
        n=L-m
        if m and n in h and n:
            a+=Fraction(h[n]*n,k+n)*Fraction(gm*m,k+L)
            b+=Fraction(gm*m,k+m)*Fraction(h[n]*n,k+L)
    return a-b


def test_exact():
    examples=[({1:1},{2:1}),({1:1,2:1},{2:1,3:1}),
              ({1:2,3:-2,4:1},{2:-1,4:3}),({2:7},{2:3}),
              ({1:0,2:5,5:-2},{1:3,2:2,3:-1})]
    tests=0
    for g,h in examples:
        for L in range(2,11):
            for k in range(0,24):
                assert comm_coefficient(g,h,k,L)==via_matrix(g,h,k,L)
                tests+=1
        w=symbol(g,h)
        for L in range(2,11):
            for k in [1000,10000,100000]:
                # leading symbol; rigorous asymptotic follows from rational expansion
                error=float((k**3)*comm_coefficient(g,h,k,L)-w.get(L,0))
                assert abs(error)<1600*(max(1,abs(w.get(L,0))))/k
                tests+=1
    for m in range(1,10):
        for n in range(1,10):
            if m==n: continue
            z=abs(Fraction(m*n*(m-n),m*n*(m+n)))
            assert z==Fraction(abs(m-n),m+n)
            for k in range(0,50):
                a=abs(comm_coefficient({m:1},{n:1},k,m+n))
                b=Fraction(m*n*abs(m-n),(k+m)*(k+n)*(k+m+n))
                assert a==b
                tests+=1
    print('exact coefficient, symbol and monomial checks:',tests,'PASS')


def test_numerical():
    try:
        import numpy as np
        from scipy.linalg import svdvals
    except ImportError:
        print('optional numerical SVD checks skipped: numpy/scipy missing')
        return
    g={1:1,2:1};h={2:1,3:1}
    N=350
    M=np.zeros((N,N))
    for k in range(N):
        for L in range(2,6):
            if k+L<N: M[k+L,k]=float(comm_coefficient(g,h,k,L))
    s=svdvals(M)
    coeff=symbol(g,h)
    theta=np.linspace(0,2*np.pi,24000,endpoint=False)
    W=sum(v*np.exp(1j*L*theta) for L,v in coeff.items())
    C=float(np.mean(np.abs(W)**(1/3))**3)
    # Finite sections suppress the remote tail, so do not treat these as proofs.
    vals=[(j, float((j**3)*s[j-1])) for j in (15,25,40)]
    assert C>0 and all(v>0 for j,v in vals)
    print('symbol coefficient:',format(C,'.10g'),'finite-section scaled singular values:',vals)
    print('optional numerical spectral probes: PASS')

if __name__=='__main__':
    test_exact()
    test_numerical()
