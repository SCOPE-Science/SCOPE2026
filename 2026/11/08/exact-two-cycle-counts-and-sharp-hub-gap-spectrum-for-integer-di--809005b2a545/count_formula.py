"""Exact multinomial census for two-periodic integer diffusion on K_{2,n}.

All counts are of labelled configurations modulo adding a common integer.
Hub one is fixed at 0, hub two at d, and leaves are individually labelled.
"""
from math import factorial, prod


def multinomial(n, counts):
    q = factorial(n)
    for k in counts:
        q //= factorial(k)
    return q


def gap_counts(n):
    if n < 1:
        raise ValueError("n must be positive")
    B = [0] * (2 * (n + 1) + 1)
    for a in range(n + 1):
        for b in range(n - a + 1):
            f = n - a - b
            U = f - a
            w = [max(0, 1-U), int(U == 0), max(0, 1+U)]
            ex = (a,b,f)
            B[0] += multinomial(n,ex)*prod(t**k for t,k in zip(w,ex))
    for d in range(1,len(B)):
        for a in range(n + 1):
            for b in range(n - a + 1):
                for c in range(n - a - b + 1):
                    for e in range(n - a - b - c + 1):
                        f = n - a - b - c - e
                        U = c + e + f - a
                        V = d + f - a - b - c
                        w = [max(0, 1-max(U,V)),
                             int(U == 1 and V <= 0),
                             max(0, min(d-1,U-1)-max(1,V+1)+1),
                             int(U >= d and V == d-1),
                             max(0, 1+min(U,V)-d)]
                        ex = (a,b,c,e,f)
                        if all(k == 0 or t > 0 for t,k in zip(w,ex)):
                            B[d] += multinomial(n,ex)*prod(t**k for t,k in zip(w,ex))
    return B


if __name__ == "__main__":
    for n in range(1,11):
        B=gap_counts(n)
        N = B[0]+2*sum(B[1:])
        if n >= 3:
            assert [d for d in range(1,len(B)) if B[d]] == list(range(1,2*n-1))
            assert B[2*n-2] == 1
        print(f"n={n} N={N} B0={B[0]} positive_gaps="+",".join(f"{d}:{q}" for d,q in enumerate(B) if d and q))
