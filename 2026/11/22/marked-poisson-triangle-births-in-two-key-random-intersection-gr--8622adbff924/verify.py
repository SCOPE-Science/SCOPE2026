"""Finite combinatorial and quantitative checks for triangle births in two-key random intersection graphs."""
from itertools import combinations,product
from collections import Counter
from math import comb,exp,factorial

def triangles(edges):
    n=len(edges); out=[]
    for i,j,k in combinations(range(n),3):
        a,b,c=edges[i],edges[j],edges[k]
        if a&b and b&c and a&c:
            shared=a&b&c
            out.append(((i,j,k),shared))
    return out

# Exact classification: every triangle of 2-subsets is a 3-star or a three-key cycle.
checked=0
for m in range(3,7):
    pool=[frozenset(e) for e in combinations(range(m),2)]
    for e in product(pool,repeat=3):
        t=triangles(e)
        if t:
            a,b,c=e
            if not (a&b&c):
                assert len(set(e))==3
                assert len(a|b|c)==3
            else:
                assert any(x in a&b&c for x in range(m))
        checked+=1
print('triangle classification exact triples:',checked)

# At n=3: exact expectation from star witnesses plus cycle exceptions and double stars.
for m in range(3,8):
    pool=[frozenset(e) for e in combinations(range(m),2)]
    total=sum(bool(triangles(e)) for e in product(pool,repeat=3))
    N=comb(m,2)
    star=m*(2/m)**3
    cycle=6*comb(m,3)/N**3
    double_star=1/N**2
    assert abs(total/N**3-(star+cycle-double_star)) < 1e-14
    print('m',m,'P(triangle)',total/N**3,'star/cycle/double',star,cycle,double_star)

# Exact process-to-third-hit identity on every clean finite configuration.
# Clean means: no four appearances of a key; no cyclic triangle with empty
# three-way intersection; no triangle witnessed by two shared keys.
process_cases=0
for m in (3,4,5):
    pool=[frozenset(e) for e in combinations(range(m),2)]
    for edges in product(pool,repeat=4):
        counts=Counter(k for e in edges for k in e)
        tris=triangles(edges)
        clean=(max(counts.values())<=3 and
               all(len(shared)==1 for _,shared in tris))
        if clean:
            assert len(tris)==sum(v==3 for v in counts.values())
            # The ordered triangle process has the same arrival indices.
            graph_jumps=Counter(max(indices)+1 for indices,_ in tris)
            key_jumps=Counter()
            hit=Counter()
            for i,e in enumerate(edges,1):
                for key in e:
                    hit[key]+=1
                    if hit[key]==3: key_jumps[i]+=1
            assert graph_jumps==key_jumps
        process_cases+=1
print('exact four-vertex process cases:',process_cases)

# Probability the initial n sample keys hit count >=3, approximate first-triangle law.
from random import Random
rng=Random(330917)
for m in (300,1000,3000):
    n=round(m**(2/3)); trials=2500
    zero=0; k3=0; k4=0
    for _ in range(trials):
        counts=[0]*m
        for __ in range(n):
            a=rng.randrange(m); b=rng.randrange(m-1)
            if b>=a:b+=1
            counts[a]+=1;counts[b]+=1
        births=sum(v>=3 for v in counts)
        zero+= (births==0); k3+=births
        k4+=any(v>=4 for v in counts)
    print('m',m,'n',n,'Pr(zero 3-hit)',zero/trials,'target',exp(-4*n**3/(3*m*m)),'mean births',k3/trials,'target mean',4*n**3/(3*m*m),'Pr(4-hit)',k4/trials)
print('PASS')
