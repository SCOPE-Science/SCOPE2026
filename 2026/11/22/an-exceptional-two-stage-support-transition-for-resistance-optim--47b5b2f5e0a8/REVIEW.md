# Scientific review

## Correctness — PASS

On the connected set, \(n\operatorname{tr}(L^+)\) is strictly convex as a function of independently specified edge conductances; each off-diagonal Laplacian entry identifies the corresponding conductance. The compact-budget and connectivity argument ensures a unique unrestricted minimizer, which must inherit the two-block permutation symmetry. The exact three eigenvalue families are derived in `RESULT.md`. Their KKT system produces a full-support radical solution and checks the two possible zero-conductance faces. The pivotal size-\(5\) thresholds are the exact fractions \(9/5\) and \(45/23\), with the latter checked by both missing-edge KKT inequalities. For sizes at least \(6\), the positive complement-class solution meets all KKT conditions for prices above the triangle threshold. Independent full-matrix KKT and rational spectral checks replayed successfully (3007 counted checks). Risk: code tests are finite and do not replace the proof; the proof uses linear pricing and a connected Laplacian.

## Originality — PASS on inspected evidence, qualified

The full Ghosh–Boyd–Saberi 2006/2008 resistance paper proves a general convex framework and several special cases, not this price-class classification. The complete matching-priced result gives an exact deletion threshold, but its marked edges are disjoint and its complete-network quotient has two rather than three orbits. The complete-tripartite result studies absent within-part edges and does not imply the present ordinary-edge-before-premium-edge phenomenon. Johnson–Chertkov treats general price-weighted network design algorithmically, including nonlinear sparsity penalties, rather than these exact KKT support boundaries. Semantic published-finding corpus searches for triangular tariffs, complement-edge elimination, the exact thresholds, and equivalent group-orbit formulations returned no covering claim. Generalized overlapping or obscure historical results may be unindexed; absence from searches alone is not a uniqueness proof.

## Value — PASS

This is a complete, exact, unrestricted network-design classification across all network sizes, budgets, and premium prices in a natural single-motif tariff model. Its five-vertex exception shows a counterintuitive **support cascade**: a unit-price edge is optimally omitted before any of the more-expensive triangle edges. That cannot be inferred from the known two-class matching price frontier or a routine fixed-graph resistance calculation. Its disappearance for every \(n\ge6\) is explained by explicit spectral multiplicities and exact KKT inequalities. The precise fact distinguishes support topology, not merely a small numerical improvement. It does not claim a universal physical installation policy.

## Closest sources and remaining scope

Ghosh–Boyd–Saberi, *Minimizing Effective Resistance of a Graph* (MTNS 2006 / SIAM Review 2008); Johnson–Chertkov, arXiv:1004.2285; published matching-priced complete-network and tripartite price-threshold classifications cited in `RESULT.md`. No independent audit or unbounded exhaustive literature coverage is represented.

Self-review: passed. Independent audit: not yet performed.
