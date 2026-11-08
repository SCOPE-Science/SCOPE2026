"""Independent exhaustive labelled-state simulation on fan graphs over GF(2)."""
from collections import defaultdict


def step(n, state):
    hub = state & 1
    rim = [(state >> (i + 1)) & 1 for i in range(n)]
    new_hub = sum(rim) % 2
    new_rim = [hub ^ (rim[i - 1] if i else 0)
               ^ (rim[i + 1] if i < n - 1 else 0)
               for i in range(n)]
    return new_hub | sum(bit << (i + 1) for i, bit in enumerate(new_rim))


def expected_counts(n):
    N = n + 1
    if n % 2 == 0:
        return {0: 1 << n, 1: 1 << n}
    if n % 4 == 1:
        return {0: 1 << N}
    e = (n + 1) & -(n + 1)
    d = n - e + 3
    c = lambda t: min(t, 1) + min(t, e - 3)
    out = {0: 1 << d}
    for t in range(1, e - 2):
        out[t] = (1 << d) * ((1 << c(t)) - (1 << c(t - 1)))
    return out


def main():
    tested = 0
    for n in range(2, 12):
        got = defaultdict(int)
        primitive_periods = defaultdict(int)
        for init in range(1 << (n + 1)):
            seen = {}
            cur = init
            while cur not in seen:
                seen[cur] = len(seen)
                cur = step(n, cur)
            T = seen[cur]
            period = len(seen) - T
            got[T] += 1
            if T == 0:
                primitive_periods[period] += 1
            tested += 1
        assert dict(got) == expected_counts(n), (n, dict(got), expected_counts(n))
        if n == 7:
            assert primitive_periods == {1: 2, 2: 2}, primitive_periods
    print(f'LABELLED_EVOLUTION_OK n=2..11; states={tested}; entry census verified')
    print('FAN_7_RECURRENT_OK: 2 fixed states and one primitive two-cycle')


if __name__ == '__main__':
    main()
