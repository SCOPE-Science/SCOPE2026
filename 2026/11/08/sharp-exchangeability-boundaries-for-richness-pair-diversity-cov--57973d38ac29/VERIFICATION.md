---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For fixed positive occupancy count k, transferring one unit from a larger to a smaller occupancy with gap at least two lowers the collision count, yielding the balanced minimum; transferring to a largest occupancy until all others are singletons gives the maximum. For n=2 through 6 every next-richness collision range lies at or below the preceding one, including ties at n=6. The independent-copy covariance identity then applies to any sample law. For n>=7, a balanced two-cell profile and the three-cell profile (n-2,1,1) are inverted: their collision-count difference is (h-1)(h-3) at n=2h and h^2-3h+1 at n=2h+1, positive in the applicable ranges. Mixing their uniformly permuted words yields exchangeability and -1/84 at n=7. On at most two labels, diversity vanishes at richness one and is nonnegative at richness two, proving immunity under any law, not just infinite exchangeability. For the equal mixture of the two specified iid laws (a valid infinite exchangeable sequence), the displayed fixed-law covariance is obtained by conditioning on absence of a label: the pair collision probability then becomes (s2-p_i^2)/(1-p_i)^2, which yields the stated term after multiplying by the absence probability. Total covariance gives the mixture expression. Independently, exact integer path recursion followed by rational aggregation gave the exact negative n=22 fraction, and finite occupancy comparisons reproduced the n=7 inversion and its absence for n<=6 (`python3 /workspace/audit_evidence/reproduce.py 4`). Counts converge to their conditional frequencies, and eventual richness equals support size almost surely; bounded convergence gives the equal-mixture covariance of (2,1/2) with (3,37/200), namely -63/800.

## originality

PASS

The fixed-iid covariance and conditional calculation are prior, while the sharp finite-law sample-size boundary and exact sign reversal in a specified infinitely exchangeable ternary mixture are distinct. A model-specific exchangeable partition result concerns the same pair statistic up to complementation but has the opposite sign from the new mixture and does not cover arbitrary exchangeable laws. Same-date frequency-class results were compared at the level of the actual statistics, not excluded by date.

## value

PASS

There is a precise robustness question for two standard sample diversity measures: how many observations and labels are needed before richness can covary negatively with unbiased pairwise diversity when independence is relaxed? The sharp, joint finite-law thresholds and a simple exchangeable witness answer it quantitatively. The exact ternary mixture also isolates why the usual fixed-iid sign can fail even for an infinitely extendible sequence. These are useful constraints and counterexamples, not a claim of infinite-sample-size optimality for the witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
