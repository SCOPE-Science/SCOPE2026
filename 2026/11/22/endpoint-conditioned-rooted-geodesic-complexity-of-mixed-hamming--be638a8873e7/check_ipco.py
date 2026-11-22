"""Exact small-case checks for isometric path complexity of Hamming products.

Run with Python 3.10+: python check_ipco.py
No external dependencies.
"""
from itertools import product, combinations, permutations
from collections import Counter


def comparable(x,y,root):
    return all(a == b or a == r for a,b,r in zip(x,y,root)) or all(a == b or b == r for a,b,r in zip(x,y,root))


def antichain_width(path,root):
    n=len(path)
    best=0
    for mask in range(1,1<<n):
        if mask.bit_count()<=best:continue
        indices=[i for i in range(n) if mask>>i&1]
        if all(not comparable(path[i],path[j],root) for i,j in combinations(indices,2)):
            best=len(indices)
    return best


def exact_max_for_root(q,root):
    vertices=list(product(*(range(x) for x in q)))
    max_width=0
    count=0
    witness=None
    for a,b in combinations(vertices,2):
        change=[i for i in range(len(q)) if a[i]!=b[i]]
        for order in permutations(change):
            v=list(a);path=[tuple(v)]
            for i in order:
                v[i]=b[i]
                path.append(tuple(v))
            w=antichain_width(path,root)
            count+=1
            if w>max_width:
                max_width=w; witness=path
    return max_width,count,witness


def direct_cover_number(path,root,q):
    # Enumerate every root-to-vertex geodesic, then solve the exact set cover
    # for target vertices on the given path by bitmask dynamic programming.
    path_index={v:i for i,v in enumerate(path)}
    cover_masks=set()
    for endpoint in product(*(range(x) for x in q)):
        active=[i for i in range(len(q)) if endpoint[i]!=root[i]]
        for order in permutations(active):
            v=list(root);mask=0
            if tuple(v) in path_index:mask|=1<<path_index[tuple(v)]
            for i in order:
                v[i]=endpoint[i]
                if tuple(v) in path_index:mask|=1<<path_index[tuple(v)]
            cover_masks.add(mask)
    target=(1<<len(path))-1
    dp=[len(path)+1]*(target+1);dp[0]=0
    for mask in range(target+1):
        if dp[mask]>=len(path):continue
        for cover in cover_masks:
            m2=mask|cover
            if dp[m2]>dp[mask]+1:dp[m2]=dp[mask]+1
    return dp[target]


def predicted(q):
    binary=sum(x==2 for x in q)
    return 1+sum(x>=3 for x in q)+binary//2


def main():
    cases=[(2,),(3,),(2,2),(3,3),(2,3),(2,2,2),(2,2,3),(2,3,3),(3,3,3),(2,2,2,2),(2,2,3,3),(2,3,4)]
    for q in cases:
        root=(0,)*len(q)
        measured,count,witness=exact_max_for_root(q,root)
        expected=predicted(q)
        assert measured==expected,(q,measured,expected)
        # Independent exact cover test at the extremal path for small graphs.
        if len(q)<=3:
            cover=direct_cover_number(witness,root,q)
            assert cover==measured,(q,cover,measured)
        print('PASS',q,'vertices',__import__('math').prod(q),'geodesics',count,'width',measured)
    print('ALL_HAMMING_IPCO_TESTS_PASS')

if __name__=='__main__':main()
