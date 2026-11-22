# Self-review — Right-polynomial maps on every finite radical-square-zero quiver algebra

## Correctness — PASS

For a loop-permitting, parallel-arrow-permitting finite quiver with vertex idempotents and square-zero arrow ideal, multiplication by a basis idempotent or arrow gives an exact divided-difference evaluation formula. The equality cases at arrow endpoints force the first derivative at every emitting vertex; all other data are just field values. The Chinese remainder theorem for the squarefree polynomial \(H(X)=X^q-X\) gives independent Hermite interpolation of values and first derivatives, proving both the kernel and the full function count for every prime power. On each diagonal fiber the map is an affine arrow-coordinate map, with determinant the product of edge divided differences. Permuting the vertex field values forces every unequal-input multiplier nonzero; all remaining nonzero conditions are exactly the outgoing-source first derivatives. The resulting formula is \((q!)^v(q-1)^{qr}q^{qm}\). For each nonloop arrow \(i\to j\), composing \(G(x)=e_i x\) with \(F(x)=x^2\) violates the divided-difference rule when the two endpoint coordinates are 0 and 1. When all arrows are loops, the algebra is commutative and polynomial maps are substitution-closed. No unproved induction or unbounded search is used.

The standalone finite-field checker calculates actual evaluation-vector ranks and exhaustive bijective function counts (nine small prime-field models), ending `RIGHT_POLYNOMIAL_QUIVER_CHECKS_OK`. These checks only corroborate, not prove, the all-quiver statement.

## Originality — PASS, with bounded priority risk

Werner's *Some results on null ideals of finite rings* (arXiv:2608.25853, first public 2026-08-26) proves the general implication \(J^3=0\) implies that the null ideal is two-sided. The present \(J^2=0\) case is therefore already covered **for two-sidedness alone**; the new claim does not assert novelty of that corollary. The source does not state the exact vertex-and-arrow kernel, arbitrary-quiver counts or composition criterion. Frisch's *Polynomial functions on upper triangular matrix algebras* (arXiv:1605.06027) studies the unrestricted full triangular-matrix algebra and provides earlier path/divided-difference technology, but does not state the full family, especially arbitrary quivers with directed cycles, parallel arrows and loops, nor the two cardinality formulas. Al-Maktry–El-Deken (arXiv:2409.10208) analyze central square-zero extensions; these cover special commutative settings but not noncentral arrow Peirce bimodules. The classification is not simply the previous two-sidedness theorem restated: its source-versus-target dependence is needed to count maps and to prove the sharp composition boundary.

Literal and equivalent-formulation queries covered null polynomials, right-polynomial functions, square-zero quiver algebras, Hermite derivatives, bijections and polynomial-permutation functions. No encompassing pre-existing exact all-quiver classification was identified. Priority is not certified against inaccessible, unindexed or alternate terminology in prior literature. Independent specialist comparison is outstanding.

## Mathematical value — PASS

This addresses the naturally motivated full function-enumeration problem in the class where the recent general null-ideal theorem guarantees ideality, but does not provide representatives or counts. The answer captures the precise orientation-sensitive parameter of vertices emitting arrows, gives exact bijection counts for arbitrary finite fields, and isolates an intrinsic obstruction to composition for every noncommutative member. It includes all finite directed multiquivers, not an arbitrary finite slice or a recomputation of a known table. The exact form is usable for counting the right-polynomial image of \(A[X]\), benchmarking noncommutative polynomial permutation problems, and distinguishing source/sink configurations.

## Limitations and closest sources

The proof does not treat quiver relations beyond square-zero radical, nor claim that bijective polynomial maps form a group in the noncommutative cases. Earlier special cases follow from central-dual-number and upper triangular theories, and the two-sidedness property follows from Werner's broader theorem. The novel classification is the simultaneous all-quiver null kernel, counts, and composition threshold. The direct checker enumerates only selected finite prime-field models; generality rests on the explicit proof.

Self-review: passed. Independent audit: not yet performed.
