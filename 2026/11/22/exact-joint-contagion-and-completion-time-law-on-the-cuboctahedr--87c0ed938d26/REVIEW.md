# Independent mathematical audit

## correctness

PASS

The frozen table and polynomial are correct, but its conditional-law quantifier included p=0, where the conditioning event has probability zero. The complete corrected RESULT.md restricts that law to 0<p<=1 (the all-active set alone has positive mass p^12), gives its formula, and treats T=infinity at p=0. At p=1 the corrected formula gives the point mass at zero. For degree four, inactive vertices survive exactly when they retain two inactive neighbors; a cycle survives forever and every nonempty forest loses at least one vertex each round. An induced line-graph forest requires cube-edge degrees at most two (a degree-three star creates a triangle) and no cube cycle, hence a linear forest. Seven selected edges force a single spanning path; its inactive component of order seven prunes through 7,5,3,1,0. In general a longest cube path with L edges takes ceil(L/2) rounds, with zero rounds for the empty complement. The independent bounded replay `python3 /workspace/evidence/cuboctahedral_census.py` checked all 4096 labelled seeds, the 13 nonzero (k,t) entries, the separate linear-forest marginals, full five-seed profiles and all three symmetry orbits. Independently expanding the resulting Bernstein-form sum gives the stated monomials; the sum is 1572, so p=1/2 gives 393/1024. Supplied scripts were read, not executed. This is exact for the specified graph and synchronous update only.

## originality

PASS

Pass only the surviving labelled seed-size and synchronous completion-time census for this network and its probability law. The corrected file credits the same-day decycling result for the equivalent minimum-set characterization and three orbits; that overlap neither implies publication order nor supplies timing for larger seed budgets.

## value

PASS

The strict-majority threshold on a canonical four-regular polyhedral graph is natural. The complete labelled joint table distinguishes exact success probabilities and speed at each possible budget, including 300 successful six-sets split between two and three rounds and no one-round six-set. Neither the known optimal-set count nor the static forest criterion supplies those distinctions without a new census. The result is useful as a finite benchmark without a general-graph or large-size claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
