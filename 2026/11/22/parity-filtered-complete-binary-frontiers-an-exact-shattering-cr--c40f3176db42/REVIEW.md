# Independent mathematical audit

## correctness

PASS

Comparable queries cannot both be selected, and sibling leaves must be selected together. For a permissible support, positive queries plus parents of negative queried leaves are an antichain; completing with original leaves realizes the trace. A free bottom parent can be split or not without changing this trace. With no free parent the all-positive frontier is forced: internal queries remain and a queried leaf requires its sibling. Changing only a bottom-level query forces the opposite split decision in that slot and reverses parity. If all queries are higher, they form a complete frontier; replacing each negative query by a three-vertex descendant frontier preserves parity, while all positives force the parity of the support. Counting all permissible supports and those touching every bottom parent by the root-or-two-branches decomposition yields A_h and B_h; upper frontiers supply the disjoint parity projection of K_{h-2}. Disjoint occupied bottom-parent blocks force the size and count of largest supports with one free block, while upper supports have size at most half the number of those blocks. Height two is checked separately and for every h>=3 the odd root singleton and even pair of root children are inclusion-maximal and strictly smaller than maximum size. In Step 3 parity refers to the constructed realizations, not to all realizations of a negative trace. Independently enumerated frontiers via prefix-closed split sets and checked traces at h=2,3,4 (python3 /workspace/checks/finite_review.py 2; /workspace/checks/2.txt), matching all recorded counts, including 73901/73902 faces at h=4. Enumeration is bounded; the all-height claim uses the structural proof.

## originality

PASS

The unrestricted pair obstructions, A_h and unrestricted nonpurity are already covered. The distinct result is the exact effect of parity: deleting supports with all bottom blocks touched, restoring exactly the parity-matched upper frontiers, and obtaining the resulting extremal counts and nonpurity for each parity. No inspected stronger statement entails that parity restriction. The conclusion is limited to checked evidence.

## value

PASS

Parity of the number of leaves is a natural global constraint on complete prefix codes. The local free-block criterion and exact exceptional upper fronts determine every face, explaining features that the one-unit VC loss alone misses, including parity-dependent small facets and the maximum-support census. This is structural information at every height, not just an enumeration of small trees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
