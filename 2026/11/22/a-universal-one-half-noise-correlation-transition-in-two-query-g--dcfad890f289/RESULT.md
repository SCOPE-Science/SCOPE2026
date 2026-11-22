# A universal one-half noise-correlation transition in two-query Gaussian quadrature

## Finding

The choice between two redundant signal measurements and one signal measurement paired with a low-signal reference changes at the **exact correlation coefficient** \(\rho=1/2\) in the high-measurement-noise limit. The statement applies to a class of Gaussian-process integration problems, not only to one covariance kernel.

Let \(X(t)\), \(t\in T\), be a centered Gaussian process on a compact metric set with continuous covariance \(K\). Let \(J\) be a jointly Gaussian scalar integral/linear functional, and put \(g(t)=\operatorname{Cov}(J,X(t))\). Assume \(0\le g(t)\le M\), \(M>0\), the maximum \(M\) is attained at the unique point \(t_*\), and the nonempty zero set is \(Z=\{t:g(t)=0\}\). Two predetermined observations are \(Y_i=X(t_i)+\epsilon_i\), with errors independent of \((J,X)\) and covariance \(\eta\begin{psmallmatrix}1&\rho\\\rho&1\end{psmallmatrix}\), where \(\eta>0\) and \(-1<\rho<1\). Both equal and distinct sites are allowed. Let \(G_\eta(t_1,t_2)=\operatorname{Var}(J)-\operatorname{Var}(J\mid Y_1,Y_2)\).

As \(\eta\to\infty\), the globally optimal gain obeys
\[
\max_{t_1,t_2\in T}G_\eta(t_1,t_2)
=\frac{M^2}{\eta}\max\!\left\{\frac{2}{1+\rho},\frac{1}{1-\rho^2}\right\}+O(\eta^{-2}).
\]
If \(\rho<1/2\), *every* globally optimal pair approaches \((t_*,t_*)\). If \(\rho>1/2\), every globally optimal pair approaches the set \(\bigl(\{t_*\}\times Z\bigr)\cup\bigl(Z\times\{t_*\}\bigr)\), in the sense that its distance to the indicated set tends to zero. This threshold is independent of the latent kernel and target beyond the stated assumptions. At \(\rho=1/2\) the leading-order comparison ties; no assertion of a unique limiting geometry is made.

For the *standard zero-endpoint Brownian bridge* on \([0,1]\), with \(J=\int_0^1X(t)\,dt\), one has \(t_*=1/2\), \(M=1/8\), \(Z=\{0,1\}\), and \(\operatorname{Var}(J)=1/12\). Thus the two high-noise optimal geometries are coalescing midpoint queries below \(\rho=1/2\) and a midpoint plus an endpoint noise-reference query above it. The exact finite-noise gains for the midpoint-repeat and endpoint-plus-midpoint benchmarks are
\[
G_{\mathrm{repeat}}=\frac{1}{16[1+2\eta(1+\rho)]},\qquad
G_{\mathrm{reference}}=\frac{1}{16[1+4\eta(1-\rho^2)]}.
\]
For every \(\eta>0\), the reference benchmark strictly beats the repeat benchmark if and only if \(\rho>1/2\), tying at equality.

A stronger finite-noise consequence is that, whenever \(\rho>1/2\) and \(2\eta(1+\rho)(2\rho-1)>1\), **no globally optimal two-site design is reflection-symmetric** (that is, no optimizer has \(t_1+t_2=1\)). In particular, at \(\eta=1\) and \(\rho=3/4\), a query at \(0\) and a query at \(1/2\) attain gain \(1/44\), whereas every reflection-symmetric pair has gain at most \(1/56\), an exact gap of at least \(3/616\) in explained integral variance. The benchmark's posterior integral variance is exactly \(2/33\). These statements do **not** claim that the reference pair is globally optimal at that finite noise level.

## Assumptions and scope

The observation noises have fixed marginal variance \(\eta\) and fixed equicorrelation \(\rho\), independent of the chosen sites, even for colocated queries. Their covariance is positive definite because \(-1<\rho<1\). The latent covariance matrix at any pair of sites is positive semidefinite. The site domain is compact; covariance and cross-covariance are continuous. A zero of \(g\) need not be an almost surely pinned value for the general theorem; for the Brownian-bridge specialization the endpoints really are pinned. The noise-dominated asymptotic holds with \(\rho\) fixed, not with \(\rho\) approaching \(\pm1\) simultaneously with \(\eta\to\infty\).

## Proof

For \(\mathbf g=(g(t_1),g(t_2))^{\mathsf T}\), write \(R=\begin{psmallmatrix}1&\rho\\\rho&1\end{psmallmatrix}\), and let \(K_2\) be the two-site covariance matrix. Gaussian conditioning gives
\[
G_\eta(t_1,t_2)=\mathbf g^{\mathsf T}(\eta R+K_2)^{-1}\mathbf g.
\]
Since \(K_2\succeq0\) and is uniformly bounded on \(T^2\), the resolvent identity implies, uniformly in both query positions,
\[
\left\|(\eta R+K_2)^{-1}-\eta^{-1}R^{-1}\right\|
\le\frac{\sup_{T^2}\|K_2\|}{\eta^2(1-|\rho|)^2}.
\]
Consequently \(\eta G_\eta\) converges uniformly to
\[
Q(g(t_1),g(t_2))=\frac{g(t_1)^2-2\rho g(t_1)g(t_2)+g(t_2)^2}{1-\rho^2}.
\]
The form \(Q\) is strictly convex because its Hessian is \(2R^{-1}\succ0\). Over \([0,M]^2\), a strict convex quadratic can attain its maximum only at a vertex. The nonzero vertex values are \(Q(M,M)=2M^2/(1+\rho)\) and \(Q(M,0)=Q(0,M)=M^2/(1-\rho^2)\). Their difference has the sign of \(2\rho-1\). Continuity, compactness, and uniform convergence imply that every cluster point of globally maximizing query pairs must realize a maximizing vertex of \(Q\). The assumed unique maximizer and zero set of \(g\) give the claimed location limits. Uniformity also yields the claimed \(O(\eta^{-2})\) optimal-gain remainder. This is an infinite-noise-limit theorem, not an assertion that any finite-\(\eta\) optimizer is exactly at a limiting vertex.

For a Brownian bridge, \(K(u,v)=\min(u,v)-uv\). Direct integration yields \(g(t)=t(1-t)/2\), with \(M=1/8\). The equal-site design \((1/2,1/2)\) and the reference design \((0,1/2)\) give the two rational expressions in the Finding. Their denominators show that the reference beats the repeat precisely when \(2(1-\rho)<1\), equivalently \(\rho>1/2\).

For any reflection-symmetric pair \(t_1=(1-d)/2\), \(t_2=(1+d)/2\), \(0\le d\le1\), conditioning gives the exact gain
\[
G_\eta^{\mathrm{sym}}(d)=\frac{(1-d^2)^2}{16[1-d+2\eta(1+\rho)]}
\le\frac{1}{32\eta(1+\rho)}.
\]
The reference gain is larger than that uniform upper bound if \(2\eta(1+\rho)(2\rho-1)>1\). Hence every reflection-symmetric design is strictly suboptimal in that region. Substitution of \(\eta=1\), \(\rho=3/4\) gives the stated exact fractions. The strict inequality proves nonoptimality of *all* symmetric pairs, not uniqueness or complete identification of the global asymmetric maximizer.

## Verification

The standalone `verify.py` checks the symmetric and reference conditioning identities symbolically; the exact \(\rho=1/2\) benchmark tie; strict convexity and leading-vertex comparison; and the rational witness at \(\eta=1\), \(\rho=3/4\). It further checks 501 rational reflection-symmetric test pairs and 1,200 fixed-seed rational instances against the proved uniform resolvent-error bound. Exact arithmetic is used for the finite tests and symbolic expressions for the critical identities. The general theorem follows from the analytic compactness and convexity proof, not from finite enumeration.

## Relationship to prior work

Attia and Constantinescu (first public preprint July 28, 2020) develop general optimal design with correlated observational errors, including covariance-aware optimization, but the inspected work does not state this two-query high-noise vertex transition or the Brownian-bridge reflection-breaking inequality. Cai, Lam and Scarlett (first public February 22, 2022) study numerical integration with Gaussian observation noise, concentrating on minimax/error-rate bounds with independent noises rather than a fixed correlated two-query location geometry. Existing two-site independent-noise Brownian-bridge integral designs address the special case \(\rho=0\), where this result's high-noise limiting geometry is midpoint coalescence, not the positive-correlation reference regime. A separate correlated-*erasure* quadrature problem is not an equivalent model: failed observations are missing, while here both readings arrive with correlated additive errors. The classical Gaussian-conditioning formula and the Brownian-bridge covariance are prior tools, not newly claimed formulas.

## Limitations

The coefficient \(\rho=1/2\) is a sharp high-noise phase boundary; the theorem leaves the critical correlation's finer asymptotic tie-breaking unresolved. It does not provide the complete finite-noise global phase diagram. The sufficient finite-noise inequality for excluding reflection-symmetric designs is not asserted to be necessary. No conclusion is drawn for site-dependent error covariance, more than two queries, adaptive query placement, or simultaneous singular-noise/high-noise limits. Historical priority is provisional; no independent mathematical audit has been performed.

## References

1. A. Attia and E. Constantinescu, *Optimal Experimental Design for Inverse Problems in the Presence of Observation Correlations*, arXiv:2007.14476 (first posted July 28, 2020), https://arxiv.org/abs/2007.14476.
2. X. Cai, C. T. Lam and J. Scarlett, *On Average-Case Error Bounds for Kernel-Based Bayesian Quadrature*, arXiv:2202.10615 (first posted February 22, 2022), https://arxiv.org/abs/2202.10615.
3. M. Naslidnyk, J. Gonzalez and M. Mahsereci, *Invariant Priors for Bayesian Quadrature*, arXiv:2112.01578 (first posted December 2, 2021), https://arxiv.org/abs/2112.01578.
