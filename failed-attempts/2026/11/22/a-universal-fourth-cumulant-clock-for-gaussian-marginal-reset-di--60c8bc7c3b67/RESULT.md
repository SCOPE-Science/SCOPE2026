# A universal fourth-cumulant clock for Gaussian-marginal reset diffusion

## Finding
A stationary multivariate diffusion can have exactly Gaussian single-time observations and exactly the covariance of an ordinary Gaussian Ornstein–Uhlenbeck process, while independent Poisson refreshes are nonetheless recoverable from a *single* fourth-order, two-time observation. For every integer \(d\ge2\), let \(C_{ik}(t)=\mathbb E[X_i(0)X_k(t)]\), and write \(K_{ijkl}(t)=\operatorname{cum}(X_i(0),X_j(0),X_k(t),X_l(t))\). For the non-Gaussian-reset class defined below, at each \(t>0\),
\[
\boxed{K_{ijkl}(t)=(e^{rt}-1)\bigl(C_{ik}(t)C_{jl}(t)+C_{il}(t)C_{jk}(t)\bigr).}
\]
In particular, \(C(t)\) is invertible, and its contraction with the connected fourth-order tensor determines the reset intensity with no knowledge of the drift matrix, diffusion matrix or refresh distribution:
\[
\boxed{r=\frac1t\log\left(1+\frac1{d(d+1)}\sum_{i,j,k,l=1}^{d}K_{ijkl}(t)[C(t)^{-1}]_{ki}[C(t)^{-1}]_{lj}\right).}
\]
Every \(r>0\) in this class produces a strictly positive fourth-cumulant witness for suitable linear probes, even though every one-time cumulant of order greater than two vanishes. An ordinary Gaussian Ornstein–Uhlenbeck process can have precisely the same stationary one-time law and every two-time covariance, but its connected fourth moments vanish.

## Assumptions and scope
Fix an integer \(d\ge2\), a real \(d\times d\) matrix \(A\) with eigenvalues of strictly positive real part, a symmetric positive-definite diffusion matrix \(D\), and \(r>0\). Between reset events the entire state follows
\[
 dX_t=-AX_t\,dt+\sqrt{2D}\,dW_t.
\]
A state-independent Poisson clock of rate \(r\), independent of the Brownian noise, replaces the entire position vector at each event by a fresh independent draw from a fixed Borel law \(\rho\), independent of past states and events. Assume that \(\rho\) is genuinely non-Gaussian, and the process is stationary with exact marginal law \(N(0,\Sigma)\) for a positive-definite \(\Sigma\). The existence of such inputs is established constructively below; this theorem does not claim the general stationary-Gaussian feasibility characterization already available in the literature. The measured correlations and cumulants are ensemble quantities, not empirical estimators. The convention \(D\) is the coefficient of \(\operatorname{tr}(D\nabla^2)\) in the generator.

## Proof
**1. Renewal decomposition and covariance.** Let \(E_t\) denote the event of no reset in \((0,t]\). Its probability is \(p=e^{-rt}\), independently of \(X_0\). On \(E_t\),
\[
 X_t=H_tX_0+Z_t,\qquad H_t=e^{-At},
\]
where \(Z_t\) is centered Gaussian, independent of the centered Gaussian \(X_0\). Thus the no-reset pair is jointly Gaussian with cross-covariance \(B(t)=\Sigma H_t^{\mathsf T}\). On \(E_t^c\), a last independent refresh severs all dependence between \(X_0\) and \(X_t\). The stationary mean is zero, so
\[
 C(t)=pB(t)=e^{-rt}\Sigma e^{-A^{\mathsf T}t}.
\]
This matrix is invertible because \(\Sigma\) and the matrix exponential are invertible.

**2. The connected fourth tensor.** Let \(S^{(0)}(t)=\mathbb E[X_tX_t^{\mathsf T}\mid E_t]\) and \(S^{(1)}(t)=\mathbb E[X_tX_t^{\mathsf T}\mid E_t^c]\). By stationary Gaussianity, \(pS^{(0)}+(1-p)S^{(1)}=\Sigma\). On \(E_t\), Isserlis' identity for the jointly Gaussian pair gives
\[
 \mathbb E[X_i(0)X_j(0)X_k(t)X_l(t)\mid E_t]
 =\Sigma_{ij}S^{(0)}_{kl}+B_{ik}B_{jl}+B_{il}B_{jk}.
\]
On \(E_t^c\), the earlier Gaussian state and the later state are independent, giving \(\Sigma_{ij}S^{(1)}_{kl}\). Combining these contributions,
\[
 \mathbb E[X_i(0)X_j(0)X_k(t)X_l(t)]
 =\Sigma_{ij}\Sigma_{kl}+p(B_{ik}B_{jl}+B_{il}B_{jk}).
\]
Subtract the three covariance pairings that define the centered fourth joint cumulant. Since \(C=pB\), the remaining pairings have coefficient \(p-p^2=p^2(e^{rt}-1)\), proving the boxed identity. No Gaussian assumption about the reset-conditioned later state was used.

**3. Universal clock reconstruction and strict detection.** In the contraction in the second box, the first Wick pairing contributes \(d^2\) and the second contributes \(d\), since \(\sum_k C_{ik}[C^{-1}]_{kj}=\delta_{ij}\). Consequently the sum is \(d(d+1)(e^{rt}-1)\); logarithmic inversion gives the rate. For real vectors \(u,v\),
\[
 \operatorname{cum}(u^{\mathsf T}X_0,u^{\mathsf T}X_0,v^{\mathsf T}X_t,v^{\mathsf T}X_t)
 =2(e^{rt}-1)(u^{\mathsf T}C(t)v)^2\ge0.
\]
Because \(C(t)\) is invertible, some choice of \(u,v\) makes this expression strictly positive.

**4. Covariance-matched Gaussian process.** The stationarity equation forces the reset density \(\rho=g_\Sigma-r^{-1}L^*g_\Sigma\), where \(g_\Sigma\) is the target Gaussian density. The quadratic coefficient of \(\rho/g_\Sigma\), in the coordinate \(\Sigma^{-1}x\), is \(Q=(A\Sigma+\Sigma A^{\mathsf T})/2-D\). Nonnegativity of \(\rho\) on all rays forces \(Q\succeq0\). Define \(\widetilde A=A+rI_d\), \(\widetilde D=(A\Sigma+\Sigma A^{\mathsf T})/2+r\Sigma=D+Q+r\Sigma\succ0\). The ordinary stationary Gaussian Ornstein–Uhlenbeck process with drift \(-\widetilde A\) and diffusion \(\widetilde D\) has stationary covariance \(\Sigma\), since \(\widetilde A\Sigma+\Sigma\widetilde A^{\mathsf T}=2\widetilde D\). Its two-time covariance equals \(\Sigma e^{-\widetilde A^{\mathsf T}t}=C(t)\) at all nonnegative lags. Its entire path is Gaussian, so its fourth connected tensor vanishes, in strict contrast to Step 3.

**5. Non-vacuity with non-Gaussian refreshes in every dimension.** Choose arbitrary \(d\ge2\), \(\kappa,D_0,r>0\) and a number \(\delta\) satisfying \(0<\delta<\min\{\kappa,r/d\}\). Put \(s=D_0/(\kappa-\delta)\). For the isotropic drift \(A=\kappa I_d\), diffusion \(D=D_0I_d\), and target density \(g_s=N(0,sI_d)\), choose
\[
 \rho(x)=g_s(x)\left[1-\frac{d\delta}{r}+\frac{\delta\lVert x\rVert^2}{rs}\right].
\]
The bracket is everywhere strictly positive and its Gaussian average is one. The forward Ornstein–Uhlenbeck generator satisfies \(L^*g_s=\delta(d-\lVert x\rVert^2/s)g_s\), so \(L^*g_s-rg_s+r\rho=0\). Therefore the unique invariant law is exactly \(g_s\), but \(\rho\) is non-Gaussian for \(\delta>0\). It follows that the fourth-tensor identity applies to genuine non-Gaussian resets, not just equilibrium-Gaussian rethermalization.

## Verification
The companion `verify.py` uses the reset-augmented polynomial generator and matrix exponentials to compute mixed two-time moments for three non-Gaussian scalar calibration cases, then tests the full cumulant relation independently. A separate nonsymmetric two-dimensional drift case, a nonisotropic Gaussian target and positive non-Gaussian source are tested using the direct no-event/event four-moment decomposition, numerical matrix exponentials, and the full index contraction. The checker passes 156 deterministic comparisons; those computations corroborate but do not establish the universal assertions. Run `python verify.py` with NumPy and SciPy installed.

## Relationship to prior work
Olsen (2023), arXiv:2310.04840, gives the renewal representation and complete stationary **one-time** moment recursion for Ornstein–Uhlenbeck diffusion reset to an arbitrary distribution; the renewal identity used here is standard. The published 2026 result *Exact Gaussian stationary-state engineering by non-Gaussian stochastic resets* already characterizes the permissible Gaussian invariant measures, their unique non-Gaussian reset distributions, and their stationary lag covariance. None of those existence, uniqueness, source-design or covariance formulas is a novelty claim here.

The published result *Gaussian covariance twins and displacement-only identification of Poisson-rethermalized Ornstein–Uhlenbeck motion* establishes the **scalar equilibrium-Gaussian rethermalization special case** and an integrated-displacement inverse theorem. The special case is explicitly covered by that work, not claimed separately. The present contribution is the exact **full arbitrary-dimension tensor identity and one-lag contraction** for stationary Gaussian marginals created by *genuinely non-Gaussian* independent resets under general stable, possibly nonsymmetric drifts. The published *Four-time sign fingerprints of covariance-matched resetting, Gaussian, and telegraph baths* instead treats Brownian noise reset to a point, whose stationary marginal is not Gaussian, and compares different non-Gaussian bath mechanisms; it does not supply the present universal tensor inversion.

The result is a finite-dimensional, fourth-order observable identity deduced from Poisson independence and Gaussian conditioning, not a new general resetting construction or a proof of global publication priority. Stronger, unindexed general multi-time reset-correlation identities may subsume it and remain the principal originality risk.

## Limitations
The assumptions require independent constant-rate full-state refreshes, a stable linear Gaussian free evolution, a nondegenerate centered Gaussian stationary marginal and exact ensemble moments. They exclude state-dependent resetting, renewal clocks that are not Poisson, partial-coordinate resetting and non-Gaussian invariant marginals. The fourth-order identity does not establish statistical efficiency, finite-sample error bounds, or the ability to identify drift and diffusion separately from a single lag. Its strict witness concerns suitable direction pairs, not every possible pair. The cited scalar equilibrium-Gaussian case is covered by existing literature; no claim of priority is made for that restriction. Independent scientific assessment remains outstanding.

## References
1. K. Stølevik Olsen, *Steady-state moments under resetting to a distribution*, arXiv:2310.04840 (first public 7 October 2023), Phys. Rev. E 108, 044120 (2023). https://arxiv.org/abs/2310.04840 ; https://doi.org/10.1103/PhysRevE.108.044120 .
2. *Exact Gaussian stationary-state engineering by non-Gaussian stochastic resets* (2026), public mathematical finding: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-gaussian-stationary-state-engineering-by-non-gaussian-stoc--08050fc52754 .
3. *Gaussian covariance twins and displacement-only identification of Poisson-rethermalized Ornstein–Uhlenbeck motion* (2026), public mathematical finding: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-gaussian-covariance-twins-and-displacement-only-identification-o--d13d753808a7 .
4. *Four-time sign fingerprints of covariance-matched resetting, Gaussian, and telegraph baths* (2026), public mathematical finding: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-four-time-sign-fingerprints-of-covariance-matched-resetting-gaus--c69dc0d762a5 .
5. Eule and Metzger, *Non-equilibrium steady states of stochastic processes with intermittent resetting*, New J. Phys. 18, 033006 (2016), https://doi.org/10.1088/1367-2630/18/3/033006 .
