# Independent mathematical audit

## correctness

PASS

For the actual fixed-basis hypothesis on both C and D, the disjoint coordinate embeddings V,J give W=VC+JD with W*W=I and V*W=C. For column j the first possible index of W is 2 max(0,j−r)+2r+3>j; V advances support as well. Iteration into the coordinate tails proves purity, not just absence of eigenvectors. V has an infinite-dimensional orthogonal complement, and W does too: y↦−VD_*y+JC*y is isometric by D_*²+CC*=I and orthogonal to W by DC*=C*D_*, which follows by polynomial approximation of the square root. For the commutator step, the two-copy Y commutes with Z and satisfies Y²=I+4Z², so the block Q is idempotent and [P,Q] is the symmetric off-diagonal block with entries Z. Diagonalizing that block, alternating signs on wandering levels, and using Wold multiplicity give the asserted isometries and their scalar multiples as idempotent commutators; adjoint reverses the commutator order. Scaling then gives AB=T and AA*=B*B=sI, hence both norms are √s. This also handles the singular-defect boundary, with the zero case trivial. RESULT.md lines 18–36 supply the identities; CHECK.py and VERIFICATION.md were inspected, not executed. The reported 80 finite checks do not certify purity or endpoint attainment in infinite dimension.

## originality

PASS

The distinct part supported here is exact endpoint attainment for the stated class, not existence of two factors, the Wold commutator lemma, or the value of the infimum of admissible normalization constants. The closest primary theorem has the same factor identities with a strict normalization inequality. No materially equivalent distinct indexed result or covering prior endpoint theorem was found in the evidence inspected.

## value

PASS

Exact attainment is a meaningful distinction in an infinite-dimensional factorization problem already known with arbitrary positive slack. The basis-support construction handles familiar classes such as weighted shifts and diagonals with singular or nonclosed-range exact defects. It answers a concrete endpoint question in those cases, without suggesting that the propagation condition is necessary or that general factor existence is new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
