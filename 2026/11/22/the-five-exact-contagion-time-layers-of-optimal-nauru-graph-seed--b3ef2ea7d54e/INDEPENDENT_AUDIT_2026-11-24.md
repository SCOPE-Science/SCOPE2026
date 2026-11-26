# Independent mathematical audit

## correctness

PASS

In a cubic graph, the synchronous inactive-set dynamics remove induced degree 0 or 1, so a cycle survives forever and a forest is removed. A tree of diameter d has stripping time floor(d/2)+1, including a singleton, by peeling both ends of a longest path toward the center. The two counts of residual edges give 2k=12+e(S)+c and k>=7 for any proper seed. An independently written enumeration classifies each of the 346104 seven-subsets by connected-component vertex/edge counts and obtains times from two breadth-first sweeps per residual tree, without simulating infection. It recovers 12384 percolating sets. The one-tree/two-tree rows for rounds 4 to 8 are (0,120), (1872,1416), (4968,1488), (1224,360), (864,72). The extreme order/diameter profiles and multiplicities also match exactly. Existence at k=7 completes the lower-bound argument.

## originality

PASS

The distinct claim credited is the full minimum-seed census by exact synchronous time and residual shape, not the scalar minimum, the decycling reduction, or the elementary peeling formula. The strongest inspected analogues do not give or mechanically imply this joint census for GP(12,5).

## value

PASS

The natural minimum-size stratum on a named symmetric cubic graph exposes a genuine timing/geometry relation: every fastest optimum leaves two trees, whereas the slowest stratum contains both connected and disconnected residual forests with precise extremal diameters. The joint table is usable as an exact benchmark for algorithms that optimize seed size and time concurrently. The value is in the complete natural classification, not simply finding the known optimum or applying a generic graph routine.

The dated certificate retains the supplied scientific assessment, sources and limitations.
