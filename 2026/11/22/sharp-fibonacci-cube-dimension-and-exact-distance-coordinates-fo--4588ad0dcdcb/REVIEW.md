# Independent mathematical audit

## correctness

PASS

The original paper's monomer/dimer definition agrees with the frozen even-run parsing and legal moves. Each move changes one effective level by one or toggles just one dimer start. Dissolve source-only dimers, keep the common dimers (their endpoints already have target effective levels), adjust the remaining monomers monotonically, and insert target-only dimers. Target dimers are disjoint and each insertion is then legal, so the coordinate distance is attained. A list of moves and the label can be produced in O(kn) time; this does not count printing a full word per move. Threshold bits turn level differences into Hamming distance. For k=2r, consecutive bits inside a site block are a low test h<j<=r and a high test h>=j'>r, so cannot both be one. A dimer bit of one forces both neighbouring low tests to vanish. This permits precisely kn−1 positions, including at n=1. In an isometric hypercube encoding the metric cross-sums of two edges differ iff their bit directions coincide. The frozen witnesses use all kn−1 directions, hence require that many in any isometric encoding; every Fibonacci cube has its Hamming metric by dropping nonshared ones and then adding target ones. Distance one also proves that the image is induced.

## originality

PASS

The explicit even-alphabet construction at the hypercube lower bound is distinct from the longer embedding in the original paper, the general semicube characterization, and results on similarly named but nonidentical cubes. The published problem asks about arbitrary subgraph embeddings, so the shorter construction answers the reduction question on this family, but exact minimality is only among isometric embeddings.

## value

PASS

The construction reduces the dimension in an explicit published problem by (k−2)n and meets a metric lower bound for an infinite natural subfamily. The level/dimer coordinates additionally give exact distances and a constructive geodesic, not just an improved numerical bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
