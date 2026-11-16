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

Execute `python verify_quartic_latitude.py` using Python 3, SymPy and NumPy. The program checks all five exactly normalized Gegenbauer branches, the trace identity, five rational optimization inequalities, the algebraic root, and independent generalized Gram eigenvalues. For the latter it derives a basis of all 25 degree-four harmonics from the nullspace of a 10-by-35 polynomial Laplacian matrix; all moment integrals forming its Gram matrices are rational and evaluated exactly before the final floating-point eigensolver. Six rational latitude tests passed, with maximum eigenvalue discrepancy approximately \(3.6\times10^{-15}\). High-precision algebraic root evaluation printed \(\tau=0.24057281685482981386940719\ldots\) and \(H=0.56345027418007798187002081\ldots\).

The global uniqueness and sharp optimization are certified by the written rational-interval proof, not by the finite tests. The result has not undergone an independent audit.
