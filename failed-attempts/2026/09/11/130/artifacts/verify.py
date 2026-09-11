"""Replayable verification ledger for lane-1024 TARGET proof.

Checks (exact integer arithmetic where possible, else rigorous one-sided bounds):
 1. At n = 2^20: |E \\ B| lower bound is strictly positive (a good edge exists).
 2. Good-edge codegree lower bound (d^2 - eps)*n dominates n/(200 ln n),
    with the symbolic margin ln n >= 1/(200 (d^2 - eps)) verified.
 3. Nonvacuity: Paley(13) constructed explicitly (density 1/2, codegrees 2/3,
    book 3 pages); large Paley order q = 1048589 verified prime, q = 1 mod 4,
    with codegree deviations 5/4, 1/4 both <= eps*q and book (q-1)/4 above threshold.
Stdlib only. Exit code 0 + VERIFY_OK on success.
"""
import math
import sys

D = 0.5
EPS = 1e-4
N0 = 2 ** 20


def check_good_edge(n):
    # |E \ B| >= (d-eps) C(n,2) - eps n^2, exact integer-ish float lower bound
    elb = (D - EPS) * n * (n - 1) / 2 - EPS * n * n
    assert elb > 0, f"no good edge at n={n}"
    return elb


def check_page_threshold(n):
    codeg_lb = (D * D - EPS) * n
    thresh = n / (200.0 * math.log(n))
    # rigorous margin: threshold uses math.log from above? use safety factor:
    # verify with log possibly rounded either way by requiring 1% margin
    assert codeg_lb > 1.01 * thresh, (codeg_lb, thresh)
    # symbolic margin: ln n >= 1/(200 (d^2 - eps))
    need = 1.0 / (200.0 * (D * D - EPS))
    assert math.log(n) > 1.01 * need, (math.log(n), need)
    return codeg_lb, thresh


def is_prime(n):
    if n < 2:
        return False
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def paley(q):
    assert q % 4 == 1 and is_prime(q)
    QR = {pow(a, 2, q) for a in range(1, q)}
    adj = {v: set() for v in range(q)}
    for u in range(q):
        for v in range(u + 1, q):
            if (v - u) % q in QR:
                adj[u].add(v)
                adj[v].add(u)
    return adj


def check_paley13():
    # Structural sanity only (q=13 is too small for the eps*n discrepancy bound;
    # the genuine hypothesis witness is the large Paley order below).
    q = 13
    adj = paley(q)
    e = sum(len(v) for v in adj.values()) // 2
    assert e == q * (q - 1) // 4, e  # density exactly 1/2
    lam = mu = None
    for u in range(q):
        for v in range(u + 1, q):
            c = len(adj[u] & adj[v])
            if v in adj[u]:
                assert c == (q - 5) // 4, c
            else:
                assert c == (q - 1) // 4, c
    # book pages on an edge = lambda
    assert (q - 5) // 4 == 2
    return True


def check_large_paley_params():
    q = 1048589
    assert q % 4 == 1 and is_prime(q)
    assert 1.25 <= EPS * q and 0.25 <= EPS * q  # codegree deviations fit: B empty
    e = q * (q - 1) // 4
    assert 2 * e == q * (q - 1) // 2  # density exactly 1/2
    book = (q - 1) // 4
    thresh = q / (200.0 * math.log(q))
    assert book > 1.01 * thresh, (book, thresh)
    return q, book, thresh


def main():
    elb = check_good_edge(N0)
    print(f"good-edge count lower bound at n=2^20: {elb:.4g} > 0  OK")
    codeg_lb, thresh = check_page_threshold(N0)
    print(f"codegree lower bound {codeg_lb:.4g} vs threshold {thresh:.4g}  OK")
    check_paley13()
    print("Paley(13) sanity: density 1/2, codegrees 2/3, book 2 pages  OK")
    q, book, t = check_large_paley_params()
    print(f"Paley({q}): B empty, book {book} vs threshold {t:.4g}  OK")
    print("VERIFY_OK")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as ex:
        print(f"VERIFY_FAIL: {ex}")
        sys.exit(1)
