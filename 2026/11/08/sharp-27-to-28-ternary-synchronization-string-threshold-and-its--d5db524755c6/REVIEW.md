# Scientific assessment

## Correctness — PASS

The standard insertion/deletion distance identity reduces the strict condition to the maximum normalized adjacent-interval LCS ratio. Square factors have ratio exactly one, so all finite minimizers with ratios below one are square-free. The restricted-growth generator reaches every symmetry class exactly once; its suffix-square rejection is complete by induction. Independent C++ dynamic-programming LCS and Python bit-vector LCS programs agree on all 28 exact rational minimum values, each symmetry-class count and all 14 listed critical extremizers. Thus the exact 27/28 threshold follows from exhaustive, independently replicated finite computations plus the elementary hereditary-prefix argument, not an extrapolation. There has been no external mathematical audit.

## Originality — PASS, qualified

The closest source is Xu et al., arXiv:2609.04122, first public 2026-09-03. Its ternary construction establishes all-length existence at parameters near one, not the sharp finite thresholds at 27 and 28 or their multiplicities. Cheng et al., arXiv:1803.03530, Appendix A and Table 1, explicitly compute the **infinite-word** lower bound \(B_3\ge12/13\), not the length-27 and length-28 optimum, and their unpublished enumeration data may conceal overlapping intermediate results. Camungol–Rampersad, arXiv:1308.1620, analyzes equal-length adjacent blocks, not the unequal-length intervals required here. Comparisons with related published mathematical records and a ledger of earlier available claims identified no covering statement. Priority cannot be certified against unindexed manuscripts or unavailable historical code.

## Value — PASS

For the newly established ternary synchronization-string existence problem, a sharp short-length phase transition quantifies the precise limit of a three-symbol labeling scheme at demanding edit-distance parameters. The exact natural cutoffs, one canonical 27-symbol extremizer and thirteen canonical 28-symbol minimizers are nontrivial finite extremal facts with reproducible certificates and clear bearing on improving finite blocklength synchronization parameters; the result neither claims a new long-string construction nor assumes a downstream theorem.

## Scientific limitations and closest prior work

The result treats only three-symbol strings and the standard insertion/deletion synchronization condition; its full minimum-parameter spectrum stops at length 28. The older computational bound for an infinite string is stronger numerically but neither entails nor reports the finite classification. Independent validation, and definitive priority checking of unpublished intermediate enumeration data, remain open.

Self-review: passed. Independent audit: not yet performed.
