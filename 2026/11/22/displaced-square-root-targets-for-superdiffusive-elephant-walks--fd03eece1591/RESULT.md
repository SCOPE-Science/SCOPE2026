# Displaced square-root targets for superdiffusive elephant walks: a Brownian range law

## Finding

Let \((S_m)_{m\geq0}\) be the classical one-dimensional elephant random walk with memory parameter \(p\in(3/4,1)\) and arbitrary first-step bias \(q\in[0,1]\). Put \(a=2p-1\in(1/2,1)\), \(\delta=2a-1>0\), and \(V=1/\delta\). For every deterministic sequence of integers \(k_n\) satisfying \(k_n/\sqrt n\to c\in\mathbb R\), the singleton target \(\{k_n\}\) is held fixed throughout the trajectory whose last-visit time is
\[
T_{k_n}=\sup\{m\geq0:S_m=k_n\},\qquad\sup\varnothing=0.
\]
Then
\[
\boxed{\lim_{n\to\infty}n^{a-1/2}\Pr(T_{k_n}\geq n)
=f_a(0)\,\mathcal K_a(c),}
\]
where \(f_a(0)>0\) is the density at zero of the superdiffusive elephant-walk limit (independent of \(q\)), and
\[
\mathcal K_a(c)=\mathbb E\bigl[\operatorname{osc}_{0\leq u\leq V}
\{B_u-c(1-\delta u)^{a/\delta}\}\bigr],
\qquad \operatorname{osc}g=\sup g-\inf g,
\]
for standard Brownian motion \(B\) started at zero. In particular, \(\mathcal K_a\) is **even, convex and strictly increasing on** \([0,\infty)\), and
\[
\mathcal K_a(0)=\sqrt{\frac8{\pi\delta}},\qquad
\max\left\{\mathcal K_a(0),|c|\right\}\leq\mathcal K_a(c)
\leq |c|+\mathcal K_a(0),\qquad
\lim_{|c|\to\infty}\frac{\mathcal K_a(c)}{|c|}=1.
\]
This differs from the large-radius coefficient \(2\) for *centered intervals*: one displaced point and a growing centered interval have different limiting hitting geometries.

There is also an exact conditional spatial limit. Define
\[
h_{a,c}(z)=\Pr\{\exists u\in[0,V]:z+B_u=c(1-\delta u)^{a/\delta}\}.
\]
Conditionally on \(T_{k_n}\geq n\), the rescaled position \(S_n/\sqrt n\) converges weakly to a random variable with density \(h_{a,c}(z)/\mathcal K_a(c)\). The density is normalized by the range identity \(\int_{\mathbb R}h_{a,c}(z)\,dz=\mathcal K_a(c)\). All statements hold for every fixed admissible \(p,q,c\) and every sequence \(k_n\) with the indicated limit.

## Assumptions and scope

The walk starts at \(S_0=0\), with \(S_1=1\) with probability \(q\) and \(-1\) otherwise. For every \(m\geq1\),
\[
\Pr(S_{m+1}=x+1\mid S_m=x)=\tfrac12(1+ax/m),\quad
\Pr(S_{m+1}=x-1\mid S_m=x)=\tfrac12(1-ax/m).
\]
Only admissible lattice states \(x\equiv m\pmod2\), \(|x|\leq m\), occur. The target \(k_n\) may depend on the observation index \(n\), but not on the walk time \(m\) while \(T_{k_n}\) is evaluated. In particular this is **not** a time-dependent moving-target problem. The condition \(k_n/\sqrt n\to c\) allows rounding and arbitrary lower-order perturbations.

We use the established uniform superdiffusive lattice local limit theorem of Trinas and Valle (2026):
\[
\sup_{x\equiv n\ (\mathrm{mod}\,2)}\left|\frac{n^a}{2}\Pr(S_n=x)-f_{q,a}(x/n^a)\right|\longrightarrow0,
\qquad \sup_x\Pr(S_n=x)\leq C_an^{-a},
\]
where \(f_{q,a}\) is continuous and \(f_{q,a}(0)=f_a(0)>0\). The future-martingale Gaussian functional limit and standard martingale concentration bounds are recalled and applied below. These published inputs, not finite experimentation, support the infinite-scale theorem.

## Proof

**1. Normalize the future walk.** Fix an observation index \(n\), a starting state \((n,x)\), and put
\[
R_{n,m}=\prod_{j=n}^{m-1}(1+a/j)^{-1},\quad
M_m=R_{n,m}S_m,\qquad m\geq n.
\]
The transition rule gives \(\mathbb E[S_{m+1}\mid S_m]=(1+a/m)S_m\), so \((M_m)_{m\geq n}\) is a martingale with \(M_n=x\) and \(|M_{m+1}-M_m|\leq2R_{n,m+1}\). Uniformly for bounded \(t\),
\[
R_{n,n+\lfloor nt\rfloor}\longrightarrow(1+t)^{-a},\quad
n^{-1}\sum_{m=n}^{n+\lfloor nt\rfloor-1}R_{n,m+1}^2
\longrightarrow v_a(t)=\frac{1-(1+t)^{-\delta}}{\delta}.
\]
Indeed logarithmic comparison of the product with the integral gives a uniform \(O(n^{-1})\) error on bounded intervals. The predictable variance increment is
\(R_{n,m+1}^2\{1-a^2S_m^2/m^2\}\). From
\(\mathbb E[S_{m+1}^2\mid S_m]=(1+2a/m)S_m^2+1\), one obtains \(\sup_{n\leq m\leq n(1+T)}\mathbb E_{n,x}[S_m^2]\leq C_{a,T,K}n\) whenever \(|x|\leq K\sqrt n\). Hence the predictable-variance correction divided by \(n\) vanishes. Bounded increments give the martingale Lindeberg condition. The martingale functional central limit theorem, also stated in Trinas (2026, Theorem 3.4), therefore yields, for any \(x_n/\sqrt n\to z\),
\[
\left(M_{n+\lfloor nt\rfloor}/\sqrt n\right)_{0\leq t\leq T}
\Longrightarrow\bigl(z+B_{v_a(t)}\bigr)_{0\leq t\leq T}.
\]
The total future squared-increment bound and its tail are
\[
\sum_{m\geq n}(2R_{n,m+1})^2\leq C_an,\qquad
\sum_{m\geq n+\lfloor nT\rfloor}(2R_{n,m+1})^2\leq C_an(1+T)^{-\delta}
\]
for \(T\geq1\), with constants independent of \(n,x\).

**2. Crossing a fixed, displaced integer point.** Define
\(H_{n,T}(x)=\Pr_{n,x}\{S_m=k_n\text{ for some }n\leq m\leq n+\lfloor nT\rfloor\}\).
A hit is exactly a zero of \(M_m-R_{n,m}k_n\). Since \(S_m-k_n\) changes by nearest-neighbor integer steps, a sign crossing, or equality at the initial time, forces an exact integer hit. On \([0,T]\), the scaled target curve converges uniformly to \(c(1+t)^{-a}\). Applying the functional limit and the continuity-set theorem to the minimum (from above) or maximum (from below) of the signed difference gives
\[
H_{n,T}(x_n)\longrightarrow
h_{a,c,T}(z):=\Pr\{\exists t\in[0,T]:z+B_{v_a(t)}=c(1+t)^{-a}\}.
\]
For \(z\ne c\), the shifted Brownian minimum or maximum has no atom at the crossing level: on a finite interval the deterministic curve is continuously differentiable, so its Brownian drift is absolutely continuous with respect to Brownian law (Cameron–Martin), whose one-sided extrema have atomless distributions. For \(z=c\), Brownian motion crosses both sides of the boundary immediately almost surely, so the hitting probability tends to one even when \(x_n\ne k_n\). The function \(h_{a,c,T}\) is continuous in \(z\); sequential convergence then gives convergence uniform over \(|x|\leq K\sqrt n\) for fixed \(K,T\).

**3. Eliminate late hits.** Let \(m_T=n+\lfloor nT\rfloor\). If the point is hit at some \(m\geq m_T\), then, for every \(\eta>0\), at least one of
\[
|M_{m_T}|\leq\eta\sqrt n+|k_n|R_{n,m_T},\qquad
\sup_{m\geq m_T}|M_m-M_{m_T}|\geq\eta\sqrt n
\]
occurs, because \(|R_{n,m}k_n|\leq R_{n,m_T}|k_n|\). The first event has, for \(T\geq1\), limiting probability at most
\(C_a\{\eta+|c|(1+T)^{-a}\}\), uniformly over starting states \(|x|\leq K\sqrt n\), by the Gaussian endpoint limit and bounded normal density. Doob's \(L^2\) inequality and the tail of the squared increments bound the second probability by \(C_a\eta^{-2}(1+T)^{-\delta}\). Choosing \(\eta=(1+T)^{-\delta/4}\) and letting \(T\to\infty\) gives a uniform negligible late-hit probability. In the Brownian clock \(u=v_a(t)\in[0,V)\), the boundary becomes
\[
b_c(u)=c(1-\delta u)^{a/\delta},\qquad b_c(V)=0.
\]
The compact-time probabilities increase to
\(h_{a,c}(z)=\Pr\{\exists u\in[0,V]:z+B_u=b_c(u)\}\). Consequently \(H_n(x_n)\to h_{a,c}(z)\) along every \(x_n/\sqrt n\to z\), and uniformly on compact scaled starting-state windows. A possible hit only at the endpoint \(u=V\) changes no probability because \(z+B_V\) has a continuous density.

**4. Control distant starting sites and average.** For \(|x|>|k_n|\), any future hit forces a martingale displacement of at least \(|x|-|k_n|\); maximal Azuma–Hoeffding gives
\[
H_n(x)\leq 2\exp\{-((|x|-|k_n|)_+)^2/(C_an)\}.
\]
For the remaining \(x\), this inequality is harmless after enlarging its prefactor. Since \(|k_n|=O(\sqrt n)\), the right-hand side is integrable as a function of \(x/\sqrt n\), uniformly in \(n\) outside a fixed compact set. Conditioning at time \(n\) gives
\[
\Pr(T_{k_n}\geq n)=\sum_{x\equiv n\ (\mathrm{mod}\,2)}\Pr(S_n=x)H_n(x).
\]
For \(|x|\leq K\sqrt n\), the local limit theorem gives
\(\Pr(S_n=x)=2n^{-a}(f_a(0)+o(1))\) uniformly, and the starting-site lattice has mesh \(2/\sqrt n\). The Riemann sum tends to \(f_a(0)\int_{-K}^K h_{a,c}(z)\,dz\). The uniform global mass bound and exponential hitting envelope eliminate the tails as \(K\to\infty\). Therefore
\[
\lim_n n^{a-1/2}\Pr(T_{k_n}\geq n)=f_a(0)\int_{\mathbb R}h_{a,c}(z)\,dz.
\]
The same Riemann-sum argument with a bounded continuous test function \(\phi(x/\sqrt n)\), and the just-proved positive normalization, yields the conditional spatial density asserted in the finding.

**5. Identify the Brownian range.** For each continuous Brownian sample path, the values of \(z\) for which \(z+B_u=b_c(u)\) holds at some \(u\in[0,V]\) form the image of a continuous path \(b_c(u)-B_u\). Hence this set is an interval whose length equals the oscillation of \(B_u-b_c(u)\). Tonelli's theorem gives
\[
\int_{\mathbb R}h_{a,c}(z)\,dz
=\mathbb E\bigl[\operatorname{osc}_{0\leq u\leq V}(B_u-b_c(u))\bigr]=\mathcal K_a(c).
\]
The expectation is finite because the Brownian expected range is finite and \(\operatorname{osc}b_c=|c|\).

**6. Geometry of the constant.** For each path, the oscillation of \(B-cb_1\) is the maximum of affine functions of \(c\) minus their minimum, hence convex in \(c\). Brownian sign symmetry makes its expectation even. For \(c\ne0\), midpoint convexity is strict in expectation: on the positive-probability event \(\sup_{u\leq V}|B_u|<|c|/8\), the sum of the oscillations of \(B+cb_1\) and \(B-cb_1\) is at least \(2|c|-4(|c|/8)\), whereas twice the oscillation of \(B\) is less than \(4(|c|/8)\). Thus \(\mathcal K_a(c)>\mathcal K_a(0)\) for every \(c\ne0\). Evenness and convexity now force strict increase on the positive half-line. Brownian reflection gives \(\mathcal K_a(0)=2\mathbb E\sup_{u\leq V}B_u=\sqrt{8V/\pi}\). Jensen's inequality for the convex oscillation functional yields \(\mathcal K_a(c)\geq\operatorname{osc}(-cb_1)=|c|\), while strict minimality gives \(\mathcal K_a(c)\geq\mathcal K_a(0)\). The pathwise inequality
\[
\bigl|\operatorname{osc}(B-cb_1)-|c|\bigr|\leq\operatorname{osc}(B)
\]
provides the upper bound and implies \(\mathcal K_a(c)/|c|\to1\). The theorem is proved.

## Verification

Run `python3 verify.py` (standard Python library only) to reproduce exact rational checks of the elephant transition and future-martingale identities, exhaustive finite-tree versus dynamic-programming checks of singleton hitting, deterministic range inequalities and seeded Brownian-grid numerical diagnostics. All countable-check statements and sample sizes are printed by the program. These finite tests are sanity checks; the universal asymptotics and monotonicity are consequences of the analytical argument and the cited local/functional limit inputs, not of Monte Carlo evidence.

## Relationship to prior work

Trinas (2026, arXiv:2611.01279v1, first publicly available 2026-10-31), Theorem 1.1 and Corollary 8.2, prove the last-return constant for zero and for targets contained in a window of size \(o(\sqrt n)\). Section 10 expressly leaves comparable-to-\(\sqrt n\) *target locations* open. Its future-martingale functional limit and subsequent hitting bounds are explicitly used here. The independently published earlier theorem *Critical-scale interval last visits for superdiffusive elephant random walks* (published-finding corpus, 2026-11-08, identifier `07dd1168bd98`) covers a **symmetric interval centered at zero** with radius \(c\sqrt n\), not a singleton displaced by \(c\sqrt n\). Its Brownian **swept-interval** constant is \(2\mathbb E\sup(B_u+c(1-\delta u)^{a/\delta})\), in contrast to the **swept-point** Brownian-range constant here. Neither symmetric-interval coverage nor spatial translation gives the singleton statement: the elephant transition probability depends on the absolute position. Trinas and Valle (2026, arXiv:2609.14753v1) supply the uniform local limit theorem used in the averaging step. Classical smooth-boundary Brownian hitting analysis, e.g. Salminen (1988), concerns Brownian paths rather than this elephant-walk last-visit law and does not by itself supply the required combination of finite-horizon, infinite-horizon, and lattice averaging arguments.

## Limitations

The memory parameter is fixed strictly inside the superdiffusive range, and the singleton location is a fixed finite multiple of \(\sqrt n\) at the observation scale. The target is frozen throughout each trajectory. No uniformity as \(a\downarrow1/2\) or \(a\uparrow1\), no error rate in \(n\), no growing target width, no time-dependent tracking, and no explicit elementary closed form for \(\mathcal K_a(c)\) when \(c\ne0\) are asserted. The proof relies on the published superdiffusive local limit theorem and standard martingale Gaussian convergence. The result has not received independent mathematical auditing or exhaustive priority certification.

## References

- H. Trinas, *The Prodigal Elephant Returns: Last-Return Laws in the Superdiffusive Regime*, arXiv:2611.01279v1, first submitted 2026-10-31, especially Theorem 3.4, Lemmas 4.2–4.4, Corollary 8.2, Section 10. https://arxiv.org/html/2611.01279v1
- H. Trinas and G. Valle, *A Superdiffusive Local Limit Theorem for the Elephant Random Walk and the Breakdown of Log-Concavity*, arXiv:2609.14753v1, first submitted 2026-09-13, Theorem 3.1. https://arxiv.org/html/2609.14753v1
- *Critical-scale interval last visits for superdiffusive elephant random walks*, published-finding corpus research record `07dd1168bd98`, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-critical-scale-interval-last-visits-for-superdiffusive-elephant--07dd1168bd98
- P. Salminen, *On the first hitting time and the last exit time for a Brownian motion to/from a moving boundary*, Advances in Applied Probability 20 (1988), 411–426, DOI:10.2307/1427397. https://doi.org/10.2307/1427397
- P. Mörters and Y. Peres, *Brownian Motion*, Cambridge University Press (2010), for the reflection principle and standard Brownian range formulas.
