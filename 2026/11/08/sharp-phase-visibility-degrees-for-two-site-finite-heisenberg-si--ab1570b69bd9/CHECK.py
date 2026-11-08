"""Finite sanity checks for two-site Heisenberg phase-visibility degrees.
Proof of all-order lower bound is the congruence argument in RESULT.md.
This script is only finite confirmation, not an infinite certificate.
"""
import cmath, math, random

def balanced_candidate_exists(N,d,maxdegree):
    m=N//math.gcd(N,d)
    for L in range(1,maxdegree+1):
        for u in range(L+1):
          for v in range(L-u+1):
           for s in range(L-u-v+1):
            t=L-u-v-s
            if u+v!=s+t:continue
            if ((v-t)*d)%N==0 and v!=t:
                return L
    return None

def full_candidate_exists(N,d,maxdegree):
    for L in range(1,maxdegree+1):
        for u in range(L+1):
          for v in range(L-u+1):
           for s in range(L-u-v+1):
            t=L-u-v-s
            if (u+v-s-t)%N: continue
            if ((v-t)*d)%N:continue
            if v!=t: return L
    return None

def mixed_invariant(x,d):
    N=len(x);m=N//math.gcd(N,d)
    return sum(x[(j+d)%N]**m*x[j].conjugate()**m for j in range(N))

def holomorphic_invariant(x):
    N=len(x)
    return sum(z**N for z in x)

def act(x,k,n,alpha):
    N=len(x);w=cmath.exp(2j*math.pi/N)
    return [alpha*w**(n*j)*x[(j+k)%N] for j in range(N)]

def close(z,w,tol=1e-7):
    return abs(z-w)<tol*max(1,abs(z),abs(w))

checks=0
for N in range(2,17):
 for d in range(1,N):
    m=N//math.gcd(N,d)
    assert balanced_candidate_exists(N,d,min(2*m,13)-1) is None
    assert full_candidate_exists(N,d,min(min(N,2*m),13)-1) is None
    checks+=2
    if 2*m<=13:
        assert balanced_candidate_exists(N,d,2*m)==2*m
        checks+=1
    if min(N,2*m)<=13:
        assert full_candidate_exists(N,d,min(N,2*m))==min(N,2*m)
        checks+=1
for N in range(2,29):
 for d in range(1,N):
    m=N//math.gcd(N,d)
    A,B=1.2+0j,0.8*cmath.exp(0.31j)
    x=[0j]*N;x[0]=A;x[d]=B
    F=mixed_invariant(x,d);H=holomorphic_invariant(x)
    phase_x=x[:]; phase_x[d]*=cmath.exp(0.46j)
    assert not (close(F,mixed_invariant(phase_x,d)) and close(F,mixed_invariant([A if j==0 else (B*cmath.exp(0.82j) if j==d else 0j) for j in range(N)],d)))
    # Independent evaluations at translated, modulated and globally rotated inputs.
    for k,n,theta in [(0,1,0.3),(1,2,0.7),(N-1,N-1,1.1)]:
        y=act(x,k,n,cmath.exp(1j*theta))
        assert close(F,mixed_invariant(y,d))
        # For H only Nth-root global phases are allowed.
        z=act(x,k,n,cmath.exp(2j*math.pi/N))
        assert close(H,holomorphic_invariant(z))
        checks+=2
    checks+=1
print('PASS',checks,'assertion groups; finite checks do not replace general proof')
