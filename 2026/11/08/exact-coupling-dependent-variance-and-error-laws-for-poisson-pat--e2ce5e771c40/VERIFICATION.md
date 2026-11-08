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

# Verification
Run `python3 verify.py` on Python 3 without third-party packages. It has deterministic algebraic and distributional checks, pathwise comparisons and seeded Monte Carlo tests. At construction it reported 204657 passing checks. The analytic proof, not randomized tests, proves the stated result.

The proof relies on explicit Poisson marked point-process identities and an elementary coupling bound; no machine-assisted infinite certificate or independently conducted audit is claimed.
