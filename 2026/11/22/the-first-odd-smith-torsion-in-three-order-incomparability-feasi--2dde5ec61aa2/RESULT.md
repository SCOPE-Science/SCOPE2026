# The first odd Smith torsion in three-order incomparability feasibility

## Finding

Let \(\mathcal G_3\) be the Fraïssé limit of the class of all finite sets equipped with three independently specified strict linear orders \(<_1,<_2,<_3\). Define the derived strict partial order by \(x\prec y\) exactly when \(x<_i y\) in all three orders. Name an arbitrary set of \(n\) distinct parameters pointwise, irrespective of its three ranking patterns. Each complete nonalgebraic one-point type is an insertion-gap triple from \(\{0,\ldots,n\}^3\). Form the symmetric integer matrix \(K_n\) whose entry for two such types is one when distinct realizations \(x,y\) of those types can be chosen to be incomparable for \(\prec\), and zero otherwise.

For \(n=1,2,3\), the exact Smith normal forms over \(\mathbb Z\) are
\[
\begin{aligned}
\operatorname{SNF}(K_1)&=\operatorname{diag}(I_3,0_5),\\
\operatorname{SNF}(K_2)&=\operatorname{diag}(I_{15},2,0_{11}),\\
\operatorname{SNF}(K_3)&=\operatorname{diag}(I_{44},3,0_{19}).
\end{aligned}
\]
In particular, among all pointwise-named finite parameter sets, **odd-primary cokernel torsion first occurs at parameter size three**, where it is precisely one cyclic factor \(\mathbb Z/3\mathbb Z\). The rational ranks at sizes \(1,2,3\) are \(3,16,45\); at size three the rank drops from \(45\) to \(44\) in characteristic three. The empty parameter set gives \(K_0=(1)\) and has no torsion.

## Assumptions and scope

The orders are individually named, independent, and strict. The base consists of \(n\) distinct, individually named points; its induced three ranking permutations may be arbitrary. Only new points \(x,y\) distinct from each other and from the base are used. Matrix entries test the *existence* of an incomparable joint realization, not a count of realizations and not noncomparability in a single order. The exact integral classifications asserted here are for \(0\le n\le3\) only.

The fixed indexing of the types is lexicographic order on \(\{0,\ldots,n\}^3\), with gap \(0\) preceding all named points and gap \(n\) succeeding all named points in the corresponding order. As an isomorphism invariant the Smith form does not depend on the indexing or on the parameter ranking patterns.

## Proof

**Existence and criterion.** The class of finite structures with three arbitrary linear orders has amalgamation: extend each coordinate order separately. Its Fraïssé limit realizes every consistent finite insertion diagram. Thus all \((n+1)^3\) gap triples represent distinct complete nonalgebraic one-point types. For gap triples \(p,q\), the relative order of their realizations in coordinate \(i\) is forced to be \(x<_i y\) if \(p_i<q_i\), forced to be \(y<_i x\) if \(p_i>q_i\), and can be chosen either way when \(p_i=q_i\). The two new points can be incomparable for the intersection order exactly when there is an orientation with at least one positive and one negative coordinate. Such an orientation fails to exist precisely if \(p_i<q_i\) in all three coordinates, or if \(p_i>q_i\) in all three. Therefore
\[
(K_n)_{p,q}=1-\mathbf1_{\{p_i<q_i\ \forall i\}}-\mathbf1_{\{p_i>q_i\ \forall i\}}.
\]
In particular, if \(U_m\) denotes the strict upper-triangular all-ones matrix, \((U_m)_{ij}=\mathbf1_{i<j}\), and \(m=n+1\), then
\[
K_n=J_{m^3}-U_m^{\otimes3}-(U_m^{\mathsf T})^{\otimes3}.
\]
This also proves independence from the named base's three relative orderings.

**Exact finite integral reduction.** The accompanying `CERTIFICATE.json` contains complete, explicit elementary integer row and column operations on the matrices defined by the preceding equation, for all \(n\in\{1,2,3\}\). The operations are of five kinds: swapping two rows, swapping two columns, negating one row, adding an integer multiple of one row to another, and adding an integer multiple of one column to another. Every operation is unimodular over \(\mathbb Z\), and hence preserves the Smith invariant factors. The 25, 183, and 853 recorded operations transform the respective \(8\)-, \(27\)-, and \(64\)-square matrices *exactly*, with no division and no floating-point arithmetic, into the stated diagonal matrices. Their positive diagonal entries are already in divisibility order, so these diagonals are Smith normal forms. `VERIFY.py` reconstructs all three input matrices independently, checks each operation's admissibility, replays the complete transformations and checks every diagonal and off-diagonal entry. This is a finite exact constructive certificate, not extrapolation from sampled ranks.

The case \(n=0\) follows directly from the one-by-one formula. The absence of odd torsion for \(n<3\), and presence of a single factor three for \(n=3\), prove the claimed sharp onset without any assumption about larger parameter sets.

## Verification

From a directory containing `VERIFY.py` and `CERTIFICATE.json`, run `python3 VERIFY.py CERTIFICATE.json` with any standard Python 3 installation. No packages or external downloads are needed. The replay tests every off-diagonal entry after all 1,061 elementary operations and independently tests 4,889 feasibility entries from sign-choice enumeration. A separate exact Gaussian elimination checks matrix ranks modulo \(2\), \(3\), and \(5\). The expected final line is `CERTIFICATE_OK`. `GENERATE.py` independently regenerates the operation file by an exact integer-pivot algorithm; the delivered certificate itself, rather than the generator's output, is the object verified.

## Relationship to prior work

Cameron's 2002 homogeneous-permutation paper establishes the Fraïssé viewpoint for pairs of linear orders and explicitly discusses its higher-order generalization; it does not supply this integral pair-type matrix. Braunfeld's 2017 preprint and 2018 classification address homogeneous structures with three orders, providing the ambient homogeneous setting, not the integer invariant factors of this new matrix. Linman and Pinsker study the reduct structure of the generic two-order permutation. A previously recorded two-order incomparability-feasibility theorem has a parity-dependent two-primary Smith form; its matrix is two-dimensional and does not imply the three-dimensional factor of order three. A previously recorded type-spectrum theorem for unordered generic multiorders concerns an orbit quotient and counts one-types, not the fixed-order incomparable-pair relation. General Smith computations for partition-indexed matrices, such as those of Bessenrodt and Stanley, concern different matrices and do not imply these three explicit forms. Searches for the product-grid strict-dominance/incomparability Smith matrix did not produce an equivalent exact computation; absence of such a hit cannot establish absolute historical priority.

## Limitations

No formula for \(n\ge4\) is asserted. Finite exact certificates prove the specified small cases only. The matrices concern existential feasibility over a named base, not the adjacency matrix of a finite induced substructure of the Fraïssé limit. The original-status assessment is provisional: an equivalent statement under product-poset adjacency or integer matrix terminology might exist outside the inspected literature. No independent mathematical audit has been performed.

## References

1. P. J. Cameron, *Homogeneous Permutations*, Electronic Journal of Combinatorics 9(2), R2 (public 2002-10-31). https://doi.org/10.37236/1674 . Full paper: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v9i2r2/pdf
2. J. Linman and M. Pinsker, *Permutations on the random permutation* (preprint 2014-05-16). https://arxiv.org/abs/1405.4297
3. S. Braunfeld, *Homogeneous 3-dimensional permutation structures* (preprint 2017-10-14; journal 2018). https://arxiv.org/abs/1710.05138 ; https://doi.org/10.37236/7506
4. S. Braunfeld, *Infinite Limits of Finite-Dimensional Permutation Structures, and their Automorphism Groups* (2018 thesis), especially Chapter 6. https://arxiv.org/abs/1805.04219
5. C. Bessenrodt and R. P. Stanley, *Smith normal form of a multivariate matrix associated with partitions* (2013 preprint). https://arxiv.org/abs/1311.6123
