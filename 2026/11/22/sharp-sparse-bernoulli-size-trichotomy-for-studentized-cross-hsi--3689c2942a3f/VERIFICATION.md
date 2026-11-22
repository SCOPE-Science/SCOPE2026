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

The provided `verify_sparse_cross_hsic.py` reconstructs linear cross-HSIC's four-cell estimator and exact jackknife from the original ordered-pair kernel. It exhaustively compares exact rational expressions across every binary joint sample of sizes \(3,4,5,6\), checks algebra on all enumerated zero-overlap cases, and checks explicit finite critical-count asymptotics and the Poisson-tail formula. An independent finite multinomial summation gives exact null rejection probabilities \(0.03031332282645029\), \(0.08109219386009066\), and \(0.17443530520706607\) at per-half sizes \(20,40,60\), for \(p_n=\sqrt{1/(2n)}\), supplemented by optional reproducible simulations.

A fresh invocation of the packaged checker passed **6,638 assertions**. The number refers to finite algebraic/numerical assertions, not infinite certification. The proof in RESULT.md supplies the asymptotic probability arguments; only the high-intensity central limit is invoked from the cited primary source under its stated moment condition. The critical result excludes integer \(\theta\), and the upper-tail numerical limit is stated only at \(\theta=1/2\).

Run: `python verify_sparse_cross_hsic.py`. NumPy is optional for the seeded Monte Carlo portion; exact and deterministic checks use only Python's standard library. Independent audit: not performed.
