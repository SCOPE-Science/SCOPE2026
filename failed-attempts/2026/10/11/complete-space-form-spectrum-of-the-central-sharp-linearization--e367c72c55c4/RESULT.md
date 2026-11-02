# Complete space-form spectrum of the central sharp linearization

## Finding

Let
\[
n\ge4
\]
and let
\[
R_\kappa=\frac{\kappa}{2}g^2
\]
be the algebraic curvature tensor of constant sectional curvature \(\kappa\) on an \(n\)-dimensional Euclidean vector space.

Belkhirat's central Clifford component satisfies
\[
\Gamma_{1,1}(R)(S)=\frac14 R\#S,
\]
and the quadratic map
\[
\mathcal Q(R)=-\frac14R\#R
\]
has linearization
\[
d\mathcal Q_R(S)=-2\Gamma_{1,1}(R)S.
\]

Write the orthogonal Ricci decomposition of algebraic curvature tensors as
\[
\mathcal C
=
\mathcal C_{\mathrm{sc}}
\oplus
\mathcal C_{\mathrm{Ric}_0}
\oplus
\mathcal C_W,
\]
for the scalar-curvature, traceless-Ricci, and Weyl summands. At \(R_\kappa\), each of these three summands is an eigenspace of the central channel:
\[
\boxed{
\Gamma_{1,1}(R_\kappa)
=
\begin{cases}
2(n-2)\kappa\,I,&\mathcal C_{\mathrm{sc}},\\[3pt]
(n-4)\kappa\,I,&\mathcal C_{\mathrm{Ric}_0},\\[3pt]
-2\kappa\,I,&\mathcal C_W.
\end{cases}
}
\]
Therefore the complete spectrum of the sharp quadratic linearization is
\[
\boxed{
d\mathcal Q_{R_\kappa}
=
\begin{cases}
-4(n-2)\kappa\,I,&\mathcal C_{\mathrm{sc}},\\[3pt]
-2(n-4)\kappa\,I,&\mathcal C_{\mathrm{Ric}_0},\\[3pt]
4\kappa\,I,&\mathcal C_W.
\end{cases}
}
\]

The corresponding multiplicities are
\[
1,\qquad
\frac{n(n+1)}2-1,\qquad
\frac{n(n+1)(n+2)(n-3)}{12}.
\]

A notable consequence occurs in dimension four:
\[
\boxed{
d\mathcal Q_{R_\kappa}
=
-8\kappa\,I
\ \text{on }\mathcal C_{\mathrm{sc}},
\qquad
0
\ \text{on }\mathcal C_{\mathrm{Ric}_0},
\qquad
4\kappa\,I
\ \text{on }\mathcal C_W.
}
\]
Thus \(n=4\) is the unique dimension \(n\ge4\) in which the sharp-only reaction linearization is neutral on every traceless-Ricci perturbation. The Weyl eigenvalue \(4\kappa\) is independent of dimension.

## Assumptions and scope

The statement uses the normalization of the cited double-form source:
\[
R_\kappa=\frac{\kappa}{2}g^2,
\qquad
\Gamma_{1,1}(R)=\frac14R\#,
\qquad
\mathcal Q(R)=-\frac14R\#R.
\]

The result concerns only the algebraic sharp contribution to the Ricci-flow curvature reaction. It is not the spectrum of the full Ricci-flow linearization, which also contains the rough Laplacian and the remaining algebraic reaction terms.

The decomposition is the usual orthogonal decomposition of algebraic curvature tensors under \(O(n)\). The source explicitly recovers these three irreducible summands from its extreme Clifford channels.

## Proof

Let
\[
E_{ij}=e^i\wedge e^j,
\qquad
1\le i<j\le n,
\]
be the standard orthonormal basis of \(\Lambda^2V^\ast\). For constant curvature, the source gives
\[
\Gamma_{1,1}(R_\kappa)
=
\kappa\sum_{a<b}D_L(E_{ab})D_R(E_{ab}).
\]

The construction is \(O(n)\)-equivariant. Hence its restriction to the algebraic-curvature space preserves the three irreducible Ricci-decomposition summands and is scalar on each one. It is therefore enough to calculate one nonzero vector in each summand.

First consider a diagonal algebraic curvature operator
\[
S=\sum_{i<j}w_{ij}\,E_{ij}\otimes E_{ij}.
\]
The derivation \(D(E_{ab})\) annihilates \(E_{ij}\) unless exactly one of \(a,b\) belongs to \(\{i,j\}\). In the nonzero case it replaces that common index by the other index of \(\{a,b\}\), up to sign. Because the same derivation acts in both tensor factors, the two signs cancel. Consequently the coefficient of \(E_{ij}\otimes E_{ij}\) after applying the central channel is
\[
\boxed{
\bigl(\Gamma_{1,1}(R_\kappa)S\bigr)_{ij}
=
\kappa
\sum_{k\ne i,j}
\bigl(w_{ik}+w_{jk}\bigr),
}
\]
where \(w_{ij}=w_{ji}\).

For the scalar summand take
\[
w_{ij}=1.
\]
Then
\[
\sum_{k\ne i,j}(w_{ik}+w_{jk})=2(n-2),
\]
so the scalar eigenvalue of \(\Gamma_{1,1}(R_\kappa)\) is
\[
2(n-2)\kappa.
\]

For the traceless-Ricci summand, take a traceless diagonal symmetric tensor with entries
\[
s_1,\ldots,s_n,
\qquad
\sum_i s_i=0.
\]
The associated curvature operator has weights proportional to
\[
w_{ij}=s_i+s_j.
\]
The common proportionality factor is irrelevant to the eigenvalue. Then
\[
\begin{aligned}
\sum_{k\ne i,j}(w_{ik}+w_{jk})
&=
\sum_{k\ne i,j}
\bigl(s_i+s_k+s_j+s_k\bigr)\\
&=
(n-2)(s_i+s_j)
+
2\sum_{k\ne i,j}s_k\\
&=
(n-4)(s_i+s_j).
\end{aligned}
\]
Thus the traceless-Ricci eigenvalue is
\[
(n-4)\kappa.
\]

For the Weyl summand choose the diagonal weights supported on four coordinate directions
\[
w_{12}=w_{34}=1,
\qquad
w_{13}=w_{24}=-1,
\]
with all other \(w_{ij}\) equal to zero. Every row sum vanishes:
\[
\sum_{j\ne i}w_{ij}=0.
\]
Hence this diagonal curvature operator has zero Ricci contraction and is a nonzero Weyl tensor. For every pair \(i\ne j\),
\[
\sum_{k\ne i,j}(w_{ik}+w_{jk})
=
-2w_{ij},
\]
so the Weyl eigenvalue is
\[
-2\kappa.
\]

This proves the three central-channel eigenvalues. The source's linearization identity
\[
d\mathcal Q_{R_\kappa}
=
-2\Gamma_{1,1}(R_\kappa)
\]
then gives the three displayed eigenvalues of \(d\mathcal Q_{R_\kappa}\).

Finally, the standard dimensions of the three Ricci-decomposition pieces are
\[
1,
\qquad
\frac{n(n+1)}2-1,
\qquad
\frac{n(n+1)(n+2)(n-3)}{12},
\]
which sum to the dimension of the algebraic-curvature space. This completes the spectrum with multiplicities.

## Verification

The bundled checker constructs the matrices of all derivations
\[
D(E_{ab}):\Lambda^2V^\ast\to\Lambda^2V^\ast
\]
directly from the source definition. It forms
\[
\Gamma(S)
=
\sum_{a<b}D(E_{ab})S D(E_{ab})^T
\]
and replays the scalar, traceless-Ricci, and Weyl eigenvalue calculations for every dimension
\[
4\le n\le9.
\]

The same checker separately verifies the all-\(n\) diagonal coefficient identity symbolically:
\[
\sum_{k\ne i,j}
\bigl((s_i+s_k)+(s_j+s_k)\bigr)
=
(n-4)(s_i+s_j)
\]
under \(\sum_k s_k=0\), as well as the row-sum Weyl reduction to \(-2w_{ij}\).

The finite matrix replay is not used as a proof for arbitrary dimension; it is an independent implementation check of the analytic formula above.

## Relationship to prior work

The sharp product itself is classical in curvature-operator formulations of Ricci flow. Böhm and Wilking use the curvature ODE
\[
R'=R^2+R^\#
\]
in their positive-curvature-operator work, and Labbi develops the sharp operation in double-form calculus.

Belkhirat identifies the central degree-preserving Clifford channel with one quarter of the sharp action and proves that
\[
-2\Gamma_{1,1}(R)
\]
is the linearization of
\[
\mathcal Q(R)=-\frac14R\#R.
\]
The same paper separately reconstructs the scalar, traceless-Ricci, and Weyl components from the extreme channels and gives a constant-curvature normalization check. Its inspected text does not state the spectrum of the central channel on those three curvature summands; searches within the full text find no eigenvalue or spectrum statement.

The result here combines those two structures and computes the complete space-form spectrum. It exposes a dimension-four cancellation in the traceless-Ricci channel and a dimension-independent Weyl eigenvalue, neither of which is stated in the motivating source.

Targeted searches for the source identifier, the sharp-product linearization, the three Ricci-decomposition eigenvalues, and the dimension-four cancellation did not locate a published statement with these constants.

## Limitations

This is the spectrum of the central sharp contribution only. Stability conclusions for the full Ricci flow require the other algebraic terms, gauge considerations, and the spatial differential operator.

The proof uses the constant-curvature background. For a general curvature tensor, the central channel need not act by scalars on the Ricci-decomposition pieces.

The classical sharp-product literature is extensive. Although the checked sources and searches did not locate this exact three-eigenvalue statement, an equivalent computation could exist under curvature-operator conventions with different overall factors.

## References

1. A. Belkhirat, *Clifford Actions and the Algebra of Double Forms*, arXiv:2610.04428v1, first submitted 3 October 2026.
2. C. Böhm and B. Wilking, *Manifolds with positive curvature operators are space forms*, Annals of Mathematics 167 (2008), 1079--1097; arXiv:math/0606187.
3. M.-L.. Labbi, *Hodge-de Rham and Lichnérowicz Laplacians on double forms and some vanishing theorems*, arXiv:2405.12828v1, first submitted 21 May 2024.
