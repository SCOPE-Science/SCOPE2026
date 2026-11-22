# Sharp Hurwitz–Radon lineability of real Keller counterexamples

## Finding
For each integer \(n\ge 3\), write \(n=2^{4a+b}u\) uniquely with \(u\) odd, \(a\ge 0\), and \(0\le b\le 3\), and put \(\rho(n)=8a+2^b\). Let \(\mathcal C_n(\mathbb R)\) consist of polynomial self-maps of \(\mathbb R^n\) which are noninjective on real points and have nonzero constant Jacobian determinant. The largest dimension of a real linear subspace \(V\) of polynomial self-maps satisfying \(V\setminus\{0\}\subset\mathcal C_n(\mathbb R)\) is **exactly** \(\rho(n)\). More strongly, for every \(F\in\mathcal C_n(\mathbb R)\), a subspace of this largest dimension can be chosen to contain \(F\).

For example, these dimensions for \(n=3,4,5,6,8,12,16\) are respectively \(1,4,1,2,8,4,9\). In particular every even \(n\ge4\) admits a two-dimensional pencil of real counterexamples, answering negatively Question 2 of Bernal-González, Calderón-Moreno and Prado-Bassas [1].

## Assumptions and scope
All polynomial maps and linear spaces are over \(\mathbb R\); injectivity is tested on \(\mathbb R^n\), not merely after complexification. Linearity means real-linear combinations of componentwise polynomial maps. The full real matrix theorem of Adams and its Hurwitz–Radon construction are used in their classical forms [2,3]. The statement concerns the unbounded-degree ambient polynomial space, not maps of a prescribed degree, fixed Jacobian constant, or maps with special normalization. The dimension-two Jacobian problem is not addressed.

## Proof
**Nonemptiness.** Take the rational-coefficient polynomial map \(F_0=(P,Q,R)\) in three variables, with \(t=1+xy\),
\[
P=t^3z+y^2t(4+3xy),\qquad
Q=y+3xt^2z+3xy^2(4+3xy),\qquad
R=2x-3x^2y-x^3z.
\]
Its Jacobian determinant is \(-2\), and the three distinct real inputs
\[
(0,0,-1/4),\quad(1,-3/2,13/2),\quad(-1,3/2,13/2)
\]
all map to \((-1/4,0,0)\). These identities are verified by direct polynomial arithmetic and were also recorded in [1]. For \(n>3\), extend \(F_0\) by \(n-3\) identity coordinates; this gives a member of \(\mathcal C_n(\mathbb R)\).

**Upper bound.** Suppose \(V\) is a real-linear subspace whose every nonzero polynomial map has nonzero constant Jacobian and is noninjective. The linear map
\[
D_0:V\longrightarrow M_n(\mathbb R),\qquad H\longmapsto JH(0)
\]
 is injective: if \(JH(0)=0\), the constant determinant of \(JH\) must vanish, so \(H=0\). Furthermore, every nonzero element of \(D_0(V)\) is a nonsingular real matrix. The exact nonsingular-matrix-subspace theorem \(\dim D_0(V)\le\rho(n)\) of Adams, Lax and Phillips [2] therefore gives \(\dim V\le\rho(n)\), including for an initially infinite-dimensional \(V\).

**Pointwise lower bound.** By the Hurwitz–Radon theorem in its explicit orthogonal-matrix formulation [3], there are \(\rho(n)-1\) real matrices \(J_1,\ldots,J_{\rho(n)-1}\) of size \(n\) satisfying
\[
J_i^{\mathsf T}=-J_i,\qquad J_i^2=-I,
\qquad J_iJ_j=-J_jJ_i\quad(i\ne j).
\]
(If \(\rho(n)=1\), take the empty family.) Let
\[
W_n=\operatorname{span}_{\mathbb R}\{I,J_1,\ldots,J_{\rho(n)-1}\}\subset M_n(\mathbb R).
\]
For \(A=a_0I+\sum_i a_iJ_i\), the relations imply
\[
A^{\mathsf T}A=\left(a_0^2+\sum_i a_i^2\right)I.
\]
Thus every nonzero \(A\in W_n\) is invertible and \(\dim W_n=\rho(n)\) (linear independence follows from the same identity).

Fix **any** \(F\in\mathcal C_n(\mathbb R)\) and define
\[
V_F=\{A\circ F:A\in W_n\},
\]
where \(A\) denotes its linear action on the output. For \(A\ne0\), \(A\circ F\) has constant Jacobian determinant \(\det(A)\det(JF)\ne0\) and preserves every collision of \(F\), so is noninjective. The linear map \(A\mapsto A\circ F\) is injective: if \(A\ne0\) then \(A\) is invertible and \(A\circ F\) cannot be the zero polynomial map (as \(JF\) is nonsingular). Consequently \(\dim V_F=\rho(n)\), and \(F\in V_F\) because \(I\in W_n\). This attains the upper bound at every counterexample.

## Verification
The standalone `checker.py` uses exact symbolic rational arithmetic to check \(\det JF_0=-2\), all three rational collisions, the four-dimensional quaternionic Hurwitz–Radon family, the determinant formula \(\det(aI+bi+cj+dk)=(a^2+b^2+c^2+d^2)^2\), and a sample list of \(\rho(n)\) values. These checks passed. They do not replace the all-dimensional Hurwitz–Radon and Adams theorems [2,3], which supply the general existence and upper bound.

## Relationship to prior work
Bernal-González, Calderón-Moreno and Prado-Bassas [1, Theorems 2.1 and 5.2] establish lineability one over algebraically closed characteristic-zero fields and over real closed fields in odd dimensions, and explicitly ask in Question 2 whether two-lineability also fails over \(\mathbb R\) in even dimensions. Their paper does not claim the full real lineability dimension. Adams, Lax and Phillips [2] classify nonsingular real matrix spaces, while Geramita and Pullman [3] supply integral orthogonal Hurwitz–Radon matrices; neither reference states a polynomial-counterexample lineability theorem. The derivative-at-a-point obstruction and output-matrix transfer here identify the two extremal problems and answer the stated even-dimensional question. No identical application was identified in the inspected literature or queried mathematical records; the standard nature of the matrix theorem remains an originality-priority caveat.

## Limitations
This is a self-reviewed mathematical deduction, not independently audited. It proves an exact **real** lineability invariant but not a classification of all extremal subspaces or their polynomial conjugacy classes. It requires the established deep nonsingular-matrix-space upper bound; the auxiliary checker cannot certify that theorem. It does not settle any characteristic-positive analogue or the two-variable Jacobian conjecture. No claim of publication priority beyond the checked materials is made.

## References
[1] L. Bernal-González, M. C. Calderón-Moreno and J. A. Prado-Bassas, *Counterexamples to the Jacobian Conjecture from the viewpoint of lineability*, arXiv:2611.03572v1 (first public 2026-11-02), https://arxiv.org/html/2611.03572v1, especially Theorem 5.2 and Question 2.

[2] J. F. Adams, P. D. Lax and R. S. Phillips, *On Matrices Whose Real Linear Combinations Are Nonsingular*, Proc. Amer. Math. Soc. **16** (1965), 318–322, DOI:10.2307/2033871; full text https://studylib.net/doc/7954703/on-matrices-whose-real-linear-combinations-are-nonsingular.

[3] A. V. Geramita and N. J. Pullman, *A Theorem of Hurwitz and Radon and Orthogonal Projective Modules*, Proc. Amer. Math. Soc. **42** (1974), 51–56, DOI:10.1090/S0002-9939-1974-0332764-4; full text https://www.academia.edu/24327322/A_THEOREM_OF_HURWITZ_AND_RADON_AND_ORTHOGONAL_PROJECTIVE_MODULES1journal_terms_of_use.
