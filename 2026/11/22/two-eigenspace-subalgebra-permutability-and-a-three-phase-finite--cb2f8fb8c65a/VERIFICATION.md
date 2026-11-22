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

# Reproducibility and verification

Run `python3 artifacts/verify.py` using only Python 3 standard-library modules. The program independently constructs all subspaces of the listed small vector spaces in reduced row-echelon form, tests every basis bracket for Lie closure, tests ordered subalgebra pairs directly by bracket-in-sum containment, and compares these independent counts with the Gaussian formulas. This checks the implementation of the structural formula against a different enumeration method.

Actual successful output is embedded verbatim in `artifacts/verification_output.txt`, ending in `TWO_EIGEN_LIE_VERIFY_OK 5`. It includes the genuinely new cases \((a,b,q)=(2,2,2)\) and \((2,2,3)\). The code uses prime fields for its brute-force tests; nonprime-field and large-dimension assertions follow from the written proof, not from extrapolating tests. Independent audit: not performed.
