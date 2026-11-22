"""Exact integer checks for five-branch two-field Potts ground energy on cubic bipartite triangle expansions.

The all-order theorem is proved by inequalities; these tests check the sharpness
constructions, incidence rules, and rational field witnesses on two nonisomorphic
finite cubic bipartite graphs and reject potential sign or normalization slips.
"""
from fractions import Fraction as F
from itertools import combinations
from random import Random

def bases():
    k33=[(i,3+j) for i in range(3) for j in range(3)]
    cube=[(u,v) for u in range(8) for bit in range(3) for v in [u^(1<<bit)] if u<v]
    return [('K33',6,k33,set(range(3)),lambda u,v:(u+(v-3))%3),
            ('cube',8,cube,{u for u in range(8) if u.bit_count()%2==0},lambda u,v:(u^v).bit_length()-1)]

L=[(0,1,2),(0,0,1),(0,0,1),(0,0,1),(0,0,0)]
R=[(1,2,0),(1,2,0),(1,1,0),(1,0,0),(0,0,0)]

def graph(n,edges):
    half=[(v,i) for i,(u,w) in enumerate(edges) for v in (u,w)]
    pos={z:i for i,z in enumerate(half)}
    out=[]
    for v in range(n):
        local=[pos[(v,i)] for i,(u,w) in enumerate(edges) if v in (u,w)]
        assert len(local)==3
        out+=list(combinations(local,2))
    for i,(u,v) in enumerate(edges):out.append((pos[(u,i)],pos[(v,i)]))
    assert len(out)==9*n//2
    return half,out

def calc(spin,ed):
    e=sum(spin[i]==spin[j] for i,j in ed)
    a=spin.count(0);b=spin.count(1);c=spin.count(2)
    return (e,a,b,c)

def branches(n,x,y):
    return [n*(-x+y),n*(F(1,2)-F(3,2)*x+F(1,2)*y), n*(1-F(3,2)*x),
            n*(F(3,2)-2*x),n*(F(9,2)-3*x)]

def check(n,ed,rec):
    e,a,b,c=rec
    assert a+b+c==3*n
    assert e>=0
    assert e-a>=-n
    assert 2*e-4*a>=-5*n
    assert 2*e-6*a>=-9*n
    assert e+c>=n
    assert 2*e-2*a+2*c>=-n

def main():
    total=0
    fields=[(F(1,4),F(1,4)),(F(5,4),F(1,4)),(F(1,4),F(7,4)),
            (F(7,4),F(5,4)),(F(4),F(1,4))]
    rng=Random(1127)
    for name,n,edges,left,color in bases():
        half,ed=graph(n,edges)
        assert all(len([i for i,(u,v) in enumerate(edges) if z in (u,v)])==3 for z in range(n))
        for phase in range(5):
            spins=[]
            for v,i in half:
                u,w=edges[i]
                j=color(u,w)
                assert j in (0,1,2)
                spins.append((L if v in left else R)[phase][j])
            got=calc(spins,ed)
            target=[(0,n,n,n),(n//2,3*n//2,n,n//2),(n,3*n//2,3*n//2,0),
                    (3*n//2,2*n,n,0),(9*n//2,3*n,0,0)][phase]
            assert got==target,(name,phase,got,target)
            check(n,ed,got)
            x,y=fields[phase]
            energy=got[0]-x*got[1]+y*got[3]
            bs=branches(n,x,y)
            assert energy==min(bs) and bs.count(min(bs))==1,(phase,bs)
            total+=1
        for _ in range(1500):
            s=[rng.randrange(3) for _ in half]
            e,a,b,c=calc(s,ed)
            check(n,ed,(e,a,b,c))
            x=F(rng.randrange(1,51),10);y=F(rng.randrange(1,51),10)
            assert e-x*a+y*c >= min(branches(n,x,y))
            total+=1
        print(f'{name}: {n} base sites, {len(half)} spins, {len(ed)} bonds, five sharp witnesses, 1500 random checks')
    print('TWO_FIELD_POTTS_UNIVERSAL_CHECKS_PASSED',total)
if __name__=='__main__':main()
