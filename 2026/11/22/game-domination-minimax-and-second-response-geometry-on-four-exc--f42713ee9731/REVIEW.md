# Scientific review

## Correctness

**PASS.** The claim is a finite exact game-minimax classification with complete graph definitions. A legal move strictly increases the dominated-vertex mask. The two recurrence equations therefore follow by backward induction on the number of undominated vertices, with terminal value zero. They are not probabilistic or heuristic. Two separately implemented checkers produce identical value pairs and conditional reply counts for all four graphs; one performs descending-mask dynamic programming on the full state cube, the other memoizes recursive optimal play. Both are present and executable. The full four-graph tables and the all-opening-vertex checks are reproduced by code, including the non-distance-regular split at distance three in the Möbius–Kantor case.

## Originality

**PASS, with residual priority uncertainty.** The original 2010 domination-game paper was inspected in accessible full text and proves general comparison bounds, including the possibility of S-first shortening; it does not classify the four target graph instances. The 2013 and 2016 papers contribute general bounds. The classification of cubic symmetric girth-six graphs identifies the four exceptional objects but studies their structure rather than optimal domination-game play. Targeted searches for exact values, aliases and optimal second strategies did not reveal a prior table implying the claimed complete classification. Full-text coverage of the later bounds literature is not complete, and an unindexed numerical table could have priority. This limitation is recorded rather than treated as proof of absence.

## Value

**PASS.** These four graph objects form a distinguished natural set in the classification of arc-transitive cubic girth-six graphs, not arbitrary hand-picked small instances. The result gives a complete optimal-play comparison for both turn orders and a complete tactical second-response geometry. It demonstrates that three symmetric graphs have the counterintuitive S-first-shortening phenomenon while the fourth does not, and that D's reply to an S opening ranges from universally optimal to only two choices, depending on the graph. These sharp tactical counts go beyond general game-length inequalities and cannot be inferred from domination numbers alone.

## Limits and closest sources

The result does not extend to all cubic graphs or assert a general theorem beyond the specified quartet. Earliest qualifying primary public source: Brešar–Klavžar–Rall (online 2010-08-17), DOI 10.1137/100786800. More general bounds: Kinnersley–West–Zamani (2013) and Henning–Kinnersley (2016). The natural graph quartet comes from the 2008 cubic-symmetric girth-six classification, DOI 10.1016/j.jctb.2008.06.001. Indexed-search coverage is incomplete; independent scholarly audit is pending.

Self-review: passed. Independent audit: not yet performed.
