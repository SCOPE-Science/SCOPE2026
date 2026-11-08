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

# Verification of the directed correlation theorem

`verify.py` uses only the Python standard library. It independently computes the cube integral of \(\operatorname{Cov}(Z_0,Y_n)\) by enumerating all \(3^n\) ternary driving paths and \(2^n\) binary initial cells for \(0\le n\le5\). On each cell, the dependence on \(Z_0\) enters only through a fixed branch itinerary, so its midpoint gives the exact integral of the initial centered coordinate; integrating the independent initial \(Y_0\) amounts to starting at its mean \(1/2\).

A separate exact-rational calculation implements the binary-digit Koopman recurrence, and a third calculation expands the algebraic resolvent as a formal power series. The two agree for all 17 coefficients through degree 16 and match the six direct integrals. Six larger lags compare with the sharp two-edge asymptotic at an explicitly limited numerical tolerance. The first coefficients are \(C_0=0\), \(C_1=1/144\), \(C_2=1/216\), \(C_3=7/1728\), \(C_4=5/1944\), and \(C_5=131/62208\).

Actual execution completed successfully. These checks are supporting evidence only: the all-integer identity, exact vanishing in the reverse direction and the asymptotic transfer are analytical theorems proved in `RESULT.md`. The analysis does not cover arbitrary observables or nonstationary starts. No independent mathematical audit has been performed.
