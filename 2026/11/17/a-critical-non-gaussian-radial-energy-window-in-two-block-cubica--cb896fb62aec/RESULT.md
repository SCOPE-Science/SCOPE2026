# A critical non-Gaussian radial-energy window in two-block cubical joins

## Finding

For integers \(p,q\ge1\) with \(N=p+q\), define the canonical Euclidean cubical join
\[
K_{p,q}=\operatorname{conv}\bigl(([-1,1]^p,0),(0,[-1,1]^q)\bigr)
=\{(x,y):\|x\|_\infty+\|y\|_\infty\le1\}\subset\mathbb R^N.
\]
Let \(X_N\) be uniform in its \(N\)-dimensional volume, write \(T_N=\|X_N^{(p)}\|_\infty\), \(U_N=\|X_N^{(q)}\|_\infty\), and set
\[
F_N=\frac{\|X_N\|_2^2}{N},\qquad
C_N=\mathbb E(F_N\mid T_N,U_N),\qquad m_{p,q}=\mathbb E F_N.
\]
The exact conditional and unconditional means are
\[
C_N=\frac{(p+2)T_N^2+(q+2)U_N^2}{3N},\qquad
m_{p,q}=\frac{p(p+1)(p+2)+q(q+1)(q+2)}{3N(N+1)(N+2)}.
\tag{1}
\]
If \(p=p_N\), \(q=q_N\), and \(p_N/N\to\alpha\in(0,1)\), then
\[
\sqrt N\,(F_N-m_{p,q})\ \Longrightarrow\
\mathcal N\left(0,\,\frac4{45}\left[1-15\alpha^2(1-\alpha)^2\right]\right).
\tag{2}
\]
Its variance is minimized uniquely at \(\alpha=1/2\), where it is \(1/180\).
Away from equal block proportions, the radial information retained by just the two block maxima has its own normal law:
\[
\alpha\ne\tfrac12:\qquad
\sqrt N\,(C_N-m_{p,q})\ \Longrightarrow\
\mathcal N\left(0,\frac49\alpha(1-\alpha)(2\alpha-1)^2\right).
\tag{3}
\]
At balance the linear fluctuation vanishes, and the **sharp critical window is of order \(\sqrt N\) in the block-size difference**. For any real \(\kappa\), if \((p_N-q_N)/\sqrt N\to\kappa\), then
\[
N(C_N-m_{p,q})\ \Longrightarrow\
\boxed{\frac{Z^2-1+4\kappa Z}{12}-\frac{E-1}{6}},
\tag{4}
\]
where \(Z\sim\mathcal N(0,1)\), \(E\sim\operatorname{Exp}(1)\), and \(Z\) and \(E\) are independent. The right side is centered, non-Gaussian (including at \(\kappa=0\)), and has variance \(1/24+\kappa^2/9\). This is a transition in the conditional radial-energy observable, **not** a transition in the raw squared radius: (2) remains Gaussian even at balance.

## Assumptions and scope

All metrics and volumes are the standard ambient Euclidean ones. The two cube blocks occupy perpendicular coordinate subspaces and have side length two; no affine normalization is applied. The random point is Lebesgue-volume-uniform, not vertex-uniform. For exact identities (1), \(p,q\) are arbitrary positive integers. For asymptotic (2) and (3), both block sizes grow proportionally to \(N\) with a limit \(\alpha\in(0,1)\). The centered mean \(m_{p,q}\) must be the exact finite-size expression: replacing it by a fixed limiting mean is not justified for arbitrary rates of approach of \(p_N/N\).

## Proof

**1. Polytope, radial coordinates, and sampling.** The equality of the convex-hull and norm descriptions follows by writing a point with \(\|x\|_\infty=t\), \(\|y\|_\infty=u\), \(t+u\le1\), as a convex combination of points in the two cube blocks. The upper-volume of the \(p\)-cube of maximum norm at most \(t\) is \((2t)^p\), so a change to block maxima gives the joint density proportional to \(t^{p-1}u^{q-1}\) on \(t,u\ge0\), \(t+u\le1\). Hence
\[
(T_N,U_N,S_N)\sim\operatorname{Dirichlet}(p,q,1),\quad S_N=1-T_N-U_N.
\tag{5}
\]
In particular \(\operatorname{vol}(K_{p,q})=2^Np!q!/N!\).

Conditioned on the two maxima, the coordinate-signs are independent fair signs; in each block exactly one coordinate has absolute value the block maximum, its location is uniform, and the other coordinates are independent uniforms between minus and plus that maximum. The tie set has zero volume. Each block therefore has conditional squared-norm mean \(\frac{n+2}{3}t^2\) and conditional squared-norm variance \(\frac{4(n-1)}{45}t^4\). This proves the first equation of (1). Using the Dirichlet second moments \(\mathbb ET_N^2=p(p+1)/((N+1)(N+2))\) and its \(q\)-analogue proves the second.

**2. Normal law for total radial energy.** Introduce
\[
W_N=\frac{T_N}{T_N+U_N},\quad S_N=1-T_N-U_N.
\]
The beta-Dirichlet factorization gives independent \(W_N\sim\operatorname{Beta}(p,q)\), \(S_N\sim\operatorname{Beta}(1,N)\). Thus for \(p/N\to\alpha\) we have \(\sqrt N(W_N-p/N)\Longrightarrow \mathcal N(0,\alpha(1-\alpha))\), and \(S_N=O_{\mathsf P}(1/N)\). By the delta method, the conditional mean has the Gaussian limit (3) whenever \(\alpha\ne1/2\), since the derivative of \([\alpha w^2+(1-\alpha)(1-w)^2]/3\) at \(w=\alpha\) is \(2(2\alpha-1)/3\).

Conditional on \(T_N,U_N\), the centered square-energy is a sum of \(p-1\) independent copies of \(T_N^2(V^2-1/3)\) and \(q-1\) independent copies of \(U_N^2(V^2-1/3)\), scaled by \(1/N\), where \(V\sim\operatorname{Uniform}[-1,1]\). Since \(\operatorname{Var}(V^2)=4/45\), bounded triangular-array Lindeberg convergence and convergence of the maxima show
\[
\sqrt N(F_N-C_N)\Longrightarrow\mathcal N\left(0,\frac4{45}[\alpha^5+(1-\alpha)^5]\right).
\]
The conditional characteristic functions converge in probability to a nonrandom Gaussian characteristic function. The limiting noise is consequently independent of the beta fluctuation controlling \(C_N\). Adding the independent variances proves (2), because
\[
\frac4{45}[\alpha^5+(1-\alpha)^5]
+\frac49\alpha(1-\alpha)(2\alpha-1)^2
=\frac4{45}[1-15\alpha^2(1-\alpha)^2].
\]
The product \(\alpha(1-\alpha)\) is uniquely maximized at \(1/2\), proving the stated uniqueness of the variance minimum.

**3. Exact second-order critical expansion.** Let \(d_N=p-q\), \(\delta_N=W_N-1/2\). The identity
\[
C_N=\frac{(1-S_N)^2}{3N}\left(\frac{N+4}{4}+d_N\delta_N+(N+4)\delta_N^2\right)
\tag{6}
\]
is exact. Under \(d_N/\sqrt N\to\kappa\), the independent beta and slack limits are
\[
\sqrt N\,\delta_N\Longrightarrow\frac{\kappa+Z}{2},\qquad NS_N\Longrightarrow E,
\]
independently, and the exact mean expands to
\[
m_{p,q}=\frac1{12}+\frac{1+\kappa^2}{4N}+o(1/N).
\]
Insert these into (6) and expand the products through order \(1/N\). All deterministic \(\kappa^2\) terms cancel after centering, giving precisely (4). The variance formula follows from independence and \(\operatorname{Var}(Z^2)=2\), \(\operatorname{Var}(E)=1\), and \(\operatorname{Cov}(Z^2,Z)=0\). The limit is non-Gaussian for every \(\kappa\), since its fourth cumulant is strictly positive and equals \( (3+16\kappa^2)/432\); this follows from the independent noncentral-chi-square and exponential summands. This proves the sharp critical-window assertion.

## Verification

The attached standalone `verify_two_cube_radial.py` computes the exact first and second moments of \(F_N\) and \(C_N\) using rational Dirichlet moments and conditional uniform-coordinate laws. It reports `PASS 276 exact/statistical assertions`. It independently samples points through a gamma-Dirichlet representation and tests the moments at selected finite dimensions; it also checks the large-dimension limiting variances numerically. The numerical tests are diagnostics; the universal and asymptotic assertions follow from the preceding analytic derivation. Run `python verify_two_cube_radial.py` with Python 3 and NumPy.

## Relationship to prior work

The 2026 paper of Mori, Motomura, Ohsugi and Tsuchiya gives an algebraic framework for unconditional lattice polytopes associated to anti-blocking polytopes. Its verified May 19, 2026 public posting motivates this symmetric stable-set instance; the publicly accessible abstract emphasizes toric normality and quadratic generators, not Euclidean radial laws. The full text was unavailable at this inspection, so no whole-paper negative coverage claim is made.

The previously published *Sharp isotropic-constant range of all Hanner polytopes* gives the exact volume and covariance transformation laws for perpendicular \(\ell_1\)-sums, and those known finite-dimensional facts are not claimed as new. The previously published *Complete moment law and covariance-sign recovery for multipartite stable-set polytopes* contains an all-degree moment formula for the positive-coordinate (nonnegative) joins. Absolute-square moments of the unconditional joins can be obtained from that formula, so their mere existence is not claimed as original. Neither inspected work states the double-scaling transition of the **conditional** energy at the balanced block split, or the independent quadratic-Gaussian and exponential limit in (4). That critical limit and its contrast with (2) are the asserted contribution. A differently phrased unpublished or earlier probabilistic result remains a priority risk.

## Limitations

This is an asymptotic distributional theorem for exactly two orthogonal cube blocks; it is not a universal radial-shell theorem for general unconditional polytopes or arbitrary graph stable-set polytopes. The non-Gaussian law concerns a conditional expectation, not the raw Euclidean norm. Its Gaussian/exponential components follow from beta and slack fluctuations; no finite-dimensional distributional equality to the limiting law is claimed. Priority is based on checked records and accessible materials, not an exhaustive independent certification. No independent mathematical audit has been performed.

## References

1. K. Mori, R. Motomura, H. Ohsugi and A. Tsuchiya, *Algebraic aspects of unconditional lattice polytopes*, arXiv:2605.19586, first public May 19, 2026, https://arxiv.org/abs/2605.19586.
2. *Sharp isotropic-constant range of all Hanner polytopes*, full available research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-isotropic-constant-range-of-all-hanner-polytopes--7976b0937cd2.
3. *Complete moment law and covariance-sign recovery for multipartite stable-set polytopes*, full available research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-moment-law-and-covariance-sign-recovery-for-multipartit--e8f71c4a8c8b.
