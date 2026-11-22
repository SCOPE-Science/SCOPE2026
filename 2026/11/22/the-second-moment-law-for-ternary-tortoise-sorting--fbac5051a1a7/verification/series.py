"""Binary-block enumeration and all-length series identity checks.

Run: python3 verification/series.py
No third-party dependencies.
"""
from itertools import product


def binary_fertility(word):
    if not word.count('1'):
        return 1
    return len(word) - len(word.lstrip('0')) + 1 if word.endswith('1') else 0


def double_fertility(word):
    return sum(binary_fertility(word[:i]) * binary_fertility(word[i:])
               for i in range(len(word) + 1))


def c_closed(word):
    h = len(word) - len(word.lstrip('0'))
    if '1' not in word:
        return len(word) + 1
    if word.endswith('0'):
        return h + 1
    L = len(word) - h
    return (h + 1) * (2 * L + h + 2) // 2


def convolve(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return result


def rational_coeff(numerator, denominator, count):
    a = []
    for n in range(count):
        q = (numerator[n] if n < len(numerator) else 0)
        q -= sum(denominator[j] * a[n-j]
                 for j in range(1, min(n, len(denominator)-1)+1))
        assert q % denominator[0] == 0
        a.append(q//denominator[0])
    return a


def main():
    # B2=(1-2z+3z^2)/((1-z)^2(1-2z)),
    # C2=(1+z+6z^2)/((1-z)(1-2z)^3).
    bden = convolve([1,-2,1], [1,-2])
    cden = convolve([1,-1], convolve([1,-2],convolve([1,-2],[1,-2])))
    b = rational_coeff([1,-2,3], bden, 81)
    c = rational_coeff([1,1,6], cden, 81)
    tested = 0
    for n in range(13):
        by_enum_b = 0
        by_enum_c = 0
        for letters in product('01', repeat=n):
            word = ''.join(letters)
            f = binary_fertility(word)
            d = double_fertility(word)
            assert d == c_closed(word), word
            by_enum_b += f*f
            by_enum_c += d*d
            tested += 1
        assert (by_enum_b, by_enum_c) == (b[n], c[n]), n

    # R=B2+z C2/(1-z B2).  The recurrence below is independent
    # of brute-force ternary enumeration and of symbolic simplification.
    r=[]
    for n in range(81):
        if n==0:
            r.append(b[0]); continue
        value = b[n] + c[n-1]
        value += sum(b[j] * (r[n-j-1]-b[n-j-1]) for j in range(n))
        r.append(value)
    num = [1, -8, 32, -68, 83, -60, 24]
    den = convolve(convolve([1,-2,1], [1,-4,4]), [1,-5,7,-5])
    direct = rational_coeff(num, den, 81)
    assert r == direct
    print('PASS: exhaustive binary blocks of lengths 0..12:',tested)
    print('PASS: two rational coefficient constructions through degree 80')
    print('collision sums:', *direct[:10])


if __name__ == '__main__':
    main()
