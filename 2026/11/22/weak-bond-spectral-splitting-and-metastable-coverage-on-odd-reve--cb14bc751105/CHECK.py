#!/usr/bin/env python3
"""Reproducible finite checks for a weak closing bond in reversible dimer adsorption.
Only standard-library modules are required for the exact checks.
Optional NumPy confirms small-positive-rate spectral asymptotics.
"""
from collections import deque
from fractions import Fraction
from math import comb

checks = 0

def assert_exact(condition, context):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(context)

def shell(N, k):
    return [bits for bits in range(1 << N) if bits.bit_count() == k]

def swaps(bits, N):
    for j in range(N-1):
        if ((bits >> j) & 1) != ((bits >> (j+1)) & 1):
            yield bits ^ (3 << j)

def kw(N, k, j):
    return sum((-1)**l * comb(k,l)*comb(N-k,j-l)
               for l in range(max(0, j-(N-k)), min(k,j)+1))

def birth(N,k):
    return Fraction((N-k)*(N-k-1), N*(N-1))

def death(N,k):
    return Fraction(k*(k-1), N*(N-1))

def exact_checks(N):
    m = (N-1)//2
    parity = m%2
    choices = list(range(parity, N+1, 2))
    assert_exact(len(choices)==m+1, ('sector count', N))
    allowed = [v for v in range(1<<N) if v.bit_count()%2==parity]
    assert_exact(len(allowed)==2**(N-1), ('parity class',N))
    for k in choices:
        states = shell(N,k)
        assert_exact(len(states)==comb(N,k),('binomial sector',N,k))
        # Path exchanges connect every fixed-particle-number sector.
        seen = {states[0]}; queue=deque([states[0]])
        while queue:
            for z in swaps(queue.popleft(), N):
                if z not in seen:
                    seen.add(z); queue.append(z)
        assert_exact(len(seen)==len(states), ('irreducibility',N,k))
        # The weak bond flips endpoint bits only if they coincide.
        n00=sum(((x&1)==0 and ((x>>(N-1))&1)==0) for x in states)
        n11=sum(((x&1)==1 and ((x>>(N-1))&1)==1) for x in states)
        a=comb(N-2,k) if k<=N-2 else 0
        b=comb(N-2,k-2) if k>=2 else 0
        assert_exact(n00==a and n11==b, ('endpoint selection',N,k))
        assert_exact(Fraction(n00,comb(N,k))==birth(N,k),('birth rate',N,k))
        assert_exact(Fraction(n11,comb(N,k))==death(N,k),('death rate',N,k))
        assert_exact(2*(birth(N,k)-death(N,k))==
                     -Fraction(4,N)*(Fraction(k)-Fraction(N,2)),
                     ('linear moment eigenmode',N,k))
        for j in range(m+1):
            lhs=0
            if k+2<=N:
                lhs+=birth(N,k)*(kw(N,k+2,j)-kw(N,k,j))
            if k-2>=0:
                lhs+=death(N,k)*(kw(N,k-2,j)-kw(N,k,j))
            lam=Fraction(4*j*(N-j),N*(N-1))
            assert_exact(lhs==-lam*kw(N,k,j),('Krawtchouk eigenrelation',N,k,j))
    assert_exact(sum(comb(N,k) for k in choices)==2**(N-1),('normalization',N))
    # Original occupation count from eta: odd sites occupied = eta; even = 1-eta.
    init_eta=sum(1<<j for j in range(N) if j%2==1)
    assert_exact(init_eta.bit_count()==m,('initial',N))
    k=m
    sector_total=sum(sum(((bits>>j)&1) if j%2==0 else 1-((bits>>j)&1)
                          for j in range(N)) for bits in shell(N,k))
    sector_theta=Fraction(sector_total, N*comb(N,k))
    assert_exact(sector_theta==Fraction(N*N-1,2*N*N),('isolated path equilibrium',N))
    global_total=sum(sum(((bits>>j)&1) if j%2==0 else 1-((bits>>j)&1)
                          for j in range(N)) for bits in allowed)
    assert_exact(Fraction(global_total,N*len(allowed))==Fraction(1,2),
                 ('closed-ring equilibrium',N))

if __name__ == '__main__':
    for n in (3,5,7,9,11):
        exact_checks(n)
    print(f'PASS: {checks} exact finite assertions on N=3,5,7,9,11')
    try:
        import numpy as np
    except ImportError:
        print('Optional numerical spectral checks skipped (NumPy unavailable).')
    else:
        checked=0
        for N in (3,5,7):
            m=(N-1)//2
            states=[x for x in range(1<<N) if x.bit_count()%2==m%2]
            ind={x:i for i,x in enumerate(states)}
            e=1.e-4
            M=np.zeros((len(states),len(states)))
            for ix,x in enumerate(states):
                for z in swaps(x,N):
                    M[ix,ind[z]]+=1; M[ix,ix]-=1
                if (x&1)==((x>>(N-1))&1):
                    z=x ^ 1 ^ (1<<(N-1))
                    M[ix,ind[z]]+=e; M[ix,ix]-=e
            val, vec=np.linalg.eigh(M)
            eig=np.sort(-val)[:m+1]
            target=np.array([4*j*(N-j)/(N*(N-1)) for j in range(m+1)])
            if max(abs(eig/e-target))>0.001:
                raise AssertionError(('low spectral comparison', N,eig/e,target))
            checked+=len(eig)
            # Independent finite-rate transient comparison on the slow time scale.
            initial=sum(1<<j for j in range(N) if j%2==1)
            obs=np.array([sum(((bits>>j)&1) if j%2==0 else
                              1-((bits>>j)&1) for j in range(N))/N
                          for bits in states])
            for s in (0.5,1.,2.):
                distribution=vec @ (np.exp(val*s/e)*vec[ind[initial],:])
                observed=float(obs @ distribution)
                limit=0.5-np.exp(-4*s/N)/(2*N*N)
                if abs(observed-limit)>0.0001:
                    raise AssertionError(('slow coverage',N,s,observed,limit))
                checked+=1
        print(f'PASS: {checked} small-weak-rate spectral and slow-coverage comparisons')
