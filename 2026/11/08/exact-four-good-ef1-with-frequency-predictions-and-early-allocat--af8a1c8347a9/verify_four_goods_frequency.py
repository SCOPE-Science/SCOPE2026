"""Exhaustive ordinal recursion for the first surplus good in three-agent EF1.

Every agent knows its four positive single-good values as an exact multiset,
without knowing which values belong to future goods. A rank vector describes
one arriving good, with each agent's four ranks used exactly once.
"""
from functools import lru_cache
from itertools import product
from pathlib import Path
import json

N = 3
M = 4
RANKS = (0, 1, 2, 3)


def terminal_ok(records):
    bundles = [[] for _ in range(N)]
    for vector, who in records:
        bundles[who].append(vector)
    lengths = sorted(map(len, bundles))
    if lengths != [1, 1, 2]:
        return False
    double = next(i for i in range(N) if len(bundles[i]) == 2)
    for i in range(N):
        if i == double:
            continue
        singleton_rank = bundles[i][0][i]
        smaller_pair_rank = min(vector[i] for vector in bundles[double])
        if singleton_rank < smaller_pair_rank:
            return False
    return True


def game(mode):
    @lru_cache(None)
    def solve(remaining, records):
        if not remaining[0]:
            return terminal_ok(records)
        for vector in product(*remaining):
            following = tuple(tuple(r for r in remaining[i] if r != vector[i])
                              for i in range(N))
            answers = []
            for recipient in range(N):
                if mode == 'first_two_distinct' and len(records) == 1 \
                        and records[0][1] == recipient:
                    continue
                if mode == 'first_two_together' and len(records) == 1 \
                        and records[0][1] != recipient:
                    continue
                if mode == 'first_three_distinct' and len(records) < 3 \
                        and any(j == recipient for _, j in records):
                    continue
                following_records = tuple(sorted(records + ((vector, recipient),)))
                answers.append(solve(following, following_records))
            if not any(answers):
                return False
        return True

    initial = solve((RANKS,) * N, ())
    return initial, solve.cache_info().currsize


def verify_restricted_witnesses():
    path = Path(__file__).with_name('four_goods_restricted_witnesses.json')
    trees = json.loads(path.read_text(encoding='utf-8'))['trees']
    leaves = {}
    for mode, tree in trees.items():
        def allowed(history):
            used = [recipient for _, recipient in history]
            result = []
            for recipient in range(N):
                if mode == 'first_two_together' and len(history) == 1 and recipient != used[0]:
                    continue
                if mode == 'first_three_distinct' and len(history) < 3 and recipient in used:
                    continue
                result.append(recipient)
            return result
        def check(node, remaining, history):
            if 'terminal' in node:
                assert not remaining[0]
                encoded = tuple(sorted((tuple(v), who) for v, who in node['terminal']))
                assert encoded == tuple(sorted(history))
                assert not terminal_ok(history)
                return 1
            ranks = tuple(node['arrival'])
            assert len(ranks) == N and all(ranks[i] in remaining[i] for i in range(N))
            following = tuple(tuple(r for r in remaining[i] if r != ranks[i]) for i in range(N))
            permitted = allowed(history)
            assert set(node['responses']) == set(map(str, permitted))
            return sum(check(node['responses'][str(recipient)], following, history + ((ranks, recipient),))
                       for recipient in permitted)
        leaves[mode] = check(tree, (RANKS,) * N, ())
    print('witness_leaves:', leaves)
    assert leaves == {'first_two_together': 27, 'first_three_distinct': 18}


def main():
    expected = {
        'unrestricted': True,
        'first_two_distinct': True,
        'first_two_together': False,
        'first_three_distinct': False,
    }
    for mode, expected_win in expected.items():
        win, states = game(mode)
        print(f'{mode}: winning={win}, memo_states={states}')
        assert win == expected_win
    verify_restricted_witnesses()


if __name__ == '__main__':
    main()
