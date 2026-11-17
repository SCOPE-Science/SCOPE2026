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

## Reproducibility checks
Run `python3 verify_sign_quotients.py` using Python 3.8 or later. The expected complete standard output appears in `check_output.txt`, with final line `POLYGON_MOMENT_ANGLE_ALL_SIGN_INVOLUTIONS_PASS cases=243`.

The verifier uses the subdivision of each unit interval at zero, constructs an explicit finite cubical cell complex, enumerates all nontrivial coordinate sign involutions for \(3\le n\le7\), counts invariant cells and quotient-cell orbit sizes, checks the Euler identity and the genus/crosscap formulas, and independently counts fixed connected components and isolated branch points. All its assertions must hold.

The proof in RESULT.md establishes the uniform, infinite theorem by local links, orientation parity, Euler characteristic and surface classification; finite tests do not supply a proof beyond \(n=7\). Independent mathematical audit has not been performed. The corresponding bibliographic priority determination also remains open.
