"""Standalone arithmetic verifier for neighbor-sum dynamics on incidence graphs of complete triple systems.
Run: python3 check_hypergraph_xor.py. Uses only Python standard library.
"""
import itertools
import math
import random

def adjacency(n):
    triples=list(itertools.combinations(range(n),3))
    N=n+len(triples)
    rows=[0]*N
    for j,t in enumerate(triples):
        for i in t:
            rows[i] ^= 1 << (n+j)
            rows[n+j] ^= 1 << i
    return rows

def matmul(A,B):
    out=[]
    for a in A:
        x=0
        while a:
            z=a & -a
            x ^= B[z.bit_length()-1]
            a-=z
        out.append(x)
    return out

def rank(A):
    piv={}
    for a in A:
        while a:
            i=a.bit_length()-1
            if i not in piv:
                piv[i]=a
                break
            a^=piv[i]
    return len(piv)

def apply(rows,x):
    out=0
    for i,r in enumerate(rows):
        if (r & x).bit_count() & 1:
            out |= 1<<i
    return out

def expected(n):
    m=math.comb(n,3); N=n+m; z=N-3*n
    if n%4==0:
        return [N,2*n,2*n,2*n,2*n], {'recurrent':2*n,'nilpotent':{1:m-n},'one_eigenswap':n,'first_entry_exp':[2*n,N]}
    if n%4==1:
        return [N,2*n,2*n-1,2*n-2,2*n-2], {'recurrent':2*n-2,'nilpotent':{1:m-n-1,3:1},'one_eigenswap':n-1,'first_entry_exp':[2*n-2,N-2,N-1,N]}
    if n%4==2:
        return [N,2*n,n,0,0], {'recurrent':0,'nilpotent':{1:m-2*n,3:n},'one_eigenswap':0,'first_entry_exp':[0,N-2*n,N-n,N]}
    return [N,2*n,n+1,2,2], {'recurrent':2,'nilpotent':{1:m-2*n+1,3:n-1},'one_eigenswap':1,'first_entry_exp':[2,N-2*n+2,N-n+1,N]}

# Rational canonical data verified by ranks of A^k (not by a separately coded symbolic congruence assertion).
for n in range(4,17):
    A=adjacency(n); N=len(A)
    e,info=expected(n)
    powers=[[(1<<i) for i in range(N)],A]
    for k in range(2,5):powers.append(matmul(powers[-1],A))
    rr=list(map(rank,powers))
    assert rr==e,(n,rr,e)
    r=info['recurrent']
    assert info['first_entry_exp']==[N-z+r for z in rr[:len(info['first_entry_exp'])]],(n,rr,info['first_entry_exp'])
    assert sum(s*k for k,s in info['nilpotent'].items())+info['recurrent']==N
    if n%4==0: assert powers[3]==powers[1]
    elif n%4 in (1,3):
        assert matmul(powers[4],A)==powers[3]
        assert powers[4]!=powers[2]
    else: assert powers[3]==[0]*N and powers[2]!=[0]*N
    print('RANK_AND_POLYNOMIAL',n,N,rr,'PASS')

# Independent direct state propagation, not using rank calculations.
for n in (4,5):
    A=adjacency(n); N=len(A); m=math.comb(n,3)
    info=expected(n)[1]
    population={}; period_counts={}
    for x in range(1<<N):
        seen={};y=x;t=0
        while y not in seen:
            seen[y]=t
            y=apply(A,y);t+=1
            assert t<=10
        entry=seen[y];p=t-entry
        assert p in (1,2)
        population[entry]=population.get(entry,0)+1
        if entry==0:period_counts[p]=period_counts.get(p,0)+1
    assert sum(population.values())==1<<N
    exp=info['first_entry_exp']
    cumulative=0
    for d,dim in enumerate(exp):
        cumulative+=population.get(d,0)
        assert cumulative==2**dim,(n,d,cumulative,2**dim)
    assert period_counts[1]==2**info['one_eigenswap'],(n,period_counts,info)
    assert period_counts.get(2,0)==2**info['recurrent']-period_counts[1]
    print('EXHAUSTIVE',n,2**N,'first_entry',population,'periodic_state_periods',period_counts,'PASS')

# Monte Carlo testing of all four residue cases across independent direct trajectories.
rng=random.Random(20261119)
for n in (6,7,8,9,10,11,12):
    A=adjacency(n);info=expected(n)[1]
    d=len(info['first_entry_exp'])-1
    for _ in range(256):
        y=rng.getrandbits(len(A))
        for _ in range(d): y=apply(A,y)
        z=apply(A,y)
        assert apply(A,z)==y,(n,'not 2-periodic')
        if info['recurrent']==0: assert y==0
    print('DIRECT_SAMPLE',n,256,'PASS')
print('ALL_CHECKS_PASS')
