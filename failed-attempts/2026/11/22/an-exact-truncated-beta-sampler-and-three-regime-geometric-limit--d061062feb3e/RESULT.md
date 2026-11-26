# An exact truncated-Beta sampler and three-regime geometric limit for two-rank pointed order polytopes

## Finding
Let \(p,q\ge1\) be integers and let \(P=A_p\oplus A_q\) be the ordinal sum of a lower antichain of size \(p\) and an upper antichain of size \(q\). Fix one lower element \(a\) at value zero and take the pointed order polytope in the Euclidean coordinates of the other \(p+q-1\) elements:
\[
Q_{p,q}=\{(x_1,\ldots,x_{p-1},y_1,\ldots,y_q): -1\le x_i\le1,\ 0\le y_j\le1,\ x_i\le y_j\ \text{for all }i,j\}.
\]
This is the standard \([-1,1]\)-valued pointed-order-polytope realization, with the distinguished coordinate deleted. Put \(N=p+q\), and let \(T=\min_jY_j\) for a Euclidean-volume-uniform point \((X,Y)\) of \(Q_{p,q}\).

**Exact volume and marginal theorem.** Its ordinary \((N-1)\)-dimensional coordinate volume is
\[
\boxed{V_{p,q}=q\int_0^1(1+t)^{p-1}(1-t)^{q-1}\,dt
=\frac{(p-1)!q!}{(N-1)!}\sum_{k=0}^{p-1}\binom{N-1}{k}.}
\]
Consequently the explicit integer number of equal-volume simplex-chain pieces in the general pointed-order-polytope triangulation is
\[
\boxed{(N-1)!V_{p,q}=(p-1)!q!\sum_{k=0}^{p-1}\binom{N-1}{k}.}
\]
Furthermore,
\[
\boxed{\frac{1+T}{2}\ \stackrel{d}{=}\ \operatorname{Beta}(p,q)\ \big|\ \left\{\operatorname{Beta}(p,q)\ge\frac12\right\}.}
\]
This gives an exact sampler without generating or counting simplex chains: draw this truncated Beta variable \(U\), set \(T=2U-1\), uniformly select one of the \(q\) upper coordinates to equal \(T\), sample the other upper coordinates independently uniformly from \([T,1]\), and sample each lower coordinate independently uniformly from \([-1,T]\). The construction yields exactly normalized Euclidean volume on \(Q_{p,q}\).

A second exact finite sampler needs neither a rare-event rejection nor a truncated-Beta primitive. Define
\[
w_k=\binom{p-1}{k}\frac{k!q!}{(k+q)!},\qquad 0\le k\le p-1.
\]
Choose \(K=k\) with probability \(w_k/V_{p,q}\); select uniformly which \(k\) lower coordinates are positive, assign the first \(k\) of \(k+q\) independent \(\operatorname{Uniform}(0,1)\) order statistics to those lower coordinates in random order, and assign the last \(q\) order statistics to the upper coordinates in random order. Assign independent \(\operatorname{Uniform}(-1,0)\) values to the remaining lower coordinates. Both sampling descriptions are exact (up to probability-zero ties).

**Sharp three-regime limit.** Let \(N\to\infty\) through integers \(p=p_N,q=q_N\ge2\), and write \(T_N\) for the minimum upper coordinate:

- If \(p_N/N\to\alpha\in(0,1/2)\), then \(NT_N\Rightarrow\operatorname{Exp}(1-2\alpha)\) (the parameter is a rate), and \(V_{p_N,q_N}\to(1-\alpha)/(1-2\alpha)\).
- If \((p_N-q_N)/\sqrt N\to\lambda\in\mathbb R\), then \(\sqrt N T_N\) converges to a standard normal with mean \(\lambda\), conditioned to be nonnegative. In particular, at \(\lambda=0\) the limit is half-normal, and
\[
\frac{V_{p_N,q_N}}{\sqrt N}\longrightarrow \sqrt{\frac\pi2}\,e^{\lambda^2/2}\Phi(\lambda),
\]
where \(\Phi\) is the standard normal cumulative distribution function.
- If \(p_N/N\to\alpha\in(1/2,1)\), put \(t_N=(p_N-q_N)/(N-2)\). Then \(T_N\to2\alpha-1\) in probability and
\[
\sqrt N(T_N-t_N)\Rightarrow\mathcal N(0,4\alpha(1-\alpha)),\qquad
\frac1N\log V_{p_N,q_N}\longrightarrow \alpha\log(2\alpha)+(1-\alpha)\log(2(1-\alpha)).
\]
The sharp critical window is therefore \(p-q\) of order \(\sqrt N\), separating a boundary-attached exponential law from an interior Gaussian law.

## Assumptions and scope
The pointed poset is exactly the ordinal sum of two antichains and the distinguished neutral element belongs to the lower antichain. The coordinate inequalities are those displayed; all coordinates are ordinary Euclidean coordinates after deleting the fixed zero coordinate. No claim is made about arbitrary pointed posets, arbitrary pin values, or boundary-volume sampling. Each \(p,q\) is a positive integer; the asymptotic limit requires \(p,q\ge2\) eventually, with the stated scaling assumptions. The beta law is the two-shape Beta distribution restricted and renormalized on \([1/2,1]\), not an unconditioned Beta distribution. The exponential law uses rate rather than scale normalization. The critical normal is conditioned on the closed half-line (equivalently, a truncated normal), not reflected or absolute-valued for nonzero \(\lambda\).

## Proof
**1. Exact fibers and volume.** Because the pin is at zero and below every upper element, \(0\le y_j\le1\). Outside the null set of tied minima, one of the \(q\) upper coordinates uniquely realizes \(t=\min_jy_j\). Each of the remaining \(q-1\) upper coordinates ranges independently over \([t,1]\). Every one of the \(p-1\) free lower coordinates ranges independently over \([-1,t]\). Therefore the volume density of such fibers is precisely \(q(1+t)^{p-1}(1-t)^{q-1}\,dt\), proving the integral. With \(u=(1+t)/2\), the kernel becomes \(q2^{N-1}u^{p-1}(1-u)^{q-1}\,du\) on \([1/2,1]\). The elementary beta-binomial tail identity gives
\[
\frac{\int_{1/2}^1u^{p-1}(1-u)^{q-1}\,du}{B(p,q)}
=2^{-(N-1)}\sum_{k=0}^{p-1}\binom{N-1}{k}.
\]
Since \(B(p,q)=(p-1)!(q-1)!/(N-1)!\), the finite binomial sum follows. The simplex-chain count then follows from the general equal-volume triangulation of pointed order polytopes, which assigns volume \(1/(N-1)!\) to each simplex.

**2. Exact samplers.** The same disintegration shows that conditional on \(T=t\), its unique minimizing upper index is uniform in \(\{1,\ldots,q\}\), the other upper coordinates are independent \(\operatorname{Uniform}(t,1)\), and the lower coordinates are independent \(\operatorname{Uniform}(-1,t)\). The marginal of \(U=(1+T)/2\) is precisely the displayed truncated \(\operatorname{Beta}(p,q)\), so the first sampler is uniform in volume. To derive the second, partition \(Q_{p,q}\) by the \(k\) strictly positive lower coordinates. Negative lower coordinates contribute volume one each. Among the other \(k+q\) coordinates, uniform points in \([0,1]^{k+q}\) satisfy all lower-before-upper inequalities with probability \(k!q!/(k+q)!\), because all \((k+q)!\) strict rankings are equally likely. There are \(\binom{p-1}{k}\) ways to select the positive lowers, giving cell volume \(w_k\). Within the chosen cell, independently sorted continuous uniforms and uniform label permutations produce its uniform distribution. Thus \(\sum_kw_k=V_{p,q}\) and the sampler is exact.

**3. Log-concavity and location of mass.** Up to a constant, the density of \(T\) is
\[
h_N(t)=(1+t)^{p-1}(1-t)^{q-1},\qquad 0\le t\le1.
\]
Its logarithmic derivative is
\[
(\log h_N)'(t)=\frac{(p-q)-(N-2)t}{1-t^2},
\]
so the unique mode is zero when \(p\le q\), and is \((p-q)/(N-2)\) when \(p>q\ge2\). Its logarithm is strictly concave in the interior whenever \(N>2\).

**4. Boundary regime.** When \(p/N\to\alpha<1/2\), substitute \(t=z/N\). For fixed \(z\ge0\), \(h_N(z/N)\to e^{-(1-2\alpha)z}\). Moreover \((\log h_N)'(t)\le p-q\) for \(p<q\) and \(t\in[0,1)\), hence \(h_N(z/N)\le\exp(-(q-p)z/N)\); eventually this is bounded by an integrable exponential in \(z\). Dominated convergence for the normalized density proves the exponential limit and \(V_{p,q}\sim q/[N(1-2\alpha)]\), giving the stated volume constant.

**5. Critical window.** If \((p-q)/\sqrt N\to\lambda\), put \(t=z/\sqrt N\). Taylor expansion at zero gives
\[
\log h_N(z/\sqrt N)=\lambda z-\frac{z^2}{2}+o(1)
\]
for every fixed \(z\ge0\). On the full half-line, the second derivative satisfies \((\log h_N)''(t)\le-(q-1)\) for \(t\in[0,1)\), so the scaled integrands are dominated by \(e^{Cz-cz^2}\) for fixed positive constants \(C,c\) and all large \(N\). Dominated convergence yields density proportional to \(e^{\lambda z-z^2/2}\) on \([0,\infty)\). Its normalizer is \(\sqrt{2\pi}e^{\lambda^2/2}\Phi(\lambda)\). Since \(q/N\to1/2\), the identity \(V_{p,q}/\sqrt N=(q/N)\int_0^{\sqrt N}h_N(z/\sqrt N)\,dz\) and the same dominated-convergence argument prove the volume scaling.

**6. Interior regime.** If \(p/N\to\alpha>1/2\), then eventually \(p>q\ge2\) and the unique interior mode is \(t_N=(p-q)/(N-2)\to 2\alpha-1\). Strict concavity separates any fixed neighborhood of the mode from its complement by an exponentially small density ratio. The normalized second derivative at the mode satisfies
\[
\frac1N(\log h_N)''(t_N)\longrightarrow-\frac1{4\alpha(1-\alpha)}.
\]
Standard one-variable Laplace expansion, with domination from strict concavity and the mode bounded away from both endpoints, yields the asserted centered Gaussian limit. Evaluating \(N^{-1}\log h_N(t_N)\) gives \(\alpha\log(2\alpha)+(1-\alpha)\log(2(1-\alpha))\). The prefactor \(q\) and Gaussian integration width have logarithms \(o(N)\), so the volume has the same exponential rate.

## Verification
The standalone file `verification.py` uses only Python standard-library modules. Three independently organized exact-rational calculations (fiber polynomial integration, binomial tail, and sign-pattern cell enumeration) agree on the volume for every \(1\le p,q\le19\): 361 parameter pairs. It additionally evaluates 1,083 exact-rational first-three-moment numerators, checks all corresponding moment bounds, and generates 140,000 valid uniform-sampler points across four parameter pairs. Their empirical means agree with the exact rational marginal means to a stated numerical tolerance. Independent continuous quadrature, used during derivation, checks the three predicted scale regimes at increasing dimensions; its finite results are not proofs. The proof for all parameters and all asymptotic sequences is the analytic argument above.

To reproduce the finite checks, run `python verification.py` in a Python 3 environment. No external data, third-party packages, or files are required.

## Relationship to prior work
Miranda and García-Segador's 2021 paper introduced pointed order polytopes and studied their vertices, edges and faces [1]. García-Segador and Miranda's 2023 article [2] proved that all pointed order polytopes have equal-volume simplex-chain triangulations and a formal uniform sampler based on selecting a simplex chain (Theorem 3, Algorithm 1). These theorems imply integrality of \((N-1)!V_{p,q}\) and generic sampling in principle; they do **not** supply this family-specific binomial coefficient, disintegration, no-chain-enumeration samplers, or the three asymptotic regimes. The combinatorial number of chains is here evaluated explicitly, not claimed to be an independent general triangulation method.

A published two-level signed-chain volume theorem [3] deals with the different, full-dimensional body defined by \(|x_i|,|y_j|,|x_i+y_j|\le1\), with no distinguished neutral element; its volume is a symmetric function of its block sizes. The present \((N-1)\)-dimensional pointed-order-polytope family has a fixed coordinate, one-sided ordinal inequalities, and an asymmetric volume law. Existing two-level ordinary and enriched order-polytope covariance and directional-width results concern different geometric objects or statistics and do not entail the stated truncated-Beta marginal. The normal and exponential limit laws are standard analytical limit types, but identifying their exact sharp scaling and their governing variable for this polytope is the subject of the present result. Priority outside the searched sources is not asserted as certified.

## Limitations
No assertions are made for general pointed posets, other pinned positions, or nonuniform volume measures. The second sampler is mathematically exact; a numerical implementation must represent probabilities and random variables with sufficient precision, and a naive unconditioned Beta rejection sampler may be exponentially inefficient in the boundary regime. The displayed asymptotics do not cover vanishing limiting proportions, which need different scalings. The proof does not establish a computational complexity bound for arbitrary pointed order polytopes. Historical priority is provisional: an unindexed treatment of this exact two-rank slice or a general conditioned-order-statistics theorem could imply part of the result. Independent mathematical validation is not claimed.

## References
[1] P. Miranda and P. García-Segador, *Pointed order polytopes: Studying geometrical aspects of the polytope of bi-capacities*, Fuzzy Sets and Systems 444 (2022), 182–205, DOI:10.1016/j.fss.2021.11.001, publicly available by November 2021; https://doi.org/10.1016/j.fss.2021.11.001.

[2] P. García-Segador and P. Miranda, *A triangulation for pointed order polytopes*, Fuzzy Sets and Systems 470 (2023), article 108655; available online 20 July 2023, DOI:10.1016/j.fss.2023.108655; https://doi.org/10.1016/j.fss.2023.108655.

[3] *Exact volume and strict imbalance law for two-level signed-chain polytopes*, published result, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-volume-and-strict-imbalance-law-for-two-level-signed-chain--84c1d3d87a65.
