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

Sign change is postcomposition by the diagonal unitary conjugation. PSD of the Hermitian symbol is equivalent to T√(ab)≤1 on the two normalized part means; the other eigenvalues are one. A PSD symbol gives a unital CP map; the strict supercritical lower bound proves noncontractivity, and positivity itself would require a PSD symbol by testing the all-ones positive matrix. For z=2(abT²−1)/D, D=2abT+a+b, the positive difference is zww* and the plus certificate determinant is 4−4abT²+2Dz=0, with positive diagonal. Their CP norms add to 1+z. The stated α,β satisfy aα+bβ=1. Multiplying the witness discriminant by D² reduces the identity to D²=(a−b)²+4ab(bT+1)(aT+1). The two remaining eigenvalues have opposite signs and sum of magnitudes T. Thus the trace norm is 1+T−α−β=1+z, attained on the sign contraction. For two infinite parts, diagonal expectation plus t/2 times the difference of identity and the part-sign conjugation gives a normal cb upper bound 1+T, and increasing balanced finite corners give the ordinary lower bound tending to 1+T. This includes T=0. The frozen rational code was inspected, not executed; these identities prove all dimensions and real weights.

## originality

PASS

The supported distinct finding is the supercritical sharp closed-form evaluation with two unequal finite parts of size at least two and variable real weight. The known T=1 projection, the singleton family, and general Schur norm principles are not original claims. The balanced case and two-infinite-parts corollary also admit immediate symmetry calculations and carry no separate novelty credit.

## value

PASS

For a natural diagonal-preserving bipartite filter with unequal parts, the exact operator-space amplification tells how attenuation above the positivity threshold propagates under arbitrary matrix amplification. The equality between the attainable ordinary witness and cb upper bound across the unequal-size regime is not a fixed endpoint evaluation or a transitive trace formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
