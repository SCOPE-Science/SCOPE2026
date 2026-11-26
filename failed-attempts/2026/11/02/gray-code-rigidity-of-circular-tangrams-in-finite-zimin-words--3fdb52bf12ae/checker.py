"""Independent exhaustive finite check of circular tangrams in Zimin words.

Python 3 standard library only. Run `python checker.py`.
All cyclic starting positions and all even lengths up to the entire word are
examined through rank 8; this verifies examples, not the infinite theorem.
"""
from collections import Counter


def zimin(rank):
    word = ''
    for letter in range(rank):
        word = word + chr(ord('a') + letter) + word
    return word


def check(max_rank=8):
    for rank in range(1, max_rank + 1):
        word = zimin(rank)
        n = len(word)
        doubled = word + word
        parity_prefix = 0
        for pos, char in enumerate(word, 1):
            parity_prefix ^= 1 << (ord(char)-ord('a'))
            assert parity_prefix == (pos ^ (pos >> 1)), (rank, pos)
        expected = {(n - half, half) for half in range(1, n // 2 + 1)}
        even_parikh, abelian_squares = set(), set()
        for half in range(1, n // 2 + 1):
            for start in range(n):
                a = doubled[start:start + half]
                b = doubled[start + half:start + 2 * half]
                ab = a+b
                if all(count % 2 == 0 for count in Counter(ab).values()):
                    even_parikh.add((start, half))
                if Counter(a) == Counter(b):
                    abelian_squares.add((start, half))
        assert even_parikh == expected, (rank, 'even_parikh', even_parikh ^ expected)
        assert abelian_squares == expected, (rank, 'abelian_squares', abelian_squares ^ expected)
        print('rank', rank, 'length', n, 'tangrams', len(even_parikh),
              'abelian_squares', len(abelian_squares), 'expected', (n-1)//2)
    print('CHECKER_PASS')


if __name__ == '__main__':
    check()
