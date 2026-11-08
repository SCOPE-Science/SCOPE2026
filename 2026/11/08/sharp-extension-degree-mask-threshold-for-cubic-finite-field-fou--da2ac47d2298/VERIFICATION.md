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

The exact algebraic proof, as written in `RESULT.md`, establishes the rank formula over every field \(\mathbb F_{p^m}\) of characteristic \(p\ge5\). The argument is not a computer census. It includes explicit quantifiers for all nonempty mask sets and accounts separately for the diagonal trace and complex-conjugate opposite differences. The one-mask singular values are computed using the stated normalized Fourier-space norm, rather than unnormalized output singular values.

The accompanying standard-library `CHECK.py` independently constructs finite-field polynomial-difference incidence matrices, checks exact modular ranks for \(q=5,7,11,13,25\), and validates all tested reflection identities. It also constructs an explicit nonzero Hermitian off-diagonal kernel witness for two masks in \(\mathbb F_{25}\) and verifies that a third mask detects it. For \(q=5,7\), independent complex Fourier evaluations check that every Hermitian profile is real and verify the exact finite Fourier normalization to numerical tolerance. Run `python3 CHECK.py` from this directory. Successful execution prints `CHECK_OK exact_and_numeric_assertions=4900`.

The test matrix ranks are exact over an auxiliary prime; their agreement in finitely many cases supplements rather than proves the universal claim. Numerical Fourier tests are subject to floating-point roundoff. No external independent mathematical audit or independent validation has been performed. The diagonal traceless kernel is unavoidable; the sharp \(m+1\) lower bound is only for the cubic-plus-quadratic offset family and off-diagonal Hermitian recovery, not arbitrary phase masks.
