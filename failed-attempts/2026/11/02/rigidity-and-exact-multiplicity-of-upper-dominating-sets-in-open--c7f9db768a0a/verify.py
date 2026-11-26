"""Independent finite checks for upper-dominating-set rigidity in open ladders.

Usage: python verify.py
Requires only Python standard library.
"""
from itertools import combinations


def closed_masks(n):
    a=[]
    for i in range(n):
        for row in (0,1):
            v=2*i+row
            neighbours=[v,2*i+1-row]
            if i>0: neighbours.append(2*(i-1)+row)
            if i<n-1: neighbours.append(2*(i+1)+row)
            a.append(sum(1<<w for w in neighbours))
    return a


def minimal_dominating(mask, neighbourhoods):
    # Independent definition; no column classification is used.
    if any(not (mask & neighbourhood) for neighbourhood in neighbourhoods):
        return False
    for v in range(len(neighbourhoods)):
        if not(mask>>v & 1): continue
        smaller=mask ^ (1<<v)
        if all(smaller & neighbourhood for neighbourhood in neighbourhoods):
            return False
    return True


def predicted(n):
    # Four singleton-in-each-rung patterns.
    patterns=[]
    for mode in ('top','bottom','alternating-top','alternating-bottom'):
        mask=0
        for col in range(n):
            if mode=='top':row=0
            elif mode=='bottom':row=1
            elif mode=='alternating-top':row=col%2
            else:row=1-col%2
            mask|=1<<(2*col+row)
        patterns.append(mask)
    # Exactly two full/empty column profiles for even n.
    if n%2==0:
        for lead in (0,1):
            mask=0
            for col in range(n):
                full=((col//2+col)%2)==lead  # paired opposites, unmatched equal
                # Equivalent strings 300330... / 033003...
                if full:mask|=3<<(2*col)
            patterns.append(mask)
    return set(patterns)


def reference_extremal(n):
    N=2*n; neigh=closed_masks(n)
    ans=set()
    for verts in combinations(range(N),n):
        mask=sum(1<<v for v in verts)
        if minimal_dominating(mask,neigh):ans.add(mask)
    return ans


def check():
    total=0
    for n in range(2,11):
        actual=reference_extremal(n)
        expected=predicted(n)
        assert actual==expected,(n,len(actual),len(expected),list(actual^expected)[:10])
        assert len(actual)==(6 if n%2==0 else 4)
        total+=len(actual)
    # Whole minimal-domination cardinality profile and known scalar totals.
    counts_expected=(2,6,7,18,39,75,155,310,638)
    subset_count=0
    for n in range(1,10):
        neigh=closed_masks(n)
        got=sum(minimal_dominating(mask,neigh) for mask in range(1<<(2*n)))
        assert got==counts_expected[n-1],(n,got,counts_expected[n-1])
        subset_count+=1<<(2*n)
    for n in range(11,101):
        # The six or four described words are feasible in arbitrarily long test examples.
        neigh=closed_masks(n)
        for mask in predicted(n):
            assert mask.bit_count()==n
            assert minimal_dominating(mask,neigh)
    print(f'VERIFY_OK extremal_lengths=2..10 distinct_sets={total} '\
          f'direct_all_subset_lengths=1..9 examined={subset_count} constructions=11..100')

if __name__=='__main__':check()
