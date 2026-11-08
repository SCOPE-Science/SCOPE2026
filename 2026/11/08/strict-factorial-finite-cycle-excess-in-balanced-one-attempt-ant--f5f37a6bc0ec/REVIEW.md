# Scientific review: Strict factorial finite-cycle excess in balanced one-attempt antagonistic adsorption

## Correctness — PASS
The candidate theorem is precise for every simple cycle of order at least three, balanced independent species proposals, one attempt per site and continuous uniform arrival priorities. Conditional bichromatic conflict edges reduce the dynamics exactly to ordinary greedy maximal independent sets. First-vertex recursion supplies the path count and its generating function. Explicit exceptional wraparound cases cover even and odd cycles, and the beta-integral Taylor coefficients give all-size *strict* signs plus rigorous factorial asymptotics. An independently implemented exact-rational vertex-subset recurrence agrees at sizes three through ten, but no finite enumeration is used as an infinite proof.

## Originality — PASS, qualified
Do Amaral and dos Santos (arXiv:2306.09786, first publicly dated 2023-06-16) derive the infinite-line one-attempt density, which at equal species probabilities and terminal time is \(1-e^{-1}\). Krivelevich et al. (DOI 10.1002/rsa.21200) already give the path greedy recurrence and local-limit theory. Neither inspected article contains the finite-cycle identity or the strictly positive, different odd/even factorial constants. Page--Rényi parking (Gerin, DOI 10.37236/5150) and repeated-proposal antagonistic adsorption are distinct stochastic dynamics. Available semantic and literature searches found no stronger implication, but unindexed prior work and the uninspected full Gerin article remain priority risks.

## Value — PASS
Finite periodic cycles are a natural finite-volume counterpart of the source model. Proving a *uniform strict finite-volume bias* and resolving its sharp parity-dependent rate is a motivated boundary effect; the result is not implied by knowing the infinite-volume limiting density and is not just an arbitrary finite-table extension. Explicit rational finite-size formulas and a standalone checker make it a reproducible benchmark for periodic adsorption.

## Scientific limitations
No biased species probabilities, later retries, other graph geometries, terminal-coverage distribution or second-order asymptotic are claimed. The finite checker corroborates, rather than establishes, the infinite theorem. Historical novelty is best-knowledge only.

Self-review: passed. Independent audit: not yet performed.
