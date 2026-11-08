# Universal refresh-rate localization ordering for doubly stochastic diffusion resetting

## Finding
Consider a stationary, independently refreshed reset-rate environment. Let \(\nu\) be a non-point-mass probability distribution supported on \([\lambda_-,\lambda_+]\), where \(0<\lambda_-\leq\lambda_+<\infty\), let \(\bar\lambda=\int\lambda\,\nu(d\lambda)\), and let \(\mu\geq0\) be the environmental refresh frequency. For every age threshold \(t>0\) and every pair \(0\leq\mu_1<\mu_2<\infty\), the stationary times since the last particle reset satisfy the **strict first-order stochastic order**
\[
\Pr(A_{\mu_1}>t)>\Pr(A_{\mu_2}>t).
\]
Put \(\varphi(s)=\int e^{-\lambda s}\,\nu(d\lambda)\). The difference has the explicit, strictly positive lower bound
\[
\Pr(A_{\mu_1}>t)-\Pr(A_{\mu_2}>t)
\geq(\mu_2-\mu_1)e^{-\mu_2t}\int_0^t
\bigl[\varphi(t)-\varphi(s)\varphi(t-s)\bigr]ds>0.
\]
The sharp endpoint envelopes are
\[
e^{-\bar\lambda t}<\Pr(A_\mu>t)<\varphi(t)
\qquad(0<\mu<\infty,\ t>0).
\]
The right-hand equality is attained at \(\mu=0\), and the left-hand envelope is attained as \(\mu\to\infty\). For Brownian motion in any dimension \(d\geq1\) with generator \(D\Delta\), \(D>0\), reset to the origin independently of the rate-refresh process, the stationary radius \(R_\mu=|X_\mu|\) obeys, for every \(r>0\),
\[
\Pr(R_{\mu_1}>r)>\Pr(R_{\mu_2}>r),
\]
with strict endpoint envelopes. In dimension one these are explicitly
\[
e^{-r\sqrt{\bar\lambda/D}}<\Pr(|X_\mu|>r)
<\int e^{-r\sqrt{\lambda/D}}\,\nu(d\lambda).
\]
For each real \(p>0\), \(\mathbb E|X_\mu|^p\) is finite and strictly decreasing with \(\mu\). No ordering of pointwise spatial densities or search-time optimization is claimed.

## Assumptions and scope
On the entire time axis, let the environmental rate \(\Lambda_\mu(s)\) change at points of an independent homogeneous Poisson process of rate \(\mu\), with a fresh independent sample from \(\nu\) on each resulting plateau. The initial plateau rate has distribution \(\nu\). For \(\mu=0\), a single rate is sampled once and held fixed. Conditional on the complete environment trajectory, particle resets to the origin form an inhomogeneous Poisson process with instantaneous intensity \(\Lambda_\mu(s)\). In between resets, a \(d\)-dimensional standard Brownian motion scaled to have generator \(D\Delta\) evolves independently. Refresh events themselves **do not reset the particle**, and resetting does **not refresh the environmental rate**.

The lower bound \(\Lambda_\mu(s)\geq\lambda_->0\) ensures that a reset has occurred at a finite time in the past almost surely, yielding a unique stationary position process conditional on this stationary environment. The stationary age \(A_\mu\) is the elapsed time since that last reset, not the interval length between successive resets. Parameters \(D\), \(d\), and the law \(\nu\) are fixed while \(\mu\) varies. The strict conclusions require nondegenerate \(\nu\); for a point mass every refresh frequency gives the same law.

## Proof
**1. Backward no-reset probability.** At a stationary observation time zero, the event \(A_\mu>t\) means no particle reset occurred in \((-t,0]\). Conditional on \(\Lambda_\mu\), its probability is
\[
\exp\!\left(-\int_{-t}^0\Lambda_\mu(s)\,ds\right).
\]
Let \(\Pi_\mu(t)\) be the partition of this interval formed by all refresh marks. The rate on each plateau is an independent \(\nu\)-sample; averaging them yields the exact identity
\[
S_\mu(t):=\Pr(A_\mu>t)
=\mathbb E_{\Pi_\mu(t)}\prod_{I\in\Pi_\mu(t)}\varphi(|I|).
\tag{1}
\]
This is a backward stationary-interval identity, not a renewal assumption about successive reset intervals.

**2. Strict loss under partition refinement.** Let \(L,L'\) be independent \(\nu\)-samples. For \(u,v>0\),
\[
\varphi(u+v)-\varphi(u)\varphi(v)
=\frac12\mathbb E\left[(e^{-uL}-e^{-uL'})(e^{-vL}-e^{-vL'})\right]>0.
\tag{2}
\]
The integrand is nonnegative, and is positive with positive probability because \(\nu\) is not a point mass. Hence splitting one nonzero plateau of length \(u+v\) into lengths \(u\) and \(v\) replaces its factor in (1) by the **strictly smaller** product \(\varphi(u)\varphi(v)\). Coupling \(\Pi_{\mu_2}(t)\) to \(\Pi_{\mu_1}(t)\) by superimposing an independent Poisson process of rate \(\mu_2-\mu_1\) shows the product for the faster refresh process is never larger and is strictly smaller whenever an additional interior mark appears. Such a mark has positive probability for each \(t>0\), proving strict stochastic age ordering.

For the quantitative bound, restrict to the event that \(\Pi_{\mu_1}\) has no marks and there is exactly one additional mark at distance \(s\) from the left endpoint. Its probability density in \(ds\) is \((\mu_2-\mu_1)e^{-\mu_2t}\,ds\). On this event the difference of conditional products is exactly \(\varphi(t)-\varphi(s)\varphi(t-s)\); on every other event it is nonnegative. Integration proves the displayed lower bound, with strict positivity from (2).

**3. Sharp endpoint sandwich and high-refresh convergence.** With no refresh \(\Pi_0(t)\) has a single plateau, so \(S_0(t)=\varphi(t)\). For finite positive \(\mu\), there is a positive probability of at least one mark, giving \(S_\mu(t)<\varphi(t)\) by (2). Jensen's inequality gives
\[
S_\mu(t)=\mathbb E e^{-H_\mu(t)}\geq e^{-\mathbb EH_\mu(t)}=e^{-\bar\lambda t},
\quad H_\mu(t)=\int_{-t}^0\Lambda_\mu(s)\,ds.
\]
For finite \(\mu\), \(H_\mu(t)\) is nonconstant: with probability \(e^{-\mu t}>0\) there is no refresh, in which case \(H_\mu(t)=tL\) has a nondegenerate law. Strict convexity therefore makes Jensen strict. Since the rate environment is stationary and independently refreshed,
\[
\operatorname{Cov}(\Lambda_\mu(s),\Lambda_\mu(s+u))
=\operatorname{Var}_\nu(L)e^{-\mu|u|}.
\]
Thus for \(\mu>0\),
\[
\operatorname{Var}(H_\mu(t))
=2\operatorname{Var}_\nu(L)\int_0^t(t-u)e^{-\mu u}\,du
\leq\frac{2t\operatorname{Var}_\nu(L)}{\mu}.
\]
Consequently \(H_\mu(t)\to\bar\lambda t\) in \(L^2\) as \(\mu\to\infty\), whence \(S_\mu(t)\to e^{-\bar\lambda t}\). At \(\mu\downarrow0\), Poisson partitions have no marks with probability tending to one, so \(S_\mu(t)\to\varphi(t)\). The endpoint bounds are therefore sharp.

**4. Spatial ordering and moment consequences.** The Brownian evolution after the most recent reset is independent of reset times and environment. Therefore, with \(Z\sim N(0,I_d)\) independent of \(A_\mu\),
\[
X_\mu\ \overset{\mathrm d}=\sqrt{2DA_\mu}\,Z.
\tag{3}
\]
For every \(r>0\), the conditional tail \(h_r(a)=\Pr(\sqrt{2Da}|Z|>r)\) is continuous and **strictly increasing** in \(a>0\), with \(h_r(0)=0\). The strict age survival order at every positive threshold, together with
\[
\mathbb Eh_r(A_\mu)=\int_0^\infty h_r'(t)S_\mu(t)\,dt
\]
(the derivative is positive for every \(t>0\)), establishes the strict spatial-radius order. For a general dimension, the same conclusion follows directly from a strictly increasing Gaussian-radius tail. The endpoint limits follow by bounded convergence applied to (3) and the age laws. In dimension one, a constant-reset-rate Brownian particle has the standard Laplace law, whose absolute tail is \(e^{-r\sqrt{\lambda/D}}\). Mixture over frozen rates and the fast-refresh deterministic mean rate gives the two explicit endpoints.

Finally, for \(p>0\),
\[
\mathbb E|X_\mu|^p=(4D)^{p/2}
\frac{\Gamma((d+p)/2)}{\Gamma(d/2)}\,
\mathbb EA_\mu^{p/2},\qquad
\mathbb EA_\mu^q=q\int_0^\infty t^{q-1}S_\mu(t)\,dt.
\]
All integrals are finite because \(S_\mu(t)\leq e^{-\lambda_-t}\). Strict age ordering makes all these power moments strictly decreasing.

**5. Independent exactly solvable check.** For \(\nu=(\delta_a+\delta_b)/2\) with \(a,b>0\), \(a\ne b\), put \(m=(a+b)/2\), \(\delta=(b-a)/2\), and \(w=\sqrt{\delta^2+\mu^2/4}\). Two-state Feynman--Kac evolution gives
\[
S_\mu(t)=e^{-(m+\mu/2)t}
\left[\cosh(wt)+\frac\mu{2w}\sinh(wt)\right]
\]
and hence
\[
\mathbb E|X_\mu|^2
=2dD\frac{m+\mu}{ab+\mu m},\qquad
\frac d{d\mu}\mathbb E|X_\mu|^2
=-\frac{2dD\delta^2}{(ab+\mu m)^2}<0.
\]
The general ordering is **not** inferred from this special case, which is included for reproducibility and a concrete observable. This two-rate second-moment formula is not asserted to be independently new.

## Verification
The accompanying standard-library `verify.py` computes the Feynman--Kac ODE independently from the two-rate closed form, tests three-rate hazards, verifies strict finite-refresh order and the explicit one-extra-mark lower bound, integrates the second moment, and checks one-dimensional radial tails against the frozen-rate mixture. Execute `python3 verify.py`. Its bounded numerical tests check arithmetic and conventions only. The universal statements in this document are proved in Steps 1--4 and are not certified by finite tests.

## Relationship to prior work
Arutkin and Reuveni (2025) introduced the independently refreshed doubly stochastic resetting environment and derived a general stationary Fourier-space formula, their Eq. (23), for arbitrary rate laws, as well as slow-/fast-refresh endpoint distributions. Their Eq. (11) also uses the integrated hazard. Those model definitions, stationary-transform formulas, and limiting profiles are **prior results**, not claimed here. Their accessible main text was inspected, including the explicit Fourier transform; the separately cited supplementary derivation was not available. The specific contribution established here is the **strict first-order cross-refresh ordering of the entire stationary age family and all radial excursion probabilities**, the distribution-free strict endpoint envelopes, and a computable strictly positive gap valid simultaneously for every positive age threshold. An earlier stationary-covariance calculation in this same model also supplies a fixed-refresh Laplace transform of the backward no-reset probability; that kernel representation is likewise prior work. The presently assessed all-threshold strict cross-refresh comparison requires an explicit stochastic partition-refinement argument, not merely a fixed-parameter transform.

The broader directionally convex ordering theory for Cox point processes developed by Meester and Shanthikumar (1993) and by Błaszczyszyn and Yogeshwaran (2011) is a related comparison framework. The latter full text was inspected; it analyzes clustering and percolation orders, rather than this refresh-parameter age/radius family. The former's abstract was accessible but not its full text. Any general process-order theorem in that inaccessible work that directly yields this specific rate-refresh comparison would affect publication priority. The positive-correlation inequality behind Step 2 is elementary; its mathematical utility here is the full physical ordering, not the elementary inequality in isolation.

## Limitations
The theorem assumes that environmental refresh times form a homogeneous Poisson process, each refreshed rate is drawn independently from the same fixed bounded distribution, the environment is stationary and evolves independently of particle reset events, the spatial motion is Brownian, and rate values are uniformly bounded away from zero. It does not compare spatial densities pointwise, first-passage times, correlated rate renewals, or arbitrary time-dependent refresh schedules. When \(\nu\) is a point mass all strict inequalities become equalities. The leading source already supplied exact transform formulas and the two limiting steady laws; neither is claimed new. A general unpublished or inaccessible Cox-process ordering could subsume this comparison. Independent scientific and literature-priority reviews have not been performed.

## References
1. M. Arutkin and S. Reuveni, *Diffusion with doubly stochastic resetting*, arXiv:2509.25365v1 (first publicly posted 2025-09-29), https://arxiv.org/abs/2509.25365 ; full text https://www.researchgate.net/publication/396048096_Diffusion_with_doubly_stochastic_resetting .
2. M. R. Evans and S. N. Majumdar, *Diffusion with stochastic resetting*, Physical Review Letters **106**, 160601 (2011), https://doi.org/10.1103/PhysRevLett.106.160601 .
3. B. Błaszczyszyn and D. Yogeshwaran, *Clustering, percolation and directionally convex ordering of point processes*, arXiv:1105.4293v1 (2011), https://arxiv.org/abs/1105.4293 .
4. L. E. Meester and J. G. Shanthikumar, *Regularity of Stochastic Processes: A Theory Based on Directional Convexity*, Probability in the Engineering and Informational Sciences **7** (1993), 343--360, https://doi.org/10.1017/S0269964800002965 (abstract inspected; complete text not accessible).
