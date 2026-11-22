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

# Reproducible verification

Execute `python3 check.py` with the standard Python 3 library. The program recomputes the modular falling-factorial Taylor coefficients, the critical center digits and critical images, then independently uses \(D_n=nD_{n-1}+(-1)^n\) on each complete period \(2\cdot11^k\) for \(k=1,2,3,4,5,6\). It compares every target residue multiplicity with the formula of `RESULT.md` and checks the asserted image sizes. The verified outputs were `ALL CHECKS PASS`, attained counts \(7,77,847,9317,102487,1127357\), and maximum multiplicities \(6,26,48,125,246,1335\).

The checker exercises finite cases only. For arbitrary exponents, correctness depends on the eleven-adic convergence, eight regular local isometries, three quadratic normal forms and elementary square-root lifting proved in `RESULT.md`. Those arguments do not require any external computational certificate or unspecified data file.
