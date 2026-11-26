# Independent mathematical audit

## correctness

PASS

The original complement and block arguments are correct: every possible successful pair leaves at most two vertices, forcing the large block and triangles for four classes. At three classes the feasible omitted one-block sizes give profiles (1,1,n-2), (1,2,n-3), and (2,2,n-4), with an n=6 perfect matching counted three times and thus a subtraction of twice its count. The genuine repaired claim concerns nondetermination and minimality rather than these formulas. The size bound from distinct witnesses excludes omissions of size at least three for n=5. Direct pair tests give six feasible pairs in both P5 and K2,3, but a triangle only in the former. A four-block partition at order five is precisely one doubleton with the other three vertices singleton, and the three partner unions require the three corresponding omitted pairs; K2,3 also explicitly has a valid three-block partition. On three vertices all singleton classes can partner; the exhaustive six connected isomorphism types on four vertices give (number of feasible pairs, C_s) equal to (0,3), (2,4), or (4,4); the polynomial therefore still determines C_s. The original six-vertex pair has no feasible triple, with identical omitted-set counts but distinct spectra; the witness and partition computations independently match all stated coefficients.

## originality

PASS

The repaired statement is the first connected obstruction to recovering the coalition number from the size-only super-domination polynomial, with an additional six-vertex obstruction even to recovering the three-block coefficient. The earlier enumerator results are credited and not claimed afresh. Their dependence on more than |E(H)| does not by itself exhibit a realizable collision, let alone its first order; matching source checks did not establish an earlier exact collision and cutoff.

## value

PASS

A natural inverse question is whether the previously computed set enumerator already determines coalition data without tracking vertex labels. Finding the smallest connected obstruction makes the precise loss of information usable, and the six-vertex pair shows loss not only of the maximum but also of the three-block frequency. This is a realizability counterexample and a motivated exact cutoff, not a small-table recomputation of the prior general census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
