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

# Finite diagnostics

The accompanying `check_sylvester_annulus.py` uses NumPy, a fixed seed, direct Cartesian barycentric tests of triangle inclusion, and independent annular sampling. Run with `python check_sylvester_annulus.py`.

Expected successful diagnostic groups:

```
CONDITIONAL_EXPANSION_ALGEBRA_OK
FIXED_POINT_LOCAL_EXPANSION_DIAGNOSTICS_OK
TWO_POINT_COLLISION_DIAGNOSTICS_OK
ANNULAR_CONVEX_POSITION_DIAGNOSTICS_OK
```

Sample deterministic run: disk baseline `0.7044798810431815`; first hole-area coefficient `0.3582991702651941`; second coefficient `-0.6042520743370148`. With two points uniform in a disk of radius `0.005` and two uniform in the unit disk, the observed four-point convexity frequency was `0.5003386` (700,000 draws), against the limiting value `0.5`. The annulus simulations at hole-area fractions `0.015`, `0.035`, `0.060` yielded respectively `0.7106771`, `0.7159957`, `0.7250186`, compared with two-term predictions `0.7097184`, `0.7162801`, `0.7238025` (700,000 draws each). These discrepancies lie within the conservative finite-sample and higher-order tolerances.

The mathematical verification rests on the exact conditioning identity, explicit angular and area derivatives, and the almost-sure cone-limit reduction; empirical checks do not certify limiting assertions. The coefficient is valid only at a vanishing centered hole. Historical priority and independent audit remain unresolved.
