# Integral homology of the six-point projective special-linear permutation complex

## Finding

Let \(P=\mathbb P^1(\mathbb F_5)=\{0,1,2,3,4,\infty\}\). Let \(G=\operatorname{PSL}_2(\mathbb F_5)\) act on \(P\) by fractional linear transformations. Form the permutation complex \(X(G)\): its \(j\)-cells are the injective ordered words of length \(j+1\) that occur as subsequences of the six-letter words \((g(0),g(1),g(2),g(3),g(4),g(\infty))\), for \(g\in G\). A face deletes one entry, with the induced word ordering; distinct words with the same underlying letter set remain distinct cells.

**Theorem.** The only nonzero reduced integral homology groups are
\[
\widetilde H_3(X(G);\mathbb Z)\cong\mathbb Z^{30},\qquad
\widetilde H_4(X(G);\mathbb Z)\cong\mathbb Z^5.
\]
Every reduced integral homology group is torsion-free. The complex is \(2\)-connected and is a pure five-dimensional Boolean regular cell complex, but is **not shellable**. A complete homotopy classification is **not asserted**.

## Assumptions and scope

The field has exactly five elements. The symbol \(\infty\) is encoded as label \(5\) in the accompanying checker. Two invertible matrices define the same projective action when they differ by a nonzero scalar. The acting group consists of the projective classes with square determinant, equivalently the projective classes of determinant-one matrices. It has exactly \(60\) distinct permutations in its natural six-point action. The result is for this specific six-point action and this specific ordered-subword complex; it is not a statement about arbitrary \(A_5\)-actions or all projective special-linear groups.

For \(k=1,\ldots,6\), let \(C_{k-1}\) denote the free integral group on the admitted words of length \(k\), and use the cellular differential
\[
\partial_{k-1}(v_0\cdots v_{k-1})
 =\sum_{i=0}^{k-1}(-1)^i v_0\cdots\widehat{v_i}\cdots v_{k-1}.
\]
The augmented degree-zero differential is standard. No simplicial identification of differently ordered words is made.

## Proof

**1. Exhaustive finite cell description.** Enumerate all \(625\) matrices over \(\mathbb F_5\), retain determinant \(1\) (or, independently, nonzero square determinant), evaluate their actions on all six points and deduplicate projective actions. Both constructions give the same set of \(60\) permutations. Generate all nonempty ordered subsequences of those permutations. The exact cell numbers in dimensions \(0,1,2,3,4,5\) are, respectively,
\[
(6,30,120,360,300,60).
\]
In particular every injective word of length at most four occurs. The signed cellular boundary squares to zero; the checker verifies this in every degree using integer arithmetic.

**2. Integral cancellation lemma.** Suppose a differential between free integral chain groups has basis generators \(x\) and \(y\) in consecutive degrees with coefficient \(\varepsilon=\pm1\) of \(y\) in \(\partial x\). For every other generator \(z\) in the degree of \(x\), replace \(z\) by
\[
z-\varepsilon\langle y,\partial z\rangle x.
\]
This is an integral unimodular basis change. In the resulting basis the \(y\)-coefficient of all other boundaries is zero. Replace the lower generator \(y\) by \(\varepsilon\partial x\), an integral unimodular change that exhibits a contractible two-generator direct summand with differential a unit. Removing that summand preserves integral homology. If higher differentials are zero, the operation requires no changes to higher matrices; the remaining lower differentials are inherited unchanged. Thus processing dimensions from highest to lowest, after higher boundaries have been eliminated, is legitimate.

**3. Exhaustive integral certificate.** The attached `certificate.py` performs only integer additions, multiplications and divisions by units in its cancellation stage. At each degree it deterministically selects a unit coefficient and performs the stated operations. All transformed boundaries become zero, and the exact numbers of unit cancellations from the word lengths \(6,5,4,3,2\) are
\[
(60,235,95,25,5).
\]
The remaining zero-differential chain groups, from lengths \(1\) through \(6\), have ranks
\[
(1,0,0,30,5,0).
\]
Because every cancellation is unimodular, there can be no unobserved finite torsion. Subtracting the ordinary degree-zero class gives the asserted reduced integral homology. The largest absolute coefficient observed during the integer operations is \(2\); no modular computation is used to infer integral torsion-freeness.

**4. Connectivity and shellability.** Since all ordered words of length at most four occur, the three-skeleton agrees with that of the full six-letter injective-word complex. The latter is homotopy equivalent to a wedge of five-spheres by the classical Björner–Wachs theorem. Cellular approximation therefore makes its three-skeleton two-connected; adjoining only four- and five-cells cannot alter \(\pi_1\) or \(\pi_2\). Hence \(X(G)\) is two-connected. It is pure of dimension five because every admitted word extends to a generating six-letter permutation. A pure shellable Boolean cell complex has reduced homology concentrated in its top dimension, contrary to the nonzero third and fourth homology here. Hence \(X(G)\) is not shellable.

## Verification

Run `python3 certificate.py` using Python 3.8 or later, without third-party packages. Expected final line: `PSL5_WORD_INTEGRAL_CERTIFICATE_PASS`. The script checks independently determinant-one versus square-determinant action enumeration, bijectivity, face counts, integral \(\partial^2=0\), every integral unit pivot, absence of residual differentials, remaining chain ranks, Euler characteristic, and modular ranks at primes \(2,3,5,7\). The complete recorded output is `certificate_output.txt`.

The modular comparisons are secondary cross-checks: **only** the integral unimodular cancellations prove torsion-freeness. There are \(876\) nonempty cells; all are considered. The chain calculation is a finite exhaustive proof, not an extrapolation to larger fields.

## Relationship to prior work

Chachólski, Levi and Meshulam (2019, arXiv:1908.03394) define permutation complexes, give the signed ordered-word cellular chain model, and classify complexes generated by two permutations; their stable realization theorem does not compute this sixty-generator projective action. Elizalde, Hanlon and Hersh (first posted October 5, 2026, arXiv:2610.07303) establish shellability and homology bases for classes defined by pattern avoidance; the present complex is determined by a proper permutation subgroup, has a full three-skeleton but not the full five-skeleton, and is non-shellable. Govc (first posted November 8, 2026, arXiv:2611.11362, primary MSC \(55U10\)) establishes free fundamental groups for all permutation complexes; that result does not determine the third and fourth integral homology of this example. Searches for this particular projective-line action and its exceptional \(A_5\subset A_6\) realization found no matching classification. No priority claim beyond the inspected evidence is certified.

## Limitations

The result does not establish a wedge-of-spheres homotopy equivalence or the induced integral automorphism representations. In particular, an acyclic *algebraic chain* cancellation need not be an acyclic *discrete-Morse* matching on the face poset. It provides the exact integral homology and connectivity only. A previously unindexed or differently named computation could exist; searches and comparisons cannot certify uniqueness.

## References

- W. Chachólski, R. Levi and R. Meshulam, *On the topology of complexes of injective words*, arXiv:1908.03394 (2019), https://arxiv.org/abs/1908.03394.
- S. Elizalde, P. Hanlon and P. Hersh, *Complexes of pattern-avoiding injective words*, arXiv:2610.07303v1 (2026-10-05), https://arxiv.org/html/2610.07303v1.
- D. Govc, *Fundamental Groups of Permutation Complexes*, arXiv:2611.11362v1 (2026-11-08), https://arxiv.org/html/2611.11362v1.
