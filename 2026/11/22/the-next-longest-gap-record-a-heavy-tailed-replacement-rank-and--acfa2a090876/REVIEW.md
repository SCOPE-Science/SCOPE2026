# Review of the marked first-longest-gap record theorem

## Correctness — PASS

The claim's quantifiers are one-dimensional, unit-circle uniform sampling, every sufficiently large initial sample size tending to infinity, a single next strict decrease, joint weak convergence in a discrete rank and two continuous observables, and explicit laws for the limit. The proof uses the exact Dirichlet/exponential representation of circular spacings; independent thinned Poisson first-hit clocks; conditional Poisson counts to recover the discrete waiting time; and a uniform-on-first-cut bound that rules out damaged top-ranked parents as winners. The key truncation failure probability tends to exactly \(1/m\) for the top \(m\) original gaps, allowing \(m\to\infty\). The surviving gap differences are independent exponential rank increments; conditioning on the first-hit clock produces a beta-integral rank law. Summing the conditional maximum CDF gives the stated non-Gumbel drop law. All critical probability limits are proved analytically, with no appeal to simulation as infinite evidence. The reproducible checker performs 113739 deterministic algebraic and fixed-seed finite-simulation assertions.

## Originality — PASS under inspected sources

Penrose, arXiv:2608.19104 (2026), Theorem 2.2 and its Section 6 proof give aggregate counts and times of maximal-spacing records, not an original parent-gap replacement rank, a joint next-record waiting/rank/drop law, or the drop-size distribution. Holst, *J. Applied Probability* 17 (1980), Sections 2, 3, and 6, contains the exponential spacing representation, ranked-gap limit laws, and a fixed-threshold full-coverage waiting-time result. These are essential antecedents and are explicitly credited. The present dynamic one-record mark is not merely a rephrasing of either cited conclusion. Other nearby published mathematical records concerning Greenwood dependence and circular scans compare simultaneous fixed-sample statistics, not insertion-induced replacements. Searches for the theorem's exact law, its rank, and equivalent fragmentation formulations did not identify stronger prior coverage. Historical priority outside indexed and inspected sources remains a risk; search absence is not a uniqueness proof.

## Value — PASS

The quantity is a mathematically intrinsic mark of the record process studied in recent stochastic geometry: when a longest gap is first broken, which original gap takes over and by how much? The answer is a heavy-tailed replacement rank with infinite mean, despite an exponential waiting-time limit, and an explicitly solvable non-Gumbel next-drop distribution with finite mean. It distinguishes the first local record transition from aggregate record frequencies and links extreme order statistics to online fragmentation. This is structural information not supplied by knowing only the current maximal gap, the Gumbel marginal law, or aggregate record frequency. The theorem deliberately makes no new claim about all future records, convergence rates, or finite-sample expectation convergence.

## Sources and remaining limits

- M. D. Penrose (2026), *Record times for coverage thresholds and maximal spacings*, arXiv:2608.19104, especially Introduction, Theorem 2.2, Section 6 proof, Section 8.
- L. Holst (1980), *On the lengths of the pieces of a stick broken at random*, J. Applied Probability 17, 623–634, DOI:10.2307/3212956, especially Sections 2, 3, 6.
- Relevant published comparisons: *A rank-one threshold law for Greenwood dependence in uniform spacings*; *A doubly logarithmic covariance crossover for uniform circular spacings*. The former concerns a fixed-sample gap rank covariance, the latter a fixed-sample gap-exceedance covariance; neither specifies the first replacement parent under new insertions.

A historical equivalent not found by the searches, or a specialization from an uninspected broader fragmentation theorem, remains possible. Only the stated unit-circle uniform limit is proved.

Self-review: passed. Independent audit: not yet performed.
