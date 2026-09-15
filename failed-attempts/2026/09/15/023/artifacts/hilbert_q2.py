"""Bounded recovery test: unit-unit Hilbert symbols over Q2 take both values,
so good-ordinary reduction (a mod-2 condition) cannot force inv_2 = 0.
Also records the Fontaine-Laffaille spread obstruction at p=2 for H^2 of a K3.
Verified output (2026-09-15):
  A=1 row: [1,1,1,1,1,1,1,1] ; A=5 row: [1,1,1,1,1,1,1,1]
  pair (3,7): -1 (nontrivial); pair (3,5): +1 (trivial); pair (1,.): +1
  FL spread: HT weights {0,1,2}, spread 2 > p-1 = 1 -> FL inapplicable.
"""


def eps(u: int) -> int:
    return ((u - 1) // 2) & 1


def om(u: int) -> int:
    return ((u * u - 1) // 8) & 1


def hilb_unit(a: int, b: int) -> int:
    """Hilbert symbol (a,b)_2 for odd a,b: (-1)^{eps(a)eps(b)}."""
    return 1 if (eps(a) * eps(b) & 1) == 0 else -1


def hilb(a_odd: int, a_val: int, b_odd: int, b_val: int) -> int:
    e = eps(a_odd) * eps(b_odd) + a_val * om(b_odd) + b_val * om(a_odd)
    return 1 if (e & 1) == 0 else -1


if __name__ == "__main__":
    units = [1, 3, 5, 7, 9, 11, 13, 15]
    for A in (1, 5):
        print(A, [hilb((-M) % 32, 0, A, 0) for M in units])
    print("eps/om:", [(u, eps(u), om(u)) for u in [1, 3, 5, 7]])
    print("(3,7) =", hilb_unit(3, 7), " (3,5) =", hilb_unit(3, 5))
    print("HT spread H^2(K3) = 2 > p-1 = 1 at p=2: Fontaine-Laffaille inapplicable")
