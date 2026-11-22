# Marked late-survivor law for threshold-reset Brownian motion in a wedge

## Finding

Consider Brownian search in a planar wedge with one absorbing edge and one instantaneous-reset edge. Conditional on target absorption taking longer than a large observation time, the number of resets already completed has an asymptotic geometric law, while the *eventual* exit edge of the unusually long, currently active excursion is asymptotically fair, independently of the geometric count. The last reset occurs at a tight, unscaled random time. In contrast, the eventual total reset count has a different, explicitly computable law: a geometric count plus, with probability one half, one further reset and an independent geometric count.

Precisely, write \(a=1-b\), where \(b=\theta_0/\alpha\). If \(K_t\) is the number of completed resets by observation time \(t\), \(Y_t\in\{0,1\}\) is the eventual exit indicator of the currently active free excursion (zero for target, one for reset edge), \(S_t\) is its starting epoch, and \(N\) is the total eventual number of resets before target absorption, then, as \(t\to\infty\), conditional on \(T>t\),

\[
(K_t,S_t,Y_t,N)\ \Longrightarrow\ (K,U_1+\cdots+U_K,B,K+B(1+G)).
\]

Here \(K\) and \(G\) are independent geometric random variables on the nonnegative integers, each with \(\Pr(K=k)=\Pr(G=k)=ab^k\); \(B\) is an independent fair Bernoulli random variable; and the \(U_i\) are independent copies of the one-excursion duration conditional on a reset-edge exit, independent of \(K,G,B\). The empty sum is zero. Consequently, for each \(k\ge0\) and \(j\in\{0,1\}\),

\[
\lim_{t\to\infty}\Pr(K_t=k,Y_t=j\mid T>t)=\frac{ab^k}{2},
\]

and, for each \(n\ge0\),

\[
\lim_{t\to\infty}\Pr(N=n\mid T>t)
=\frac{ab^n}{2}+\frac{a^2n b^{n-1}}{2}\,\mathbf 1_{\{n\ge1\}}.
\]

The limiting probability-generating function of the total count is

\[
\mathbb E[z^{K+B(1+G)}]
=\frac{a}{2(1-bz)}+\frac{a^2z}{2(1-bz)^2},\qquad |z|\le1,
\]

with limiting-law mean \((1+2b)/(2a)\) and variance \((1+6b)/(4a^2)\). The starting epoch of the active excursion is tight under late-survivor conditioning, and therefore \(S_t/t\to0\) in conditional probability. These are distributional limits; convergence of moments of the unbounded finite-time count variables is not asserted.

## Assumptions and scope

Fix \(0<\alpha<2\pi\), \(D>0\), \(r_0>0\), and \(0<\theta_0<\alpha\). Starting at polar position \((r_0,\theta_0)\), let planar Brownian motion have generator \(D\Delta\) in the wedge \(\{(r,\theta):r>0,0<\theta<\alpha\}\). At the first hit of \(\theta=0\), terminate the trajectory (target absorption). At the first hit of \(\theta=\alpha\), instantly reset to \((r_0,\theta_0)\), with an independent fresh Brownian excursion. There is no auxiliary Poisson resetting or drift. The almost surely finite first exit time of one free excursion is \(X\); its exit mark is \(Y=0\) for \(\theta=0\) and \(Y=1\) for \(\theta=\alpha\). By harmonic measure of a wedge, \(\Pr(Y=1)=b=\theta_0/\alpha\) and \(\Pr(Y=0)=a=1-b\).

The random time \(T\) is the first actual absorption at the target after any number of threshold resets. For each \(t<T\), \(K_t\) counts completed threshold resets no later than \(t\), \(S_t\) is the time of the last reset (zero when none occurred), and \(Y_t\) denotes the eventual free-excursion exit mark for the excursion containing \(t\). Thus \(Y_t\) is a *retrospectively defined future mark*, not information available to an observer at time \(t\). Define \(N\) as the total count of threshold resets before final absorption. Conditional laws are well defined because \(\Pr(T>t)>0\) for finite \(t\).

## Proof

**1. The two free-excursion marked tails.** Set \(\beta=\pi/(2\alpha)>0\). Let \(Q(t)=\Pr(X>t)\) and \(J_j(t)\,dt=\Pr(X\in dt,Y=j)\). The absorbing-wedge heat-kernel expansion gives

\[
Q(t)\sim A_0t^{-\beta},\qquad
J_0(t)\sim J_1(t)\sim\frac{\beta A_0}{2}t^{-\beta-1},
\]

where the positive constant is

\[
A_0=\frac4\pi\frac{\Gamma(1+\beta)}{\Gamma(1+2\beta)}
\left(\frac{r_0^2}{4D}\right)^{\beta}
\sin\left(\frac{\pi\theta_0}{\alpha}\right).
\]

Indeed, the principal angular Dirichlet eigenfunction is \(\sin(\pi\theta/\alpha)\). Its normal derivatives at the two edges have equal absolute magnitude. In the radial heat-kernel integral its contribution scales as \(t^{-\beta}\), and all higher angular modes decay by strictly higher powers. Differentiation at each edge gives the two equal leading currents. Equivalently, these current asymptotics appear explicitly as Eq. (104) in the cited wedge resetting work. Integration of the positive currents over \((t,\infty)\) yields, for both marks,

\[
H_j(t):=\Pr(X>t,Y=j)=\int_t^\infty J_j(u)\,du
\sim\frac{A_0}{2}t^{-\beta}.
\]

Thus the future exit mark of a long free excursion becomes asymptotically fair despite unequal *unconditional* exit probabilities.

**2. Fixed-count marked renewal identity.** Define the finite measure \(F(ds)=\Pr(X\in ds,Y=1)=J_1(s)\,ds\) of total mass \(b\). Put \(F^{*0}=\delta_0\). For each fixed \(k\ge0\), \(j\in\{0,1\}\), bounded measurable test function \(f\), and \(t>0\), independence of fresh excursions gives the exact identity

\[
\mathbb E\big[f(S_t)\mathbf1_{\{T>t,K_t=k,Y_t=j\}}\big]
=\int_{[0,t]}f(s)H_j(t-s)F^{*k}(ds).
\]

For \(k\ge1\), the convolution \(F^{*k}\) has a density bounded by \(O((1+s)^{-\beta-1})\) for \(s\ge1\). This follows inductively from \(J_1(s)=O(s^{-\beta-1})\) at infinity: splitting each convolution at half its argument bounds both halves by the same power times the finite total mass of its other factor. Local integrability near zero follows from the first-exit density.

Split the displayed integral at \(t/2\). On \([0,t/2]\), regular variation implies \(H_j(t-s)/H_j(t)\) is uniformly bounded, and for each fixed \(s\) it converges to one. Dominated convergence yields

\[
\lim_{t\to\infty}t^\beta\int_{[0,t/2]}f(s)H_j(t-s)F^{*k}(ds)
=\frac{A_0}{2}\int_{[0,\infty)}f(s)F^{*k}(ds).
\]

For \(s\in[t/2,t]\), the density bound (for \(k\ge1\)) and \(H_j(u)\le C(1+u)^{-\beta}\) give the remainder estimate

\[
O\left(t^{-\beta-1}\int_0^{t/2}(1+u)^{-\beta}\,du\right)=o(t^{-\beta})
\]

for every \(\beta>0\). The \(k=0\) case is immediate because \(F^{*0}\) is an atom at zero. It follows for each fixed \(k,j\) that

\[
\mathbb E[f(S_t)\mathbf1_{\{T>t,K_t=k,Y_t=j\}}]
\sim\frac{A_0}{2}t^{-\beta}\int f(s)F^{*k}(ds)
\]

when the integral on the right is positive, and otherwise the corresponding scaled convergence holds with zero limit. In particular, the unweighted event has asymptotic probability \((A_0/2)b^k t^{-\beta}\).

**3. Independent total-survival normalization and no escaped reset-count mass.** The renewal equation \(\Pr(T>t)=Q(t)+(F*\Pr(T>\cdot))(t)\) is equivalent to the following random-sum representation. Unconditionally, \(N\) has geometric mass \(ab^n\) and, given \(N=n\), the completed search duration is the independent sum of \(n\) free-excursion durations conditioned on a threshold exit plus one free-excursion duration conditioned on a target exit. Their regularly varying tails are respectively \(A_0t^{-\beta}/(2b)\) and \(A_0t^{-\beta}/(2a)\). For each fixed \(n\), the finite-sum one-large-excursion estimate gives

\[
\Pr(T>t\mid N=n)\sim\left(\frac{nA_0}{2b}+\frac{A_0}{2a}\right)t^{-\beta}.
\]

To justify averaging over \(n\), use the elementary union bound for a sum of \(n+1\) nonnegative durations and the uniform power bound \(\Pr(X>u\mid Y=j)\le C(1+u)^{-\beta}\): for \(n\le t-1\), the conditional survival probability is at most \(C'(n+1)^{\beta+1}t^{-\beta}\), while \(\Pr(N\ge t)\le b^t\). This polynomial envelope is integrable under the geometric count. Dominated convergence then gives the *directly derived* total tail

\[
\Pr(T>t)\sim\frac{A_0}{2}\left(\frac{\mathbb E[N]}{b}+\frac{1}{a}\right)t^{-\beta}
=\frac{A_0}{a}t^{-\beta},
\]

since \(\mathbb E[N]=b/a\). This independently reproduces the pure-threshold survival asymptotic also reported in Najeeb, Pal and Prasad (2026). The marked fixed-count conditional weights therefore tend to \(ab^k/2\). These probabilities sum to one across the two marks and all \(k\ge0\). Consequently there is no residual mass escaping to arbitrarily large completed reset count. More explicitly, convergence on each finite set of \(k\)'s, together with total mass one, proves tightness in \(k\); weak convergence of the continuous last-reset epoch within each fixed-count event follows from the preceding bounded-continuous-test identity. Given \(K=k\), the limiting epoch measure is \(F^{*k}/b^k\), i.e. a sum of \(k\) independent threshold-exit-conditioned durations. The limiting mark has probability one half for either edge and is independent of both \(K\) and the epoch.

**4. Total reset count and the future.** On \(Y_t=0\), the active excursion is ultimately absorbed at the target and \(N=K_t\). On \(Y_t=1\), that excursion adds one reset and is followed, by strong Markov restart, by an independent fresh search. Its further number \(G\) of resets has \(\Pr(G=g)=ab^g\) for \(g\ge0\), independently of the history and of the active excursion's duration and exit mark. This geometric distribution is the same for each finite \(t\), so adjoining it preserves joint convergence. The representation \(N=K+B(1+G)\) follows. Expanding its generating function gives the claimed mass formula. Differentiating this generating function at one gives the mean and variance of the **limiting** count law. Finally, the epoch component converges to a finite random variable, which implies \(S_t/t\to0\) in conditional probability.

## Verification

The standalone `check.py` reproduces the probability-generating function coefficients, the normalization and two moments of the limiting law over a range of parameters. It checks the free-wedge leading coefficient against independent exact reflection-principle and quadrant-product formulas. A discrete marked renewal process with exact Pareto excursion tails and unequal total exit probabilities provides a separate consistency test: its survivor-conditioned reset/mark distribution approaches the predicted fair-mark geometric law. Successful finite computations test formulas only; the preceding analytic argument establishes the limit for the continuum Brownian wedge.

## Relationship to prior work

Biswas, Majumdar and Pal (first public preprint April 18, 2025) introduce event-triggered threshold resetting and the defective renewal formalism. Najeeb, Pal and Prasad (first public preprint May 7, 2025) give the Brownian absorbing-wedge kernel, free-exit currents, and conditional two-edge quantities. Their combination motivates the concrete absorbing-edge/threshold-edge wedge renewal experiment, while the present proof derives its required late-tail normalization from scratch. A subsequent Najeeb–Pal–Prasad preprint publicly submitted November 19, 2026 explicitly analyzes that particular pure-threshold-reset wedge model, deriving the same *unconditional* survival tail and reset-count formulas. Its Secs. III and V and Appendix B have been examined as especially relevant overlap checks. The present result **does not** claim these ingredients: it adds the joint late-survivor conditional law for the completed reset count, the tight last-reset epoch, the ongoing excursion's future exit mark, and the eventual total reset count. The general single-big-jump and survivor-conditioned renewal mechanisms are also acknowledged as prior; their marginal conclusions alone cannot be treated as new. An unstated marked-renewal specialization in broader literature remains a publication-priority risk.

## Limitations

This is a strict \(t\to\infty\) conditional-distribution theorem in the *pure threshold-reset* wedge model with iid excursions; it does not cover additional Poisson resets, nonidentical reset positions, drift, or nonabsorbing boundary conditions. The future edge mark is retrospective and not immediately observable. No finite-time error rate or convergence of unbounded count moments is proved. The last-reset epoch may itself have infinite limiting mean for sufficiently broad wedges, although its distribution is tight. Bibliographic novelty is subject to independently checking broader renewal-theoretic equivalents.

## References

1. A. Biswas, S. N. Majumdar and A. Pal, *Target search optimization by threshold resetting* (first public version April 18, 2025), arXiv:2504.13501v1, https://arxiv.org/abs/2504.13501 . Threshold-triggered renewal model.
2. F. Najeeb, A. Pal and V. V. Prasad, *Diffusion in a wedge geometry: First-Passage Statistics under Stochastic Resetting* (first public version May 7, 2025), arXiv:2505.04208v1, https://arxiv.org/html/2505.04208v1 . Absorbing-wedge heat kernel and boundary currents.
3. F. Najeeb, A. Pal and V. V. Prasad, *First-passage and correlated reset-count statistics under threshold and Poissonian resetting in a two-dimensional wedge geometry* (initial public version November 19, 2026), arXiv:2611.26345v1, https://arxiv.org/html/2611.26345v1 . Directly relevant subsequent analysis and overlap check, including unconditional target-survival tails and reset counts.
4. M. Chupeau, O. Bénichou and S. N. Majumdar, *Survival probability of a Brownian motion in a planar wedge of arbitrary angle*, Physical Review E 91, 032106 (2015), https://doi.org/10.1103/PhysRevE.91.032106 . Wedge survival reference.
5. A. Vezzani, E. Barkai and R. Burioni, *The Single Big Jump Principle in Physical Modelling*, arXiv:1804.02932, https://arxiv.org/abs/1804.02932 . General heavy-tailed rare-excursion mechanism.
6. J. Duvall, *Survivor-conditioned renewal laws and observable bounds for open intermittent maps* (2026), arXiv:2606.27488, https://arxiv.org/abs/2606.27488 . Different-system survivor conditioning analogy.
