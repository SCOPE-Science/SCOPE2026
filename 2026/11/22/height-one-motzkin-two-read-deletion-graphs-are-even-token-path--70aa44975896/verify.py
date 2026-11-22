"""Reproducible finite tests for Motzkin two-read deletion graphs.

Only checks finite instances; the accompanying mathematical proof establishes
all-length assertions.
"""
from itertools import combinations
from math import comb


def paths(n):
    # The non-flat step positions alternate U and D.
    for t in range(n // 2 + 1):
        for occupied in combinations(range(n), 2*t):
            w = ['F'] * n
            for j, i in enumerate(occupied):
                w[i] = 'U' if j % 2 == 0 else 'D'
            yield ''.join(w), occupied, t


def deletion_set(w):
    return {w[:i] + w[i+1:] for i in range(len(w))}


def predicted_edge(a, b):
    if len(a) != len(b):
        return False
    differing = [i for i,(x,y) in enumerate(zip(a,b)) if x != y]
    if len(differing) != 2 or differing[1] != differing[0]+1:
        return False
    i = differing[0]
    return a[i:i+2] in ('FU','UF','FD','DF') and b[i:i+2] == a[i:i+2][::-1]


def capacity_formula(n,t):
    return (comb(n,2*t) + comb(n//2,t)) // 2


def main():
    for n in range(1,11):
        words = list(paths(n))
        ds = {w: deletion_set(w) for w,_,_ in words}
        actual = 0
        pred = 0
        for j, (v,_,_) in enumerate(words):
            for w,_,_ in words[:j]:
                x = len(ds[w] & ds[v])
                p = predicted_edge(w, v)
                assert (x == 2) == p, (n,w,v,x,p)
                assert x <= 2
                actual += (x == 2)
                pred += p
        expected_e = (n-1)*2**(n-3) if n>=3 else 0
        assert actual == pred == expected_e, (n, actual,pred,expected_e)
        colcount = {}
        for w, idx, t in words:
            colcount[(t,sum(i+1 for i in idx) % 2)] = colcount.get((t,sum(i+1 for i in idx) % 2), 0)+1
        for t in range(n//2+1):
            lhs=colcount.get((t,t%2),0)
            rhs=colcount.get((t,1-(t%2)),0)
            assert lhs == capacity_formula(n,t), (n,t,lhs,capacity_formula(n,t))
            assert lhs + rhs == comb(n,2*t)
            assert lhs-rhs == comb(n//2,t)
        total = sum(capacity_formula(n,t) for t in range(n//2+1))
        assert total == (2**(n-1) + 2**(n//2))//2
        print(f'direct n={n}: paths={len(words)}, edges={actual}, optimum={total}')

    # Disjoint-pair matching involution, and exact edge counts per layer.
    for n in range(1,19):
        for t in range(n//2+1):
            k=2*t
            paired=set()
            unmatched=[]
            for occupied in combinations(range(n),k):
                pos=set(occupied)
                first=None
                for i in range(0,n-1,2):
                    if (i in pos) != (i+1 in pos):
                        first=i
                        break
                if first is None:
                    unmatched.append(occupied)
                else:
                    pos.symmetric_difference_update((first,first+1))
                    mate=tuple(sorted(pos))
                    assert mate != occupied and len(set(occupied)^set(mate))==2
                    if occupied not in paired:
                        paired.add(occupied); paired.add(mate)
            assert len(paired) + len(unmatched) == comb(n,k)
            assert len(unmatched) == comb(n//2,t)
            assert all(sum(a+1 for a in S)%2 == t%2 for S in unmatched)
        if n <= 12:
            print('matching n=',n,'passed')
    print('ALL TESTS PASS')

if __name__ == '__main__':
    main()
