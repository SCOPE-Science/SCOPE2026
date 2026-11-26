# Independent mathematical audit

## correctness

PASS

A shattered depth-d tree exists exactly when some comparison leaves two depth-(d-1) shattered version spaces; each branch must have at least 2^(d-1) orders. I tested this recurrence independently using complete comparison-sign patterns filtered by the queried sign constraints. The 2,520-order branch for 1<2 passed depth 10 and failed depth 11; all pairs and both outcomes at the unrestricted root are isomorphic by relabeling, so the unrestricted dimension is 11. For n=1 through 6 the independent search reached 0,1,2,4,6,9, and the cardinality bound certifies the respective upper bounds. Routing each permutation separately through the attached tree, with outcome 0 first, reached all 2,048 leaves with minimum occupancy 1. Replay: python3 /workspace/branches/audit_comparison.py with the frozen permutation_comparison_witness.json path as its argument. The check says nothing about ranks beyond seven.

## originality

FAIL

A distinct indexed finding already gives rank 11 on all seven-element total orders and explicitly identifies seven as the first cardinality deficit. With unrestricted pair queries every root comparison and outcome are relabelings, so the comparison-root recurrence gives rank(unrestricted)=1+rank(1<2). The conditional 10 is therefore covered by implication even if not stated separately. This is a coverage judgment, not a priority judgment from path dates. The witness does not salvage a distinct mathematical claim, and the available evidence does not establish that the two witness trees are identical.

## value

FAIL

The first deficit is a meaningful test of the information bound for adaptive comparison trees, but this record supplies no distinct useful exact invariant after accounting for the indexed exact census and the immediate conditional-rank implication. The particular reproduced witness and rerun of the exact recurrence substantiate correctness, not an additional valuable finding or a new method relative to the indexed finite certification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
