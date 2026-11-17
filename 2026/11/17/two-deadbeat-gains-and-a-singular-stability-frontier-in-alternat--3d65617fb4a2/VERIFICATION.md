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

# Verification and limitations

The proof is the exact integration and algebra in RESULT.md. Run `python3 verify.py` from the extracted artifact directory. The checker uses only Python standard-library routines. It reports the number of random parameter and endpoint consistency tests, exact-rational evaluation for the displayed example, and a numerical probe of the singular limit. It does not establish an infinite theorem by enumeration and does not perform an independent mathematical audit.

Scientific domain: a scalar nonimpulsive generalized piecewise-constant-argument negative-feedback equation with constant positive decay and gain and alternating sampling locations. The finite-time extinction assertion is exact for every real initial state. Full dynamics outside that domain have not been established.
