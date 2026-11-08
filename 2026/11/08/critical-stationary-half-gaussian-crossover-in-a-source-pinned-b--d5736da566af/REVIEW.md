# Self-review

## Correctness — PASS

The finite Markov transition rates follow from the specified bipartite graph and permanent source. The exact drift identities for total infection \(S\) and class difference \(D\) were independently checked by symbolic expansion. Stationarity of \(D\) and \(D^2\) controls the fast imbalance, while stationarity of \(S\) bounds \(\mathbb ES^2\) at order \(n\). Generator convergence on compactly supported smooth test functions identifies the critical Feller-logistic diffusion stationary equation. The boundary-flux calculation excludes an atom at zero and yields a unique normalized density. Uniform second moments justify convergence of means. The package verifier passed 59 finite-state, algebraic and normalization assertions, testing three parameter offsets and four graph sizes. Numerical agreement supplements, but does not replace, the analytic all-size proof.

## Originality — PASS on examined material

The closest primary sources are Dolgoarshinnykh–Lalley (2005), https://arxiv.org/abs/math/0512252, which derives an unforced one-population critical SIS diffusion with extinction, Peterson (2010), https://arxiv.org/abs/1005.0810, which treats contact processes on weighted cliques and extinction / supercritical quasi-stationarity, and Foxall (2014), https://doi.org/10.1239/aap/1401369707, which studies convergence and monotonicity with spontaneous infection. None of their inspected statements gives the stationary balanced two-population, one-permanently-infected-source law with its explicit critical-window half-Gaussian tilt. The closest accessible previous claims treat either star networks with many leaves but a single small hub class, or \(K_{2,n}\) with a two-vertex class; their limits have different scales/limits and do not imply the balanced growing-parts result. Published result-index queries returned epidemic models without the stated fixed-source bipartite invariant law. The possibility of an unindexed stronger historical theorem, or a general theorem specialized to yield the same stationary law, remains a nonzero priority risk.

## Mathematical value — PASS

The contact process is a standard interacting-particle model of epidemic activity near an absorbing critical point. A single pinned source removes extinction, and a balanced bipartition introduces two coupled nonreversible infection counts with no closed-form finite invariant law. The theorem rigorously determines the entire stationary critical-window distribution, not just its scale or mean: it shows \(\sqrt n\) activity, fast inter-part synchronization, an explicit one-parameter Gaussian tilt, and a quantitative response curve through criticality. This resolves a natural finite-size question for two growing populations, not a relabeling of a one-dimensional birth-death calculation. It provides a benchmark distinct from star and fixed-hub models.

## Scientific limits and closest sources

The claim does not include mixing-time rates, dynamic convergence for all initial laws, or offsets increasing with network size. The primary literature comparisons are bounded by accessible material and search coverage; historical priority is provisional. No external scientific audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
