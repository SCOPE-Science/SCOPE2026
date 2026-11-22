# Review

## Correctness — PASS

The standard game is completely determined by the two finite minimax recurrences. Every legal move strictly enlarges the dominated mask, so reverse-mask dynamic programming is exhaustive rather than heuristic. A 1,048,576-mask C++ evaluator and an independently written memoized Python evaluator agree on the two game values, the twenty opening values, all 760 conditional two-ply scores, and every distance profile. The statement is explicitly restricted to the graph \(\operatorname{GP}(10,2)\), with no unproved extrapolation.

## Originality — PASS, with residual historical-priority risk

The founding 2010 paper defines the game, proves general bounds and displays the smaller \(C_6\) first-player disadvantage. The 2016 full-text paper treats very small game values and diameter-extremal graph characterizations; neither entails exact values eight and nine on the dodecahedral graph. The 2013 publisher summary gives general bounds and existence constructions, not the exact 20-vertex minimax score or geometric reply classes; its full text remained inaccessible here, a concrete residual risk. Indexed records on static domination, power domination and matching games involve different state rules. Existing publications may contain unindexed computations. A failed search alone has not been treated as a novelty proof.

## Value — PASS

This determines both adversarial game values and all optimal second moves for a canonical cubic planar symmetric graph. The contrast between its minimum static domination size six and game lengths eight and nine measures a concrete adversarial cost; the five distance classes explain the counterintuitive starting disadvantage. This is a complete natural finite strategic classification rather than a single arbitrary parameter sample, and it is exactly reproducible.

## Scientific limitations

The claim is finite and graph-specific. Exhaustive programs are part of the proof and do not establish an infinite family. Bibliographic completeness and independent scholarly validation are not claimed.

Self-review: passed. Independent audit: not yet performed.
