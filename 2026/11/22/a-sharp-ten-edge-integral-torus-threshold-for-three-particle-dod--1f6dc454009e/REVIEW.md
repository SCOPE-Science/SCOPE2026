# Independent mathematical audit

## correctness

PASS

Independent replay: python /workspace/review-evidence/3.py. It reconstructs GP(10,2), enumerates every simple cycle via its least edge, verifies girth 5 and 1,168 cycles, and enumerates all relevant vertex-disjoint triples: no cycle over length 10 fits alongside two cycles of length at least 5. The 56 triples split 20/30/6 at maxima 5/8/10. Using a different vertex numbering, consecutive reduced half-edge differences, and signed exterior products, the replay gives 9,120 top chains, 22,800 degree-two chains, 56 zero integer boundaries, binary differential rank 9,094, and unit minors (-1,+1) for the 20 and 26 chosen chains. This gives a rational kernel of dimension 26, and the full unit minor gives an integral coordinate retraction: no finite index remains. Every octagon chain matches a signed pair of distinct pentagon chains in all coordinates; independently, each octagon is the outer boundary of two pentagons sharing an edge, with no new vertices, so this relation is compatible with the other two disjoint cycles. The first 20 elements of the basis span a primitive lattice, leaving a free rank-six quotient. The exhaustive maximum-length list rules out generation at nine as well as eight. The weight-three reduced comparison theorem, its natural embedding maps, and its tensor product on disjoint subgraphs identify the signed cycle products with actual geometric tori of the unordered space, not merely cycles in an arbitrary chain complex. The frozen verifier and output were inspected, not executed.

## originality

PASS

The ambient top rank and general chain/geometric-class machinery are known. The distinct contribution is an identified integral basis of product tori and the primitive strict cycle-length filtration up to the sharp threshold, including every octagon relation in this graph. Neither an arbitrary integral nullspace basis nor a two-particle torus lattice computes that filtration.

## value

PASS

The dodecahedral graph and its face loops give a natural geometric filtration of a known configuration-space group. Knowing that face tori already span a primitive rank-20 subgroup, that all allowable octagons add nothing, and that six specific ten-cycle tori supply exactly the missing primitive generators distinguishes geometry and integral structure invisible to the known Betti number. This is an exact usable basis and cutoff, not a repeat of the rank calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
