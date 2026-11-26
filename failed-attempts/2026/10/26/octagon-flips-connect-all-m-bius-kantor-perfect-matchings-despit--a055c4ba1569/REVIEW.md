# Independent mathematical audit

## correctness

PASS

The symmetric difference of two perfect matchings is a union of disjoint even alternating cycles; a single length-ℓ flip is equivalent to that difference being connected and having ℓ edges. A fresh finite replay (independent_gp83_check.py with output independent_gp83_check.txt) used least-uncovered-vertex exact cover to enumerate all 33 matchings, then tested all 528 unordered pairs. Separate cycle enumeration gave 24 hexagons and 30 octagons. The 96 length-six adjacencies give components 30,1,1,1; the mobile component has degrees 6^24,8^6, radius 3 and diameter 4. The 36 length-eight adjacencies give the three hubs, each with eight leaves, and exactly two degree-two paths per hub pair. The hubs are precisely the three hexagon isolates. The all-spoke matching cannot alternate on a hexagon: an alternating six-cycle would need three spokes, but any cycle uses an even number of spokes. A no-spoke matching has one of two phases on each rim. A six-cycle uses two spokes and rim paths of total length four; for alternation with no spokes selected, their lengths are 1 and 3. The matching phases in the positive strides +1 and +3 must then agree, so the two opposite-phase states are the other isolates. The replay verified octagon radius 3 and diameter 4, and eccentricity 3 at every vertex of the 132-edge union, with degrees 7^24,10^6,12^3. There is no four-cycle: with two spokes the rim steps ±1 and ±3 cannot have the same endpoints, and the rims are 8-cycles. Thus the successful maximum length 8 is least possible. The frozen scripts, certificate and recorded outputs were inspected, not executed. The replay's agreement with the certificate was checked on counts, structure and hub indices, not by claiming byte-for-byte replay. The proof permits all simple cycles, not just faces, and applies only to GP(8,3).

## originality

FAIL

A distinct indexed record states the same theorem for the same graph, same matching states and all simple cycles of the two lengths. The subdivided doubled triangle with eight leaves at each hub is exactly the claimed octagon-only graph; the other move rules and the sharp length bound are likewise covered, with additional two-factor types and pair-distance counts in the comparator. This is verified duplicate mathematical coverage at review, not a determination of historical priority: the comparator is catalogued later than the frozen source date. Explicit labels for the three frozen states and a different certificate do not furnish a separate substantive reconfiguration theorem.

## value

FAIL

A sharp difference between hexagon and octagon reconfiguration on this natural symmetric graph would be useful, and independently replaying it is valuable as corroboration. But the exact structure and threshold are already available in the independently catalogued classification, and the frozen item supplies no distinct claim beyond a routine coordinate identification of the three hubs. The alternative certificate does not add a new scientific result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
