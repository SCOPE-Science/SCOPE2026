---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Finite computational verification of geodesic convexity
Run `python3 verify_geodesic_convexity.py` with Python 3 and no external dependencies. The script constructs projective-plane incidence graphs over prime fields, computes all graph distances and all shortest-path interval masks, and checks convex hulls against an independently assembled family of star subsets.

The saved execution produced: order two — 14 graph vertices, 93 convex sets, 16,384 vertex subsets exhaustively classified, 1,001 four-subset Helly and Radon tests; order three — 26 vertices, 366 convex sets, 14,950 four-subset tests, 65,780 five-subset VC upper tests, 2,600 triple hulls; order five — 62 vertices, 3,784 convex sets, 37,820 triple hulls. Terminal verdict: `VERIFICATION PASS`.

All-order and non-Desarguesian validity depends on the incidence-axiom proof in `RESULT.md`, not the finite computations. No external or independent validation is claimed.
