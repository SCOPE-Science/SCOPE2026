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

# Reproducibility of square-zero symplectic centralizer counts

Use Python 3 and run `python3 verification/verify.py` from the directory containing `verification/`. The code uses only the Python standard library; `verification/output.txt` is the captured output of the completed run.

The checker enumerates every skew-adjoint four-dimensional \(A\) over \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\), and tests their squares and ranks. It calculates the nullspace of the linear map taking symmetric \(B\) to \(AB-BA^{\mathsf T}\). For \(q=3\) it enumerates every compatible \(B\) for every nonzero \(A\), constructs each \(8\times8\) matrix \(X\), and checks \(X^2=0\) and rank four. It also computes a direct histogram for all \(3^{10}\) symmetric \(4\times4\) matrices. Polynomial total identities are checked at orders \(3,5,7,9\), but no genuine extension-field matrix enumeration is performed at order nine. The unrestricted theorem for all odd prime powers relies on the provided proof. No independent mathematical audit has been performed.
