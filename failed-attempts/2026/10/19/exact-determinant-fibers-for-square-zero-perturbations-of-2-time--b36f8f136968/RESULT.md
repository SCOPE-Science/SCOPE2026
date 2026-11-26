# Exact determinant fibers for square-zero perturbations of \(2\times2\) finite-field matrices

## Finding
Let \(q\) be any prime power and \(A\in M_2(\mathbb F_q)\). Write \(e(A)\) for the number of \(A\)-invariant lines in the projective line \(\mathbb P^1(\mathbb F_q)\). Necessarily \(e(A)\in\{0,1,2,q+1\}\), with the last possibility exactly for scalar matrices. For every \(z\in\mathbb F_q\), let
\[
F_A(z)=\#\{N\in M_2(\mathbb F_q):N^2=0,\ \det(A+N)=z\}.
\]
Then the **complete determinant-fiber distribution** is
\[
\boxed{F_A(z)=\begin{cases}1+e(A)(q-1),&z=\det A,\\q+1-e(A),&z\ne\det A.\end{cases}}
\]
In particular, the total number of square-zero matrices is \(q^2\), and the fiber law depends on the similarity type only through \(e(A)\) and \(\det A\).

Let \(C(A)\) count ordered pairs \((D,N)\) satisfying \(A=D+N\), \(N^2=0\), and \(D\) diagonalizable **over \(\mathbb F_q\)**. Then:

* If \(q\) is even, \(C(A)=1\) for \(\operatorname{tr}A=0\), and \(C(A)=q(q+1)/2\) otherwise.
* If \(q\) is odd, \(C(A)=1\) for scalar \(A\); \(C(A)=q(q-1)/2+1\) for nonscalar matrices with a repeated rational eigenvalue; \(C(A)=(q^2+1)/2\) for matrices with two distinct rational eigenvalues; and \(C(A)=(q^2-1)/2\) for matrices with irreducible quadratic characteristic polynomial.

All four odd-characteristic cases are exhaustive and mutually exclusive. In particular every such matrix admits a decomposition, but the theorem determines **its exact multiplicity**, not merely existence.

## Assumptions and scope
The coefficient field is an arbitrary finite field \(\mathbb F_q\), including prime-power extensions and characteristic two. Matrices have order exactly two. The zero matrix \(N=0\) is included among square-zero perturbations. Each ordered pair is counted once: selecting \(N\) determines \(D=A-N\). Diagonalizability is over the given ground field, not just its algebraic closure. No restriction on trace, determinant, invertibility, or similarity class is imposed.

## Proof
**1. All square-zero perturbations and their determinant shifts.** A nonzero \(2\times2\) square-zero matrix has rank one and its image equals its kernel, a unique line \(L\) in \(\mathbb F_q^2\). Conversely, for any fixed line \(L=\mathbb F_q u\), the maps \(N=u\varphi\) with \(\varphi(u)=0\) form a one-dimensional vector space; it has \(q-1\) nonzero square-zero matrices. Different lines give disjoint nonzero families, and hence there are \(1+(q+1)(q-1)=q^2\) square-zero matrices in all.

For every such \(N\), the determinant identity in order two and \(\det N=\operatorname{tr}N=0\) yield
\[
\det(A+N)=\det A+\operatorname{tr}(\operatorname{adj}(A)N)
=\det A-\operatorname{tr}(AN)
=\det A-\varphi(Au).
\]
This formula remains valid in characteristic two, where the last subtraction coincides with addition. The linear functional \(\varphi\mapsto\varphi(Au)\) on the one-dimensional annihilator of \(u\) is identically zero precisely when \(Au\in L\), i.e. when \(L\) is invariant under \(A\). Thus for each of the \(e(A)\) invariant lines, all \(q-1\) nonzero perturbations keep the determinant fixed. For each of the other \(q+1-e(A)\) lines, the \(q-1\) perturbations yield each nonzero determinant shift exactly once. Adding \(N=0\) proves the boxed fiber formula, including both boundary cases \(e(A)=q+1\) and \(e(A)=0\).

**2. Characteristic two.** Put \(s=\operatorname{tr}A\) and \(d=\det A\). Every square-zero perturbation preserves \(s\). If \(s=0\), the characteristic polynomial of \(A-N\) is \(T^2+\det(A-N)\). The squaring map is a bijection of \(\mathbb F_q\), so this polynomial has one repeated root. A diagonalizable \(2\times2\) matrix with that characteristic polynomial must be scalar. There is exactly one possible scalar \(D=cI\), where \(c^2=d\); the Cayley–Hamilton identity \(A^2+dI=0\) shows \((A-cI)^2=0\). Therefore \(C(A)=1\).

If \(s\ne0\), the characteristic polynomial \(T^2+sT+z\) is separable for every \(z\). Such a matrix is diagonalizable exactly when the polynomial has its two roots in \(\mathbb F_q\). The admissible determinant set \(S_s=\{r(s-r):r\in\mathbb F_q\}\) has \(q/2\) elements, because \(r\mapsto s-r\) partitions the field into pairs with distinct members. Since \(s\ne0\), the original matrix has either zero or two rational invariant lines, and \(d\in S_s\) exactly in the latter case. If \(e(A)=0\), the sum of the determinant fibers over \(S_s\) is \((q/2)(q+1)\). If \(e(A)=2\), that sum is \((2q-1)+(q/2-1)(q-1)=q(q+1)/2\). This proves the even-characteristic formula.

**3. Odd characteristic.** Again put \(s=\operatorname{tr}A\). The characteristic polynomial of \(D=A-N\) has discriminant \(s^2-4z\) when \(z=\det D\). Exactly \((q-1)/2\) determinant values make this discriminant a nonzero square; for each of these values \(D\) has distinct rational eigenvalues and is diagonalizable. When the discriminant vanishes, \(D\) is diagonalizable if and only if \(D=(s/2)I\), yielding at most one additional perturbation.

If \(A\) is scalar, only \(N=0\) can make \(D\) diagonalizable: every nonzero square-zero perturbation gives a nonscalar repeated-root matrix. Thus \(C(A)=1\). If \(A\) is nonscalar with one invariant line, its discriminant vanishes and \(e(A)=1\); the \((q-1)/2\) distinct-root determinant values differ from \(d\), each carrying \(q\) perturbations by the fiber formula. The unique remaining scalar-diagonalizable case comes from \(N=A-(s/2)I\), which squares to zero by Cayley–Hamilton; hence \(C(A)=q(q-1)/2+1\).

If \(A\) has two distinct rational eigenvalues, \(e(A)=2\), and \(d\) belongs to the distinct-root determinant set. The corresponding fiber has \(2q-1\) elements; the other \((q-3)/2\) admissible determinant values each have fiber \(q-1\). The sum is \((q^2+1)/2\). Finally, if \(A\) has irreducible characteristic polynomial, \(e(A)=0\), and \(d\) is not in the distinct-root determinant set; each of its \((q-1)/2\) admissible determinant values has fiber \(q+1\), yielding \((q^2-1)/2\). No scalar correction arises in the last two cases. This finishes the proof over all finite fields.

## Verification
The accompanying standalone `verify.py` constructs finite-field operations and exhaustively iterates all \(q^4\) matrices and all \(q^2\) square-zero perturbations for \(q\in\{2,3,4,5,7,8\}\). It computes invariant lines directly, computes each determinant fiber, and tests each diagonalizability condition by finding eigenvalues over the ground field. It checks both stated formulas for every input matrix, comprising 7,475 matrices and 400,307 tested matrix–perturbation pairs. Command: `python verify.py`. The finite enumerations corroborate but are not used as a substitute for the proof for arbitrary prime powers.

## Relationship to prior work
Danchev, García and Gómez Lozano (2026, arXiv:2604.15286v1), especially Proposition 2.2, construct decompositions into diagonalizable plus square-zero matrices in characteristic two. Their 2025 paper (arXiv:2507.05762v1) gives qualitative existence results in odd characteristic and quotes the general two-by-two existence theorem from their earlier work. These establish existence, which is **not** claimed new. The exact determinant-fiber law and the complete decomposition multiplicities refine that qualitative question. Published studies of additive torsion-unit/nilpotent decompositions, multiplicative idempotent–nilpotent factorizations, and the binary three-dimensional boundary involve different summands, operations, or matrix orders; their conclusions do not directly supply these fibers.

## Limitations
The calculation treats only order-two matrices. It is not a classification in higher dimensions. The 2022 predecessor paper's complete full text was not available for inspection; its two-dimensional existence theorem was inspected as quoted in the accessible 2025 original research article. Equivalent older enumerations or an unindexed determinant-shift treatment are a residual literature risk. The finite-field exhaustive checks do not constitute a proof beyond the tested field sizes.

## References
1. P. Danchev, E. García and M. Gómez Lozano, *Matrices over finite fields of characteristic 2 as sums of diagonalizable and square-zero matrices*, arXiv:2604.15286v1, April 16, 2026, https://arxiv.org/html/2604.15286v1 (especially Proposition 2.2).
2. P. Danchev, E. García and M. Gómez Lozano, *Matrices over finite fields of odd characteristic as sums of diagonalizable and square-zero matrices*, arXiv:2507.05762v1, July 8, 2025, https://arxiv.org/html/2507.05762v1 (including its quotation of the earlier two-dimensional existence theorem).
3. P. Danchev, E. García and M. Gómez Lozano, *Decompositions of matrices into diagonalizable and square-zero matrices*, Linear and Multilinear Algebra, DOI:10.1080/03081087.2020.1862742 (full text not examined).
