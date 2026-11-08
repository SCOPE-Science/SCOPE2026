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

# Reproduction

Run `python3 verify.py` and `python3 verify_picard.py` with standard Python 3 from the same directory. The scripts have no nonstandard dependencies.

`verify.py` enumerates all projective points and all 357 lines over the field of order four, and confirms that exactly 27 lines lie on the cubic; their 45 intersection points are all ordinary triples. It computes exact Frobenius fixed-point and fixed-branch counts and checks points, boundary and complement in extension degrees one through six. Expect `VERIFY_OK`.

`verify_picard.py` constructs a six-skew-line basis, checks the full 27-by-27 geometric intersection matrix, computes the integral order-two Frobenius Picard action, checks all 15 invariant orbit sums and exhibits a determinant-one rank-four minor. Expect `PICARD_VERIFY_OK`.

The recorded outputs are `verification_output.txt` and `picard_output.txt`. Reproduce the exact finite certificates using the scripts rather than treating the output logs alone as proof. The proof for all field extensions, scheme-theoretic divisor, Picard descent and cohomology is given in `RESULT.md`; no computational enumeration of arbitrarily large finite fields is claimed.
