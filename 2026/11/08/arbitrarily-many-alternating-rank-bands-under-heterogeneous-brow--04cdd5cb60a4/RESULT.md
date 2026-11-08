# Arbitrarily many alternating rank bands under heterogeneous Brownian resetting

## Finding

**Theorem (unbounded rank-response alternation).** Fix a diffusivity \(D>0\), an integer \(K\geq1\), and any prescribed positive weights \(w_1,\ldots,w_K\) with \(\sum_{j=1}^K w_j=1\). There exist strictly increasing distances \(0<d_1<\cdots<d_K\) such that the following phenomenon occurs. Each searcher starts at a distance drawn from the fixed discrete law \(\mathbb P(d=d_j)=w_j\) and independently performs Brownian motion with generator \(D\partial_{xx}\) on the positive half-line, absorbed at the origin, with its own Poisson resets to its initial point at rate \(r\geq0\). Let \(t_r(\phi)\), for \(0<\phi<1\), be the \(\phi\)-quantile of the resulting absorption time, averaged over initial-distance classes. Then the right derivative \(\partial_r t_r(\phi)|_{r=0+}\) has **at least \(2K-1\) distinct sign-changing zeros** as \(\phi\) increases from zero to one. Equivalently, infinitesimally weak resetting alternates between delaying and accelerating rank-fraction completion in at least \(2K\) successive nonempty rank intervals. Thus no universal finite bound on the number of distinct helpful/harmful resetting bands follows from noninteracting Brownian dynamics alone.

An exact single-distance response kernel is
\[
 h(u)=(u+2)\operatorname{erfc}(u^{-1/2})-(u+1)\operatorname{erfc}((2\sqrt u)^{-1})
 +2\sqrt{u/\pi}\bigl(e^{-1/(4u)}-e^{-1/u}\bigr),\qquad u>0.
\]
The mixture's infinitesimal survival response is
\[
 H(t):=\left.\partial_r \mathbb P(T_r>t)\right|_{r=0+}
 =\sum_{j=1}^K w_j\frac{d_j^2}{D}\,h\left(\frac{Dt}{d_j^2}\right).
\]
The sign of \(\partial_r t_r(\phi)|_{r=0+}\) equals the sign of \(H(t_0(\phi))\), so the theorem is constructive through separation of the initial distance scales.

## Assumptions and scope

The process is one-dimensional, driftless, on \((0,\infty)\), with perfectly absorbing origin; every searcher has the same \(D>0\), independent Brownian increments, and an independent Poisson clock of rate \(r\). Each reset is instantaneous and returns the searcher to **its own** original distance \(d_j\); the distance class does not redraw on reset. The sampling law is a finite mixture of point masses with fixed strictly positive weights. Time-dependent conditioning, interaction, delayed returns, or collective resets are excluded. The \(\phi\)-quantile means the unique time at which the unconditional absorption CDF equals \(\phi\). This is also the deterministic large-population rank-fraction limit when empirical class frequencies approach \(w_j\). No theorem about the exact optimal reset rate, its global uniqueness, or the mean of a finite-\(N\) order statistic is claimed.

## Proof

**1. Brownian first-passage and renewal.** For a fixed initial distance \(d>0\) and no resetting, the reflection principle gives the survival function
\[
 Q_d(t)=\operatorname{erf}\left(\frac{d}{2\sqrt{Dt}}\right),
 \qquad\widehat Q_d(s)=\int_0^\infty e^{-st}Q_d(t)\,dt
 =\frac{1-e^{-d\sqrt{s/D}}}{s},\quad s>0.
\]
Writing \(Q_{r,d}(t)\) for survival with Poisson resetting to the same \(d\), the first-reset decomposition is
\[
 Q_{r,d}(t)=e^{-rt}Q_d(t)+r\int_0^t e^{-rv}Q_d(v)Q_{r,d}(t-v)\,dv.
\]
Its Laplace transform is \(\widehat Q_{r,d}(s)=\widehat Q_d(s+r)/(1-r\widehat Q_d(s+r))\). Differentiating at \(r=0+\) (equivalently differentiating the finite-time Volterra equation, using bounded survival probabilities) yields
\[
 H_d(t):=\left.\partial_r Q_{r,d}(t)\right|_{r=0+}
 =\int_0^t Q_d(v)Q_d(t-v)\,dv-tQ_d(t).
\]
With \(a=d/\sqrt D\), its Laplace transform is exactly
\[
 \widehat H_d(s)=\widehat Q_d'(s)+\widehat Q_d(s)^2
 =\frac{e^{-2a\sqrt s}+(a\sqrt s/2-1)e^{-a\sqrt s}}{s^2}.
\]
The elementary inverse transforms
\[
 \mathcal L^{-1}\{e^{-a\sqrt s}/s^2\}(t)
 =(t+a^2/2)\operatorname{erfc}(a/(2\sqrt t))-a\sqrt{t/\pi}e^{-a^2/(4t)}
\]
and
\[
 \mathcal L^{-1}\{e^{-a\sqrt s}/s^{3/2}\}(t)
 =2\sqrt{t/\pi}e^{-a^2/(4t)}-a\operatorname{erfc}(a/(2\sqrt t))
\]
produce the stated scaled kernel \(H_d(t)=(d^2/D)h(Dt/d^2)\). The displayed Laplace identities can also be checked by direct differentiation and the classical heat-kernel transform.

**2. Opposite scale-edge signs.** The standard complementary-error-function asymptotic, including the first two terms of its large-argument expansion, gives
\[
 h(u)\sim\frac{2}{\sqrt\pi}u^{3/2}e^{-1/(4u)} >0
 \quad(u\downarrow0),\qquad
 h(u)=1-\sqrt{u/\pi}+O(u^{-1/2})<0
 \quad(u\to\infty).
\]
Consequently choose fixed constants \(0<u_-<u_+\) with \(h(u_-)>0>h(u_+)\). These choices do not depend on the number of distance classes or on their weights.

**3. Arbitrarily many alternating samples by induction.** For \(1\leq j\leq K\), set
\[
 H^{(j)}(t)=\sum_{i=1}^{j}w_i\frac{d_i^2}{D}h(Dt/d_i^2).
\]
Choose any \(d_1>0\). The two sample times \(t_1^\pm=u_\pm d_1^2/D\) have \(H^{(1)}(t_1^-)>0>H^{(1)}(t_1^+)\). Suppose \(d_1,\ldots,d_{j-1}\) have already been fixed with all \(2(j-1)\) required strict signs. As \(d_j\to\infty\), the new contribution \(w_j(d_j^2/D)h(Dt/d_j^2)\) tends to zero at each previously fixed time \(t>0\), by the first asymptotic in Step 2. Hence every old strict sign survives for sufficiently large \(d_j\).

At the two new times \(t_j^\pm=u_\pm d_j^2/D\), for each fixed \(i<j\), the second asymptotic yields
\[
 \frac{d_i^2}{D}h\left(u_\pm\frac{d_j^2}{d_i^2}\right)
 =-\frac{d_i d_j\sqrt{u_\pm}}{D\sqrt\pi}+O(1).
\]
Thus
\[
 H^{(j)}(t_j^\pm)=\frac{w_jd_j^2}{D}h(u_\pm)+O(d_j),
\]
and therefore has the desired positive and negative signs for large enough \(d_j\). Increasing \(d_j\) also guarantees \(t_{j-1}^+<t_j^-\). Complete the induction through \(j=K\). Since the final mixture is a finite sum of analytic functions of \(t>0\), it has alternating strict signs at
\[
 t_1^-<t_1^+<t_2^-<t_2^+<\cdots<t_K^-<t_K^+.
\]
The intermediate-value theorem gives at least \(2K-1\) distinct sign-changing zeros of \(H(t)\), one in each gap.

**4. Transfer to ranks.** With \(F_r(t)=1-\sum_jw_jQ_{r,d_j}(t)\), the no-reset density is strictly positive:
\[
 f_0(t)=F_0'(t)=\sum_{j=1}^K w_j\frac{d_j}{2\sqrt{\pi D}\,t^{3/2}}
  e^{-d_j^2/(4Dt)}>0,\qquad t>0.
\]
Thus \(F_0\) maps \((0,\infty)\) strictly increasingly onto \((0,1)\), and the implicit-function theorem at every \(\phi\in(0,1)\) gives
\[
 \left.\partial_r t_r(\phi)\right|_{r=0+}
 =\frac{H(t_0(\phi))}{f_0(t_0(\phi))}.
\]
The time-to-rank change of variables preserves the ordered alternating signs, completing the theorem. For independent searchers with empirical proportions tending to the prescribed finite weights, the ordinary law of large numbers for each class gives uniform CDF convergence and hence convergence of every interior order-statistic rank fraction to \(t_r(\phi)\).

**Concrete three-scale witness (not needed for the general proof).** Set \(D=1\), equal weights \(1/3\), and \((d_1,d_2,d_3)=(1,100,10000)\). Evaluating the exact formula at \(t=\tfrac14 d_j^2\) and \(t=2d_j^2\) for \(j=1,2,3\) gives six successive signs \(+,-,+,-,+,-\), hence at least five distinct rank-response reversals. The accompanying standalone verifier evaluates this witness and independently checks the renewal integral.

## Verification

Run `python3 verify.py` in the directory containing the file. It uses only the Python standard library. It independently integrates the renewal convolution against the closed kernel, numerically checks the exact Laplace-domain identity, checks the three-scale sign witness, and checks the predicted scaling limits. The symbolic derivation and scale-separation induction, not the numerical tests, establish the theorem for every integer \(K\).

## Relationship to prior work

The 2026 Brownian multiparticle study of Vatash, Goldfarb, Rudyak and Roichman provides finite-population ordered-arrival benchmarks, a single critical rank fraction for identical starts in the large-population limit, and heterogeneous geometry examples. The present statement addresses a different question: whether heterogeneous geometry admits a universal finite bound on the number of **zero-rate rank-response sign reversals**. The construction shows that no such bound exists, even with independent searchers and Poisson resetting. It neither asserts a new renewal formula nor replaces the source's finite-\(N\) optimal-rate analysis. Classical renewal-reset theory supplies the Laplace representation; Górska, Sevilla, Chacón-Acosta and Sandev (2024) give an accessible first-passage renewal-transform treatment in another transport model. Evans, Majumdar and Mallick (2013) consider resetting searches and many-particle survival, while Evans and Ray (2024) study random target-distance distributions with a mean-time objective. Those results do not, as stated in the material accessible for comparison, imply an arbitrary number of alternating **quantile-response** intervals.

## Limitations

Only the derivative at zero reset rate, not global finite-rate optimality, is classified. The distance scales in the existence proof can be widely separated; the claim is an existence theorem, not a typicality theorem. The finite three-scale witness checks five transitions but is not an exhaustive root census. The result does not establish an exact finite-\(N\) optimal-rate sequence. The complete text of the particularly relevant September 2026 multiparticle preprint could not be inspected, so detailed publication-priority comparison with any unabstracted analysis there remains a specific residual originality risk. Independent mathematical review has not been performed.

## References

1. R. Vatash, E. Goldfarb, V. Yu. Rudyak, and Y. Roichman, *Rank-dependent optimal resetting in multiparticle search*, arXiv:2609.23542, first submitted 2026-09-20, https://arxiv.org/abs/2609.23542 .
2. M. R. Evans, S. N. Majumdar, and K. Mallick, *Optimal diffusive search: nonequilibrium resetting versus equilibrium dynamics*, J. Phys. A 46 (2013), 185001, https://doi.org/10.1088/1751-8113/46/18/185001 .
3. K. Górska, F. J. Sevilla, G. Chacón-Acosta, and T. Sandev, *Fractional Telegrapher's Equation under Resetting: Non-Equilibrium Stationary States and First-Passage Times*, Entropy 26 (2024), 665, https://pmc.ncbi.nlm.nih.gov/articles/PMC11353880/ .
4. M. R. Evans and S. Ray, *Stochastic resetting prevails over sharp restart for broad target distributions*, arXiv:2410.01941, first submitted 2024-10-02, https://arxiv.org/abs/2410.01941 .
5. P. Singh and A. Pal, *First-passage Brownian functionals with stochastic resetting*, J. Phys. A 55 (2022), 234001, arXiv:2202.02715, https://arxiv.org/abs/2202.02715 .
