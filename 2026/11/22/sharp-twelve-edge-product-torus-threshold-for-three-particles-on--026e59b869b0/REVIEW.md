# Independent mathematical audit

## correctness

PASS

Both frozen edge lists were read without executing either program; they are identical, with eight disjoint triangles covering the vertices. Their contracted quotient admits an explicit bit-cube labeling, and each of the three vertices in a triangle has one external edge. Independently constructed the graph from cube vertices and direction ports. A nontriangle simple loop uses exactly two external edges at each triangle it meets, since the number of external crossings there is positive, even, and at most three. It projects to a simple cube loop and at each visited triangle independently uses the direct or the detour path. Vertex-disjoint nontriangular loops cannot share a cube vertex, because each uses at least two of the triangle's three vertices. Two such loops use all eight cube vertices, leaving no third loop. The cube has 6 simple four-cycles, 16 six-cycles and 6 eight-cycles by edge-subset enumeration. Thus the disjoint triple counts by maximum length d are 56 at 3, and otherwise 36 binom(4,d−8)+16 binom(6,d−12) with out-of-range entries zero, for 1656 total. In the reduced Świątkowski model the degree-one, weight-one local differences have boundary the difference of edge variables. One factor at each of three distinct vertices gives 16192 degree-three generators; two such factors and one edge give 39744 degree-two generators. Weight three has no degree four. On a cycle the sum of oriented local differences is the integral once-around generator. The model for the disjoint union of the three cycle subgraphs is the tensor product; the inclusion sends the weight-(1,1,1) fundamental class to the signed product of the three loop chains. The independent boundary reconstruction has rank 16096 over F2, hence rank at least 16096 over Q. Independently enumerated oriented torus columns have exact unit pivots, yielding 96 independent cycles and thus the matching upper bound on boundary rank. The pivot rows of the accepted torus columns give a triangular determinant ±1 after integral column operations, so their span is primitive in the ambient chain group. It is in the rank-96 kernel and therefore equals it integrally. Each filtration stage spans exactly the corresponding accepted columns, since all dependent reductions use integer coefficients. The ranks are 56 at 3, 92 from 8 through 11, and 96 from 12 through 18. The selected columns are of the stated 56+36+4 types, and the quotient by L11 is free of rank four. The cutoffs are on the maximum individual cycle length, not total length or exactly d.

## originality

PASS

The supported distinct claim is the truncated cube's integral top-homology filtration by constituent-cycle length, including the sharp cutoff and free rank-four deficit below it. The model, product-torus construction and finite elimination method are not original here. The closest available graph-specific statements use the same kind of filtration on different graphs, and no located general theorem supplies this graph's exact filtered lattice. Several underlying primary passages and the closest analogue's full record were inaccessible, so this is a bounded comparison, not a priority certificate.

## value

PASS

For this natural trivalent polyhedral graph, the result tests whether the most localized product cycles, in particular those supported on faces, account for all top homology. They do not: the short-cycle lattice has an exact free deficit of four, persisting even at length 11. Length 12 suffices integrally, not just over a field. The primitive filtration and the shortest integral basis types add information to a rank computation, giving a precise benchmark for geometric generation in graph configuration spaces.

The dated certificate retains the supplied scientific assessment, sources and limitations.
