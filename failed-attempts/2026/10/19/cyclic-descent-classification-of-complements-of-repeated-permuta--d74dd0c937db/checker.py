"""Reproducibility checks for cyclic-descent complement theorem.

Run: python3 checker.py
The independent oracle uses deletion/nondeletion dynamic programming;
no statement about infinite parameter ranges is deduced from finite tests.
"""
from functools import lru_cache
from itertools import product
from math import comb


def brute_complements(w, u):
    @lru_cache(maxsize=None)
    def dp(i, j):
        if i == len(w):
            return frozenset(((),)) if j == len(u) else frozenset()
        out = {(w[i],) + x for x in dp(i + 1, j)}
        if j < len(u) and w[i] == u[j]:
            out.update(dp(i + 1, j + 1))
        return frozenset(out)
    return dp(0, 0)


def rotations_class(q, m, k):
    r = m - k
    answer = set()
    for s in product(range(q), repeat=r):
        d = sum(s[i] > s[i+1] for i in range(r - 1))
        if r:
            d += s[-1] > 0
        if d <= k:
            answer.add(tuple((v + t) % q for v in s for t in range(q)))
    return answer


def count_formula(q, m, k):
    r = m - k
    return sum((-1)**(k-j) * comb(r, k-j) * comb(q*j+r, r)
               for j in range(k+1) if k-j <= r)


def independent_transfer(q, r, k):
    # DP over last rotation and descent counter; independent of alternating sum.
    states = {(0, 0): 1}
    for step in range(r):
        nxt = {}
        for (last, d), count in states.items():
            for new in range(q):
                key = (new, d + (step > 0 and last > new))
                nxt[key] = nxt.get(key, 0) + count
        states = nxt
    return sum(value for (last, d), value in states.items()
               if d + (last > 0 if r else 0) <= k)


def main():
    exhaustive_cases = total_words = 0
    for q in range(2, 6):
        p = tuple(range(q))
        for m in range(1, 8):
            if q*m > 27:
                continue
            for k in range(m+1):
                oracle = brute_complements(p*m, p*k)
                predicted = rotations_class(q, m, k)
                formula = count_formula(q, m, k)
                assert oracle == predicted, (q, m, k, oracle ^ predicted)
                assert len(oracle) == formula, (q, m, k, len(oracle), formula)
                assert independent_transfer(q, m-k, k) == formula
                total_words += len(oracle)
                exhaustive_cases += 1
    transfer_cases = 0
    for q in range(2, 10):
        for m in range(1, 33):
            for k in range(m+1):
                assert independent_transfer(q, m-k, k) == count_formula(q,m,k), (q,m,k)
                transfer_cases += 1
    print(f"EXHAUSTIVE_OK cases={exhaustive_cases} complement_outputs={total_words}")
    print(f"TRANSFER_OK cases={transfer_cases}")
    print("EXAMPLE q=3,m=3,k=1 count=", count_formula(3,3,1))
    print("EXAMPLE q=2,m=4,k=1 count=", count_formula(2,4,1))
    print("VERIFIED_FINITE_CHECKS_ONLY")

if __name__ == '__main__':
    main()
