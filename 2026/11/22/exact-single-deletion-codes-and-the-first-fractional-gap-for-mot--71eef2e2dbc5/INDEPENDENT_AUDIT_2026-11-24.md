# Independent mathematical audit

## correctness

PASS

The frozen text fails as written when it says the relaxation is integral through length six. At length four take FUFD, FUDF, UFDF: the three deletion shadows have pairwise intersections but no triple intersection. Half weight on each and zero elsewhere is feasible, and the tight pair constraints uniquely determine the three positive coordinates on the face fixing all others to zero. This gives a fractional vertex despite equality of the optimal objectives. The corrected Finding asserts zero objective gap through six, not polyhedral integrality, and gives the explicit counterexample. The table and first strict objective gap are correct. A received word identifies its source layer by max(#U,#D), even when the output is not an excursion. I independently generated the layers by choosing nonflat positions and balanced up positions, reconstructed the deletion incidence, and used exact fractions to check every capacity and cover constraint and matching objective. Each disjoint-shadow witness attains the floor of the layer's bound. An independent ordered enumeration of compatible sets of that known optimal size counted every optimizer once, without relying on either frozen graph search. It confirmed the entire table; at n=7 the layer capacities are 1,5,14,5, values 1,5,217/15,5, and counts 1,9,11,1440. The repaired text also correctly describes the pruned Bron–Kerbosch search as retaining every maximum clique, not necessarily visiting every smaller maximal clique. No certificate data or executable changes are needed.

## originality

PASS

The supported distinct claim is the full Motzkin single-deletion table, including optimum codebook counts and the first strict objective gap. Path enumeration and the general deletion-shadow LP are prior, and the no-flat even layers reduce to Dyck instances. The repair preserves the novel aggregate table and makes no priority claim for the small counterexample used to clarify polyhedral terminology.

## value

PASS

Classical Motzkin paths with an unmarked deletion form a natural constrained channel. The cutoff is meaningful because it pinpoints the first strict loss of the basic fractional bound, while showing its floor is still exact. Moreover, the repaired statement separates the geometry of the relaxation from its objective: fractional vertices occur earlier than the first strict objective gap. Exact populations of labeled maximum codebooks add a reproducible design benchmark not supplied by the capacity alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
