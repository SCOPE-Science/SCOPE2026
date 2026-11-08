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

# Exact verification

Run `python3 verification/verify_hesse.py` in the directory containing this file. The script uses only the Python standard library. Its output is saved as `verification/execution.txt`.

The first enumeration examines all \(2^{21}=2\,097\,152\) choices of the nine exceptional sections and twelve fiber components, using the explicit four-condition incidence criterion. Independently, a second enumeration constructs the integral twenty-one-by-twenty-one negative intersection matrix and recursively checks candidate principal submatrices using exact rational Schur pivots; hereditary pruning is valid because a positive-definite matrix has all principal submatrices positive definite. This computation tested \(106\,218\) candidate matrices.

Both methods returned the support polynomial coefficients \((1,21,210,1236,4497,10308,14772,12612,5634,874)\), total \(50\,165\), and maximum support size nine. The script asserts equality coefficient by coefficient and returns `ALL_CHECKS_PASSED` only when all checks succeed.

The finite certificate is exhaustive *for the stated twenty-one-curve matrix*. The geometric proof that there are no other negative curves uses adjunction and the Shioda–Tate lattice index, as explained in `RESULT.md`. There is no independent scientific audit, no claim about the priority of the result beyond the inspected literature, and no claim about surfaces outside the stated hypotheses.
