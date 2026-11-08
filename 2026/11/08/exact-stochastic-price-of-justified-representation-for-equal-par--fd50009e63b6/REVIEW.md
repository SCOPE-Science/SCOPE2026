# Scientific assessment

## Correctness — PASS

The statement specifies equal-sized disjoint approval blocs, a size-matched committee, nonnegative iid candidate qualities and fixed \(q\) asymptotics. JR forces exactly one selection per bloc; there are no \(\ell\)-cohesive groups for \(\ell\ge2\), so PJR/EJR impose no additional constraints. The formulas for the unconstrained and EJR-constrained optima are therefore identities, not algorithmic assumptions. Tail-integral representations prove the finite expectations. The top-\(k\) variational identity and quantile concentration give an \(O_p(1)\) residual in the asymptotically linear expansion, allowing an ordinary independent-bloc CLT. Uniform order-statistic expectations establish the finite rational loss; conditional expectation of a block maximum gives the fluctuation covariance. The self-contained checker passed exact rational, finite-grid and seeded numerical checks. These numerical checks do not certify infinite limits; the complete analytic proof is in RESULT.md.

## Originality — PASS, with publication-priority limitations

The most closely related motivating work, Boehmer–Dong–Kreisel–Utke (arXiv:2609.08830, September 8, 2026), analyzes quality-aware multiwinner voting and deterministic worst-case quality tradeoffs, including reciprocal proportionality. The new claim instead concerns JR/EJR under iid quality uncertainty on an equal-party-list domain; its exact finite expected deficit, universal general-distribution dependent-block CLT, and sharp uniform \(8/9\) ratio do not follow from the reported worst-case guarantees. Foundational JR/EJR work introduces the axioms, while fair top-\(k\) ranking literature studies different feasibility/ranking constraints. Relevant published record comparisons by object, exact constants, aliases, and asymptotic formulation found no matching theorem. The 2026 motivating manuscript was not available as full original text; abstracts and section-level accounts were read, and these cannot exclude an uninspected appendix. Standard empirical-process and L-statistic results supply mathematical techniques but not the stated stochastic representation benchmark without the specific coupled-maxima calculation. The claim of originality is best knowledge, not a proof of global priority.

## Mathematical value — PASS

The 2026 candidate-quality framework raises the concrete question of how much additive candidate quality is lost when every cohesive party has representation. On the natural equal-party-list stress test, all feasible committees can be characterized, allowing a non-arbitrary stochastic benchmark. The exact expected cost distinguishes finite-electorate effects from a limiting constant. The sharp \(8/9\) limit for the most costly uniform candidate-list size contrasts with potentially extreme deterministic quality losses under standard quotas. The Gaussian variance of the *coupled* quality loss, especially the exact \(1/72\) deficit variance and \(52/2187\) ratio variance for two candidates per party, quantifies fluctuations relevant to sample-size assessment. The arbitrary-distribution theorem identifies which pieces of the law persist beyond uniform scores. No claim is made about arbitrary approval profiles, correlated qualities or strategic behavior.

## Closest literature and residual risks

- Boehmer, Dong, Kreisel, Utke (2026), arXiv:2609.08830: strongest topical overlap, incomplete access to original manuscript; future full-text comparison is important.
- Aziz et al. (2015), DOI 10.1609/aaai.v29i1.9324: original JR/EJR notions, not stochastic candidate-quality analysis.
- Zehlike et al. (2017), arXiv:1706.06368: fair top-\(k\) ranking under protected-group constraints, not the JR equal-party-list loss law.
- Delemazure et al. (2023), DOI 10.1609/aaai.v37i5.25694: party-approval elections and proportionality/strategyproofness rather than candidate-quality order-statistic fluctuations.
- Unindexed work or general stochastic-selection results could contain an equivalent formula. No negative search is treated as proof of uniqueness.

Self-review: passed. Independent audit: not yet performed.
