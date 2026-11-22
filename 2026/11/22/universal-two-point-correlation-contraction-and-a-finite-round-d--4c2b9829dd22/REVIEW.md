# Scientific review

## Correctness — PASS

The target is an explicitly normalized zero-field Ising Markov law on an open path, with \(L\ge2\) and \(0<|\lambda|<1\). The proof provides the exact conditional bridge mean and nonnegative conditional covariance, proves all-pair correlation domination by induction across arbitrary fixed reveal partitions, and derives a pointwise strictly positive conditional-covariance lower bound on an adjacent co-reveal. Independent reveal-label collision probabilities and the exact target energy identity yield the \(1/K\) defect and cross-entropy inequalities. A separate exact-arithmetic implementation tests 3812 pair inequalities, 571 local lower bounds, 12 single-site target-law cases and a nonuniform random-label mixture. These finite tests support, but do not replace, the general proof.

## Originality — PASS, with scope qualification

The closest full primary text is Baule, arXiv:2611.07845v1, which gives the same underlying ideal parallel decoder, a closed labelled-gap recursion for expected output adjacency counts, and numerical domain-wall/perplexity excess. That work is credited; it does not assert the all-pair monotone signed-correlation theorem for every deterministic batch partition, or the explicit schedule-uniform \(1/K\) lower bound. The Lavenant–Zanella error bounds and the Wen–Liang–Lu serial-depth/conditional-total-correlation theorems focus on distinct metrics and permit coordinated schedules. A related rejection sampler explicitly corrects within-batch dependence. Comparisons against relevant publicly described mathematical results found related decoding-schedule asymptotics, not this correlation-order implication. The exact recurrence in the initiating paper could support a future derivation of part of the result, and unindexed general positive-association theory remains a priority risk. These limitations do not turn a search absence into proof of uniqueness.

## Value — PASS

The physically relevant observable is the unfavorable-neighbor density of the underlying lattice model, which controls the target cross-entropy and the perplexity penalty of factorized parallel generation. The theorem establishes a structural sign and correlation-order law at **all separations**, and a **strict finite-length, finite-round universal defect floor** under the common independent site-clock model, for both ferromagnetic and antiferromagnetic chains. It makes explicit why mere optimization of an independent site-clock distribution cannot eliminate the output-quality cost and why coordinated schedules are a separate regime. It does not assert optimality of the constant, finite-denoiser robustness or an information-theoretic bound for arbitrary adaptive policies.

Self-review: passed. Independent audit: not yet performed.
