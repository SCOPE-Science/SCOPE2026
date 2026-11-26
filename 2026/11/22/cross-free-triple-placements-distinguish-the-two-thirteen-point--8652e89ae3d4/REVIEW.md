# Independent mathematical audit

## correctness

PASS

For four points per class all but one point are assigned, so all 20 blocks off the unused point need an intra-class pair; the 18 available pairs cannot serve 20 distinct Steiner blocks. Restriction excludes larger placements. Pair uniqueness for both explicit designs was checked independently. For three points per class, I enumerated the 200200 unordered disjoint triples of classes per design, using the third point of each A-by-B pair to mark forbidden elements of C. I built the graph by grouping legal placements by the two unchanged classes and the two retained points of the changed class. Each bucket is a clique, each exchanged pair has exactly one bucket, and both endpoints' extra points are unused at the opposite endpoint. This exhausts the graph without using the archived outputs. It gave 6214 vertices, 25896 edges and components of sizes 5902, 39 times 4 and 156 times 1, versus 6148 vertices, 25032 edges and sizes 5904, 18 times 4, 4 times 7 and 144 times 1. Four-vertex components are complete; in each seven-vertex component the universal vertex leaves a 2-regular six-vertex graph containing a triangle, necessarily two triangles. Intersection and differences were 3868, 2346 and 2280. The unequal counts additionally certify nonisomorphism of the constructed designs; the count is invariant under relabelling, while the overlap uses the fixed common labels. In the exchange lemma, legality of adding a point is independent of the removed point because only newly rainbow blocks using the added point can violate the condition. Its four choices of the omitted point give a clique, and no distinct moves share the same destination after forgetting class names. The scope is precisely the two isomorphism types on 13 points, not designs on other orders or an isomorphism classification of the giants. Replay: python3 /workspace/branches/replay_3_5/scope_frozen_12345_sts.py, with recorded stdout in the matching .log. Archived programs and expected outputs were inspected, not run.

## originality

PASS

The exact finite placement and exchange-graph census is distinct from the inspected cross-free and exchange-graph antecedents. Neither the cross-free definition, the Pasch switch nor the predicted maximum of three is new.

## value

PASS

Order thirteen is the first nontrivial comparison of nonisomorphic Steiner triple systems. The trade perturbs the extremal objects of the existing cross-free problem, and the census measures both the change in their number and the effect on local move connectivity. The emergence of seven-vertex glued cliques only on one side and the exact overlap are structural benchmarks for reconfiguration or trade-sensitivity work, not a recomputation of the order or block counts. The exchange lemma explains the basic clique structure without pretending to classify larger orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
