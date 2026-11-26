"""Exact arithmetic verification of eight-node matching-averaging consensus counts.

This independent enumeration uses integer path multiplicities; three rounds of
averaging equal the rank-one average exactly iff every final integer row is 1^8.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations

N = 8

def perfect_matchings(vertices):
    if not vertices:
        yield ()
        return
    first = vertices[0]
    for index in range(1, len(vertices)):
        second = vertices[index]
        remain = vertices[1:index] + vertices[index + 1:]
        for rest in perfect_matchings(remain):
            yield ((first, second),) + rest


def next_rows(rows, matching):
    new = [None] * N
    for u, v in matching:
        row = tuple(rows[u][i] + rows[v][i] for i in range(N))
        new[u] = row
        new[v] = row
    return tuple(new)


def topology(first, second):
    owners = {}
    for index, (u, v) in enumerate(first):
        owners[u] = index
        owners[v] = index
    if any(owners[u] == owners[v] for u, v in second):
        return 'overlap'
    pairs = Counter(tuple(sorted((owners[u], owners[v]))) for u, v in second)
    if sorted(pairs.values()) == [2, 2]:
        return 'two_4_cycles'
    assert sorted(pairs.values()) == [1, 1, 1, 1]
    return 'one_8_cycle'


def main():
    matchings = list(perfect_matchings(tuple(range(N))))
    assert len(matchings) == 105
    assert len(set(matchings)) == 105
    unit = tuple(tuple(int(i == j) for j in range(N)) for i in range(N))
    target = tuple((1,) * N for _ in range(N))
    by_type = Counter()
    type_sizes = Counter()
    first = matchings[0]
    one = next_rows(unit, first)
    for second in matchings:
        category = topology(first, second)
        type_sizes[category] += 1
        two = next_rows(one, second)
        successful_thirds = 0
        for third in matchings:
            three = next_rows(two, third)
            # Every row divided by 8 after three rounds; target=all ones.
            if three == target:
                successful_thirds += 1
        by_type[category] += successful_thirds
        expected = {'overlap': 0, 'two_4_cycles': 24, 'one_8_cycle': 4}[category]
        assert successful_thirds == expected, (category, second, successful_thirds)
    assert type_sizes == {'overlap': 45, 'two_4_cycles': 12, 'one_8_cycle': 48}
    assert by_type == {'overlap': 0, 'two_4_cycles': 288, 'one_8_cycle': 192}
    assert Fraction(sum(by_type.values()), len(matchings)**2) == Fraction(32, 735)
    # The first matching has no special role: conjugation by any vertex permutation
    # sends every perfect matching to another. Check a representative permuted first.
    last_first = matchings[-1]
    one_other = next_rows(unit, last_first)
    successes = 0
    for second in matchings:
        two = next_rows(one_other, second)
        for third in matchings:
            if next_rows(two, third) == target:
                successes += 1
    assert successes == 480
    print('VERIFY_OK')
    print('matchings=', len(matchings))
    print('second_round_classes=', dict(sorted(type_sizes.items())))
    print('successful_last_round_triples=', dict(sorted(by_type.items())))
    print('success_count_conditional_on_first=', sum(by_type.values()))
    print('success_probability=', Fraction(sum(by_type.values()), len(matchings)**2))

if __name__ == '__main__':
    main()
