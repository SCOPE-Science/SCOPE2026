# Independent mathematical audit

## correctness

PASS

The frozen saturation paragraph overreached by looking at other excitation times and did not correctly justify the recurrence for a general resting or refractory vertex. The complete replacement in repairs/5/RESULT.md derives it pointwise: total earlier contacts equal total later contacts, each excitation has at least r earlier contacts, and disjointness caps their joint count by 2r; equality forces exactly r to each adjacent layer. If the vertex itself fires one time away, that balance counts its r contacts at the time in question; otherwise any contact would contradict saturation applied to the excited neighbor. This repairs the proof without changing the claim. Rechecking downstream: connectedness makes firing multiplicity k uniform, periodic second differences make layer size constant, and p|e_t|=k|V|. Temporal Fourier analysis with integral adjacency permits frequencies of orders 1,2,3,4,6. Graph order prime to 3 excludes p=3,6 by multiplicity and forces k=3 at p=12. Vanishing at a primitive twelfth root forces a rotated equilateral triple at each vertex, hence four-periodicity. Balancing four phases gives opposite phase parity across edges and exactly r neighbors of each sign, with the converse checked on both resting phases; two parity orientations per signed vector count states, then divide by four. For the application, the incidence filtration proves integrality, Lucas gives residue 2, the pair-difference eigenfunction is nonzero with eigenvalue +m/2, and a two-step replacement bound proves the exact odd girth against the explicit odd walk. The labelled-orbit scope and lack of a transient bound are unchanged. See the repaired proof for analytic replay. The frozen verify.py and CHECK_OUTPUT.txt were inspected, not executed; they give only finite supporting examples and an exact spectral certificate for KG(7,3), not a state census for that graph.

## originality

PASS

The repaired proof is for the unchanged classification. The spectral ceiling is covered by a distinct catalogue result with wider graph scope, and the period-three size obstruction is covered by the prior half-degree three-phase classification. Credit the distinct surviving result for the full order-three exclusion, the signed-kernel temporal-orbit census, and the resonant odd-graph application. The same-day date of the spectral comparator does not establish priority or erase its overlap.

## value

PASS

The strengthened claim converts a coarse spectral period bound into a complete attractor classification on a natural arithmetic graph class and exposes the mechanism that spectrally permitted periods still need compatible firing multiplicities. The exact signed-kernel bijection is useful for computing attractors, and the odd-graph family gives an unbounded-odd-girth example of extinction in the presence of a permitted threshold eigenvalue, beyond the known spectral exclusion criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
