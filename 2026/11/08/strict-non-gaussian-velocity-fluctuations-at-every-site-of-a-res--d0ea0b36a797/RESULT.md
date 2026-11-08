# Strict non-Gaussian velocity fluctuations at every site of a reset-driven harmonic chain

## Finding
Consider the finite damped harmonic chain specified below, driven at its two ends by independent stationary Brownian walls with Poisson resetting. For **every** length \(N\ge2\), **every** site \(1\le\ell\le N\), every positive wall diffusivity and reset rate, and all independent nonnegative-temperature Gaussian Langevin endpoint forcing, its stationary velocity is a centered Gaussian variance mixture with a **genuinely nonconstant** mixing variance \(\Sigma_\ell\). Therefore
\[
\boxed{\operatorname{cum}_4(v_\ell)=3\operatorname{Var}(\Sigma_\ell)>0.}
\]
This rigorously upgrades earlier numerical observations of finite-chain non-Gaussian velocity statistics to a strict analytical all-site, all-parameter theorem. Replacing both resetting Brownian walls with independent, covariance-matched Gaussian Ornstein–Uhlenbeck (OU) walls leaves **all stationary two-point covariances and quadratic mean observables unchanged**, but makes **every** stationary velocity fourth cumulant identically zero.

An explicit positive four-time connected cumulant for the resetting wall is presented and verified below as a **previously established input** (Knight, Kaveh and Pruessner, 2025, Supplemental Sec. SIII.2), not as a new discovery. The new contribution assessed here is the finite-chain, every-site, thermal-robust strictness proof via a nondegenerate conditional Gaussian variance mixture.

## Assumptions and scope
Take integers \(N\ge2\) and positive masses \(m\), spring stiffness \(k\), and endpoint friction \(\gamma\). Write \(q\in\mathbb R^N\) and \(v=\dot q\). Let \(K\) be the tridiagonal matrix with diagonal entries \(2\) and neighboring entries \(-1\), and \(B=e_1e_1^\top+e_Ne_N^\top\). The chain obeys
\[
m\ddot q+\gamma B\dot q+kKq
=k(e_1Y_1+e_NY_N)+\xi,
\]
where the stationary reset Brownian walls \(Y_j\) are mutually independent with positive diffusivities \(D_j\) and rates \(r_j\), and are independent of centered Gaussian white forcing \(\xi\) with covariance
\[
\mathbb E[\xi(t)\xi(s)^\top]
=2\gamma(T_1e_1e_1^\top+T_Ne_Ne_N^\top)\delta(t-s),\qquad T_1,T_N\ge0.
\]
All processes are defined in their stationary, two-sided versions. Fourth cumulants are classical joint cumulants of commuting real-valued observations, not time-ordered quantum correlations. The OU control replaces each \(Y_j\) by an independent stationary process satisfying \(dU_j=-r_jU_j\,dt+\sqrt{4D_j}\,dW_j\), with the same independent thermal forcing law.

## Proof
**Background four-time wall identity and self-contained reconstruction.** The reset diffusion generator on polynomials is
\[
Lf(x)=D f''(x)+r[f(0)-f(x)].
\]
Stationarity gives \(\mathbb E Y^2=2D/r\) and \(\mathbb E Y^4=24D^2/r^2\). The Markov semigroup on the required monomials is
\[
P_t x=e^{-rt}x,\qquad
P_t x^2=e^{-rt}x^2+\frac{2D}{r}(1-e^{-rt}),\qquad
P_t x^3=e^{-rt}(x^3+6Dtx).
\]
Put \(a=t_2-t_1\), \(b=t_3-t_2\), and \(c=t_4-t_3\). Conditioning successively at \(t_3\), \(t_2\), and \(t_1\) yields
\[
\mathbb E[Y_{t_1}Y_{t_2}Y_{t_3}Y_{t_4}]
=\frac{4D^2}{r^2}e^{-r(a+c)}
\big[1+(5+3ra)e^{-rb}\big].
\]
The covariance is \(\mathbb E[Y_sY_t]=(2D/r)e^{-r|s-t|}\). Subtracting the three pairwise covariance products, whose sum equals
\[
\frac{4D^2}{r^2}e^{-r(a+c)}(1+2e^{-2rb}),
\]
recovers the previously known fourth cumulant [Knight–Kaveh–Pruessner, 2025, Supplement SIII.2]. Its bracket is at least \(3\) because \(a,b\ge0\). A Gaussian OU process with the stated covariance has zero fourth joint cumulant, proving the strict fourth-order distinction even though the two-point functions coincide.

**Chain stability and responses.** For \(\xi=Y_1=Y_N=0\), the chain energy has derivative \(-\gamma(v_1^2+v_N^2)\). Every eigenvector of the positive Dirichlet chain matrix \(K\) has a nonzero endpoint entry; therefore no nontrivial normal mode avoids endpoint damping. The finite-dimensional drift matrix is Hurwitz. Thus all linear impulse-response kernels decay exponentially. Let \(g_{\ell1}(t)\) be the causal response of \(v_\ell\) to the left wall *displacement*, including the factor \(k\). For \(z>0\), its Laplace transform is
\[
\widehat g_{\ell1}(z)
=kz\left(mz^2I+\gamma zB+kK\right)^{-1}_{\ell1}>0.
\]
Strict positivity follows because the displayed matrix is an irreducible symmetric positive-definite nonsingular \(M\)-matrix (weak diagonal dominance in the bulk and strict dominance at the boundaries). In particular,
\[
g_{\ell1}(t)=\frac{(k/m)^\ell}{[2(\ell-1)]!}
 t^{2(\ell-1)}+O(t^{2\ell-1})\quad(t\downarrow0).
\]
The shortest nonzero term comes from the unique nearest-neighbor path from site \(1\) to site \(\ell\) in the state-space matrix powers. The same arguments hold for the right-wall response after reversing site indices.

**Nondegenerate conditional variance.** Condition on the two complete Poisson reset-clock histories. Since Brownian increments and all thermal forcings are independent Gaussian variables, \(v_\ell\) is conditionally centered Gaussian, with conditional variance \(\Sigma_\ell\). The thermal part is a deterministic constant; the two wall contributions are independent nonnegative random variables. It suffices to show that the left-wall contribution has nonzero variance.

For a general causal exponentially decaying response \(g\) to a wall \(Y\), write \(Z=\int_0^\infty g(s)Y_{-s}\,ds\), and let \(V\) denote the conditional variance of \(Z\) given the Poisson clock. Condition only on the wall age \(A\), the time since the last reset at zero. Its density is \(re^{-ra}\) on \(a>0\). Brownian increments on the present reset interval are independent of the pre-reset history. With \(G(u)=\int_0^u g(s)\,ds\), this gives the exact conditional-variance mean
\[
H(a):=\mathbb E[V\mid A=a]
=2D\int_0^a G(u)^2\,du
+\frac{2D}{r}\int_a^\infty\!\int_a^\infty
 g(s)g(t)e^{-r|s-t|}\,ds\,dt.
\]
For any smooth such kernel,
\[
H'(a)=2DG(a)^2-\frac{4D}{r}g(a)
\int_a^\infty g(t)e^{-r(t-a)}\,dt.
\]
For the left-wall chain kernel, let \(p=2(\ell-1)\) and \(c=(k/m)^\ell/p!>0\). Then \(g(a)=ca^p+O(a^{p+1})\), \(G(a)^2=O(a^{2p+2})\), and the last integral tends to \(\widehat g(r)>0\). Hence
\[
H'(a)=-\frac{4Dc}{r}\widehat g(r)a^p+o(a^p)<0
\quad\text{for sufficiently small }a>0.
\]
Thus \(H(A)\) is nonconstant and \(\operatorname{Var}(V)\ge\operatorname{Var}(H(A))>0\). The right-wall and thermal contributions cannot cancel this random variance, because the two clock contributions are independent and the thermal part deterministic. Conditional Gaussianity now gives \(\mathbb E[v_\ell^4]=3\mathbb E[\Sigma_\ell^2]\) and \(\mathbb E[v_\ell^2]=\mathbb E[\Sigma_\ell]\), proving \(\operatorname{cum}_4(v_\ell)=3\operatorname{Var}(\Sigma_\ell)>0\). Under OU forcing all inputs are Gaussian and the chain is linear, so \(\operatorname{cum}_4(v_\ell)=0\), while matching covariances preserve all second-order outputs.

## Verification
The accompanying standalone `check.py` tests the literature-established fourth-moment/cumulant identity symbolically, its zero-lag normalization and positive values on multiple rational parameter triples, and the response Taylor coefficients and strictly positive Laplace transfer values at every site for finite chains of lengths \(2\) through \(6\). It reports 226 successful checks. The all-time positivity and all-parameter finite-chain strictness follow from the analytic proof above, **not** from a finite set of tests. Run with `python check.py` after installing `sympy`.

## Relationship to prior work
Sarkar and Roy, arXiv:2307.06127v1 (first public 2023-07-12), introduce **this same reset-wall-driven finite harmonic chain**, derive its two-time reservoir covariance and bulk second-order transport, and **numerically** find positive finite-size velocity kurtosis (with an approximately inverse-size bulk trend). These are their observations; no new non-Gaussianity phenomenon is claimed. Their inspected full text and appendices do not prove the site-uniform, all-positive-parameter assertion by a conditional-variance argument, nor arbitrary independent thermal Gaussian robustness. The theorem here supplies precisely that rigorous uniform statement, not an exact finite-size kurtosis amplitude or thermodynamic asymptotic.

Knight, Kaveh and Pruessner, arXiv:2507.22199 (first public 2025-07-29), Supplemental Sec. SIII.2, Eqs. (S75)–(S78), **already obtain the full ordered Brownian-resetting four-time moment and connected fourth cumulant** in a different model (hidden self-propulsion and entropy production). The wall formula in the proof is a self-contained reconstruction and is explicitly **not original**. Their setting does not state a theorem about finite harmonic chains, every-site conditional variance nondegeneracy, or thermal robustness; the mathematical implications are different.

Sarkar, Santra and Basu, arXiv:2210.09035 (2022), investigate Gaussian OU and other active harmonic-chain baths but not the every-site reset-wall mixture rigidity. Olsen, arXiv:2310.04840 (2023), studies stationary reset-to-distribution moments for confined particles rather than the finite-chain response theorem. An accessible prior analysis of arXiv:2307.06127 concerns inverse identification of reset rates from **two-point** chain covariance; it neither establishes nor subsumes the fourth-cumulant positivity result.

## Limitations
No finite-\(N\) closed rational formula for the chain's kurtosis magnitude, no proof of an \(N^{-1}\) asymptotic coefficient, and no high-dimensional joint fourth-order classification are asserted. A broad literature search and primary-text comparisons do not establish publication priority for the new every-site theorem; in particular, the main 2023 source numerically observed positive kurtosis and the 2025 supplement explicitly provides the input wall four-point identity. The nondegenerate variance-mixture argument could have appeared elsewhere without being indexed. The thermal baths are independent Gaussian sources, and the wall resets are to zero at independent Poisson times; non-Poisson renewal clocks and feedback coupling are outside scope. The result does not claim statistical detectability from finite sampled data without uncertainty analysis.

## References
- R. Sarkar and P. Roy, *Stationary state of harmonic chains driven by boundary resetting*, arXiv:2307.06127v1 (first public 12 July 2023); full text and appendices in arXiv:2307.06127v3, https://arxiv.org/html/2307.06127v3.
- R. Sarkar, I. Santra and U. Basu, *Stationary states of activity-driven harmonic chains*, arXiv:2210.09035, https://arxiv.org/abs/2210.09035.
- K. S. Olsen, *Steady-state moments under resetting to a distribution*, Phys. Rev. E 108, 044120 (2023), https://arxiv.org/html/2310.04840v1.
- J. Knight, F. Kaveh and G. Pruessner, *Self-propulsion symmetries determine entropy production of active particles with hidden states*, arXiv:2507.22199v1 (2025), Supplemental Sec. SIII.2, Eqs. (S75)–(S78), https://arxiv.org/abs/2507.22199.
