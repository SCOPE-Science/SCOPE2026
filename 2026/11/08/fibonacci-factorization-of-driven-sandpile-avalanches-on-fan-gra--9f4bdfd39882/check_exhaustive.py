"""Independent enumeration of recurrent fan sandpiles and their principal avalanches.

Only Python standard library. Run: python check_exhaustive.py
"""
from collections import Counter
from itertools import product


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a


def weight(m):
    return 1 if m == 0 else fibonacci(2*m)


def stabilize(state, n):
    """Legal toppling simulation, records the full vector of toppling counts."""
    h = list(state)
    fired = [0]*n
    while True:
        index = next((i for i in range(n) if h[i] >= (2 if i in (0, n-1) else 3)), None)
        if index is None:
            break
        d = 2 if index in (0, n-1) else 3
        h[index] -= d
        if index: h[index-1] += 1
        if index+1 < n: h[index+1] += 1
        fired[index] += 1
        assert sum(fired) <= 5*n, "stabilization did not finish as expected"
    return tuple(h), tuple(fired)


def is_recurrent_by_burning(state):
    n = len(state)
    after_burning, fired = stabilize(tuple(x+1 for x in state), n)
    return after_burning == state and fired == (1,)*n


def forbidden_zero_pattern(state):
    seen_zero = False
    for h in state:
        if h == 2: seen_zero = False
        elif h == 0:
            if seen_zero: return True
            seen_zero = True
    return False


def run():
    total_tests = 0
    for n in range(2, 10):
        rec = []
        for h in product(*([range(2)]+[range(3)]*(n-2)+[range(2)])):
            is_rec = is_recurrent_by_burning(h)
            assert is_rec == (not forbidden_zero_pattern(h)), (n, h)
            if is_rec: rec.append(h)
        assert len(rec) == fibonacci(2*n), (n, len(rec))
        for j in range(n):
            obs = Counter()
            sum_size = 0
            for h in rec:
                inp = list(h)
                inp[j] += 1
                _, fired = stabilize(inp, n)
                assert all(x in (0, 1) for x in fired)
                support = tuple(i for i, x in enumerate(fired) if x)
                if support:
                    L, R = support[0], support[-1]
                    assert support == tuple(range(L, R+1)) and L <= j <= R
                    obs[(L, R)] += 1
                else: obs[None] += 1
                sum_size += sum(fired)
                total_tests += 1
            # All spatial intervals compared to the proposed complete exact law.
            nonzero = 0
            for L in range(j+1):
                for R in range(j,n):
                    predicted = weight(L)*weight(n-R-1)
                    assert obs[(L,R)] == predicted, (n,j,L,R,obs[(L,R)],predicted)
                    nonzero += predicted
            predicted_nonzero = fibonacci(2*(j+1)-1)*fibonacci(2*(n-j)-1)
            assert nonzero == predicted_nonzero
            assert obs[None] == len(rec)-nonzero
            assert sum_size == len(rec), (n,j,sum_size,len(rec))
        print('n=%d | recurrent=%d | %d sites verified' % (n, len(rec), n))
    print('PASS: %d full recurrence/avalanche simulations; all interval laws and means agree.' % total_tests)


if __name__ == '__main__': run()
