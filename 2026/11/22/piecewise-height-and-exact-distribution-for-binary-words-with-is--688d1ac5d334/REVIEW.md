# Review: piecewise height of isolated-marker words

## Correctness
**PASS.** At depth \(t+1+M\) the required and forbidden patterns with all \(t\) markers fix every positive zero gap. The original insertion characterization and side-distance recursion show no smaller depth works, by cutting each zero gap and obtaining combined side depth \(t+a_i\). The inclusion-exclusion count and simplex limit are derived from positive compositions, with finite checker corroboration. The premise is cited and its proof inspected.

## Originality
**PASS, subject to residual priority risk.** The closest 2023/2024 papers give general height algorithms; the 2024 binary compressed-run reduction treats internal isolated letters but does not state the all-marker max-gap formula or height law in the inspected relevant results. A recorded weight-two height distribution and its limiting moments are acknowledged as prior, and the new range is \(t\ge3\). A four-run height enumerator applies to a different family. Searches do not establish global novelty, and equivalent unindexed work remains possible.

## Value
**PASS.** The formula is an all-parameter natural structural classification, and it unlocks the exact length-and-depth census and a longest-spacing probability law for every fixed number of at least three isolated markers. This supplies descriptive-complexity information not represented by a generic algorithm's ability to calculate one input.

## Limitations and comparison risks
The alphabet is binary; all zero gaps must be positive, and limit theorems hold at fixed marker count. General algorithms in the cited literature handle a larger word universe, and another already-existing result handles exactly two markers; these are not claimed as discoveries. Priority against unindexed prior statements requires external review. Computation covers only bounded examples.

Self-review: passed. Independent audit: not yet performed.
