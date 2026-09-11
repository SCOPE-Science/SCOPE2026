"""Permutation/split-choice independence: gamma=max vs gamma=min (low13 split)."""
import sys
sys.setrecursionlimit(100000)
from functools import lru_cache

def make_engine(r, gamma_pick):
    @lru_cache(maxsize=None)
    def inv(d, tup):
        n = len(tup)
        for a in tup:
            if a < 0 or a > r: return 0
        if sum(tup) != r + (r+1)*d + n - 3: return 0
        if d < 0: return 0
        if d == 0: return 1 if (n == 3 and sum(tup) == r) else 0
        if n <= 1: return 0
        if n == 2: return 1 if (d == 1 and tup == (r, r)) else 0
        if n == 3: return 1
        lst = list(tup)
        if 0 in lst: return 0
        if 1 in lst:
            i = lst.index(1)
            return d * inv(d, tuple(sorted(lst[:i]+lst[i+1:])))
        a1 = lst[0]; alpha, beta = 1, a1-1
        rest = lst[1:]
        gamma = max(rest) if gamma_pick == 'max' else min(rest)
        tmp = list(rest); tmp.remove(gamma)
        delta = max(tmp); tmp.remove(delta)
        S = tmp
        e_skip = r - a1; m = len(S)
        lhs_rest = 0
        for mask in range(1 << m):
            S1=[S[i] for i in range(m) if (mask>>i)&1]
            S2=[S[i] for i in range(m) if not (mask>>i)&1]
            for d1 in range(d+1):
                d2=d-d1
                for e in range(r+1):
                    if mask==0 and d1==0 and e==e_skip: continue
                    A=inv(d1,tuple(sorted([alpha,beta]+S1+[e])))
                    if A: lhs_rest+=A*inv(d2,tuple(sorted([r-e,gamma,delta]+S2)))
        rhs=0
        for mask in range(1 << m):
            S1=[S[i] for i in range(m) if (mask>>i)&1]
            S2=[S[i] for i in range(m) if not (mask>>i)&1]
            for d1 in range(d+1):
                d2=d-d1
                for e in range(r+1):
                    A=inv(d1,tuple(sorted([alpha,gamma]+S1+[e])))
                    if A: rhs+=A*inv(d2,tuple(sorted([r-e,beta,delta]+S2)))
        return rhs-lhs_rest
    return inv, lambda d,l: inv(d,tuple(sorted(l)))

outs = {}
for gp in ['max','min']:
    _, call = make_engine(4, gp)
    outs[gp] = call(4,[4]*7)
    print(gp, "target=", outs[gp], flush=True)
assert outs['max'] == outs['min'] == 1
print("SPLIT_AGREE_PASS", flush=True)
