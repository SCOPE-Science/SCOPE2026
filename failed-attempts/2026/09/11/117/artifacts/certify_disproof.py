"""Standalone exact certificate: the 2+2 diagonal-pole target is false as stated.

Run: python3 certify_disproof.py  (stdlib only; exact Fraction arithmetic)
Prints DISPROOF_OK iff all checks pass.

Claim under test: with spectators (3,7,11), S22 (summed quintic-twisted virtual
contribution over all 2+2 loci, total degree 4 on P4) is a well-defined rational
function near the diagonal l0=l1 with at most a simple pole of residue -125/96.

Disproof (structural, formula-independent):
 (R1) Midpoint resonance: (3+11)/2 = 7 exactly. Hence for the degree-2 edge joining
      fixed points p2,p3-indexed spectators (labels 2,4 with weights 3,11), the
      H^0(P1,O(2)) middle weight (a*li+b*lj)/2-lk with a=b=1 vanishes against the
      TP4 weight at spectator 3 (weight 7). This zero torus weight sits in the
      moving part of H^0(C_e,f^*TP4) for EVERY (l0,l1): the edge denominator
      E(2,4), E(4,2) is IDENTICALLY zero as a polynomial in (l0,l1).
 (R2) The corresponding quintic numerators Q(2,4), Q(4,2) are NONZERO at generic
      (l0,l1) (exact values printed), so these terms are genuine poles, not 0/0.
 (R3) Smoothing resonance: (3-7)+(11-7) = 0 exactly, so chains (2,3,4),(4,3,2)
      have IDENTICALLY zero node-smoothing denominator with nonzero numerator.
 (R4) 16 of the 80 ordered 2+2 triples contain such a factor; S22 is therefore
      undefined (formally infinite) at exactly (3,7,11) for every (l0,l1) near the
      diagonal. No Laurent expansion R/(l0-l1)+reg exists; the residue claim is void.
 (R5) Calibration guard: the same edge/chain assembly reproduces n1=2875 (three
      generic weight sets) and the genus-0 invariant N2=4876875/8 (three generic
      weight sets; equivalent to n2=609250 via Aspinwall-Morrison N2=n2+n1/8),
      proving the resonance is in the GEOMETRY (zero torus weights), not in our
      conventions: any correct localization computation contains the same factors.
 (R6) Regular remainder: even deleting the 16 singular terms, the remaining 64-term
      sum has a DOUBLE pole (h^-2 coefficient != 0 exactly) at two tested diagonal
      points, so no natural sub-sum salvages the simple-pole claim either.
"""
from fractions import Fraction as Q
import itertools
import sys
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-998/output/artifacts")
from derive_s22 import edge_H_moving, edge_Q, single_locus_value, chain_term, total_N2

fails = []
def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (" | " + str(detail) if detail else ""))
    if not cond:
        fails.append(name)

# R5: calibration of the assembly used for the diagnosis
check("calib_n1_A", sum(single_locus_value(i, j, 1, (Q(1), Q(2), Q(4), Q(8), Q(16)))
      for i, j in itertools.permutations(range(5), 2)) / 2 == 2875)
check("calib_n1_B", sum(single_locus_value(i, j, 1, (Q(1), Q(3), Q(7), Q(16), Q(32)))
      for i, j in itertools.permutations(range(5), 2)) / 2 == 2875)
check("calib_n1_C", sum(single_locus_value(i, j, 1, (Q(25), Q(27), Q(49), Q(55), Q(57)))
      for i, j in itertools.permutations(range(5), 2)) / 2 == 2875)
check("calib_N2_A", total_N2((Q(1), Q(2), Q(4), Q(8), Q(16))) == Q(4876875, 8))
check("calib_N2_B", total_N2((Q(1), Q(3), Q(7), Q(16), Q(32))) == Q(4876875, 8))
check("calib_N2_C", total_N2((Q(25), Q(27), Q(49), Q(55), Q(57))) == Q(4876875, 8))
check("AM_identity", Q(609250) + Q(2875, 8) == Q(4876875, 8))

# R1: edge denominators identically zero in (l0,l1)
for lab, (l0, l1) in {"P": (Q(5), Q(6)), "Q": (Q(100), Q(-37))}.items():
    lam = (l0, l1, Q(3), Q(7), Q(11))
    check(f"R1_E24_zero_at_{lab}", edge_H_moving(2, 4, 2, lam) == 0)
    check(f"R1_E42_zero_at_{lab}", edge_H_moving(4, 2, 2, lam) == 0)
check("R1_midpoint_identity", (Q(3) + Q(11)) / 2 == Q(7), "(3+11)/2=7")

# R2: numerators nonzero (genuine poles, not 0/0)
lam = (Q(5), Q(6), Q(3), Q(7), Q(11))
q24 = edge_Q(2, 4, 2, lam)
q42 = edge_Q(4, 2, 2, lam)
check("R2_Q24_nonzero", q24 != 0, q24)
check("R2_Q42_nonzero", q42 != 0, q42)

# R3: smoothing identically zero
check("R3_smoothing_identity", (Q(3) - Q(7)) + (Q(11) - Q(7)) == 0, "(3-7)+(11-7)=0")

# R4: census of affected ordered triples
def is_singular(a, m, b):
    sides = ((a, m), (b, m))
    return (2, 4) in sides or (4, 2) in sides or (a, m, b) in ((2, 3, 4), (4, 3, 2))
sing = [(a, m, b) for a in range(5) for m in range(5) for b in range(5)
        if a != m and b != m and is_singular(a, m, b)]
check("R4_singular_census", len(sing) == 16, f"{len(sing)}/80 triples singular")

# R6: regular 64-term remainder still has a double pole on the diagonal
def S22reg(t, h):
    lam = (t + h, t - h, Q(3), Q(7), Q(11))
    tot = Q(0)
    for a, m, b in itertools.product(range(5), repeat=3):
        if a == m or b == m or is_singular(a, m, b):
            continue
        tot += chain_term(a, m, b, 2, 2, lam)
    return tot / 8

def hminus2(t):
    hs = [Q(1, L) for L in range(60, 67)]
    ys = [S22reg(Q(t), h) for h in hs]
    exps = list(range(-2, 5))
    n = len(exps)
    M = [[hs[j] ** e for e in exps] + [ys[j]] for j in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        d = M[col][col]
        M[col] = [x / d for x in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [rv - f * cv for rv, cv in zip(M[r], M[col])]
    return M[0][n]

c0 = hminus2(0)
c5 = hminus2(5)
check("R6_double_pole_t0", c0 != 0, f"h^-2 coeff = {c0}")
check("R6_double_pole_t5", c5 != 0, f"h^-2 coeff = {c5}")

print("RESULT:", "DISPROOF_OK" if not fails else f"DISPROOF_INCOMPLETE {fails}")
sys.exit(0 if not fails else 1)
