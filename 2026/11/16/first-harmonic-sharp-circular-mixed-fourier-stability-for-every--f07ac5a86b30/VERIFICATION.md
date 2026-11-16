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

# Verification and proof boundary

Execute `python3 CHECK.py` with Python 3 in the same directory as the other result files. No packages outside the standard library are required. Exact rational or fixed-point integer arithmetic certifies: \(I_1(9)>137/10000\), \(I_1(6)<109/1000\), every bounded-order sixth-moment inequality \(I_k(6)<1/10\) for \(2\le k\le11\), the Bernstein and Sonin inequalities for order two, all positive rational final comparisons, and the Simpson error terms.

The infinite-order part is proved separately from the imported analytic facts \(I_k(5)<13/40\) for \(k\ge4\), \(\sup_r|J_k(r)|<(7/10)k^{-1/3}\), and the Watson–Nicholson radial envelope. The all-real-exponent argument is analytic Hölder log-convexity. The equality cases and sharp stability formula rely on Xu's published spectral reduction. Finite checker success is not presented as independent or infinite mathematical validation. No independent audit has been performed.
