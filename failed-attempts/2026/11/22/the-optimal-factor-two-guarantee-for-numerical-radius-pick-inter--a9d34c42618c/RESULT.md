# The optimal factor-two guarantee for numerical-radius Pick interpolation and its sharp collision defect

## Finding
For any integer \(m,d\ge1\), any pairwise distinct nodes \(\lambda_1,\ldots,\lambda_m\in\mathbb D\) and target matrices \(W_1,\ldots,W_m\in M_d(\mathbb C)\), write \(\mathcal S=[(1-\lambda_i\overline{\lambda_j})^{-1}I_d]_{i,j=1}^m\), \(D=\operatorname{diag}(W_1,\ldots,W_m)\), and \(T=\mathcal S^{-1/2}D\mathcal S^{1/2}\). Let \(P=\nu(T)\) be the minimum budget passing the numerical-radius Pick-circle necessary test in [1, Theorem 2.4], and let \(\Gamma\) be the infimum of \(\sup_{z\in\mathbb D}\nu(F(z))\) over all bounded holomorphic \(M_d(\mathbb C)\)-valued functions interpolating the data. Then the **universal sharp relaxation guarantee** is
\[
\boxed{P\le\Gamma\le2P.}
\]
The constant \(2\) cannot be replaced by any smaller universal constant, even with exactly two nodes and \(d=2\); the following quantitative witness proves its sharpness.

Let \(0<r<1\) and \(t>0\). Consider the two-point matrix interpolation data
\[
F(0)=tE_{12},\qquad F(r)=tE_{21}
\]
for bounded holomorphic \(F:\mathbb D\to M_2(\mathbb C)\), where \(E_{ij}\) are matrix units and \(\nu(A)=\sup_{\|x\|_2=1}|\langle Ax,x\rangle|\) is the numerical radius. Define the true optimal interpolation cost
\[
\Gamma(r,t)=\inf_F\sup_{z\in\mathbb D}\nu(F(z)).
\]
Define \(Q(r,t)\) to be the smallest budget for which the natural one-parameter numerical-radius Pick positivity test of Ahmed–Bhowmik–Das–Sau [1, Theorem 2.4] passes for these data. Then
\[
\boxed{Q(r,t)=\frac{t}{2r}},
\]
while the actual interpolation cost obeys the two explicit global inequalities
\[
\boxed{1+\sqrt{1-r^2}\ \le\ \frac{\Gamma(r,t)}{Q(r,t)}\ \le\ 2.}
\]
Consequently, **the proposed Pick relaxation underestimates the true optimal interpolation norm by an asymptotically sharp factor of two** as the nodes coalesce:
\[
\boxed{\lim_{r\downarrow0}\frac{\Gamma(r,t)}{Q(r,t)}=2,\qquad
\lim_{r\downarrow0}\frac{r\,\Gamma(r,t)}{t}=1.}
\]
Both limits are **uniform over all \(t>0\)** because the displayed bounds are independent of \(t\). The formula also gives an exact parameter region of false positives: the one-parameter Pick test at budget one passes, yet no holomorphic numerical-radius-one interpolant exists, whenever
\[
\boxed{\frac{2r}{1+\sqrt{1-r^2}}<t\le2r.}
\]
The region is nonempty for every \(r\in(0,1)\). At \(r=1/2\), \(t=1\), it contains the individual counterexample already given in [1]; the new statement includes the universal optimal factor-two guarantee, its sharp small-separation witness, and a two-parameter false-positive wedge.

## Assumptions and scope
The disk is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). Values are complex \(2\times2\) matrices, and the numerical radius uses the standard Euclidean inner product. The universal bound applies to arbitrary finite sets of distinct disk nodes and arbitrary complex square-matrix values. For the sharpness family we optimize over **all** bounded holomorphic matrix-valued interpolants, without restricting to affine or off-diagonal functions; an affine interpolation below is a supplementary explicit witness. The positive node separation is real \(r\in(0,1)\), and positive data amplitude \(t>0\) is arbitrary. The lower bound is a necessary condition, **not** an asserted exact finite-\(r\) formula for \(\Gamma\).

## Proof
**0. Universal estimate for arbitrary finite interpolation data.** For any budget \(M\) of a genuine numerical-radius-bounded interpolant, the necessity direction of [1, Theorem 2.4], scaled by \(M\), gives \(P=\nu(T)\le M\), hence \(P\le\Gamma\). On the other hand, the classical finite-dimensional **matrix-valued Nevanlinna--Pick theorem** guarantees an operator-norm-bounded holomorphic interpolant at the sharp budget \(\|T\|_2\), since the usual matrix Pick criterion \(\mathcal S-\|T\|_2^{-2}D\mathcal S D^*\succeq0\) is equivalent to \(\|T\|_2\) dominating \(\|\mathcal S^{-1/2}D\mathcal S^{1/2}\|_2\). For every complex matrix, \(\nu(T)\le\|T\|_2\le2\nu(T)\). The interpolant from matrix Nevanlinna--Pick therefore satisfies \(\sup_z\nu(F(z))\le\|T\|_2\le2P\), proving \(\Gamma\le2P\). The case \(P=0\) has \(D=0\) and the zero interpolant, so no division by zero is needed. Sections 1--4 exhibit a family for which \(\Gamma/P\to2\), proving universal optimality.

**1. Exact evaluation of the relaxed positivity test.** Let
\[
S=\begin{pmatrix}1&1\\1&(1-r^2)^{-1}\end{pmatrix},\quad
\mathcal S=S\otimes I_2,\quad D=\operatorname{diag}(tE_{12},tE_{21}).
\]
Theorem 2.4 of [1] states that the positivity of its entire circle of Pick matrices at budget \(M>0\) is equivalent to \(\nu(\mathcal S^{-1/2}D\mathcal S^{1/2})\le M\). Put \(T=\mathcal S^{-1/2}D\mathcal S^{1/2}\). Since \(D^2=0\), we have \(T^2=0\), and hence \(\nu(T)=\|T\|_2/2\); indeed, every square-zero operator is unitarily a block matrix \(\begin{psmallmatrix}0&B\\0&0\end{psmallmatrix}\), with numerical radius \(\|B\|_2/2\).

A direct multiplication gives
\[
S^{-1}=\frac1{r^2}\begin{pmatrix}1&-(1-r^2)\\-(1-r^2)&1-r^2\end{pmatrix},
\qquad D\mathcal SD^*=
\operatorname{diag}\!\left(t^2E_{11},\frac{t^2}{1-r^2}E_{22}\right).
\]
The two nonzero eigenvalues of \(\mathcal S^{-1}D\mathcal SD^*\) are both \(t^2/r^2\): the first arises from \((S^{-1})_{11}t^2\), and the second from \((S^{-1})_{22}t^2/(1-r^2)\). This matrix is similar to \(TT^*\), so the two nonzero singular values of \(T\) are \(t/r\). It follows that
\[
Q(r,t)=\nu(T)=\frac{t}{2r}.
\]
In particular, the Pick family at budget one passes if and only if \(t\le2r\).

**2. Schwarz–Pick lower bound for every interpolant.** Fix the unit vector \(u=(1,i)^T/\sqrt2\). For any admissible \(F\) with \(\sup_z\nu(F(z))\le M\), the scalar holomorphic function \(h(z)=\langle F(z)u,u\rangle/M\) maps the disk to its closed unit disk. Its two values are opposite imaginary numbers with modulus \(x=t/(2M)\). The scalar Schwarz–Pick inequality implies
\[
r\ge\frac{2x}{1+x^2}.
\]
Since each interpolation target has numerical radius \(t/2\), necessarily \(M\ge t/2\), so \(0<x\le1\). Inverting the strictly increasing map \(x\mapsto 2x/(1+x^2)\) on \([0,1]\) yields
\[
x\le\frac{r}{1+\sqrt{1-r^2}},\qquad
M\ge\frac{t}{2r}(1+\sqrt{1-r^2}).
\]
Take the infimum over all \(F\). This proves the lower bound, including possible nonattainment of the infimum.

**3. Constructive upper bound.** The affine polynomial
\[
F_0(z)=t\bigl((1-z/r)E_{12}+(z/r)E_{21}\bigr)
\]
has precisely the prescribed values. For any complex numbers \(a,b\),
\[
\nu\!\left(\begin{pmatrix}0&a\\b&0\end{pmatrix}\right)=\frac{|a|+|b|}{2};
\]
this follows by maximizing the phase of \(\overline{x_1}x_2\) and using \(|x_1x_2|\le1/2\). Therefore
\[
\sup_{|z|<1}\nu(F_0(z))
=\frac t2\sup_{|z|<1}(|1-z/r|+|z|/r)
=\frac t2(1+2/r).
\]
The last upper bound follows from the triangle inequality and is approached as \(z\to-1\) within the disk. Thus \(\Gamma(r,t)\le(t/2)(1+2/r)=Q(r,t)(2+r)\). This independently gives the weaker elementary upper bound \(Q(r,t)(2+r)\). The universal estimate in Section 0 gives the claimed stronger upper bound \(2Q(r,t)\), and together with Section 2 establishes both limits uniformly in amplitude.

**4. A whole false-positive wedge.** The exact Pick test passes at budget one when \(t\le2r\), but the Schwarz–Pick lower bound forces \(\Gamma(r,t)>1\) if \(t>2r/(1+\sqrt{1-r^2})\). The open-to-closed parameter interval claimed above follows. Its width is strictly positive for every \(0<r<1\), and the ratio between the two test thresholds is exactly \(1+\sqrt{1-r^2}\), approaching two as \(r\downarrow0\). This completes the proof.

## Verification
Every identity in the proof uses finite explicit matrices, the square-zero numerical-radius identity, classical matrix-valued Nevanlinna--Pick, the standard two-sided numerical-radius inequality, scalar Schwarz--Pick, and an explicit affine interpolant. There is no finite-to-infinite extrapolation. The supplementary standalone exact-rational checker `check_exact.py` verifies the displayed inverse-Szegő formulas and equality of both nonzero squared singular values at multiple rational node radii. The checker is not used to establish the infinite analytic statement.

## Relationship to prior work
Ahmed, Bhowmik, Das and Sau [1] formulate numerical-radius Schur interpolation, prove their Pick-circle condition is necessary (Theorem 2.4), and give the particular unsolvable data \(r=1/2\), \(t=1\) in Example 2.5 even though their necessary test passes. Those contributions are explicitly acknowledged. The new result gives the **universal factor-two norm guarantee and proves its optimality**, using the classical matrix Nevanlinna--Pick theorem and the standard \(\|T\|\le2
u(T)\) inequality as credited ingredients. The explicit family computes the exact relaxed budget, supplies a false-positive wedge, and proves the sharp limiting factor two. It does not claim to solve general numerical-radius interpolation or give the exact finite-distance true cost.

## Limitations
The universal estimate covers arbitrary finite square-matrix data; its *sharpness witness* is restricted to the two-node, two-by-two nilpotent target family. The finite-distance value of the true interpolation cost is only bounded, not determined. The sharp factor two arises partly from the standard operator-versus-numerical-radius inequality, but saturation by holomorphic interpolation is the additional nontrivial point. A full independent mathematical audit has not been undertaken, and relevant unindexed literature could affect publication priority.

## References
[1] Hamidul Ahmed, Mainak Bhowmik, B. Krishna Das and Haripada Sau, *Interpolation, Factorization, and Approximation in the Numerical Radius Unit Ball*, arXiv:2611.19189v1, publicly submitted 2026-11-14, https://arxiv.org/html/2611.19189v1; Theorem 2.4 and Example 2.5.
