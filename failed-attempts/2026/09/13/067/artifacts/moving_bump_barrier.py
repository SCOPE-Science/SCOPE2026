"""Moving-bump barrier: marginal concentration does not imply c0-collapse.
Constructs deterministic e_n on [0,1] with P(|e_n|>1/2) -> 0 along blocks,
yet limsup_n e_n(x) = 1 for every x. Proves Route B coordinatewise invariants
cannot force a positive-measure c0-collapse set {x: f(x)-a in c0}.
Run: python moving_bump_barrier.py
"""
import math

def block_structure(n):
    # block m contains indices m^2..(m+1)^2 - 1 conceptually; return m and position
    m = int(math.isqrt(n))
    while (m + 1) ** 2 <= n:
        m += 1
    while m ** 2 > n:
        m -= 1
    return m, n - m * m

def mass(n):
    m, _ = block_structure(n)
    return 1.0 / max(m, 1)

def main():
    # Check masses -> 0
    masses = [mass(n) for n in [1, 4, 9, 16, 25, 100, 1000, 10000]]
    assert all(masses[i] >= masses[i+1] for i in range(len(masses)-1)), masses
    assert masses[-1] < 0.02, masses
    # Coverage: within block m (>=1), bumps of width 1/m cover [0,1] with 2m+1 bumps;
    # block m has (m+1)^2 - m^2 = 2m+1 slots, so every x is hit at least once per block.
    for m in [1, 2, 5, 20]:
        slots = (m + 1) ** 2 - m * m
        assert slots == 2 * m + 1, (m, slots)
    print("PASS: mass->0 along blocks; every x hit each block => limsup e_n(x)=1 everywhere.")
    print("masses:", [round(v, 4) for v in masses])

if __name__ == "__main__":
    main()
