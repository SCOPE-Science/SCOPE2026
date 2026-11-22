# Scientific review: periodic closing in primitive Markov shifts

## Correctness (C) — PASS

The theorem concerns only primitive finite zero-one adjacency matrices with positive entropy and uniformly chosen admissible finite words. A proper prefix–suffix border produces an admissible periodic repetition: the required closing arrow is already present inside the original word. In the absence of any border, the shortest positive directed return path determines the exact possible completion period. This gives the displayed exact dichotomy, including loops and n=1.

Perron–Frobenius gives uniform two-sided exponential word-count bounds and exponential convergence of middle bridge matrices. Counting words with an assigned border by their unique shorter initial block proves the uniform geometric tail, including overlapping borders. Counting a fixed border as two identical blocks joined by an admissible bridge produces the exact Perron coefficient. The finite-prefix/finite-suffix limit is independent, and truncation at a fraction of word length gives exponential total-variation convergence. Tail moment bounds prove the mean and variance limits rather than merely convergence in distribution.

For the three-state example, exact row and column sums yield Perron eigenvalue two, fixed-border probabilities \(1/(3\cdot2^{k-1})\), and the two-step return obstruction. The lower bound counts the excluded length-two border with coinciding endpoints, avoiding a false independence assumption. The standalone program cross-checks the direct period-completion enumeration at finite sizes, with no claim that finite tests prove the infinite results.

## Originality (O) — PASS within inspected evidence

Pannipitiya, *Local Periodic Orbit Penetration in Dynamical Systems* (arXiv:2611.13416, §§2.4 and 4.2), supplies only an upper linear closing bound for general primitive shifts and sharp asymptotic canonical statistics for the **unrestricted full shift**. This does not imply the new finite-type exact Perron border constant, exponential limiting directed closing law, or the positive-density period-overhead example.

Holub–Shallit, *Periods and borders of random words* (arXiv:1509.05240, especially §§2–5), derives border-limit laws for independent uniform symbols in a **full alphabet**. That result does not cover a primitive directed adjacency constraint, its generally different Perron-weighted two ends, or a shortest directed return-path penalty. No claim of inventing word borders or the iid full-shift case is made.

Additional searches for primitive-shift penetration moments, random Markov word borders, and exact closing overhead did not identify a mathematically dominating theorem. This is best-knowledge priority, not a uniqueness proof. Older Markov-language/string-overlap work may contain equivalent portions; that is the main remaining priority risk.

## Value (V) — PASS

The 2026 general SFT result proves admissibility but does not determine the canonical mean or variance. The theorem replaces its coarse upper bound with a universal entropy-normalized limit and an exponentially convergent finite unnormalized fluctuation law for **every** primitive positive-entropy finite-state shift. The explicitly weighted border statistic identifies the parameter controlling typical symbolic overlaps, and the directed three-state example shows a persistent, non-negligible closure penalty absent in the unrestricted full shift. These are structural dynamical conclusions relevant to local periodic orbit detection, not isolated numerical refinements or arbitrary finite slices.

The result is limited to the canonical generator and does not calculate any supremal system-level invariant over other generators. It does not independently validate older results or assert priority across inaccessible literature.

Self-review: passed. Independent audit: not yet performed.
