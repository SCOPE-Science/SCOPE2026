# Review: rare terminal dimers on a matching-deleted clique

## Correctness — PASS

The graph complement consists of disjoint pairs, making all terminal states other than zero or two vacancies impossible. The reduced Markov recurrence counts all three allowed edge types without double counting. Conditional survival of one tagged deleted pair is bracketed by explicitly telescoping products; two-pair survival is bounded using a second telescoping product and an algebraically verified inequality. A finite-\(T\) lower bound matches the one-pair upper bound after sequential limits. The all-size result therefore does not rely on numerical extrapolation. The standalone checker independently compares the reduced recurrence to labeled-vertex enumeration for \(2\le m\le7\) and evaluates exact finite inequalities.

## Originality — PASS on examined evidence, provisional

Gamarnik–Goldberg (arXiv:0807.1277) treats the same random-edge greedy mechanism, but its matching bounds require bounded degree and girth at least four, in contrast with the dense triangle-containing \(K_{2m}\setminus M\). Turban (arXiv:1908.00940) has a fully connected substrate with no forbidden pairs and necessarily complete terminal coverage. The Dyer–Frieze and Miller–Pritikin matching papers concern approximation ratios on graph families; their accessible abstracts do not assert the sharp constant here. Searches of exact model aliases, formula aliases, and neighboring dense-graph results found no direct implication. Full text for Dyer–Frieze could not be accessed; its absence is a remaining priority risk and is not counted as proof of originality.

## Value — PASS

The model removes a maximal collection of independent edges from an otherwise complete adsorption substrate. This is a natural controlled defect of a dense irreversible-deposition model. Its rare failure probability has the exact leading constant \(3/4\), rather than the \(1/2\) suggested by treating the two final vertices as an unconstrained uniformly random pair. The difference measures the accumulated late-stage effect of excluding partners and supplies an all-size reproducible benchmark for greedy matching and adsorption models.

## Scope and residual risk

The theorem is specific to equal-rate edge choice, a removed perfect matching, and irreversibly blocked occupied vertices. It does not cover general forbidden graphs, arbitrarily weighted deposition, or Gibbs sampling. No independent external audit has been performed.

Self-review: passed. Independent audit: not yet performed.
