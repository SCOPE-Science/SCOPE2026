"""Reproduce finite checks for the adjacent-pair spectrum of generalized Stirling words.
Requires Python 3.9+; no dependencies.
"""
from collections import Counter, defaultdict
from math import factorial, prod


def stirling_words(k, n):
    words = [tuple([1] * k)]
    for j in range(2, n + 1):
        block = (j,) * k
        words = [word[:i] + block + word[i:]
                 for word in words for i in range(len(word) + 1)]
    return words


def profile(word):
    return tuple(sorted(Counter(zip(word, word[1:])).items()))


def recursive_fiber(profile_key, k, n):
    """Derive a fiber size from counts only, not from a representative word."""
    counts = Counter(dict(profile_key))
    fiber = 1
    for j in range(n, 1, -1):
        assert counts[(j, j)] == k - 1
        outgoing = [(v, counts[(j, v)]) for v in range(1, j) if counts[(j, v)]]
        incoming = [(v, counts[(v, j)]) for v in range(1, j) if counts[(v, j)]]
        assert len(outgoing) <= 1 and len(incoming) <= 1
        assert sum(a for _, a in outgoing) <= 1
        assert sum(a for _, a in incoming) <= 1
        assert incoming or outgoing
        lower = counts.copy()
        for pair in list(lower):
            if j in pair:
                del lower[pair]
        if incoming and outgoing:
            a = incoming[0][0]
            b = outgoing[0][0]
            lower[(a, b)] += 1
            fiber *= lower[(a, b)]
        else:
            # With k copies of every smaller label, indegree k-1 marks the
            # initial symbol and outdegree k-1 marks the final symbol.
            first = [a for a in range(1, j)
                     if k - sum(lower[(b, a)] for b in range(1, j)) == 1]
            last = [a for a in range(1, j)
                    if k - sum(lower[(a, b)] for b in range(1, j)) == 1]
            assert len(first) == len(last) == 1
            if outgoing:
                assert outgoing[0][0] == first[0]
            else:
                assert incoming[0][0] == last[0]
        counts = +lower
    assert counts == Counter({(1, 1): k - 1})
    return fiber


def check(k, n):
    words = stirling_words(k, n)
    grouped = defaultdict(list)
    for word in words:
        grouped[profile(word)].append(word)
    assert len(words) == prod(k * j + 1 for j in range(1, n))
    assert all(len(ws) == recursive_fiber(pr, k, n) for pr, ws in grouped.items())
    max_fiber = max(map(len, grouped.values()))
    assert max_fiber == (k - 1) ** (n - 1)
    if k >= 3:
        largest = [pr for pr, ws in grouped.items() if len(ws) == max_fiber]
        if n > 1:
            assert len(largest) == 1
        singleton = [word for ws in grouped.values() if len(ws) == 1 for word in ws]
        assert len(singleton) == factorial(n)
        def contiguous(word):
            return all(any(word[i:i+k] == (j,) * k for i in range(len(word)-k+1))
                       for j in range(1, n+1))
        assert all((len(grouped[profile(w)]) == 1) == contiguous(w) for w in words)
    else:
        assert len(grouped) == len(words)
    return (k, n, len(words), len(grouped), max_fiber,
            sum(len(ws) == 1 for ws in grouped.values()))


if __name__ == '__main__':
    parameters = [(2, n) for n in range(1, 6)]
    parameters += [(3, n) for n in range(1, 6)]
    parameters += [(4, n) for n in range(1, 6)]
    parameters += [(5, n) for n in range(1, 5)]
    for args in parameters:
        print('k n words profiles worst singleton_profiles:', *check(*args))
    print('PASS: direct sources, profile-only recurrence, all claimed finite consequences')
