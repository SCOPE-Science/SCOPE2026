# A sharp five-lag threshold for the logarithmic clock of critical sine-memory dynamics

## Finding
Fix any integer \(m\ge1\) and nonnegative weights \(w_0,\ldots,w_m\) satisfying \(w_0>0\), \(w_m>0\), and \(\sum_{j=0}^m w_j=1\). For arbitrary real initial values \(z_{-m},\ldots,z_0\), define
\[
z_{n+1}=\sum_{j=0}^m w_j\sin(z_{n-j}),\qquad n\ge0.
\]
Every real trajectory converges to zero. For every strictly positive initial history \(0<z_{-j}\le1\) (all \(0\le j\le m\)), set
\[
\mu=\sum_{j=0}^m j w_j,\qquad \nu=\sum_{j=0}^m j^2w_j,\qquad W=1+\mu.
\]
There is a finite initial-history-dependent real constant \(C\) such that
\[
\boxed{\quad z_n^{-2}=\frac{n}{3W}+K\log n+C+o(1),\quad K=\frac{9\mu^2+8\mu+4-5\nu}{20W^2}.\quad}
\]
In particular \(\sqrt n\,z_n\to\sqrt{3W}\). The leading coefficient depends only on mean lag \(\mu\); the logarithmic coefficient also depends on the second moment \(\nu\).

The sign of \(K\) admits a sharp delay-horizon classification. If \(m\le3\), necessarily \(K>0\). If \(m=4\), then \(K\ge0\), with equality **only** for \(w_0=5/6\), \(w_4=1/6\), and the other weights zero. Negative \(K\) is possible for the first time at maximum active lag \(m=5\): the weights \(w_0=4/5\), \(w_5=1/5\) have \(K=-1/20\). For comparison, the two-lag weights \(w_0=w_2=1/2\) have the **same** mean lag \(\mu=1\), hence the same leading rate \(n/6\), but \(K=11/80>0\).

## Assumptions and scope
This is a deterministic, exact-real, finite-memory recurrence; \(m\) is fixed before taking \(n\to\infty\). Weights are constant, sum to one, and include strictly positive immediate and maximal-delay terms. The full asymptotic expansion is asserted for strictly positive histories bounded by one; global convergence alone applies to arbitrary real histories. By odd symmetry, negative histories in \([-1,0)^{m+1}\) have the same inverse-square formula. No uniformity as \(m\to\infty\), as weights approach a reducible boundary, or over initial histories is asserted.

The model is the positive critical-feedback restriction of the three-dimensional sine map reported in Almatroud et al. (2024). In that displayed map, writing \((x_{n+1},y_{n+1},z_{n+1})=(y_n,\sin z_n,\beta_1x_n+\beta_2y_n-\gamma\sin z_n)\) gives, after elimination of the two lag coordinates, the case \(m=2\) with \((w_0,w_1,w_2)=(-\gamma,\beta_2,\beta_1)\) when these entries are nonnegative and \(\beta_1+\beta_2-\gamma=1\). The higher-memory recurrence is a mathematically defined extension of this displayed map.

## Proof
**1. Global extinction.** Every newly generated value has modulus at most one. After \(m+1\) steps, the entire lag window is contained in \([-1,1]\). On this interval \(|\sin t|\le\sin|t|<|t|\) for nonzero \(t\). Let \(M_n=\max_{0\le j\le m}|z_{n-j}|\). Then \(M_{n+1}\le M_n\), and after \(m+1\) further steps \(M_{n+m+1}\le\sin M_n\). The limit of the decreasing window maxima is therefore zero. Positive initial histories remain positive and at most one.

**2. A non-exponential positive orbit.** For positive histories write \(a_n=\min_{0\le j\le m}z_{n-j}\). The positivity and monotonicity of sine on \([0,1]\) give \(a_{n+1}\ge\sin a_n\), while the preceding block estimate gives \(M_{n+m+1}\le\sin M_n\). Since \(\sin t=t-t^3/6+O(t^5)\) as \(t\downarrow0\), comparison with the scalar sine iteration yields \(c_1n^{-1/2}\le a_n\le M_n\le c_2n^{-1/2}\) for sufficiently large \(n\), with positive history-dependent constants. In particular no such orbit decays exponentially.

**3. The center mode.** The linearized companion matrix has characteristic polynomial
\[
P(\lambda)=\lambda^{m+1}-\sum_{j=0}^m w_j\lambda^{m-j}.
\]
It has a simple unit eigenvalue \(1\) since \(P'(1)=1+\mu>0\). All other roots are strictly in the unit disk: the modulus inequality rules out roots outside it, and equality on the circle, together with \(w_0>0\), forces \(\lambda=1\). Thus the origin has one center direction, along \((1,\ldots,1)\), and a uniformly contracting complementary subspace for each fixed weight vector. A finite-order smooth center manifold with local stable fibers exists. Each sufficiently small forward orbit has an exponentially close orbit on that manifold. For positive histories the polynomial lower bound from step 2 excludes the zero center orbit as shadow, and the shadow is eventually positive. This transfer permits calculation of the asymptotic from the scalar center coordinate without changing its constant or remainder.

**4. Fifth-order center reduction.** Use the newest lag value \(t\) as a coordinate on the center manifold and write its return as \(f(t)=t+At^3+Bt^5+O(t^7)\). Oddness makes the finite Taylor jet odd. The past lags on this manifold are \(f^{-j}(t)\), for which formal composition, valid for each fixed integer \(j\), gives
\[
f^{-j}(t)=t-jAt^3+\left[\frac{3j(j+1)}2A^2-jB\right]t^5+O(t^7).
\]
Substitution into \(f(t)=\sum_jw_j\sin(f^{-j}(t))\), and comparison of cubic and fifth-order coefficients, yields
\[
A=-\frac1{6W},\qquad
B=\frac{\mu+\nu}{24W^3}-\frac{\mu}{12W^2}+\frac1{120W}.
\]
These coefficients are determined by the invariant-manifold equation itself, rather than by a numerical fit.

**5. Summable clock remainder.** For the positive center orbit,
\[
f(t)^{-2}-t^{-2}=-2A+(3A^2-2B)t^2+O(t^4).
\]
Step 2 implies \(t_n\asymp n^{-1/2}\), so first summation shows \(t_n^{-2}=n/(3W)+O(\log n)\) and hence \(t_n^2=3W/n+O(\log n/n^2)\). A second summation now has a summable remainder and gives a finite limit after subtraction of \(n/(3W)\) and \(K\log n\), with
\[
K=3W(3A^2-2B)=\frac{9\mu^2+8\mu+4-5\nu}{20W^2}.
\]
The exponentially small difference from the actual positive orbit does not affect this limit.

**6. Sharp horizon and cancellation.** Because \(j^2\le mj\) on \(0\le j\le m\), \(\nu\le m\mu\). Thus the numerator of \(20W^2K\) is at least \(9\mu^2+(8-5m)\mu+4\). For \(m\le3\), this expression is strictly positive for all \(\mu\ge0\). For \(m=4\), it equals \((3\mu-2)^2\), and equality in \(\nu\le4\mu\) requires support only at lags zero and four, while \(\mu=2/3\) fixes the unique weights claimed. For \(m=5\), the explicit weights \((w_0,w_5)=(4/5,1/5)\) give \(\mu=1\), \(\nu=5\), and \(K=-1/20\). This proves both the cutoff and its attainability.

## Verification
The accompanying `checker.py` reconstructs the moment formulas exactly using rational arithmetic, checks the cubic and quintic coefficient identities, verifies positive/negative/zero logarithmic examples, and runs finite double-precision trajectories. At 100,000, 200,000, and 400,000 steps, the corrected inverse-square residuals stabilize while the uncorrected residuals show the predicted logarithmic trend. These finite diagnostics are not a proof of the infinite-time statements; the proof is the analysis above.

## Relationship to prior work
Almatroud et al. (2024) introduce the three-dimensional sine map, discuss fixed-point stability, and investigate numerical chaos and stabilization. Their displayed recurrence motivates the finite-memory family, but their reported results do not contain a moment-sensitive parabolic clock or its five-lag sign threshold. Garab and Pötzsche (2018) develop Morse decompositions for delay-difference equations and establish a broad qualitative context; their relevant statements address global attractors rather than this two-term inverse-square asymptotic. Standard center-manifold theory supplies the reduction method, not the specific delay-moment coefficient. Related published continuous-time critical sine/Ikeda delay results involve different evolution operators and do not yield this discrete logarithmic coefficient merely by changing notation. The novelty assessment is limited to the literature and indexed claims inspected; equivalent unindexed work remains possible.

## Limitations
The fine clock is not asserted for arbitrary sign-changing initial data, including exceptional strong-stable orbits. The proof requires a fixed finite memory with strictly positive immediate and maximal-lag weights; it does not cover variable/infinite delay or stochastic perturbation. The zero coefficient cancels only the logarithm and does not imply finite-time convergence. No result about chaos, synchronization under forcing, or finite-precision implementations follows. Independent verification has not been performed.

## References
1. O. A. Almatroud, M. Abu Hammad, A. Dababneh, L. Diabi, A. Ouannas, A. A. Khennaoui, S. Alshammari, "Multistability, Chaos, and Synchronization in Novel Symmetric Difference Equation," *Symmetry* **16** (2024), 1093; published 2024-08-22. https://doi.org/10.3390/sym16081093.
2. Á. Garab and C. Pötzsche, "Morse Decompositions for Delay-Difference Equations," *Journal of Dynamics and Differential Equations* **31** (2019), 903–932; first online 2018-07-07. https://doi.org/10.1007/s10884-018-9685-8.
3. J. Carr, *Applications of Centre Manifold Theory*, Springer, 1981, for standard center-manifold and stable-fiber methods. The finite-jet invariance computation used here is displayed in full above.
