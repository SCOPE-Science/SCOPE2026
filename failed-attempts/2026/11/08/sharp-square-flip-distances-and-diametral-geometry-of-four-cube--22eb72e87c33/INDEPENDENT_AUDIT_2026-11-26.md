# Independent mathematical audit

## correctness

PASS

Independent code scanned all 8! even-to-odd bijections and retained exactly the cube-edge matchings. It formed adjacency by swapping two odd partners precisely when both crossed edges exist for the two even vertices opposite on a square. This gives exactly the legal move, with no hexagon moves or quotient by symmetry. Complete component traversal gave 272 states, 768 edges and one 264-state component plus eight singletons. All-source BFS in the mobile component reproduced the eight distance bins (768,2640,6032,9360,9504,5296,1104,12), totaling 34,716, and eccentricities 7 on 252 states and 8 on 12 states. It checked the supplied witness at distance 8, equality of the degree-four and peripheral sets, and a two-regular farthest-pair graph on three connected four-vertex sets. Applying all 384 translations composed with coordinate permutations verified both the peripheral matching orbit and the unordered diametral pair orbit. Replay: python3 /workspace/branches/e5186c03-e039-4713-b9ae-b355aac582e1/independent_q4_audit.py. The exact finite enumeration establishes the labeled Q₄ theorem, not any larger-box result; uploaded verifiers were inspected but not executed.

## originality

FAIL

A distinct earlier Resultary record states the same exact mobile diameter, radius, distance histogram, eccentricity tally, degree-four peripheral orbit and 3C₄ diametral geometry under the identical square-only move. Its complete orbit table also makes the degree-four converse explicit. The only residual assertion in the frozen Finding is that the diametral edges themselves are one orbit. This is confirmed by the independent calculation but was not found stated explicitly in the earlier text; the failure is for the materially duplicated submitted classification, not a claim that the earlier theorem states edge transitivity.

## value

FAIL

The square-only geodesic profile of the smallest four-dimensional box is a well-motivated finite benchmark, but its exact classification and peripheral geometry are already available. The sole additional count is a routine one-edge orbit tally using the previously constructed exact distance-eight graph and the same finite action, without a separate mechanism or a new substantial boundary. The frozen contribution as a whole is largely recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
