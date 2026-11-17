# Scientific assessment

## Correctness — PASS

The graph definitions uniquely fix all three neighbor masks; factorization F(a,b)=(U(b),V(a)) is exact for both odd inner steps. Exhaustively evaluating the 1024 possible inputs of each shore proves |Fix(UV)|=|Fix(VU)|=124 and (UV)^3=(UV)^2, (VU)^3=(VU)^2, giving F^6=F^4 and 124 fixed/7626 primitive-two orbits. The fixed-attraction basin equals sum_{b in Fix(VU)} p_B(b) p_A(U(b)), which is evaluated exactly and independently reproduced by uncompressed evolution of all 2^20 states for both graphs; all entry, weight and flip histograms match. No unexamined nonstandard lemma or infinite extrapolation is involved.

Two independently written programs reconstruct the maps directly and independently. The reduced program enumerates all ten-bit shore states and the exact basin-indicator sum; the direct program exhaustively evolves every twenty-bit state. Their exact fixed populations, primitive-two populations, graph-specific fixed-attraction basins, orbit-flip histograms and first-entry/period tables agree for each graph. The full-state criterion is checked for every initial assignment, not inferred from sampling.

## Originality — PASS, qualified

The old all-size circular-prism majority recurrence census already covers the prism fixed/two-cycle count (and must not be claimed as original). The present composite claim adds the Desargues comparison, exact two fixed basins, the equality of attractor totals despite a 70440-state basin discrepancy, entry-clock and fixed-weight histograms. published-finding corpus semantic searches for the same two graph names, fixed/oscillator values, basin numbers and reductions returned no statement implying the composite claim. Open full-text general majority analyses establish convergence and bounds but not these two-graph basin counts; dodecahedral GP(10,2) and Shrikhande/rook prior findings are different graph families. Absence of an indexed match is not conclusive novelty proof; unindexed enumerations remain a genuine risk.

The key distinction is between new paired basin behavior and the already known prism recurrent counts. The closest indexed comparisons include general majority convergence, the dodecahedral \(GP(10,2)\) census and the other 16-vertex graph-pair experiments; these do not imply the joint present theorem. An inaccessible published full page and possible unindexed historical tables remain named priority risks.

## Mathematical value — PASS

The decagonal prism and Desargues graph are two canonical nonisomorphic cubic 20-vertex networks. The numerical equality of *both* recurrent-state populations creates a natural test of whether recurrence counts can proxy for attraction outcomes. Their fixed-basin sizes differ by 70440 states and their equilibrium weight distributions are structurally different. The result is a complete natural finite dynamical invariant on a matched pair, with a counterexample to inferring basin size from attractor census, not an arbitrary new graph or an incremental rounding improvement.

## Boundaries

The conclusion is restricted to two named twenty-vertex cubic graphs under simultaneous deterministic open-neighbor majority, not a universal statement about equal counts, arbitrary generalized Petersen graphs or every initial measure. A same-method check is reproducible; there is no independent external mathematical audit.

Self-review: passed. Independent audit: not yet performed.
