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

Run `python3 verify_so4.py` with Python 3 and its standard library. The program recomputes the sixteen quaternion basis matrices and their exact pairwise Gram products, compares every coefficient of the quartic polynomial \(\operatorname{tr}((B^{\mathsf T}B)^2)-12S^2+8U-96D\) as a polynomial in sixteen independent matrix entries, and independently reproduces fourth moments from the double-sphere formula. It evaluates the three exact extremal examples. The checker is provided as a complete standalone file.

The coefficient test verifies a polynomial identity for all real matrices because it compares all monomial coefficients. It is not an exhaustive search over real matrices, and no such finite search is needed: the proof establishes nonnegativity and classifies equality through nonnegative squares, Cauchy--Schwarz, and AM--GM. The optimal Euclidean comparison uses group averaging, not computation. The result has not undergone independent external audit.
