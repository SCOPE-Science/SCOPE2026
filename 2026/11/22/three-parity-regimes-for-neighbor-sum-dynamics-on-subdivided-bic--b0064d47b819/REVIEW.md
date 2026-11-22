# Review: Three parity regimes for neighbor-sum dynamics on subdivided bicliques

## Correctness — PASS

The state map, its incidence factorization, powers and finite-field Jordan blocks are defined and proved in `RESULT.md`. The mixed-parity size-four block is witnessed by an explicit periodic vector; this avoids an unproved inference from fixed-point counts alone. Every claim follows from the Jordan decomposition. Separate bitset-rank and trajectory-enumeration checks pass (49 graph parameter profiles and 1,233,152 exhaustively followed initial states). These finite checks do not establish the infinite statement; the field-uniform matrix proof does.

## Originality — PASS, qualified

The closest comparison is the published subdivided-clique rigidity theorem (source [4]), whose general connected-base condition concerns three-step zero extinction, not this complete biclique family. The all-even multipartite edge-parity theorem (source [5]) gives the line-graph factor `B^T B` but does not classify the subdivision update or odd shores. Barrett et al. (2009) study optimized graph-compatible minimum ranks rather than powers of the actual adjacency matrix. Moreno et al. (2006) and Pasqualetti et al. (2013) supply general finite-field dynamics tools, not these family-specific invariants. Unindexed equivalent results remain a residual historical-priority risk. Exact queries, relevant material inspected, and implication comparisons appear in `AUDIT.json`.

## Value — PASS

The graph family is canonical, and its complete orbit/attraction structure has distinct and sharp parity regimes. Full Jordan blocks, primitive orbits and first-entry distributions yield structural information about dynamical consequences of graph incidence, rather than a parameter substitution or isolated computer census. The theorem is finite-field and all-size, with a natural four-update extinction and four-cycle contrast.

## Limitations

Only uniform unweighted synchronous open-neighbor addition, characteristic two and ordinary once-subdivided bicliques with each shore at least two are covered. Computation is supplementary and neither a historical uniqueness certificate nor independent external audit. Some primary sections rather than each page of every long source were examined; source-specific limits are recorded.

Self-review: passed. Independent audit: not yet performed.
