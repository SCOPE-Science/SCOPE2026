---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

Every labelled 3×n all-on press set corresponds exactly to a seed x1 in F2^3 satisfying x0=0, x_(n+1)=0 and x_(i+1)=111+B x_i+x_(i−1). The eight first seeds are exhaustive. Independent recurrence evaluation for all eight seeds confirms all twelve displayed columns, each pair-state (x13,x14)=(x1,x2), and six-block weights 10 for seeds 0,7 and 6 for seeds 1–6. Terminal-zero seed sets by n mod 6 are {0},{2},{1,3,4,6},{5},{7},all 8; their exact prefix weights yield all six boxed polynomials including n=1 and q>=1 for residue 0. Independent checks verified the formula for 1<=n<=600; an independently built full 3n×3n GF(2) elimination verified complete solution spectra for n<=40; direct full assignment enumeration checked 299592 assignments over widths 1..6. The infinite proof is the exact finite-state 12-period identity, not extrapolation. All ten actual source-tree blobs were identified and the Git tree SHA independently recomputed as a3e6a8bb52e0ef8ec5be1e63cc1d8742b43e7bd3.

## originality

PASS

Bounded best-of-knowledge originality for the complete all-on affine solution-weight polynomial and optimal-set multiplicities, excluding known minimal cardinalities, seed recurrence, total solution counts and homogeneous code spectra. Caro–Klostermeyer (2003) already teaches the exact eight-seed calculation and all six minima, but its inspected section does not give the complete weights. Goldwasser–Klostermeyer (2005) gives total solution counts through Fibonacci gcd nullity; the Nov 2 low-width code result treats the homogeneous kernel rather than the affine all-ones coset. The new complete periodic coset weight census is an exact natural classification with a substantive albeit small incremental calculation. The inaccessible full 2002 grid article and other unindexed weight tables are recorded as priority risks, not automatic failure.

## value

PASS

The full cardinality distribution over every valid all-on press strategy is a natural optimization invariant of classical three-row Lights Out strips. Scalar minimum-press values and total affine-solution counts do not tell whether there are exactly 2, 6 or 1 optimal strategies or identify the distinct heavier solution stratum. The exact six-residue formula classifies every labelled press set at each weight for all lengths and makes the tie-breaking multiplicity transparent; this is a motivated, independently useful complete enumeration, not an arbitrary parameter slice or merely a fixed small-board calculation. Its scope is deliberately only height three and no broad method is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
