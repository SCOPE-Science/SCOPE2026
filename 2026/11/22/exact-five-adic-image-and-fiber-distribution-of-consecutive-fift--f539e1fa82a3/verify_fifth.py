"""Exact full-range checks for consecutive fifth-power differences modulo 5^k.

Only Python standard-library integers and collections are used.  All cases
are exhaustive at their specified finite moduli, not infinite proofs.
"""
from collections import Counter


def square_fibers(m):
    return Counter((x*x) % m for x in range(m))


def expected_fibers(k):
    modulus = 5**k
    if k == 1:
        return {1: 5}
    j = max(0, k - 3)
    square_modulus = 5**j
    sq = square_fibers(square_modulus)
    inv2 = pow(2, -1, square_modulus) if j else 0
    predicted = {}
    for y in range(modulus):
        if (16*y + 4) % 5:
            continue
        u = ((16*y + 4)//5) % (5**(k-1))
        if u % 5 == 4:
            predicted[y] = 10
        elif u % 25 == 1:
            if k == 2:
                predicted[y] = 5
            else:
                a = ((u - 1)//25) % square_modulus
                count = sq.get((inv2*a) % square_modulus, 0)
                if count:
                    predicted[y] = 25*count
        elif u % 25 == 0:
            if k == 2:
                predicted[y] = 10
            else:
                a = (u//25) % square_modulus
                count = sq.get(a, 0)
                if count:
                    predicted[y] = 50*count
    return predicted


def run():
    tested = 0
    for k in range(1, 9):
        modulus = 5**k
        actual = Counter(((x+1)**5 - x**5) % modulus for x in range(modulus))
        predicted = expected_fibers(k)
        assert actual == predicted, (k, actual-predicted, predicted-actual)
        j = max(0,k-3)
        count_formula = (1 if k == 1 else 5**(k-2) + 2*len(square_fibers(5**j)))
        assert len(actual) == count_formula, (k,len(actual),count_formula)
        assert sum(actual.values()) == modulus
        tested += modulus
        print(f"k={k}, modulus={modulus}, image={len(actual)}, complete-fibers=OK")
    print(f"PASS: exact complete-fiber comparisons on {tested} inputs")


if __name__ == "__main__":
    run()
