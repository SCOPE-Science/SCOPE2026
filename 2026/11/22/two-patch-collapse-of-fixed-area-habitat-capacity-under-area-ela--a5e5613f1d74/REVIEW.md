# Scientific self-review

## Correctness — PASS
For each positive row, the bound uses the nonnegative power-sum inequality at elasticity at least one and the sharp arithmetic–geometric mean inequality. The Perron root is bounded by the maximum row sum. Allocating half the budget to each endpoint of a maximum-weight edge attains the bound; equality analysis on a positive irreducible component forces all component vertices to carry half the total budget, hence exactly two. The equal three-site comparison follows from an explicit rank-three spectrum. A clean replay of `checker.py` passed 8,103 diagnostics; these are supplementary, not a proof of the universal statement.

## Originality — PASS relative to accessed evidence
Research-record searches across fixed-area allocation, area exponents, spectral-radius optimization, the strongest-edge formulation and eigenvalue capacity did not expose this same general fixed-budget classification. Closest indexed items optimize colonization effort, extinction time, conductance gaps, or a distinct uniform-patch recruitment matrix. Hanski–Ovaskainen (2000) supplies the capacity motivation, Etienne and Heesterbeek (2000) and Etienne (2004) study reserve sizes and stochastic viability, Nicol–Possingham (2010) studies restoration dynamic programming, and Bertuzzo et al. (2015) analyze fluvial-network topology with spectral tools. The full Bertuzzo et al. article was read in its mathematical methods and results sections and does not optimize all area vectors with fixed affinities. Some closest historical articles were not fully accessible; the priority conclusion is provisional, and no independent audit was performed.

## Value — PASS
This is a complete, sharp classification for an arbitrary finite weighted symmetric habitat network, revealing a model-selection hazard: under the specified elastic kernel, a pure spectral objective will always recommend deleting all but two habitat sites, irrespective of the network size. The contrasting three-site square-root exponent gives an exact boundary on extending this conclusion. Because real conservation objectives include robustness, spatial constraints and stochastic extinction, the collapse theorem is most useful as a diagnostic against relying on the proxy alone, not as advice to reduce biodiversity habitat to two reserves.

## Closest literature and limitations
The nearest literature is Hanski–Ovaskainen (2000), Etienne–Heesterbeek (2000), Etienne (2004), Nicol–Possingham (2010), and Bertuzzo–Rodriguez-Iturbe–Rinaldo (2015). The first and some related papers could not be inspected in full; other modeling choices and earlier exact statements remain a historical priority risk. The model allows zero-area patches and fixes dispersal affinities under area changes. No claim is made about all standard metapopulation kernels, physical restoration feasibility or the globally sharp phase boundary below elasticity one.

Self-review: passed. Independent audit: not yet performed.
