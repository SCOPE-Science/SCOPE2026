#!/usr/bin/env python3
"""Exact checks for the signed Euler characteristic of two-independence
complexes of squared cycles. Only Python standard-library modules are used.
"""

STATES = [tuple((q >> (3 - i)) & 1 for i in range(4)) for q in range(16)]
POS = {s: k for k, s in enumerate(STATES)}

def matrix():
    T = [[0] * 16 for _ in range(16)]
    for i, bits in enumerate(STATES):
        for incoming in (0, 1):
            window = bits + (incoming,)
            if not window[2] or sum(window[t] for t in (0, 1, 3, 4)) <= 1:
                j = POS[bits[1:] + (incoming,)]
                T[i][j] = 1 if incoming == 0 else -1
    return T

def multiply(A, B):
    size = len(A)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j, a in enumerate(A[i]):
            if a:
                for k, b in enumerate(B[j]):
                    if b:
                        result[i][k] += a * b
    return result

def traces(T, nmax):
    A = [[int(i == j) for j in range(16)] for i in range(16)]
    out = [16]
    for n in range(1, nmax + 1):
        A = multiply(A, T)
        out.append(sum(A[i][i] for i in range(16)))
    return out

def polynomial_from_traces(tr):
    # Newton identities: determinant(lambda I-T) = lambda^16+c1 lambda^15+...+c16.
    c = [1]
    for k in range(1, 17):
        numerator = -sum(c[k-j] * tr[j] for j in range(1, k+1))
        assert numerator % k == 0
        c.append(numerator // k)
    return c

def direct_valid(mask, n):
    for v in range(n):
        if mask & (1 << v):
            d = 0
            for step in (-2,-1,1,2):
                d += bool(mask & (1 << ((v+step) % n)))
            if d > 1:
                return False
    return True

def local_valid(mask, n):
    for i in range(n):
        if (mask >> i) & 1:
            bits = [((mask >> ((i+j) % n)) & 1) for j in (-2,-1,1,2)]
            if sum(bits) > 1:
                return False
    return True

def brute_sum(n):
    sum1 = 0
    sum2 = 0
    faces = 0
    for mask in range(1 << n):
        a = direct_valid(mask, n)
        b = local_valid(mask, n)
        assert a == b, (n, mask)
        if a:
            faces += 1
            sum1 += -1 if mask.bit_count() % 2 else 1
        if b:
            sum2 += -1 if mask.bit_count() % 2 else 1
    assert sum1 == sum2
    return sum1, faces

def main():
    T = matrix()
    tr = traces(T, 70)
    coeffs = polynomial_from_traces(tr)
    assert coeffs == [1,-1,0,1,-1,-1]+[0]*11, coeffs
    assert tr[5:17] == [6,10,8,1,-2,6,23,34,27,8,3,33]
    for n in range(1,64):
        assert tr[n+7] == tr[n+2]+2*tr[n+1]+tr[n]
    for n in range(5,17):
        signed, faces = brute_sum(n)
        assert tr[n] == signed, (n, signed, tr[n])
        print(f'n={n}, signed_sum={signed}, number_of_faces_including_empty={faces}')
    assert all(tr[n] > 0 for n in range(10,71))
    print('charpoly = x^11 * (x^5 - x^4 + x^2 - x - 1)')
    print('seven_step = z[n+7] - z[n+2] - 2*z[n+1] - z[n] = 0')
    print('bruteforce = independently checked 5<=n<=16')
    print('ALL_CHECKS_PASS')

if __name__ == '__main__':
    main()
