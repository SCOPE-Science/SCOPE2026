"""Direct combinatorial enumeration independent of the transfer-state graph.

The outer cycle colors determine the inner colors if each vertex is to
have exactly one neighbor of the opposite color.
"""


def valid_color(a, b):
    n = len(a)
    return all(
        sum((a[(i-1) % n] != a[i], a[(i+1) % n] != a[i], b[i] != a[i])) == 1
        and sum((b[(i-2) % n] != b[i], b[(i+2) % n] != b[i], a[i] != b[i])) == 1
        for i in range(n)
    )


def direct(n):
    configurations = []
    for bits in range(1 << n):
        a = tuple((bits >> i) & 1 for i in range(n))
        b = []
        for i in range(n):
            outer_opposite = int(a[(i-1) % n] != a[i]) + int(a[(i+1) % n] != a[i])
            if outer_opposite > 1:
                break
            b.append(a[i] ^ (1 - outer_opposite))
        if len(b) == n and valid_color(a, b):
            configurations.append((a, tuple(b)))
    return configurations


def predicted(n):
    out = set()
    for a_value in (0, 1):
        out.add((tuple([a_value] * n), tuple([1 - a_value] * n)))
    if n % 5 == 0:
        aa = (1, 0, 0, 1, 1)
        bb = (1, 0, 0, 1, 0)
        for shift in range(5):
            for complement in (0, 1):
                out.add((
                    tuple(aa[(i + shift) % 5] ^ complement for i in range(n)),
                    tuple(bb[(i + shift) % 5] ^ complement for i in range(n)),
                ))
    return out


for n in range(5, 20):
    actual = set(direct(n))
    expect = predicted(n)
    assert actual == expect, (n, actual - expect, expect - actual)
    print(f'n={n} checked_outer_assignments={1 << n} exact_labeled_colorings={len(actual)}')
print('DIRECT_VERIFIED')
