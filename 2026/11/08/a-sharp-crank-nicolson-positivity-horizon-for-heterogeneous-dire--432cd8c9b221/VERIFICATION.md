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

# Verification instructions

Run `python3 verify_cn_cycle.py` using Python 3 with its standard library. The script checks exact-rational inverses for cycle sizes three through eight and seeded heterogeneous rational rate vectors, as well as the analytic numerator identities and row-stochasticity. Expected output consists of four lines starting with `PASS` and the test counts. The package was replayed from its own extracted contents.

The proof's infinite-length and real-rate assertions rely on the resolvent expression, Newton inequalities, Descartes' rule and rate monotonicity, not on extrapolation from the finite checks. Independent mathematical validation is not represented here.
