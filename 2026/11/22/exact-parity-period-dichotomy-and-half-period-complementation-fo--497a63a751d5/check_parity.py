"""Exact finite-field checks for the parity of generalized Pell recurrences.

Uses integer-bitset arithmetic over F_2; no external dependencies.
The infinite theorem in RESULT.md is proved algebraically, not by this program.
"""


def degree(poly):
    return poly.bit_length() - 1


def rem(poly, divisor):
    while poly and degree(poly) >= degree(divisor):
        poly ^= divisor << (degree(poly) - degree(divisor))
    return poly


def gcd(a, b):
    while b:
        a, b = b, rem(a, b)
    return a


def derivative(poly):
    out = 0
    for j in range(1, degree(poly) + 1, 2):
        if poly >> j & 1:
            out ^= 1 << (j - 1)
    return out


def charpoly(k):
    return (1 << k) | ((1 << (k - 1)) - 1)


def cycle(k, cutoff=1_000_000):
    state = 1  # newest value is bit 0; older values occupy bits 1,...,k-1
    mask = (1 << k) - 1
    ones = 0
    values = []
    for t in range(cutoff):
        values.append(state & 1)
        ones += state & 1
        new = ((state >> 1).bit_count()) & 1
        state = ((state << 1) & mask) | new
        if state == 1:
            return t + 1, ones, values
    raise RuntimeError(f"State period for k={k} exceeded {cutoff}")


def run():
    table = []
    for k in range(2, 19):
        c = charpoly(k)
        g = gcd(c, derivative(c))
        expected = 0b101 if k % 4 == 2 else 1
        assert g == expected, (k, hex(g), hex(expected))
        T, ones, values = cycle(k)
        assert (T % 2 == 0) == (k % 4 == 2)
        if k % 4 == 2:
            assert T % 4 == 2
            assert ones * 2 == T
            assert all(values[i] ^ values[i + T // 2] == 1 for i in range(T // 2))
        else:
            assert T % 2 == 1 and ones * 2 != T
        table.append((k, T, ones, T - ones))
    for k in range(19, 501):
        c = charpoly(k)
        g = gcd(c, derivative(c))
        assert g == (0b101 if k % 4 == 2 else 1), k
    print("K_PELL_PARITY_OK exact cycles k=2..18; squarefree/gcd k=2..500")
    print("k, least period, ones, zeros")
    for r in table:
        print(*r, sep=",")


if __name__ == "__main__":
    run()
