"""Exact rational certificate for 19 closure components of s_{-3}."""
from fractions import Fraction as F
from itertools import product
from math import prod

PRIMES = (2,3,5,7)

def sieve(n):
    mark = [True]*(n+1)
    mark[0:2] = [False,False]
    for d in range(2,int(n**0.5)+1):
        if mark[d]:
            for m in range(d*d,n+1,d):
                mark[m]=False
    return [i for i in range(n+1) if mark[i]]

def local(p,a):
    t=F(1,p**3)
    return (1-(-t)**(a+1))/(1+t)

def exact_zeta_bound():
    # Euler sum plus integral test. The rounding is downward by construction.
    N=200000
    SCALE=10**20
    scaled=sum(SCALE//(n**3) for n in range(1,N+1))
    lower=F(scaled,SCALE)
    upper=F(scaled+N,SCALE)+F(1,2*N**2)
    # For each n, floor(SCALE/n^3)/SCALE <=1/n^3
    # < (floor(SCALE/n^3)+1)/SCALE; tail < 1/(2N^2).
    return lower,upper

def run():
    zzlo,zzhi=exact_zeta_bound()
    m=prod((1-F(1,p**3) for p in PRIMES),start=F(1))
    tlo=1/(zzhi*m)
    thi=1/(zzlo*m)
    assert F(998191,10**6) < tlo < thi < F(998192,10**6)
    # Tail from p>=11: for 11<=p<137, exact finite product
    plist=sieve(3*137)
    tested=[]
    for p in (q for q in plist if 11<=q<137):
        qs=[q for q in plist if p<q<=3*p]
        tail=prod((1-F(1,q**3) for q in qs),start=F(1))
        assert tail<1-F(1,p**3),(p,tail)
        tested.append(p)
    # For p>=137 Rosser-Schoenfeld bounds ensure >=13 primes in (p,2p]; 
    # nine suffice because (1-1/(8*p^3))^9 < 1-1/p^3.
    # Check second inequality for p>=137 by symbolic upper bound
    assert F(9,8)-F(36,64*137**3)>1
    assert (F(12,7)-F(125506,100000))*F(137,5)>12
    assert len(tested)>0 and tested[-1]==131
    # Finite prime-exponent states, with each local exponent in [0,4].
    f=[[local(p,k) for k in range(7)] for p in PRIMES]
    state_coeff={idx:prod((f[j][a] for j,a in enumerate(idx)),start=F(1))
        for idx in product(range(5),repeat=4)}
    coeff_sorted=sorted(set(state_coeff.values()))
    assert len(coeff_sorted)==625
    comps=[]
    start=coeff_sorted[0]
    prev=start
    overlap=0
    gaps=0
    for c in coeff_sorted[1:]:
        if c*tlo>prev:
            comps.append((start,prev))
            start=c
            gaps+=1
        else:
            assert c*thi<=prev, 'undecidable overlap for supplied interval enclosure'
            overlap+=1
        prev=c
    comps.append((start,prev))
    assert len(comps)==19 and gaps==18 and overlap==606
    assert comps[0][0]*tlo>=1/zzhi and comps[-1][1]==1
    # Every larger exponent a>=5 lies between f(5),f(6). Create
    # four-dimensional interval rectangles for a∈{0,1,2,3,4,>=5};
    # each rectangle times [T,1] must be swallowed by ONE known component.
    states=[]
    for j in range(4):
        v=[(f[j][k],f[j][k]) for k in range(5)]
        v.append((min(f[j][5],f[j][6]),max(f[j][5],f[j][6])))
        states.append(v)
    witness=[0]*len(comps)
    tail_cases=0
    min_margin=None
    for ix in product(range(6),repeat=4):
        low=prod((states[j][x][0] for j,x in enumerate(ix)),start=F(1))
        high=prod((states[j][x][1] for j,x in enumerate(ix)),start=F(1))
        containing=[i for i,(a,b) in enumerate(comps) if low>=a and high<=b]
        assert len(containing)>=1,(ix,low,high)
        witness[containing[0]]+=1
        if 5 in ix:
            tail_cases+=1
            margin=min(low-comps[containing[0]][0],comps[containing[0]][1]-high)
            if min_margin is None or margin<min_margin: min_margin=margin
    assert tail_cases==1296-625 and min_margin>0 and all(witness)
    # Selected exact endpoint labels (unique in finite state table).
    inverse={v:k for k,v in state_coeff.items()}
    endpoint_labels=[(inverse[a],inverse[b]) for a,b in comps]
    # Independent finite sample: evaluate the multiplicative function from n's factorization.
    # Each exact sample must lie in one of the proven interval enclosures.
    for n in range(1,3001):
        x=n
        v=F(1)
        for q in sieve(int(n**0.5)+1):
            if x%q==0:
                a=0
                while x%q==0:
                    x//=q
                    a+=1
                v*=local(q,a)
        if x>1:
            v*=local(x,1)
        assert any(a*tlo<=v<=b for a,b in comps),(n,v)
    print('VERIFY_OK')
    print('local_finite_prime_checks=',len(tested),'first_last=',tested[0],tested[-1])
    print('zeta_bounds_approx=',float(zzlo),float(zzhi),'tail_T_approx=',float(tlo),float(thi))
    print('finite_coefficients=',len(coeff_sorted),'overlap_links=',overlap,'gaps=',gaps)
    print('tail_rectangles=',tail_cases,'total_rectangles=1296')
    print('minimum_tail_containment_margin_approx=',float(min_margin))
    print('component_count=',len(comps))
    print('component_endpoint_exponents:')
    for i,(l,r) in enumerate(endpoint_labels,1):
        print(f'{i:02d}',l,r,'approximately',round(float(comps[i-1][0]*tlo),12),round(float(comps[i-1][1]),12))
    return comps, endpoint_labels

if __name__ == '__main__':
    run()
