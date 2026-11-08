# Scientific review

## Correctness — PASS

The four-round firing count is constant across vertices by Jiang's periodicity lemma (arXiv:1003.0943, Proposition 2.5). The impossibility of cyclic firing patterns containing both adjacent firings and adjacent waits (arXiv:1211.6786, Theorem 6.2) excludes the two-firings-per-four-round case unless every vertex alternates, which gives period two. Direct time-phase analysis excludes equal and adjacent left-side firing times for the one-firing case. Opposite times yield explicit necessary and sufficient integer inequalities for both left initial chip counts and binary right initial chips; they give the exact mass polynomial. Complementation gives three-firing states without omission. The resulting finite sums simplify by the binomial theorem. Proof is all-parameter. Direct exhaustive labelled-state enumeration, independent multinomial-histogram enumeration and polynomial-identity checks independently corroborate their respective finite ranges; captured outputs are included. Main risk is a previously unnoticed special phase or counting multiplicity, addressed by a necessary-and-sufficient phase proof and two distinct exhaustive approaches.

## Originality — PASS with residual priority risk

Jiang (arXiv:1003.0943) determines *which* period lengths can occur on complete bipartite graphs; this does not imply counts of primitive-four states at each chip total. Jiang–Scully–Zhang (arXiv:1211.6786) supply a necessary firing-word restriction but no energy census. Ji–Li–Wang (arXiv:2408.10508) and Jung (arXiv:2608.01350) characterize the open middle-stair region, not its two boundary counts. Levine (arXiv:0811.2800) studies a different graph family. Searches included 'parallel chip firing complete bipartite period four configuration count', 'K_{2,b} chip-firing four cycles exact count', 'period four chip-firing generating polynomial by chip total', and related aliases; none produced a covering claim. An earlier unindexed calculation, especially in inaccessible older literature, remains possible. Source titles alone have not been taken as evidence of noncoverage; the specific existing theorems have been compared by implication.

## Value — PASS

The energy distribution of recurrent states is a natural dynamical invariant behind activity staircases. The graph family is the thinnest nontrivial complete bipartite family supporting primitive period four, and the complete exact enumeration resolves whether the endpoints excluded by the sharp middle-stair inequalities are actually attained. The polynomial identifies two maximal contiguous energy bands, their precise lengths, sharp endpoint multiplicities, and exponential-periodic-state population for every \(b\). These statements cannot be obtained from period existence alone and are useful for comparing energy-conditioned dynamics across graph families. This is not an arbitrary isolated table value.

## Scientific limitations

Only immediately periodic primitive-four states are counted, not their eventual basins or all other periods. Historical-priority uncertainty persists; the Bitar–Goles 1992 full article was not available for inspection. There is no independent external audit.

Self-review: passed. Independent audit: not yet performed.
