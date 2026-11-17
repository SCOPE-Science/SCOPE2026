---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

PASS. The pinned six-by-twenty-four ternary generator has full row rank and nonsingular Gram matrix over F3. Independently reconstructed all 3^6=729 codewords and all 56,631 nonzero-dimensional message subspaces using unique RREF pivot/free-entry normal forms; every subspace maps injectively to a code subspace. Support histograms give generalized weights (12,16,19,21,23,24), one 2D support-16 minimizer and 3D/4D minima with multiplicity three; the weight enumerator matches the submitted 729-word census. The three minimal dependent triples consist of disjoint coordinate triples {1,15,23},{2,5,11},{8,12,24}. No zero/proportional columns, 102 minimal 4-circuits and complete coordinate coverage by these circuits establish exact locality two on nine coordinates and three on the other fifteen. Full finite census is logically exhaustive and exact; this does not assert properties for other [24,6,12] codes.

## originality

PASS

PASS. In An–Hong–Kim–Lim (2026) Proposition 4.1, the identical six-by-twenty-four generator appears with LCD code parameters [24,6,12], but the inspected paper does not furnish the generalized-weight hierarchy, complete subspace-support histogram or local dual-circuit partition. Generalized-weight and Sage algorithm papers provide definitions/algorithms but no numerical results for this matrix. Nearby published records computing C3,2 [23,5,12] or C3,4 [25,5,14] concern different code spaces; a code's length, dimension and minimum distance alone do not determine the asserted higher-dimensional support census. No exact prior table found; code equivalence to an unsearched table is a residual risk.

## value

PASS

PASS. A published distance-optimal LCD code is a naturally motivated object and its whole generalized Hamming weight profile is a standard nontrivial invariant for multiword support and erasure/wiretap-II thresholds. The exact unique minimum-support 2-plane and uneven 9/15 all-symbol repair locality distinguish this particular generator beyond its [24,6,12] parameters; they could be needed for structure or localized recovery analyses. A finite exhaustive standalone classification is valuable without a general code-family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
