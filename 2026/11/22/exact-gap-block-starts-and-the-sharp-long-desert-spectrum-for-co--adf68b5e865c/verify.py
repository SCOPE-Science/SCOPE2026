"""Direct reachability check of the triangular long-gap spectrum."""


def triangular(n):
    return n * (n + 1) // 2


def observed_long_blocks(n):
    a, b, c = (triangular(n + shift) for shift in range(3))
    represented = bytearray([1])
    streak = 1
    start = None
    blocks = []
    x = 1
    while streak < a:
        member = any(x >= s and represented[x - s] for s in (a, b, c))
        represented.append(member)
        if member:
            streak += 1
            if start is not None:
                if x - start > n + 1:
                    blocks.append((start, x - 1))
                start = None
        else:
            streak = 0
            if start is None:
                start = x
        x += 1
    return blocks


if __name__ == "__main__":
    total = 0
    for n in range(3, 41):
        a, c = triangular(n), triangular(n + 2)
        expected = [(q * c + 1, (q + 1) * a - 1) for q in range((n + 1) // 4)]
        actual = observed_long_blocks(n)
        if actual != expected:
            raise AssertionError((n, actual, expected))
        total += len(actual)
    print(f"PASS: n=3..40; {total} long blocks")
