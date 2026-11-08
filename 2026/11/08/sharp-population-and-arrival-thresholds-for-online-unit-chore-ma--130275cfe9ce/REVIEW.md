# Mathematical review

## Correctness (PASS)

The complete forcing-horizon classification has three regimes: no finite adversarial failure for at most three machines, five chores for four machines, and three chores for five or more machines. The unit-chore discrepancy \(d_i=L_i-P_i\) updates exactly by \(1-1/k\) at a receiving eligible machine and by \(-1/k\) at each other eligible machine. With at most three machines, the minimum-discrepancy greedy rule preserves \(-5/6\le d_i\le5/6\) on the \(1/6\)-lattice for all prefixes, by an analytic two-/three-eligible case proof. With four machines, the adaptive five-chore witness forces an actual discrepancy above one on every allocation branch. The four-chore positive bound is exhaustive: the delivered Python proof searches all 16,105 non-singleton eligibility sequences of length at most four, while a separate C++ implementation checks all 54,241 sequences including singleton sets directly from loads and proportional shares. Exact integer arithmetic and the verified singleton-elimination argument bridge the finite enumeration to its universal four-step claim. For five or more machines, two universally eligible chores followed by one eligible for their distinct recipients force violation; minimum discrepancy always survives two arrivals, proving the horizon three is exact. The finding is about unit chores, not arbitrary weights.

## Originality (PASS; with search limitations)

Biburger, Megow and Shahkarami, *Online Fair Division under Eligibility Constraints* (arXiv:2610.08064, 2026-10-06), analyze the same eligibility-aware PROP1 notion and establish asymptotically tight deterministic approximation factors. Their unit-chore lower-bound specialization to four machines is only tight at equality and does not force strict failure, nor does their general upper bound prove an exact three-machine guarantee. Sun, Wang and Li, *Fair Orientations: Proportionality and Equitability* (arXiv:2602.18098, 2026-02-20), establish offline existence for the same relevance-based shares, not an online universal guarantee. The temporal-fairness work of Elkind et al. (arXiv:2410.14593) concerns temporal envy, a different target. Source-level implication comparisons and topical literature searches found no equivalent finite first-obstruction theorem. Residual risk is unpublished or unindexed equivalent small-instance work and incomplete access to all historical papers.

## Mathematical value (PASS)

The recent eligibility-aware proportionality model has a genuine gap between unconditional offline existence and asymptotically degraded online guarantees. The exact all-population forcing-horizon function, including three versus four machines, four safe arrivals versus five adversarial arrivals at four machines, and three sufficient arrivals at five or more machines, locates the first inevitable online loss. The analytic small-machine invariant and minimal adaptive construction explain the structural transition; the finite cutoff is complete rather than a partial census or an arbitrary slice.

## Scope and limitations

This classification covers homogeneous unit-size chores, nonempty eligibility sets, irrevocable online decisions and an adaptive adversary. It does not prove arbitrary-size chore results, oblivious-adversary impossibility, known-future results, or higher-population optimal approximation ratios. The four-step certificate is computationally exhaustive, not an extrapolation to unbounded sequences. Independent external scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
