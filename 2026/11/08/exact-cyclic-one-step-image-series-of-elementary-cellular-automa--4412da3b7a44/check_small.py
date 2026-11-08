"""Independent exhaustive check for indexed cyclic ECA Rule 73 images."""

def step(x, n):
    out = 0
    for i in range(n):
        left = (x >> ((i - 1) % n)) & 1
        center = (x >> i) & 1
        right = (x >> ((i + 1) % n)) & 1
        out |= ((73 >> (4 * left + 2 * center + right)) & 1) << i
    return out


def brute():
    reference = (2, 2, 5, 12, 17, 34, 79, 140, 275, 544, 992, 1950, 3668, 6983, 13345, 25156)
    for n in range(1, 17):
        images = {step(x, n) for x in range(1 << n)}
        assert len(images) == reference[n - 1], (n, len(images), reference[n - 1])
    print('BRUTE_OK: all 2^n inputs independently mapped for n=1..16')


if __name__ == '__main__':
    brute()
