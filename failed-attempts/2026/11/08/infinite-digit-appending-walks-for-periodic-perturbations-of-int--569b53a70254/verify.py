"""Exact-arithmetic checks for periodic-offset digit-appending theorems."""
from math import gcd, log2


def step_exists(A, B, offsets, m, k, t):
    n=m+k
    am=A**m + offsets[m % len(offsets)]
    an=A**n + offsets[n % len(offsets)]
    d=an-B**t*am
    return 0 <= d < B**t, d


def is_resonant(A,B,k,t):
    return A**k == B**t


def verify():
    configs=[(2,2,[-1,0,1,2,-2,3]),(2,4,[0,-1,3,-4,2]),
             (4,2,[-1,1,0,2,-3]),(4,8,[0,2,-1,-4,3]),
             (8,4,[-3,-2,3,1,0,-1]),(9,3,[2,0,-1,-5,3]),
             (3,9,[-1,2,-3,0]),(16,8,[3,-2,0,-1,-4])]
    checked=0; actual=0; cross=0
    for A,B,offsets in configs:
        C=max(map(abs,offsets))
        bound=C.bit_length()-1 if C else 0
        for m in range(16,32):
            for k in range(1,22):
                for t in range(1,13):
                    yes,d=step_exists(A,B,offsets,m,k,t)
                    checked+=1
                    if not yes:
                        continue
                    actual+=1
                    assert is_resonant(A,B,k,t), (A,B,offsets,m,k,t)
                    assert offsets[m%len(offsets)] == offsets[(m+k)%len(offsets)]//(B**t)
                    if offsets[m%len(offsets)] in (0,-1):
                        cross+=1
        # Independent of bounded sample, check symbolic deterministic construction:
        # exponent pairs k multiple of both period and denominator exponent
        for m in range(16,32):
            if offsets[m%len(offsets)] not in (0,-1):
                continue
            for k in range(1,400):
                # find an explicit resonant period-preserving k
                if k%len(offsets)==0 and any(A**k==B**t for t in range(1,350)):
                    t=next(t for t in range(1,350) if A**k==B**t)
                    assert step_exists(A,B,offsets,m,k,t)[0]
                    break
            else:
                raise AssertionError((A,B,offsets,m))
        # Finite-state dynamic search for nonterminal paths up to bound + 1
        states=list(range(len(offsets)))
        edges={i:set() for i in states}
        for i in states:
            for k in range(1, 6*len(offsets)+1):
                for t in range(1,12):
                    if A**k != B**t:
                        continue
                    j=(i+k)%len(offsets)
                    if 0 <= offsets[j]-B**t*offsets[i] < B**t:
                        edges[i].add(j)
        def walk_max(i,depth):
            if depth > bound+1:
                raise AssertionError('long nonterminal path')
            if not edges[i]:
                return 0
            return 1+max(walk_max(j,depth+1) for j in edges[i])
        for i in states:
            if offsets[i] not in (0,-1):
                assert walk_max(i,0) <= bound, (A,B,offsets,i)
    # Sharp family: one zero-digit step from each consecutive offset 2**i
    for L in range(0,12):
        offsets=[2**i for i in range(L+1)]
        m=(L+1)*3
        for i in range(L):
            yes,d=step_exists(2,2,offsets,m+i,1,1)
            assert yes and d==0
        assert max(offsets)==2**L
        assert L==(max(offsets).bit_length()-1)
    print('VERIFY_OK dependent_configs=%d raw_step_tests=%d accepted_steps=%d terminal_origin_steps=%d sharp_families=%d exact_integer=yes' % (len(configs),checked,actual,cross,12))

if __name__=='__main__':
    verify()
