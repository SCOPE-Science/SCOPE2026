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

# Verification and limits

The proof uses exact integer lifting and the reflection identity for a symmetric simple random walk. Its critical analytical step is a binomial Stirling expansion with a geometric right-tail sum when \(a/\sqrt t\to\infty\) and \(a/t\to0\), followed by the quartic Cramér-rate correction. The two-sided excursion union bound and the cover-time inversion are written in `RESULT.md`. No infinite-volume assertion is based solely on finite computation.

Reproduce the independent finite checks by running `python verify.py` with standard Python 3; the output is exactly `PASS 3242 exact checks` for the supplied script. These checks include the reflection formula up to 50 steps and levels, exhaustive sign-path confinement enumeration for 0–9 steps, and two independently constructed cycle-cover-time CDFs for 3–9 vertices, 1–4 walkers, and 0–8 steps. All arithmetic in these checks is exact rational/integer arithmetic.

The known continuum two-Gumbel convolution is attributed to the 2016 Brownian literature, not claimed as an original result. The new finite-lattice boundary uses the simultaneous \(n\to\infty\) and \(\log k_n/n^{2/3}\to c\) regime; it does not provide moment convergence, a centering in every supercritical regime, or conclusions for interacting, biased, asynchronous, or non-nearest-neighbor walks.

Scientific literature comparisons were conducted against original sources named in `RESULT.md`; remaining unindexed-priority risks are described in `REVIEW.md` and `AUDIT.json`. No independent scientific audit was performed.
