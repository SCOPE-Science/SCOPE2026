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

The analytic proof is in RESULT.md. The provided independent numerical implementation in check_spectrum.py calculates roots of the exact two-wall matching equation using arbitrary precision and verifies the \(T^{5/2}\) correction for five distinct length/stiffness profiles and six decreasing temperatures each. It also checks the gamma quotient against directly differentiated parabolic-cylinder solutions and checks the local Taylor coefficient.

Reproduction: `python check_spectrum.py` with `mpmath` installed. Recorded result: **PASSED 125 numeric assertions**. All equations tested are finite-precision diagnostics. They do not certify the global Sturm argument, the asymptotic remainder or mathematical originality. Independent audit was not performed.
