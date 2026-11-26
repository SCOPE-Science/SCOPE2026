# Sharp matching phases and unbounded rank-pairing loss for Gaussian antithetic particles

## Finding

Fix a one-dimensional diffusion stage with Gaussian displacement standard deviation \(\sigma>0\). Two pre-stage particle configurations have the same number \(N\ge2\) of particles, sorted positions \(a_1<\cdots<a_N\) and \(b_1<\cdots<b_N\), and identical positive masses \(m>0\). For a bijection \(\pi\) from the first cloud to the second, reflect each matched pair's Gaussian displacement and use independent Gaussian draws across different pairs. Write \(G_\pi\) for the reduction, relative to independent displacements between the two simulations, in the conditional spatially integrated variance of the average particle field just after this diffusion stage.

Let \(Z\sim N(0,1)\) and define
\[
 g_t(d)=\mathbb E|d+tZ|,\qquad K_\sigma(d)=g_{2\sigma}(d)-g_{\sqrt2\sigma}(d),\qquad d_c=2\sigma\sqrt{\log2}.
\]
The exact gain, already implicit in the same-sign case of Abkin--Daripa's Corollary 4.8, is
\[
 G_\pi=\frac{m^2}{4}\sum_{i=1}^N K_\sigma(a_i-b_{\pi(i)}).
\]
The following *optimization of this gain over all pairings* is the new result.

1. If every cross-cloud separation satisfies \(|a_i-b_j|<d_c\), the unique gain-maximizing permutation is rank matching \(\pi(i)=i\), and the unique gain-minimizer is reverse-rank matching \(\pi(i)=N+1-i\).
2. If the two clouds are strictly separated beyond the same threshold, that is, \(a_N+d_c<b_1\) or \(b_N+d_c<a_1\), the two extrema reverse: reverse-rank uniquely maximizes \(G_\pi\), and rank matching uniquely minimizes it.
3. The threshold \(d_c\) is sharp for the local two-pair exchange: a four-point rectangle shrunk to a displacement \(d\) has normalized rank-versus-reverse gain difference of the sign of \(-K_\sigma''(d)\), which changes exactly at \(|d|=d_c\).
4. No fixed positive approximation ratio for rank matching is possible over all configurations with \(N=2\), despite rank matching always minimizing total absolute partner distance. In fact,
\[
 \inf_{a_1<a_2,\ b_1<b_2}\frac{G_{\mathrm{rank}}}{\max_\pi G_\pi}=0.
\]

All gains are nonnegative; the ratio in item 4 has a strictly positive denominator for each admissible finite configuration.

## Assumptions and scope

The state entering a *single* Gaussian diffusion stage is fixed, and all variances are conditional on that pre-stage state. Both simulations contain \(N\) equal positive masses; their positions within each simulation are strictly ordered. New Gaussian displacements have variance \(\sigma^2\); each matched pair uses \((Z,-Z)\) and distinct pairs are independent. The spatially integrated variance is \(\int_{\mathbb R}\operatorname{Var}[(U^A(x)+U^B(x))/2\mid\text{state}]\,dx\). Its absolute integral may include an irrelevant spatially constant field baseline; the *difference between couplings* is finite and is the quantity being optimized. Every pairing is selected before the new displacements. No multi-stage or nonlinear-flux assertion is made.

## Proof

**1. Identify the exact objective.** For integrable random variables \(X,Y\) and \(Y'\) with the marginal law of \(Y\) but independent of \(X\), the indicator covariance identity is
\[
 \int_{\mathbb R}\operatorname{Cov}(\mathbf1_{\{X\le x\}},\mathbf1_{\{Y\le x\}})\,dx
 =\frac12\bigl(\mathbb E|X-Y'|-\mathbb E|X-Y|\bigr).
\]
One derivation introduces an independent copy \((X',Y')\), writes twice the covariance as the expectation of the product of indicator differences, and integrates the four indicator terms; the resulting differences of absolute distances give the displayed identity. In a reflected matched pair, \(X=a+\sigma Z\), \(Y=b-\sigma Z\), so \(X-Y\) has Gaussian scale \(2\sigma\). For the independent-coupling reference, the same difference has Gaussian scale \(\sqrt2\sigma\). The pair-mean variance has cross-covariance weight \(m^2/2\); the reduction is therefore \(m^2K_\sigma(a-b)/4\). Distinct pairs are independent, and all single-simulation terms are pairing-invariant. Summation gives the gain formula. In particular, changing the matching before drawing the next Gaussian vectors preserves both separate simulation laws, as in Abkin--Daripa's Proposition 3.3.

**2. Locate the exact curvature transition.** With \(\phi(t)=\exp(-t^2/2)/\sqrt{2\pi}\), differentiation of the normal absolute first moment gives \(g_t''(d)=2\phi(d/t)/t\). Thus
\[
 K_\sigma''(d)=\frac1{\sigma\sqrt{2\pi}}
 \left(\exp\!\left[-\frac{d^2}{8\sigma^2}\right]
 -\sqrt2\exp\!\left[-\frac{d^2}{4\sigma^2}\right]\right).
\]
Its sign equals that of \(\exp(d^2/(8\sigma^2))-\sqrt2\); it is negative exactly when \(|d|<d_c\), positive exactly when \(|d|>d_c\), and zero precisely at \(d=\pm d_c\).

**3. Apply the strict exchange principle.** For \(a<a'\) and \(b<b'\), define the rank-minus-crossed two-pair score
\[
 \begin{aligned}
 \mathcal D&=K_\sigma(a-b)+K_\sigma(a'-b')-K_\sigma(a-b')-K_\sigma(a'-b)\\
 &=-\int_a^{a'}\int_b^{b'}K_\sigma''(x-y)\,dy\,dx.
 \end{aligned}
\]
In the near regime every difference occurring in such a rectangle lies strictly within the negative-curvature interval, so \(\mathcal D>0\). Removing any crossing increases gain; iterated swaps give rank matching as the unique maximizer. Inserting crossings into any matching other than the fully reversed one decreases gain, proving unique reverse-rank minimization. In the separated regime all corresponding differences lie in a positive-curvature interval and \(\mathcal D<0\), reversing both extrema. Strictness follows from strictly ordered positions. Shrinking the side lengths of the rectangle to zero at a prescribed separation \(d\) gives \(\mathcal D/((a'-a)(b'-b))\to-K_\sigma''(d)\), proving the sharp local sign transition.

**4. Give the zero-ratio obstruction.** The kernel is strictly positive at every finite displacement: \(\partial_t g_t(d)=\sqrt{2/\pi}\exp[-d^2/(2t^2)]>0\). It vanishes at infinity, \(K_\sigma(d)\to0\) as \(|d|\to\infty\), because \(g_t(d)-|d|\to0\) for each fixed \(t>0\). Choose any fixed \(\delta>0\) and \(T>\delta\), and set
\[
 (a_1,a_2)=(0,T),\qquad(b_1,b_2)=(T-\delta,2T).
\]
Rank matching has total absolute partner distance \(2T-\delta\), whereas the crossed pairing has \(2T+\delta\). Nevertheless, with \(c=m^2/4\),
\[
 G_{\mathrm{rank}}=c\bigl[K_\sigma(T-\delta)+K_\sigma(T)\bigr]\longrightarrow0,
 \qquad G_{\mathrm{cross}}=c\bigl[K_\sigma(2T)+K_\sigma(\delta)\bigr]\longrightarrow cK_\sigma(\delta)>0.
\]
For sufficiently large \(T\), crossed pairing is the gain-maximizing permutation, and the ratio tends to zero. This proves the fourth assertion.

## Verification

The standalone standard-library program `verify.py` independently evaluates the normal absolute-moment kernel and its analytic curvature, checks the curvature signs around the exact threshold for four diffusion scales, compares second derivatives against finite differences, enumerates all permutations through five particles in both uniform-curvature regimes, and tests an explicit family with rank gain divided by optimal gain tending downward. It reports `VERIFICATION_OK` after 2,492 checks. These numerical checks are supplementary; strict global optimality and the zero-limit statement follow from the analytic proof, not from enumeration.

## Relationship to prior work

Abkin and Daripa, *Sign-switched antithetic coupling in gradient random-walk methods for convection--diffusion equations* (arXiv:2610.01120v2), Proposition 3.3 and Corollary 4.8, establish admissibility and the per-pair reduction kernel. Their Remark 4.7 proves that rank matching minimizes total absolute partner distance, and their numerical work retains rank matching. Those facts do **not** imply maximizing the sum of nonlinear Gaussian gains. The contribution here is the explicit sign-changing curvature threshold for *optimal variance matching*, the unique global optimizers in two natural regimes, and the family proving that minimal partner distance gives no positive relative gain guarantee. The exchange argument uses standard one-dimensional Monge matching principles, as described, for example, in Peyre's *Optimal Matching between Point Clouds*, and those general principles are not claimed as new.

## Limitations

This is a conditional, one-stage integrated-variance result for equal positive masses and independent reflected Gaussian pairs. Unequal/signed masses lead to weighted or mixed kernels; multiple stages, nonlinear transport, full simulation variance, finite computational time, and alternative joint cross-pair couplings are not covered. The threshold is a sharp **local curvature** switch; the two stated uniform-curvature conditions are sufficient for their global optimizer identities, not necessary criteria for arbitrary interlaced clouds. Prior specialized matching applications of this kernel may exist outside the inspected literature. No independent audit has been performed.

## References

1. Stephen Abkin and Prabir Daripa, *Sign-switched antithetic coupling in gradient random-walk methods for convection--diffusion equations*, arXiv:2610.01120v2, 12 October 2026, especially Proposition 3.3, Remark 4.7 and Corollary 4.8. https://arxiv.org/html/2610.01120v2
2. Stephen Abkin and Prabir Daripa, first preprint of the same work, arXiv:2610.01120v1, first public 1 October 2026. https://arxiv.org/abs/2610.01120
3. Gabriel Peyre, *Optimal Matching between Point Clouds*, Sections “Convex Costs on the Line” and “Concave Costs on the Line”, online course notes. https://www.gpeyre.com/ot4ml/myst/_build/html/matching/
