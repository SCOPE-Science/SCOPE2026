# Independent mathematical audit

## correctness

PASS

The three binary forms have no base point (at u²+v²=0 the first is −2u⁷). On Y≠0 the coordinates are f(t) and t⁵. A nontrivial fifth-root coincidence requires a root of the stated cubic T_a in w=t², after discarding zero and the two poles. The difference identity follows by expanding (w³−1)(aw+1)−(a³w³−1)(w+1) and using a⁵=1. It is not identically zero; hence the map is birational, and pullback of a line gives degree seven. Independent exact reproduction used polynomial discriminants and Sylvester resultants, then computed each norm as Res_q(Φ₅(q), g(q) mod Φ₅(q)); it gave four discriminant norms 674041 and six pair-resultant norms 2000. Replay: python3 check_septic_independent.py with SymPy. The 24 oriented parameter coincidences count exactly 12 distinct images: a triple would make two distinct cubics share a w, and no exceptional parameter shares any of these fibers. Since t⁵ is étale there, each simple zero of the difference gives distinct branch tangents. At P the only parameters are ±i, Y/X has simple zero on each branch and the ratio Z/Y limits to ±i. At t=0 the function of w=(t²) giving X/Y has derivative 1 in w, so the local coordinates are exactly (t²,t⁵), the A₄ cusp. At infinity X/Z has order one in u/v; away from these parameters t⁵ has nonzero derivative. The genus sum 13+2=15 checks exhaustion and Plücker gives 42−26−5=11. An independent cross-product computation gave primitive Gauss coordinates of degrees 7, 11, 6 (after canceling t); homogenization has no base point at infinity and agrees with the class via characteristic-zero biduality. This establishes the stated complex curve result, not other septics or behavior in positive characteristic. The supplied script was inspected, not executed.

## originality

FAIL

The distinct indexed record 44854ac77ae1 already treats precisely this parametrization over Q and proves the twelve additional ordinary nodes, the distinguished node, and the sole (2,5) cusp; its proof works in characteristic zero and has stronger arithmetic and good-reduction information. Over C the local formula in its Proof §3 gives the A₄ equation by an invertible target-coordinate change. The dual degree, though not stated there, follows immediately by the standard Plücker class formula from the established degree and local types. This is actual equivalent coverage, not inferred priority from equal dates. The author's source alone does not cover the basket and misdescribes P as smooth, but the separate indexed proof already gives the correct local description. The frozen cyclotomic calculation provides another certificate for the same classification, not a surviving separate finding as stated.

## value

FAIL

The septic is a well-motivated object and its analytic basket is worth knowing, particularly because the original source misidentifies P. As a separate narrow invariant finding here, however, the correct local types and exhaustive basket are already covered by the exact-curve proof, and the remaining dual number is just one standard substitution. The cyclotomic norms are useful for checking an alternative proof but are not shown to supply an independent geometric or arithmetic result in this claim. The exact numerical computation therefore does not leave a substantive standalone contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
