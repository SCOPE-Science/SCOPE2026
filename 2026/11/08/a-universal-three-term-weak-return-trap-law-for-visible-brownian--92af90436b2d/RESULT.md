# A universal three-term weak-return-trap law for visible Brownian first passage

## Finding

A diffusive search with finite-duration, Ornstein–Uhlenbeck (OU) home returns has a three-term mean-first-passage expansion when the return trap becomes weak. The leading two terms are independent of *the entire reset-clock distribution*, and the first clock-dependent term is a strictly positive penalty relative to permanent OU search.

For the protocol defined below, put \(c_D=\sqrt{\pi/(2D)}\), \(T=\inf\{t\ge0:B_t=L\}\), \(S=T\wedge R\), \(X=B_S\),
\[
 p_0=\Pr(T<R)+\frac1L\mathbb E[B_R\mathbf1_{\{R<T,\,0<B_R<L\}}]
     =\frac1L\mathbb E[-B_R\mathbf1_{\{R<T,\,B_R<0\}}]>0,
\]
\[
 H=\mathbb E[(R-T)_+]>0.
\]
Then the mean search time, \(M_R(\kappa)\), satisfies, as \(\kappa\downarrow0\) with \(D,L\) and the law of \(R\) fixed,
\[
 \boxed{M_R(\kappa)=\frac{Lc_D}{\sqrt\kappa}+\frac{L^2}{2D}
 +c_D\left(\frac{L^3}{6D}+\frac{LH}{p_0}\right)\sqrt\kappa+O(\kappa).}
\]
If \(M_{\mathrm{OU}}(\kappa)\) is the hitting-time mean from zero for uninterrupted OU motion under the same \(D,\kappa\), then
\[
 \boxed{M_R(\kappa)-M_{\mathrm{OU}}(\kappa)
 =\frac{Lc_D H}{p_0}\sqrt\kappa+O(\kappa)>0}
\]
for all sufficiently small positive \(\kappa\). At \(\kappa=0\), \(M_R(0)=+\infty\): the return phase from a negative reset point has infinite Brownian mean hitting time.

For independent exponential reset clocks of rate \(r>0\), define \(q=L\sqrt{r/D}\). In this special case,
\[
 p_0=\frac{1-e^{-2q}}{2q},\qquad H=\frac{e^{-q}}r,
\]
so
\[
 \boxed{M_r(\kappa)=\frac{Lc_D}{\sqrt\kappa}+\frac{L^2}{2D}
 +\frac{c_DL^3}{6D}\left(1+\frac{6}{q\sinh q}\right)\sqrt\kappa+O(\kappa).}
\]
The correction factor \(1+6/(q\sinh q)\) decreases strictly from infinity to one as \(q\) increases from zero to infinity. No uniformity at \(r=0\) or \(r=\infty\) is asserted.

## Assumptions and scope

Fix \(D,L>0\). Each search cycle begins at the origin with independent, driftless Brownian motion \(B_t=\sqrt{2D}W_t\) and a fresh, independent nonnegative clock \(R\). The clock has \(\Pr(R>0)>0\) and \(\mathbb E[R^2]<\infty\); the law is unchanged between cycles. The particle detects the absorbing target at \(L\) during *both* the free-search and the return phases. If the target is not reached by \(R\), the particle moves continuously from \(B_R<L\) according to \(dY_t=-\kappa Y_t\,dt+\sqrt{2D}\,dW'_t\), with independent return noise. The return ends at the first visit to either the origin (new search cycle) or \(L\) (target found). The return clock does not continue running. Thus no teleportation and no detection suppression occur during return. At \(B_R<0\), continuity makes hitting the target before the origin impossible.

The expansion is pointwise in each clock law with finite second moment, at fixed \(L,D\); the constants hidden in \(O(\kappa)\) may depend on its distribution. No statement concerns global optimal resetting rates, moving targets, OU search in the off phase, or the energetic cost of potential switching.

## Proof

**1. Exact renewal representation.** Put \(A=\{R<T\}\) and \(X=B_S\). Let \(p_\kappa(x)\) be the probability that an OU process started at \(x\in(0,L)\) hits \(L\) before zero, and let \(u_\kappa(x)\) be the mean exit time from the return interval (for negative \(x\), the mean time to zero). Standard one-dimensional backward equations give
\[
 p_\kappa(x)=\frac{\int_0^x e^{\kappa y^2/(2D)}dy}{\int_0^L e^{\kappa y^2/(2D)}dy},\qquad
 u_\kappa(x)=\mathbb E_x[\tau_{\{0,L\}}]\quad(0<x<L).
\]
Set \(\alpha_\kappa=\Pr(T<R)+\mathbb E[\mathbf1_A\mathbf1_{\{X>0\}}p_\kappa(X)]\). A cycle succeeds with probability \(\alpha_\kappa\), and its expected duration is \(\mathbb E S+\mathbb E[\mathbf1_Au_\kappa(B_R)]\). By regeneration,
\[
 M_R(\kappa)=\frac{\mathbb E S+\mathbb E[\mathbf1_Au_\kappa(B_R)]}{\alpha_\kappa}.
\]
This expression is a renewal identity, not the novel result by itself. All terms are finite for positive \(\kappa\), since \(\mathbb E[R^2]<\infty\) and OU return times have at most polynomial-logarithmic growth in the starting distance. The limiting success probability is \(p_0>0\), because \(\Pr(R<T,B_R<0)>0\).

**2. Asymptotic boundary-value solutions.** Write \(a=-x>0\) for a negative reset position. The return-to-origin mean has derivative
\[
 \frac{d}{da}u_\kappa(-a)=\frac{c_D}{\sqrt\kappa}
 \operatorname{erfcx}\left(a\sqrt{\frac\kappa{2D}}\right),
 \qquad \operatorname{erfcx}(z)=e^{z^2}\operatorname{erfc}(z).
\]
The integral representation \(\operatorname{erfcx}(z)=(2/\sqrt\pi)\int_0^\infty e^{-v^2-2zv}dv\), for \(z\ge0\), gives globally bounded derivatives of every fixed order. Its Taylor expansion at zero therefore has a global cubic remainder bound. Integration in \(a\) yields
\[
 u_\kappa(-a)=\frac{c_Da}{\sqrt\kappa}-\frac{a^2}{2D}
  +\frac{c_Da^3}{6D}\sqrt\kappa+O(\kappa a^4).
\]
With the constants depending on fixed \(D\), the final bound is uniform for all \(a\ge0\). The Burkholder–Davis–Gundy inequality applied to \(B_{T\wedge R}\) implies \(\mathbb E[|X|^4\mathbf1_A]<\infty\) from \(\mathbb E[R^2]<\infty\), so expectation preserves the \(O(\kappa)\) remainder.

For \(0<x<L\), uniform regular perturbation of the bounded-interval boundary problem gives
\[
 u_\kappa(x)=\frac{x(L-x)}{2D}+O(\kappa),\quad
 p_\kappa(x)=\frac{x}{L}+\frac{\kappa(x^3-L^2x)}{6DL}+O(\kappa^2).
\]
Hence \(\alpha_\kappa=p_0+\kappa p_1+O(\kappa^2)\), with
\[
 p_1=\frac1{6DL}\mathbb E[(X^3-L^2X)\mathbf1_{A,\,X>0}].
\]

**3. Cancellation of the constant term.** Let
\[
 A_1=\mathbb E[-X\mathbf1_{A,\,X<0}],\qquad
 A_3=\mathbb E[(-X)^3\mathbf1_{A,\,X<0}].
\]
Optional stopping of \(B_t\) at \(S=T\wedge R\) gives \(\mathbb E[X]=0\), and therefore \(A_1=Lp_0\). Optional stopping of \(B_t^2-2Dt\) gives
\[
 2D\mathbb E S=L^2\Pr(T<R)+\mathbb E[X^2\mathbf1_A].
\]
The numerator in the renewal formula consequently has leading and constant coefficients \(c_DA_1\kappa^{-1/2}\) and \(N_0=L^2p_0/(2D)\), respectively. Dividing by \(\alpha_\kappa\) proves the two reset-law-independent terms \(Lc_D/\sqrt\kappa\) and \(L^2/(2D)\).

**4. Cubic stopped-moment identity and first protocol correction.** Combining the \(\sqrt\kappa\) numerator term with the \(\kappa\) denominator correction gives the coefficient
\[
 \frac{c_D}{6Dp_0}\left(A_3+\mathbb E[X(L^2-X^2)\mathbf1_{A,\,X>0}]\right).
\]
The expression inside parentheses equals \(L^3p_0-\mathbb E[X^3]\). The stopped cubic Itô martingale gives
\[
 \mathbb E[X^3]=6D\mathbb E\int_0^S B_t\,dt.
\]
For every \(t>0\), \(\mathbb E[B_t\mathbf1_{\{T>t\}}]=-L\Pr(T\le t)\), by the stopped Brownian martingale. Independence of \(R\) then yields
\[
 \mathbb E\int_0^S B_t\,dt
 =-L\int_0^\infty\Pr(R>t)\Pr(T\le t)dt
 =-L\mathbb E[(R-T)_+]=-LH.
\]
These interchanges are justified by \(\mathbb E[R^2]<\infty\); for example \(\mathbb E\int_0^R|B_t|dt\le C\mathbb E[R^{3/2}]<\infty\). Thus the cubic expression is \(L^3p_0+6DLH\), proving the displayed three-term expansion. Since \(H>0\), the first nonuniversal term is strictly positive.

**5. Continuous-OU comparator and Poisson specialization.** The uninterrupted OU hitting-time mean has the exact quadrature
\[
 M_{\mathrm{OU}}(\kappa)=\frac1D\int_0^L e^{\kappa x^2/(2D)}
  \left(\int_{-\infty}^{x}e^{-\kappa y^2/(2D)}dy\right)dx
 =\frac{Lc_D}{\sqrt\kappa}+\frac{L^2}{2D}
 +\frac{c_DL^3}{6D}\sqrt\kappa+O(\kappa).
\]
Subtraction proves the strict positive weak-trap correction. For \(R\sim\mathrm{Exp}(r)\), the Brownian target-hitting transform is \(\mathbb E[e^{-rT}]=e^{-q}\). The killed resolvent density or a one-dimensional Green-function calculation gives \(p_0=(1-e^{-2q})/(2q)\); independence and memorylessness give \(H=e^{-q}/r\). Substitution produces the claimed factor \(1+6/(q\sinh q)\). Differentiation of \(q\sinh q\) establishes its strict monotonicity.

**6. Singular zero-trap endpoint.** At \(\kappa=0\), Brownian first passage from any negative return position to zero has infinite mean, and such a position occurs with positive probability in every admissible cycle. Hence the total mean at precisely zero trap strength is infinite, consistent with the divergent leading coefficient.

## Verification

The standalone `verify_weak_return.py` numerically reconstructs the exit-time backward boundary-value problem, evaluates positive-position splitting probabilities independently by quadrature, evaluates the negative-position OU passage time by integration of its exact derivative, and assembles the renewal mean from killed Brownian resolvents. It also calculates the uninterrupted-OU comparator independently. Five clock laws are tested (three exponential, two deterministic) at four positive return stiffnesses. All 52 asserted checks passed in the delivered program; these are finite consistency tests and not a substitute for the uniform remainder proof.

Reproduce with `python verify_weak_return.py` (requires Python 3, NumPy and SciPy). The formula concerns fixed clock laws and cannot be numerically tested at \(\kappa=0\) by direct finite-time simulation.

## Relationship to prior work

Dubey and Pal, arXiv:2610.18814 (first public October 13, 2026), formulate stochastic-return first passage with harmonic search/return phases and active target detection in the return phase. Frydel, arXiv:2511.14646 (first public November 18, 2025), develops the same visible-return free-search subprotocol (SR-B), splitting probabilities, and an exact mean-time formula for exponential switching. Biswas, Kundu and Pal, arXiv:2307.16294, give the broader regeneration/renewal framework for stochastic home returns; these formulas are not claimed as new. Singh, arXiv:2407.02071, analyzes a target-blind return protocol and a different cost-time objective. The present claim is the **three-term weak-harmonic-return expansion for every independent finite-second-moment reset clock, including complete cancellation of clock dependence through the constant term and the explicit positive first clock-dependent correction**. The compared full Frydel and Biswas papers discuss MFPTs, phase diagrams and harmonically confined returns, but do not state this law. Existing general formulas can serve as starting points for deriving it; their mere existence is not a novelty claim for the derivation of the renewal identity.

## Limitations

Only one-dimensional driftless free-search Brownian motion, a fixed positive diffusion coefficient, a fixed positive target distance, an OU return with target visibility, and independent reset clocks of finite second moment are proved. The remainder constant may depend on the full clock law. The model omits preparation and switching costs and does not address optimal protocols beyond the infinitesimal return-trap regime. Publication-priority comparison is qualified by the possibility of unindexed supplementary asymptotic calculations and by restricted access to some presentations of the October 2026 source. The cited work already covers the exact finite-parameter MFPT framework; no independent scholarly audit has been performed.

## References

- A. Dubey and A. Pal, *Towards synergy between theory and experiments: First-passage processes under resetting with stochastic return protocols*, arXiv:2610.18814 (first submitted 2026-10-13), https://arxiv.org/abs/2610.18814.
- D. Frydel, *Search by Return: Stochastic Resetting in Fluctuating Harmonic Potentials*, arXiv:2511.14646 (first submitted 2025-11-18), https://arxiv.org/abs/2511.14646.
- A. Biswas, A. Kundu and A. Pal, *Search with stochastic home returns can expedite classical first passage under resetting*, arXiv:2307.16294, https://arxiv.org/abs/2307.16294.
- P. Singh, *Emerging cost-time Pareto front for diffusion with stochastic return*, arXiv:2407.02071, https://arxiv.org/abs/2407.02071.
- D. S. Grebenkov, *First exit times of harmonically trapped particles: a didactic review*, Journal of Physics A **48** 013001 (2015), https://doi.org/10.1088/1751-8113/48/1/013001.
