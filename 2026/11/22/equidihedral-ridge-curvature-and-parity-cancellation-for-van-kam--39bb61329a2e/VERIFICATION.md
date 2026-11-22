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

# Reproduction and limits

The `check.py` artifact is a self-contained Python 3 script requiring NumPy and SciPy. Run `OPENBLAS_NUM_THREADS=1 python check.py` from the directory containing the script. It computes the zero-sum cube-section vertices directly, detects all edges by common active coordinate constraints, builds the corresponding primal simplices from signed projected basis vectors, and checks every intrinsic ridge measure and adjacent normal angle for \(n=4,5,6,7,8\). Its separate primal convex-hull call checks that the candidate signed projected basis vectors form the expected full-dimensional polytope, and logarithmic-factorial evaluations check approach to the parity-independent asymptotic constant through \(n=1001\).

Observed on replay: `VAN_KAMPEN_FLORES_RIDGE_CHECK_PASS`; the exact edge counts were respectively \(12,60,90,420,560\), and \(V_1(\Omega_4)=3\). These are finite consistency tests. The proof for all integers rests on polar combinatorics, a rank-one Gram determinant and the polyhedral angle formula; no finite enumeration proves a general result. No independent mathematical audit was performed.
