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

The standalone `verification/check_cassini.py` uses the Python standard library. Running `python3 verification/check_cassini.py` prints `CASSINI_CONVEX_HULL_STABILITY_CHECKS_OK 9 area regimes` when its checks pass.

It compares independent area-deficit integrands, checks the rationalized square identity, verifies strict normalized monotonicity at nine parameter values, tests both sharp endpoint constants, and checks the perimeter critical coefficient numerically. The proof of strict monotonicity over the full interval, the exact endpoint evaluation, and the uniform asymptotic estimates are analytic; sampling is not presented as an exhaustive proof. The 2013 published convex-hull contact geometry is credited as prior work. Independent validation is not performed.
