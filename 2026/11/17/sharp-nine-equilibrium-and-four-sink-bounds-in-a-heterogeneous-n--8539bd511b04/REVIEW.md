# Scientific review: sharp nine-equilibrium and four-sink bounds

## Correctness — PASS
The steady-state reduction fixes the central voltage and separates the two transcendental outer equations. A single-maximum derivative argument proves the three-root ceiling for each. The factorized six-dimensional characteristic polynomial implies that a decreasing outer root forces a real eigenvalue beyond one, proving the global four-sink ceiling including arbitrarily strong positive return coupling. For the sharp example, disjoint rational endpoint sign intervals guarantee exactly nine states; exact eigenvalue brackets and a strict Rouché bound guarantee precisely four sinks at nonzero return coupling. The included independent-of-floating-point rational checker passed. No conclusion about global basins is inferred from this local spectral analysis.

## Originality — PASS within inspected literature
The 2024 originating paper already eliminates the central variable and constructs the outer transcendental equations; we explicitly credit those equations, rather than claiming that reduction. Its inspected Sections 3–5 proceed numerically and contain neither the general exact sharp nine/four ceiling nor a certified four-sink positive-state witness. A 2024 companion paper concerns a different Chialvo-only ring-star network. Single-neuron stability work is structurally weaker, and nearby indexed records on other network maps have different equilibrium equations. Unindexed equivalent theorems and stronger general results are residual priority risks. The sharp four-sink obstruction is a statement about the full six-dimensional characteristic polynomial, not merely a title or parameter mismatch.

## Value — PASS
This solves the natural equilibrium multiplicity and simultaneous multistability counting problem for a deliberately small but nonlinear heterogeneous network. The nontrivial part is that return coupling cannot stabilize an outer scalar decreasing branch: it globally constrains the number of possible stable steady states. The exact positive witness demonstrates that four distinct local resting-state basins coexist in a genuinely bidirectional chain, complementing chaotic/periodic coexistence in the original source. No oversized biological claim is made.

## Closest prior work and limitations
Ghosh et al., arXiv:2405.05675 (2024), Sections 3–5, give the network and fixed-point equations but not the sharp theorem. Nair et al., arXiv:2405.06000 (2024), use a different Chialvo-only topology. The result excludes no periodic or chaotic attractors and does not classify global attraction. A separate external mathematical review could identify unindexed earlier equivalent results.

Self-review: passed. Independent audit: not yet performed.
