# Exact complementation constant two for discretely represented ideal-null sequence spaces

## Finding
Let \(\mathcal I\) be a proper discretely represented ideal on \(\mathbb N\): in the terminology of Rincón-Villamizar--Uzcátegui Aylwin, \(\mathcal I\) is either \(k\)-maximal for some finite \(k\ge1\) or strongly \(\omega\)-maximal. Then
\[
\lambda_{\mathrm{comp}}\!\left(c_{0,\mathcal I},\ell_\infty\right)=2.
\]
More precisely, for the discrete maximal-ideal representation and block partition used in their explicit construction, the complementary projections
\[
P:\ell_\infty\longrightarrow c_{0,\mathcal I},
\qquad
Q=I-P
\]
satisfy
\[
\|P\|=2,
\qquad
\|Q\|=1.
\]
Consequently, the open question in the 2026 paper *Structure properties of Banach spaces of I-null sequences* asking whether every complemented \(c_{0,\mathcal I}\) has complementation constant exactly \(2\) has an affirmative answer for the entire class of discretely represented ideals.

## Assumptions and scope
For an ideal \(\mathcal I\) on \(\mathbb N\),
\[
c_{0,\mathcal I}
=
\left\{
x\in\ell_\infty:
\{n\in\mathbb N:|x_n|\ge\varepsilon\}\in\mathcal I
\text{ for every }\varepsilon>0
\right\}.
\]
For a complemented closed subspace \(Y\subseteq\ell_\infty\), write
\[
\lambda_{\mathrm{comp}}(Y,\ell_\infty)
=
\inf\{\|R\|:R^2=R,\ \operatorname{ran}R=Y\}.
\]

A discretely represented ideal has a representation
\[
\mathcal I=\bigcap_{m\in F}\mathcal I_m,
\]
where \(F\) is finite or countably infinite, the \(\mathcal I_m\) are maximal ideals forming the required discrete family, and there is a partition \(\{A_m:m\in F\}\) of \(\mathbb N\) with \(A_m\in\mathcal I_m^*\). If
\[
L_m(x)=\mathcal I_m^*-\lim x
\]
denotes the corresponding ultrafilter limit, the 2025 paper constructs the blockwise operator
\[
Qx=\sum_{m\in F}L_m(x)\chi_{A_m},
\qquad
P=I-Q.
\]
The sum is interpreted blockwise on the pairwise disjoint partition.

## Proof
The 2025 paper proves that \(P\) is a continuous projection from \(\ell_\infty\) onto \(c_{0,\mathcal I}\) and explicitly records
\[
\|P\|\le2.
\]
Therefore
\[
\lambda_{\mathrm{comp}}\!\left(c_{0,\mathcal I},\ell_\infty\right)\le2.
\]

The 2026 paper proves that for every proper ideal \(\mathcal J\), the complementation constant of \(c_{0,\mathcal J}\), whenever the space is complemented in \(\ell_\infty\), cannot be strictly smaller than \(2\). Applying this universal lower bound to the present proper ideal gives
\[
\lambda_{\mathrm{comp}}\!\left(c_{0,\mathcal I},\ell_\infty\right)\ge2.
\]
Hence
\[
\lambda_{\mathrm{comp}}\!\left(c_{0,\mathcal I},\ell_\infty\right)=2.
\]

Because \(P\) is one of the projections onto \(c_{0,\mathcal I}\),
\[
2
=
\lambda_{\mathrm{comp}}\!\left(c_{0,\mathcal I},\ell_\infty\right)
\le \|P\|
\le2,
\]
so \(\|P\|=2\).

It remains to identify the complementary projection norm. Each ultrafilter limit \(L_m\) is a positive norm-one functional on \(\ell_\infty\), so
\[
|L_m(x)|\le\|x\|_\infty.
\]
Since the \(A_m\) form a partition,
\[
\|Qx\|_\infty
=
\sup_{m\in F}|L_m(x)|
\le
\|x\|_\infty.
\]
Thus \(\|Q\|\le1\). On the constant unit sequence \(\mathbf 1\), every \(L_m(\mathbf1)=1\), hence \(Q\mathbf1=\mathbf1\). Therefore \(\|Q\|=1\).

## Verification
The argument has two independent quantitative inputs.

First, Lemma 6.4 and Theorem 6.5 of *On the complementation of spaces of \(\mathcal I\)-null sequences* supply the explicit block projection, prove that its range is \(c_{0,\mathcal I}\), and give \(\|P\|\le2\). The same displayed formula gives \(\|Q\|=1\) directly because the partition makes the supremum norm of \(Qx\) equal to the supremum of the ultrafilter-limit coefficients.

Second, Corollary 5.9 of *Structure properties of Banach spaces of I-null sequences* supplies the lower bound \(2\) for the complementation constant of every proper ideal. Combining the two inequalities forces equality. No limiting computation, finite experiment, or unproved structural assumption is used.

## Relationship to prior work
The 2025 paper develops the structural class of discretely represented ideals and constructs a projection \(P\) with the upper estimate \(\|P\|\le2\). That result by itself does not identify the infimum over all projections onto \(c_{0,\mathcal I}\).

The 2026 paper proves the universal lower bound \(2\) and then asks whether a complemented ideal can ever have complementation constant strictly larger than \(2\). The present observation combines that lower bound with the earlier explicit projection on a natural, already-developed class. It therefore settles the 2026 question for all discretely represented ideals, while leaving the general complemented case open.

Targeted searches for the exact constant on finite intersections of maximal ideals, strongly \(\omega\)-maximal ideals, and discretely represented ideals did not locate a published statement of this combination. The closest checked sources are precisely the two papers whose one-sided bounds meet here.

## Limitations
The conclusion is restricted to discretely represented ideals. It does not show that every complemented \(c_{0,\mathcal I}\) has complementation constant \(2\), and the 2025 paper exhibits complemented ideals outside the at-most-\(\omega\)-maximal framework.

The exactness argument is a short cross-paper corollary, so an equivalent observation may exist informally or under different terminology. Very recent literature on ideal-null sequence spaces may also be incompletely indexed.

## References
1. M. A. Rincón-Villamizar and C. Uzcátegui Aylwin, *On the complementation of spaces of \(\mathcal I\)-null sequences*, arXiv:2507.13866, first public 2025-07-18. See Lemma 6.4 and Theorem 6.5.
2. M. A. Rincón-Villamizar, V. S. Ronchim, and C. Uzcátegui Aylwin, *Structure properties of Banach spaces of I-null sequences*, arXiv:2609.17972, first public 2026-09-16. See Corollary 5.9 and Question 5.12.
