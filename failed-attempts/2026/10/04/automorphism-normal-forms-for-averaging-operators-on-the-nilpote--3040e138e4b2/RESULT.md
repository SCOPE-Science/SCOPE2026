# Automorphism normal forms for averaging operators on the nilpotent two-dimensional pre-Lie algebra
## Finding
Let \(A\) be the complex pre-Lie algebra with basis \(e_1,e_2\) and multiplication
\[
e_1\cdot e_1=e_2,
\]
with all other basis products zero. An averaging operator is a linear map \(P:A\to A\) satisfying
\[
P(x)\cdot P(y)=P\bigl(x\cdot P(y)\bigr)=P\bigl(P(x)\cdot y\bigr)
\]
for all \(x,y\in A\).

Up to isomorphism of averaging pairs, every averaging operator is represented uniquely by exactly one of
\[
S_a=aI\quad(a\in\mathbb C),
\]
\[
J_a=aI+E_{21}\quad(a\in\mathbb C),
\]
or
\[
D_d=\operatorname{diag}(0,d)\quad(d\in\mathbb C^\times),
\]
where \(E_{21}(e_1)=e_2\) and \(E_{21}(e_2)=0\).

The corresponding stabilizers inside \(\operatorname{Aut}(A)\) are, respectively, the full automorphism group, the one-dimensional subgroup \(\xi=1\), and the one-dimensional subgroup \(\nu=0\).

## Assumptions and scope
The ground field is \(\mathbb C\). The result concerns the single nilpotent two-dimensional pre-Lie algebra \(A\) with \(e_1\cdot e_1=e_2\). Isomorphism of pairs means conjugacy by an algebra automorphism: \((A,P)\cong(A,P')\) exactly when \(P'=\phi P\phi^{-1}\) for some \(\phi\in\operatorname{Aut}(A)\).

No statement is made here about the other two-dimensional pre-Lie isomorphism types, about positive characteristic, or about averaging bialgebra structures.

## Proof
Write
\[
P(e_1)=ae_1+ce_2,\qquad P(e_2)=be_1+de_2.
\]
Because the only nonzero product is \(e_1\cdot e_1=e_2\), imposing the averaging identity on the four ordered basis pairs gives
\[
b^2=0,\qquad ab=0,\qquad b(a-d)=0,\qquad a(a-d)=0.
\]
Over \(\mathbb C\), the first equation forces \(b=0\). Hence either \(a=0\), with \(c,d\) arbitrary, or \(d=a\), with \(a,c\) arbitrary. Thus every averaging operator lies in the union of the two families
\[
Q_{c,d}=\begin{pmatrix}0&0\\ c&d\end{pmatrix},
\qquad
P_{a,c}=\begin{pmatrix}a&0\\ c&a\end{pmatrix}.
\]
Their intersection is \(Q_{c,0}=P_{0,c}\).

Next, since \(e_2=e_1\cdot e_1\), an automorphism is determined by the image of \(e_1\). Writing
\[
\phi(e_1)=\xi e_1+\nu e_2
\]
with \(\xi\ne0\), multiplicativity forces
\[
\phi(e_2)=\phi(e_1)^2=\xi^2e_2.
\]
Conversely every such map is invertible and multiplicative. Therefore
\[
\operatorname{Aut}(A)=\{\phi_{\xi,\nu}:\xi\in\mathbb C^\times,\ \nu\in\mathbb C\}.
\]
Direct conjugation gives
\[
\phi_{\xi,\nu}P_{a,c}\phi_{\xi,\nu}^{-1}=P_{a,\xi c},
\]
and
\[
\phi_{\xi,\nu}Q_{c,d}\phi_{\xi,\nu}^{-1}
=Q_{\xi c-d\nu/\xi,d}.
\]

For \(P_{a,c}\), if \(c=0\) the operator is the scalar \(S_a\), while if \(c\ne0\) choosing \(\xi=c^{-1}\) gives \(J_a\). For \(Q_{c,d}\), if \(d\ne0\) choose \(\nu=\xi^2c/d\) to obtain \(D_d\); if \(d=0\), the operator already belongs to the \(P_{0,c}\) family and yields either \(S_0\) or \(J_0\).

Uniqueness follows from the displayed action and ordinary similarity invariants. Scalars cannot be conjugate to nonscalars. The operators \(J_a\) have one eigenvalue \(a\) and a nontrivial Jordan block, while \(D_d\) has two distinct eigenvalues \(0,d\). Within each family, \(a\) or \(d\) is fixed by the action. Finally, the stabilizer formulas follow immediately from the two conjugation equations.

## Verification
The accompanying `verify.py` checks the averaging identity on an exact integer grid for a general matrix and confirms that the accepted points are precisely those with \(b=0\) and either \(a=0\) or \(d=a\). It separately checks all displayed candidate families, verifies the automorphism law on a grid of \((\xi,\nu)\), and checks the two conjugation formulas and the stated normalizations. Running the packaged script produces `CHECK_OK`.

These computations are regression checks only. The infinite classification is proved by the polynomial equations and conjugation calculation above, not by finite enumeration.

## Relationship to prior work
Basdouri, Mosbahi and Zahari list averaging operators on all two-dimensional complex pre-Lie algebras in arXiv:2504.20297v1. Their table contains the two matrix shapes relevant to the algebra \(e_1\cdot e_1=e_2\), but the paper does not analyze conjugacy under algebra automorphisms; document-wide searches for “automorphism” and “conjug” return no occurrence. The table also attaches nonzero parameter restrictions, whereas the defining identities show that boundary values such as scalar maps and the zero map must be retained in a complete classification.

Abdelwahab, Kaygorodov and Makhlouf, DOI 10.3842/SIGMA.2024.107, denote the same algebra by \(C_{03}\) and give its full automorphism group
\[
\phi(e_1)=\xi e_1+\nu e_2,\qquad \phi(e_2)=\xi^2e_2.
\]
Their orbit calculations concern compatible bilinear products, not averaging endomorphisms. Combining the independently rederived averaging equations with this automorphism action yields the three normal-form strata above.

Searches using the terms “averaging operators two-dimensional pre-Lie algebra e1 squared equals e2 automorphism conjugacy orbit”, “A3 pre-Lie averaging operator conjugacy classification”, “C03 pre-Lie averaging operators automorphism orbits”, and “averaging operator pre-Lie isomorphism classes dimension two” did not locate the stated normal-form classification or stabilizers.

## Limitations
The classification is only for this one complex two-dimensional pre-Lie algebra. The result does not claim a global orbit classification for all two-dimensional pre-Lie algebras. The orbit \(J_a\) has \(S_a\) in its Zariski closure, so the set of orbit representatives should not be interpreted as a separated geometric quotient without additional invariant-theoretic analysis.

A residual literature risk remains that an older thesis or differently indexed operator-classification paper may have carried out the same conjugacy calculation under another name for \(C_{03}\).

## References
1. I. Basdouri, B. Mosbahi, A. Zahari, “Rota-Type Operators on 2-Dimensional Pre-Lie Algebras”, arXiv:2504.20297v1, first posted 28 April 2025.
2. H. Abdelwahab, I. Kaygorodov, A. Makhlouf, “The Algebraic and Geometric Classification of Compatible Pre-Lie Algebras”, SIGMA 20 (2024), 107, DOI 10.3842/SIGMA.2024.107.
