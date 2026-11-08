# Dual conditional extreme laws for a Brownian search with Poisson resets

## Finding

Consider one-dimensional Brownian motion with generator \(D\partial_{xx}\), started at \(a>0\), absorbed at the origin, and independently reset to \(a\) at Poisson rate \(r>0\). Let \(T\) be its almost surely finite first-passage time, \(N\) the number of resets strictly before \(T\), and \(M=\sup_{0\le t\le T}X_t\) its spatial maximum. Write \(\kappa=\sqrt{r/D}\), \(z=\kappa a\), \(p=e^{-z}\), and \(q=1-p\). For a threshold \(m>a\), set

\[
A_m=\frac{\sinh[\kappa(m-a)]}{\sinh(\kappa m)},\quad
B_m=\frac{\sinh(\kappa a)}{\sinh(\kappa m)},\quad
C_m=1-A_m-B_m.
\]

**Theorem (joint maximum/reset-count law and its two conditional extremes).** For every integer \(n\ge0\) and every \(m>a\),

\[
\Pr(N=n,M<m)=A_m C_m^n,\qquad \Pr(N=n)=p q^n.
\]

Consequently \(N\mid\{M<m\}\) is exactly geometric with mass \((1-C_m)C_m^n\). Moreover, the conditional maximum \(M\mid\{N=n\}\) is strictly increasing in the usual stochastic order as \(n\) increases. The same joint law has the following distinct sharp conditional limits:

1. For any fixed \(r,D,a>0\), the maximum *conditional on exactly \(n\) resets* satisfies, for every real \(y\),
\[
\lim_{n\to\infty}\Pr\left(\kappa M-\log n-\log(1+e^z)\le y\mid N=n\right)=\exp(-e^{-y}).
\]
2. For fixed \(r,D,a>0\), conditioning on a *very high spatial maximum* instead gives the size-biased geometric count law
\[
\lim_{m\to\infty}\Pr(N=n\mid M>m)=
\begin{cases}0,&n=0,\\ n p^2q^{n-1},&n\ge1.\end{cases}
\]
3. The apparently sharp exclusion of zero-reset trajectories in item 2 has a singular low-rate crossover. Hold \(a,D>0\) fixed, let \(r\downarrow0\), and choose thresholds \(m_r>a\) with \(\kappa m_r\to u\in(0,\infty)\). Then
\[
\Pr(M>m_r)\sim\frac{\kappa a}{\sinh u},\qquad
(N\mid M>m_r)\ \Longrightarrow\ \mathrm{Bernoulli}(1-e^{-u}),
\]
where the Bernoulli variable takes values \(0\) and \(1\). Thus the no-reset and one-reset weights are \(e^{-u}\) and \(1-e^{-u}\), respectively.

The theorem is one coherent classification of the joint first-passage maximum and reset count: its exact finite-threshold formula determines both the count-conditioned Gumbel regime and the rare-maximum count-selection regime, while the low-rate limit resolves their nonuniform boundary.

## Assumptions and scope

Brownian trajectories are continuous between instantaneous resets. All Brownian segments and exponential reset clocks are independent. A reset at \(T\) has probability zero. The target is absorbing at \(0\), with the positive starting and reset coordinate \(a\). There are no drift, refractory times, spatially distributed reset positions, or additional particles. All fixed-rate limits retain positive \(r,D,a\); the low-rate limit holds \(a,D\) fixed with \(\kappa m_r\to u>0\), so \(m_r\to\infty\). The Gumbel limit takes \(n\to\infty\) under the conditional probability measure given \(N=n\).

## Proof

**Step 1: One-cycle trichotomy.** Start one independent diffusion segment at \(a\) and let \(\tau_0,\tau_m\) be the hitting times of \(0,m\), with independent \(E\sim\mathrm{Exp}(r)\). The probability of reaching \(0\) before \(m\) and \(E\) is the unique solution of \(Df''=rf\) on \((0,m)\), with \(f(0)=1\), \(f(m)=0\). Evaluating at \(a\) gives \(A_m\). Analogously, reaching \(m\) before \(0,E\) has probability \(B_m\). All remaining paths have \(E<\tau_0\wedge\tau_m\) and probability \(C_m\). These three events partition probability one, and \(0<C_m<1\) for \(m>a\).

Without an upper absorbing boundary, the one-segment success probability is \(\Pr(\tau_0<E)=\mathbb E[e^{-r\tau_0}]=e^{-\kappa a}=p\), hence the failure/reset probability is \(q\). Since every reset renews the starting state and the independent driving noises, there are exactly \(n\) reset-before-boundary cycles followed by one target-hit-before-reset cycle, all below \(m\), precisely with probability \(C_m^nA_m\). Removing \(m\) gives \(p q^n\). Geometric summation also yields
\[
\Pr(M<m)=\frac{A_m}{1-C_m}=\frac{A_m}{A_m+B_m},\qquad
\Pr(M>m)=\frac{B_m}{A_m+B_m}.
\]
The first identity agrees with the known unconditioned first-passage maximum distribution; the count refinement is essential for what follows. Dividing the joint mass by the first identity gives the conditional geometric law.

**Step 2: Count-conditioned Gumbel maximum.** For fixed \(z>0\) write \(L=\kappa m\). As \(L\to\infty\),
\[
B_m=2\sinh z\,e^{-L}(1+O(e^{-2L})),\quad
p-A_m=\frac{2\sinh z\,e^{-2L}}{1-e^{-2L}},\quad
C_m=q-B_m+(p-A_m).
\]
Therefore \(A_m/p\to1\) and
\[
\frac{q-C_m}{q}=(1+e^z)e^{-L}+O(e^{-2L}),
\]
using \(2\sinh z/(1-e^{-z})=1+e^z\). For \(L_n=\log n+\log(1+e^z)+y\), this gives \(n(1-C_{m_n}/q)\to e^{-y}\) and \(C_{m_n}/q\to1\). From \(\Pr(M<m\mid N=n)=(A_m/p)(C_m/q)^n\), the limit is \(e^{-e^{-y}}\). The exact relation \(q-C_m=2\sinh z/(e^L+1)>0\) shows \(0<C_m/q<1\) for all finite \(m>a\). Therefore its conditional cumulative distribution \((A_m/p)(C_m/q)^n\) is strictly decreasing in \(n\) at each \(m>a\), proving the claimed stochastic order. The equality/strict threshold distinction is immaterial because the maximum has a continuous distribution.

**Step 3: High-maximum size bias.** The exact tail-at-fixed-count difference is
\[
\Pr(N=n,M>m)=p q^n-A_mC_m^n.
\]
For fixed \(n\ge1\) and \(L\to\infty\), the expansions above give
\[
p q^n-A_mC_m^n=n p q^{n-1}B_m+O(e^{-2L}),
\]
whereas for \(n=0\) this probability equals \(p-A_m=O(e^{-2L})\). Also \(\Pr(M>m)=B_m/(A_m+B_m)\sim B_m/p\). Their ratio tends to \(np^2q^{n-1}\) for \(n\ge1\) and to zero for \(n=0\). The limiting masses sum to \(p^2\sum_{n\ge1}nq^{n-1}=1\). Pointwise convergence of these probability masses to a normalized law yields convergence in total variation (for example by the elementary discrete Scheffé lemma). No unjustified interchange of an infinite count sum is used.

**Step 4: Low-rate crossover.** Set \(z=\kappa a\to0\) and \(L=\kappa m_r\to u>0\). Taylor expansions yield
\[
A_{m_r}=1-z\coth u+o(z),\quad
B_{m_r}=\frac{z}{\sinh u}+o(z),\quad
C_{m_r}=z\tanh(u/2)+o(z),\quad p=1-z+o(z).
\]
Thus \(\Pr(M>m_r)=B/(A+B)\sim z/\sinh u\). The zero-reset joint tail is \(p-A=z(\coth u-1)+o(z)\), so
\[
\Pr(N=0\mid M>m_r)\to\sinh u(\coth u-1)=e^{-u}.
\]
Because \(\Pr(N\ge2)=q^2=O(z^2)\) and the conditioning event has probability of order \(z\), the conditional probability of \(N\ge2\) tends to zero. The complementary mass converges to \(1-e^{-u}\) at \(N=1\), as claimed.

## Verification

All identities are analytic. A self-contained standard-library Python checker, `check_current.py`, independently evaluates first-cycle normalization, marginalization and Bayes identities over a deterministic parameter grid; it also examines numerical convergence to the Gumbel, size-biased geometric, and low-rate Bernoulli profiles. Run it with `python3 check_current.py` from the extracted package directory. Its finite tests are diagnostic, not a substitute for the infinite-limit derivations above.

## Relationship to prior work

Guo, Yan and Chen (2023), arXiv:2306.15929, derive the *marginal* first-passage maximum law and the maximum/time-of-maximum joint transform; its expression for \(\Pr(M<m)\) coincides with the summation of the new joint law. Sunil, Blythe, Evans and Majumdar (2023), arXiv:2304.09348, derive the geometric first-passage reset-count law and joint transforms for reset number, time, and additive spatial return cost, but do not treat the path maximum. Singh and Pal (2021), arXiv:2102.07111, derive joint extremal/reset-interval formulas for a *fixed observation time*, rather than absorption at a target. The count-conditioned Gumbel centering, high-maximum size bias and low-rate crossover need the dependence between the stopped maximum and reset count; neither marginal distribution alone determines them. Generic Gumbel and size-bias mechanisms are acknowledged, rather than claimed as new universality classes.

## Limitations

The argument is restricted to one-dimensional driftless Brownian motion with instantaneous, independent Poisson resets to the same fixed point. It gives no finite-sample estimation guarantee, no distributional limit in which the reset-count conditioning varies simultaneously with the reset rate, and no theorem for other restart-clock distributions. A more general unindexed renewal-excursion result could cover some or all conditional laws; novelty is assessed relative to the specific primary works inspected, not mathematically certified by search.

## References

- W. Guo, H. Yan and H. Chen, *Extremal statistics for a resetting Brownian motion before its first-passage time*, arXiv:2306.15929 (first posted 2023-06-28), https://arxiv.org/abs/2306.15929 ; Phys. Rev. E 108, 044115 (2023).
- J. C. Sunil, R. A. Blythe, M. R. Evans and S. N. Majumdar, *The cost of stochastic resetting*, arXiv:2304.09348 (first posted 2023-04-19), https://arxiv.org/abs/2304.09348 ; J. Phys. A 56, 395001 (2023).
- P. Singh and A. Pal, *Extremal statistics for stochastic resetting systems*, arXiv:2102.07111 (first posted 2021-02-14), https://arxiv.org/abs/2102.07111 ; Phys. Rev. E 103, 052119 (2021).
- A. K. Hartmann, S. N. Majumdar and G. Schehr, *The distribution of the maximum of independent resetting Brownian motions*, arXiv:2309.17432 (first posted 2023-09-29), https://arxiv.org/abs/2309.17432 .
