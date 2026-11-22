# Mathematical review

## Correctness (PASS)

The proof checks the actual strictly positive Markov reset rows, the unique equilibrium by strict sign of \(q_m(t)-t\), the local eigenvalues \(\pm1/\sqrt2\), the disjoint swap \(L\leftrightarrow R\), and the \(m\)-full-branch map \(q_m^2|_L\). Applying standard entropy identities yields exact subsystem entropy \(\tfrac12\log m\) and the full-square lower bound, for every integer \(m\ge2\). Exact rational checks verify construction details for finite test values; they do not establish the infinite proof by themselves.

## Originality (PASS in inspected evidence)

Galatolo–Lippi (arXiv:2611.15649v1) introduce the coupled self-consistent transfer formulation, small-step local convergence, and numerical oscillations; their investigated statements do not dominate the arbitrary-degree exact-entropy construction. Piliouras–Yu (arXiv:2201.10483v1, Theorem 4.6) previously show **single-agent** performative chaos; this fact is prior, not claimed as a discovery. A related two-state frozen-refresh/convex-loss calculation determines a sharp stability and attracting-two-cycle boundary, but does not imply entropy unbounded across full-branch examples. The specific stronger simultaneous constraints—one-step maximal mixing, unique attracting equilibrium, arbitrary growing subsystem entropy—were not located in inspected sources. An equivalent earlier embedding may exist and is an acknowledged priority risk.

## Value (PASS)

The theorem separates stochastic plant relaxation from global deterministic learning complexity. It explicitly proves no universal bound on adaptive entropy follows from maximal frozen mixing, strong convexity and a unique locally stable equilibrium. Its \(m\)-indexed exact invariant subsystem gives a quantitative boundary, rather than merely demonstrating one divergent trajectory or one two-cycle.

## Limits

Piecewise-affine parameter dependence becomes less Lipschitz as \(m\) increases; no uniform bound on controller sensitivity is claimed. The equilibrium is locally rather than globally attracting. The exact entropy is for the invariant subsystem, not the full square. The learning update uses expected gradients rather than finite-sample randomness. Historical priority and independent validation remain open.

Self-review: passed. Independent audit: not yet performed.
