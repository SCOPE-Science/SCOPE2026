# Independent mathematical audit

## correctness

PASS

Stable 3-vertex cells have common within-cell outdegree one and are directed triangles; size-two stable cells are impossible. Between two triples the directed 3×3 cross-adjacency has constant row/column sum k, so k∈{0,3} is uniform and k∈{1,2} gives exactly a perfect matching or complement. Every automorphism preserves refinement cells and rotates each triangle by t_P∈Z/3; matching preservation imposes t_Q=sgn(π_PQ)t_P. Balanced signed components admit one free C3 rotation; a negative cycle gives t=−t, hence t=0 modulo 3. All compatible rotations preserve every arc; this proves full group and orbit partition, not just necessary conditions. Unbalanced signed cycle needs >=3 triple blocks => >=9 vertices. Independent reconstruction of explicit three-triangle witness verified degree partition 3,3,3/4,4,4/5,5,5 and unique automorphism among 27 possible classwise rotations; appending dominating singleton vertices maintains a negative cycle and rigid property. Inspected full verify.py with 2744 pattern families (2310 in-scope), but finite checks only corroborate the unbounded symbolic theorem.

## originality

PASS

General undirected graph refinability and C²-identifiability literature develops the concept but does not give a tournament-specific matching-sign holonomy classification or full automorphism-group formula for all small stable cells. A published rooted tournament 8-vertex obstruction has stable classes 1+7, so it lies outside this size<=3 condition and cannot imply its nine-vertex cutoff. The parity/holonomy logic is an original-looking structural specialization, with unindexed tournament-equitable-partition precedent still a risk.

## value

PASS

The theorem computes full automorphism groups and orbits from an elementary signed auxiliary graph rather than exhaustive permutations. It explains exact obstruction to refinability for unbounded tournament sizes with naturally small equitable color cells and gives a sharp threshold and rigid counterexample family; it is a structural classification, not just a finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
