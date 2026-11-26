# Independent mathematical audit

## correctness

PASS

Independently checked cell and disjoint-pair occupancy and sign cancellation, giving the normalized simplex quadratic in RESULT.md lines 36–50. Expanding that quadratic into constant, row, column and zero-margin parts gives the first exact deficit. Interpolating from the critical quadratic to the full-permutation endpoint gives the second deficit via the permutation variance. Its equality conditions force a pairwise-intersecting support and constant permutation sum, hence a whole row or column of equal masses. At criticality the only constraint besides simplex membership is zero interaction. The upper proof uses the clique support reduction by strict convexity on a pair of conflicting cells and the uniform masses on a largest matching; the only q>1 cases are (2,2) and (3,3), and q=1 only at (4,4). The sphere gives the interval. Averaging both quadratic comparison inequalities over row/column signs and permutations removes off-diagonal terms and makes the diagonal constant, proving the claimed exact Banach–Mazur distance. The supplied checker and its verification description were inspected, not executed; the proofs do not depend on exhaustive experiments. 'Positive slice' means the nonnegative simplex intersection, as the stated extremizers can include zeros.

## originality

PASS

The full-rank fourth-moment and equality theorem has exact indexed overlap, not an independently new special case; the catalog date does not establish order. The supported distinction is the sharp fixed-rank family, in particular the codimension away from complete matchings, the transition n=3k−2 and the critical equality set. No inspected source supplies these or a theorem implying them by parameter substitution.

## value

PASS

Fixed cardinality is a natural regime between a single occupied cell and a signed permutation. The entire equality family changes structure at a specific density, where the minimizing set gains nontrivial row-column degrees of freedom. This gives usable optimum and distortion data, not just another calculation at an isolated size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
