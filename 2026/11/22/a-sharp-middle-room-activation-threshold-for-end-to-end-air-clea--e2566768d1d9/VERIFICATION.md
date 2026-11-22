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

## Reproducible checks

Run `python3 verify.py` with Python 3.9 or later. The program uses only the standard library and was executed from the supplied standalone source, reporting `PASS 54269 assertions`.

Checks cover independent tridiagonal determinant and Cramer's-rule calculations, exact rational boundary instances, the sharp threshold example, the two-room comparator, 45 parameter choices including zero baseline removal, 49,500 random feasible allocations, endpoint symmetrization, and stationary-equation residuals. The analytic proof in `RESULT.md`, not finite sampling, establishes the universal result for all admissible real rates.

## Limits

Numerical testing cannot certify arbitrary real-parameter cases or historical originality. The proof relies on positive definiteness, cofactor expansion, endpoint symmetrization and strict log-determinant concavity. Scientific premises remain model assumptions; there is no field calibration or independent validation.
