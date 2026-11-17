# Independent mathematical audit

## correctness

PASS

The graph is KG(5,2) with 15 edges, four *named* edge colours, and adjacency by one legal edge recolour. At each cubic vertex, recolouring an edge swaps its local colour with the missing one, changing each endpoint permutation sign; their product is invariant. The move criterion is equality of endpoint missing colours; frozen maps have pattern (4,2,2,2). Two exhaustive verifiers were inspected (DFS colour assignments versus four matching-class partitions). Independently generated 49,920 states, 109,440 edges, 960 isolated and two connected components of 24,480; verified degree/sign profiles. An independently constructed complete A5 x S4 orbit enumeration gave 42 orbits and 40 full BFS over mobile representatives, radius 24, diameter 25, eccentricity census 38,880 at 24 and 10,080 at 25. These finite computations are exhaustive over THIS graph, not a general cubic theorem.

## originality

PASS

OEIS A159233 already counts the 49,920 named edge-colourings; explicitly prior. McDonald–Mohar–Scheide 2010 proves Kempe connectivity for all subcubic four-edge-colourings, but a Kempe switch along an alternating path/cycle is not a single-edge move. Ito–Kamiński–Demaine study exactly one-edge recolouring in general but not this exhaustive Petersen metric. The fully inspected Resultary Petersen vertex-colouring reconfiguration concerns a different configuration space, not edge-colourings (or vertex colouring of the line graph). Exact mobile sectors, sign completeness and radius/diameter remain independently qualified.

## value

PASS

The single-edge reconfiguration geometry of a canonical non-three-edge-colourable cubic graph is a natural finite boundary for recolouring dynamics. Exact connectivity obstruction and shortest-path metrics under the strict elementary move supply interpretable nontrivial data distinct from known Kempe connectivity and counting. The finite census is exhaustive and meaningfully structured by parity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
