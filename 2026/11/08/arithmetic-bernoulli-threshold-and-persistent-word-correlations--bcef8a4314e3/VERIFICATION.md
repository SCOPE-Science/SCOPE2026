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

The proof uses normalized Haar measure, a unimodular torus-coordinate change, exact integer-matrix determinants, the full-cell covering property when the quantizer resolution divides the base, conditional mixing of \(x\mapsto bx+z\), Parseval, and the fourth-Bernoulli Fourier identity. The analytical positive-term test for the covariance limit is the \(m=1\) term, and proves the sharp divisibility boundary without any finite enumeration.

Run `python3 checker.py` in the same directory as the six text files. Its exact-rational computation partitions the environmental shift parameter at changes of interval-overlap combinatorics and integrates the square of an affine overlap probability. This is algebraically distinct from the Fourier/Bernoulli derivation. The checker tests \(2\le b\le12\), \(2\le q\le10\), three cell-pair selections for each combination, the rational closed form, and the zero-iff-divisible condition; it has no external dependencies. Finite tests do not establish a universal assertion.

No independent review or external formal verification has been performed. Publication priority beyond the sources described in the scientific review is not established.
