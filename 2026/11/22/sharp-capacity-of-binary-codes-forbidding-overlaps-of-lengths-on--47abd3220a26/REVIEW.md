# Scientific review

## Correctness — PASS

The quantified statement is confined to binary words of length at least fourteen forbidding overlap lengths one through seven. The first-bit/last-bit separation and all-middle-word bijection reduce the unrestricted code optimum exactly to a finite 64-by-64 compatibility product. The supplied program constructs each mask directly and performs complete search with two mathematically justified pruning rules: the cardinality bound from remaining choices, and same-state dominance. Forward and reversed adjacency searches agree at 744, reproducing established smaller-cutoff optima; explicit strings independently confirm the known 24-by-31 lower witness. The finite computation establishes the finite base optimum; the elementary factorization proves the all-length theorem. Residual correctness risk is implementation error, mitigated but not eliminated by transpose search, low-cutoff exhaustive subset tests and transparent source.

## Originality — PASS, with residual historical-priority risk

Blackburn et al. (arXiv:2211.10309, sections IV–V, especially Tables III and V) published the 744 lower bound and compatible 24-by-31 witness, but not the matching upper; their listed upper is larger. The sharp upper certificate is the contribution assessed here. Stanovnik (arXiv:2411.02899) gives general bounds and expansion methods, not this stated optimum; the inspected Yang–Ding later treatment concerns broader alphabet/overlap parameters rather than the same sharp binary cutoff. Related prior records address fixed weight, all-overlap codes, or cutoff two and so do not imply an unrestricted cutoff-seven theorem. The full text of one related Cai–Wang–Feng paper was not accessible and could contain more specific remarks; other unindexed coverage remains possible. Searches and comparison do not establish absolute priority.

## Value — PASS

The first cutoff beyond the exact values tabulated by the 2022–2023 foundational study was a motivated boundary at which the authors supplied a substantial lower construction but no matching upper bound. The exact sharp value closes that concrete gap for every blocklength n at least fourteen, with an independently replayable certificate of manageable size and a clear synchronization-code interpretation. This is more than a routine parameter substitution or an unmotivated integer table entry.

Self-review: passed. Independent audit: not yet performed.
