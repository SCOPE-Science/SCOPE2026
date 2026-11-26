---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The exact proof is in `RESULT.md`. For a finite replay, take heights 1, 2, 3, 6 and each coordinate of the test point from {-1,0,1,2,3,4}/6. At height q, visit third coordinates of the integer translate from floor(z) down to floor(z)-(3q-1); visit the first and second integer coordinates from floor(x) down to floor(x)-2 and floor(y) down to floor(y)-2 respectively. Reject any translate with a negative vertex coefficient, using apical coefficient (z-n_3)/q and transverse coefficients x-n_1-(z-n_3)/q and y-n_2-(z-n_3)/q. The box contains all shifts admitting scale less than 3, because each vertex has horizontal coordinates at most one and height at most q. Initialize the minimum at 3 and compare each final minimum to equation (1) in exact arithmetic. The 864 comparisons agree. The analytic proof, not this replay, establishes the all-points claim and the integrated mean and limit.
