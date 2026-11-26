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

From the grounded block matrix the two class-constant eigenvalues (when both blocks remain) have sum p+q+a and product 2p+a(q−2+a); contrast eigenvalues are p and p+q. Handling the empty blocks separately gives the same stated orbit spectra in their proper form. The mixed-minus-clique reciprocal prefix gaps are positive for k≤q−1 and have sign p−2 thereafter. Independent-minus-clique gaps for q≥3 are positive through k=q−1 and thereafter equal (q−4)/(2p)+1/(p+q); the sole negative full-sum case is (2,3), and equality only at (3,3). At q=2 independent leaders dominate both alternatives in weak submajorization with strict full-sum comparisons. Strict power comparison for r>1 follows from integrating the upper-tail sums (x−t)_+, which have nonnegative differences and are strictly ordered on an interval for the distinct reciprocal vectors. For (2,3) the mixed orbit never wins, and the difference between independent and clique orbits has sign given by the strictly convex function f(r)=2^r+2^(−r)+(2/5)^r−3, with f(0)=0, f(1)<0<f(2). This proves the unique crossing and the listed ties. The quoted approximate decimal is off by about 1.2×10^(−16); the exact defining equation and all classifications are unaffected.

## originality

PASS

The supported distinction is the complete split-graph classification for exactly two leaders and all real r≥1, in particular the isolated fractional switch and first-order ties. Neither the known grounded inverse-trace framework nor the previously studied balanced first-order slice is claimed as new.

## value

PASS

The natural objective interpolates between aggregate noise sensitivity and emphasis on the smallest grounded eigenvalues. The exact transition on the five-vertex graph and exhaustive ties distinguish genuine order-dependence from size- or weight-driven changes. The prefix result also yields convex spectral robustness in the regimes of domination.

The dated certificate retains the supplied scientific assessment, sources and limitations.
