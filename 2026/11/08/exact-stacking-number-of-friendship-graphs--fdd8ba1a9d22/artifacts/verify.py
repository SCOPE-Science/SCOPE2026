"""Exact finite checks for pebbling on bouquets of triangles.

The unrestricted theorem is proved separately by the blade-resource argument.
This script checks local transition certificates and small graph boundaries.
"""
from functools import lru_cache
from itertools import product
from math import comb


def compositions(total, parts):
    if parts == 1:
        yield (total,)
    else:
        for first in range(total+1):
            for rest in compositions(total-first, parts-1):
                yield (first,)+rest


def neighbors(r):
    n=2*r+1
    out=[tuple(range(1,n))]
    for i in range(r):
        a=2*i+1;b=a+1
        out.extend(((0,b),(0,a)))
    return tuple(out)


def reachability(r):
    nbr=neighbors(r)
    @lru_cache(maxsize=None)
    def can(c):
        if sum(x>0 for x in c)==1:
            return True
        for u,x in enumerate(c):
            if x<2: continue
            for v in nbr[u]:
                d=list(c);d[u]-=2;d[v]+=1
                if can(tuple(d)):
                    return True
        return False
    return can


def three_vertex_endings(h,a,b):
    @lru_cache(maxsize=None)
    def outcomes(x,y,z):
        result={x} if y==0 and z==0 else set()
        state=(x,y,z)
        for src,dst in ((0,1),(0,2),(1,0),(1,2),(2,0),(2,1)):
            if state[src]>=2:
                q=list(state);q[src]-=2;q[dst]+=1
                result.update(outcomes(*q))
        return frozenset(result)
    return outcomes(h,a,b)


def gamma(s):
    if s==0:return 0
    if s<=2:return -1
    return (s-2)//2


def main():
    for s in range(4,23):
        for a in range(s+1):
            b=s-a
            outcomes=three_vertex_endings(0,a,b)
            assert outcomes and max(outcomes)>=gamma(s),(s,a,b,outcomes)
    print('LOCAL_HIGH_BLADE_REDUCTION_OK s=4..22')
    for s in range(6,22):
        assert gamma(s)==gamma(s-2)+1
    print('LOCAL_INDUCTION_OK')
    for r in range(1,5):
        # arithmetic proof is independent of this bounded corroboration
        for h in range(4*r+1):
            for ss in compositions(4*r-h,r):
                assert h+sum(gamma(s) for s in ss)>=1,(r,h,ss)
    print('ARITHMETIC_RESOURCE_BOUND_OK r=1..4')
    for r in (1,2,3):
        can=reachability(r)
        for t in range(2,4*r+1):
            vals=[can(c) for c in compositions(t,2*r+1)]
            assert (all(vals) == (t==4*r)),(r,t,sum(vals),len(vals))
        print('FULL_CONFIGURATIONS_OK r=%d threshold=%d'%(r,4*r))
    for r in range(2,8):
        c=(0,2*r+1,0)+(1,1)*(r-1)
        assert not reachability(r)(c),r
        print('OBSTRUCTION_OK r=%d mass=%d'%(r,4*r-1))
    print('VERIFY_OK')


if __name__=='__main__':main()
