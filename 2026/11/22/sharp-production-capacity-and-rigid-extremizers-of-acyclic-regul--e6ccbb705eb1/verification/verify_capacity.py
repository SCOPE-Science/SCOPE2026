"""Independent arithmetic and constructive tests for acyclic regular grammars."""
from functools import lru_cache
from itertools import product

@lru_cache(None)
def capacity(p):
    if p == 0:
        return 1
    return max(r * capacity(p-r) for r in range(1, p+1))


def partition_optimal(p):
    assert p >= 1
    parts=[]
    while p:
        r=next(r for r in range(1,p+1) if r*capacity(p-r)==capacity(p))
        parts.append(r)
        p -= r
    return parts


def unary_grammar_exponents(branches):
    # Each production at layer i contributes digit * product of remaining branching widths.
    weights=[1]*len(branches)
    for i in range(len(branches)-2,-1,-1):
        weights[i]=weights[i+1]*branches[i+1]
    paths=[sum(d*w for d,w in zip(digits,weights)) for digits in product(*(range(r) for r in branches))]
    return paths

for p in range(1,25):
    branches=partition_optimal(p)
    paths=unary_grammar_exponents(branches)
    assert len(paths)==capacity(p)
    assert set(paths)==set(range(capacity(p)))
    assert len(set(paths))==len(paths)
    assert sum(branches)==p
    assert capacity(p)==(1 if p==1 else 3**(p//3) if p%3==0 else 4*3**((p-4)//3) if p%3==1 else 2*3**((p-2)//3))
    print(f'{p:2} productions -> {capacity(p):8} consecutive unary outputs; branching {branches}')

for n in range(1,1001):
    p=next(p for p in range(1,25) if capacity(p)>=n)
    assert p==1 or capacity(p-1)<n
print('All integer endpoints 1..1000 satisfy the sharp inverse-cover threshold.')
