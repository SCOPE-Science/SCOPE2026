---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For either Laurent polynomial and n=5q+d, its dth power has exponents in [-4,4], so the product with a polynomial in x^5 has constant term only from two zero exponents. Frobenius therefore gives exact digit multiplication modulo five. The direct residues give the increments (0,0),(0,1),(3,1),(1,1),(2,0), so all n have nonzero residues and a padded length-L word is one of 5^L equally counted words. Convolution on (Z/4Z)^2 diagonalizes with the four rows 2+3i^s, i^s, 2−i^s, i^s. Inversion gives the table including L=0. For the differences of opposite rows only odd r contribute: they cancel for rows 1 and 3, and sum to the character delta at f=L mod 4 for rows 0 and 2. At L=3, f=0 requires zero second-coordinate increments, so first coordinates are even; for f=1 and f=2 there is a spare digit giving increment 2 if needed, and for f=3 choosing three first coordinates from {0,1,3} spans all four. At L=4 both missing cells occur, and zero padding preserves all cells. Adding high digit 4 in pairs creates infinitely many distinct indices with each unchanged pair. Projection off the marginals kills modes with r=0 or s=0; the nine remaining squared magnitudes are 9 once, 5 twice and 1 six times. Parseval gives (3); the (2,2) mode yields the 3^L checkerboard, with the remaining absolute amplitudes bounded as in (4). The full-table energy uses additionally 13 twice and 1 four times after removal of the constant, consistent with (8). The (2,0),(0,2),(2,2) modes give 1, (−1)^L, 3^L; dividing by block length and subtracting the product of the means gives the stated covariance. Direct sparse Laurent multiplication, not the digit recurrence, recovered the L=3 missing pair positions and all L=4 cells (minimum count 16, cross sum 81), via python3 /workspace/branches/independent-reproduction/arithmetic_review.py. Frozen checker inspected, not executed; the finite replay is corroboration.

## originality

PASS

The pass is for the evaluated same-index mod-five trinomial–Delannoy interaction and exact block classification, not the generic Lucas congruence, constant-term scheme, existence of a joint automaton, or Fourier inversion. The closest indexed cross-sequence table concerns different sequences, and the closest same-sequence tables and correlations do not supply the Delannoy coordinate or a cross-character law. No inspected statement gives an equivalent evaluated interaction. The synthesis is elementary and the comparison is not exhaustive.

## value

PASS

The two standard generalized-trinomial specializations give a natural test of what the known marginal laws miss. The closed-form interaction after removing both marginals distinguishes dependence from bias: a sharp dominant mixed mode, exact opposite-row cancellations and an exact support threshold are useful explicit data, beyond constructing an automaton or printing a finite table. The result is a narrow evaluated invariant for this pair and prime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
