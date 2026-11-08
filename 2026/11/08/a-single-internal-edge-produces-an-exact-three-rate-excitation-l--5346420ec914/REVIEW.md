# Scientific review: a one-edge excitation-rate phase law

## Correctness — PASS

The exact domain and both synchronous update rules are fixed in `RESULT.md`. The published cycle-integral maximum theorem applies to all finite connected graphs here. The proof establishes a universal quotient of at most eight colour-types, rules out the sole potentially competing seven-cycle mean, and characterizes the triangle, square and six-cycle sources of all positive rates. Integer cycle-space reduction establishes that no other positive rate is hidden when the named small cycles are non-resonant. Explicit support-set inclusion-exclusion derives both count formulas; no asymptotic or numerical approximation enters the identities. The finite quotient check exhaustively covers 504 patterns, and an independent direct-map simulation checks 13,716 initial configurations. The generality comes from the quotient proof and the previously established cycle theorem, not the sample sizes.

## Originality — PASS, with historical-priority qualification

Closest primary source: Gravner, Lyu, Sivakoff (2016, arXiv:1610.07320v1, Theorem 3) supplies the general cycle-maximum characterization but does not give the graph-specific three-rate and two-parameter probability census for one internal edge. The earlier lattice papers address different interaction geometries. A later general-graph treatment by Doba (2018) is relevant and its abstract was inspected; its full text was not available in this check. Existing complete-bipartite recurrence and temporal-population classifications without the added edge do not logically imply the added-edge counts or the sharp book transition. Searches for same-object aliases, complete-bipartite-plus-edge dynamics, and graph-specific maximum-cycle-density counts yielded no decisive covering statement. This is best-knowledge originality, not a proof of global priority.

## Mathematical value — PASS

The family is a minimal natural perturbation of complete bipartite interactions; its two shore sizes and one added frustrated edge are structural parameters. The result gives a complete all-size rate distribution, not merely a small-graph census, and identifies an exact discontinuity: on every triangular book \(K_{2,q}\) with the hub edge added, the intermediate phase disappears and six previously quiescent colourings become active. This illustrates quantitatively how a single edge can reorganize persistent excitation while all other interactions are unchanged. The precise counts permit sharp comparisons of susceptibility under graph perturbation. No claim is made that the general cycle-maximization criterion, or ordinary surjection counting alone, is new.

## Sources and unresolved limitations

The main derivation relies on the 2016 finite-graph cycle-integral theorem. A potentially relevant 2018 general finite-graph article was accessible only by abstract, so exact specialized consequences in its unexamined body remain a priority risk. No complete transient-time or primitive-period census is established, and no independent scientific audit has been performed. The independent direct simulation is finite evidence only.

Self-review: passed. Independent audit: not yet performed.
