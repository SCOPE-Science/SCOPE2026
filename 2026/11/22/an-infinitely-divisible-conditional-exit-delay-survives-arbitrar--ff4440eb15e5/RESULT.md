# An infinitely divisible conditional-exit delay survives arbitrary reset-return overhead

## Finding
Consider diffusion with generator \(D\partial_x^2\) in \((0,L)\), started and independently reset to the same point \(a\), with \(0<a<L/2\) and \(b=L-a\). For every exponential exploration-interruption rate \(r>0\), let \(T_0\) and \(T_L\) denote the **total completion times, including return phases**, conditional on eventual absorption at 0 and \(L\), respectively. Every aborted exploration is followed by an arbitrary almost surely finite return interval and a fresh exploration from \(a\), under the renewal assumptions below.

There exists a strictly positive, nondegenerate random variable \(\Delta_r\), independent of \(T_0\) in a distributional coupling, such that
\[
 T_L\ \stackrel{d}{=}\ T_0+\Delta_r.
\]
This is a full convolution ordering of the farther-target and nearer-target completion-time distributions, not merely an inequality between their means. Its entire delay law is **independent of the distribution and path-dependence of the return durations**. For every \(s\ge0\), its Laplace transform is
\[
 \mathbb E e^{-s\Delta_r}=
 \frac{\sinh\!\left(a\sqrt{(r+s)/D}\right)}{\sinh\!\left(b\sqrt{(r+s)/D}\right)}
 \frac{\sinh\!\left(b\sqrt{r/D}\right)}{\sinh\!\left(a\sqrt{r/D}\right)}.
\]
Set \(\lambda_{\ell,n}=r+D\pi^2n^2/\ell^2\) for \(\ell\in\{a,b\}\) and \(n\ge1\). There is also an almost surely convergent **independent Bernoulli–exponential series**
\[
 \Delta_r\stackrel d=\sum_{n\ge1} B_n E_n,
 \qquad \Pr(B_n=1)=1-\frac{\lambda_{b,n}}{\lambda_{a,n}},
 \qquad E_n\sim\operatorname{Exp}(\lambda_{b,n}),
\]
with all variables on the right independent. Consequently \(\Delta_r\) is infinitely divisible and has Lévy measure \(\nu_r(dt)=v_r(t)dt\), where
\[
 v_r(t)=\frac1t\sum_{n\ge1}
 \left(e^{-\lambda_{b,n}t}-e^{-\lambda_{a,n}t}\right)>0\quad(t>0).
\]
Every positive-integer cumulant is strictly positive and is explicitly
\[
 \kappa_k(\Delta_r)=(k-1)!\sum_{n\ge1}
 \left(\lambda_{b,n}^{-k}-\lambda_{a,n}^{-k}\right),\qquad k=1,2,\ldots.
\]
In particular, the gap between conditional mean completion times, whenever both are finite, equals \(\mathbb E\Delta_r\). This gap is a strictly completely monotone function of \(r>0\): for every integer \(j\ge0\), \((-1)^j d^j\mathbb E\Delta_r/dr^j>0\). Its endpoint behavior is
\[
 \mathbb E\Delta_r\longrightarrow\frac{b^2-a^2}{6D}\quad(r\downarrow0),
 \qquad \mathbb E\Delta_r\sim\frac{b-a}{2\sqrt{Dr}}\quad(r\to\infty).
\]
At a symmetric reset point \(a=b=L/2\), the two conditional laws coincide and the delay collapses to zero; for \(a>L/2\) reverse the target labels.

## Assumptions and scope
1. A new exploration starts at the interior point \(a\) with independent one-dimensional Brownian motion of variance rate \(2D\), \(D>0\), killed upon reaching 0 or \(L\). Each exploration has its own independent rate-\(r>0\) exponential interruption clock. Hitting a target terminates the search immediately.
2. If the clock rings before target absorption, the attempt fails. After an almost surely finite nonnegative return duration \(R\), a fresh, independent exploration from \(a\) begins. The joint law of the failed exploration, its return duration, and any cost marks is allowed to be arbitrary except that the entire failed-cycle law is the same from cycle to cycle, and is independent of the next fresh exploration. Thus \(R\) may depend on interruption time, interruption position, and other failed-cycle marks.
3. Neither target can be absorbed during return, and the return phase is finished before the next independent exploration clock starts. The first exploration also begins at \(a\). The event of a successful attempt, whichever target is reached, has strictly positive probability.
4. \(T_0\) and \(T_L\) denote two separately conditioned random variables; the asserted equality involves an independent **distributional** coupling, not subtraction of times on the same sample path. No finite moment condition is needed for the convolution law. A finite mean (or higher moment) of return overhead is needed only for interpreting differences of the corresponding moments of the completed searches.

## Proof
**1. One-attempt boundary transforms.** Write \(\tau\) for the target-hitting time without interruption and \(J\in\{0,L\}\) for its side. The backward boundary-value equations \(Du''=(r+s)u\) with data 1 at the chosen boundary and 0 at the other yield, for \(s\ge0\),
\[
 f_0(s)=\mathbb E_a[e^{-(r+s)\tau};J=0]
 =\frac{\sinh(bk_s)}{\sinh(Lk_s)},\quad
 f_L(s)=\frac{\sinh(ak_s)}{\sinh(Lk_s)},\quad
 k_s=\sqrt{(r+s)/D}.
\]
These are the joint Laplace weights of a successful uninterrupted exploration ending at each boundary.

**2. Universal failure factor.** Let \(\sigma\) be the interruption clock and define the transform of one entire unsuccessful exploration-plus-return cycle by
\[
 B(s)=\mathbb E[e^{-s(\sigma+R)};\ \sigma<\tau].
\]
This definition remains valid when \(R\) depends on the unsuccessful trajectory. By iid regeneration, the joint transform of total time and eventual side is a convergent geometric sum,
\[
 H_j(s)=\mathbb E[e^{-sT};J=j]=\sum_{m\ge0}B(s)^m f_j(s)
 =\frac{f_j(s)}{1-B(s)},\qquad j\in\{0,L\}.
\]
Here \(0\le B(s)\le B(0)<1\). Dividing \(H_j(s)\) by \(H_j(0)\) gives conditional Laplace transforms \(\Phi_j(s)\), and cancelling the common renewal factor gives
\[
 \frac{\Phi_L(s)}{\Phi_0(s)}
 =\frac{f_L(s)f_0(0)}{f_0(s)f_L(0)}
 =\frac{\sinh(ak_s)}{\sinh(bk_s)}\frac{\sinh(bk_0)}{\sinh(ak_0)}.
\]
In particular, the full failed-cycle history and its return costs are independent of the eventual side; their distribution is the same under both conditionings.

**3. Positivity and exact convolution.** Consider independent Brownian motion on \((0,b)\), initially at \(a\). Let \(\theta_b\) denote its first time at \(b\), and \(\theta_0\) its first time at 0. The ordinary Dirichlet calculation gives
\[
 \mathbb E_a[e^{-q\theta_b};\theta_b<\theta_0]
 =\frac{\sinh(a\sqrt{q/D})}{\sinh(b\sqrt{q/D})},\qquad q>0.
\]
Thus the previous ratio is the Laplace transform of \(\theta_b\) under the probability measure with density proportional to \(e^{-r\theta_b}\mathbf1_{\{\theta_b<\theta_0\}}\). This probability measure is proper because the denominator is strictly positive. Define \(\Delta_r\) with this law. It is strictly positive almost surely. The equality \(\Phi_L=\Phi_0\mathbb E e^{-s\Delta_r}\), uniqueness of Laplace transforms and an independent product-space coupling prove the assertion.

**4. Infinite product, a.s. series and infinite divisibility.** The classical locally uniformly convergent product \(\sinh z=z\prod_{n\ge1}(1+z^2/(\pi^2n^2))\) gives
\[
 \mathbb E e^{-s\Delta_r}=\prod_{n\ge1}
 \frac{1+s/\lambda_{a,n}}{1+s/\lambda_{b,n}}.
\]
Since \(a<b\), \(\lambda_{b,n}<\lambda_{a,n}\). Each factor is the Laplace transform of \(B_nE_n\), where \(E_n\) is exponential of rate \(\lambda_{b,n}\) and \(B_n\) is Bernoulli with success probability \(1-\lambda_{b,n}/\lambda_{a,n}\). Their expectation series is
\[
 \sum_{n\ge1}\mathbb E[B_nE_n]
 =\sum_{n\ge1}(\lambda_{b,n}^{-1}-\lambda_{a,n}^{-1})<\infty,
\]
so the sum converges and is finite almost surely. Independence and convergence of its finite-product Laplace transforms establish the distributional representation.

For each factor, elementary integration gives
\[
 \log\frac{1+s/\lambda_{a,n}}{1+s/\lambda_{b,n}}
 =-\int_0^\infty(1-e^{-st})
 \frac{e^{-\lambda_{b,n}t}-e^{-\lambda_{a,n}t}}t\,dt.
\]
Tonelli's theorem applies because the summands in the Lévy density are positive. The first-moment sum above guarantees \(\int_0^1t\nu_r(dt)<\infty\), and exponential decay gives \(\nu_r([1,\infty))<\infty\). Therefore this is a valid drift-free subordinator Lévy–Khintchine exponent, proving infinite divisibility without relying on a heuristic product-to-law inference.

**5. Cumulants, strictness and limits.** Expanding the convergent logarithmic product at \(s=0\) proves the displayed cumulant series; its convergence for each fixed integer \(k\ge1\) follows from \(n^{-2k}\). Each summand is strictly positive. Termwise differentiation in \(r\) on compact subsets of \((0,\infty)\) yields complete monotonicity of the mean. At \(r\downarrow0\), dominated convergence and \(\sum_{n\ge1}n^{-2}=\pi^2/6\) give the first endpoint. Alternatively, differentiating the hyperbolic-sine transform at \(s=0\) yields
\[
 \mathbb E\Delta_r=\frac{b\coth(b\sqrt{r/D})-a\coth(a\sqrt{r/D})}{2\sqrt{Dr}},
\]
which gives the high-rate asymptotic by \(\coth z\to1\). Strict stochastic ordering follows from an independent strictly positive \(\Delta_r\).

## Verification
Run \(\texttt{python verify.py}\) with Python 3 (standard library only). The script checks conditional-transform cancellation under two illustrative return-time mixtures, the product formula against the hyperbolic ratio with 50,000 spectral factors, positive cumulant sums, and analytic zero-rate limits. It performs 120 numerical/algebraic checks. The infinite-product convergence, positivity of the Lévy density and convolution identity are proved above, not inferred from numerical truncation.

## Relationship to prior work
Pal, Dagdug, Ghosh, Boyer and Pal (2025) derive the general conditional-exit renewal current (their Eq. (4)), conditional mean formula (Eq. (10)), and an absorbing-interval example. Pal and Prasad (2019) provide corresponding classical interval-reset formulas. Those ingredients are credited, and neither formula is presented as new. The present finding extracts a stronger **factorable conditional-law difference** and proves that it is a positive, infinitely divisible independent delay with explicit all-order cumulants, **invariant under arbitrary regenerative return-time overhead**. This is distinct from a comparison of unconditional mean hitting times, a generic outcome-bias criterion, or a bare likelihood-ratio/stochastic-order comparison. Newton and Vega Coso (2026) investigate exit-side stochastic orders and reset bias; their accessible abstract does not settle whether they prove the exact convolution or Lévy claim. Pitman and Yor (2000/2002) study infinitely divisible laws of hyperbolic functions, and spectral first-hitting-time representations are classical. These are material priority comparisons, not claims of novelty for hyperbolic functions or renewal theory themselves.

## Limitations
The proof relies on a common reset/initial site, exponential exploration clocks, independent regenerative cycles, and suppression of absorption during physical return. It does not cover target absorption while returning, resetting to a changed location, interaction between cycles, or an arbitrary nonexponential reset clock. No pathwise monotonicity between two naturally paired trajectories is claimed. When the return duration has infinite moments, conditional mean/variance differences need not be well-defined even though the exact convolution law remains valid. The external literature comparison cannot exclude every implicit equivalent or all contents of access-restricted sources; no independent scientific validation has occurred.

## References
- S. Pal, L. Dagdug, D. Ghosh, D. Boyer, and A. Pal, *Universal criterion for selective outcomes under stochastic resetting* (first public 2025-02-13), https://arxiv.org/abs/2502.09127.
- A. Pal and V. V. Prasad, *First passage under stochastic resetting in an interval* (arXiv 2018, published 2019), https://arxiv.org/abs/1812.03009.
- T. Newton and J. A. Vega Coso, *Stochastic Orders of the Exit Pair and the Monotone Response to Resetting* (first public 2026-11-01), https://arxiv.org/abs/2611.01756.
- J. Pitman and M. Yor, *Infinitely divisible laws associated with hyperbolic functions* (2000 technical report, 2002 journal), https://statistics.berkeley.edu/tech-reports/581.
- E. A. van Doorn, *An Orthogonal-Polynomial Approach to First-Hitting Times of Birth–Death Processes* (2015 online), https://doi.org/10.1007/s10959-015-0659-z.
- P. C. Bressloff, *Search processes with stochastic resetting and multiple targets* (2020), https://doi.org/10.1103/PhysRevE.102.022115. Full original was not accessible at review time.
