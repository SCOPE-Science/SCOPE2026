# Unique uniform-marginal coupling for two-point Brownian-bridge kernel quadrature

## Finding
Let \(B\) be a standard Brownian bridge on \([0,1]\), with covariance \(K(s,t)=\min(s,t)-st\), and let \(J=\int_0^1B(t)\,dt\). Two noiseless observation sites \((X,Y)\) are drawn independently of \(B\), with **each individual marginal uniformly distributed on \([0,1]\)**, but with their joint dependence otherwise completely unrestricted. For each realized pair, estimate \(J\) by its Gaussian conditional mean given \(B(X),B(Y),X,Y\). Let \(V(X,Y)\) denote the conditional variance of \(J\) given the sites and observations (equivalently the squared worst-case error of the fixed-site optimal kernel quadrature rule on the unit ball of \(H_0^1(0,1)\)).

**Theorem.** Among **every Borel coupling of two uniform \([0,1]\) marginals**, the unique joint law minimizing \(\mathbb E V(X,Y)\) is the half-period cyclic translation
\[
Y=\tau(X)=\begin{cases}X+\tfrac12,&0\le X<\tfrac12,\\ X-\tfrac12,&\tfrac12\le X\le1,\end{cases}\qquad X\sim\mathrm{Uniform}[0,1],
\]
up to the inconsequential definition of \(\tau\) on null sets. Its exact minimum is
\[
\boxed{\inf_{\mathcal L(X)=\mathcal L(Y)=U[0,1]}\mathbb E V(X,Y)=\frac1{64}.}
\]
For comparison, two **independent** uniforms give \(1/40\), while central reflection \(Y=1-X\) gives \(5/192\). Thus the uniquely optimal dependence reduces expected conditional variance by precisely \(37.5\%\) compared with independence and \(40\%\) compared with central reflection. The half-period sampling construction is classical; the claim is its exact **global uniqueness and sharp risk bound for this specific conditional-variance criterion** under arbitrary Borel dependence.

## Assumptions and scope
All integrals are over \([0,1]\). The bridge is centered, pinned at both endpoints, and has covariance \(K(s,t)=\min(s,t)-st\). Its sample-site randomization is independent of the bridge and is fully revealed to the estimator. Observations are noiseless. The estimator is the conditional Gaussian mean and is allowed to use site-dependent (not necessarily equal) weights. Both sites must each have the exactly uniform marginal law; the joint law may be discrete-conditionally supported, singular or absolutely continuous, and is not assumed exchangeable. Site collisions and boundary locations are included, using the obvious redundant-observation interpretation. The criterion is **expected posterior integral variance**, \(\mathbb E_{X,Y}[\operatorname{Var}(J\mid B(X),B(Y),X,Y)]\), equivalently expectation of the squared *fixed-site* RKHS worst-case error. It is not the distinct minimax objective \(\sup_f \mathbb E_{X,Y}|J(f)-Q_{X,Y}(f)|^2\).

## Proof
**1. Fixed-site risk.** Sort the two sites into \(0\le a\le b\le1\). Conditional on the observations, the residual process on each of \([0,a]\), \([a,b]\), and \([b,1]\) is an independent centered Brownian bridge rescaled to that interval (zero-length intervals contribute nothing). Its integrated covariance on an interval of length \(h\) equals
\[
\int_0^h\int_0^h\left(\min(s,t)-\frac{st}{h}\right)\,ds\,dt=\frac{h^3}{12}.
\]
Therefore the posterior integral variance is
\[
V(x,y)=\frac1{12}\left[\min(x,y)^3+|x-y|^3+(1-\max(x,y))^3\right].\tag{1}
\]
The same expression is obtained from the \(2\times2\) Gaussian conditioning formula at distinct interior nodes, and extends continuously through collisions and endpoints.

**2. Explicit global dual certificate.** Let \(c(x,y)=12V(x,y)\) and define the continuous, reflection-symmetric piecewise cubic function
\[
\phi(x)=\begin{cases}x^3-\frac34x+\frac14,&0\le x\le\frac12,\\ (1-x)^3+\frac34x-\frac12,&\frac12\le x\le1.\end{cases}\tag{2}
\]
We prove the **pointwise inequality**
\[
\boxed{c(x,y)\ge\phi(x)+\phi(y)\quad(0\le x,y\le1),}\tag{3}
\]
with equality exactly when \(|x-y|=1/2\).

By symmetry in \(x,y\), it suffices to take \(x\le y\). If \(x\le1/2\le y\), put \(d=y-x\). A direct polynomial identity gives
\[
c(x,y)-\phi(x)-\phi(y)=d^3-\frac34d+\frac14=(d-\tfrac12)^2(d+1)\ge0,\tag{4}
\]
with equality if and only if \(d=1/2\).

If \(0\le x\le y\le1/2\), put \(F(x,y)=c(x,y)-\phi(x)-\phi(y)\). Then
\[
\frac{\partial F}{\partial x}(x,y)=\frac34-3(y-x)^2\ge0,
\qquad F(0,y)=(2-y)(\tfrac12-y)^2\ge0.\tag{5}
\]
Equality in this region occurs only at \((x,y)=(0,1/2)\), which already obeys \(|x-y|=1/2\). The region \(1/2\le x\le y\le1\) follows by reflecting both arguments, since \(c(1-x,1-y)=c(x,y)\) and \(\phi(1-x)=\phi(x)\). This proves (3) and its exact equality set without an appeal to numeric optimization.

**3. Integrate over all couplings.** Each marginal is uniform, so for every admissible joint law
\[
12\mathbb E V(X,Y)=\mathbb E c(X,Y)\ge\mathbb E\phi(X)+\mathbb E\phi(Y)
=2\int_0^1\phi(t)\,dt=\frac3{16},\tag{6}
\]
because \(\int_0^1\phi(t)\,dt=3/32\). The half-period map \(\tau\) preserves Lebesgue measure, and \(|X-\tau(X)|=1/2\) almost surely, so it attains equality in (3) pointwise, giving \(\mathbb E V= (3/16)/12=1/64\).

If an admissible joint law attains the minimum, the nonnegative, bounded deficit in (3) has expectation zero. Its equality characterization forces \(|X-Y|=1/2\) almost surely. For each \(x\in(0,1/2)\) there is exactly one \(y\in[0,1]\) at distance \(1/2\), namely \(x+1/2\); for each \(x\in(1/2,1)\) it is \(x-1/2\). Since \(X\) is atomless, the joint law is uniquely \((\mathrm{id},\tau)_\#U[0,1]\).

**4. Exact benchmark risks.** For independent \(X,Y\sim U[0,1]\), the three ordered gaps have Dirichlet\((1,1,1)\) law. Their expected sum of cubes is \(3/10\), hence \(\mathbb E V=1/40\). For the central reflection coupling \(Y=1-X\), its smaller site \(a=\min(X,1-X)\) is uniform on \([0,1/2]\). Thus
\[
12\mathbb E V=2\int_0^{1/2}\left[2a^3+(1-2a)^3\right]da=\frac5{16},
\]
giving \(5/192\). These comparisons use the same conditional-mean estimator and the same fixed-site loss, changing only the coupling.

## Verification
The standalone standard-library Python program `verify.py` carries out exact rational tests of the dual inequality and its equality set on dense finite rational grids, checks the left/left lower bound and cross-half factorization at rational points, and compares the exact \(2\times2\) Gaussian-conditioning formula against (1) for distinct interior rational sites. It also checks the exact integrals for the optimal, independent and central-reflection couplings. Run `python verify.py` with Python 3.10 or later; no external packages are required. The analytic inequalities (4)–(5), integration and equality characterization are the infinite-dimensional proof; the finite checks do not constitute such a proof independently.

## Relationship to prior work
Briol, Oates, Cockayne, Chen and Girolami (2017) study the distribution-selection problem for kernel quadrature and motivate sensitivity to random sites, but their displayed design formulation optimizes an iid sampling law and uses a different supremum/expectation ordering. Santin (2022) treats Brownian-bridge kernel interpolation, exact cardinal functions and the *deterministic* equally spaced placement minimizing maximum pointwise interpolation power; that criterion does not impose individually uniform random sites or optimize over copulas. Cai, Lam and Scarlett (2022) establish general noisy and randomized Bayesian-quadrature error bounds but not an exact joint-distribution optimizer under uniform marginals. Hayakawa, Oberhauser and Lyons (2023) address general Nyström kernels, potentially non-iid landmarks and convex quadrature guarantees; their results do not state this two-node posterior-variance copula classification.

The published work *Unique optimal i.i.d. two-node design for Brownian-bridge kernel quadrature* (2026) derives a nonuniform, truncated optimal **iid marginal density** for the same bridge kernel and fixed-site expected loss. Its proof gives the same cubic-gap objective, but its admissible laws are \(\mu\otimes\mu\), whereas the present theorem fixes **both marginals** to \(U[0,1]\) and optimizes all dependence; neither theorem is a corollary of the other, and the optimized values differ. The half-period systematically shifted pair is a familiar randomized lattice construction; no novelty is claimed for the construction itself. The contribution claimed here is the sharp all-copula lower bound, exact dual certificate, and uniqueness for this specific conditional-variance objective.

## Limitations
This theorem is for exactly two, noiseless, independently-of-process sampled sites, a pinned first-order Brownian bridge, an integral target with uniform weight, and a restriction of individually uniform site marginals. Its optimal loss \(1/64\) is not the unrestricted deterministic two-site optimum \(1/108\). It does not prove superiority for an arbitrary deterministic integrand, higher sample counts, noisy observation, adaptive design, alternate kernels or the worst-integrand-after-randomization objective. Classical systematic sampling and optimal-transport literature could contain an equivalent special case; an unrestricted publication-priority claim would require further specialist comparison. The mathematical proof is self-contained; independent validation has not been performed.

## References
1. F.-X. Briol, C. J. Oates, J. Cockayne, W. Y. Chen and M. Girolami, *On the Sampling Problem for Kernel Quadrature*, arXiv:1706.03369v1, first public 2017-06-11, Sections 1–3, https://arxiv.org/abs/1706.03369.
2. G. Santin, *Equally spaced points are optimal for Brownian Bridge kernel interpolation*, arXiv:2210.15959v1, first public 2022-10-28, Sections 2 and 4–5, https://arxiv.org/abs/2210.15959.
3. X. Cai, C. T. Lam and J. Scarlett, *On Average-Case Error Bounds for Kernel-Based Bayesian Quadrature*, arXiv:2202.10615v1, first public 2022-02-22, Sections 1–4, https://arxiv.org/abs/2202.10615.
4. S. Hayakawa, H. Oberhauser and T. Lyons, *Sampling-based Nyström Approximation and Kernel Quadrature*, arXiv:2301.09517v1, first public 2023-01-23, Sections 2–5 and Appendix, https://arxiv.org/abs/2301.09517.
5. *Unique optimal i.i.d. two-node design for Brownian-bridge kernel quadrature*, published research record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-unique-optimal-i-i-d-two-node-design-for-brownian-bridge-kernel--1c7b05ec88c4.
