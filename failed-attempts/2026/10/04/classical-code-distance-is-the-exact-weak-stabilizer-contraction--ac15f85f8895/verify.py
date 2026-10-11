from itertools import combinations


def parity_dot(a, b):
    return (a & b).bit_count() & 1


def word_weight(columns, u):
    return sum(parity_dot(u, v) for v in columns)


def minimum_weight(columns, r):
    return min(word_weight(columns, u) for u in range(1, 1 << r))


def unit_columns(r):
    return tuple(1 << j for j in range(r))


def full_nonzero_columns(r):
    return tuple(range(1, 1 << r))


def check_endpoints():
    checked = 0
    for r in range(1, 7):
        assert minimum_weight(unit_columns(r), r) == 1
        full = full_nonzero_columns(r)
        weights = {word_weight(full, u) for u in range(1, 1 << r)}
        assert weights == {1 << (r - 1)}
        checked += (1 << r) - 1
    return checked


def check_intermediate():
    # Columns e1, e2, e3, and e1+e2+e3.
    columns = (1, 2, 4, 7)
    weights = sorted(word_weight(columns, u) for u in range(1, 8))
    assert weights == [2, 2, 2, 2, 2, 2, 4]
    return weights


def exhaust_distinct_r3():
    universe = tuple(range(1, 8))
    best = {}
    schedules = 0
    for length in range(3, 8):
        optimum = 0
        for columns in combinations(universe, length):
            schedules += 1
            optimum = max(optimum, minimum_weight(columns, 3))
        best[length] = optimum
    assert best == {3: 1, 4: 2, 5: 2, 6: 3, 7: 4}
    return best, schedules


if __name__ == '__main__':
    endpoint_characters = check_endpoints()
    weights = check_intermediate()
    best, schedules = exhaust_distinct_r3()
    print('VERIFY_OK',
          f'endpoint_characters={endpoint_characters}',
          f'intermediate_weights={weights}',
          f'distinct_r3_schedules={schedules}',
          f'best={best}')
