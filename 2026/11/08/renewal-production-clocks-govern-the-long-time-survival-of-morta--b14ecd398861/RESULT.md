# Renewal production clocks govern the long-time survival of mortal diffusive searchers

## Finding

An initially empty reaction system is populated by independent searchers arriving at renewal epochs. Each searcher has probability \(p\in(0,1)\) to hit the target before death, and may take an arbitrarily distributed positive time to do so. In the class of bounded, strictly positive interbirth gaps, the no-reaction probability has the exact logarithmic decay rate

\[
\lim_{t\to\infty}-\frac{\log Q(t)}{t}=\theta_W(p),\qquad
(1-p)\,\mathbb E[e^{\theta_W(p)W}]=1.
\]

The root is unique and positive. It depends on the single-searcher dynamics **only** through the eventual success probability, not the successful search-time distribution. Among interbirth laws with a fixed mean \(\tau\), every increase in convex variability weakens the exponential decay, and the constant clock uniquely maximizes its rate:

\[
\theta_W(p)\le -\frac{\log(1-p)}{\tau},
\]

with equality if and only if \(W=\tau\) almost surely. By comparison, a Poisson production clock of rate \(b=1/\tau\) yields rate \(bp\). Pareto waiting-time clocks of any positive tail index have zero exponential rate, though a reaction occurs almost surely.

For the physical example of a particle diffusing along a half-line, starting at distance \(L>0\) from the origin, with generator \(D\partial_{xx}\) and independently dying at rate \(d>0\), the success probability is

\[
p=e^{-L\sqrt{d/D}}.
\]

Therefore regular production and Poisson production with the same mean interbirth gap have exactly the rates \(-b\log(1-p)\) and \(bp\), respectively. The distinction concerns asymptotic survival tails; it is not a claim of finite-time dominance or equal mean reaction times.

## Assumptions and scope

Let \((W_i)_{i\ge1}\) be independent identically distributed strictly positive waiting times, let \(S_n=\sum_{i=1}^n W_i\), and set \(N_t=\#\{n:S_n\le t\}\). An independent searcher is created at each \(S_i\), with an independent, identically distributed defective completion delay \(U_i\in[0,\infty]\); \(U_i=\infty\) records a searcher that degrades without detecting the target. Assume \(p=\Pr(U_i<\infty)\in(0,1)\). No integrability is needed for the finite conditional delay to obtain the logarithmic exponent. Define \(T=\inf_{i\ge1}(S_i+U_i)\) and \(Q(t)=\Pr(T>t)\).

For the general root, assume \(0<w_-\le W_i\le w_+<\infty\) almost surely. For the convex-order comparison, both laws obey this hypothesis and share mean \(\tau\); their bounds need not agree. Poisson interbirth and Pareto interbirth laws are treated separately, not asserted to satisfy bounded support. In the mean-reaction-time claim additionally assume \(\mathbb E[U_i\mid U_i<\infty]<\infty\).

## Proof

**1. Exact conditional survival and two bounds.** Write \(G(u)=\Pr(U_i\le u)\) for finite \(u\), so \(G(u)\uparrow p\). Independence across particles gives the exact identity

\[
Q(t)=\mathbb E\left[\prod_{i:S_i\le t}(1-G(t-S_i))\right].
\]

For \(c\in(0,1)\), set \(g_c(t)=\mathbb E[c^{N_t}]\). Each factor in the product is at least \(1-p\), and for births at least \(K\) units before \(t\), each factor is at most \(1-G(K)\). Thus, for \(t>K\) and \(0<G(K)<1\),

\[
g_{1-p}(t)\le Q(t)\le g_{1-G(K)}(t-K).
\tag{1}
\]

This comparison is uniform over the distribution of successful arrival delays.

**2. Elementary exponential-tilt lemma for a bounded renewal clock.** For every \(c\in(0,1)\), let \(\theta_c>0\) be the unique solution of \(c\mathbb E[e^{\theta_c W}]=1\). Existence and uniqueness follow from strict positivity and boundedness of \(W\). Define a tilted waiting-time law

\[
\widetilde F(dw)=c e^{\theta_c w}F(dw).
\]

This is a probability law on the same support. Since the first renewal strictly after \(t\) has index \(N_t+1\), changing measures on the event \(S_{n-1}\le t<S_n\) gives exactly

\[
g_c(t)=c^{-1}\widetilde{\mathbb E}
       [e^{-\theta_c S_{N_t+1}}].
\]

The tilted overshoot lies in \((0,w_+]\), hence, for all \(t\ge0\),

\[
c^{-1}e^{-\theta_c(t+w_+)}
\le g_c(t)\le c^{-1}e^{-\theta_ct}.
\tag{2}
\]

In particular \(\lim_{t\to\infty}-t^{-1}\log g_c(t)=\theta_c\); no renewal theorem, arithmeticity assumption, or uncontrolled asymptotics are necessary.

**3. Arbitrarily delayed successes do not change the exponent.** Apply (2) to both sides of (1). It yields

\[
\theta_{1-G(K)}\le\liminf_{t\to\infty}-t^{-1}\log Q(t)
\le\limsup_{t\to\infty}-t^{-1}\log Q(t)
\le\theta_{1-p}.
\]

Here \(\theta_c\) decreases continuously with \(c\in(0,1)\) by strict monotonicity of the exponential moment. As \(K\to\infty\), \(G(K)\uparrow p\); consequently the two endpoints coalesce at \(\theta_{1-p}\).

**4. Sharp clock ordering.** If \(W_a\le_{\mathrm{cx}}W_b\) and their means coincide, then for every \(s>0\),

\[
\mathbb E e^{sW_a}\le\mathbb E e^{sW_b}.
\]

Comparing the unique roots yields \(\theta_{W_b}(p)\le\theta_{W_a}(p)\), strictly whenever the convex-order comparison is nontrivial. Jensen's inequality gives \(\mathbb E e^{sW}\ge e^{s\tau}\), with equality for \(s>0\) only when the clock is constant. This proves the unique global fixed-mean maximizer within bounded renewal clocks. The deterministic expression is \(\theta=-\log(1-p)/\tau\).

**5. Unbounded benchmarks.** When interbirth times are exponential with rate \(b\), the count \(N_t\) is Poisson with mean \(bt\), so

\[
Q(t)=\exp\left[-b\int_0^tG(u)\,du\right].
\]

As \(G(u)\uparrow p\), Cesàro averaging gives exponent \(bp\). When \(\Pr(W_1>t)=(1+t/a)^{-\alpha}\), with \(a,\alpha>0\), the initially empty system cannot react before its first birth: \(Q(t)\ge(1+t/a)^{-\alpha}\). Therefore its logarithmic exponential decay rate is zero. Independently, the number of births is almost surely infinite and each succeeds with probability \(p>0\), so \(T<\infty\) almost surely. Let \(J\) be the first successful birth by birth order. Then \(J\) is geometric with mean \(1/p\), and \(T\le S_J+U_J\). If the mean successful delay is finite and \(\mathbb EW<\infty\), Wald's sum gives \(\mathbb ET\le\mathbb EW/p+\mathbb E[U\mid U<\infty]<\infty\). Conversely \(T\ge W_1\), so \(\mathbb EW=\infty\) forces \(\mathbb ET=\infty\). For Pareto waiting times the finite-mean threshold is exactly \(\alpha>1\).

**6. Diffusive example.** For Brownian diffusivity \(D>0\), source distance \(L>0\), and exponential degradation \(d>0\), the success probability is \(p=\mathbb E[e^{-d\tau_0}]=e^{-L\sqrt{d/D}}\), obtained by solving \(Dq''=dq\), \(q(0)=1\), \(q(\infty)=0\). Its conditional successful delay has finite mean because \(\tau_0e^{-d\tau_0}\) has finite expectation. The preceding rates and Pareto mean threshold therefore apply to this physical system.

## Verification

The standalone program `verify_renewal.py` numerically tests the root for deterministic and two-point renewal clocks, the independent delayed-success renewal equation with log-domain arithmetic, strict clock comparisons, and the exact Poisson formula. All tests passed. Equation (2), the conditional survival identity, the squeeze limit, and the convex-order argument are analytical proofs; the program is supporting finite numerical evidence, not a certification of the infinite-time statement.

## Relationship to prior work

Mercado-Vásquez and Boyer, *Stochastic synthesis-degradation processes: first-passage properties and connections with resetting* (first arXiv publication 11 February 2026), study Poisson birth/death clocks and derive first-passage and optimization results. Linn and Kumar (first arXiv publication 11 January 2026) independently study dynamic redundancy with Poisson recruitment and mortality. Boyer and Mercado-Vásquez, *Stochastic synthesis and degradation of arbitrary diffusive processes* (3 November 2026), extend the constant-rate setting to Poisson burst sizes, not independent renewal gaps; their conclusion highlights the outstanding non-Markov production problem. The exact 2025 injection-time analysis by Grebenkov, Metzler and Oshanin concerns a finite number of particles with deterministic or independent injection times, not the indefinitely repeated renewal clock considered here. Classical Bernoulli thinning of renewal point processes underlies the zero-delay reduction, and the present result should be understood as a delayed-mortal-search specialization with a sharp fixed-mean clock-ordering statement, not as a claim that renewal tilting or Jensen's inequality is new.

## Limitations

The general renewal root is proved for strictly positive bounded interbirth gaps; its validity is not asserted for all light-tailed unbounded laws. The Poisson and Pareto cases are proved separately. The result gives the logarithmic decay exponent, not a universal asymptotic prefactor or exact finite-time first-passage law. The fixed-mean comparison is for long-time survival exponents and does not order survival at every finite time. Searchers do not interact, and the birth clock is independent of their delays. A general existing renewal-thinning or marked-process theorem may already imply the delayed-search exponential rate, and the results have not undergone independent priority assessment.

## References

- G. Mercado-Vásquez and D. Boyer, *Stochastic synthesis-degradation processes: first-passage properties and connections with resetting*, arXiv:2602.11095v1 (11 February 2026); Phys. Rev. E 114, L022107 (2026). https://arxiv.org/abs/2602.11095
- D. Boyer and G. Mercado-Vásquez, *Stochastic synthesis and degradation of arbitrary diffusive processes*, arXiv:2611.04843v1 (3 November 2026). https://arxiv.org/abs/2611.04843
- S. Linn and A. Kumar, *Dynamic redundancy and mortality in stochastic search*, arXiv:2601.07096v1 (11 January 2026). https://arxiv.org/abs/2601.07096
- D. S. Grebenkov, R. Metzler and G. Oshanin, *Fastest first-passage time statistics for time-dependent particle injection*, Phys. Rev. Research 7, 023239 (2025). https://arxiv.org/abs/2503.19105
- J. Chandramohan and L.-K. Liang, *Bernoulli, multinomial and Markov chain thinning of some point processes*, J. Appl. Probab. 22, 828–835 (1985). https://doi.org/10.2307/3213950
