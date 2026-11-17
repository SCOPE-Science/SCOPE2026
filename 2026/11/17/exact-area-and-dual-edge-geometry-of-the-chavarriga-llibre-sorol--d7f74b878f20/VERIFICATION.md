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

# Verification and reproducibility

## Exact arguments
The polynomial cofactor identity is \(P\,\partial_x f+Q\,\partial_y f=4(2-3ax+2y)f\); this is reproduced symbolically. The two roots, branch difference, and area integral are elementary algebraic identities. The moment reduction to \(K(m)\) and \(E(m)\), the DLMF §19.12 expansion, and the exact shear-adjusted endpoint change of variables are printed in `RESULT.md`; their proofs, not finite tests, support the universal statements.

## Executable checks
With Python 3.10 or later and the installed `sympy` and `mpmath` libraries, run `python check.py` in the directory containing this file and `check.py`. Expected standard output is `CLS_QUARTIC_ELLIPTIC_AREA_CHECK_OK`. The script verifies the invariant polynomial identity exactly and compares independently evaluated quadratures and elliptic forms to high precision for several allowed parameters. It checks finite-parameter approximations of both edge laws.

## Limits
The numerical cases do not prove monotonicity or asymptotic behavior for every parameter; those follow from nested slices and analytic expansions. Full text of the original 2004 degree-four classification article was not inspected; bibliographic abstract only. No independent external audit has been performed.
