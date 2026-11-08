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

The exact finite-field script `verify.py` was run with Python 3 from the standalone supplied file and completed successfully. It implements polynomial-field addition, multiplication, and inversion directly, then counts points of the smooth normalization via the fiber-product equations. Tests include all field elements of F_(3^n) for n=1..8 in the c=2 case and n=1..4 in the c=1 case; no point sample is mistaken for an exhaustive proof over all primes or parameters.

The zeta-numerator leading halves are [1,2,9,14,40] for c=1 (expected genus 4), and [1,4,22,60,201,432,1094,1928,3956] for c=2 (expected genus 8). In each case the middle coefficient is nonzero modulo 3, confirming ordinary p-rank given the proven genus. Independent local polynomial expansions check both singular points for p=3,5,7 and c=1,2. The recorded output concludes `POINT_COUNT_AND_LOCAL_CHECKS_PASSED`.

Exact geometric genus, connectedness, cusp unibranchedness, and general p-rank rely on the local Artin–Schreier ramification argument, Riemann–Hurwitz, and Deuring–Shafarevich provided in RESULT.md. Historical priority and any stronger unpublished computations have not been independently certified.
