"""Independent finite checks for quotient-state spectrum of two-run conjugate languages.

Usage: python3 verify_circular_dfa.py
No nonstandard packages or network dependencies.
"""
from collections import defaultdict
from random import Random


def brute_quotients(a, b):
    w = '0' * a + '1' * b
    n = a + b
    words = set(w[i:] + w[:i] for i in range(n))
    assert len(words) == n
    result = []
    for j in range(n):
        residuals = defaultdict(set)
        for word in words:
            residuals[word[:j]].add(word[j:])
        result.append(len({frozenset(z) for z in residuals.values()}))
    return result


def minimized_trie_states(a, b):
    w = '0' * a + '1' * b
    n = a + b
    words = set(w[i:] + w[:i] for i in range(n))
    nodes = [{}]
    for word in words:
        p = 0
        for c in word:
            if c not in nodes[p]:
                nodes[p][c] = len(nodes)
                nodes.append({})
            p = nodes[p][c]
        nodes[p]['accept'] = True
    state_ids = {}
    def visit(node):
        e = nodes[node]
        if 'accept' in e:
            key = (True, None, None)
        else:
            key = (False, visit(e['0']) if '0' in e else -1,
                          visit(e['1']) if '1' in e else -1)
        if key not in state_ids:
            state_ids[key] = len(state_ids)
        return state_ids[key]
    visit(0)
    return len(state_ids) + 1   # absorbing dead state


def predicted_layers(a, b):
    n = a + b
    return [1] + [2 * min(j, a, b, n-j) for j in range(1, n)]


def counted_layers(a, b):
    n = a + b
    counts = [1]
    for j in range(1, n):
        t = n-j
        A = max(a-j+1, 0)
        B = max(b-j+1, 0)
        u = max(a-t+1, 0) - int(j == b)
        v = max(b-t+1, 0) - int(j == a)
        assert u >= 0 and v >= 0
        counts.append(n-A-B-max(u-1, 0)-max(v-1, 0)+int(A>0)+int(B>0))
    return counts


def run():
    checks = 0
    for a in range(1, 23):
        for b in range(1, 23):
            direct = brute_quotients(a,b)
            pred = predicted_layers(a,b)
            counted = counted_layers(a,b)
            assert direct == pred == counted, (a, b, direct, pred, counted)
            assert 2 + sum(direct) == 2*a*b + 3
            assert minimized_trie_states(a,b) == 2*a*b + 3
            checks += 1
    rng = Random(20261107)
    for _ in range(150):
        a = rng.randrange(1, 101)
        b = rng.randrange(1, 101)
        assert brute_quotients(a,b) == predicted_layers(a,b) == counted_layers(a,b)
        checks += 1
    print('VERIFY_OK', checks, 'independent parameter instances; complete quotient-layer and trie-minimalization checks (a,b<=22); further seeded pairs (a,b<=100)')


if __name__ == '__main__':
    run()
