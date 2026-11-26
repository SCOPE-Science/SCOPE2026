#!/usr/bin/env python3
"""Exact checks for the balanced-pair-insertion degree of Dyck words.

No external modules or downloaded data are used.
"""
from math import comb
from collections import Counter


def catalan(n):
    return comb(2*n, n) // (n+1)


def dyck_words(n):
    def walk(word, up, down):
        if down == n:
            yield word
            return
        if up < n:
            yield from walk(word + 'U', up+1, down)
        if down < up:
            yield from walk(word + 'D', up, down+1)
    yield from walk('', 0, 0)


def valid_dyck(word):
    height = 0
    for char in word:
        height += 1 if char == 'U' else -1
        if height < 0:
            return False
    return height == 0


def direct_updegree(word):
    answers = set()
    for i in range(len(word)+1):
        inserted_up = word[:i] + 'U' + word[i:]
        for j in range(len(inserted_up)+1):
            candidate = inserted_up[:j] + 'D' + inserted_up[j:]
            if valid_dyck(candidate):
                answers.add(candidate)
    return len(answers)


def component_sizes(word):
    result, height, last = [], 0, 0
    for index, char in enumerate(word):
        height += 1 if char == 'U' else -1
        if height == 0:
            result.append((index+1-last)//2)
            last = index+1
    assert last == len(word)
    return result


def predicted_degree(sizes):
    return 1 + sum(a*a for a in sizes) + sum(
        sizes[i]*sizes[j] for i in range(len(sizes)) for j in range(i+1, len(sizes))
    )


def deficit(sizes):
    return sum(sizes[i]*sizes[j] for i in range(len(sizes))
               for j in range(i+1, len(sizes)))


def target_sum_deficit(n):
    return 4**n//2 - 3*comb(2*n, n)//2 + catalan(n)


def check():
    total_checked = 0
    for n in range(1, 9):
        sum_q = 0
        num = 0
        histogram = Counter()
        for word in dyck_words(n):
            sizes = component_sizes(word)
            value = direct_updegree(word)
            assert value == predicted_degree(sizes), (word, value, sizes)
            q = deficit(sizes)
            assert value == n*n + 1 - q
            sum_q += q
            histogram[n-max(sizes)] += 1
            num += 1
        assert num == catalan(n)
        assert sum_q == target_sum_deficit(n), (n, sum_q, target_sum_deficit(n))
        for r, count in histogram.items():
            if n > 2*r:
                assert count == catalan(n-r-1)*catalan(r+1), (n,r,count)
        total_checked += num
        print(f'n={n} words={num} sum_deficit={sum_q} max_deficit={max(deficit(component_sizes(w)) for w in dyck_words(n))}')
    # Independently count total pairwise component-product using append recurrences.
    F, G = [1], [0]
    for n in range(1, 151):
        f = 0
        g = 0
        for a in range(1, n+1):
            factor = catalan(a-1)
            f += factor*F[n-a]
            g += factor*(G[n-a] + a*(n-a)*F[n-a])
        assert f == catalan(n)
        assert g == target_sum_deficit(n)
        F.append(f)
        G.append(g)
    print(f'VERIFY_OK: {total_checked} literal Dyck words; exact aggregate identity n=1..150; fixed-r identity checked where n>2r')

if __name__ == '__main__':
    check()
