# Mathematical assessment: logarithmic-multiplicity uniform subset coverage

## Correctness — PASS

The proof fixes the domain \(p_N=d_N/N\to p\in(0,1)\), \(m_N=\lceil\alpha\log N\rceil\) with \(\alpha>0\), and independently sampled uniform \(d_N\)-subsets in successive integer rounds. The large-deviation rate equation has one solution beyond \(\alpha/p_N\); the derivative of the entropy exponent is \(-\log r_N\), giving both the local survival ratio and the \(-\frac12\log\log N\) displacement. Exact hypergeometric pattern probabilities show multiplicative joint survival approximation, stronger than an additive total-variation estimate at \(N^{-h}\) rarity. Negative pairwise covariance of deficient indicators controls the early tail; the binomial conditional boundary mass controls the late tail. These facts justify the Poisson law and additive \(o(1)\) first-two-moment errors. `verify.py` passed 3,326 finite exact/numerical assertions. No numerical experiment is treated as a proof of the limit.

## Originality — PASS, subject to historical priority risk

The closest sources have different assumptions or conclusions. Castro–Marinho (2026) treats one coupon per round and a growing multiplicity; the terminal window grows and has a continuous Gumbel law. Berend–Sher (2026) treats proportional-size subsets but one occurrence per type. Schilling–Henze (2021) treats fixed coverage multiplicity, while Betken–Thäle (2023) controls the zero-occupancy statistic. Their statements do not directly imply the nontrivial growing-multiplicity entropy saddle, the phase-dependent lattice ratio, and the half-log-log correction together. The pre-existing fixed-multiplicity phase law likewise does not cover \(m_N\) diverging. Searches for aliases, group allocation, binomial maxima, quota and multiple-coverage regimes did not identify a stronger directly covering result. Shioda's quota framework and older general occupancy/extreme-value literature are residual priority risks; absence of a retrieved theorem is not evidence of uniqueness.

## Value — PASS

Logarithmic collection multiplicity is the natural scale where a single type is deficient with exponentially small probability at a logarithmic number of rounds. This regime requires a binary-entropy rate instead of the fixed-quota geometric tail. The second-order \(-\frac12\log\log N\) correction is larger than the constant-width final fluctuation; omitting it miscenters the distribution. The phase-dependent discrete law and its moment formulas quantify the number of batches necessary to achieve multiple repeated observations of each item, relevant to repeated pooled sampling and batch coverage. The result is a natural scaling regime, not a small fixed-parameter computation.

## Scientific limitations

Only the logarithmic multiplicity regime and fixed interior batch fraction are proved. The periodic lattice phase need not settle to a fixed value; claims therefore retain the moving \(\theta_N\). The complete 2021 Schilling–Henze article and Shioda's older quota paper were not available in full text for decisive comparison, although their accessible abstracts indicate distinct hypotheses. A more general unlocated theorem could subsume the result. The analysis has not received independent mathematical review.

Self-review: passed. Independent audit: not yet performed.
