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
# Verification of the one-nodal quartic census

The standalone Python standard-library program `verify.py` was executed from its complete file with `python3 verify.py`. It computes the exact integral intersection matrix of the thirteen geometric negative-curve classes and tests all \(8192\) subsets by rational Schur-complement elimination. It independently evaluates the closed-form support polynomials as an integer-coefficient polynomial calculation, checks both coefficient vectors and verifies their total.

The accompanying `verify_output.txt` records the actual successful execution. The proof of completeness of the curve list relies on anticanonical nefness, adjunction, Cauchy--Schwarz, and the incidence assumption; the executable is a finite arithmetic check only. The volume classification uses the published Bauer--Schmitz theorem and is not numerically approximated. Exact external proof validation has not been performed.
