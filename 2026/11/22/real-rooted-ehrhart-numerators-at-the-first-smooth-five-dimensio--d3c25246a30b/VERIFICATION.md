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

At height j the dilated slice is (t+cj)Delta_4, giving the weak-composition count and finite-difference numerator. The two simplex layers give ten vertices; both height inequalities, the four coordinate walls and the sloping cap are genuine facets. At each vertex the four primitive horizontal simplex directions are a lattice basis of the height-zero slice, and the primitive interlayer edge has height ±1; this verifies smoothness even at c=0. A fresh exact reconstruction from the slice sums verified the Ehrhart polynomial, numerator, twenty coefficients of the shifted discriminant identity, negative evaluation, and exceptional discriminants. A separate sign check bypasses the discriminant: 24H_c(−4)=−276c^4−1240c^3+2100c^2+2680c−360<0 for c≥3 (group the middle three terms); 24H_c(−1)=32c^3+96c^2−32c−72>0 for c≥1. With H_c(−1/(c+1))<0, H_c(0)=1, and the left-hand quartic limit positive, there are four disjoint root intervals. For the cubics c=1,2 the left limit is negative, and the last three signs give the three distinct negative roots; c=0 is linear. The linear coefficient equals −f(c)/720, with f(c)=c^4−175c^2−750c−2220. Descartes' rule and f(15)=−2220, f(16)=6516 give the exact integer cutoff. This uses symbolic identities and a sign argument, not extrapolation from small c.

## originality

PASS

The established distinct content is an all-twist simple-negative numerator-root theorem and a sharp integer cutoff in the already known Q_4,c family. The geometry, slice count, eventual negativity, and example at c=16 already have coverage and receive no separate originality credit.

## value

PASS

This is the smooth low-facet family already used to exhibit Ehrhart nonpositivity in dimension five. Identifying its exact transition and proving that simple negative h* roots nevertheless persist for every twist separates two positivity phenomena on a natural, motivated infinite test family. It is more than a recalculation of the cited counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
