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

# Reproducibility and claim-to-evidence map

The exact theorem is stated in `RESULT.md`, including its positive-real-rate domain, chosen \(L^2\) inner product, bounded \(L^\infty\) extension, and the distinction between norm-attaining \(L^\infty\) inputs and integrable inputs.

The kernel calculation is an explicit inversion of a two-by-two Gram matrix. The unique endpoint switching location follows from comparing \(R e^{-Rs}\) with \(e^{-s}\), and the endpoint sign input exactly attains the kernel row norm.

All other evaluation times are excluded analytically by splitting \(w\) into \(((R+1)/(2R),1]\), \([1/R,(R+1)/(2R)]\), and \((0,1/R)\). In the first interval a single root is dominated by \(R^{-1/(R-1)}\); in the middle interval the entire row is nonnegative; in the last interval the single-root expression is bounded by a scalar function whose maximum ratio is strictly less than one. Differentiating the exact closed form proves monotonicity, and direct limits prove the sharp envelope.

Run `python check.py` with Python 3, SymPy and mpmath installed. Its observed execution passed exact symbolic normalization identities, 72 high-precision kernel-row comparisons with independent absolute-value quadrature, and both endpoint-limit samples. The program samples a finite collection of rates and times; it is not claimed to verify the continuum of rates and times.

Only the stated two-real-rate half-line orthogonal projection is established. No independent audit or formal proof certificate is asserted.
