# Pareto search-time tails and a Gamma-selected hidden target under Poisson resetting

## Finding

A target drawn once from an exponential spatial law can turn an otherwise exponentially light, fixed-target first-passage time into a regularly varying *annealed* search time. The phenomenon includes a sharp posterior law for the difficult target and an asymptotically locked reset-count burden.

Let \(D,r,\beta>0\), \(k=\sqrt{r/D}\), and \(a=\beta/k\). Start a one-dimensional Brownian searcher with infinitesimal generator \(D\partial_{xx}\) at zero, independently reset it instantaneously to zero at the events of a rate-\(r\) Poisson process, and absorb it on first hitting a target at \(R>0\). The location \(R\) is drawn **once** at the outset with density \(\beta e^{-\beta R}\), is independent of everything else, and is held fixed for all reset cycles. Let \(T\) be the absorption time and \(N\in\{0,1,\ldots\}\) the number of resets strictly before absorption. All probabilities not conditioned on \(R\) average both target uncertainty and path randomness.

**Theorem.** For every \(a>0\):

1. The exact reset-count distribution and its survival tail are
   \[
   \Pr(N=n)=a\,\mathrm B(a+1,n+1),\qquad
   \Pr(N\ge n)=\frac{\Gamma(a+1)\Gamma(n+1)}{\Gamma(a+n+1)}
     \sim\Gamma(a+1)n^{-a},
   \]
   for integers \(n\ge0\), with the asymptotic as \(n\to\infty\).

2. The **physical** absorption time has the sharp survival law
   \[
   \boxed{\Pr(T>t)\sim\Gamma(a+1)(rt)^{-a}\quad(t\to\infty).}
   \]
   Consequently, for each real \(q>0\), \(\mathbb E[T^q]<\infty\) holds **if and only if** \(q<a\). For \(a>1\), \(\mathbb E[T]=1/[r(a-1)]\); for \(a>2\),
   \[
   \mathbb E[T^2]=\frac{a^2}{r^2(a-2)(a-1)^2}.
   \]

3. Put \(V_t=rt\exp(-kR)\). Conditional on \(T>t\), the following joint weak convergence holds as \(t\to\infty\):
   \[
   \boxed{\left(V_t,\frac{T}{t},\frac{N}{rt}\right)
       \ \Longrightarrow\ \left(G,1+\frac E G,1+\frac E G\right),}
   \]
   where \(G\sim\operatorname{Gamma}(a,\mathrm{rate}=1)\) and \(E\sim\operatorname{Exp}(1)\) are **independent**. In particular, the hidden-target posterior satisfies
   \[
   kR-\log(rt)\ \Longrightarrow\ -\log G\quad\text{given }T>t,
   \]
   and the terminal reset count is, to first order, the Poisson-clock cost of the exceptional search time.

**Conjugate-target boundary.** In the exponential target distribution \(\beta=2\sqrt{r/D}\) identified in Evans--Ray [1] as conjugate to Poisson resetting, \(a=2\). Thus \(\mathbb E[T]=1/r\) but \(\operatorname{Var}(T)=\infty\), with
\[
\Pr(T>t)\sim\frac{2}{r^2t^2},\qquad
\Pr(N\ge n)=\frac{2}{(n+1)(n+2)},\qquad
\Pr(N=n)=\frac{4}{(n+1)(n+2)(n+3)}.
\]
The source's conjugacy is a mean-first-passage extremality property; the present theorem does **not** assume, or independently assert, global optimality among all reset-clock distributions.

## Assumptions and scope

All results use a single quenched target per search, one spatial dimension, independent Brownian paths and exponential reset times, instantaneous positional resetting with no time overhead, and full absorption upon contact. The fixed-rate limits in the theorem are \(t\to\infty\) or \(n\to\infty\), with \(D,r,\beta\) fixed and strictly positive. These statements do not hold automatically when the target is redrawn at every reset, the target lies in a bounded interval, resetting time is nonexponential, or multiple searchers interact. The proof allows \(a\) at either moment threshold, including the integer boundary \(a=2\), without excluding equalities.

## Proof

**Step 1: exact fixed-target Laplace transform and moments.** For a free Brownian first hit \(\tau_R\) of the level \(R>0\), the standard boundary-value problem \(Df''=sf\), \(f(R)=1\), \(f(-\infty)=0\), gives
\[
\mathbb E[e^{-s\tau_R}]=e^{-R\sqrt{s/D}}\quad(s\ge0).
\]
Let \(p=e^{-kR}\in(0,1)\) and \(z=kR=-\log p\). In each reset cycle, success occurs before the rate-\(r\) exponential clock with probability \(p\). Independent restart cycles give, for \(s\ge0\),
\[
\Phi_p(s):=\mathbb E[e^{-sT}\mid p]
 =\frac{(r+s)q_s}{s+rq_s},\qquad
 q_s=e^{-R\sqrt{(r+s)/D}}=p^{\sqrt{1+s/r}}.
\tag{1}
\]
For clarity, this follows by summing a geometric series of failed cycles: the successful-cycle time transform is \(q_s\), and the failed-cycle time transform is \(\frac r{r+s}(1-q_s)\). Differentiating (1) at zero gives
\[
\mathbb E[T\mid p]=\frac{1-p}{rp},\qquad
\mathbb E[T^2\mid p]=\frac{2/p^2-(2+z)/p}{r^2}.
\tag{2}
\]
These formulas are nonnegative for all \(p\in(0,1)\) (and have the correct zero-distance limit).

**Step 2: exact count law and annealed moments.** The change of variable \(p=e^{-kR}\) maps the exponential target density to \(a p^{a-1}\,dp\) on \((0,1)\). Conditional on \(p\), the reset count is geometric on nonnegative integers: \(\Pr(N=n\mid p)=p(1-p)^n\). Beta integration yields the two count formulas. Stirling's Gamma ratio gives their \(n^{-a}\) asymptotics. Integrating (2) against \(a p^{a-1}dp\) produces \(\mathbb E[T]=1/[r(a-1)]\) when \(a>1\) and
\[
 r^2\mathbb E[T^2]
 =\frac{2a}{a-2}-\frac{2a}{a-1}-\frac{a}{(a-1)^2}
 =\frac{a^2}{(a-2)(a-1)^2}
\]
when \(a>2\). Nonnegative conditional second moments diverge when \(a\le2\), since their leading term is \(2/(r^2p^2)\) as \(p\downarrow0\).

**Step 3: rare-success scaling and a uniform exponential envelope.** Let \(X_p=rpT\) under the conditional law given \(p\). For any fixed \(s\ge0\), substitute \(s rp\) into (1). Since \(p\log p\to0\),
\[
\frac{q_{srp}}p
 =\exp\!\left[-z\left(\sqrt{1+sp}-1\right)\right]\longrightarrow1,
\qquad
\mathbb E[e^{-sX_p}\mid p]\longrightarrow\frac1{1+s}.
\]
Hence \(X_p\Rightarrow X\sim\operatorname{Exp}(1)\) as \(p\downarrow0\). The convergence also admits the following **uniform** survival estimate. For \(0<\theta<1\), the same geometric-cycle transform is valid at the negative argument \(-\theta rp\): its denominator is strictly positive because
\(q_{-\theta rp}=p^{\sqrt{1-\theta p}}\ge p\). Therefore
\[
\mathbb E[e^{\theta X_p}\mid p]
 =\frac{(1-\theta p)q_{-\theta rp}}{q_{-\theta rp}-\theta p}
 \le\frac{1}{1-\theta}.
\]
In particular, Markov's inequality at \(\theta=1/2\) gives the bound, valid **simultaneously for all** \(p\in(0,1)\) and \(v\ge0\),
\[
\Pr(X_p>v\mid p)\le2e^{-v/2}.
\tag{3}
\]
The negative-argument transform is finite by summation of the nonnegative renewal series (its renewal ratio is strictly below one); no analytic-continuation assumption is required.

**Step 4: sharp annealed time tail.** Set \(v=rtp\). Using \(p\sim\operatorname{Beta}(a,1)\) in the exact integral (and assigning zero outside its natural domain),
\[
\Pr(T>t)=\frac{a}{(rt)^a}
\int_0^{rt}v^{a-1}\Pr\bigl(X_{v/(rt)}>v\mid p=v/(rt)\bigr)\,dv.
\tag{4}
\]
For each fixed \(v>0\), the integrand's conditional probability tends to \(e^{-v}\), since \(X_p\Rightarrow\operatorname{Exp}(1)\). The envelope (3) gives the integrable bound \(2v^{a-1}e^{-v/2}\) for every \(a>0\). Dominated convergence yields \(a\Gamma(a)=\Gamma(a+1)\) as the integral constant. Thus the sharp time-tail statement follows. The tail-integral identity \(\mathbb E[T^q]=q\int_0^\infty t^{q-1}\Pr(T>t)\,dt\) gives the exact real-moment criterion \(q<a\), including divergence at equality.

**Step 5: asymptotic identity of reset count and elapsed clock time.** Let \(C_u\) be the underlying rate-\(r\) reset-counting Poisson process and \(M_u=C_u-ru\) its compensated martingale. At the absorption stopping time \(T\), the reset count is \(N=C_T\) almost surely (no simultaneous hit and clock jump). Since \(\mathbb E[T\mid p]<\infty\), the stopped martingale has the exact isometry
\[
\mathbb E[(N-rT)^2\mid p]=r\mathbb E[T\mid p]=\frac{1-p}{p}.
\]
Consequently, \(\mathbb E[(pN-X_p)^2\mid p]=p(1-p)\to0\). Together with Step 3 this proves \((X_p,pN)\Rightarrow(X,X)\) as \(p\downarrow0\). The result holds for the *same* limiting variable, rather than for independent exponentials.

**Step 6: posterior and the full conditional joint law.** Let \(F\) be any bounded continuous test function of three variables. In the conditional expectation of \(F(V_t,T/t,N/(rt))\mathbf1_{\{T>t\}}\), substitute \(v=rtp\) just as in (4). For every fixed \(v>0\), Step 5 and the fact that the exponential law has no atom at \(v\) imply convergence of the conditional integrand to
\[
\mathbb E\left[F(v,X/v,X/v)\mathbf1_{\{X>v\}}\right].
\]
The absolute value is bounded by \(\|F\|_\infty\Pr(X_p>v)\), so (3) again supplies the same integrable majorant. Dividing the resulting dominated-convergence integral by the asymptotic denominator from Step 4 identifies the limiting joint distribution with density proportional to \(v^{a-1}e^{-x}\mathbf1_{\{x>v\}}\,dv\,dx\). Write \(x=v+e\). It factors into a \(\operatorname{Gamma}(a,1)\) density in \(v\) and an independent \(\operatorname{Exp}(1)\) density in \(e\). The second and third coordinates become \(1+e/v\), proving the stated joint limit. Continuity of the logarithm on \((0,\infty)\) yields the posterior location limit.

## Verification

The accompanying `verify.py` (Python 3, `mpmath`) checks 153 finite mathematical diagnostics: direct Beta integrals and Gamma-tail relations for reset counts, a change of variable in the exact annealed Laplace transform, first two derivatives of the fixed-target Laplace transform, negative-argument exponential-moment bounds, the rare-success scaling at increasingly distant targets, and the exact critical \(a=2\) count formulas. Run with `python verify.py` after installing `mpmath` if needed. All 153 assertions passed on the packaged file. Numerical tests do **not** prove the universal weak limits; the rigorous finite-to-infinite argument is in Steps 3--6. No statistical independence between the terminal count and elapsed time is claimed: their scaled limits are identical.

For an independent transform cross-check, the exact annealed Laplace transform for \(u=s/r\ge0\) is
\[
\mathbb E[e^{-sT}]
 =a\sqrt{1+u}\int_0^1
 \frac{w^{a/\sqrt{1+u}}}{u+w}\,dw,
\]
obtained directly from (1) via \(w=p^{\sqrt{1+u}}\). At the conjugate point \(a=2\), the nonintegrable second moment is not an artifact of numerical truncation: it follows from the sharp \(t^{-2}\) tail and from (2).

## Relationship to prior work

Evans and Ray [1] introduced the target distribution conjugate to a resetting protocol and derived the exponential spatial law \(\beta=2\sqrt{r/D}\) for Poisson resetting, together with an averaged mean first-passage time \(1/r\). Their main text and supplementary derivations provide the general renewal formula for survival and a mean-optimization discussion. The precise annealed temporal power law, complete moment thresholds, Gamma posterior, and *joint* time/reset-count conditional scaling are not stated there. These new asymptotics are extracted nontrivially from the renewal setting, rather than claimed to supersede its exact fixed-target transform.

Linn and Lawley [2] proved general exponentially distributed rare-success first-passage limits under **increasing reset rate** for fixed search problems. The rare-success fixed-target argument in Step 3 is closely related, but here the reset rate stays fixed while the *target distance* grows and is then integrated over a quenched exponential prior. The joint Gamma selection and reset-count/time locking are not consequences stated by [2]. Pal, Kuśmierz and Reuveni [3] study home-return search and variance control in a different protocol, but not the heavy-tailed random-target search-time law above. The geometric and Beta integral algebra is classical; no novelty is claimed for those tools in isolation.

## Limitations

This is a result for an explicitly specified physical model, not a universal statement for arbitrary target distributions. It does not show that Poisson resetting minimizes variance, nor that conjugacy entails a mathematically established global optimum among all clocks. General mixed-geometric and mixture-of-exponentials theory could contain formulations that dominate parts of the claim; a comprehensive publication-priority guarantee is not supplied. The precise rates in the joint limit rely on memoryless exponential resets and a one-time target draw. All assertions of independence concern the two **new limiting variables** \(G\) and \(E\), not the original search time and reset count.

## References

1. M. R. Evans and S. Ray, *Stochastic resetting prevails over sharp restart for broad target distributions*, arXiv:2410.01941v1 (public 2024-10-02), subsequent *Physical Review Letters* **134**, 247102 (2025). https://arxiv.org/abs/2410.01941 ; full text https://arxiv.org/html/2410.01941v2 .
2. S. Linn and S. D. Lawley, *First-passage times under frequent stochastic resetting*, arXiv:2302.05409v1 (2023), *Physical Review E* **108**, 024114 (2023). https://arxiv.org/abs/2302.05409 .
3. A. Pal, Ł. Kuśmierz and S. Reuveni, *Search with home returns provides advantage under high uncertainty*, arXiv:1906.06987 (2019), *Physical Review Research* **2**, 043174 (2020). https://arxiv.org/abs/1906.06987 .
4. M. R. Evans and S. N. Majumdar, *Diffusion with stochastic resetting*, *Physical Review Letters* **106**, 160601 (2011). https://doi.org/10.1103/PhysRevLett.106.160601 .
