# Complete finite-field commutator fibers of three-dimensional square-zero matrices

## Finding

Let \(q\) be any prime power, \(F=\mathbb F_q\), \(Z_q=\{A\in M_3(F):A^2=0\}\), and for each \(C\in M_3(F)\), put
\[
 f_q(C)=\#\{(A,B)\in Z_q^2:AB-BA=C\},\qquad
 N=(q^2+q+1)(q^2-1).
\]
Then \(|Z_q|=N+1\), and the complete pointwise fiber distribution is as follows.

1. At zero, \(f_q(0)=1+N(2q^2-q+1)\).
2. At every nonzero square-zero matrix \(C\), \(f_q(C)=2q^2(q-1)\). There are exactly \(N\) such targets.
3. In odd characteristic, the other targets with nonzero fiber are precisely the matrices similar over \(F\) to \(\operatorname{diag}(h,-h,0)\) with \(h\ne0\). Each has fiber \(2(q-1)\), and there are exactly \(|\operatorname{GL}_3(q)|/[2(q-1)^2]\) such target matrices.
4. In characteristic two, the other targets with nonzero fiber are precisely \(hP\), where \(h\in F^\times\) and \(P\) is an idempotent of rank two. Each has fiber \(q(q^2-1)\), and there are exactly \((q-1)q^2(q^2+q+1)\) such target matrices.

There are no other targets. In particular, the rank-two fibers have different characteristic-dependent sizes, even though each nonzero square-zero target has one uniform size. For \(q=2\), the fiber sizes are \(148\) at zero, \(8\) at each of the \(21\) nonzero square-zero targets, and \(6\) at each of \(28\) rank-two targets. Their weighted sum is \(22^2=484\).

## Assumptions and scope

The pair \((A,B)\) is ordered; no relation other than \(A^2=B^2=0\) is imposed. Matrices are actual \(3\)-by-\(3\) matrices over the finite field, not conjugacy classes. Both zero and nonzero factors are counted. Here \(\operatorname{GL}_3(q)\) is the group of invertible matrices, and \(F^\times\) is its coefficient field's multiplicative group. All characteristics, including two, are included. No assertion is made in higher matrix dimension.

## Proof

**Square-zero parametrization.** Every nonzero \(A\in Z_q\) has rank one, so write \(A=u\varphi\), where \(u\in F^3\setminus\{0\}\), \(\varphi\in(F^3)^*\setminus\{0\}\), and \(\varphi(u)=0\). There are \(q^2+q+1\) choices of the image line \(Fu\) and \(q^2-1\) nonzero functionals annihilating a fixed line once one representative \(u\) has been chosen. Thus there are \(N\) nonzero square-zero matrices. Write \(B=x\psi\) similarly, and set \(a=\varphi(x)\), \(b=\psi(u)\). Direct multiplication gives
\[
 [A,B]=a\,u\psi-b\,x\varphi. \tag{1}
\]
This representation also covers a zero factor by treating it separately.

**Zero fiber.** Fix nonzero \(A=u\varphi\). Both products vanish precisely when \(x\in\ker\varphi\) and \(\psi(u)=\psi(x)=0\). If \(Fx=Fu\), there are \(q^2-1\) nonzero possible functionals \(\psi\). The other \(q\) lines \(Fx\) inside the two-dimensional plane \(\ker\varphi\) each yield \(q-1\) choices of \(\psi\). Thus exactly \(2q^2-q-1\) nonzero \(B\) commute with \(A\); for square-zero rank-one factors, commuting with both products zero follows from the case analysis below. If \(a=b\ne0\), equation (1) has rank two, whereas if exactly one is nonzero it has rank one. Hence \([A,B]=0\) with nonzero factors forces \(a=b=0\), and conversely. Adding the \(2N+1\) ordered pairs with a zero factor yields \(f_q(0)=1+N(2q^2-q+1)\).

**Rank-one fibers.** If exactly one of \(a,b\) is nonzero, equation (1) is a nonzero square-zero matrix. Conversely, if \(ab\ne0\), the vectors \(u,x\) are independent (because \(\varphi(u)=0\) and \(\varphi(x)\ne0\)) and the functionals \(\psi,\varphi\) are independent (because \(\psi(x)=0\) and \(\psi(u)\ne0\)), so (1) has rank two. Fix \(C=e_1e_3^\top\). For \(AB=C\) and \(BA=0\), necessarily \(A=e_1(0,a,c)\) with \(a\in F^\times,c\in F\), and \(B=(d,a^{-1},0)^\top e_3^\top\) with \(d\in F\). This gives \(q^2(q-1)\) ordered pairs. The opposite case \(BA=-C\), \(AB=0\), gives an equal disjoint number by swapping factors and scaling. Every nonzero square-zero \(C\) is conjugate to \(e_1e_3^\top\), so its fiber has size \(2q^2(q-1)\).

**Rank-two targets.** Suppose \(ab=h\ne0\). Then \([A,B]u=hu\) and \([A,B]x=-hx\), and \(\operatorname{im}[A,B]=Fu\oplus Fx\). A third eigenvalue is zero because the commutator is of rank two. Consequently \(C=[A,B]\) is diagonalizable with eigenvalues \(h,-h,0\), even in characteristic two (where the first two values coincide). Conversely, fix such a matrix \(C\). Write \(E\) for the rank-two nonzero-eigenvalue space and \(K=\ker C\). Formula (1) forces both functionals to vanish on \(K\). A choice of ordered distinct eigenlines \((Fu,Fx)\) spanning \(E\) and compatible with the respective \(h,-h\) eigenvalues leaves exactly \(q-1\) choices for the scalar of \(A\); the scalar of \(B\) is forced by the required eigenvalue product. In odd characteristic there are precisely two ordered assignments of the two distinct nonzero eigenlines. In characteristic two there are \((q+1)q\) ordered decompositions of the two-dimensional eigenspace into distinct lines. This gives the rank-two fiber sizes \(2(q-1)\) and \(q(q+1)(q-1)=q(q^2-1)\), respectively.

**Number of rank-two targets.** In odd characteristic, each unordered pair \(\{h,-h\}\) with \(h\ne0\) defines one semisimple conjugacy class with centralizer \((F^\times)^3\). There are \((q-1)/2\) such classes, so the number of matrices is \(|\operatorname{GL}_3(q)|/[2(q-1)^2]\). In characteristic two a matrix with eigenvalues \(h,h,0\) is uniquely \(hP\) for a rank-two projection \(P\). Its image plane can be chosen in \(q^2+q+1\) ways, and there are \(q^2\) complementary kernel lines; there are \(q-1\) choices of \(h\). The counts above cover all cases and their fiber-weighted total equals \((N+1)^2\), confirming completeness.

## Verification

The standalone Python standard-library program `verify_squarezero.py` enumerates projectively normalized rank-one square-zero matrices, calculates every actual ordered commutator and counts its fiber, and independently tests rank, square-zero status and all listed multiplicities over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\). The extension field \(\mathbb F_4\) is implemented as \(\mathbb F_2[t]/(t^2+t+1)\). The observed total pair counts are \(484\), \(11025\), \(99856\), and \(555025\), respectively. The program returns `ALL_EXACT_CHECKS_PASSED 4`. Exhaustive finite checks support but do not replace the parameter-uniform proof.

## Relationship to prior work

Marcoux, Radjavi, and Zhang (arXiv:2402.15676v1) characterize the **set of images** of commutators of square-zero operators over a complex Hilbert space; their finite-dimensional results do not enumerate ordered finite-field fibers. Fulman and Guralnick enumerate **commuting pairs** of Lie-algebra elements over finite fields, but do not tabulate all prescribed **nonzero restricted commutator** fibers. Huang's mutually-annihilating matrix-pair enumeration concerns the zero-product locus \(AB=BA=0\), which only contributes part of this paper's zero fiber. Hoopes-Boyd provides existence of general matrix commutator representations for nilpotent targets, with no requirement that both factors square to zero. The new claim is the exact pointwise census in dimension three; it does not assert priority over prior general image characterizations.

## Limitations

The result concerns the restricted map on \(Z_q^2\) in matrix dimension exactly three, not the unrestricted commutator map or other dimensions. Equivalent older finite-semigroup or finite-matrix counting formulas might exist under different terminology and have not been ruled out by an exhaustive survey. The proof is self-contained, and the computational validation is finite, not independent mathematical certification.

## References

- L. W. Marcoux, H. Radjavi, and Y. Zhang, *On commutators of square-zero Hilbert space operators*, arXiv:2402.15676v1 (first public 2024-02-24), https://arxiv.org/abs/2402.15676 .
- J. Fulman and R. Guralnick, *Enumeration of Commuting Pairs in Lie Algebras over Finite Fields*, Annals of Combinatorics 22 (2018), 295–316; doi:10.1007/s00026-018-0390-4.
- Y. Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity*, arXiv:2110.15566v1 (2021).
- E. Hoopes-Boyd, *Representing nilpotent matrices as single commutators*, Communications in Algebra 49 (2021), 39–42; doi:10.1080/00927872.2020.1791900.
