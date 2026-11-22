"""Independent finite checks for even-dimensional folded cubes, standard library only.
Run: python3 verify_walsh.py
Checks exact adjacency spectra, all predicted critical states, and two-point covariances.
Finite tests are not a substitute for the all-dimensional proof.
"""
from itertools import combinations, product
from fractions import Fraction
from math import comb

def hamming(x): return x.bit_count()

def test(n):
    N=1<<n
    neighbor=[tuple(x^(1<<j) for j in range(n))+(x^(N-1),) for x in range(N)]
    spectrum={}
    for mask in range(N):
        vec=[(-1)**hamming(x&mask) for x in range(N)]
        lam=n-2*hamming(mask)+(-1)**hamming(mask)
        assert all(sum(vec[z] for z in neighbor[x])==lam*vec[x] for x in range(N))
        spectrum[mask]=lam
    mineig=1-n
    assert [k for k,v in spectrum.items() if v==mineig]==[k for k in range(N) if hamming(k)>=n-1]
    modes=[tuple((-1)**hamming(x&k) for x in range(N)) for k in spectrum if spectrum[k]==mineig]
    d=n+1
    states={tuple(0 for _ in range(N))}
    for p in modes:
        for z in (-1,1):states.add(tuple(z*q for q in p))
    for i,j in combinations(range(d),2):
        for ai,aj in product((-1,1),repeat=2):
            p,q=modes[i],modes[j]
            f=tuple((ai*p[x]+aj*q[x])//2 for x in range(N))
            assert all(ai*p[x]+aj*q[x] in (-2,0,2) for x in range(N))
            states.add(f)
    assert len(states)==1+2*d*d
    cnt={0:0,N//2:0,N:0}
    for s in states:
        K=sum(z*z for z in s)
        cnt[K]+=1
        assert all(z in (-1,0,1) for z in s)
        edge=sum(s[x]*s[y] for x in range(N) for y in neighbor[x])//2
        assert 2*edge+(n-1)*K==0
    assert cnt=={0:1,N//2:2*d*(d-1),N:2*d}
    for dist in range(n+1):
        y=(1<<dist)-1
        cov=sum(s[0]*s[y] for s in states)
        want=Fraction((n+2)*((-1)**dist)*(n+1-2*dist),1+2*(n+1)**2)
        assert Fraction(cov,len(states))==want, (n,dist,cov,want)
    # Independent count of all possible ternary affine functions with half-integral coefficients.
    if n<=6:
        found=set()
        for coeff in product(range(-2,3),repeat=n+1):
            if not any(coeff): found.add(tuple(0 for _ in range(N)));continue
            # g(x)=(coeff[0]+sum coeff[i+1]*(-1)^x_i)/2
            values=tuple((coeff[0]+sum(coeff[j+1]*(1 if not (x>>j)&1 else -1) for j in range(n))) for x in range(N))
            if all(v in (-2,0,2) for v in values):
                found.add(tuple((values[x]//2)*((-1)**hamming(x)) for x in range(N)))
        assert found==states
    print(f'PASS folded_dim={n} vertices={N} min_eigen={mineig} min_mult={d} critical_states={len(states)} full={cnt[N]} half={cnt[N//2]} empty={cnt[0]} correlation_distances={n+1}')

if __name__=='__main__':
    for n in (4,6,8):test(n)
