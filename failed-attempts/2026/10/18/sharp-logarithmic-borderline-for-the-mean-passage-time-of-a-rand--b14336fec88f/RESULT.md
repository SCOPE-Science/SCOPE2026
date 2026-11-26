# Sharp logarithmic borderline for the mean passage time of a randomly clocked walk

## Finding

For a symmetric continuous-time random walk on the positive integers whose nonnegative total jump rate is independently redrawn at every fixed interval, the following integral in the rate's Laplace transform is a **necessary and sufficient** condition for a finite mean time to hit zero:

\[
\mathbb E T_x<\infty\quad\Longleftrightarrow\quad
\int_0^1\frac{ds}{\sqrt{s}\,[1-\phi(s)]}<\infty,
\qquad \phi(s)=\mathbb E e^{-sR}.
\]

It holds for every fixed initial integer \(x\ge1\) and every fixed resampling period \(\tau>0\), without requiring any positive or finite moment of the rate. In particular, if the upper-tail distribution satisfies \(\Pr(R>u)\sim u^{-1/2}L(u)\), where \(L\) is positive and slowly varying, then

\[
\mathbb E T_x<\infty\quad\Longleftrightarrow\quad
\int^\infty\frac{du}{uL(u)}<\infty.
\]

Consequently a critical tail \(\Pr(R>u)\sim c u^{-1/2}(\log u)^\kappa\), with \(c>0\), gives **finite** mean exactly for \(\kappa>1\), and **infinite** mean for \(\kappa\le1\). In this model, a slowly varying factor can reverse the finiteness verdict at the critical power index. More generally, for \(\Pr(R>u)\sim u^{-\alpha}L(u)\), \(0<\alpha<1\), the mean is finite for \(\alpha<1/2\) and infinite for \(\alpha>1/2\).

## Assumptions and scope

Let \(R_j\), \(j=0,1,\ldots\), be independent copies of a finite \([0,\infty)\)-valued random variable \(R\) with \(\Pr(R>0)>0\). Fix \(\tau>0\). Start a symmetric nearest-neighbor walk at an integer \(x\ge1\) and kill it at its first visit to zero. At physical time \(t\), conditional on the rate sequence and on its current positive state, jumps occur at total rate \(R_{\lfloor t/\tau\rfloor}\), each with left/right probability \(1/2\). The jump directions, clocks and rates are independent. Write \(T_x\) for the hitting time. Every rate is finite almost surely, so the walk makes finitely many steps during any bounded time interval. No stationarity assumption beyond iid resampling is made.

The displayed convergence criteria are independent of the starting site and the period, but numerical values of mean first-passage times, when finite, generally do depend on both.

## Proof

**1. Time change and a uniform comparison of starting sites.** Let \(Y_a\) be the rate-one symmetric continuous-time walk (total rate one) killed at zero, and define its survival function \(h_x(a)=\Pr_x(Y_s>0\text{ for all }0\le s\le a)\). The integrated clock

\[
A_t=\int_0^tR_{\lfloor v/\tau\rfloor}\,dv
\]

is continuous, nondecreasing and finite on compact intervals. Conditional on the rate sequence, the absorbed walk is \(Y_{A_t}\). Thus \(\Pr(T_x>t)=\mathbb E h_x(A_t)\).

The unrestricted rate-one walk kernel at displacement \(j\in\mathbb Z\) is \(p_a(j)=e^{-a}I_{|j|}(a)\), where \(I_j\) is the modified Bessel function. Reflection at zero gives

\[
h_x(a)=\sum_{j=1-x}^{x}p_a(j).
\]

Every term is nonnegative, and \(p_a(j)\le p_a(0)\); the latter follows directly from the Fourier integral for the unrestricted kernel. Since the sum contains \(p_a(0)+p_a(1)=h_1(a)\), for all \(a\ge0\),

\[
h_1(a)\le h_x(a)\le2x\,h_1(a).
\]

Therefore finiteness of \(\mathbb ET_x\) is the same as finiteness for \(x=1\), and this comparison is uniform in the random clock.

**2. Resampling-epoch resolvent.** Since survival is nonincreasing in physical time,

\[
\tau\sum_{m=1}^\infty\Pr(T_1>m\tau)
\le \mathbb ET_1\le
\tau\sum_{m=0}^\infty\Pr(T_1>m\tau).
\]

Consequently the mean is finite exactly when the sampled survival series is finite. At a resampling epoch,

\[
A_{m\tau}=\tau\sum_{j=0}^{m-1}R_j.
\]

The Fourier/Bessel representation yields

\[
h_1(a)=e^{-a}\,[I_0(a)+I_1(a)]
=\frac1\pi\int_0^\pi e^{-a(1-\cos\theta)}(1+\cos\theta)\,d\theta.
\]

Writing \(\phi(s)=\mathbb E e^{-sR}\), independence and Tonelli's theorem give the **exact** identity, including the possibly infinite case,

\[
\sum_{m=0}^\infty\Pr(T_1>m\tau)
=\frac1\pi\int_0^\pi
\frac{1+\cos\theta}{1-\phi(\tau(1-\cos\theta))}\,d\theta.
\tag{1}
\]

For \(s>0\), \(\phi(s)<1\) because \(\Pr(R>0)>0\). Thus the integrand is bounded on every closed subinterval avoiding \(\theta=0\); the only potential singularity is at zero. There \(1+\cos\theta\to2\) and \(1-\cos\theta\sim\theta^2/2\). The change of variable \(s=\tau(1-\cos\theta)\) therefore proves that (1) is finite precisely when

\[
\int_0^1\frac{ds}{\sqrt{s}\,[1-\phi(s)]}<\infty.
\]

The upper integration endpoint can be replaced by any positive constant: the integrand is finite and bounded on compact subintervals of \((0,\infty)\). This proves the arbitrary-rate criterion. It also shows that the same criterion works for all \(\tau>0\) and all fixed \(x\ge1\).

**3. Sharp slowly varying boundary.** Suppose \(\bar F(u)=\Pr(R>u)\sim u^{-\alpha}L(u)\) as \(u\to\infty\), where \(0<\alpha<1\) and \(L\) is positive and slowly varying. Integrating by parts gives

\[
1-\phi(s)=s\int_0^\infty e^{-su}\bar F(u)\,du.
\]

The standard Laplace form of Karamata's theorem yields

\[
1-\phi(s)\sim\Gamma(1-\alpha)s^\alpha L(1/s),\qquad s\downarrow0.
\]

The criterion is thus equivalent to convergence of \(\int_0^\epsilon s^{-1/2-\alpha}/L(1/s)\,ds\). Potter bounds for positive slowly varying functions prove convergence when \(\alpha<1/2\), and divergence when \(\alpha>1/2\). At \(\alpha=1/2\), the substitution \(u=1/s\) gives precisely

\[
\int^\infty\frac{du}{uL(u)}<\infty.
\]

For \(L(u)\sim c(\log u)^\kappa\) the integral reduces to the familiar logarithmic endpoint integral; convergence is exactly \(\kappa>1\).

**4. Nonempty realizable critical regimes.** For any real \(\kappa\), take \(B=\exp(2+\max\{0,2\kappa\})\), and define a probability distribution by

\[
\Pr(R>u)=
\begin{cases}
1,&0\le u<B,\\
(B/u)^{1/2}(\log u/\log B)^\kappa,&u\ge B.
\end{cases}
\]

Its survival function is continuous and nonincreasing, since \(-1/(2u)+\kappa/(u\log u)<0\) for \(u\ge B\). It has the asserted upper-tail exponent and logarithmic factor. The cases \(\kappa=0\) and \(\kappa=2\), for instance, have identical power indices but opposite mean-finiteness verdicts. This demonstrates a genuine critical separation rather than a formal integral test.

## Verification

The accompanying `verify.py` uses only Python's standard library. It independently reconstructs finite-step survival by the discrete reflection principle, Poissonizes it, evaluates the Bessel representation, and checks the spectral/resampling-epoch identities for a two-point rate distribution. It tests multiple starting sites, times and resampling epochs. Run `python3 verify.py` from the extracted package. These finite deterministic checks corroborate the exact formulas; the infinite-series and critical-logarithm claims are established by the analytic argument above, not by finite enumeration.

## Relationship to prior work

Levit and Reuveni (2026, arXiv:2609.26925) establish this doubly stochastic walk's first-passage transition for Mittag-Leffler rate laws. Their main Eq. (2) provides the general half-line survival integral and Appendix A extends the power-law transition to distributions with an **asymptotically constant** power-tail prefactor. In that class, the mean diverges at exponent \(\alpha=1/2\). Their general survival identity is an explicit premise here and is not claimed as new. The added results are a rate-law-independent **if and only if** Laplace integrability criterion and the resolved **slowly varying critical boundary**, including finite-mean examples of power index \(1/2\) not covered by the pure-power statement. The criterion's proof requires translating the survival representation into a resolvent and applying the marginal Tauberian integral test; the general propagator alone does not state this classification.

Arutkin and Reuveni (2023/2024, arXiv:2302.07041) introduce the doubly stochastic continuous-time random walk and random-rate time change; that framework is pre-existing. Karamata's Tauberian theorem and regular-variation estimates are classical; their underlying theory is not new. The result is specifically the rigorous boundary classification for the stated absorbed random-rate walk.

## Limitations

The result assumes independent rate redraws at **deterministic equal intervals**, symmetric nearest-neighbor steps and a fixed positive starting site. It does not assert the criterion for correlated rates, moving boundaries, biased walks or continuous-space diffusions. No uniform joint limit as \(x\) or \(\tau\) vary is claimed. An older general random-clock first-passage theorem might imply the criterion by specialization; independent priority assessment is outstanding. A proof of the rate tail's regular variation is an assumption, not established from empirical data.

## References

1. B. Levit and S. Reuveni, *First Passage in the Presence of Jump Rate Fluctuations: A Transition from Infinite to Finite Mean*, arXiv:2609.26925 (first public submission 2026-09-22), especially Eq. (2), Eq. (4), Appendix A. https://arxiv.org/abs/2609.26925
2. M. Arutkin and S. Reuveni, *Doubly stochastic continuous time random walk*, arXiv:2302.07041 (2023); *Physical Review Research* 6, L012033 (2024). https://arxiv.org/abs/2302.07041
3. N. H. Bingham, C. M. Goldie and J. L. Teugels, *Regular Variation*, Cambridge University Press (1987), Karamata's theorem and Potter bounds.
