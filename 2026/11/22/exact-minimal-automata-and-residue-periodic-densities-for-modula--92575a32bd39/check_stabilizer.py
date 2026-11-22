#!/usr/bin/env python3
"""Check the left stabilizer independently for small parameters."""
from itertools import product

def test(q,m):
    pairs=[(i,j) for i in range(q) for j in range(i+1,q)]
    d=q+len(pairs)
    S=list(product(range(m),repeat=d))
    F={x for x in S if all(x[q+k]==0 and x[i]*x[j]%m==0 for k,(i,j) in enumerate(pairs))}
    def mul(a,b):
        return tuple((a[i]+b[i])%m for i in range(q))+tuple((a[q+k]+b[q+k]+a[i]*b[j])%m for k,(i,j) in enumerate(pairs))
    left=[h for h in F if {mul(h,x) for x in F}==F]
    assert left==[(0,)*d],(q,m,left)
    print(f'q={q} m={m} |G|={len(S)} |F|={len(F)} left_stabilizer=1 PASS')
if __name__=='__main__':
    for x in [(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(4,2)]:test(*x)
