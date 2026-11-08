"""Exact independent exhaustive checker for five-mark B_5 sets.

No outside packages. Usage: python3 verify.py
The loops cover every normalized 0<a<b<c<d<=72 without symmetry reduction.
"""
from itertools import combinations_with_replacement

FIVE = tuple(combinations_with_replacement(range(5), 5))
FOUR = tuple(combinations_with_replacement(range(4), 5))


def distinct(marks, index_tuples):
    seen = set()
    for indices in index_tuples:
        total = sum(marks[i] for i in indices)
        if total in seen:
            return False
        seen.add(total)
    return True


def verify():
    checked = 0
    survivors = 0
    all_solutions = []
    for d in range(4, 73):
        for a in range(1, d - 2):
            for b in range(a + 1, d - 1):
                for c in range(b + 1, d):
                    checked += 1
                    if not distinct((0, a, b, c), FOUR):
                        continue
                    survivors += 1
                    five = (0, a, b, c, d)
                    if distinct(five, FIVE):
                        all_solutions.append(five)
    expected = [(0, 1, 16, 66, 72), (0, 6, 56, 71, 72)]
    assert checked == 1028790, (checked, 'quadruples')
    assert survivors == 342414, (survivors, 'survivors')
    assert all_solutions == expected, all_solutions
    assert len({sum(expected[0][i] for i in t) for t in FIVE}) == 126
    assert tuple(72 - x for x in reversed(expected[0])) == expected[1]
    print('EXACT_5SUM_DISTINCT=126')
    print('QUADRUPLES_EXHAUSTED=1028790')
    print('FOUR_MARK_PRUNING_SURVIVORS=342414')
    print('OPTIMAL_SETS=0,1,16,66,72;0,6,56,71,72')
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
