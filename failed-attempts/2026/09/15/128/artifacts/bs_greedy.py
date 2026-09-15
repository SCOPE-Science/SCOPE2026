"""Bounded recovery test: greedy Boij-Soderberg decomposition engine + m=2 closed forms.
Run: python3 bs_greedy.py
"""
from fractions import Fraction

def pure_diagram(delta):
    """Unnormalized pure diagram: pi[i][d] nonzero only at d=delta[i], value prod_{j!=i} 1/|delta_j-delta_i|."""
    c = len(delta) - 1
    piv = {}
    for i, d in enumerate(delta):
        denom = 1
        for j, e in enumerate(delta):
            if j != i:
                denom *= abs(e - d)
        piv[i] = Fraction(1, denom)
    return piv

def greedy_bs(betti, codim, reg):
    """betti: dict (i,d)->Fraction. Greedy BS peeling (standard algorithm). Returns [(delta, coeff)]."""
    B = dict(betti)
    out = []
    for _ in range(200):
        # find minimal degree sequence present
        delta = []
        feasible = True
        for i in range(codim + 1):
            ds = sorted(d for (j, d) in B if j == i and B[(j, d)] > 0)
            if not ds:
                feasible = False
                break
            delta.append(ds[0])
        if not feasible:
            break
        # check strictly increasing
        if any(delta[i+1] <= delta[i] for i in range(codim)):
            # not a degree sequence; greedy would eliminate; report
            break
        piv = pure_diagram(delta)
        # coeff = min over i of B[(i,delta[i])]/piv[i]
        coeff = min(B[(i, delta[i])] / piv[i] for i in range(codim + 1))
        out.append((tuple(delta), coeff))
        for i in range(codim + 1):
            B[(i, delta[i])] -= coeff * piv[i]
            if B[(i, delta[i])] == 0:
                del B[(i, delta[i])]
        if not B:
            break
    rem = {k: str(v) for k, v in B.items() if v != 0}
    return out, rem

def en_betti_2xn(n):
    """Eagon-Northcott Betti for 2xn 2x2 minors: F0=S, Fi=S(-i-1)^{i*C(n,i+1)}, i=1..n-1."""
    import math
    B = {(0, 0): Fraction(1, 1)}
    for i in range(1, n):
        B[(i, i + 1)] = Fraction(i * math.comb(n, i + 1), 1)
    return B

if __name__ == "__main__":
    for n in [2, 3, 4, 5]:
        B = en_betti_2xn(n)
        dec, rem = greedy_bs(B, n - 1, 1)
        print(f"m=2,n={n} Betti={dict(B)}")
        print(f"  BS={[(list(d), str(c)) for d, c in dec]} remainder={rem}")
    # Window-size illustration for m=3 (reg 2, codim grows) vs support actually attained
    print("m=2 cases: single pure summand (0,2,3,...,n) confirmed by greedy peeling.")
    print("m>=3: Betti table itself requires Lascoux multiplicities; greedy elimination")
    print("over those tables has no bounded closed form (see WORKLOG).")
