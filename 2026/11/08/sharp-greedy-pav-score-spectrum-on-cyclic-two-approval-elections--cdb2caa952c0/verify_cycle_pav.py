"""Standalone exhaustive verifier for cycle-edge PAV versus greedy PAV.
Run: python verify_cycle_pav.py (standard library only).
All ties retained, all subsets considered; fractions are exact halves.
"""


def direct_twice_score(mask, n):
    # voter i approves the two adjacent candidates i-1 and i
    total = 0
    for i in range(n):
        num = ((mask >> i) & 1) + ((mask >> ((i - 1) % n)) & 1)
        total += (0, 2, 3)[num]
    return total


def adjacency(mask, n):
    return sum(bool(mask & (1 << i) and mask & (1 << ((i + 1) % n))) for i in range(n))


def theoretical_score_twice(mask, n):
    return 4 * mask.bit_count() - adjacency(mask, n)


def run():
    checked = 0
    for n in range(3, 16):
        reachable = {0}
        reached_maximal_independent_sizes = set()
        for k in range(n + 1):
            # Confirm exact welfare formula from voter-level harmonic utilities.
            for mask in reachable:
                checked += 1
                assert direct_twice_score(mask, n) == theoretical_score_twice(mask, n)
            opt = max(direct_twice_score(mask, n) for mask in range(1 << n) if mask.bit_count() == k)
            assert opt == 4*k - max(0, 2*k-n)
            c = (n+2)//3
            min_g = min(direct_twice_score(mask, n) for mask in reachable)
            gap = max(0, min(k, n-k)-c)
            expected_min = opt - gap
            assert min_g == expected_min, (n,k,min_g,expected_min)
            spectrum = {direct_twice_score(mask, n) for mask in reachable}
            assert spectrum == {opt-j for j in range(gap+1)}, (n,k,spectrum)
            if n <= 5:
                assert min_g == opt
            if n == 6 and k == 3:
                assert opt == 12 and min_g == 11
            if k == n: break
            next_states = set()
            for mask in reachable:
                # Marginal score computed directly, not via adjacency shortcut.
                gains = [(direct_twice_score(mask | (1 << j), n) - direct_twice_score(mask,n), j)
                         for j in range(n) if not (mask >> j) & 1]
                best = max(x for x,j in gains)
                if best < 4 and adjacency(mask, n) == 0:
                    reached_maximal_independent_sizes.add(k)
                for gain,j in gains:
                    if gain == best: next_states.add(mask | (1 << j))
            reachable = next_states
        assert reached_maximal_independent_sizes == set(range((n+2)//3, n//2+1)), (n,reached_maximal_independent_sizes)
    print('PASS: direct voter scores, all greedy tie paths, optimal scores, and sharp minimum, n=3..15')
    print('Reachable-state assessments:',checked)
    print('Global lower bound 11/12 is attained at n=6,k=3 and at n divisible by six, k=n/2.')

if __name__ == '__main__':
    run()
