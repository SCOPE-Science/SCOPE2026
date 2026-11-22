# A square-root singleton-association window in two-capacity exclusion

## Finding
For a periodic \(L\)-site \((q,t)\) two-capacity exclusion process, let \(\eta_i\in\{0,1,2\}\) be the stationary occupation at site \(i\), let \(N=\sum_i\eta_i\), and put \(I_i=\mathbf1_{\{\eta_i=1\}}\). Fix \(L\ge3\), \(0\le N\le2L\), \(q\ge0\), \(t>0\), and any distinct sites \(i,j\). Define
\[
w=\frac{1+t}{\sqrt t}\ge2,\qquad p=\frac1{w+2},\qquad a=\frac w{w+2}.
\]
The stationary law is independent of \(q\). The following statements constitute a single density-dependent singleton-association theorem.

1. **Exact positive association at half filling.** For every \(L\ge3\) and every \(t>0\), at \(N=L\), \(\operatorname{Cov}(I_i,I_j)>0\), whereas \(\operatorname{Cov}(\eta_i,\eta_j)<0\). More strongly, if \(k\) specified distinct sites are singly occupied, then the conditional probability that one additional site is singly occupied strictly increases with \(k\), for \(0\le k\le L-2\).
2. **Universal mesoscopic window.** For a fixed \(t>0\), if the integer particle counts satisfy \((N_L-L)/\sqrt L\to c\in\mathbb R\), then
\[
\lim_{L\to\infty}L^2\operatorname{Cov}(I_i,I_j)
=\frac{a^2}{2}\left(1-\frac{c^2}{p}\right).
\]
Thus the covariance is strictly positive for all sufficiently large \(L\) when \(|c|<\sqrt p\), and strictly negative for all sufficiently large \(L\) when \(|c|>\sqrt p\). No sign is asserted on the boundary \(|c|=\sqrt p\). In particular, at half filling its positive correlation is of order \(L^{-2}\), while \(L\operatorname{Cov}(\eta_i,\eta_j)\to-2p\).
3. **Exact finite-size window at the undeformed point.** When \(t=1\) (any \(q\ge0\)), for \(0\le N\le2L\),
\[
\operatorname{Cov}(I_i,I_j)=
\frac{N(2L-N)\big[L(L-1)-(4L-3)(N-L)^2\big]}
{L^2(L-1)(2L-3)(2L-1)^2}.
\]
For \(0<N<2L\) its sign is positive, zero, or negative exactly according as
\[
(N-L)^2<\frac{L(L-1)}{4L-3},\qquad
(N-L)^2=\frac{L(L-1)}{4L-3},\qquad
(N-L)^2>\frac{L(L-1)}{4L-3},
\]
respectively. At \(N=0\) or \(N=2L\) the covariance is zero. At \(N=L\) the exact values are \(\operatorname{Cov}(I_i,I_j)=L/[(2L-1)^2(2L-3)]\) and \(\operatorname{Cov}(\eta_i,\eta_j)=-1/(2L-1)\).

This identifies a fluctuation-scale interval of positive correlations for the nonmonotone single-occupancy observable, despite the fixed-particle constraint enforcing negative correlations for the ordinary occupation numbers.

## Assumptions and scope
The model has periodic nearest-neighbor bonds, occupancy capacity two, and particle-conserving hops. Write \([0]_t=0\), \([1]_t=1\), \([2]_t=1+t\). On each directed bond, the rightward hop from an adjacent pair \((b,c)\) occurs at rate \([b]_t([2]_t-[c]_t)\); its leftward counterpart has rate \(q[c]_t([2]_t-[b]_t)\). All parameters above are fixed except in the specified large-\(L\) limit. The observables concern distinct sites but not necessarily neighbors; at stationarity the joint law is exchangeable, even though the dynamics is not. The theorem is a statement about equal-time stationarity, not dynamical space-time correlations.

## Proof
**1. Stationary weights and canonical gauge.** On \(\sum_i\eta_i=N\), the strictly positive stationary weight is
\[
\pi(\eta)\ \propto\ \prod_i f(\eta_i),\qquad
f(0)=t,\quad f(1)=1+t,\quad f(2)=1.
\]
One may verify this independently of a preexisting product-state formula: for the right-hopping kernel, the normalized edge difference between incoming and outgoing flux at occupations \((b,c)\) equals \(h(c)-h(b)\), where \(h(0)=0\), \(h(1)=1+t\), and \(h(2)=(1+t)^2\). This identity holds for all nine possible pairs, including the forbidden-hop boundaries. Its sum around the periodic ring telescopes to zero. Reversing bonds establishes the analogous identity for the left-hopping kernel, and therefore for every \(q\ge0\). Positive right hops connect all configurations at fixed mass, giving uniqueness. Replacing \(f(j)\) by \(f(j)z^j\) multiplies each canonical configuration by the same \(z^N\); choosing \(z=\sqrt t\) and rescaling gives equivalent site weights \((1,w,1)\), with \(w=(1+t)/\sqrt t\).

**2. Exact fixed-mass two-site formula.** Let \(P_{m,d}\) denote \(\Pr(Y_1+\cdots+Y_m=d)\), where each independent \(Y\) takes \(-1,0,1\) with probabilities \(p,a,p\), respectively. Then the stationary canonical distribution with total mass \(N=L+d\) is the law of \((1+Y_1,\ldots,1+Y_L)\) conditioned on \(\sum_iY_i=d\). For \(\lvert d\rvert\le L\),
\[
\Pr(I_i=1)=a\frac{P_{L-1,d}}{P_{L,d}},\qquad
\Pr(I_i=I_j=1)=a^2\frac{P_{L-2,d}}{P_{L,d}},
\]
with zero assigned when a numerator index is impossible. Therefore
\[
C_{L,d}:=\operatorname{Cov}(I_i,I_j)
=a^2\frac{P_{L,d}P_{L-2,d}-P_{L-1,d}^2}{P_{L,d}^2}.
\]
The characteristic function of \(Y\) is \(\phi(\theta)=a+2p\cos\theta=1-2p(1-\cos\theta)\), which is nonnegative on \([-\pi,\pi]\) because \(w\ge2\). At \(d=0\), the Fourier identity \(P_{m,0}=\int_{-\pi}^{\pi}\phi(\theta)^m\,d\theta/(2\pi)\) makes \((P_{m,0})\) a strictly log-convex moment sequence: Cauchy--Schwarz gives \(P_{m,0}P_{m-2,0}>P_{m-1,0}^2\) for \(m\ge2\), since \(\phi\) is not almost everywhere constant. The same inequality shows that the next-singleton conditional probabilities \(aP_{L-k-1,0}/P_{L-k,0}\) strictly increase with \(k\). Since the ordinary total occupation is fixed and \(\operatorname{Var}(\eta_i)=1-\Pr(I_i=1)>0\) at half filling, exchangeability yields \(\operatorname{Cov}(\eta_i,\eta_j)=-\operatorname{Var}(\eta_i)/(L-1)<0\).

**3. Sharp square-root asymptotic.** For \(d_L/\sqrt L\to c\), Fourier inversion and a Gaussian Laplace expansion yield
\[
P_{L,d_L}\sim\frac{1}{\sqrt{4\pi pL}}\exp\left(-\frac{c^2}{4p}\right).
\]
Crucially, one should not subtract two separately truncated central-limit approximations. Instead symmetrize the *exact* determinant:
\[
P_{L,d}P_{L-2,d}-P_{L-1,d}^2
=\frac12\int_{[-\pi,\pi]^2}
\phi(\theta)^{L-2}\phi(\psi)^{L-2}
(\phi(\theta)-\phi(\psi))^2 e^{-id(\theta+\psi)}
\frac{d\theta\,d\psi}{(2\pi)^2}.
\]
Set \(\theta=u/\sqrt L\), \(\psi=v/\sqrt L\). As \(L\to\infty\), \(\phi(u/\sqrt L)^{L-2}\to e^{-pu^2}\) and \(L(\phi(u/\sqrt L)-\phi(v/\sqrt L))\to-p(u^2-v^2)\). Gaussian domination holds outside any shrinking neighborhood of zero because \(\phi\in[0,1]\) and has a unique maximum at zero; it also controls the quartic factors after scaling. Consequently the determinant divided by \(P_{L,d_L}^2/L^2\) tends to
\[
\frac{p^2}{2}\frac{
\displaystyle\int_{\mathbb R^2}e^{-p(u^2+v^2)}(u^2-v^2)^2e^{-ic(u+v)}\,du\,dv}
{\displaystyle\left[\int_{\mathbb R}e^{-pu^2}e^{-icu}\,du\right]^2}
=\frac12\left(1-\frac{c^2}{p}\right).
\]
For the final Gaussian identity, regard the normalized tilted integral as a Gaussian with variance \(1/(2p)\) and complex mean \(-ic/(2p)\), and evaluate twice its quadratic variance. Multiplication by \(a^2\) proves the asserted limit. The same concentration argument gives \(\Pr(I_i=1)\to a\) at \(d=0\), hence \(L\operatorname{Cov}(\eta_i,\eta_j)\to-(1-a)=-2p\).

**4. Exact undeformed window.** For \(t=1\), each site is a pair of ordinary Bernoulli slots and the canonical stationary state corresponds to a uniformly random \(N\)-subset of \(2L\) slots. Thus
\[
\Pr(I_i=1)=\frac{N(2L-N)}{L(2L-1)},\quad
\Pr(I_i=I_j=1)=\frac{N(N-1)(2L-N)(2L-N-1)}{L(L-1)(2L-1)(2L-3)}.
\]
Their exact difference factors as the rational expression in the Finding section. The denominator is positive for \(L\ge3\); for \(0<N<2L\), the remaining sign is precisely that of \(L(L-1)-(4L-3)(N-L)^2\). The half-filled ordinary-occupation covariance reduces to \(-1/(2L-1)\).

## Verification
The standard-library script `check.py` independently builds exact finite-state transition balances for several short rings, exactly enumerates canonical weights and pair moments, verifies the fully factored \(t=1\) formula and its sign criterion for all sizes \(3\le L\le41\) and all particle numbers, and spot-checks the large-size scaling at multiple deformations. It reports 8187 deterministic assertions passing. These finite checks do not replace the strict Cauchy--Schwarz argument, the exact hypergeometric identity, or the Gaussian asymptotic analysis.

## Relationship to prior work
Ayyer and Misra, arXiv:2310.03343 (first public version October 5, 2023), establish the \((q,t)\) \(K\)-ASEP dynamics, the stationary canonical product law, particle-hole symmetry, and one-site occupation probabilities. Their full April 2024 version was inspected through Sections 2--5, Appendix A, and its references; it does not state the singleton-pair sign criterion or the square-root density window. Their general stationary law and the earlier \(t=1\) binomial law are inputs, not new claims here. Schütz and Sandow's 1994 partial-exclusion work addresses density-correlation functions and provides relevant older background. The finite \(t=1\) expression follows algebraically from the established binomial canonical law; the claim of added mathematical content is the sharp association threshold and the uniform deformed-model mesoscopic asymptotic, not the binomial law itself.

## Limitations
For \(t\ne1\), this result proves eventual signs in the specified \(\sqrt L\) window and an exact half-filling sign, not a complete finite-\(L\), all-density sign classification. On the limiting mesoscopic boundary \(\lvert c\rvert=\sqrt p\), the displayed leading coefficient vanishes; higher-order analysis would be required. No result is claimed for other site capacities or unequal site-dependent hopping parameters. The older Schütz--Sandow full publisher text was not accessible in the available open sources; bibliographic and abstract evidence does not certify absence of an equivalent statement. No independent scientific audit has been performed.

## References
1. A. Ayyer and S. Misra, *An exactly solvable asymmetric \(K\)-exclusion process*, arXiv:2310.03343, first posted 2023-10-05; HTML full text https://arxiv.org/html/2310.03343v2 (2024 revision). Primary model and stationary law.
2. G. Schütz and S. Sandow, *Non-Abelian symmetries of stochastic processes: Derivation of correlation functions for random-vertex models and disordered-interacting-particle systems*, Phys. Rev. E **49**, 2726 (1994), https://doi.org/10.1103/PhysRevE.49.2726. Earlier partial-exclusion and two-point density-correlation context.
3. G. M. Schütz, R. Ramaswamy, and M. Barma, *Pairwise balance and invariant measures for generalized exclusion processes*, J. Phys. A **29**, 837 (1996), https://doi.org/10.1088/0305-4470/29/4/011. General invariant-measure context.
