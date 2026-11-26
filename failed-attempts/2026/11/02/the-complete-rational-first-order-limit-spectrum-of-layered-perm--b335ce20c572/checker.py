"""Finite, independent tests of a first-order limiting probability construction.

The exhaustive checks are not a proof of the all-denominator theorem.
"""
from itertools import product, permutations
from fractions import Fraction


def patterns(b):
    assert b >= 1
    t = max(1, (b - 1).bit_length())
    L = t + 3
    words = ['0' * L + '1' + format(i, '0%db' % t) + '1' for i in range(b)]
    return words


def occurrences(bits, patterns_):
    N = len(patterns_[0]); lookup = {w: i for i, w in enumerate(patterns_)}
    return [(i, lookup[bits[i:i + N]]) for i in range(len(bits)-N+1) if bits[i:i+N] in lookup]


def replacement(bits, pats, i, j):
    a, b = pats[i], pats[j]; out = list(bits)
    for pos, k in occurrences(bits, pats):
        if k in (i, j):
            out[pos:pos+len(a)] = b if k == i else a
    return ''.join(out)


def from_cuts(bits):
    block_lengths = []
    last = 0
    for p, c in enumerate(bits):
        if c == '1':
            block_lengths.append(p+1-last);last = p+1
    block_lengths.append(len(bits)+1-last)
    out = []
    start = 1
    for length in block_lengths:
        out.extend(range(start + length-1, start - 1, -1))
        start += length
    return tuple(out)


def avoid231312(pi):
    n = len(pi)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1,n):
                x,y,z = pi[i], pi[j], pi[k]
                if y>x>z or x>z>y:
                    return False
    return True


def main():
    for b in range(1, 17):
        pats = patterns(b)
        N = len(pats[0])
        assert len(set(pats)) == b
        for a in pats:
            for c in pats:
                for k in range(1, N):
                    assert a[k:] != c[:N-k], (b,a,c,k)
        # Certify an equality of finite first-occurrence counts for several sizes.
        for M in range(N, min(N+5, 19)):
            counts = [0] * b
            for bits in map(''.join, product('01',repeat=M)):
                occ = occurrences(bits, pats)
                if occ:
                    counts[occ[0][1]] += 1
            assert len(set(counts)) == 1, (b,M,counts)
        # Deterministically verify the swap involution for small b / finite words.
        if b <= 4:
            for M in range(N, min(N+4,19)):
                for bits in map(''.join, product('01',repeat=M)):
                    for i in range(b-1):
                        changed = replacement(bits,pats,i,i+1)
                        assert replacement(changed,pats,i,i+1) == bits
                        assert [p for p,k in occurrences(bits,pats)] == [p for p,k in occurrences(changed,pats)]
    for n in range(1, 8):
        ps = {from_cuts(''.join(x)) for x in product('01', repeat=n-1)}
        eq = {p for p in permutations(range(1,n+1)) if avoid231312(p)}
        assert ps == eq, (n,len(ps),len(eq))
        for p in ps:
            bits = ''.join('1' if p[i]<p[i+1] else '0' for i in range(n-1))
            assert from_cuts(bits) == p
            for i in range(n):
                for j in range(i+1,n):
                    assert (p[i]<p[j]) == ('1' in bits[i:j])
    for b in range(1, 12):
        p=patterns(b);N=len(p[0]);
        for a in range(b+1):
            for M in range(N, min(N+4, 20)):
                hits=0;win=0
                for bits in map(''.join,product('01',repeat=M)):
                    occ=occurrences(bits,p)
                    if occ:
                        hits+=1
                        win+=int(occ[0][1]<a)
                assert Fraction(win,2**M)==Fraction(a,b)*Fraction(hits,2**M)
    print('ALL_CHECKS_OK: cross-bifix family b<=16; finite symmetry and exact probabilities; layered-avoidance n<=7')


if __name__=='__main__': main()
