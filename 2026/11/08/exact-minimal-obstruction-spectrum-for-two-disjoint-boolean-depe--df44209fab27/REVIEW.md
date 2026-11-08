# Scientific review

## Correctness — PASS
The split/disjoint-function envelope equivalence is proved in the result. The 16 total-function pairs give 16 maximal 12-row satisfying teams, and their four-row complements are precisely the transversal constraints. Exhaustive checks of all 65,536 Boolean teams show 32,377 satisfiers and 132 inclusion-minimal failures; their size polynomial is \(12z^4+16z^5+96z^6+8z^8\). The nine-orbit obstruction certificate proves no minimal falsifiers were omitted. Independent 2-SAT and envelope checkers agree. The eight-row maximal minimal obstruction is explicit (`0x5a69`). All three included checkers executed successfully.

## Originality — PASS within inspected evidence
Fröhlich–Kolaitis–Meier (arXiv:2508.16146, DOI:10.4230/LIPIcs.CSL.2026.10) prove the unrestricted formula incoherent and give 2-SAT model checking; neither result states the exact fixed-binary 16-envelope/132-minimal-transversal classification or nine orbit sizes. Barlag et al. (arXiv:2605.31269) establish the general semantics and coherence/rewritability landscape, including generic bounds for Boolean teams. The exact minimal-obstruction polynomial is not entailed by the general statements alone. Relevant full-text sections were inspected, source-alias searches were conducted, and published similarity records were compared. A matching unindexed computation is a residual priority risk; no independent priority audit has been done.

## Mathematical value — PASS
This is a complete classification of admissible and minimally forbidden tables for the smallest nontrivial alphabet under a natural split-functional-dependency integrity constraint. The eight-row local test is sharp, half the naive 16-row bound, and the nine symmetry classes organize all forbidden obstructions. Both the exact hereditary profile and its dual maximal-envelope system provide reusable finite constraint information beyond the general fact of unrestricted incoherence.

## Scope and limitations
The binary alphabet, four named attributes, set-valued teams, and lax disjunction are essential; no extension to larger alphabets or other formulas is asserted. Exhaustive enumeration is a proof only for the stated finite case. Historical priority beyond accessible sources remains unverified.

Self-review: passed. Independent audit: not yet performed.
