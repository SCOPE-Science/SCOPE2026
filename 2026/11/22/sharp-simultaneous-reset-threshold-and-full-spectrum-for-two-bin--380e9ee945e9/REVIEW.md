# Review of the sharp three-state synchronous-product reset spectrum

## Correctness — PASS

The claim is finite and exactly delimited: two independently labeled three-state complete automata with the same binary alphabet. The base-three encoding covers all \(729\) component tables; the Cartesian-image lemma reduces product resetting to membership in both component reset-word languages. The full subset-reachability search proves that the 180 excluded components are genuinely nonsynchronizing, not merely without short words. Exhaustive direct evaluation of all binary words through length six gives a common reset for every one of the \(549^2\) synchronizing pairs and the precise six-entry spectrum. An independently coded C++ subset-pair BFS agrees; explicit symmetry enumeration yields eleven extremal orbits, and the displayed witness is proved minimal by direct enumeration of all shorter words. Both checker paths and outputs are embedded. The theorem asserts no extrapolation to larger automata.

## Originality — PASS against inspected evidence

Fernau–Rystsov, arXiv:2611.09136v1 (2026), supplies the intersection identity and the general max/sum bounds, but the relevant complete HTML sections do not state the exact 3-by-3 binary spectrum, sharp six bound or eleven orbits. Volkov's 2022 survey supplies individual three-state reset upper bounds and finite-subset search, not a pairwise product census. A separate published claim on simultaneous Černý resets treats the restricted Černý family, not all 729 binary three-state transition tables, and therefore cannot imply the full conditional distribution. Searchable prior summaries and open primary literature were compared by mathematical domain and implication; no full-word prior covering the result was found. The complete text behind the specialized published summary was inaccessible, and possible unindexed equivalent finite classifications remain a residual originality risk.

## Value — PASS

The direct product uses one input controller to synchronize two devices simultaneously, and the 2026 product-operation paper explicitly poses questions about when generic bounds are tight. The natural first genuinely nontrivial equal-size pair has component reset thresholds at most four, for which the sum bound only gives eight. The sharp cutoff six, exact full spectrum over all labeled choices, and eleven extremal symmetry types quantify a real two-letter shared-control obstruction without arbitrary parameter slicing or a known-table recomputation. This is a natural complete finite classification, not a claim about asymptotic state complexity.

## Limits and closest literature

The result applies only to binary three-state component pairs; no inference is made about larger state sets or more letters. It was verified by finite complete computations with fully included source programs, not by a symbolic state-size induction. Relevant literature: Fernau–Rystsov (2026), arXiv:2611.09136; Volkov, *Synchronization of Finite Automata*, Russian Mathematical Surveys 77(5); a published finite comparison record about simultaneous Černý pairs, for which only the summary could be inspected. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
