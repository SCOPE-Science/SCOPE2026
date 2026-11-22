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

# Reproducibility and scope of verification

Install the dependency from `requirements.txt`, then execute `python3 checker.py` alongside this file and `RESULT.md`. A direct replay completed **2,141 assertions**. The checks include symbolic stationarity and norm identities, tangent-Hessian determinants at both parameter endpoints, the resonant positive sum-of-squares equality, the sharp threshold expansion, exact Fourier coefficient convolution for a variety of integer frequency pairs, and numerical simplex tests of the nonresonant branches.

The proof in `RESULT.md` provides the universal steps: a complete six-pair-sum collision classification, global quadratic concavity in the three-mode regime, exact boundary comparison, a resonant sum-of-squares certificate, and an implicit-function argument. The checker does not exhaust real parameters or infinitely many frequencies; numerical samples do not certify those quantifiers. The precise resonant global optimizer at arbitrary radii is not claimed determined. Independent audit is not performed.
