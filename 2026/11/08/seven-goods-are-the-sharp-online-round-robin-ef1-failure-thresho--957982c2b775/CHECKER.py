#!/usr/bin/env python3
"""Reproduce and check finite online round-robin equilibrium certificate.

All arithmetic is exact integer arithmetic; Python standard library only.
Run alongside DP_CERTIFICATE.json as: python3 CHECKER.py
"""
import json
from pathlib import Path

WEIGHTS = (
    (904, 192, 132, 144, 514, 385, 672),
    (1296, 160, 136, 960, 900, 129, 386),
    (648, 641, 144, 672, 192, 898, 132),
)
ORDER = (0, 1, 2, 0, 1, 2, 0)
N = 7

def solve():
    """Exact backward induction on all subsets of remaining goods."""
    values = [(0, 0, 0)] * (1 << N)
    choices = [-1] * (1 << N)
    bundles = [(0, 0, 0)] * (1 << N)
    for count in range(1, N + 1):
        for mask in range(1, 1 << N):
            if mask.bit_count() != count:
                continue
            player = ORDER[N - count]
            best = None
            for g in range(N):
                if not (mask & (1 << g)):
                    continue
                next_mask = mask ^ (1 << g)
                vec = list(values[next_mask]); vec[player] += WEIGHTS[player][g]
                item = (vec[player], -g)
                if best is None or item > best:
                    best = item
                    values[mask] = tuple(vec)
                    choices[mask] = g
                    b = list(bundles[next_mask]); b[player] |= (1 << g)
                    bundles[mask] = tuple(b)
    return values, choices, bundles

def value(player,mask):
    return sum(WEIGHTS[player][g] for g in range(N) if mask & (1 << g))

def exhaustive_history_solver(expected_choices):
    """Independently traverse every ordered history, without DP state caching."""
    nodes = 0
    terminals = 0
    def recursive(history, masks):
        nonlocal nodes, terminals
        nodes += 1
        turn = len(history)
        if turn == N:
            terminals += 1
            return masks
        player = ORDER[turn]
        used = 0
        for g in history:
            used |= 1 << g
        remaining = ((1 << N) - 1) ^ used
        best_result = None
        best_score = None
        chosen = -1
        for g in range(N):
            if remaining & (1 << g):
                child = list(masks)
                child[player] |= 1 << g
                result = recursive(history + (g,), tuple(child))
                score = value(player, result[player])
                if best_score is None or score > best_score:
                    best_score = score
                    chosen = g
                    best_result = result
        assert chosen == expected_choices[remaining], (history,chosen,expected_choices[remaining])
        return best_result
    root = recursive((), (0,0,0))
    assert nodes == 13700 and terminals == 5040, (nodes,terminals)
    return root, nodes, terminals

def main():
    data = json.loads(Path(__file__).with_name('DP_CERTIFICATE.json').read_text(encoding='utf-8'))
    assert data['valuation_matrix'] == [list(w) for w in WEIGHTS]
    assert data['turn_order_zero_based'] == list(ORDER)
    states = data['states']
    assert len(states) == 1 << N
    calculated, moves, bundles = solve()
    count_edges = 0
    for mask in range(1 << N):
        obj = states[mask]
        assert obj['remaining_mask'] == mask
        assert obj['choice_zero_based'] == moves[mask]
        assert tuple(obj['continuation_payoffs']) == calculated[mask]
        assert tuple(obj['allocated_masks']) == bundles[mask]
        assert sum(m.bit_count() for m in bundles[mask]) == mask.bit_count()
        assert sum(bundles[mask]) == mask
        for agent in range(3):
            assert calculated[mask][agent] == value(agent, bundles[mask][agent])
        if mask:
            player = ORDER[N - mask.bit_count()]
            maximizing = []
            for g in range(N):
                if mask & (1 << g):
                    count_edges += 1
                    child = mask ^ (1 << g)
                    score = calculated[child][player] + WEIGHTS[player][g]
                    maximizing.append((score, -g, g))
            assert moves[mask] == max(maximizing)[2]
    assert count_edges == N * (1 << (N - 1))
    path = []
    remaining = (1 << N) - 1
    while remaining:
        g = moves[remaining]
        path.append(g + 1)
        remaining ^= 1 << g
    assert path == [1, 2, 3, 5, 4, 6, 7], path
    assert bundles[127] == (81, 10, 36), bundles[127] # A: bits 0,4,6; B: bits 1,3; C: bits 2,5
    assert calculated[127] == (2090, 1120, 1042)
    full_history_result, visited_nodes, terminal_paths = exhaustive_history_solver(moves)
    assert full_history_result == bundles[127]
    agent = 1  # B, envies A after removing any one good.
    envy_set = bundles[127][0]
    other_goods = [g for g in range(N) if envy_set & (1 << g)]
    assert other_goods == [0, 4, 6]
    after_deletion = [value(agent, envy_set ^ (1 << g)) for g in other_goods]
    assert min(after_deletion) == 1286 > calculated[127][agent]
    # The low bits encode unique distinct subsets of goods for each agent.
    for agent in range(3):
        bundle_values = [value(agent, mask) for mask in range(1 << N)]
        assert len(set(bundle_values)) == 128
    print('PASS: 128 dynamic-program states and 448 state actions;')
    print('      independently exhausted 13700 game-history nodes and 5040 terminals;')
    print('      unique subset utilities for all 3 agents, the 7-pick SPNE path,')
    print('      allocations, and strict EF1 failure (minimum residual 1286 > 1120).')

if __name__ == '__main__':
    main()
