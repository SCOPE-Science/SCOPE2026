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

The four cell sums omit only the two marked activities; their determinant gives Cov=-x_e x_f(Z10 Z01-Z00 Z11)/Z² with the original normalization. The independent replay in branches/15333b53-a4cb-4a50-91da-58ef995f75f5/independent_check.py exhausted 1024 subsets and recomputed all 45 unordered pairs, not just sample activities. It verified all quotients by multiplication by q²(1-q), independently generated the eight S2×S3 pair orbits of sizes 6,3,6,3,6,12,6,3, and matched every table. Their term counts are 32,28,82,82,76,82,68,78. Seven quotients are nonzero and coefficientwise nonnegative. Pair (1,5), i.e. {0,2} and {1,3}, has exactly the coefficients -50 of q^0 v^5 w and -20 of q^0 v^6 w as its negative terms. All positive-q-degree coefficients are nonnegative. In degree zero subtracting 25v^4(v-w)^2+v^5(84v²-20vw+96w²) leaves 14 strictly positive terms; the quadratic has positive leading coefficient and discriminant -31856. Hence that quotient is strictly positive too. The sign follows for all 0<q<1, v,w>0 and gives zero at q=1 by the factor, as expected. This does not cover fully heterogeneous ordinary activities or negative association. See replay-notes.md in the replay directory for the exact remainder and replay output. The frozen verifier was inspected, not executed.

## originality

PASS

Best of current knowledge for K5 with one arbitrary defect and every pair at all positive activities and 0<q<1. Credit the prior conclusions on homogeneous activities at least 1, all activities at least 2, and certain enlarged pair-specific regions. Those do not cover the arbitrarily small ordinary activity regime or establish this full strict classification and its exact polynomials. The general finite-graph upper bounds do not imply it either. No priority guarantee.

## value

PASS

K5 is a natural finite complete graph outside the small-rank and small-corank theorem. It probes whether known lower activity bounds reflect essential behavior on this host. The one independent defect tests robustness under unrestricted single-bond inhomogeneity, and all-pair certification reaches the low-activity region where the general sufficient conditions do not apply. The single mixed-sign quotient explains why naive coefficientwise positivity is insufficient, while its exact decomposition proves the sign uniformly; this gives a usable benchmark beyond positive-activity sampling or the already-covered high-activity regimes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
