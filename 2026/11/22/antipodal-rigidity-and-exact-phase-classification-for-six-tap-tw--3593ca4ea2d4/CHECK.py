"""Independent finite tests of two-channel cyclic Gabor tightness; no optional dependencies."""
from itertools import product
from cmath import exp, pi
from math import gcd

def r_taps(t):
    return [sum(t[j+s]*t[j].conjugate() for j in range(6-s)) for s in range(1,6)]

def tight_lags(t,N,k,tol=1e-7):
    z=exp(2j*pi*k/N)
    return all(abs((1+z**s)*v)<tol for s,v in enumerate(r_taps(t),1))

def proposed(t,tol=1e-7):
    a,b=t[:2]; x=t[2]/a
    return any(all(abs(y-w)<tol for y,w in zip(t,(a,b,a*x,eps*1j*b*x,-a*x*x,b*x*x))) for eps in (-1,1))

for q,N in ((2,12),(4,12),(6,12),(8,12),(4,20)):
    roots=[exp(2j*pi*j/q) for j in range(q)]
    # Exhaustively enumerate normalized pair using g0=g1=1; restore q^2 symmetry.
    pass_tight=pass_formula=0
    for rest in product(roots, repeat=4):
        t=(1+0j,1+0j)+rest
        for k in range(1,N):
            if tight_lags(t,N,k):
                pass_tight+=1
                assert k==N//2 and proposed(t)
                pass_formula+=1
    predicted=2*q if q%4==0 else 0
    assert pass_tight==predicted,(q,N,pass_tight,predicted)
    print(f'PHASE_COUNT_OK q={q} N={N} normalized={pass_tight} labelled={pass_tight*q*q}')

# Direct time-domain frame-operator check, independent of lag criterion.
def frame_operator(t,N,k):
    from math import isclose
    z=exp(2j*pi/N)
    S=[[0j]*N for _ in range(N)]
    for p in (0,k):
        for a in range(N):
            v=[(z**(p*j))*t[(j-a)%N] if (j-a)%N<6 else 0j for j in range(N)]
            for i in range(N):
                for j in range(N): S[i][j]+=v[i]*v[j].conjugate()
    return S
for N in (12,14,20):
    g=(1+0j,1+0j,1+0j,1j,-1+0j,1+0j)
    S=frame_operator(g,N,N//2)
    err=max(abs(S[i][j]-(12 if i==j else 0)) for i in range(N) for j in range(N))
    assert err<1e-8,(N,err)
    print(f'DIRECT_GRAM_OK N={N} max_error={err:.3g}')
print('ALL_CHECKS_OK')
