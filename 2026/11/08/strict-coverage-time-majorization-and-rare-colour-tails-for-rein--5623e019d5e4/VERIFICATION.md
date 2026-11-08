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

The exact, standard-library-only checker `verify.py` enumerates three mutually independent constructions of finite-time coverage probabilities, verifies the strict balancing inequality at attainable times (including positive rational initial masses), checks the convexity kernel and numerically checks asymptotic gamma ratios. Execute `python3 verify.py` in a directory containing the extracted files. A successful replay prints `VERIFY_OK 2981`.

Finite enumeration and asymptotic numerical sampling are finite checks, **not** a certificate of the all-parameter theorem. The infinite proof uses conditional Beta splitting, convexity, majorization transfers, Dirichlet mixed moments, Bonferroni bounds and gamma-ratio asymptotics. Independent audit has not been performed.
