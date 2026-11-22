---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For every n>=3, the two-row Latin rectangle is a uniform ordered pair of permutations with no column collisions. Within-row incidence pair probabilities are 1/n (identical), 0 (same row/column or symbol exclusively), 1/[n(n-1)] (both different); between rows they are 0 (same column and symbol), 1/[n(n-1)] (exactly one same), (n-2)/[n(n-1)^2] (both different). After subtracting 1/n^2 the covariance blocks equal [[1/(n-1),-1/(n-1)^2],[-1/(n-1)^2,1/(n-1)]] tensor P_n tensor P_n; centered Walsh multiplies by four. Diagonalizing row symmetry gives eigenvalues 4(n-2)/(n-1)^2 and 4n/(n-1)^2 each (n-1)^2, nullity 4n-2 and sharp nonzero condition sqrt[n/(n-2)]. The formula at n=2 has rank 1 and eigenvalue 8; n<2 is outside scope. Independently enumerated all pairs n=2,3,4,5 (2,12,216,5280) and checked eight pair orbits as exact fractions; finite checks corroborate the universal algebra.

## originality

PASS

Bounded PASS for a joint two-permutation centered degree-one frame identity, not the classical Latin-rectangle count or generic derangement distribution. Neither inspected primary paper asserts its two complete Gram sectors and sharp sampling quotient condition number.

## value

PASS

Natural all-n degree-one observation frame for the canonical pair of disjoint perfect matchings. A complete rank/nullspace classification identifies exactly deterministic line-sum aliases, and the sharp quotient condition sqrt(n/(n-2)) gives identifiable signal stability and its asymptotic tightness. Not an arbitrary table or mere renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
