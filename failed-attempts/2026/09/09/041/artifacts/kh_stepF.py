"""Step F: bigraded Kh homology of 10_124 over finite fields (2 primes).
Block by q-degree: differential preserves q. For each (h,q) block build sparse
matrix over Fp and rank via elimination on dict-of-rows. Sizes: worst block?
q range about 7..29ish; height dims up to 5352 split across q's -> blocks ~ hundreds.
Implement carefully with lists.
Frobenius maps (q-homogeneous, Lee convention qdeg(v+)=+1, v-=-1):
 merge: ++ -> +, +-/-+ -> -, -- -> 0
 split of circle x into a,b: += +a -b + -a +b ; - = -a -b.
Circle identity: compare lab0/lab1 dicts.
Edge sign: (-1)^{popcount(mask & lowmask(k))}.
"""
import json
from collections import defaultdict
import sys
sys.path.insert(0, 'output/artifacts')
from kh_stepD import parse_pd, smoothing_data

P = 1000000007
P2 = 998244353

def qdeg_of(mask_circles_word, h, shift):
    # (#plus - #minus) + h + shift ; shift = nplus - nminus = 10
    s = bin(mask_circles_word)
    return None

def build_blocks(pd, nplus, nminus):
    n = len(pd)
    shift = nplus - nminus
    # enumerate basis: key (h,q) -> list of (mask, word)
    blocks = defaultdict(list)
    info = {}
    for mask in range(1 << n):
        h = bin(mask).count('1')
        roots, lab = smoothing_data(pd, mask)
        c = len(roots)
        for word in range(1 << c):
            # bit 0 => v+, 1 => v-
            nplus_w = c - bin(word).count('1')
            nminus_w = bin(word).count('1')
            q = (nplus_w - nminus_w) + h + shift
            blocks[(h, q)].append((mask, word))
    return blocks

if __name__ == '__main__':
    d = json.load(open('output/artifacts/pd_codes.json'))
    pd = parse_pd(d['10_124']['pd'])
    blocks = build_blocks(pd, 10, 0)
    ks = sorted(blocks)
    print('nblocks=', len(ks))
    tot = sum(len(v) for v in blocks.values())
    print('total=', tot)
    # histogram of block sizes
    from collections import Counter
    print(sorted(Counter(len(v) for v in blocks.values()).items())[:20])
    print('q range:', min(q for h, q in ks), max(q for h, q in ks))
    print('per-h totals:')
    perh = defaultdict(int)
    for (h, q), v in blocks.items():
        perh[h] += len(v)
    print(dict(sorted(perh.items())))
