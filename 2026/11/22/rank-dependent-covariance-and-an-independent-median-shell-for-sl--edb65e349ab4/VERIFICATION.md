---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Run `python3 verify.py` using only the Python standard library. The script exhausts the `(2k+1)!` relative orders of the inputs at widths `k=3,4` and compares exact covariance at distance `k` for each interior rank against the beta-CDF variance formula. It computes the beta-CDF moments using exact rational polynomial integrals. The proof in RESULT.md, not the finite computation, establishes the theorem for all permitted widths, ranks, and atomless iid laws.
