# Scientific review

## Correctness — PASS
For every finite path size and every pair of nonreflection-equivalent seed locations, the final infected cluster is a sum of two independent truncated geometric runs and the seed. Tail-sum moment identities give the exact polynomial for the variance. The proof examines the signs of coefficients in the variance difference in three ordered degree intervals. Since this difference vanishes at transmissibility one, division by the corresponding linear factor converts these coefficient blocks into a polynomial with exactly one sign change. Descartes' rule gives at most one positive crossing, and opposite signs at small and near-unit probabilities prove existence, simplicity and direction. The expected-size comparison uses an exact strict ordering of geometric power sums.

An independent open-edge-state polynomial construction reproduced all source variances through twelve vertices (45,052 source-edge configurations and 75 moment-polynomial comparisons); a separate coefficient-sign check covered 2,870 pairs through forty-one vertices. These finite tests corroborate, rather than replace, the unbounded proof.

## Originality — PASS (within inspected evidence)
Moore and Newman (2000) supply the standard epidemic–percolation mapping and a cluster generating-function framework. Lančić et al. (2009) analyze variance regimes and tree-spread dynamics; Šikić et al. (2011) analyze parameter-dependent mean-impact source ranking; Sharkey et al. (2013) supply exact Markovian SIR tree equations. Their inspected full texts do not establish this precisely quantified all-pairs single-crossover theorem for path source variances. A prior path result with uniform random seed concerns infection-indicator covariance, while a complete-bipartite result addresses different source topologies and only an infinite-family existence mechanism, so neither entails this theorem. Query and implication details are recorded in the structured audit. Priority is provisional, especially for unindexed geometric-sum literature.

## Value — PASS
The theorem identifies a complete pairwise ordering phenomenon for the simplest heterogeneous seed-location setting: a finite chain. Every comparison changes sign exactly once, whereas expected outbreaks are strictly center-favored for all transmission probabilities. It therefore separates average severity from uncertainty in a way not explained by a single isolated example or by a basic moment formula.

## Closest literature and limitations
- Moore and Newman, arXiv:cond-mat/0001393 (2000); source cluster distributions and percolation methods.
- Lančić et al., arXiv:0912.0630 (2009); tree epidemics and size/range dispersion.
- Šikić et al., arXiv:1110.2558 (2011); seed mean-impact ranking dependent on epidemic regime.
- Sharkey et al., doi:10.1007/s11538-013-9923-5 (2013); exact time-dependent Markovian tree equations.

Only homogeneous independent undirected bond percolation on paths is proved. Edge dependence in a genuine Markovian SIR process can break the two-run independence assumption. No global common probability threshold is asserted and no independent literature priority audit has been completed.

Self-review: passed. Independent audit: not yet performed.
