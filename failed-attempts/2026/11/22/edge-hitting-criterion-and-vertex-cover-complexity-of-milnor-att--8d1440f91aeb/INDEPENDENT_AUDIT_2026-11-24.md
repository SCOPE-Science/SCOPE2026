# Independent mathematical audit

## correctness

PASS

A graph homeomorphism preserves topological valence and permutes the essential open edges. A positive iterate preserves each chosen edge; compactness of its closure forces an accumulation point there for every start in that edge. Full support gives the obstruction to avoiding its closure. Conversely, after parametrizing each edge, fix A and the essential vertices, and use increasing interval maps on the complementary gaps. Every gap has at least one target endpoint. With two target endpoints, a single fixed midpoint separates two monotone drifts; with one endpoint the whole interior drifts toward it. The displacement on a gap is at most half the distance to its gap endpoints, so the maps glue continuously, also with identified loop endpoints. They are edgewise increasing bijections. Off the target, only countably many fixed midpoints and finitely many essential vertices can fail to converge to A, a null set. For any a in A and neighborhood U, either some open subinterval there is fixed in A, or take a nearby complement point on an incident parameter arc from a, with no intermediate essential vertex. The gap containing it has an intervening endpoint belonging to A inside U; an open one-sided subinterval flows to that endpoint. Thus any closed C missing a point of A misses limits of a positive-mass set; A is the smallest full-basin closed set. The circle follows by cutting at a target point. On a nondegenerate simple graph with no degree-two vertices, essential closed edges are the ordinary closed edges. Replacing any interior hitter by a corresponding endpoint cannot lose coverage of any other edge. This establishes exact equality with vertex-cover size. A vertex cover is a polynomial certificate and Uehara's Theorem 3 gives hardness already on a subclass of connected cubic planar simple graphs. Exact-size and at-most-k cover versions coincide on k<=|V| by enlarging a cover.

## originality

FAIL

There is material equivalent coverage of the flagship edge-closure characterization in distinct indexed record bf1de8186f38. Although that record states the Milnor part for measures equivalent to arclength, its actual proof uses arclength only to give positive mass to nonempty open sets and zero mass to a countable exceptional set. The same proof therefore gives the full claimed nonatomic full-support version, not merely its arclength specialization. Its separate generic-limit-set conclusion is stronger in another direction. The frozen record's vertex-cover identity and complexity conclusion are not stated in the comparison record, but are immediate consequences: a graph of the designated type has precisely its ordinary closed edges as essential edges, and replacing an interior hitting point by an incident vertex cannot uncover any other edge. The known vertex-cover hardness then transfers by identity. The evidence establishes overlapping coverage and mechanical implication, not chronological priority between records dated the same day.

## value

FAIL

A sharp finite-graph attractor classification and a link to vertex-cover optimization are mathematically natural. In this submission, however, the classification is covered and the difference does not yield a distinct substantive result: the measure variant is a direct reading of the compared proof, and the vertex-cover size and NP-completeness require only substituting ordinary closed edges and replacing interior points by endpoints. They are useful interpretations but not a separately unknown exact invariant after the indexed theorem is accounted for.

The dated certificate retains the supplied scientific assessment, sources and limitations.
