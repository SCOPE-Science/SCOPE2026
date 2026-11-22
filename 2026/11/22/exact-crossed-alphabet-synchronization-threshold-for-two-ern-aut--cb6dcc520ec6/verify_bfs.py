"""Exact full-subset-graph reset-threshold check for crossed binary automata."""
from collections import deque
from functools import reduce


def image_table(n, rotate_letter):
    full = 1 << n
    return [
        [
            reduce(int.__or__, (1 << (((i + 1) % n) if rotate_letter else (0 if i == n-1 else i))
                for i in range(n) if mask & (1 << i)), 0)
            for mask in range(full)
        ]
    ][0]


def witness(n):
    # a rotates the first coordinate, b rotates the second.
    first_a = image_table(n, True)
    first_b = image_table(n, False)
    second_a = first_b
    second_b = first_a
    maps = ((first_a, second_a), (first_b, second_b))
    full = (1 << n)-1
    start = (full, full)
    queue = deque([start])
    parent = {start: None}
    edge = {}
    while queue:
        x, y = queue.popleft()
        if x.bit_count() == y.bit_count() == 1:
            word = []
            node = (x, y)
            while parent[node] is not None:
                word.append(edge[node])
                node = parent[node]
            return ''.join(reversed(word)), len(parent)
        for symbol, (F, G) in enumerate(maps):
            node = (F[x], G[y])
            if node not in parent:
                parent[node] = (x, y)
                edge[node] = 'ab'[symbol]
                queue.append(node)
    raise AssertionError('No common reset word')


def explicit(n):
    if n == 2:
        return 'ab'
    if n == 3:
        return 'abbaab'
    if n == 4:
        return 'abbaaabaaabbba'
    return ('abb' + ('a'*(n-1)+'b')*(n-3) + 'aa'
            + ('b'*(n-1)+'a')*(n-5)
            + 'b'*(n-1)+'aa'+'b'*(n-1)+'a')


def reset_on_both(word, n):
    first = set(range(n)); second = set(range(n))
    for ch in word:
        first = {(i+1)%n if ch == 'a' else (0 if i == n-1 else i) for i in first}
        second = {(i+1)%n if ch == 'b' else (0 if i == n-1 else i) for i in second}
    return len(first) == len(second) == 1


def main():
    for n in range(2, 10):
        word, states = witness(n)
        formula = 2*(n*n-3*n+3)
        assert len(word) == formula == len(explicit(n))
        assert reset_on_both(word, n) and reset_on_both(explicit(n), n)
        print(f'n={n} shortest={len(word)} explored={states} witness={word}')
    print('VERIFY_BFS_OK: all eight full-powerset searches n=2..9')


if __name__ == '__main__':
    main()
