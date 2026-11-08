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
Run \(\texttt{python3 verify\_transfer.py}\) with SymPy installed and \(\texttt{python3 verify\_direct.py}\) with Python 3. The symbolic checker builds the 64-state transfer matrix from local minority constraints, confirms the characteristic polynomial exactly and prints every \(\operatorname{tr}(T^n)\) for lengths three through fourteen. The independent graph simulator updates every bit of every configuration for lengths three through seven.

The two scripts were run from their actual packaged source paths and their terminal outputs captured in \(\texttt{verify\_transfer.out}\) and \(\texttt{verify\_direct.out}\). The direct check covers \(2{,}396{,}672\) configurations, and the certificate's all-length conclusion uses the exact symbolic factorization plus a mathematical root-bound proof. Numerical roots are displayed only for readability; no floating-point result is required for correctness. An independent external assessment has not occurred.
