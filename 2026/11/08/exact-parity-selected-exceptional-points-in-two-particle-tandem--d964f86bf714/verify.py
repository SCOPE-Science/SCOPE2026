#!/usr/bin/env python3
"""Direct finite-state checks of two-particle cooperative hopping spectral formulas."""
from itertools import combinations
import numpy as np
from scipy.linalg import expm

def states_and_generator(N, alpha, beta):
    states=tuple(combinations(range(N),2))
    pos={s:i for i,s in enumerate(states)}
    G=np.zeros((len(states),len(states)))
    for s in states:
        occupied=set(s)
        ix=pos[s]
        for j in range(N):
            triple=tuple(int((j+h)%N in occupied) for h in range(3))
            if triple==(1,1,0):
                moving=(j+1)%N; rate=alpha
            elif triple==(1,0,1):
                moving=j; rate=beta
            else:continue
            new=tuple(sorted((occupied-{moving})|{(moving+1)%N}))
            iy=pos[new]
            G[ix,iy]+=rate
            G[ix,ix]-=rate
    return states,G

def classes(N):
    A={tuple(sorted((j,(j+1)%N))) :j for j in range(N)}
    B={tuple(sorted((j,(j+2)%N))) :j for j in range(N)}
    assert len(A)==len(B)==N and not set(A)&set(B)
    return A,B

def expected_eigenvalues(N, alpha,beta):
    return np.array([-(alpha+beta)/2+sigma*np.sqrt(complex((alpha-beta)**2+4*alpha*beta*np.exp(2j*np.pi*k/N)))/2
       for k in range(N) for sigma in [-1,1]], dtype=complex)

def mat_observable(N,alpha,beta):
    states,G=states_and_generator(N,alpha,beta)
    A,B=classes(N)
    chosen={}
    for j in range(N):
        chosen[tuple(sorted((j,(j+1)%N)))]=(j,'A')
        chosen[tuple(sorted((j,(j+2)%N)))]=(j,'B')
    active=[i for i,s in enumerate(states) if s in chosen]
    Q=G[np.ix_(active,active)]
    return states,G,chosen,active,Q

count=0
for N in [5,6,7,8,9,10,12]:
  for alpha,beta in [(1.,1.),(1.,.1),(1.,7.),(2.,3.),(1.,3.+2*np.sqrt(2)),(1.,3.-2*np.sqrt(2))]:
    states,G,chosen,active,Q=mat_observable(N,alpha,beta)
    assert np.allclose(np.sum(G,axis=1),0)
    assert np.allclose(np.sum(Q,axis=1),0)
    assert len(active)==2*N
    # All excluded states really are frozen.
    out=np.array(-np.diag(G))
    assert all(out[i]==0 for i in range(len(states)) if i not in active)
    # Genuine generator on active sector, eigenvalues independently computed.
    got=np.linalg.eigvals(Q)
    want=expected_eigenvalues(N,alpha,beta)
    assert max(min(abs(z-w) for w in want) for z in got) < 5e-7,(N,alpha,beta)
    # Each orientation moves by precisely one transition prescribed by rule.
    for j in range(N):
        a=tuple(sorted((j,(j+1)%N)));b=tuple(sorted((j,(j+2)%N)))
        nxt=tuple(sorted(((j+1)%N,(j+2)%N)))
        ia=states.index(a); ib=states.index(b); ip=states.index(nxt)
        assert abs(G[ia,ib]-alpha)<1e-9
        assert abs(G[ib,ip]-beta)<1e-9
    count+=1

for N in (6,8,10):
 for beta in (1.,0.17,3.-2*np.sqrt(2),3.+2*np.sqrt(2),6.):
    states,G,chosen,active,Q=mat_observable(N,1.,beta)
    i0=active.index(states.index((0,1)))
    obs=np.array([(-1.)**chosen[states[j]][0] if chosen[states[j]][1]=='A' else 0. for j in active])
    delta=complex((1-beta)**2-4*beta)**.5
    for t in (0.,0.17,0.45,1.25,3.0):
        numer=(np.exp(delta*t/2)-np.exp(-delta*t/2))/delta if abs(delta)>1e-5 else t
        value=np.exp(-(1+beta)*t/2)*(np.cosh(delta*t/2)+(beta-1)/2*numer)
        exact=(expm(Q*t)@obs)[i0]
        assert abs(exact-value)<5e-8,(N,beta,t,exact,value)
        count+=1

# Defective 2 x 2 block at exact algebraic rates: nilpotent, nonzero.
for beta in (3-2*np.sqrt(2),3+2*np.sqrt(2)):
    B=np.array([[-1.,1.],[-beta,-beta]])
    J=B+(1+beta)/2*np.eye(2)
    assert np.linalg.norm(J@J)<1e-13
    assert np.linalg.norm(J)>0.1
    count+=1
print('PASS',count,'generator/spectral/time comparisons')
