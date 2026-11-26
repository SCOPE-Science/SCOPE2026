# Independent mathematical audit

## correctness

PASS

Counting the abc triangles by deleted-edge incidences proves the ab lower bound. Equality forces exactly one deletion per triangle, only on largest-incidence sides. This gives the unique minimum or independent switches at A in the first two cases. In the balanced exact-one equations, two differing AB rows have a nonzero constant difference and hence are constant 0/1 rows; subtraction against either forces every AB row constant, AC complementary, BC zero. Column variation is the symmetric case. A constant AB matrix either is a pure side or leaves a C-split. Two families meet only at their common pure-side state. Within a family the batch cost is class size times Hamming distance. Across two balanced families the only overlap is on AB, of size (n−p)(n−q), so the cost n(p+q)−pq exceeds n for p,q≥1 and n≥2. This proves both sharp thresholds and that the cubes are glued solely at the specified corners. The antipodal corner distance is n, so leaving a cube cannot shorten its internal metric; for distinct cubes the two shortest routing options have lengths s and 3n−s, for s the sum of distances to their shared corner. All integers 0≤s≤2n are realized, giving diameter floor(3n/2). Independent exact-one branching and BFS gave balanced (count, diameter) (9,3), (21,4), (45,6), (93,7) at n=2,3,4,5; it also checked representative asymmetric cases.

## originality

PASS

The distinct contribution is the first connected optimum-preserving batch graph and its exact geometry. The scalar optimum and the broader transversal description are prior coverage; the minimum-family description is treated as a specialization with equality, not independently claimed. No inspected statement covers the exchange metric, subject to the stated access and indexing limitations.

## value

PASS

In a natural family of extremal graph problems the minimum exchange size determines when any optimum can be changed at all; at the onset the result gives the full labelled state graph and worst-case distance. The balanced three-cube gluing captures a genuine qualitative change from the single cube with two tied classes, beyond the scalar optimum or the number of optima.

The dated certificate retains the supplied scientific assessment, sources and limitations.
