# Independent mathematical audit

## correctness

PASS

An independent rank argument verifies the joint law. In decreasing score order consider only the cells incident with the selected k rows or selected k columns of a specified matching M. There are k(r+c−k) such cells, with uniform relative rank. The first must be in M: otherwise it blocks one of the desired cells. Conditional on which selected cell is first, that cell is already a mutual maximum and the relative order of all other entries in the union stays uniform. The new constrained union for the remaining matching is contained in that remainder; it excludes the first cell but retains relevant cross-cells. Induction gives probability 1/(r+c−k) times the (k−1)-cell inclusion probability, yielding 1/(r+c−1) falling k. Multiplying by (r falling k)(c falling k) gives the factorial moments of Hypergeom(r+c−1,r,c); finite support determines the PMF. The global maximum guarantees K≥1. Permuting rows and columns acts transitively on matchings of fixed size; dividing the PMF by their number gives exactly 1/[c(k−1)! binom(r+c−1,c)] per labelled full set. The hypergeometric variance is as stated, with the separate singleton case; one-row or one-column boards have K=1. This checks frozen RESULT.md lines 5–30 and 38–83. VERIFICATION.md and verify_rook_maxima.py were inspected, not executed.

## originality

FAIL

The distinct indexed two-copy reciprocal-minimum finding already gives the exact all-order inclusion integral on square boards at its identical-copy endpoint. That integral completely determines the square unmarked law. The advertised rectangular and labelled-set refinements do not leave a supported distinct mathematical result at the standard of more than routine implication: the same exact integral changes only by replacing its external-competitor count, and the labelled distribution follows from exchangeability. This is a coverage judgment, not a claim of publication priority between same-day records or a claim that the older primary literature has been shown to state the rectangular PMF.

## value

FAIL

The count and full location law answer a natural question and are convenient to use. However the stated contribution, compared with the inspected exact all-matching integral, reduces to a routine change in the competitor count, elementary integration and hypergeometric identification; conditional uniformity is forced by symmetry. No independently useful nonmechanical remainder is established as submitted. This is not a rejection on grounds of small size or mathematical incorrectness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
