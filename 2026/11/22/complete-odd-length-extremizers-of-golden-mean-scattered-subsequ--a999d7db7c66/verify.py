#!/usr/bin/env python3
"""Exact finite checks for golden-mean scattered-subsequence cover extremizers.
Independent of the mathematical proof; no computational extrapolation is used.
"""
from itertools import combinations


def targets(k):
    out = []
    def visit(word):
        if len(word) == k:
            out.append(word)
        else:
            visit(word + '0')
            if not word or word[-1] == '0':
                visit(word + '1')
    visit('')
    return out


def contains_subsequence(pattern, host):
    j = 0
    for letter in host:
        if j < len(pattern) and letter == pattern[j]:
            j += 1
    return j == len(pattern)


def proposed(k):
    if k % 2 == 0:
        return { '010' * (k // 2) }
    m = k // 2
    return {('010' * j) + '10' + ('010' * (m - j))
            for j in range(m + 1)} | {('010' * m) + '01'}


def brute_hosts(k):
    length = k + (k+1) // 2
    one_count = (k+1) // 2
    full_targets = targets(k)
    one_targets = ['0'*j + '1' + '0'*(k-1-j) for j in range(k)]
    chosen = set()
    single_only = set()
    checked = 0
    for inds in combinations(range(length), one_count):
        bits = ['0'] * length
        for i in inds:
            bits[i] = '1'
        host = ''.join(bits)
        checked += 1
        if all(contains_subsequence(t, host) for t in one_targets):
            single_only.add(host)
        if all(contains_subsequence(t, host) for t in full_targets):
            chosen.add(host)
    return checked, chosen, single_only


def run():
    total_hosts = 0
    total_patterns = 0
    for k in range(1, 13):
        tested, found, just_single = brute_hosts(k)
        claimed = proposed(k)
        assert found == claimed, (k, found ^ claimed)
        assert just_single == claimed, (k, just_single ^ claimed)
        assert len(found) == (1 if k % 2 == 0 else (k+3)//2)
        assert all('11' not in w for w in found)
        total_hosts += tested
        total_patterns += len(targets(k))
        print(f'EXHAUSTIVE k={k}: checked_hosts={tested}; admissible_targets={len(targets(k))}; optima={len(found)}')
    for k in range(13, 21):
        ts = targets(k)
        pp = proposed(k)
        for w in pp:
            assert len(w) == k + (k+1)//2
            assert w.count('0') == k and w.count('1') == (k+1)//2
            assert '11' not in w
            assert all(contains_subsequence(u, w) for u in ts)
        print(f'CONSTRUCTIONS k={k}: targets={len(ts)}; optima_constructed={len(pp)}')
    print(f'VERIFY_OK exhaustive_candidates={total_hosts} target_patterns_sum={total_patterns} construction_max_k=20')

if __name__ == '__main__':
    run()
