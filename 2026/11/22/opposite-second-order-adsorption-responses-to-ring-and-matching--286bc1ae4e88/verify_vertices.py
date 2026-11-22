"""Exact occupied-vertex-state certificate for weighted dimer adsorption.

Run: python3 verify_vertices.py
Requires only Python's standard library.
"""
from functools import lru_cache
from fractions import Fraction

N = 8
V = 2*N
# Undirected generalized Petersen graph G(8,3).
EDGES = sorted(
    set(tuple(sorted((i, (i+1) % N))) for i in range(N))
    | {(i, N+i) for i in range(N)}
    | set(tuple(sorted((N+i, N+(i+3) % N))) for i in range(N))
)
assert len(EDGES) == 24
assert all(sum(j in e for e in EDGES) == 3 for j in range(V))

EXPECTED_P = Fraction(903422, 3840375)
EXPECTED_RING_CURVATURE = Fraction(276830066540632837, 4793798789772300000)
EXPECTED_SPOKE_CURVATURE = -Fraction(561926341371011, 43579988997930000)


def terminal_jet(kind):
    """Derivatives 0,1,2 at t=1 via an exact backwards recurrence."""
    assert kind in ("ring", "spoke")
    def marked(edge):
        u, v = edge
        return v < N if kind == "ring" else (u < N <= v)

    @lru_cache(maxsize=None)
    def recurrence(occupied):
        allowed = [e for e in EDGES if all(not (occupied >> v & 1) for v in e)]
        if not allowed:
            return (Fraction(int(occupied == (1 << V)-1)), Fraction(0), Fraction(0))
        k = len(allowed)
        a = sum(map(marked, allowed))
        total0 = total1 = total2 = Fraction(0)
        for edge in allowed:
            child = occupied | sum(1 << v for v in edge)
            p, dp, ddp = recurrence(child)
            b = int(marked(edge))
            total0 += p
            total1 += dp + b*p
            total2 += ddp + 2*b*dp
        p = total0 / k
        dp = (total1 - a*p) / k
        ddp = (total2 - 2*a*dp) / k
        return p, dp, ddp

    jet = recurrence(0)
    assert recurrence.cache_info().currsize == 7314
    return jet


def terminal_law():
    """Separate exact matching-size distribution at homogeneous rates."""
    @lru_cache(maxsize=None)
    def rec(occupied):
        allowed = [e for e in EDGES if all(not (occupied >> v & 1) for v in e)]
        if not allowed:
            return {0: Fraction(1)}
        out = {}
        for edge in allowed:
            child = occupied | sum(1 << v for v in edge)
            for k, mass in rec(child).items():
                out[k+1] = out.get(k+1, Fraction(0)) + mass / len(allowed)
        return out
    return rec(0)


def main():
    expected_law = {
        6: Fraction(868823, 6912675),
        7: Fraction(2008042, 3142125),
        8: Fraction(903422, 3840375),
    }
    assert terminal_law() == expected_law
    assert sum(expected_law.values()) == 1
    for kind, expected in (("ring", EXPECTED_RING_CURVATURE), ("spoke", EXPECTED_SPOKE_CURVATURE)):
        p, d, dd = terminal_jet(kind)
        assert p == EXPECTED_P and d == 0 and dd == expected
        print(f"{kind}: P(1)={p}; P'(1)={d}; P''(1)={dd}")
    print("VERTEX_STATE_EXACT_OK")

if __name__ == "__main__":
    main()
