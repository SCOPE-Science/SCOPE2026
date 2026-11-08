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

The standalone `checker.py` uses finite-field arithmetic, including the irreducible quadratic extension construction of \(\mathbb F_4\), and independent enumeration of all possible quotient linear blocks \(T\) in the stated dimensions. It tests the original symplectic Leibniz identities, \(T^2=0\), the correction equation \(fT=0\), the full linear rank, and the alternating bracket rank on \(\ker D/kz\). It compares multiplicities to the formula using independently evaluated Gaussian and nonsingular-symmetric counts.

Exhaustive outcomes:

- For \(n=1\), \(q=2\): \(1+9t\); \(q=3\): \(1+32t\); \(q=4\): \(1+75t\).
- For \(n=2\), \(q=2\): \(1+45t+330t^2\).
- The corresponding bracket rank is \(2(n-d)\) at rank \(d\) in every enumerated case.

The recorded output is `verification_output.txt`; its final line is `DIRECT_HEISENBERG_SQUARE_ZERO_DERIVATION_AND_KERNEL_FORM_OK`. Formula evaluations in higher dimensions are also included but are not exhaustive original-equation enumerations. The all-field theorem is proved mathematically in `RESULT.md`, independent of these checks. No external independent audit has been performed.
