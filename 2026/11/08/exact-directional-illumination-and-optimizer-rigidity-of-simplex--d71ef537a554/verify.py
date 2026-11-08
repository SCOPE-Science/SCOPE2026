"""Exact finite tests of the type-A root-polytope illumination criterion.

No floating point arithmetic. All-dimensional proof is independent of these tests.
"""
from itertools import product


def active_facets(n, i, j):
    others=[k for k in range(n) if k not in (i,j)]
    return [sum(1<<k for k in (i,)+tuple(others[z] for z in range(len(others)) if mask>>z&1)) for mask in range(1<<len(others))]


def direct(n, v, i, j):
    return all(sum(v[k] for k in range(n) if mask>>k&1)<0 for mask in active_facets(n,i,j))


def analytic(n, v, i, j):
    return v[i]<0 and v[j]>0 and -v[i]+v[j]>sum(x for x in v if x>0)


def check():
    cases=0
    for n in range(3,8):
        for bits in product((-2,-1,0,1,2),repeat=n-1):
            v=bits+(-sum(bits),)
            if not any(v): continue
            seen=[]
            for i in range(n):
                for j in range(n):
                    if i==j:continue
                    a=direct(n,v,i,j)
                    b=analytic(n,v,i,j)
                    assert a==b,(n,v,i,j,a,b)
                    if a:seen.append((i,j))
                    cases+=1
            assert len(seen)<=n-1, (n,v,seen)
            assert len({i for i,j in seen})<=1 or len({j for i,j in seen})<=1,(n,v,seen)
            if len(seen)==n-1:
                assert (sum(x<0 for x in v)==1 and all(x!=0 for x in v)) or (sum(x>0 for x in v)==1 and all(x!=0 for x in v)),(n,v,seen)
        for center in range(n):
            v=tuple(-(n-1) if i==center else 1 for i in range(n))
            assert sorted((i,j) for i in range(n) for j in range(n) if i!=j and direct(n,v,i,j))==[(center,j) for j in range(n) if j!=center]
    return cases

if __name__=='__main__':
    print('ROOT_A_EXACT_OK',check())
