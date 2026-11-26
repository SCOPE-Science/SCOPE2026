# Independent mathematical audit

## correctness

PASS

An acyclic orientation determines a unique word of colors: linear extensions differ by swaps of incomparable vertices, and distinct colors are adjacent in the graph and comparable in the orientation. The consecutive monochromatic blocks give the cover relations: any two vertices in consecutive blocks are joined by an edge with no intervening vertex on a directed path; vertices in more distant blocks are related by paths through intermediate blocks. The cover graph is connected. Writing s_j for block sizes, its edge surplus over n−1 is sum over interior j of (s_j−1) plus sum over consecutive pairs of (s_j−1)(s_{j+1}−1), proving the stated tree cases including two blocks. A non-tree is nonsimplicial by its facet count; a tree's signed root normals form a lattice basis by leaf deletion, so the dual normal cone is smooth in any characteristic. For r≥3 the all-color projection removes the two-block term. Ordered labeled blocks contribute e^{x_i}−1, with x_i for singleton interiors; the two displayed resolvents sum exactly these transitions, with coefficient multiplied by the product of the class factorials. Independently enumerating all orientations and computing transitive closure and cover edges, without classifying by blocks, gave (smooth,total)=(58,78),(288,426),(1240,2286) in the three stated examples.

## originality

FAIL

The mathematics is correct, but the strongest earlier sources supply both the exact multipartite block-poset model and the general tree/facet criterion. They mechanically give the singleton-interior rule, and the smooth series is the ordinary word-count transfer formula with interior block weights restricted to the degree-one term. The unrefined count is explicitly covered by prior work. No earlier literal printing of the refined matrix expression was found; the failure is for mechanical implication, not a claim of verbatim prior publication. The substantial later catalogue overlap is not used to infer earlier priority.

## value

FAIL

Smooth fixed points form a natural invariant and the transfer formula is a convenient exposition, but the purported new refinement applies the existing tree criterion to the existing exact block model and changes only the allowed weights of the interior positions. Under the stated standard this routine restriction, already mechanically implied without a new classification or enumeration step, does not establish an independently useful unresolved fact; the illustrative small exact values are coefficients of the same restriction. No genuine surviving valuable remainder in the assigned claim was found to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
