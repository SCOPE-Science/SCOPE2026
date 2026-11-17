"""Exact finite checks for online ranks of acyclic K_{2,b} edge-orientations.

No external libraries or remote data are required.  Infinite-parameter claims
are proved in the accompanying mathematical argument, not by this script.
"""
from functools import lru_cache
from itertools import product, combinations


def acyclic_by_dfs(columns):
    b = len(columns)
    adj = [[] for _ in range(b + 2)]
    for j, c in enumerate(columns):
        for i in (0, 1):
            if (c >> i) & 1:
                adj[i].append(j + 2)
            else:
                adj[j + 2].append(i)
    state = [0] * (b + 2)
    def dfs(v):
        state[v] = 1
        for w in adj[v]:
            if state[w] == 1 or (state[w] == 0 and not dfs(w)):
                return False
        state[v] = 2
        return True
    return all(state[v] or dfs(v) for v in range(b + 2))


def allowed(columns):
    return not (1 in columns and 2 in columns)


def orientation_rows(b):
    return [tuple(x) for x in product(range(4), repeat=b) if allowed(x)]


def rank_from_definition(rows, b):
    masks = []
    for j in range(b):
        for i in range(2):
            masks.append(sum(1 << k for k, row in enumerate(rows) if ((row[j] >> i) & 1)))
    @lru_cache(maxsize=None)
    def depth(version):
        if version.bit_count() <= 1:
            return 0
        best = 0
        for pos in masks:
            yes = version & pos
            if not yes or yes == version:
                continue
            no = version ^ yes
            best = max(best, 1 + min(depth(yes), depth(no)))
        return best
    answer = depth((1 << len(rows)) - 1)
    return answer, depth.cache_info().currsize


@lru_cache(maxsize=None)
def state_recurrence(u, a, b):
    choices = []
    if u:
        choices.append(1 + min(state_recurrence(u-1, a+1, b),
                               state_recurrence(u-1, a, b+1)))
    if a:
        choices.append(1 + min(state_recurrence(u, a-1, b), u+a-1))
    if b:
        choices.append(1 + min(state_recurrence(u, a, b-1), u+b-1))
    return max(choices, default=0)


def formula(u, a, b):
    return max(u+a, u+b, (3*u+a+b+1)//2)


def check_vc(rows, b):
    k = 2*b
    points = []
    for row in rows:
        points.append(sum(((row[j] >> i) & 1) << (2*j+i)
                          for j in range(b) for i in range(2)))
    best = 0
    for size in range(k+1):
        for support in combinations(range(k), size):
            traces = {tuple((row >> i) & 1 for i in support) for row in points}
            if len(traces) == (1 << size):
                best = max(best, size)
    return best



def conditional_formula_checks(rows, b):
    """Independently test every consistent partial assignment at small size."""
    query_masks = [sum(1 << k for k, row in enumerate(rows)
                       if (row[j] >> i) & 1)
                   for j in range(b) for i in range(2)]
    universe = (1 << len(rows)) - 1
    @lru_cache(None)
    def depth(version):
        if version.bit_count() <= 1:
            return 0
        result = 0
        for query in query_masks:
            yes = version & query
            if yes and yes != version:
                result = max(result, 1 + min(depth(yes), depth(version ^ yes)))
        return result
    examined = 0
    for state in product((0, 1, 2), repeat=2*b):
        # 0 = not queried, 1 = answer zero, 2 = answer one.
        version = universe
        for i, v in enumerate(state):
            if v == 1:
                version &= ~query_masks[i]
            elif v == 2:
                version &= query_masks[i]
        if not version:
            continue
        u = a = c = 0
        forced = None
        for j in range(b):
            z, w = state[2*j:2*j+2]
            if z == 0 and w == 0:
                u += 1
            elif z != 0 and w != 0:
                pattern = (z == 2) + 2*(w == 2)
                if pattern == 1:
                    forced = 1
                if pattern == 2:
                    forced = 2
            else:
                possibilities = {x for x in range(4)
                                 if (z == 0 or ((x & 1) == (z-1)))
                                 and (w == 0 or (((x>>1)&1) == (w-1)))}
                if 1 in possibilities:
                    a += 1
                elif 2 in possibilities:
                    c += 1
                else:
                    raise AssertionError(('wrong half-column', possibilities))
        expected = (u + (a if forced == 1 else c)
                    if forced is not None else formula(u, a, c))
        assert depth(version) == expected, (b, state, expected, depth(version))
        examined += 1
    return examined


def main():
    graph_cases = 0
    for b in range(1, 6):
        for col in product(range(4), repeat=b):
            assert acyclic_by_dfs(col) == allowed(col), (b, col)
            graph_cases += 1
    rec_cases = 0
    for u in range(0, 11):
        for a in range(0, 12):
            for b in range(0, 12):
                assert state_recurrence(u, a, b) == formula(u, a, b), (u,a,b)
                rec_cases += 1
    partials = sum(conditional_formula_checks(orientation_rows(b), b) for b in range(1,5))
    table = []
    for b in range(1, 8):
        rows = orientation_rows(b)
        result, states = rank_from_definition(rows, b)
        assert result == (3*b + 1)//2, (b, result)
        if b <= 5:
            assert check_vc(rows, b) == b+1, b
        table.append((b,len(rows),result,states))
    print('ACYCLIC_K2B_ONLINE_PASS', 'graph_patterns', graph_cases,
          'recurrence_states',rec_cases,'partial_states',partials,'ranks',table)


if __name__ == '__main__':
    main()
