"""Exhaustive microscopic checker for fixed-threshold GH dynamics on a triangular windmill.

No third-party dependencies. This checks finite instances only; the general theorem
follows from the two-step excitation exclusion in RESULT.md.
"""
from collections import Counter
from itertools import product


def expected(k, m):
    size = 2*m+1
    last = 2*k**(2*m)-(k-1)**(2*m)-2*m*(k-1)**(2*m-1)-(k*k-2)**m
    ans = {0: 1, k: last, k-1: k**size-last-(k-1)**size}
    for j in range(1, k-1):
        ans[j] = (j+1)**size-j**size
    return ans


def update(state, k, m):
    center = state[0]
    output = [((center+1) % k if center else int(sum(a == 1 for a in state[1:]) >= 2))]
    for j in range(m):
        a,b = state[1+2*j:3+2*j]
        output.append((a+1)%k if a else int(center == 1 and b == 1))
        output.append((b+1)%k if b else int(center == 1 and a == 1))
    return tuple(output)


def run(k, m):
    obs = Counter()
    total = 0
    for initial in product(range(k), repeat=2*m+1):
        state = initial
        hit = 0 if not any(state) else None
        for t in range(1, k+1):
            state = update(state,k,m)
            if hit is None and not any(state):
                hit=t
        assert hit is not None, (k,m,initial)
        obs[hit] += 1
        total+=1
    exp = expected(k,m)
    assert dict(sorted(obs.items())) == dict(sorted(exp.items())), (k,m,obs,exp)
    assert total==k**(2*m+1)
    assert obs[k] > 0
    print('PASS', 'colors',k,'petals',m,'states',total,'counts',dict(sorted(obs.items())))


if __name__ == '__main__':
    for k,m in [(3,1),(3,2),(3,3),(3,4),(3,5),(4,1),(4,2),(4,3),(4,4),(5,1),(5,2),(5,3),(6,1),(6,2)]:
        run(k,m)
    print('VERIFY_OK')
