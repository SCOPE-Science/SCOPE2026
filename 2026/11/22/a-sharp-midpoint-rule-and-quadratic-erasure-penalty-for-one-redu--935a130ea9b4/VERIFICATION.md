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

The proof derives the complete one-erasure singular spectrum by orthonormal row reduction. It uses only Parseval's identity, a finite geometric series and strict trigonometric monotonicity, so the dimension-uniform claim does not depend on finite enumeration.

The included `check.py` builds the nonuniform discrete Fourier sample matrices directly, computes the eigenvalues of every surviving square Gram matrix, compares with the analytic two-outlier spectrum, and checks midpoint dominance for numerous sizes and locations. Run using `python check.py` with NumPy installed. Its recorded direct replay completed 6,930 assertions for integer sizes \(2\) through \(34\). Those finite calculations confirm implementation consistency but do not establish every-size correctness by themselves.

The earliest motivating source is Yu–Townsend arXiv:2202.04722v1, submitted 9 February 2022. No external validation or independent audit is claimed.
