# Scientific review: complete finite-temperature spectrum of the fully frustrated \(Q_4\) Ising cell

## Correctness — PASS

The sixteen spins, thirty-two signed edges and physical energy \(H=-J\sum\epsilon_{xy}s_xs_y\) are specified unambiguously. The signed adjacency squares to four times the identity, bounding scores by 16; the score changes by multiples of four under spin flips, so only nine energy levels are possible. The full distribution is obtained by a complete 256-by-256 decomposition into two three-cubes. Separately, all 65,536 sixteen-spin assignments are directly evaluated against their 32 signed edges. The two implementations agree at each of the nine integers and recover total mass 65,536. The code additionally verifies negative sign around all 24 squares and the spectral identity. This proves a finite result only; no inference from partial sampling or thermodynamic-limit argument is made.

## Originality — PASS, subject to historical priority

The closest exact older result is Derrida–Pomeau–Toulouse–Vannimenus (1979), which *already* establishes 16 ground states on the four-cube; that prior result is explicitly excluded from the novel content. Parisi–Potters (1995) studies orthogonal-interaction mean-field thermodynamics, explicitly including the fully frustrated finite-cell matrix, but does not provide the exact finite 16-spin energy degeneracies. Wang (2026) studies the frustration index and exact spectral-bound cases rather than finite-temperature degeneracies. Statement/implication comparisons against index searches using the partition polynomial, signed-cut enumerator, the nine energy levels, and the coefficient fingerprints did not uncover a matching table. An unknown older small-system enumeration remains possible; search absence is not a mathematical priority proof.

## Mathematical value — PASS

The sixteen-site four-cube is the smallest nontrivial square-dimensional fully frustrated hypercube with an attainable Clifford spectral bound, already a standard benchmark in older spin-glass work. Its *entire* energy census, rather than merely its ground states, is the natural data needed to fix finite-temperature free energy, internal energy, heat capacity, and excitation entropies without numerical approximation. The exact 120-fold degeneracy jump from ground to first excitation distinguishes entropic population from energy minimization, providing a self-contained, reproducible finite-temperature reference for this physically motivated model. The calculation does not assert large-system universality.

## Closest literature and limitations

Derrida et al. (1979), DOI: https://doi.org/10.1051/jphys:01979004006061700 (ground energy/count; month-only date evidence); Parisi and Potters (1995), https://arxiv.org/html/cond-mat/9503009v2 (asymptotic mean-field treatment; full accessible version March 27, 1995); Wang (2026), https://arxiv.org/html/2611.14906v1 (frustration index/spectral bound). The precise polynomial is not claimed to solve an infinite lattice, add a magnetic field, or supersede these established ground-state results. Older unpublished tabulations and inaccessible auxiliary references are residual priority risks.

Self-review: passed. Independent audit: not yet performed.
