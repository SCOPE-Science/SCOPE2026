"""Finite checks for an orbital-pair classification (not a proof of its infinite form)."""
from itertools import product
from math import comb


def group_subgroups(periods):
    elements=list(product(*[range(p) for p in periods]))
    zero=tuple(0 for _ in periods)
    for mask in range(1<<len(elements)):
        if not (mask & (1<<elements.index(zero))):
            continue
        H=frozenset(x for i,x in enumerate(elements) if mask>>i&1)
        if all(tuple((x+y)%p for x,y,p in zip(a,b,periods)) in H
               for a in H for b in H):
            yield H


def model(periods,tails):
    elements=list(product(*(range(p+d) for p,d in zip(periods,tails))))
    identity=(0,)*len(periods)
    def multiply(a,b):
        c=[]
        for x,y,d,p in zip(a,b,tails,periods):
            s=x+y
            c.append(s if s<d+p else d+(s-d)%p)
        return tuple(c)
    return elements,identity,multiply


def exhaustive_orbital_pairs(periods,tails):
    V,one,multiply=model(periods,tails)
    pair_count=0; saturated_count=0
    observed=set()
    for mask in range(1<<len(V)):
        R=frozenset(x for i,x in enumerate(V) if (mask>>i)&1)
        if one not in R:continue
        if any((multiply(a,b) in R)!=(a in R and b in R)
               for a in V for b in V):
            continue
        saturated_count+=1
        elements=sorted(R)
        for fm in range(1<<len(elements)):
            F=frozenset(x for j,x in enumerate(elements) if (fm>>j)&1)
            if one not in F:continue
            if any(multiply(a,b) not in F for a in F for b in F):continue
            if any(a not in F for a in V for f in F if multiply(a,f) in F):
                continue
            if not all(any(multiply(a,b) in F for b in R) for a in R):
                continue
            observed.add((R,F))
    expected=set()
    r=len(periods)
    for mask in range(1<<r):
        I=[i for i in range(r) if (mask>>i)&1]
        R=frozenset(x for x in V if all(x[i]==0 for i in range(r) if i not in I))
        sub_periods=[periods[i] for i in I]
        for H in group_subgroups(sub_periods):
            F=frozenset(x for x in R if tuple(x[i]%periods[i] for i in I) in H)
            expected.add((R,F))
    assert observed==expected,('orbit classification failed',periods,tails,observed^expected)
    # Separately compare the defining quotient congruence with group-coset equality.
    for R,F in expected:
        I=[i for i in range(r) if any(x[i] for x in R)]
        ps=[periods[i] for i in I]
        residue=lambda x:tuple(x[i]%periods[i] for i in I)
        imageF={residue(f) for f in F}
        for a in R:
            for b in R:
                same_quotient=any(multiply(a,f)==multiply(b,g) for f in F for g in F)
                ra,rb=residue(a),residue(b)
                same_coset=tuple((x-y)%p for x,y,p in zip(ra,rb,ps)) in imageF
                assert same_quotient==same_coset,(periods,tails,R,F,a,b)
    assert saturated_count==2**r
    print(f'EXACT_ORBITS_OK periods={periods} tails={tails} nonzero={len(V)} orbital_pairs={len(observed)}')


def gaussian(n,k,q):
    top=1;bottom=1
    for i in range(k):
        top*=q**(n-i)-1
        bottom*=q**(k-i)-1
    assert top%bottom==0
    return top//bottom


def rank_counts(r,p):
    R=sum(comb(r,k)*sum(gaussian(k,j,p) for j in range(k+1)) for k in range(r+1))
    T=sum(comb(r,k)*sum((k-j)*gaussian(k,j,p) for j in range(k+1)) for k in range(r+1))
    assert 2*T==sum(k*comb(r,k)*sum(gaussian(k,j,p) for j in range(k+1)) for k in range(r+1))
    return R,T

if __name__=='__main__':
    cases=[([2],[1]),([2],[2]),([2,2],[1,1]),([2,2],[1,2]),([2,3],[1,1]),([3,3],[1,1])]
    for pp,dd in cases: exhaustive_orbital_pairs(pp,dd)
    assert rank_counts(2,2)==(10,7)
    assert rank_counts(2,3)==(11,8)
    assert rank_counts(3,2)==(38,42)
    assert rank_counts(3,3)==(53,63)
    print('GAUSSIAN_RANK_COUNTS_OK',[(p,r,rank_counts(r,p)) for p in (2,3) for r in (1,2,3,4)])
    print('MULTIGENERATOR_ORBITS_VERIFY_OK')
