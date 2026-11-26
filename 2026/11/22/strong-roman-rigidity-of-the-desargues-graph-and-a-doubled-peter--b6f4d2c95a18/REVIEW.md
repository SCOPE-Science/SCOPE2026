# Independent mathematical audit

## correctness

PASS

On the cubic inclusion graph, each 2 can certify at most two zeros, and each 3 at most three, so for label multiplicities (a,b,c) at 1,2,3 the bound is 3w−40≥a+c. This excludes w≤13 and restricts w=14 to (0,7,0),(2,6,0),(1,5,1),(0,4,2). A separately written exact enumeration checked respectively 77,520, 3,527,160, 3,255,840 and 581,400 placements and found 0, 40, 0, 0 survivors. The rule was also checked directly on the survivors. They have the claimed shore counts and 10 complementary versus 30 incident one-label pairs. The complete pairwise Hamming histogram is {6:60,8:60,10:180,12:360,14:120}. At six the ten hubs correspond to two-subsets and each disjoint pair has exactly two common intermediate states of degree two; no other edges occur. For the specific ordered-pair indexing, the orbit of an incident one-label pair (A,B^c) determines one state because the 30 possible incident pairs form a single orbit and exactly 30 states occur. Its two neighbor anchors are disjoint and invariant as a pair under swaps within A and within B. Other two-subsets lie in an orbit of size four or an orbit of size two whose members intersect, so the two anchors must be A and B. The base Petersen graph is connected of diameter two. In the doubled subdivision every hub has eccentricity five (there are edges of the base both of whose endpoints intersect the hub); every intermediate vertex has eccentricity six (e.g. for base edge {01,23}, use {02,13}, where every cross pair intersects, and use symmetry). Thus radius five, diameter six and sharp connectivity threshold six follow for full-label Hamming exchanges among optima only.

## originality

PASS

No equivalent exact strong Roman result was established by the sources checked. The known invariant and general bounds are background. Prior Desargues Roman censuses and exchange graphs use ordinary Roman validity and different move definitions, so they do not cover the strong Roman weight, optimum-state census or doubled Petersen exchange graph.

## value

PASS

The problem couples a standard optimization invariant on a canonical cubic graph with a natural optimum-preserving exchange rule. The full census explains, via label-pair geometry, why the first possible moves make a connected doubled Petersen subdivision. This identifies more structure than a single exact domination value or an unaided finite search output.

The dated certificate retains the supplied scientific assessment, sources and limitations.
