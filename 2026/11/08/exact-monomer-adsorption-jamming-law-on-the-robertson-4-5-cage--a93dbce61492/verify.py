"""Exact monomer RSA on the Robertson graph; standard-library-only replay.

Two independent rational calculations:
(1) deletion of the first eligible arrival (memoized recurrence);
(2) integration over arrival-time simplices for every maximal independent set.
The 19 entries below are the published LCF presentation.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import permutations

LCF=(8,4,7,4,8,5,7,4,7,8,4,5,7,8,4,8,4,8,4)
N=len(LCF)
ADJ=[0]*N
for i,s in enumerate(LCF):
    for j in ((i+1)%N,(i-1)%N,(i+s)%N):
        ADJ[i]|=1<<j
        ADJ[j]|=1<<i
CLOSED=[(1<<i)|ADJ[i] for i in range(N)]
FULL=(1<<N)-1
ORBIT_12=(0,2,3,5,6,8,10,11,13,15,16,18)
ORBIT_3=(1,7,14)
ORBIT_4=(4,9,12,17)
GENERATOR_12=(10,14,15,16,17,18,0,1,5,4,3,2,9,8,7,6,13,12,11)
GENERATOR_2=(0,1,16,15,4,5,10,14,18,17,6,13,12,11,7,3,2,9,8)
EXPECTED_LAW={5:Fraction(92833,1256850),6:Fraction(520381,628425),7:Fraction(913,9310)}
EXPECTED_SITES={0:Fraction(1919129,6032880),1:Fraction(31441,99225),4:Fraction(3157883,10054800)}


def vertices(mask):
    while mask:
        bit=mask&-mask
        yield bit.bit_length()-1
        mask-=bit


@lru_cache(None)
def first_eligible_law(mask):
    if mask==0:
        return (Fraction(1),)
    size=mask.bit_count()
    result=[Fraction(0)]*(size+1)
    for v in vertices(mask):
        sub=first_eligible_law(mask&~CLOSED[v])
        for k,weight in enumerate(sub):
            result[k+1]+=weight/size
    while result and result[-1]==0:
        result.pop()
    return tuple(result)


@lru_cache(None)
def first_eligible_site(mask,target):
    if not (mask>>target)&1:
        return Fraction(0)
    size=mask.bit_count()
    total=Fraction(1,size)
    for v in vertices(mask&~(1<<target)):
        if not (CLOSED[v]>>target)&1:
            total+=first_eligible_site(mask&~CLOSED[v],target)/size
    return total


def independent(mask):
    return all((ADJ[v]&mask)==0 for v in vertices(mask))


def maximal(mask):
    return all(bool(CLOSED[v]&mask) for v in range(N))


def integrate_target_set(mask):
    """Integrate its necessary and sufficient predecessor constraints."""
    chosen=tuple(vertices(mask))
    other=tuple(vertices(FULL&~mask))
    size=len(chosen)
    total=Fraction(0)
    for order in permutations(chosen):
        rank={v:j for j,v in enumerate(order)}
        c=[0]*size
        for w in other:
            j=min(rank[v] for v in chosen if ADJ[w]&(1<<v))
            c[j]+=1
        suffix=0
        denom=1
        for j in range(size-1,-1,-1):
            suffix+=c[j]
            denom*=suffix+size-j
        total+=Fraction(1,denom)
    return total


def compose(a,b):
    return tuple(a[b[v]] for v in range(N))


def generated_group(gens):
    identity=tuple(range(N))
    known={identity}
    frontier=[identity]
    while frontier:
        a=frontier.pop()
        for g in gens:
            b=compose(a,g)
            if b not in known:
                known.add(b)
                frontier.append(b)
    return known


def count_short_cycles_at(v,length):
    def dfs(path):
        if len(path)==length:
            return int(bool(ADJ[path[-1]]&(1<<v)))
        return sum(dfs(path+(w,)) for w in vertices(ADJ[path[-1]]) if w not in path)
    return dfs((v,))//2


def main():
    assert N==19 and sum(x.bit_count() for x in ADJ)//2==38
    assert all(x.bit_count()==4 for x in ADJ)
    assert all(bool(ADJ[u]&(1<<v))==bool(ADJ[v]&(1<<u)) for u in range(N) for v in range(N))
    assert all(count_short_cycles_at(v,3)==0 and count_short_cycles_at(v,4)==0 for v in range(N))
    assert sum(count_short_cycles_at(v,5) for v in range(N))>0

    generators=(GENERATOR_12,GENERATOR_2)
    for p in generators:
        assert sorted(p)==list(range(N))
        assert all(bool(ADJ[u]&(1<<v))==bool(ADJ[p[u]]&(1<<p[v])) for u in range(N) for v in range(N))
    group=generated_group(generators)
    assert len(group)==24
    computed_orbits={frozenset(p[v] for p in group) for v in range(N)}
    assert computed_orbits=={frozenset(ORBIT_12),frozenset(ORBIT_3),frozenset(ORBIT_4)}
    # Distinct six-cycle counts forbid any automorphism mixing the three classes.
    assert {v:count_short_cycles_at(v,6) for v in (0,1,4)}=={0:33,1:32,4:30}
    assert all(count_short_cycles_at(v,6)==33 for v in ORBIT_12)
    assert all(count_short_cycles_at(v,6)==32 for v in ORBIT_3)
    assert all(count_short_cycles_at(v,6)==30 for v in ORBIT_4)

    law1=first_eligible_law(FULL)
    p1={k:weight for k,weight in enumerate(law1) if weight}
    assert p1==EXPECTED_LAW
    site1=[first_eligible_site(FULL,v) for v in range(N)]
    for O,rep in ((ORBIT_12,0),(ORBIT_3,1),(ORBIT_4,4)):
        assert all(site1[v]==EXPECTED_SITES[rep] for v in O)

    # Independent exact calculation: enumerate ALL independent dominating sets,
    # and integrate the exact inequalities imposed by their occupied neighbors.
    sets=[]
    for mask in range(1<<N):
        if independent(mask) and maximal(mask):
            sets.append(mask)
    assert Counter(mask.bit_count() for mask in sets)=={5:24,6:111,7:4}
    law2=defaultdict(Fraction)
    site2=[Fraction(0)]*N
    for mask in sets:
        p=integrate_target_set(mask)
        law2[mask.bit_count()]+=p
        for v in vertices(mask):
            site2[v]+=p
    assert dict(law2)==p1
    assert site2==site1
    assert sum(law2.values())==1
    mean=sum(k*p for k,p in law2.items())
    assert mean==Fraction(540823,89775)
    assert mean/19==Fraction(540823,1705725)
    assert site1[4]<site1[1]<site1[0]
    assert mean==sum(site1)
    print('Robertson graph: 19 vertices; 38 edges; 4-regular; girth 5.')
    print('Exact automorphism orbits (sizes):',sorted(map(len,computed_orbits)))
    print('Independent maximal sets by size:',dict(sorted(Counter(mask.bit_count() for mask in sets).items())))
    print('Jamming law:',[(k,str(p)) for k,p in sorted(law2.items())])
    print('Site probabilities for orbit representatives:',{k:str(site1[k]) for k in (0,1,4)})
    print('Expected number:',str(mean),'Mean density:',str(mean/19))
    print('Two independent exact methods agree on distribution and all nineteen sites.')


if __name__=='__main__':
    main()
