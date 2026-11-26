# Independent mathematical audit

## correctness

PASS

The tested predicate is exactly distinct edge-distance codes plus coverage of each edge by a distance-0 or distance-1 code entry, not domination of the selected vertices or resolution of vertices. I independently recomputed the finite census using shortest paths, ternary edge codes for every mask up to size six, pairwise XOR for all possible moves, and an orbit-weighted BFS. The binary point labelling 1,2,4,3,6,7,5 in cyclic point order maps each line triple of the cyclic construction to a triple with binary xor zero; every such triple is the nonzero part of a normal's orthogonal plane. Thus the graph used is exactly the specified incidence graph. The 6,476 candidate sets give edge-resolving counts (0,0,0,0,0,168,1890); all 168 five-sets miss one coverage edge and the simultaneous minimum is six, with 1386 states. The containment counts are (574,672,84,56). Jump transitions are exactly two changed bits, with slide transitions additionally requiring that bit pair to form a graph edge. BFS reaches all states from all orbit representatives and yields jump edge count 17514, radius/diameter 6/6; slide count 5040, radius/diameter 7/9. Both full pair histograms match RESULT.md lines 38–50. A bipartition-preserving automorphism must preserve the operation taking two distinct nonzero points to the third point of their line, which is their binary sum; extending by zero makes this a linear map. The 168 choices for an ordered basis image produce all such maps, and the point/normal interchange gives all bipartition-reversing automorphisms. Orbit sizes are (14,28,28,56,84,168,168,168,168,168,336). An incidence automorphism preserves both predicates and both move rules, so weighting shortest-path results by orbit size and halving positive-distance ordered counts is exact. The independent reconstruction is reproducible from /workspace/branches/heawood-enumeration.js. The two frozen programs verify_incidence.py and verify_binary.py and their outputs were inspected, not executed. The proof and replay are for this 14-vertex graph only.

## originality

PASS

The underlying invariant and the 168 Heawood edge-only bases are prior. The same-graph antecedent has a strictly weaker feasible-state definition and cannot provide the larger joint-predicate minima or their move graph by restriction or augmentation of its own minimum states. No compared broader statement or exact prior table covers those claims; the result is qualified by the finite source coverage.

## value

PASS

The combined invariant and the Heawood graph are both pre-existing natural objects. The precise one-landmark cost and the contrast between disconnected old slide optima and connected new slide optima answer a motivated structural question about adding local coverage. The exact radius/diameter and the census of optima inaccessible by a one-token augmentation of an old basis give useful benchmark facts not mechanically obtained from the weaker census. No all-order claim or applied sensor performance is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
