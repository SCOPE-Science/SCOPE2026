# Sharp Laplace envelopes and factorial stability of normalized positive chains

## Finding

For each integer \(N\ge1\), consider any probability-law chain \(\mu_0,\ldots,\mu_N\) on \([0,\infty)\) satisfying \(F(\mu_j)=\mu_{j+1}\) for \(0\le j<N\), where \(F\) is the positive infinitely divisible logarithmic-Laplace derivative map. Put
\[
q_j(s)=\int_{[0,\infty)}e^{-sx}\,\mu_j(dx),\qquad
(\mathcal T f)(s)=\exp\left(-\int_0^s f(u)\,du\right),
\qquad h_0\equiv0,\qquad h_{n+1}=\mathcal T h_n.
\]
Then for **every** \(s\ge0\),
\[
\boxed{\min\{h_N(s),h_{N+1}(s)\}\ \le q_0(s)\le\ \max\{h_N(s),h_{N+1}(s)\}.}
\]
Both endpoints are **pointwise optimal** over all such normalized chains: \(h_{N+1}\) is attained throughout by one chain, and \(h_N\) is the locally uniform limit of valid chains. In particular, with \(q_*(s)=(1+s)^{-1}\), the *exact* worst-case transform discrepancy is
\[
\boxed{
\sup_{\mu_0\,\text{of depth }N}|q_0(s)-q_*(s)|
=\max\{|h_N(s)-q_*(s)|,|h_{N+1}(s)-q_*(s)|\}.}
\]
Furthermore the following **global**, factorial-rate estimate holds simultaneously for every \(s\ge0\):
\[
\boxed{|q_0(s)-(1+s)^{-1}|\le \frac{s^N}{N!}.}
\]
The multiplicative constant one is locally sharp at each depth:
\[
\lim_{s\downarrow0}\frac{N!}{s^N}
\sup_{\mu_0\,\text{of depth }N}|q_0(s)-(1+s)^{-1}|=1.
\]
This is an optimal finite-depth transform-capacity theorem; no assertion of total-variation convergence or of uniqueness of finite chains is intended.

## Assumptions and scope

The chain comprises \(N+1\) **probability measures**, not merely positive locally finite measures. Every \(\mu_j\) is supported on \([0,\infty)\). Whenever \(F(\mu_j)\) is defined, it is characterized by
\[
q_{F(\mu_j)}(s)=-\frac{d}{ds}\log q_j(s),\quad s>0.
\]
The integer \(N\) is arbitrary but finite. There is no support bound and no assumption on the moments of the terminal law \(\mu_N\). For \(s=0\), all displayed transform bounds follow by continuity. The formal function \(h_0\equiv0\) is a comparison function **not** itself a probability transform; each \(h_n\), \(n\ge1\), is a limit of valid transforms under the stated constructions.

## Proof

**1. Inversion by a probability-valued map.** For any probability measure \(\nu\) on \([0,\infty)\), set
\[
\kappa=\nu(\{0\}),\qquad
L(dx)=\frac{\mathbf1_{(0,\infty)}(x)}{x}\,\nu(dx).
\]
Since
\[
\int_{(0,\infty)}\min(1,x)L(dx)
=\nu((0,1])+\int_{(1,\infty)}x^{-1}\nu(dx)\le1,
\]
\(L\) is a legitimate Lévy measure. Let \(G\nu\) be the probability law of the associated nonnegative infinitely divisible variable with drift \(\kappa\) and Lévy measure \(L\). Its Laplace transform is
\[
q_{G\nu}(s)=\exp\left(-\kappa s-\int_{(0,\infty)}\frac{1-e^{-sx}}{x}\nu(dx)\right)
=\exp\left(-\int_0^s q_\nu(u)\,du\right)=(\mathcal T q_\nu)(s),
\]
by Tonelli. Differentiation for positive \(s\) shows \(F(G\nu)=\nu\), since Laplace transforms uniquely determine probability laws. Repetition therefore yields valid normalized chains with initial laws \(G^N\nu\) for every terminal \(\nu\).

**2. Sharp comparison.** For any valid chain, normalization at zero and the defining differential equation give \(q_j=\mathcal T q_{j+1}\), hence \(q_0=\mathcal T^Nq_N\). Every terminal probability transform satisfies \(0\le q_N(s)\le1\), while \(\mathcal T\) reverses the pointwise order on nonnegative functions. Since \(h_0=0\), \(h_1=\mathcal T0=1\), repeated order reversal traps \(\mathcal T^Nq_N\) between \(\mathcal T^N0=h_N\) and \(\mathcal T^N1=h_{N+1}\), with the order depending on the parity of \(N\).

For the endpoint \(h_{N+1}\), choose \(\nu=\delta_0\): its Laplace transform is identically one, so \(q_{G^N\delta_0}=\mathcal T^N1=h_{N+1}\). For the other endpoint, choose \(\nu_M=\delta_M\) for \(M>0\). Its transform \(e^{-Ms}\) tends to zero at every \(s>0\), is between zero and one, and consequently \(\mathcal T e^{-M\cdot}\to\mathcal T0\) uniformly on compact \(s\)-intervals, by dominated convergence and equicontinuity of primitives. Successive applications of \(\mathcal T\) preserve this compact uniform convergence, so \(q_{G^N\delta_M}=\mathcal T^N(e^{-M\cdot})\to h_N\) locally uniformly. Thus neither endpoint can be improved, even at a single fixed positive argument.

**3. Exact deviation.** The mean-one exponential law has transform \(q_*(s)=(1+s)^{-1}\), which satisfies \(\mathcal Tq_*=q_*\). Applying the comparison above to \(q_*\) places it between \(h_N\) and \(h_{N+1}\). The absolute difference from this interior point is maximized at an endpoint, both endpoints being attained or approached by actual normalized chains. This proves the exact supremum formula.

**4. Global factorial bound.** For nonnegative functions \(f,g\), the inequality \(|e^{-a}-e^{-b}|\le |a-b|\) for \(a,b\ge0\) yields
\[
|\mathcal Tf(s)-\mathcal Tg(s)|\le \int_0^s|f(u)-g(u)|\,du.
\]
Iterating this inequality \(N\) times gives the Volterra simplex estimate
\[
|\mathcal T^Nf(s)-\mathcal T^Ng(s)|
\le\frac1{(N-1)!}\int_0^s(s-u)^{N-1}|f(u)-g(u)|\,du.
\]
Use \(f=q_N\), \(g=q_*\), both in \([0,1]\), and \(\mathcal T^Nq_*=q_*\). The integral is at most \(s^N/N!\), for arbitrary \(s\ge0\) and \(N\ge1\).

**5. Optimal local constant.** Write \(e_n=h_n-q_*\). Since \(h_1=1\),
\[
e_1(s)=s+O(s^2).
\]
For all \(n\ge1\), the exact identity
\[
e_{n+1}(s)=q_*(s)\left[\exp\left(-\int_0^s e_n(u)\,du\right)-1\right]
\]
and induction prove
\[
e_n(s)=(-1)^{n+1}\frac{s^n}{n!}+O(s^{n+1})\quad(s\downarrow0).
\]
Because \(h_N\) is an approachable endpoint, the exact worst-case discrepancy is at least \(|h_N-q_*|\). Together with the global factorial upper bound, this implies the stated local limiting constant of one. All small-argument statements are at fixed finite \(N\); no interchange of \(N\to\infty\) with \(s\downarrow0\) is asserted.

## Verification

A standalone Python 3 checker, `check.py`, reconstructs finite exact moment identities implied by the inverse Lévy transform and numerically integrates the comparison iteration across multiple depths and terminal point masses. The provided checker reports `PASS: 5539 finite exact and quadrature diagnostics`. The infinite-dimensional sharpness and all-depth bounds rest on the analytic proof above, **not** on finite computations. To reproduce, run `python3 check.py` with the Python standard library.

## Relationship to prior work

Grabchak, *On Size-Biased Distributions and the Chainability of Positive Infinitely Divisible Distributions* (arXiv:2611.11109v1, first posted 2026-11-08), Section 3, defines the positive first-logarithmic-derivative chain and proves that every probability measure has an arbitrary-length probability-valued preimage (Proposition 3); its Theorem 1 and Corollary 2 examine scaled fixed points and eventually periodic chains. Those results provide the motivating transformation and inverse construction, but do not state an optimal finite-depth Laplace envelope, its exact worst-case transform error, or the global factorial estimate.

Earlier finite-depth moment matching and weak-limit statements do not, by themselves, supply sharp *pointwise* capacities or a uniform-on-compacts factorial rate with best local constant. Bar-Lev and Letac, *Chainability of Infinitely Divisible Measures* (Statistics & Probability Letters, 2025, DOI 10.1016/j.spl.2024.110256), work with a second-logarithmic-derivative chain on the real line, rather than the normalized positive first-derivative chain here. Their full paper could not be inspected; this is a remaining literature-priority uncertainty.

## Limitations

The exact capacity concerns only Laplace transforms at a specified nonnegative argument; no optimal total-variation bound is claimed. For fixed \(N\) the endpoint \(h_N\) is generally only a limit of valid finite-terminal-law chains, not a claimed attained probability law. The factorial bound is useful for fixed transform range and large chain depth; for large \(s\) it can exceed the trivial bound one. Historical priority is based on accessible primary texts and searches and is not independently certified.

## References

1. M. Grabchak, *On Size-Biased Distributions and the Chainability of Positive Infinitely Divisible Distributions*, arXiv:2611.11109v1 (2026-11-08), https://arxiv.org/html/2611.11109v1.
2. S. K. Bar-Lev and G. Letac, *Chainability of Infinitely Divisible Measures*, Statistics & Probability Letters (2025), https://doi.org/10.1016/j.spl.2024.110256.
3. O. Kallenberg, *Foundations of Modern Probability*, 3rd ed., Springer (2021), background on Laplace transforms and Lévy–Khintchine representation.
