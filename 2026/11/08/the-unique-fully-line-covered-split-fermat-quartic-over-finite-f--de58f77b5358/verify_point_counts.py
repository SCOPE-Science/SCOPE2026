"""Exact arithmetic counts of rational points on the Fermat quartic.

For F_(p^2), the internal representation a+b*p denotes a+b*t,
where t^2=d is a nonsquare in F_p. No external packages required.
"""
from collections import Counter


class Field:
    def __init__(self, p, d=None):
        self.p, self.d = p, d
        if d is not None:
            assert pow(d, (p - 1) // 2, p) == p - 1
        self.q = p if d is None else p * p
        self.add = [[0] * self.q for _ in range(self.q)]
        self.mul = [[0] * self.q for _ in range(self.q)]
        for a in range(self.q):
            for b in range(self.q):
                if d is None:
                    self.add[a][b] = (a + b) % p
                    self.mul[a][b] = (a * b) % p
                else:
                    x, y, z, w = a % p, a // p, b % p, b // p
                    self.add[a][b] = (x + z) % p + p * ((y + w) % p)
                    self.mul[a][b] = (x*z + d*y*w) % p + p * ((x*w + y*z) % p)
        self.neg = [next(y for y in range(self.q) if self.add[x][y] == 0)
                    for x in range(self.q)]
        self.fourth = [self.mul[self.mul[x][x]][self.mul[x][x]]
                       for x in range(self.q)]


def count_surface(field):
    """Count the charts x3=1, x3=0 x2=1, x3=x2=0 x1=1.

    A(s)=#{(x,y): x^4+y^4=s}; c(t)=#{x:x^4=t}.
    Thus affine chart is sum_s A(s)c(-1-s), the first infinity
    chart is A(-1), and the final infinity chart is c(-1).
    """
    f = field
    c = Counter(f.fourth)
    A = Counter()
    for u, n in c.items():
        for v, m in c.items():
            A[f.add[u][v]] += n * m
    minus_one = f.neg[1]
    affine = sum(n * c[f.add[minus_one][f.neg[s]]]
                 for s, n in A.items())
    infinity = A[minus_one] + c[minus_one]
    return affine + infinity, affine, infinity


def main():
    known = [(17, None, 600), (5, 2, 1112),
             (41, None, 2520), (7, 3, 3480)]
    for p, d, expected in known:
        f = Field(p, d)
        actual, affine, infinity = count_surface(f)
        assert actual == expected, (p, d, actual)
        q = f.q
        assert actual - (48*q - 216) == {17: 0, 25: 128,
                                         41: 768, 49: 1344}[q]
        print(f"F_{q}: X={actual}, affine={affine}, infinity={infinity}, "
              f"outside_48_lines={actual-48*q+216}")
    print("VERIFY_POINT_COUNTS_OK")


if __name__ == '__main__':
    main()
