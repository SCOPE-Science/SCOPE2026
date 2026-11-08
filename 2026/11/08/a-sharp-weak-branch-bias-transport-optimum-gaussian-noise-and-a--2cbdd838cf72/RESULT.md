# A sharp weak-branch-bias transport optimum, Gaussian noise, and a positive finite-size current excess in a long-path exclusion network

## Finding
Consider a stationary asymmetric exclusion model with a periodic backbone and a single path-shaped side branch whose length grows proportionally to the backbone length. When the branch hopping bias is \(q_L=e^{\lambda/L}\), the macroscopic backbone density is determined by a one-dimensional chemical-potential equation. Its current has a sharp interior maximizing branch bias exactly in the density range \(1/2<\rho<c+1/2\). There is also a nondegenerate Gaussian fluctuation law, an explicit negative long-range backbone covariance, and a **positive** order-\(L^{-1}\) finite-size excess over the infinite-volume optimal current.

More precisely, put \(\sigma(s)=(1+e^{-s})^{-1}\). For each fixed \(c>0\), \(0<\rho<1+c\), \(\lambda\in\mathbb R\), the equation
\[
\rho=\sigma(\mu)+\int_0^c\sigma(\mu+\lambda x)\,dx
\]
has exactly one real solution \(\mu\). Write
\[
f=\sigma(\mu),\qquad v_b=f(1-f),\qquad v_t=\int_0^c\sigma'(\mu+\lambda x)\,dx,\qquad v_*=\frac{v_bv_t}{v_b+v_t}.
\]
Then with \(\Delta=h_f-h_b>0\),
\[
\frac{B_L}{L}\xrightarrow{\mathbb P} f,\quad
\frac{B_L-Lf}{\sqrt L}\Longrightarrow\mathcal N(0,v_*),\quad
\frac{\operatorname{Var}(B_L)}L\longrightarrow v_*,\quad
J_L\longrightarrow\Delta f(1-f).
\]
For distinct backbone sites \(i\ne j\),
\[
L\operatorname{Cov}(\eta_i,\eta_j)\longrightarrow-\frac{v_b^2}{v_b+v_t}.
\]
As the branch bias \(\lambda\) varies over all real numbers, the limiting current has a finite, unique global maximizer **if and only if** \(1/2<\rho<c+1/2\). It is the unique solution \(\lambda_*\) to
\[
\rho=\frac12+\int_0^c\sigma(\lambda_*x)\,dx,
\]
and its current is \(\Delta/4\). At this fixed optimal scaled bias, \(v_b=1/4\) and
\[
J_L(\lambda_*)=\Delta\left[\frac14+\frac{v_b^2}{(v_b+v_t)L}+o(L^{-1})\right].
\]
The finite-volume optimum is consequently above the limiting maximum for all sufficiently large \(L\), though the limiting optimization problem has maximum \(\Delta/4\).

Finally, for a **fixed** branch rate ratio \(q\) (independent of \(L\)) instead of weak scaling, the limiting backbone density is respectively \(\min\{\rho,1\}\), \(\rho/(1+c)\), or \(\max\{\rho-c,0\}\) when \(q<1\), \(q=1\), or \(q>1\). Thus \(e^{\lambda/L}\) resolves the singular thermodynamic crossover at unbiased branch hopping.

## Assumptions and scope
For integers \(L\ge3\), let the backbone be a directed nearest-neighbor exclusion ring with \(L\) sites, clockwise hopping rate \(h_f>h_b\ge0\) and counterclockwise rate \(h_b\), allowed only into vacancies. Attach a simple path of \(M_L=\lfloor cL\rfloor\) additional sites at the backbone site indexed zero; the path vertices have depths \(d=1,\ldots,M_L\). Along every path edge, hopping toward greater depth has positive rate \(h_t\), and the reverse positive rate is \(h_r\). Their ratio is \(q_L=h_t/h_r=e^{\lambda/L}\). The stationary law is restricted to exactly \(K_L=\lfloor\rho L\rfloor\) particles, with \(0<\rho<1+c\), so for sufficiently large \(L\), \(0<K_L<L+M_L\). The unique stationary distribution exists since this finite exclusion chain is irreducible in every nontrivial particle-number sector. All limits are for fixed real \(c,\rho,\lambda,h_f,h_b\), with \(L\to\infty\). The current is **per backbone bond**, not the sum over the whole backbone; \(B_L\) is the total number of occupied backbone sites. The fixed-\(q\) comparison treats \(q>0\) fixed separately from weak bias.

## Proof
**1. Exact invariant law and current.** The canonical invariant weight on every configuration with \(K_L\) particles is
\[
\pi_L(\eta)=Z_{L,K}^{-1}\prod_{d=1}^{M_L}q_L^{d\eta_d}.
\]
This is the exactly solved backbone-with-tree invariant measure [1, Eqs. (15), (31)–(35)]. It can also be checked directly: the branch edges satisfy detailed balance term by term, whereas conditional on any fixed branch configuration, uniform backbone weights have total clockwise and counterclockwise incoming/outgoing contributions cancelling around the ring. Thus every backbone arrangement with a specified number \(n\) of backbone particles is equiprobable, and the stationary signed current through an arbitrary backbone bond is exactly
\[
J_L=\Delta\frac{\mathbb E[B_L(L-B_L)]}{L(L-1)}.
\]
The denominator \(L(L-1)\) is the number of ordered choices of two distinct backbone positions, and the numerator counts occupied-vacant ordered pairs.

**2. Independent-Bernoulli conditioning representation.** For each \(L\), choose the unique chemical potential \(\mu_L\) such that
\[
L\sigma(\mu_L)+\sum_{d=1}^{M_L}\sigma(\mu_L+\lambda d/L)=K_L.
\]
Let independent Bernoulli variables be placed at backbone positions with success probability \(\sigma(\mu_L)\), and at branch depth \(d\) with success probability \(\sigma(\mu_L+\lambda d/L)\). Condition on total occupancy exactly \(K_L\). The conditional product probability equals \(\pi_L\), since the global chemical-potential factors cancel under the particle-number constraint. Riemann summation and the strict positive derivative of the density equation give \(\mu_L=\mu+O(L^{-1})\). For fixed parameters, all success probabilities remain in an interval \([\varepsilon,1-\varepsilon]\) independent of \(L\).

**3. Gaussian canonical fluctuations.** Before conditioning, the backbone and branch occupation sums are independent, with means adding exactly to \(K_L\) and variances \(Lv_b+O(1)\) and \(Lv_t+O(1)\), respectively. A uniform triangular-array local central limit theorem holds for each sum and their total: the centered characteristic function for frequencies of order \(L^{-1/2}\) converges to the relevant Gaussian, while outside a fixed multiple of \(L^{-1/2}\) its modulus is bounded by \(\exp[-C L\sin^2(t/2)]\), because every Bernoulli success probability stays in \([\varepsilon,1-\varepsilon]\). Fourier inversion therefore gives uniform local Gaussian approximations. Taking the ratio of the local masses
\[
\mathbb P(B_L=n\mid B_L+T_L=K_L)
=\frac{\mathbb P(B_L=n)\mathbb P(T_L=K_L-n)}{\mathbb P(B_L+T_L=K_L)}
\]
shows that \((B_L-Lf)/\sqrt L\) converges to the centered Gaussian whose reciprocal variance is \(v_b^{-1}+v_t^{-1}\), hence variance \(v_*\). Variance convergence is not inferred merely from weak convergence: Fourier inversion gives \(\sup_k\mathbb P(T_L=k)\le C/\sqrt L\), and the total local limit theorem gives \(\mathbb P(B_L+T_L=K_L)\ge c/\sqrt L\). Hence the conditional backbone mass at every integer is at most a fixed constant times its unconditioned binomial mass. Hoeffding bounds and the bounded-away-from-boundary binomial parameters give uniform conditioned fourth moments after scaling by \(\sqrt L\), and therefore uniform integrability of squares. This proves convergence of first and second centered moments and of \(\operatorname{Var}(B_L)/L\). Conditional exchangeability of all backbone sites yields the exact identity
\[
\operatorname{Var}(B_L)=L\bar p_L(1-\bar p_L)+L(L-1)\operatorname{Cov}(\eta_i,\eta_j),\quad
\bar p_L=\mathbb E[B_L]/L,
\]
which gives the stated negative covariance constant.

**4. Current limit, optimizer, and finite-size excess.** The exact current identity and the concentration of \(B_L/L\) prove \(J_L\to\Delta f(1-f)\). Differentiating the density constraint with respect to \(\lambda\) gives
\[
\frac{df}{d\lambda}=-\frac{f(1-f)\int_0^c x\sigma'(\mu+\lambda x)\,dx}{f(1-f)+\int_0^c\sigma'(\mu+\lambda x)\,dx}<0.
\]
As \(\lambda\to-\infty\), \(f\to\min\{\rho,1\}\), and as \(\lambda\to+\infty\), \(f\to\max\{\rho-c,0\}\), by the monotone chemical-potential equation and logistic saturation (or comparison with zero-temperature Fermi occupations). Consequently the attainable backbone density interval contains \(1/2\) **strictly** exactly for \(1/2<\rho<c+1/2\); strict decrease of \(f\) gives uniqueness of the finite maximizer. The optimizer equation follows by setting \(\mu=0\).

At \(\lambda_*\), the Gaussian and moment limits give \(\mathbb E[B_L]=L/2+o(\sqrt L)\) and \(\operatorname{Var}(B_L)=Lv_*+o(L)\). Using \(B_L(L-B_L)=L^2/4-(B_L-L/2)^2\), the exact current formula becomes
\[
\frac{J_L(\lambda_*)}{\Delta}=\frac{L}{4(L-1)}-\frac{Lv_*+o(L)}{L(L-1)}
=\frac14+\frac{1/4-v_*}{L}+o(L^{-1}).
\]
Since \(1/4-v_*=v_b^2/(v_b+v_t)>0\), the asymptotic excess has strictly positive coefficient, irrespective of how the floor operations select the particle number.

**5. Fixed-bias contrast.** For \(q=1\), all \(L+M_L\) sites are exchangeable, giving density \(K_L/(L+M_L)\to\rho/(1+c)\). If \(q>1\) is fixed, among configurations with \(K_L\) particles, weight favors filling branch sites starting from the deepest end; displacing \(\delta L\) particles away from the maximal permitted number of branch particles loses at least \(\exp[-a_\delta L^2]\) in Gibbs weight compared with the maximizer, while the total number of states is only \(\exp[O(L)]\). Thus the number of branch particles divided by \(L\) tends to \(\min\{\rho,c\}\) in probability, leaving backbone fraction \(\max\{\rho-c,0\}\). For fixed \(q<1\), the same argument using the shallowest occupied branch sites makes the backbone fill first, yielding fraction \(\min\{\rho,1\}\). Apply the current identity to obtain the corresponding fixed-bias current limits.

## Verification
`CHECK.py` is a self-contained Python 3 standard-library script. Execute `python3 CHECK.py` beside this document. It checks the finite-state master equation directly for a small ring-plus-path graph, independently evaluates the finite-volume canonical partition by Poisson-binomial convolution, compares the current, variance and off-diagonal covariance against the proposed continuum formulas, verifies the unique optimal-bias branch equation, tests the fixed-bias limits, and checks the positive finite-size current excess. The checks are finite tests, not substitutes for the limiting Fourier-inversion argument. A reference numerical case with \(c=3/4\), \(\rho=19/20\), and \(\Delta=1\) yields \(\lambda_*=1.096217645743\ldots\), an asymptotic excess coefficient \(0.146162429751\ldots\), and conditional-variance density \(0.103837570249\ldots\).

## Relationship to prior work
Ishiguro and Ando [1] derive the **exact same finite-size stationary weight** and mixed-hypergeometric backbone-current formula for a single long tree. These are explicitly prior, not new results here. They discuss numerical flow/no-flow contrasts but do not state the linear-branch, inverse-length-bias limit, its complete sharp branch-bias optimizer, the Gaussian canonical fluctuation coefficient, or the positive finite-size optimal-current excess. Sarkar and Gupta [2] derive grand-canonical fugacity/density profiles and transport for a **random comb with branches at many backbone sites**, including a qualitatively nonmonotone drift; their logistic occupation formulas strongly anticipate the chemical-potential step used here. The novelty asserted here is the coupled limit and exact covariance/optimization/finite-size classification for one macroscopic branch with independently tunable branch bias and fixed backbone drift, not the generic fugacity technique. Ishiguro and Sato [3] furnish the earlier exact steady-state framework on non-one-dimensional exclusion networks. Results for finite fixed branch geometries and general half-filled tree comparisons are also known; neither gives the joint weak-bias Gaussian and current-excess law. A sufficiently broad earlier equivalence-of-ensembles theorem may imply portions of the Gaussian statement, and this remains a specific priority limitation.

## Limitations
This proves **stationary spatial occupation** fluctuations, not dynamical current variance, a time-dependent central limit theorem, or relaxation/mixing rates. The Gaussian limit is for every fixed finite \(\lambda\) and \(0<\rho<1+c\); it is not uniform as \(\lambda\to\pm\infty\) or at density endpoints. The strict finite-size current excess is only asserted for sufficiently large \(L\) at the fixed limiting optimizer \(\lambda_*\), not at every \(L\). The two displayed branches of the asymptotic density use separate limiting orders: \(q\) fixed versus \(q=e^{\lambda/L}\). The logarithmic/Fermi-conditioning and current formulas use exact stationary weights from [1], and the individual methods are standard. Originality of their combined sharp regime should be checked further against specialized pre-2026 long-comb work. Independent scientific validation has not been carried out.

## References
[1] Y. Ishiguro and Y. Ando, *Asymmetric simple exclusion process with tree-like network branches*, arXiv:2603.09694v1 (first publicly submitted 2026-03-10), https://arxiv.org/html/2603.09694, particularly Sections III.3 and IV.2 and Eqs. (15), (31)–(42).

[2] M. Sarkar and S. Gupta, *Asymmetric simple exclusion process on a random comb: Transport properties in the stationary state*, arXiv:2502.11931 (first publicly submitted 2025-02-17), https://arxiv.org/abs/2502.11931, particularly Section 3 and the branch density formula.

[3] Y. Ishiguro and J. Sato, *Exact steady states in the asymmetric simple exclusion process beyond one dimension*, arXiv:2403.01934 (2024), https://arxiv.org/abs/2403.01934.
