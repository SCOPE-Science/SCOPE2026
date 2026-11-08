"""Finite checks for a binary uniform-substitution Abelian-period theorem.

The infinite statements follow from the accompanying mathematical proof, not
from the enumerated finite instances.
"""

def fixed_prefix(a, b, required):
    blocks = ('0' * a + '1' * b, '1' * b + '0' * a)
    w = '0'
    while len(w) < required:
        w = ''.join(blocks[int(x)] for x in w)
    return w


def predicted_period(a, b, c, t):
    L = a + b
    q, r = divmod(c, L)
    if r == 0:
        return True
    for _ in range(t - 1):
        d, q = q % L, q // L
        if min(a, b) <= d < max(a, b):
            return True
    return False


def check():
    tests = 0
    for a in range(1, 5):
        for b in range(1, 5):
            L = a + b
            for t in range(1, 4):
                p = L ** t
                max_c = 3 * L**2 + L - 1
                sample = fixed_prefix(a, b, max_c + 22 * p + 1)
                ones = [0]
                for x in sample:
                    ones.append(ones[-1] + int(x))
                for c in range(max_c + 1):
                    counts = {ones[c + (j + 1) * p] - ones[c + j * p]
                              for j in range(20)}
                    actual_first_20_blocks = len(counts) == 1
                    assert actual_first_20_blocks == predicted_period(a, b, c, t), (a, b, c, t)
                    tests += 1

    # Verify the exact census for every small parameter and power.
    census_tests = 0
    for a in range(1, 6):
        for b in range(1, 6):
            L = a + b
            S = 2 * min(a, b)
            for t in range(1, 5):
                count = sum(predicted_period(a, b, c, t) for c in range(L ** t))
                assert count == L ** t - (L - 1) * S ** (t - 1)
                census_tests += 1

    print(f'PASS: {tests} finite block comparisons and {census_tests} exact shift censuses')

if __name__ == '__main__':
    check()
