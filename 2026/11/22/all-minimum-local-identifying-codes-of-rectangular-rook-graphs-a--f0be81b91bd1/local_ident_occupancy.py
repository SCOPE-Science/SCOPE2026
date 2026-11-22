"""Independent board-incidence verifier for local identifying codes in rook graphs.

Cells use bit positions i*n+j. Counts all subsets for small boards by
row/column occupancy; independently of closed-neighborhood comparisons.
"""
from math import comb, factorial
from collections import Counter

def formula(s,l):
    q=l-s
    total=factorial(l)//factorial(q)*comb(s,2)**q
    # Number of sequences of q unordered pairs covering all or all-but-one rows.
    def onto(n):
        return sum((-1)**j*comb(n,j)*comb(n-j,2)**q for j in range(n+1))
    identifying=factorial(l)//factorial(q)*(onto(s)+s*onto(s-1))
    return total, identifying

def check(s,l):
    num=s*l
    row_masks=[sum(1<<(i*l+j) for j in range(l)) for i in range(s)]
    col_masks=[sum(1<<(i*l+j) for i in range(s)) for j in range(l)]
    t=2*l-s
    counts=Counter()
    for C in range(1<<num):
        cols=[C&x for x in col_masks]
        rows=[C&x for x in row_masks]
        if (not all(rows)) and (not all(cols)):
            continue
        if any(sum((x & ~row_masks[i])==0 for x in cols)>1 for i in range(s)):
            continue
        if any(sum((x & ~col_masks[j])==0 for x in rows)>1 for j in range(l)):
            continue
        sz=C.bit_count();counts[sz]+=1
    assert min(counts)==t,(s,l,min(counts),t)
    assert counts[t]==formula(s,l)[0],(s,l,counts[t],formula(s,l))
    return s,l,min(counts),counts[t],sum(counts.values())

if __name__=='__main__':
    for p in [(3,3),(3,4),(3,5),(3,6),(4,4),(4,5)]:
        print(*check(*p),flush=True)
    for s in range(3,11):
        for l in range(s,s+7):
            x,y=formula(s,l)
            assert y<=x and (y>0)==(l-s>=((s-1)+1)//2)
    print('formula-consistency ok')
