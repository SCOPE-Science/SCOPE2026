# Independent mathematical audit

## correctness

PASS

The bijection encoding is exhaustive; two matchings differ on four duads iff their difference is one alternating octagon because there are no 4-cycles. A flip composes with an odd 4-cycle. I reconstructed the graph directly from the six symbols, using least-choice matching enumeration and explicit cycles in the duad projection (each line between consecutive duads is uniquely determined; reject repeated lines). It gives no 4- or 6-cycles and 90 distinct octagons, each alternating in exactly 32 states. Replacing either alternating assignment gives a reciprocal neighbor and yields 288 matchings, degree 10 and 1440 undirected flips. Layer expansion from each state proves connectedness and gives 144 even states of profile (1,10,45,97,96,37,2) and 144 odd states of profile (1,10,42,97,101,37), hence radius 5, diameter 6, and non-vertex-transitivity. Applying all 720 symbol permutations to one representative of each parity gives precisely its 144-member class. Traversing all 4-cycles once using minimum start and an orientation test gives 4320. The reconstructed state and neighbor lists agree with the full frozen certificate; girth 8 excludes all earlier possible moves. Replay: python3 /workspace/branches/local_exact_audit.py 5.

## originality

FAIL

Resultary 2d0e450ce331 already constructs the very same alternating-octagon matching graph, proves exact connectivity at the first possible cycle size and gives its metric and degree census, down to the sphere vectors of its two eccentricity classes. It even classifies the antipodes. I inverted the frozen state permutations, ranked them lexicographically and serialized the edges in the earlier verifier's labeling and format. The SHA-256 digest is exactly the earlier one (ba8739d1315a1daa2d3810948317a38cdf47b81a8cd37f5377e6825b7136e6a3). The earlier result thus covers the core even though its class labels use complementary cycle type, not parity. I did not find an explicit prior statement of the S6 orbit identification, 4320 flip quadrilaterals or 32 matchings per octagon. These are direct orbit/tally extractions from the already generated exact labelled matching graph and cycle flips, not a distinct shortest-cycle geometry result.

## value

FAIL

The first legal exchange length, connectivity and exact metric classification would be valuable unknowns, but they are already resolved for this exact graph, including stronger antipodal information. The extra parity label is elementary and the new tallies/orbit confirmations run directly on the previously generated full labeled state graph, with the already explicit symmetries and move list; the frozen result does not identify a separate non-mechanical scientific gap or useful distinct structural claim in that remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
