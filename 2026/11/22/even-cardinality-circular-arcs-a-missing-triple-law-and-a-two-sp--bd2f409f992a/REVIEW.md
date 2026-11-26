# Independent mathematical audit

## correctness

PASS

A length-two interval isolates either point of a pair and each singleton of a nonconsecutive triple; a consecutive triple's middle singleton is impossible. On a nonconsecutive triple the arc joining two selected vertices while avoiding the third can be extended at an endpoint if its length is odd: if both extensions hit the excluded point, that point has both selected vertices as its neighbors, a contradiction. Empty/full traces are supplied by definition, and cyclically alternating membership on four points is impossible. This proves the face counts, including no triangles at n=4, where K4 has cycle rank three. For n≥6 the apex i+4 is not adjacent to any vertex of the omitted triangle {i,i+1,i+2}; coning its boundary gives a disk consisting of present triangles, including for n=6. Attaching the omitted triangles therefore leaves the fundamental group unchanged and recovers the simply connected full two-skeleton. Integral H2 is a subgroup of the free 2-chain group, and the Euler characteristic gives rank binom(n−1,3)−n. Hurewicz and homological Whitehead then give the claimed wedge. Inspected the supplied proof/check_even_arcs.py, proof/check_even_arcs.cpp and their archived outputs (Python through n=18, C++ through n=20, F2 boundary ranks through n=14); not rerun. Those checks do not prove integral homotopy, which follows from the disk argument.

## originality

PASS

The inspected sources do not cover the even-length arc class on even cycles. The same missing-triple rule in a neighbor class on odd cycles is important overlap, but complement preserves cardinality parity at the audited even orders. Nearest even-order comparisons have different triangular faces and topology. The decision is scoped to the exact even-cycle classification and integral homotopy claim, not to general arc VC bounds or priority against unindexed work.

## value

PASS

Cardinality parity is a natural restriction on cyclic range queries distinct from shortest paths or balls. The exact description identifies which triples fail (not just the VC dimension) and shows that losing precisely those faces changes the top sphere rank without creating first homology at all even orders ≥6, with a sharp circle-wedge exception at order four. These are useful exact comparators for cycle shattering complexes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
