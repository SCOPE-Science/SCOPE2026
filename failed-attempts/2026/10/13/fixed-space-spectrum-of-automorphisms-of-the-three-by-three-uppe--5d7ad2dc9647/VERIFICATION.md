---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Automorphisms preserve the radical and the directed adjacency of the nonzero components of J/J², so the three diagonal idempotents are fixed modulo J. If f_i are their images then V=Σ_i f_i e_ii is congruent to the identity modulo J and f_iV=Ve_ii, yielding a conjugation back to the standard idempotents. The resulting automorphism scales e_12 and e_23 independently and scales e_13 by their product, hence is diagonal conjugation. The kernel is the q−1 scalar units. The commutator with a unit U has three upper off-diagonal equations; distinct diagonal entries give three pivots. For exactly two equal diagonals the rank drops from 3 to 2 when x=0, z=0, or y+xz/(a−b)=0 in the respective patterns a=b, b=c, or a=c. Equal diagonals give ranks 0,1,2,3 as the upper coordinates are zero, only the (1,3) coordinate is nonzero, exactly one adjacent coordinate is nonzero, or both are nonzero. Thus the unit counts R_0=q−1, R_1=(q−1)^2, R_2=2q(q−1)^2+3q²(q−1)(q−2), and the remaining rank-3 units give the stated N_i after scalar division. Burnside with q^{6−r} fixed algebra elements yields q³+3q²+q, and the computation works when q=2 because no exactly-two or three-distinct nonzero diagonal patterns occur. Independent /workspace/branches/ef6beaca-a30e-463e-914f-d4af01cd919e/independent_check.py formed the full commutator on an algebra basis, matched the spectra at q=2,3,5,7, and counted directly 22,57 orbits at q=2,3. Those checks are finite and over prime fields; the proof uses arbitrary field arithmetic.

## originality

FAIL

An indexed exact classification of all T_3 centralizers supplies the dimensions by precisely the same diagonal and nilpotent strata over all finite fields. The multiplicities here are a direct weighting of those cases by the number of unit matrices; Burnside then gives the orbit count. The distinct-centralizer totals themselves are a different invariant, but the inspected normal forms and dimension strata in that record are sufficient for this claim. This conclusion does not impute historical priority to a later catalogue date.

## value

FAIL

The natural action and complete exact spectrum would make a useful small-rank benchmark if not already determined. Here every frequency follows by elementary weighting of available exact centralizer types, and the total is their Burnside average. No independently useful uncovered classification or boundary remains for a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
