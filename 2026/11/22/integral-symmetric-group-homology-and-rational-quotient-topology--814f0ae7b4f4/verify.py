"""Exact finite checks for oriented homology of partial-partition complexes.

Standard library only. A face is a collection of pairwise disjoint nonempty
subsets of the labelled ground set; its orientation is the increasing order
of their binary masks. Empty face has dimension -1.
"""
from functools import lru_cache
from itertools import permutations
from collections import Counter
from math import factorial


def parity_to_sort(seq):
    return -1 if sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i+1, len(seq)))%2 else 1


def part_types(n):
    def rec(rem, minval):
        if rem==0:
            yield ()
        for p in range(minval,rem+1):
            for tail in rec(rem-p,p):
                yield (p,)+tail
    return list(rec(n,1))


def permutations_for_cycle_type(typ):
    perm=[]; a=0
    for k in typ:
        perm += list(range(a+1,a+k))+[a]
        a+=k
    return tuple(perm)


def mask_image(mask,perm):
    return sum(1<<perm[i] for i in range(len(perm)) if mask>>i&1)


def all_faces(n):
    # Build each partial partition exactly once by choosing the least unused
    # label and either leaving it unused or placing it with a subset of later
    # unused labels into its block.
    @lru_cache(None)
    def rec(remaining):
        if remaining==0:
            return ((),)
        v=remaining & -remaining; others=remaining^v
        result=list(rec(others))
        sub=others
        while True:
            block=v|sub
            for tail in rec(others^sub):
                result.append(tuple(sorted((block,)+tail)))
            if sub==0:
                break
            sub=(sub-1)&others
        return tuple(result)
    return rec((1<<n)-1)


def partitions_full_nonsingleton(n):
    return [f for f in all_faces(n) if f and (sum(x.bit_count() for x in f)==n)
            and min(x.bit_count() for x in f)>=2]


def boundary(chain):
    ans=Counter()
    for face, coeff in chain.items():
        for i in range(len(face)):
            ans[face[:i]+face[i+1:]]+=(-1)**i*coeff
    return {f:c for f,c in ans.items() if c}


def crosspolytope_cycle(f):
    chain={():1}
    for b in f:
        one=b&-b
        temp=Counter()
        for a,coef in chain.items():
            for vert,sgn in ((b,1),(one,-1)):
                unsorted=a+(vert,)
                temp[tuple(sorted(unsorted))]+=coef*sgn*parity_to_sort(unsorted)
        chain={a:c for a,c in temp.items() if c}
    return chain


def action_character(perm, f):
    # oriented signed fixed top facets
    if set(mask_image(b,perm) for b in f)!=set(f):
        return 0
    return parity_to_sort([mask_image(b,perm) for b in f])


def reduced_lefschetz(perm,faces):
    tr=-1 # augmented empty chain in degree -1
    for f in faces:
        if not f: continue
        images=[mask_image(b,perm) for b in f]
        if set(images)==set(f):
            tr+=((-1)**(len(f)-1))*parity_to_sort(images)
    return tr


def homology_lefschetz(perm,full):
    return sum(((-1)**(len(f)-1))*action_character(perm,f) for f in full)


def strict_partition_counts(n):
    return Counter(len(t) for t in part_types(n) if t and min(t)>=2 and len(set(t))==len(t))


def test():
    print('PARTIAL-PARTITION EQUIVARIANT HOMOLOGY: INTEGER VERIFICATION')
    print('Checks use direct enumerations of distinct combinatorial faces,')
    print('integer oriented simplicial boundary, and independent Lefschetz traces.')
    for n in range(2,8):
        faces=all_faces(n)
        assert len(set(faces))==len(faces)
        F=partitions_full_nonsingleton(n)
        assert len(set(F))==len(F)
        assert len(F)==sum(1 for f in faces if f and sum(x.bit_count() for x in f)==n and all(x.bit_count()>=2 for x in f))
        # Cycles with unit coefficient on their unique fully covering
        # non-singleton face; all other such coordinates zero.
        for f in F:
            z=crosspolytope_cycle(f)
            assert not boundary(z), (n,f,'nonzero boundary')
            assert z.get(f)==1, (n,f,'not primitive')
            assert all(z.get(other,0)==0 for other in F if other!=f)
        for typ in part_types(n):
            p=permutations_for_cycle_type(typ)
            direct=reduced_lefschetz(p,faces)
            predicted=homology_lefschetz(p,F)
            assert direct==predicted,(n,typ,direct,predicted)
        # For each orbit of non-singleton partitions under S_n, a rational
        # invariant line exists iff its distinct block sizes avoid repeats.
        grouped=Counter(tuple(sorted(x.bit_count() for x in f)) for f in F)
        predicted=strict_partition_counts(n)
        invariants=Counter(len(t) for t in grouped if len(set(t))==len(t))
        assert predicted==invariants,(n,predicted,invariants)
        print('n=%d faces=%d non-singleton-full=%d cycle_boundaries=0 cycle_coordinates=identity conjugacy_types=%d rational_quotient_betti=%s' % (n,len(faces),len(F),len(part_types(n)),dict(sorted(invariants.items()))))
    print('n=4 transposition and four-cycle degree-one characters:')
    F=partitions_full_nonsingleton(4)
    for name,p in [('transposition',(1,0,2,3)),('double_transposition',(1,0,3,2)),('four_cycle',(1,2,3,0))]:
        print(name, sum(action_character(p,f) for f in F if len(f)==2))
    print('ALL CHECKS PASSED')

if __name__=='__main__':
    test()
