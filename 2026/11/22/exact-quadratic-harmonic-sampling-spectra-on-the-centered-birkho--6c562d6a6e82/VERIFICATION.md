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
# Reproducibility

`verify_characters.py` uses only the Python standard library to exhaust permutations for \(n=4,5,6,7,8\), compute the fixed-point and two-cycle characters, verify their algebraic identity, and independently check exact character orthogonality and dimension formulas. It passed with sample counts \(24,120,720,5040,40320\).

`verify_birkhoff.py` requires Python 3 and NumPy. It constructs the full normalized quadratic zonal Gram matrix on all permutation-matrix vertices and verifies the predicted eigenvalues and multiplicities for \(n=4,5,6\). It passed, with numerical maximum absolute eigenvalue discrepancies at most \(1.1\times10^{-14}\).

Run both in a directory containing these files using `python verify_characters.py` and `python verify_birkhoff.py`. The proof for all dimensions uses character orthogonality and is not replaced by finite tests. No independent mathematical audit is represented by these computations.
