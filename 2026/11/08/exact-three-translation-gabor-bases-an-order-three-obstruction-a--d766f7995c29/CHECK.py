"""Exact checks for the three-translation Gabor phase classification.
Run: python CHECK.py. No external dependencies.
"""
from itertools import product, permutations
from math import gcd
from random import Random
from collections import Counter
from cmath import exp
from math import pi

def zero_three(values,q):
    if q % 3:
        return False
    a,b,c=values
    return {(b-a)%q,(c-a)%q}=={q//3,2*q//3}

def direct_test(g,k,q):
    N=len(g); assert N%3==0
    M=N//3
    for j in range(M):
        for t,u in ((0,1),(0,2),(1,2)):
            differences=[(g[(j+s*M-t*k)%N]-g[(j+s*M-u*k)%N])%q for s in range(3)]
            if not zero_three(differences,q): return False
    return True

def construct(N,k,q,choice,scalars):
    M=N//3; d=gcd(N,k); l=M//d
    assert q%3==0 and N//d%3==0 and len(choice)==d and len(scalars)==M
    omega=q//3
    g=[None]*N
    visited=set(); ci=0; si=0
    for j in range(M):
        if j in visited: continue
        fiber_indices=[(j-h*k)%M for h in range(l)]
        visited.update(fiber_indices)
        c=(l*k//M)%3
        assert c in (1,2)
        tag=choice[ci];ci+=1
        if l%3==0:
            perm=list(permutations(range(3)))[tag]
            vectors=[[omega*perm[h%3]*s % q for s in range(3)] for h in range(l)]
        else:
            seed_b,seed_c=((0,1),(0,2),(1,0),(1,1),(2,0),(2,2))[tag]
            seed=[0,seed_b*omega,seed_c*omega]
            inv=1 if l%3==1 else 2
            vectors=[[seed[(s-c*(inv*h))%3] for s in range(3)] for h in range(l)]
        for h in range(l):
            a=scalars[si];si+=1
            for s in range(3):
                x=(j+s*M-h*k)%N
                assert g[x] is None
                g[x]=(a+vectors[h][s])%q
    assert None not in g
    return tuple(g)

def main():
    rng=Random(3519)
    stats=Counter()
    for N,q in [(3,3),(6,3),(9,3),(12,3),(6,6),(9,6),(6,9)]:
        M=N//3
        for k in range(1,N):
            # All possible windows are counted modulo their common q-th-root phase.
            if q**(N-1)>4_000_000:continue
            count=sum(direct_test((0,)+tail,k,q) for tail in product(range(q), repeat=N-1))
            d=gcd(N,k)
            want=6**d*q**(M-1) if N//d%3==0 and q%3==0 else 0
            assert count==want,(N,q,k,count,want)
            stats['exhaustive_parameter_cases']+=1
            stats['tested_normalized_windows']+=q**(N-1)
    for N in range(3,61,3):
        M=N//3
        for k in range(1,N):
            d=gcd(N,k)
            if (N//d)%3: continue
            for q in [3,6,9,12]:
                for z in range(4):
                    choice=[rng.randrange(6) for _ in range(d)]
                    scalars=[rng.randrange(q) for _ in range(M)]
                    g=construct(N,k,q,choice,scalars)
                    assert direct_test(g,k,q),(N,k,q,choice,scalars,g)
                    stats['constructed_valid_examples']+=1
    # Independent full-N Gabor synthesis Gram check, bypassing fiber criterion.
    for N in [3,6,9,12,15,18,21,24,27,30]:
        M=N//3
        for k in range(1,N):
            d=gcd(N,k)
            if N//d%3: continue
            q=3*(1+(N+k)%4)
            tags=[rng.randrange(6) for _ in range(d)]
            phases=[rng.randrange(q) for _ in range(M)]
            g=construct(N,k,q,tags,phases)
            omega=exp(2j*pi/q)
            arr=[omega**u/(N**0.5) for u in g]
            basis=[]
            for t in range(3):
                for m in range(M):
                    basis.append([arr[(j-t*k)%N]*exp(2j*pi*m*j/M) for j in range(N)])
            assert len(basis)==N
            for i in range(N):
                for j in range(N):
                    inner=sum(x.conjugate()*y for x,y in zip(basis[i],basis[j]))
                    assert abs(inner-(1 if i==j else 0))<1e-10,(N,k,i,j,inner)
            stats['direct_full_gram_cases']+=1
    # All constructive windows distinct at small sizes, matching theoretical total.
    for N,k,q in [(3,1,3),(6,1,3),(6,2,3),(6,1,6),(9,1,3),(9,3,3)]:
        M=N//3;d=gcd(N,k)
        out=set()
        for ch in product(range(6),repeat=d):
            for scalars in product(range(q),repeat=M):
                g=construct(N,k,q,ch,scalars)
                assert direct_test(g,k,q)
                out.add(g)
        assert len(out)==6**d*q**M,(N,k,q,len(out))
        stats['constructive_bijection_cases']+=1
    print('CHECK_OK',dict(sorted(stats.items())))
if __name__=='__main__':main()
