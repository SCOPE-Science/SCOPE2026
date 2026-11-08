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

# Verification details

The proof is analytic and self-contained. The exact diagonal, trace telescoping, fixed-power quadratic tail, uniform-in-power tail bound, Riemann-sum limit and unique-peak equation are reconstructed in `RESULT.md`.

Run `python3 check_bulk.py` in the directory containing these files. The standalone check returns `BERGMAN_HIGH_POWER_CHECK_OK 4245 checks`, confirming finite exact-rational telescoping and numerical spot checks. It does not provide an infinite-dimensional proof or establish publication priority.

Independent mathematical audit has not been performed.
