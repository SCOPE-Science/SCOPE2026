"""Independent direct test of minimal total domination in KG(n,2).

Enumerates every candidate of size 3..6, using open-neighborhood bitsets;
validates minimality by deleting each selected graph vertex.
"""
from collections import Counter
from itertools import combinations
from math import comb


def direct_counts(n):
    pairs = list(combinations(range(n), 2))
    N = len(pairs)
    full = (1 << N) - 1
    nbr = [sum(1 << j for j, (c,d) in enumerate(pairs)
               if a != c and a != d and b != c and b != d)
           for a,b in pairs]
    result = Counter()
    for k in range(3, min(6,N)+1):
        for ids in combinations(range(N),k):
            cover=0
            for i in ids: cover |= nbr[i]
            if cover != full: continue
            removable = False
            for j in ids:
                others = 0
                for i in ids:
                    if i != j: others |= nbr[i]
                if others == full:
                    removable = True
                    break
            if removable: continue
            result[k] += 1
    return result


def expected(n):
    C=lambda a,b:comb(a,b) if a>=b>=0 else 0
    return Counter({3:15*C(n,6),4:10*C(n,5),5:12*C(n,5),6:C(n,4)})


def main():
    for n in range(4,9):
        direct=direct_counts(n)
        pred=expected(n)
        print(f'n={n}:', {k:direct[k] for k in range(3,7)}, 'expected', {k:pred[k] for k in range(3,7)})
        assert all(direct[k]==pred[k] for k in range(3,7))
    print('DIRECT_KNESER_OK')
if __name__=='__main__':main()
