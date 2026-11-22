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

# Reproducibility

Run `python3 verify.py` from the directory containing the extracted script. It requires only the Python standard library. It computes the original generating function by finite Euler-product multiplication modulo four, independently enumerates the three quadratic representation forms, checks the Gaussian prime rule, and checks the inert-prime obstruction and \(3\pmod4\) progression for all relevant indices through 2000. Its expected terminal line begins `VERIFY_OK`.

The executable does not establish any all-index identity by enumeration. Those identities follow from the formal power-series calculation and elementary local number theory in the proof. No independent mathematical audit has been performed.
