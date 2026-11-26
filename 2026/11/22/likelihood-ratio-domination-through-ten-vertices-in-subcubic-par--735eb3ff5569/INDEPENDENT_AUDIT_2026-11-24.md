# Independent mathematical audit

## correctness

PASS

Deleting a spanning-tree leaf of any connected graph of order ≥2 leaves a connected induced graph; in the subcubic case reverse deletion attaches the new vertex to 1–3 distinct vertices of old degree ≤2. This proves completeness by induction even when using only one representative of each old class. The implementation's neighbor-degree profiles and color keys are preserved under isomorphism, and within a bucket the bijection search checks both edges and nonedges. On an available set A, the next vertex is uniform and the new set is A minus its closed neighborhood; conditional on that state the same rule applies, so the rational recurrence is exact. The static count is uniform over independent dominating sets, exactly the maximal independent sets. Every such set is reached by priorities putting all its members first, so both size laws have the same support. Exact adjacent ratio inequalities give all pairwise inequalities; since the nondecreasing ratio has mean one under the static law, its conditional means on lower tails are ≤1, which gives the first-order consequence. The original programs and outputs were inspected, not executed. In particular the separate priority check shares the graph generator and only cross-checks the laws through order six. A fresh, separately written complete bounded replay with its own isomorphism routine and exact fractions checked all 2,571 classes with zero violations and returned all order-by-order counts in the corrected table, including 1,687 unequal and 46 equal at order ten. Replay with python3 /workspace/branches/e1c4f22c-2be4-40a4-847f-f10e06b42e53f/replay_subcubic.py --max-order 10; actual rows are in replay_1_to_10.jsonl in that directory.

## originality

PASS

For the repaired claim only: prior first-order computation already covers the domain (and more), and the graph-class counts themselves are known. The positive exact result on point-mass likelihood ratios through order ten is a stronger property, not a mechanical consequence of the earlier first-order statement. A same-day distinct likelihood-ratio record overlaps at small orders but its six-vertex counterexample has maximum degree five and does not treat the larger subcubic domain. No exact prior coverage of the repaired likelihood-ratio claim was established in the examined material.

## value

PASS

The repaired claim establishes a stronger shape constraint on the size laws than first-order dominance. Subcubic graphs are singled out by the motivating conjecture; a nearby exact result shows likelihood-ratio failure for unrestricted degree already at six vertices, so complete success over the much richer sparse domain through ten is meaningful finite evidence for a different order relation, not a tabulated-count recomputation or another check of the published first-order conclusion. The exact count of equal laws distinguishes genuinely separated size laws from degenerate/equal cases. No claim of a new first-order cutoff or of extending prior first-order computations survives in the repaired files.

The dated certificate retains the supplied scientific assessment, sources and limitations.
