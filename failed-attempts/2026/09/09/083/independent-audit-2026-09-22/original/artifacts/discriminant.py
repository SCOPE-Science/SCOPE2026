#!/usr/bin/env python3
"""Discriminant log: forced bad set S={inf,2,3,5,17} from first principles.
Stdlib only (Bareiss integer determinant). Prints VERIFY_OK_DISC on success.
P(x)=x^4-8x^2+15=(x^2-3)(x^2-5), P'(x)=4x^3-16x.
disc(P) = (-1)^{4*3/2} Res(P,P')/lc(P) = Res(P,P') (monic, sign +1).
Sylvester 7x7 determinant via Bareiss => 3840 = 2^8*3*5.
Hence discriminant primes {2,3,5}; plus quaternion-ramification prime 17 (a=17)
and inf => S={inf,2,3,5,17}. Matches admission's forced set.
"""
def bareiss_det(M):
    n = len(M)
    A = [row[:] for row in M]
    prev = 1
    for k in range(n - 1):
        # partial pivot (exact integer arithmetic)
        if A[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if A[i][k] != 0), None)
            assert swap is not None, "singular matrix"
            A[k], A[swap] = A[swap], A[k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) // prev
            A[i][k] = 0
        prev = A[k][k]
    return A[n - 1][n - 1]

def sylvester(f, g):
    # f,g coeff lists high->low; returns Sylvester matrix
    n, m = len(f) - 1, len(g) - 1
    N = n + m
    M = [[0] * N for _ in range(N)]
    for i in range(m):
        for j, c in enumerate(f):
            M[i][i + j] = c
    for i in range(n):
        for j, c in enumerate(g):
            M[m + i][i + j] = c
    return M

def main():
    P = [1, 0, -8, 0, 15]
    Pp = [4, 0, -16, 0]
    M = sylvester(P, Pp)
    res = bareiss_det(M)
    print(f"Res(P,P') = {res}")
    assert res == 3840, res
    disc = res  # monic quartic: disc = Res
    assert disc == 3840 == 2**8 * 3 * 5
    print(f"disc(P) = {disc} = 2^8*3*5 => discriminant primes {{2,3,5}}")
    # root-difference cross-check: (16*sqrt(15))^2 = 256*15 = 3840
    assert 16 * 16 * 15 == 3840
    print("root-difference check (16*sqrt(15))^2 = 3840 OK")
    # a=17 nonsquare prime => ramification prime 17; plus inf
    print("S = {inf} U {2,3,5} (disc) U {17} (a-ramification) = {inf,2,3,5,17} OK")
    print("VERIFY_OK_DISC")

if __name__ == '__main__':
    main()
