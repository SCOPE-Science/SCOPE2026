"""Reproducibility tests for isolated-vertex fluctuations in growing uniform hypergraphs.
Pure Python standard-library checks; not a substitute for an asymptotic proof.
"""
from fractions import Fraction as F
from math import comb
from collections import defaultdict

COUNT=0

def check(test, what):
    global COUNT
    if not test:
        raise AssertionError(what)
    COUNT += 1

def coefficients(k, p):
    p = F(p)
    q = 1-p
    r = p/(p+k*q)
    a = k*q/p
    nn = p*q
    nj = p*r*(1-r)
    jj = p*r*(1-r)*(2+(k-2)*r)/(2-r)
    ni = r*nn+nj
    ii = r*r*nn+2*r*nj+jj
    return r,a,nn,ni,ii,nj,jj

def transitions(N,I,E,k,p):
    """Exact lumped transition probabilities with distinct, never-repeated hyperedges.
    If all k-tuples have been used, an edge attempt is a null update.
    """
    q = 1-p
    out = [(p,N+1,I+1,E)]
    C = comb(N,k)
    if E == C:
        out.append((q,N,I,E))
        return out
    available = C-E
    for y in range(k+1):
        possible = comb(I,y)*comb(N-I,k-y) if y<=I and k-y<=N-I else 0
        if y==0: possible -= E
        if possible:
            out.append((q*F(possible,available),N,I-y,E+1))
    check(sum(x[0] for x in out)==1, 'transition normalization')
    return out

def exact_dp(k,p,steps):
    states = {(k,k,0):F(1)}
    stats=[]
    for t in range(steps+1):
        mass=sum(states.values())
        check(mass==1,'total mass conservation')
        nmean=sum(F(n)*w for (n,i,e),w in states.items())
        imean=sum(F(i)*w for (n,i,e),w in states.items())
        nii=sum(F(i*i)*w for (n,i,e),w in states.items())
        cross=sum(F(n*i)*w for (n,i,e),w in states.items())
        check(nmean==k+p*t,'exact vertex birth mean')
        check(0<=imean<=nmean,'isolate mean range')
        check(nii>=imean*imean,'variance nonnegative')
        stats.append((imean,nii-imean*imean,cross-nmean*imean))
        if t==steps: break
        nxt=defaultdict(F)
        for (n,i,e),w in states.items():
            for prob,n2,i2,e2 in transitions(n,i,e,k,p):
                nxt[(n2,i2,e2)]+=w*prob
        states=nxt
    return stats

for k in range(3,8):
    for a,b in [(1,2),(1,3),(2,3),(3,5),(4,5)]:
        p=F(a,b)
        r,z,NN,NI,II,NJ,JJ=coefficients(k,p)
        check(r>0 and r<1,'r interior')
        check(NN>0 and II>0,'nondegenerate marginals')
        check(NN*II>NI*NI,'positive definite covariance')
        check(z>0,'stable exponent')
        # Algebraic Lyapunov equation in coordinates (N,J=I-r*N).
        check(NJ==p*(1-r)/(1+z),'cross Lyapunov')
        check(JJ==p*(1-r)*(2+(k-2)*r)/(1+2*z),'variance Lyapunov')
        check(NI==r*NN+NJ,'back transform cross')
        check(II==r*r*NN+2*r*NJ+JJ,'back transform variance')

check(coefficients(3,F(1,2))[2:5] == (F(1,4),F(5,32),F(41,224)), 'exact k=3 half probabilities')
for k,p in [(3,F(1,2)),(3,F(2,3)),(4,F(1,2))]:
    stats=exact_dp(k,p,11)
    # deterministic bound: E(I) at time t, constrained by number of births
    for t,(mu,var,cov) in enumerate(stats):
        check(mu <= k + p*t,'mean bound')
        check(var>=0,'exact variance')
        check(cov*cov <= var*(t*p*(1-p)) if t else cov==0,'Cauchy covariance')
print('PASS:', COUNT, 'exact arithmetic assertions')
print('k=3,p=1/2 limit variance coefficient:',coefficients(3,F(1,2))[4])
