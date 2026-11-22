"""High-precision finite diagnostics for parity-dependent Fourier heat positivity.
These tests do not replace the asymptotic proof in RESULT.md.
Requires mpmath, Python 3; run: python verify.py.
"""
from mpmath import mp
mp.dps = 135
checks=0

def check(condition,message):
    global checks
    checks+=1
    if not condition:
        raise AssertionError(message)

def spec(N,t,j):
    x=2*mp.pi*j/N
    if N%2==0:
        k=N//2
        v=1+sum(2*mp.exp(-t*r*r)*mp.cos(r*x) for r in range(1,k))
        v+=mp.exp(-t*k*k)*(-1)**j
    else:
        k=N//2
        v=1+sum(2*mp.exp(-t*r*r)*mp.cos(r*x) for r in range(1,k+1))
    return v

def theta(N,t,j):
    x=2*mp.pi*j/N
    return mp.sqrt(mp.pi/t)*sum(mp.exp(-(x-2*mp.pi*r)**2/(4*t)) for r in range(-5,7))

def tail(N,t,j):
    x=2*mp.pi*j/N
    if N%2==0:
        K=N//2
        return mp.exp(-t*K*K)*(-1)**j + 2*sum(mp.exp(-t*k*k)*mp.cos(k*x) for k in range(K+1,K+401))
    K=(N+1)//2
    return 2*sum(mp.exp(-t*k*k)*mp.cos(k*x) for k in range(K,K+401))

for N in [20,21,31,40,41,51,64,100,101,128,151,201]:
    for c in [mp.mpf('2.7'),mp.mpf('3.0'),mp.mpf('3.5')]:
        t=c/N
        for j in [0,1,N//4,N//2]:
            th=theta(N,t,j)
            sp=spec(N,t,j)
            r=tail(N,t,j)
            check(abs((th-r)-sp) < mp.mpf('1e-70'),(N,c,j,'identity',th-r-sp))
            check(th>0,(N,c,j,'theta positive'))
        check(abs(sum(spec(N,t,j) for j in range(N))-N) < mp.mpf('1e-65'),(N,c,'mass'))
    # At c=2.75 the antipodal even index is negative for sufficiently large N.
    if N>=64:
        j=2*(N//4)
        check(spec(N,mp.mpf('2.75')/N,j)<0,(N,'early negative'))
        check(all(spec(N,mp.mpf('3.55')/N,j)>0 for j in range(N)),(N,'late positive'))
    # The parity-dependent logarithmic correction is asymptotically of order 1/N^2.
    # A generous finite-N bracket deliberately makes no claim of sharp constants.
    if N>=100:
        shift=(1 if N%2==0 else 3)*mp.log(N)
        c_l=mp.pi-(shift+mp.mpf('10'))/N
        c_r=mp.pi-(shift-mp.mpf('10'))/N
        j=2*(N//4)
        check(spec(N,c_l/N,j)<0,(N,'lower bracket',j))
        check(all(spec(N,c_r/N,j)>0 for j in range(N)),(N,'upper bracket'))

print('PASS:',checks,'high-precision finite assertions')
