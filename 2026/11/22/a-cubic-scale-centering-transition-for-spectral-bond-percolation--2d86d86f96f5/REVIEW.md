# Scientific review: growing-clique windmill percolation

## Correctness — PASS

The graph's equitable quotient yields its spectral radius exactly. The rooted-cluster decomposition separates the open spoke count, which is binomial, from vertices reached through at least two edges. A two-step path count has explicit mean; simple open paths of length at least three and multiple two-step paths give an integrable error bound. Enumerating shared edge variables gives a variance bound. Together these establish concentration of the indirect count on the clique-size scale, while the binomial central limit theorem establishes the Gaussian fluctuation scale. Comparing the two scales proves all three regimes without assuming independence between them. The accompanying exact-rational checker verifies 203236 arithmetic and connectivity assertions on small instances; it is not used as a proof of asymptotic claims.

## Originality — PASS under examined evidence

Christoph, Morawski and Wigderson (2026) establish spectral percolation bounds but not a growing-windmill hub-cluster centered limit. Allard and coauthors (2015) supply general finite-component recursions, but not the explicit cubic-scale Gaussian mean-shift regime. Published finite-hub bipartite results establish different Poisson connectivity and Gaussian fluctuation limits: their finite hub set and growing independent right-side population do not imply the deterministic two-step correction in percolated cliques with growing size. Searches for windmill, clique bouquet, hub component, second-generation paths, and cubic-scale fluctuation centering did not identify an exact equivalent. This is a best-knowledge comparison, not proof of exclusive historical priority.

## Value — PASS

The question is forced by the spectral-scale analysis of irregular finite graphs: a hub's degree determines its direct-neighbor Gaussian scale, but peripheral clique edges permit indirect membership. The theorem identifies when that geometrically induced population changes the *entire normalized limit law*, giving a natural and sharp \(n^{1/3}\) separation between negligible, critical, and dominant centering corrections. It does not mistake a centered-fluctuation transition for a new giant-component threshold.

## Closest literature and limitations

Closest sources are arXiv:2608.19145 (spectral threshold bounds), arXiv:1509.01207 (general finite clustered-percolation recursions), and published finite-hub Poisson/Gaussian bipartite percolation results. Historical priority remains at risk from a specialization of a broader random-network limit theorem not identified in the inspection. The result is restricted to one shared hub, disjoint growing peripheral cliques, independent bond retention, fixed spectral multiplier, and \(s=o(n)\); it does not address largest components or complete asymptotics after re-centering in the supercritical clique-size regime.

Self-review: passed. Independent audit: not yet performed.
