"""Reproducible independent checks for minimal edge domination of once-subdivided bicliques.
Run: python verify.py (Python 3.9+, standard library only)."""
from collections import Counter
from itertools import combinations, product
from math import comb

def predicted(m,n):
    result=Counter()
    for k in range(1,m+1):
        result[m+(n-1)*k]+=comb(m,k)*n**(m-k)
    for k in range(1,n+1):
        result[n+(m-1)*k]+=comb(n,k)*m**(n-k)
    result[m+n]+=n**m*m**n-m*n**m-n*m**n+m*n
    return +result

def build(m,n):
    # Indices 2*(i*n+j) and 2*(i*n+j)+1: incidences at A_i and B_j.
    edges=[]
    for i in range(m):
        for j in range(n):
            s=m+n+i*n+j
            edges.extend(((i,s),(m+j,s)))
    masks=[]
    for e in edges:
        masks.append(sum(1<<k for k,f in enumerate(edges) if set(e)&set(f)))
    return edges,masks

def is_minimal(mask,covers):
    full=(1<<len(covers))-1
    taken=[i for i in range(len(covers)) if mask>>i&1]
    cov=0
    for i in taken:cov|=covers[i]
    if cov!=full:return False
    for discarded in taken:
        cov=0
        for i in taken:
            if i!=discarded:cov|=covers[i]
        if cov==full:return False
    return True

def exact(m,n):
    _,covers=build(m,n)
    result=set()
    for mask in range(1<<len(covers)):
        if is_minimal(mask,covers):result.add(mask)
    return result

def generate(m,n):
    configurations=set()
    # Inactive vertices within A.
    for k in range(1,m+1):
        for I in combinations(range(m),k):
            I=set(I)
            forced=sum(1<<(2*(i*n+j)+1) for i in I for j in range(n))
            active=[i for i in range(m) if i not in I]
            for choices in product(range(n),repeat=len(active)):
                mask=forced
                for i,j in zip(active,choices):mask|=1<<(2*(i*n+j))
                configurations.add(mask)
    # Inactive vertices within B.
    for k in range(1,n+1):
        for J in combinations(range(n),k):
            J=set(J)
            forced=sum(1<<(2*(i*n+j)) for i in range(m) for j in J)
            active=[j for j in range(n) if j not in J]
            for choices in product(range(m),repeat=len(active)):
                mask=forced
                for j,i in zip(active,choices):mask|=1<<(2*(i*n+j)+1)
                configurations.add(mask)
    # No inactive vertices: one outgoing incidence for each old vertex.
    for choicesA in product(range(n),repeat=m):
        if len(set(choicesA))==1:continue
        first=sum(1<<(2*(i*n+j)) for i,j in enumerate(choicesA))
        for choicesB in product(range(m),repeat=n):
            if len(set(choicesB))==1:continue
            mask=first
            for j,i in enumerate(choicesB):mask|=1<<(2*(i*n+j)+1)
            configurations.add(mask)
    return configurations

def check():
    exhaustive_cases=[(1,1),(1,2),(1,3),(1,4),(1,5),(2,2),(2,3),(2,4),(3,2),(3,3),(4,2)]
    subset_total=0
    minimal_total=0
    for m,n in exhaustive_cases:
        found=exact(m,n)
        expected=generate(m,n)
        assert found==expected,(m,n,'families',len(found),len(expected))
        count=Counter(x.bit_count() for x in found)
        assert count==predicted(m,n),(m,n,count,predicted(m,n))
        subset_total+=1<<(2*m*n)
        minimal_total+=len(found)
    other_cases=[(3,4),(4,3),(4,4),(3,5),(5,3),(2,6),(6,2)]
    checked_generated=0
    for m,n in other_cases:
        fam=generate(m,n)
        count=Counter(x.bit_count() for x in fam)
        assert count==predicted(m,n),(m,n,count,predicted(m,n))
        _,covers=build(m,n)
        assert all(is_minimal(x,covers) for x in fam),(m,n,'nonminimal generated')
        checked_generated+=len(fam)
    # Gap statement: for m,n >=3 no cardinality in [mn-s+2,mn-1], s=min(m,n).
    for m in range(3,15):
        for n in range(3,15):
            support=set(predicted(m,n))
            assert min(support)==m+n-1
            assert max(support)==m*n
            assert not (support & set(range(m*n-min(m,n)+2,m*n)))
            assert m*n-min(m,n)+1 in support
    for n in range(1,20):
        assert predicted(1,n)==Counter({n:2**n})
    print('VERIFY_OK exact_cases=%d exhaustive_subsets=%d exact_minimal_sets=%d additional_cases=%d generated_tested=%d all_coefficients=PASS all_families=PASS upper_gaps=PASS stars=PASS' % (len(exhaustive_cases),subset_total,minimal_total,len(other_cases),checked_generated))

if __name__=='__main__':check()
