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

## Reproducibility
Run `python CHECK.py` with Python 3 standard library. Exact fraction-free Bareiss elimination checks the complete determinants in dimensions three over the prime fields with \(p=3\) and \(p=5\). Direct Fourier summation evaluates all frequencies for \(p=3,5,7\), and checks both extreme singular values and the predicted logarithmic absolute determinant. A nonsquare-discriminant quadratic form is also checked. Direct arithmetic over \(\mathbb F_9\) checks both a square and nonsquare discriminant in a genuine extension field. The package checker returned `ALL_CHECKS_PASSED` after extraction and execution.

## Deductive verification
The infinite-domain proof is separate from computation: the needed premises are the finite-field Gauss identity, the quadratic Salié evaluation, a nondegenerate odd-dimensional quadratic shell count, and a finite cyclotomic product. The proof explicitly derives each normalization and computes the global determinant and exact singular extremes. Experiments over finite fields cannot prove the unrestricted result; they can reveal mistakes in normalizations or multiplicities.

## Limitations
No independent audit has been performed. Publication priority remains unconfirmed, and testing cannot establish it. The findings do not include even-dimensional quadratic spaces or same-square-class sphere pairs.
