# One-node Fourier quadrature: a sharp positivity frontier and collision noise layer

## Finding

For an odd equispaced trigonometric interpolation grid, move exactly **one** sampling node toward its next neighbor and leave all remaining nodes fixed. The unique trigonometric-exact quadrature rule has a sharp, all-grid-size phase transition: every weight is strictly positive before a half-mesh displacement; precisely the weight of the approached neighbor vanishes at the halfway point and becomes negative beyond it. The exact bounded-data quadrature amplification and the entire Fourier sampling singular spectrum are explicit. A near-collision boundary layer separates bounded quadrature noise from unbounded coefficient-recovery conditioning.

Specifically, for every odd \(N\ge3\) and \(0\le\delta<1\), let \(\Lambda_N(\delta)\) denote the operator norm of the quadrature rule from the \(N\) sample values in \(\ell^\infty\) to their normalized-circle integral. Then
\[
\Lambda_N(\delta)=1+\frac2N\max\!\left\{0,\frac{\sin(\pi\delta/N)}{\sin(\pi(1-\delta)/N)}-1\right\}.
\]
For \(0<\delta<1\), put \(c_N(\delta)=\sin(\pi\delta)/(N\sin(\pi\delta/N))\). The squared singular values of the normalized Fourier evaluation matrix are exactly
\[
1-\sqrt{1-c_N(\delta)^2},\qquad
\underbrace{1,\ldots,1}_{N-2\text{ copies}},\qquad
1+\sqrt{1-c_N(\delta)^2}.
\]
For each fixed \(t>0\), take \(\delta_N=1-t/N\) along odd \(N>t\). Then
\[
\lim_{N\to\infty}\Lambda_N(\delta_N)=1+\frac2t,
\qquad
\lim_{N\to\infty}\frac{\kappa_2(F_{\delta_N,N})}{N}=\frac2t.
\]
Thus integration remains uniformly stable in this critical collision layer while full Fourier coefficient recovery becomes linearly ill-conditioned.

## Assumptions and scope

Let \(N=2m+1\), \(m\in\mathbb N\), and \(h=2\pi/N\). Let \(\mathcal T_m\) be the complex trigonometric polynomials of degree at most \(m\), and let \(I(q)=(2\pi)^{-1}\int_0^{2\pi}q(x)\,dx\). Set
\[
x_0=\delta h,\qquad x_j=jh\ (1\le j<N),\qquad 0\le\delta<1.
\]
The nodes are distinct throughout this domain. Define \(D_m(y)=\sum_{k=-m}^{m}e^{iky}=\sin(Ny/2)/\sin(y/2)\), with the continuous extension at removable singularities. There are unique weights \(w_0,\ldots,w_{N-1}\) satisfying \(I(q)=\sum_j w_jq(x_j)\) for every \(q\in\mathcal T_m\). Define \(F_{\delta,N}=(N^{-1/2}e^{ikx_j})_{j=0,\ldots,N-1;\ k=-m,\ldots,m}\); the condition number \(\kappa_2\) is the ratio of its largest and least singular values.

## Proof

**1. Exact weights.** Write \(u_j=jh\) for the unperturbed grid. The Dirichlet cardinal identity for \(q\in\mathcal T_m\) gives
\[
q(\delta h)=\frac1N\sum_{j=0}^{N-1}D_m((\delta-j)h)q(u_j).
\]
Since \(D_m(\delta h)>0\) for \(0\le\delta<1\), solve this equation for \(q(u_0)\) and substitute into the usual trapezoidal identity \(I(q)=N^{-1}\sum_jq(u_j)\). The result is
\[
\boxed{w_0=\frac1{D_m(\delta h)},\qquad
w_j=\frac1N\left(1-\frac{D_m((\delta-j)h)}{D_m(\delta h)}\right),\quad 1\le j<N.}
\]
For \(\delta=0\), the formula has its continuous value \(w_j=1/N\). Distinctness of nodes makes the square Fourier–Vandermonde matrix invertible, proving uniqueness. Exactness on constants implies \(\sum_jw_j=1\).

**2. Exact sign frontier.** For \(0<\delta<1\), the Dirichlet formula gives
\[
\frac{D_m((\delta-j)h)}{D_m(\delta h)}
=(-1)^{j+1}\frac{\sin(\pi\delta/N)}{\sin(\pi(j-\delta)/N)},
\quad 1\le j<N.
\]
All denominators are positive. Thus each even-indexed fixed node \(j\ge2\) has \(w_j>1/N\). For odd \(j\ge3\), the circular distance \(\min\{j-\delta,N-j+\delta\}\) is strictly greater than \(\delta\). Because the sine on \((0,\pi)\) strictly increases with distance to the nearer endpoint, \(0<D_m((\delta-j)h)/D_m(\delta h)<1\); hence \(0<w_j<1/N\). Only \(w_1\) can change sign, and its exact formula is
\[
w_1=\frac1N\left(1-\frac{\sin(\pi\delta/N)}{\sin(\pi(1-\delta)/N)}\right).
\]
The sine arguments both lie in \((0,\pi/3)\), so the ratio is strictly increasing in \(\delta\), equals one precisely at \(\delta=1/2\), and is larger than one thereafter. This proves all the sign assertions. Since \(\sum_jw_j=1\), the sharp \(\ell^\infty\) norm of the quadrature functional is \(\sum_j|w_j|=1+2\max\{0,-w_1\}\), exactly the displayed formula for \(\Lambda_N\). Equality is attained by taking the sample values to be the signs of the nonzero weights, with any value of modulus at most one at a zero weight.

**3. Complete Fourier singular spectrum.** The unperturbed matrix \(F_{0,N}\) is unitary, and the perturbed matrix replaces only its zeroth row. All rows have unit norm, and the remaining \(N-1\) rows remain orthonormal. The inner product of the new row with the old zeroth row has absolute value \(c_N(\delta)=D_m(\delta h)/N\). Consequently its squared projection onto the span of the other \(N-1\) rows is \(1-c_N(\delta)^2\). In an orthonormal coordinate system adapted to this projection, the row Gram matrix has a \(2\)-by-\(2\) block with diagonal entries one and off-diagonal modulus \(\sqrt{1-c_N(\delta)^2}\), together with an identity block of size \(N-2\). Diagonalization yields the three squared singular-value levels. For \(0<\delta<1\), \(0<c_N(\delta)<1\), and therefore
\[
\kappa_2(F_{\delta,N})=
\sqrt{\frac{1+\sqrt{1-c_N(\delta)^2}}{1-\sqrt{1-c_N(\delta)^2}}}
=\frac{1+\sqrt{1-c_N(\delta)^2}}{c_N(\delta)}.
\]
At \(\delta=0\), every singular value equals one, consistently with the continuous formulas. For fixed odd \(N\) as \(\delta\uparrow1\), \(c_N(\delta)\sim\pi(1-\delta)/(N\sin(\pi/N))\), so \(\kappa_2(F_{\delta,N})\sim2N\sin(\pi/N)/(\pi(1-\delta))\).

**4. Critical boundary layer.** Fix \(t>0\) and put \(\delta_N=1-t/N\) for sufficiently large odd \(N\). Elementary small-angle limits give
\[
\frac{\sin(\pi\delta_N/N)}{N\sin(\pi(1-\delta_N)/N)}\to\frac1t,
\qquad N c_N(\delta_N)\to t.
\]
Hence \(w_1\to-1/t\) and \(w_0\to1/t\). The exact norm formula implies \(\Lambda_N(\delta_N)\to1+2/t\); the exact condition-number formula and \(c_N\to0\) imply \(\kappa_2(F_{\delta_N,N})/N\to2/t\). All limits are along the specified odd integers and use no exchange of infinite-dimensional operator limits.

## Verification

The accompanying standalone `check.py` uses the Python standard library to verify the exact quadrature moments and signs, the row-Gram two-level reduction, the predicted quadrature amplification, and the collision-layer asymptotics for several odd grid sizes and displacement parameters. Run `python check.py` alongside this file. The reproduced output is `PASS 1896 numerical assertions`. This finite diagnostic does not establish the all-\(N\) theorem; the proof above does.

## Relationship to prior work

Chen, Lin and Zhang [1, Theorems 1.4–1.5 and Corollary 1.6, v4] study general inverse-norm and quadrature-error estimates for perturbed Fourier grids. These are not exact sign or singular-spectrum statements for a single displaced node, and the stated perturbation radius is below half a mesh. Austin and Trefethen [2] treat broadly perturbed trigonometric interpolation and quadrature, rather than an all-order exact one-node phase diagram. Yu and Townsend [3] show that *multiple*-node perturbations can generate negative weights for arbitrarily small perturbation bounds, and give general norm estimates; neither implies the exact halfway sign change when only a single node moves. The related two-node *symmetric* collision result [4] keeps all weights positive up to collision, in contrast to the single-node symmetry breaking studied here. Its weights and singular-value slope do not imply the present one-sided formulas or critical boundary layer. An equivalent calculation may occur in classical cardinal-function or single-row Vandermonde literature, and no search can certify absence of such a precedent.

## Limitations

The theorem concerns a single moving node on an odd periodic grid and the exact degree-\(m\) trigonometric space; it does not extend the sign classification to simultaneous independent node movement or even-order nonstandard frequency sets. At the excluded collision \(\delta=1\), the sampling matrix is singular and exact quadrature weights do not exist: \(D_m(x)\) vanishes at every remaining distinct node \(jh\), \(1\le j<N\), while \(I(D_m)=1\). The singular spectrum is exact only for the specified normalization. In the joint limit with fixed \(t>0\), the gap \(1-\delta_N=t/N\) is measured in mesh units; the angular gap is \(2\pi t/N^2\). Publication priority is not certified.

## References

[1] L. Chen, R. Lin, and H. Zhang, *Smallest Singular Value Estimates for Nonuniform Fourier Matrices via Periodic Nonuniform Sampling*, arXiv:2608.21960v4. https://arxiv.org/abs/2608.21960v4

[2] A. P. Austin and L. N. Trefethen, *Trigonometric Interpolation and Quadrature in Perturbed Points*, arXiv:1612.04018 (first public December 13, 2016). https://arxiv.org/abs/1612.04018

[3] A. Yu and A. Townsend, *On the Stability of Unevenly Spaced Samples for Interpolation and Quadrature*, arXiv:2202.04722 (first public February 9, 2022). https://arxiv.org/abs/2202.04722

[4] *Positive Fourier quadrature survives symmetric pair collision with a sharp singular-value law*, November 16, 2026. https://github.com/Resultary/2026/blob/main/2026/11/16/SCOPE-positive-fourier-quadrature-survives-symmetric-pair-collision-wi--92a65f43a0d4/RESULT.md
