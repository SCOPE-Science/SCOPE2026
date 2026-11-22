"""Independent direct check of the binary two-cluster Abelian-square formula."""
from itertools import product


def predicted(a, b, c):
    assert a >= 0 and b >= 1 and c >= 0
    m = min(a, b)
    p = sum(x % 2 == b % 2 for x in range(m + 1))
    return max(a, b, c) // 2 + 1 + m + (b % 2 == 0) + p + (c >= b)


def direct(a, b, c):
    w = '0' * a + '11' + '0' * b + '111' + '0' * c
    n = len(w)
    squares = set()
    for h in range(1, n // 2 + 1):
        for i in range(n - 2*h + 1):
            x, y = w[i:i+h], w[i+h:i+2*h]
            if x.count('1') == y.count('1'):
                squares.add(x + y)
    return len(squares)


def predicted_minimizers(n):
    ans = []
    for a in range(n-5):
        for b in range(1, n-4-a):
            c = n - 5 - a - b
            if predicted(a, b, c) == (n+1)//4:
                ans.append((a, b, c))
    return ans


def characterized_minimizers(n):
    return [(0,b,n-5-b) for b in range(1,n-4)
            if b % 2 == 1 and (
                (n-5-b == b) or (b-4 <= n-5-b < b))]

if __name__ == '__main__':
    cases = 0
    for a,b,c in product(range(21),range(1,21),range(21)):
        assert predicted(a,b,c) == direct(a,b,c), (a,b,c)
        cases += 1
    print(f'direct-factor-enumeration PASS: {cases} triples')
    for n in range(6, 301):
        observed = predicted_minimizers(n)
        expected = characterized_minimizers(n)
        assert observed == expected, (n,observed,expected)
        assert observed
    print('all-length-parameter minimizers PASS: n=6..300 (295 lengths)')
    print('universal claims are proved by symbolic case distinction; finite tests only corroborate')
