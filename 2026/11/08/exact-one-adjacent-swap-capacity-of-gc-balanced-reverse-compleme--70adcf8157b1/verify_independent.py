"""Alternative exact search: multiset components and mask-based branch recursion.
No dependencies: python verify_independent.py
"""
import itertools
from functools import lru_cache

D = 'ACGT'
complement = {'A':'T','T':'A','C':'G','G':'C'}

def rc(x):
    return ''.join(complement[c] for c in x[::-1])

def outcomes(x):
    out = {x}
    for j in range(3):
        out.add(x[:j] + x[j+1] + x[j] + x[j+2:])
    return out

def solve(families):
    balls = [set().union(*(outcomes(w) for w in fam)) for fam in families]
    neighborhood = [0]*len(families)
    for i in range(len(families)):
        for j in range(i):
            if balls[i] & balls[j]:
                neighborhood[i] |= 1<<j
                neighborhood[j] |= 1<<i

    @lru_cache(None)
    def f(mask):
        if mask == 0:
            return 0, 1
        low = mask & -mask
        v = low.bit_length()-1
        a, count_a = f(mask ^ low)
        b, count_b = f((mask ^ low) & ~neighborhood[v])
        b += 1
        if a > b: return a, count_a
        if b > a: return b, count_b
        return a, count_a + count_b
    return f((1<<len(families))-1)

def main():
    words = [''.join(w) for w in itertools.product(D,repeat=4)
             if ''.join(w).count('G') + ''.join(w).count('C') == 2]
    grouped = {}
    for w in words:
        grouped.setdefault(''.join(sorted(w)),[]).append(w)
    assert len(grouped)==9
    independent_unrestricted = [solve([(w,) for w in values]) for values in grouped.values()]
    assert sum(v for v,_ in independent_unrestricted) == 25

    # Of all 44 two-strand pairs, remove any self-conflicting pair.
    orbits = set()
    for w in words:
        if w != rc(w):
            pair = tuple(sorted([w,rc(w)]))
            if not outcomes(pair[0]).intersection(outcomes(pair[1])):
                orbits.add(pair)
    assert len(orbits) == 40
    grouped_pairs = {}
    for pair in sorted(orbits):
        grouped_pairs.setdefault(tuple(sorted((''.join(sorted(x)) for x in pair))), []).append(pair)
    assert sorted(map(len,grouped_pairs.values())) == [4,6,6,12,12]
    separate = [solve(block) for block in grouped_pairs.values()]
    assert sorted((len(b),a,c) for b,(a,c) in zip(grouped_pairs.values(),separate)) == [
            (4,1,4),(6,2,3),(6,2,3),(12,3,12),(12,3,12)]
    assert sum(a for a,c in separate)==11
    count = 1
    for a,c in separate:count*=c
    assert count == 5184
    print('UNRESTRICTED_CARDINALITY',25)
    print('RC_CLOSED_NO_SELF_RC_CARDINALITY',22)
    print('EXACT_OPTIMAL_CODEBOOK_COUNT',count)
    print('ALTERNATIVE_COMPOSITION_DP_PASS')

if __name__=='__main__':main()
