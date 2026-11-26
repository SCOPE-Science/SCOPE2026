# Independent mathematical audit

## correctness

PASS

In the six-dimensional even-subsets/complement symplectic module, matchings give 105 distinct Lagrangians; all 15 Lagrangians through a specified two-subset class are accounted for by matchings containing that pair. The seven affine plane-partition classes close as the nonzero part of a Lagrangian and have zero pairings. Their partition families recover the affine structure: after choosing an origin, choose the side of each partition containing it and thereby recover all affine linear coordinates up to affine change. The 30 structures exhaust the complement of the matchings among 135 Lagrangians. For every partition, I independently inventoried elements of each S8 cycle type in AGL(3,2), used the centralizer/coset formula on powers, and inverted the fixed numbers; all 22 rows of orbit_profiles.json and the displayed profiles agree. The matching counts independently follow by viewing a matching as an involution without fixed points commuting with Frobenius: pair equal-length cycles with an arbitrary alignment, or exchange an even-length cycle with itself by a half-turn. At (1,7), the fixed cosets number 2 and the remaining 28 form four 7-cycles; no matching is fixed. An odd-order permutation cannot swap complementary subsets, and the only invariant even subsets here are empty and full. Thus there is no nonzero rational 2-torsion despite the two stable subgroup schemes. Direct FLINT factorization confirms x^7+x+1 is irreducible over F5 and its product with x is squarefree; the smooth degree-eight hyperelliptic model has genus three and these eight finite branch points. The zeta function follows from two degree-one and four degree-seven places.

## originality

FAIL

Demonstrable equivalent coverage: the distinct indexed Cayley-octad Göpel classification (record 8a91037e03f9) gives the identical S8-set of 30 affine structures and tabulates its fixed cardinality on every conjugacy class of S8, alongside every matching fixed count. The change from a Cayley octad to a branch octad does not change this action. All cycle counts in the frozen table and the highlighted two-kernel/no-pairing descent then follow directly from those data; no within-day publication order is asserted. The additional rational-torsion observation is immediate from the same eight-label model, and the explicit equation is a routine realization of a prescribed branch type, not a distinct original arithmetic classification.

## value

FAIL

Descent of non-pairing kernels is a natural invariant, but every displayed exact arithmetic profile is a direct decoding of existing split fixed-count data. The only residual specialization is a genus-three equation exhibiting (1,7) and the immediate no-fixed-vector observation for that permutation. This is a routine prescribed factorization and fixed-subset check, not a further obstruction or motivated new exact invariant. No useful new claim survives narrowing the supplied result to what is not already in the table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
