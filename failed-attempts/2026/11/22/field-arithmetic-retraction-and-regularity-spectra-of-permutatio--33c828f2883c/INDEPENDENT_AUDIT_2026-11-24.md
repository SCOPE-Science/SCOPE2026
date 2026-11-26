# Independent mathematical audit

## correctness

PASS

Write A_{ij} for the coefficient in output row i of the image of basis vector j, and let sigma denote the successor on the basis indices. Preservation of mixed zero products forces at most one nonzero entry per row because squaring permutes the distinct output coordinates. Preservation of each square gives A_{sigma(i),sigma(j)}=A_{ij}^2. A nonzero row thus determines a whole output cycle, with one selected input cycle of length m dividing its length n, m starting positions, and a nonzero starting coefficient satisfying a^(2^n-1)=1. Distinct used columns have disjoint support, and any hit cycle contributes every one of its input columns, yielding linear dimension d(r). A is idempotent precisely when each hit input cycle, read as an output cycle, is fixed with the identity block; all remaining output rows choose zero or a selected divisor-length cycle with the stated phase weight. For regularity, following the row-selection arrows of A, B and A in ABA=A shows that every used input cycle needs an equal-length output witness, since the witness arrows can only decrease length by divisibility. Conversely choose one same-length output witness per used input cycle, use the inverse of that isomorphism to construct B on that input coordinate, and use zero in all other output components of B. This gives ABA=A. Inclusion–exclusion on missed equal-length cycles gives (2) independently at each length, with all-zero included. The line-by-line row derivation avoids switching the roles of source and target in the frozen prose. Independent literal sparse-row enumeration via the square equations, complete search for B, and formula comparisons passed seven cases including q=7, q=4, repeated and properly dividing lengths. Replay: python3 /workspace/repro/record1.py, output /workspace/repro/record1.out. The finite checks support, but do not prove, the unrestricted identities; the row argument proves them for the stated unweighted algebras.

## originality

FAIL

The principal regular-rank formula (2) is an exact specialization of the distinct indexed all-finite-G-set rank-census theorem 5c12e7f8630c, not merely a similar-looking count. An explicit action realizes all weights, zero components, composition and rank regrading (see broader_coverage and claim_vs_prior_implication). The relative chronological priority of the two same-day records is unresolved and is not used as a premise. This is demonstrable mathematical coverage of a substantive part of the frozen joint novelty claim. The mixed-length idempotent formula (1) was not established to be independently stated by the stronger regular-rank theorem; this is not a verdict that both formulas are false or that an earlier table states both verbatim.

## value

FAIL

The frozen contribution emphasizes a distinct simultaneous pair of spectra and the field-arithmetic regular jumps as a new invariant calculation. Its main regular result and those jumps can instead be read off a general exact census with the realized marks; the companion retraction formula is the identity-on-image count using already known phase weights, i.e. the earlier cycle-selection product with zero and phase options inserted. These are useful application formulas, but as submitted they do not establish a distinct substantive quantitative finding beyond the exact specialization and routine companion. No artificial narrowing or proposed correction is counted as a repaired finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
