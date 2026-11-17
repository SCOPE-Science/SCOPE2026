#!/usr/bin/env python3
"""Independent finite checks for cycle-to-folded-cube polyhedral graph-Hom cells.
No third-party dependencies. Run: python3 verify_folded_hom.py
"""
import itertools, math, random
from collections import Counter

def join_basis(n):
    # folded n-cube in F_2^(n-1): basis plus all-ones vector
    return tuple([1<<i for i in range(n-1)] + [(1<<(n-1))-1])

def neighbor(x,y,gen):
    return (x^y) in gen

def maps(n):
    gen=join_basis(n)
    for start in range(1<<(n-1)):
        for perm in itertools.permutations(range(n)):
            vs=[start]
            for p in perm[:-1]:
                vs.append(vs[-1]^gen[p])
            yield vs,perm

def independent_subsets(n):
    return [tuple(i for i in range(n) if (bits>>i)&1)
            for bits in range(1<<n) if all(not ((bits>>i)&1 and (bits>>((i+1)%n))&1) for i in range(n))]

def map_flipped(vs,gen,I):
    n=len(vs)
    v=vs[:]
    for i in I:
        v[i]=vs[(i-1)%n]^vs[i]^vs[(i+1)%n]
    return v

def full_cube_vertices(vs,gen,I):
    choices=[]
    alt=map_flipped(vs,gen,I)
    for i in range(len(vs)):
        choices.append((vs[i],alt[i]) if i in I else (vs[i],))
    return choices

def hom_cell(choices,gen):
    n=len(choices)
    return all(neighbor(a,b,gen)
               for i in range(n) for a in choices[i] for b in choices[(i+1)%n])

def gf2rank(vectors):
    basis={}
    for v in vectors:
        while v:
            i=v.bit_length()-1
            if i in basis: v ^= basis[i]
            else: basis[i]=v;break
    return len(basis)

def link_betti(n):
    faces=[tuple(I) for I in independent_subsets(n)]
    dims=Counter(len(I)-1 for I in faces)
    rs={}
    for k in range(1,max(dims)+2):
        lower={I:i for i,I in enumerate(I for I in faces if len(I)==k)}
        # boundary C_k --> C_{k-1}; face cardinality k+1
        dom=[I for I in faces if len(I)==k+1]
        rs[k]=gf2rank([sum(1<<lower[I[:j]+I[j+1:]] for j in range(len(I))) for I in dom])
    return {i:dims[i]-rs.get(i,0)-rs.get(i+1,0)-(1 if i==0 else 0) for i in range(max(dims)+1)}

def theoretical_matching(n,d):
    return n*math.comb(n-d,d)//(n-d)

def test(n,exhaust=False):
    gen=join_basis(n)
    Is=independent_subsets(n)
    print('n=',n,'generators=',gen,'link faces=',Counter(len(I) for I in Is))
    assert len(gen)==len(set(gen))
    assert all((a^b) not in gen for a,b in itertools.combinations(gen,2))
    for d in range((n-1)//2+1):
        assert sum(len(I)==d for I in Is)==theoretical_matching(n,d)
    N=(1<<(n-1))*math.factorial(n)
    f=[N*theoretical_matching(n,d)//(1<<d) for d in range((n-1)//2+1)]
    chi=sum((-1)**i*v for i,v in enumerate(f))
    predicted=round(N*2**(1-n/2)*math.cos(n*math.pi/4))
    assert chi==predicted
    print('vertex total',N,'cell counts',f,'Euler',chi,'formula',predicted)
    tested=0
    rng=random.Random(20261113+n)
    for vs,perm in maps(n):
        if not exhaust and rng.randrange(50000)!=0: continue
        assert all(neighbor(vs[i],vs[(i+1)%n],gen) for i in range(n))
        for i in range(n):
            a,b=vs[(i-1)%n],vs[(i+1)%n]
            common={z for z in range(1<<(n-1)) if neighbor(a,z,gen) and neighbor(z,b,gen)}
            assert common=={vs[i],vs[(i-1)%n]^vs[i]^vs[(i+1)%n]}, (n,vs,i,common)
        # Every independent swap set is a legal cube. Conversely every subset of
        # vertex-alternatives describes a cube iff it is independent in C_n.
        all_legal={I for I in (tuple(i for i in range(n) if bits>>i&1) for bits in range(1<<n))
                   if hom_cell(full_cube_vertices(vs,gen,I),gen)}
        assert all_legal==set(Is),(n,vs,all_legal,set(Is))
        tested+=1
    print('complete-vertex checks',tested, 'exhaustive',exhaust)
    if exhaust: assert tested==N
    else: assert tested>1
    return f

if __name__=='__main__':
    assert test(5,True)==[1920,4800,2400]
    assert test(7,False)==[322560,1128960,1128960,282240]
    for n,expected in [(5,{0:0,1:1}),(7,{0:0,1:1,2:0}),(9,{0:0,1:0,2:2,3:0})]:
        got=link_betti(n)
        print('link mod2 Betti',n,got)
        assert got==expected
    print('ALL CHECKS PASSED')
