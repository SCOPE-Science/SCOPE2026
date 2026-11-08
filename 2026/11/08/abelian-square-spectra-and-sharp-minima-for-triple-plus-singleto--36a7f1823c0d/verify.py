"""Direct finite verification of a triple-plus-singleton Abelian-square theorem.

No dependencies beyond Python's standard library.
"""
from itertools import product


def literal_squares(word):
    answer = set()
    for half in range(1, len(word) // 2 + 1):
        for start in range(len(word) - 2 * half + 1):
            factor = word[start:start + 2 * half]
            if factor[:half].count('a') == factor[half:].count('a'):
                answer.add(factor)
    return answer


def described_squares(i, j, k):
    r = max(i, j, k)
    out = {'b' * (2 * t) for t in range(1, r // 2 + 1)}
    out.add('aa')
    u = min(j, k)
    out.update('a' + 'b' * j + 'a' + 'b' * y
               for y in range(u + 1) if (y - j) % 2 == 0)
    out.update('b' * (j + y) + 'aaa' + 'b' * j + 'a' + 'b' * y
               for y in range(k + 1) if j + y <= i)
    return out


def count_formula(i, j, k):
    u = min(j, k)
    f = u // 2 + 1 if j % 2 == 0 else (u + 1) // 2
    g = max(0, min(k, i - j) + 1)
    return max(i, j, k) // 2 + 1 + f + g - int(j == 0)


def witness(n):
    if n < 5:
        return (0, 0, 0)
    q, r = divmod(n, 4)
    if r == 0:
        return (2*q-3, 2*q-1, 0)
    if r == 1:
        return (2*q-2, 2*q-1, 0)
    if r == 2:
        return (2*q-1, 2*q-1, 0)
    return (2*q-2, 2*q+1, 0)


def main():
    tested = 0
    for i, j, k in product(range(19), repeat=3):
        w = 'b'*i + 'aaa' + 'b'*j + 'a' + 'b'*k
        actual = literal_squares(w)
        described = described_squares(i, j, k)
        assert actual == described, (i, j, k, actual ^ described)
        assert len(actual) == count_formula(i, j, k)
        assert 4*len(actual) >= i+j+k+3
        tested += 1
    for n in range(4, 41):
        minimum = 10**6
        for i in range(n-3):
            for j in range(n-3-i):
                k = n-4-i-j
                minimum = min(minimum, count_formula(i, j, k))
        target = 2 if n == 4 else (n+2)//4
        assert minimum == target, (n, minimum, target)
        i, j, k = witness(n)
        assert i+j+k+4 == n
        assert count_formula(i, j, k) == target, (n, i, j, k)
    print('PASS: 6859 triples, independent literal factor sets, counts, lower bounds')
    print('PASS: sharp minimum and constructive witnesses at every length 4..40')


if __name__ == '__main__':
    main()
