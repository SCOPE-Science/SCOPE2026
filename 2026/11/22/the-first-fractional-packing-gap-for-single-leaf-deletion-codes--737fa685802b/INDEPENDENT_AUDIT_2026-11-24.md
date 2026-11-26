# Independent mathematical audit

## correctness

PASS

For each missing label, subdividing any of the 2n−5 edges of an (n−1)-leaf output and adding that label produces a different extension; deletion and suppression recover that edge. Summing the constraints for one fixed label bounds the objective by (2n−7)!!, and the uniform weight 1/(2n−5) attains it. The witnesses at n=4,5,6 cover every output exactly once; the n=6 construction pairs the unique noncherry leaf of each five-leaf receiver with the missing label. Independently generated all topologies by taking the smallest leaf as an anchor to an unordered binary hierarchy on all other labels; constructed the receiver by literally deleting the leaf, contracting and rerooting at the smallest surviving label. Compared all 945×7 incidences with incidence7.txt, and validated the smaller codebooks. For n=7 a 105-word code must cover all 735 receivers exactly once, with seven receivers per source and nine sources per receiver. Independent bitmask exact cover partitions possible covers by the unique selected row covering receiver 0, then recursively chooses an uncovered receiver with minimum support among eligible rows; the children select each covering row in turn and discard all overlapping rows. A branch with an unsupported receiver is impossible and an empty residual receiver set is success. All nine initial slices returned false, with 1,630,010 recursive calls across the slices; the rule scans all residual columns for a zero rather than stopping at the first unit, so the count need not match the frozen solvers. Replay with python3 /workspace/branches/replay3.py; completed slice logs replay3-012.txt, replay3-345.txt and replay3-678.txt in /workspace/branches. No uploaded code was executed. This confirms the first strict optimum-value gap, not a classification of all vertices of the packing polytopes.

## originality

PASS

Leaf restriction as an operation and the counting/packing argument are not novel. Neither same-object statistics nor adjacent tree-channel results checked yield the seven-taxon nonattainment in this known-missing-label channel. The visible exact hit ending 737fa685802b is the assigned record itself, not independent coverage.

## value

PASS

This is the first failure of the natural per-missing-label counting bound for a standard family, not a computation at an arbitrarily selected size. For every earlier feasible size in scope there is simultaneous perfect decoding, including the structural three-cherry construction. Seven taxa still have exactly regular nonempty fibers, but these cannot be satisfied simultaneously. The precise transition provides a finite obstruction and a benchmark for any general capacity argument.

The dated certificate retains the supplied scientific assessment, sources and limitations.
