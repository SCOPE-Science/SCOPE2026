"""Exact finite linear-algebra certificate and independent residue checks.

This standalone script requires Python 3 and only the standard library.
"""
from math import comb

Q = ((0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2))
A = (0, 0, 1, 0, 2, 0)
B = (0, 1, 2, 0, 0, 0)


def transition():
    m = [[0] * 18 for _ in range(18)]
    for i in range(6):
        for c in range(3):
            for j, (r, s) in enumerate(Q):
                t = (c + A[i] * r + B[i] * s) % 3
                m[3 * i + c][3 * j + t] += 1
    return m


def transfer_counts(max_length):
    m = transition()
    v = [0] * 18
    for i in range(6):
        v[3 * i] = 1
    ans = [1]
    for _ in range(max_length):
        ans.append(sum(v[3 * i] for i in range(6)))
        new = [0] * 18
        for i, vi in enumerate(v):
            if vi:
                for j, mij in enumerate(m[i]):
                    if mij:
                        new[j] += vi * mij
        v = new
    return ans


def exhaustive_check():
    # Independent Pascal rows modulo nine, with digitwise Lucas products.
    w = transfer_counts(25)
    for length in range(1, 7):
        bound = 3 ** length
        row = [1]
        good = 0
        all_good = 0
        for n in range(bound):
            nd = []
            x = n
            for _ in range(length):
                nd.append(x % 3)
                x //= 3
            for k, value in enumerate(row):
                x = k
                prod = 1
                for r in nd:
                    s = x % 3
                    x //= 3
                    if s > r:
                        prod = 0
                        break
                    prod *= comb(r, s)
                if prod % 9 == value:
                    all_good += 1
                    if prod:
                        good += 1
            row = [1] + [(row[j - 1] + row[j]) % 9 for j in range(1, len(row))] + [1]
        assert good == w[length], (length, good, w[length])
        exact_one = 0 if length == 1 else 9 * (length - 1) * 6 ** (length - 2)
        predicted_all = bound * (bound + 1) // 2 - 6 ** length - exact_one + w[length]
        assert all_good == predicted_all, (length, all_good, predicted_all)
        print(f'L={length}: W={good}; E={all_good}; checked {bound * (bound + 1) // 2} pairs')


def recurrence_certificate():
    # Sequence is a linear functional of powers of a 19x19 matrix
    # T=diag(M,6). Its characteristic polynomial has degree 19.
    # If q(T) is annihilated by the first 19 matrix-functional moments,
    # Cayley-Hamilton annihilates *all* subsequent moments. The zero-th
    # scalar recurrence is checked separately. This is a complete finite
    # linear-algebra proof, not extrapolation from sample values.
    w = transfer_counts(25)
    d = [3 * w[l] - 6 ** l for l in range(26)]
    assert d[:6] == [2, 12, 39, 153, 549, 2079], d[:6]
    residuals = [d[l + 6] - 6 * d[l + 5] + 45 * d[l + 3]
                 - 45 * d[l + 2] - 81 * d[l + 1] + 243 * d[l]
                 for l in range(20)]
    assert residuals == [0] * 20, residuals
    print('Cayley-Hamilton: twenty exact residuals 0, including base L=0; order-19 certificate verified')
    print('W_0..W_9:', w[:10])
    return w


if __name__ == '__main__':
    recurrence_certificate()
    exhaustive_check()
    print('PASS: all exact finite certificates and independent checks')
