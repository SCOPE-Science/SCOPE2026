# Independent mathematical audit

## correctness

PASS

Bottman–Poliakova's Definition 4.4 and the braid-chamber argument after Theorem 4.1 make the 5! orders exhaustive: every order determines a refining normal chamber, and every vertex chamber contains one. I implemented an independent exact allocation: assign each pair of parallel lines to the last adjacent collision in its span, and each rectangle (one pair from each axis) to the later of its two assigned collisions. At an event this adds W1*W2 for its parallel pairs, then one for each rectangle with an already joined opposite pair, giving precisely W1*W2*T. This generates 108 distinct vectors of coordinate sum 27. Exact traversal reproduces every row of CHORD_SPECTRUM.csv, with 174 nonzero keys, 5778 pairs, and top entries (424,4), (430,4). It also reproduces the exact four 430 pairs; every edge joins degree 2 to degree 1, giving two disjoint P3 and 102 isolates. Convexity passes the maximum from vertices to the whole convex hull. Replay record2() in /workspace/branches/frozen_metric_replay.py; the supplied checker was read, not executed. The Table 10 count must be read at Chapoton–Pilaud's native (2,3), not their native (3,4), because they index by collision slots rather than lines. This notation clarification does not affect exhaustion or the metric theorem. The title's 'first mixed' should be read as first unequal mixed case up to swapping axes, not as excluding the smaller mixed C(3,3).

## originality

PASS

The collision realization and the vertex census were already known. The complete pair metric in those coordinates, exact runner-up and diameter-graph structure are distinct from the inspected inball theorem and the separate shuffle realization. Priority remains a bounded best-of-knowledge assessment.

## value

PASS

The smallest unequal case with both axes in the mixed regime provides a natural low-dimensional test of interaction between the collision axes; it is not a numerically chosen coordinate slice. The exact pair invariant distinguishes Euclidean realizations not distinguished by their vertex counts. The complete spectrum and very sparse diameter graph with a sharp runner-up give reproducible baseline data for extremal-chord comparisons, with no extrapolation to other dimensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
