# Independent mathematical audit

## correctness

PASS

The proof works for every finite preorder and arbitrary R, including empty rows and equivalent but distinct worlds. Replacing a row by its upward closure leaves containment in every upset unchanged. For each w, define I_w(A) as the union of the future saturated rows contained in A. An evaluation of the two premises at w says I_w(A) union I_w(B) is contained in the consequent upset C. The conclusion says I_w(A union B) is contained in C, so a strict inequality of those unions gives a countervaluation by taking C to be the smaller union; reflexivity makes it a counterexample to the outer intuitionistic implication. Conversely equality at every world ensures that implication. Union preservation on finite W gives the principal-upset decomposition of I_w, and applying it to H_x=I_w(H_x) for w<=x gives PC. Conversely each point of I_w(A) belongs by PC to I_w(up v) for some v in A, and monotonicity supplies the reverse inclusion, hence union preservation. The quantified relation translation and O(n^5) time/O(n^2) space are valid by precomputing row inclusion and testing witness pairs. A nonempty finite down-directed row has a least element up to preorder equivalence and hence satisfies PC with y=x; empty rows cause no obligation. In the three-world fork, each point of the bottom row is covered by its own available singleton leaf row, and both leaf rows satisfy PC themselves. The bottom row is not down-directed. On two comparable worlds every row is down-directed in the pairwise sense used in the result, while on a two-point antichain the only nondirected row is the full pair and its source has no future world besides itself, so PC fails there. The frozen verification files were inspected, not executed; their n<=3 census is corroborative, not the basis for the theorem.

## originality

FAIL

A distinct indexed Resultary finding states an equivalent finite-frame condition under exactly the same semantics and has a sharper decision bound. The equivalence is mathematical, not inferred from title, date or keywords. The overlapping item's November 8 UTC record date is later than the frozen item's October 13 UTC record date; the comparison establishes current equivalent coverage, not who obtained it first or that the November item preceded the frozen work. The original logic paper alone would not justify this failure.

## value

PASS

An exact relational test for a natural axiom eliminates quantification over persistent valuations on arbitrary finite frames and supplies a meaningful boundary relative to the strictly stronger directedness assumption. The smallest separating fork helps exhibit that boundary. The criterion has structural and algorithmic value; this is separate from the demonstrated equivalent coverage, and no value is attributed to a claim that O(n^5) is optimal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
