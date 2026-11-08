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

# Verification and reproducibility

Run `python3 check_two_erasure.py` using standard Python 3. The checker constructs each original chirp explicitly, erases two coordinates, computes every nonzero cyclic autocorrelation directly, and compares its squared sum against the closed character-sum formula. Across odd primes through \(17\), every root and nonzero erasure spacing is tested for two translated origin choices. Independent unnormalized discrete Fourier fourth-moment calculations check the Parseval formulation. Exact formula root-energy multisets are compared across spacings for primes through \(53\); selected larger prime lengths test the analytic sharp lower-bound gap numerically.

The verifier's successful execution produced:

`DOUBLE_ERASURE_CHIRP_PASS direct_cases=1112 fourth_moment_cases=100 spacing_primes=15 asymptotic_samples=[(101, 1.2812001), (103, 0.4872084), (197, 0.3731894), (199, 0.2807136), (401, 0.2294763), (409, 1.1960422), (1009, 0.5963846), (1013, 0.0196423)]`

The displayed asymptotic sample values are the observed nonnegative excesses over the sharp lower bounds; they are not the theoretical \(O((\log p)^2/\sqrt p)\) constant. Floating-point tolerances are explicit in the checker. Finite computations cannot prove the theorem for untested primes. The exact identity follows by an analytic inclusion-exclusion and quadratic Gauss-sum calculation; the uniform asymptotic uses the classical quadratic character and an interval Fourier estimate proved in `RESULT.md`. No formal independent audit or external verification is claimed.
