"""Exhaustive small-instance checker for prescribed block-character square-root fibers.

The direct procedure enumerates maps point by point and composes them twice.
The formula procedure uses sums over block layers and preimage cardinalities.
No numerical tables or external packages are required.
"""
from itertools import product
from math import comb


def predicted(ns, root, e):
    m = len(ns)
    if e[root] != root or any(e[e[i]] != root for i in range(m)):
        return 0
    F = [j for j in range(m) if j != root and e[j] == root]
    N = {j:sum(ns[i] for i in range(m) if e[i] == j) for j in F}
    a = ns[root]
    ans = 0
    for k in range(a):
        factor = comb(a - 1, k) * k**(a - 1 - k)
        for j in F:
            factor *= sum(comb(ns[j],h) * k**(ns[j]-h)* h**N[j]
                          for h in range(ns[j]+1))
        ans += factor
    return ans


def direct(ns, root):
    block_indices=[];block_of=[]
    for j,b in enumerate(ns):
        ids=list(range(len(block_of),len(block_of)+b))
        block_indices.append(ids)
        block_of.extend([j]*b)
    n=len(block_of); target=block_indices[root][0]
    hist={}
    for f in product(range(n), repeat=n):
        if any(f[f[x]] != target for x in range(n)):
            continue
        e=[]
        for ids in block_indices:
            images={block_of[f[x]] for x in ids}
            if len(images)!=1:break
            e.append(images.pop())
        else:
            e=tuple(e)
            hist[e]=hist.get(e,0)+1
    return hist


def check():
    configurations=[(1,),(2,),(3,),(4,),(1,1),(1,2),(2,2),
                    (1,3),(2,3),(1,1,1),(1,1,2),(1,2,2),
                    (2,2,2),(1,1,3),(1,2,3)]
    for ns in configurations:
        for root in range(len(ns)):
            brute=direct(ns,root)
            formula={e:predicted(ns,root,e)
                     for e in product(range(len(ns)), repeat=len(ns))}
            formula={e:n for e,n in formula.items() if n}
            assert brute==formula, (ns,root,brute,formula)
            print('PASS',ns,'root-block',root,'total',sum(brute.values()),
                  'nonempty block-character fibers',len(brute))
    print('ALL PRESCRIBED-BLOCK-FIBER TESTS PASSED')

if __name__=='__main__':check()
