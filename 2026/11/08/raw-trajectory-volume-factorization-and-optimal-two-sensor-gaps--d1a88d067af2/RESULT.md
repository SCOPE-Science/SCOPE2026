# Raw-trajectory volume factorization and optimal two-sensor gaps on finite cycles

## Finding

Let \(N\ge5\), \(1\le r<N/2\), and let \(C_N\) be the cycle with vertex set \(\mathbb Z/N\mathbb Z\). Its graph Fourier characters are \(e_k(x)=N^{-1/2}\exp(2\pi i kx/N)\). On the \((2r+1)\)-dimensional low-pass space \(H_r=\operatorname{span}\{e_{-r},\ldots,e_r\}\), let \(T\) act on both \(e_k\) and \(e_{-k}\) by the same **real** scalar \(\mu_k\), with \(\mu_0,\ldots,\mu_r\) pairwise distinct. In particular, \(T=h(L)\) for any real spectral function \(h\) separating the first \(r+1\) eigenvalues of the normalized cycle Laplacian.

Observe the **untreated, equally weighted space-time samples** at vertices \(0,d\), for \(1\le d<N\), and times \(0,\ldots,r\):
\[
\mathcal A_d f=\big((T^t f)(0),(T^t f)(d)\big)_{t=0}^{r}\in\mathbb C^{2r+2}.
\]
Let \(V=(\mu_j^t)_{0\le t,j\le r}\), and expand the Lagrange cardinal polynomial
\[
\ell_0(z)=\frac{\prod_{k=1}^{r}(z-\mu_k)}{\prod_{k=1}^{r}(\mu_0-\mu_k)}=\sum_{t=0}^{r}a_tz^t.
\]
Then the **raw-trajectory frame volume** factors exactly as
\[
\boxed{\det(\mathcal A_d^*\mathcal A_d)=\left(\frac2N\right)^{2r+1}(\det V)^4\left(\sum_{t=0}^{r}a_t^2\right)\prod_{k=1}^{r}\sin^2\!\left(\frac{2\pi kd}{N}\right).}
\]
The first three factors are strictly positive and independent of sensor separation. Thus recovery from the two sensors is possible precisely when the additive order of \(2d\) modulo \(N\) exceeds \(r\). Moreover, for **every** permitted real spectral evolution, the D-optimal sensor gaps are precisely the maximizers of the same sine product.

For the first nontrivial five-mode case \(r=2\), put \(g=\gcd(N,2)\), \(M=N/g\), and
\[
\alpha=\frac1\pi\arcsin\sqrt{\frac23},\qquad J=\left\lfloor M\alpha\right\rfloor.
\]
For \(u\equiv(2/g)d\pmod M\), take \(j=\min(u,M-u)\), with \(0\le u<M\). **All** D-optimal gaps are exactly those for which \(j\) is one of the at most two candidates \(J,J+1\), clipped to \(0\le j\le\lfloor M/2\rfloor\), having the larger value of
\[
F_M(j)=\sin^2\!\left(\frac{\pi j}{M}\right)\sin^2\!\left(\frac{2\pi j}{M}\right).
\]
(The rule retains both candidates in case of a tie.) Every finite cycle satisfies \(\max_d F_M(j)<16/27\), and these maxima tend to the sharp ceiling \(16/27\) with error \(O(N^{-2})\). This D-optimality differs from optimal conditioning of separately demixed spectral measurements: whenever \(6\mid N\) and \(N\ge42\), every demixed-condition-number minimizer is **strictly suboptimal** for the untreated trajectory determinant.

## Assumptions and scope

Signals and frames are complex, with counting-measure norm on vertices and ordinary Euclidean norm on the \(2r+2\) raw measurements. The real evolution scalars are allowed to be negative or zero, but must be pairwise distinct across distinct cycle eigenvalues. This excludes the Nyquist singleton, which is why \(r<N/2\) is required. The determinant is the squared \((2r+1)\)-dimensional column volume, not the smallest singular value, trace inverse, or raw-data condition number. The observation operator has one more row than column. All determinant equalities refer to this fixed normalization.

## Proof

**1. Exact demixing.** Use the real orthonormal Fourier basis \(e_0\) and \(c_k(x)=\sqrt{2/N}\cos(2\pi kx/N)\), \(s_k(x)=\sqrt{2/N}\sin(2\pi kx/N)\) for \(1\le k\le r\). Group the raw time rows by sensor, so that \(\mathcal A_d=\operatorname{diag}(V,V)\mathcal B_d\). The demixed map \(\mathcal B_d\) has one constant column with entries \(N^{-1/2}\) in the two eigenvalue-zero rows and, for each positive \(k\), a two-row, two-column block
\[
\sqrt{\frac2N}\begin{pmatrix}1&0\\ \cos\theta_k&\sin\theta_k\end{pmatrix},\qquad \theta_k=\frac{2\pi kd}{N}.
\]
Consequently
\[
\det(\mathcal B_d^*\mathcal B_d)=\left(\frac2N\right)^{2r+1}\prod_{k=1}^{r}\sin^2\theta_k.
\]
Whenever this determinant is nonzero, the unit vector \(w=(e_0,-e_0)/\sqrt2\) in the two sensor blocks spans \(\ker\mathcal B_d^*\). Here each \(e_0\) denotes the coordinate vector selecting the constant-eigenvalue row in \(\mathbb C^{r+1}\).

**2. Rectangular determinant transport.** If \(B\) is an \((m+1)\)-by-\(m\) full-rank matrix, \(R\) is invertible square of size \(m+1\), and \(w\) is a unit vector spanning \(\ker B^*\), the cofactor-vector form of Cauchy–Binet gives
\[
\det(B^*R^*RB)=|\det R|^2\det(B^*B)\,\|R^{-*}w\|_2^2.
\]
Indeed the signed maximal minors form a vector of squared norm \(\det(B^*B)\), parallel to \(w\); under \(R\) the vector transforms by \((\det R)R^{-*}\). Apply this with \(R=\operatorname{diag}(V,V)\). Because \(V\) is real,
\[
|\det R|^2=(\det V)^4,\qquad \|R^{-*}w\|_2^2=\|V^{-T}e_0\|_2^2.
\]
The coefficient vector \((a_0,\ldots,a_r)^T\) obeys \(V^T a=e_0\), since \(\ell_0(\mu_j)=\mathbf1_{j=0}\). Hence \(\|V^{-T}e_0\|_2^2=\sum_ta_t^2\), proving the formula. Both sides vanish when any \(\sin\theta_k=0\), so the identity also holds in singular cases by continuity (or directly from the rank of \(\mathcal B_d\)). This is an exact finite-dimensional identity, not an inference from numerical rank experiments.

**3. Observability arithmetic.** A sine factor vanishes if and only if \(N\mid2kd\). The smallest positive such \(k\) is \(N/\gcd(N,2d)\), the additive order of \(2d\) modulo \(N\). Thus the stated strict order criterion is necessary and sufficient.

**4. Complete five-mode placement.** For \(r=2\), folding the angle modulo reflection around \(\pi/2\) reduces the product to \(F_M(j)\) on \(0\le j\le\lfloor M/2\rfloor\). For \(0\le\theta\le\pi/2\),
\[
F(\theta)=\sin^2\theta\sin^2(2\theta)=4y^2(1-y),\qquad y=\sin^2\theta.
\]
The derivative \(8y-12y^2\) is positive for \(0<y<2/3\) and negative for \(2/3<y<1\), so the unique continuous maximum occurs at \(\theta_*=\arcsin\sqrt{2/3}\), with value \(16/27\). Since the grid is ordered, every discrete maximizer lies at one of the two grid points bracketing \(\theta_*\), proving the exact two-candidate rule (including boundary clipping). The continuous maximum cannot lie on any finite grid: otherwise \(\cos(2\theta_*)=-1/3\), whereas \(2\cos(2\pi j/M)\) is an algebraic integer, and the rational number \(-2/3\) is not an integer.

The identity
\[
F(\theta)=\frac14-\frac18\cos(2\theta)-\frac14\cos(4\theta)+\frac18\cos(6\theta)
\]
shows \(|F''(\theta)|\le9\) everywhere. A nearest grid point is within \(\pi/(2M)\) of \(\theta_*\), so Taylor's theorem gives \(0<16/27-\max_jF_M(j)\le9\pi^2/(8M^2)=O(N^{-2})\).

**5. Separation from spectral-demixed conditioning.** For \(r=2\), the two demixed positive-frequency Gram blocks have eigenvalues \((2/N)(1\pm|\cos\theta|)\) and \((2/N)(1\pm|\cos2\theta|)\). Their condition number is minimized exactly at \(\theta\equiv\pm\pi/3\pmod\pi\), where the larger cosine modulus is \(1/2\). If \(6\mid N\), these positions occur on the actual sensor grid and have \(F=9/16\). For even \(N\), a grid angle lies within \(\pi/N\) of \(\theta_*\); Taylor's theorem then gives a sampled value at least \(16/27-9\pi^2/(2N^2)\), strictly greater than \(9/16\) for \(N\ge42\), using \(\pi^2<10\). Hence no optimal demixed-conditioning placement maximizes the raw determinant in that range.

## Verification

The standalone dependency-free `CHECK.py` directly constructs the untreated space-time sampling matrices, computes Gram volumes independently from sums of squared maximal minors, and compares those volumes with the factored expression for 801 choices of \(N,r,d\). It also checks the two-candidate five-mode rule on 496 graph sizes and the separation from demixed conditioning for 78 sizes divisible by six. These floating-point checks are supplemental; the cofactor identity, monotonicity, arithmetic criterion, and finite-grid bounds are proved above for all allowed parameters. Run `python3 CHECK.py` from the same directory.

## Relationship to prior work

Cabrelli, Cordero, Bulai, Saliani and Molter's 2026 graph Paley–Wiener dynamical-sampling preprint motivates studying graph bandlimits and ordinary time-orbit measurements; its available abstract describes finite-path numerical experiments, not the cycle volume theorem here. A closely related published result, *Sharp spectral-demixed two-sensor frame bounds on finite cycles*, exactly optimizes **demixed** lower/upper frame bounds and gives a spectral Vandermonde recovery step. Its full `RESULT.md` explicitly distinguishes that output norm from untreated time-trajectory data and does not establish a raw-trajectory determinant factorization or the five-mode raw D-optimal placement rule. The present cofactor transport law handles the nonunitary time Vandermonde with one surplus measurement; the last theorem also shows that the resulting optimum generally differs from the demixed condition-number optimum. Aldroubi and collaborators' 2024 work gives general graph space-time recovery criteria and numerical noisy-placement methods, not this exact cycle volume invariant. The Vandermonde and trigonometric ingredients are standard and are not claimed independently as new.

## Limitations

The theorem concerns precisely two sensors, consecutive times, low-pass cutoff below Nyquist, real spectrally separating evolutions, and the **determinant** of the untreated observation Gramian. It does not determine its smallest singular value, condition number, or noise-optimal mean squared error. The graph Paley–Wiener motivating preprint could not be read in full during this comparison: the arXiv and alternate public full-text routes failed, and institutional download was unavailable. An unindexed prior derivation of this exact raw-volume law remains possible. No independent mathematical audit or publication-priority certification is asserted.

## References

- C. Cabrelli, E. Cordero, I. M. Bulai, S. Saliani, U. Molter, *Dynamical Sampling in Graph Paley–Wiener Spaces*, arXiv:2609.25472, first public 2026-09-21, https://arxiv.org/abs/2609.25472.
- *Sharp spectral-demixed two-sensor frame bounds on finite cycles*, publicly available research record (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-sharp-spectral-demixed-two-sensor-frame-bounds-on-finite-cycles--b03d8e4c7818/RESULT.md.
- A. Aldroubi, V. Bailey, I. A. Krishtal, B. Miller, A. Petrosyan, *Reconstructing Graph Signals from Noisy Dynamical Samples*, arXiv:2411.12670, https://arxiv.org/abs/2411.12670.
- G. Yang, L. Yang, C. Huang, *An Orthogonal Partition Selection Strategy for the Sampling of Graph Signals with Successive Local Aggregations*, Signal Processing 188 (2021), 108211, https://doi.org/10.1016/j.sigpro.2021.108211.
