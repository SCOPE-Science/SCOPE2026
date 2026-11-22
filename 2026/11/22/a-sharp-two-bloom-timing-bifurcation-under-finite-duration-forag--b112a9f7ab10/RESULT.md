# A sharp two-bloom timing bifurcation under finite-duration foraging

## Finding
For all Gaussian widths \(\sigma>0\), half-durations \(w>0\), and half-separations \(a>0\), define the idealized resource profile and fixed-duration intake
\[
R_a(t)=\exp\!\left(-\frac{(t-a)^2}{2\sigma^2}\right)+\exp\!\left(-\frac{(t+a)^2}{2\sigma^2}\right),\qquad
J_a(z)=\int_{z-w}^{z+w}R_a(t)\,dt.
\]
The optimizer \(z\in\mathbb R\) is the center of a contiguous foraging activity window of length \(2w\). For each \(w,\sigma>0\) there is a **unique** sharp bloom-separation threshold \(a_c>w\), defined by
\[
\frac{a_cw}{\sigma^2}=\operatorname{artanh}\!\left(\frac{w}{a_c}\right).
\]
If \(0<a\le a_c\), the sole global optimum is \(z=0\): the response has exactly one stationary point. If \(a>a_c\), exactly three stationary points occur: \(z=0\) is a strict local minimum, and exactly two global maxima occur at \(z=\pm z_*(a)\), where \(z_*(a)>0\) is the unique positive solution of
\[
R_a(z+w)=R_a(z-w).
\]
At \(a=a_c\), \(z=0\) is a strict, quartically flat maximum. As \(a\downarrow a_c\) from above,
\[
z_*(a)=\sqrt{\frac{3\sigma^2}{a_c}\left(1+\frac{\sigma^2}{a_c^2-w^2}\right)}\,\sqrt{a-a_c}+O\!\left((a-a_c)^{3/2}\right).
\]
Equivalently, for fixed \(a\le\sigma\), every positive activity duration gives one optimum; for \(a>\sigma\), one unique \(w_c\in(0,a)\) satisfies \(\operatorname{artanh}(w_c/a)/(w_c/a)=a^2/\sigma^2\). Then two optima occur exactly when \(0<w<w_c\), and one optimum when \(w\ge w_c\). Thus a resource landscape with two peaks may nevertheless have only one optimal center after finite-duration integration.

## Assumptions and scope
The time coordinate extends over \(\mathbb R\). The two Gaussian blooms have identical amplitude and width, are centered at \(\pm a\), and are added linearly. The consumer chooses the center \(z\) of exactly one uninterrupted, uniformly active, fixed-length window. Intake is linear in instantaneous resource abundance; there is no crowding, depletion, mortality, travel delay, learning, or landscape boundary. The theorem classifies *all* stationary points and global maxima for every finite \(a,w,\sigma>0\). It is not a dynamical plankton model and makes no empirical prediction.

## Proof
Put \(G(x)=\exp(-x^2/(2\sigma^2))\). The function \(R_a\) and the window integral \(J_a\) are even and real analytic, and \(J_a(z)\to0\) as \(|z|\to\infty\). Differentiating moving endpoints gives
\[
J_a'(z)=R_a(z+w)-R_a(z-w),\qquad J_a''(0)=2R_a'(w).
\]
Write \(p=a+w\) and \(q=a-w\). If \(w\ge a\), both terms in
\[
\sigma^2 R_a'(w)=(a-w)e^{-q^2/(2\sigma^2)}-(a+w)e^{-p^2/(2\sigma^2)}
\]
are nonpositive, with the second strictly negative. If \(w<a\), its sign equals the sign of
\[
\frac{aw}{\sigma^2}-\operatorname{artanh}\!\left(\frac wa\right),
\]
because \(q e^{-q^2/(2\sigma^2)}>p e^{-p^2/(2\sigma^2)}\) holds exactly when \(2aw/\sigma^2>\log(p/q)\). For fixed \(w,\sigma\), the first side strictly increases with \(a>w\), whereas \(\operatorname{artanh}(w/a)\) strictly decreases, from infinity to zero. Hence there is a unique \(a_c>w\), with \(J_a''(0)<0\) for \(a<a_c\), zero at equality, and positive for \(a>a_c\).

**Zero-count lemma.** A nonzero real sum of \(k\) exponentials \(\sum_{j=1}^k c_j e^{\lambda_j z}\) with distinct real \(\lambda_j\) has at most \(k-1\) real zeros, multiplicities counted. For proof, divide by the smallest exponential, differentiate, and induct: if the original had \(k\) or more zeros counted with multiplicities, Rolle's theorem would force at least \(k-1\) zeros of a sum of only \(k-1\) exponentials, contradicting the inductive bound \(k-2\). The induction starts with a single nonvanishing exponential.

Factoring the common positive multiplier \(e^{-z^2/(2\sigma^2)}\) out of \(J_a'(z)\) leaves at most four real exponentials in \(z\), whose exponents correspond to the four centers \(\pm a\pm w\). The lemma therefore bounds the total number of real stationary points by three, multiplicities included (and covers coincident centers by merging terms). The derivative is odd. For \(z>a+w\), \(R_a\) is strictly decreasing on the interval \([z-w,z+w]\), so \(J_a'(z)<0\).

If \(J_a''(0)<0\), the derivative is negative immediately to the right of zero. Any positive root would either produce a sign reversal requiring another positive root to recover its negative eventual sign, or itself have even multiplicity. The symmetric negative roots plus the root at zero would then contribute at least five zeros, impossible. Hence \(z=0\) is the only stationary point and unique global maximum. If \(J_a''(0)>0\), the derivative is initially positive on the positive half-line and eventually negative. It must cross exactly once there; otherwise symmetry would violate the three-zero bound. That crossing is simple and a strict global maximum on the positive half-line; symmetry gives the other one, while zero is a strict local minimum.

At the critical parameter put \(K=q\exp(-q^2/(2\sigma^2))=p\exp(-p^2/(2\sigma^2))>0\), evaluated at \(a=a_c\). Direct differentiation yields
\[
R_{a_c}'''(w)=\frac K{\sigma^6}(q^2-p^2)=-\frac{4a_cwK}{\sigma^6}<0.
\]
Consequently \(J_{a_c}'(z)=R_{a_c}'''(w)z^3/3+O(z^5)\) and \(J_{a_c}^{(4)}(0)=2R_{a_c}'''(w)<0\). Its central maximizer is strict and quartically flat; the three-zero bound excludes other stationary points.

For the splitting coefficient, differentiate \(R_a'(w)\) with respect to \(a\) at the threshold:
\[
\left.\partial_a R_a'(w)\right|_{a=a_c}
=\frac{2wK}{\sigma^2}\left(\frac1{a_c^2-w^2}+\frac1{\sigma^2}\right)>0.
\]
Analyticity and symmetry give \(J_a'(z)/z=2R_a'(w)+(R_a'''(w)/3)z^2+O(z^4)\); the implicit function theorem applied in coordinates \((a,z^2)\), using the nonzero cubic coefficient, gives a unique analytic small positive \(z^2\) with
\[
z_*^2=-\frac{6\,\partial_aR_a'(w)|_{a=a_c}}{R_{a_c}'''(w)}(a-a_c)+O((a-a_c)^2),
\]
which simplifies to the claimed square-root expansion. Finally, for fixed \(a>\sigma\), \(u\mapsto\operatorname{artanh}(u)/u=\sum_{j\ge0}u^{2j}/(2j+1)\) is strictly increasing from \(1\) to infinity on \((0,1)\), so the claimed unique duration cutoff follows. If \(a\le\sigma\), the strict inequality \(\operatorname{artanh}(u)>u\) forbids splitting.

## Verification
`verify.py` reproduces the unique threshold and representative one/two-mode cases using Python's standard library; it also checks the square-root coefficient numerically against two vanishingly small supercritical perturbations. These numerical tests are supplementary: the finite root samples are not used to establish the universal theorem. The proof above directly establishes the exponential zero bound, equality boundary and the asymptotic.

With \(\sigma=w=1\), the critical separation is approximately \(a_c=1.199678640257734\). At \(a=1\), the only maximizer is zero. At \(a=1.5\), the positive optimal center is approximately \(1.35065977854\); the corresponding negative center is equally optimal. The predicted square-root coefficient is approximately \(2.86251431024\).

## Relationship to prior work
Gronchi et al. (2023) investigate plankton bloom–grazer phenological asynchrony using a detailed ecological simulation, whereas the present theorem is an exhaustive analytic classification of a different, idealized two-bloom resource-overlap functional. Armstrong et al. (2016) demonstrate ecological importance of staggered resource waves, but the accessible abstract and reference material do not establish this exact duration-induced symmetry breaking. McNamara et al. (2011) study optimal phenological timing under uncertain cues and quadratic mistiming costs, not a two-peak fixed-window objective. Aprausheva and Sorokin (2013), and Li et al. (2022), address modes of *unsmoothed* Gaussian mixtures and related statistical questions. The classical exponential-sum zero-count theorem supplies the general upper-bound tool; the complete finite-window threshold, all equality cases, and splitting coefficient are the specific claims assessed here, rather than a claim to have invented zero counting or Gaussian-mixture theory.

## Limitations
The theorem concerns two identical Gaussian resource pulses and deterministic fixed-duration integration; unequal pulse amplitudes, stochastic environmental cues, nonuniform feeding, travel costs, and multi-patch routes are outside its scope. It does not prove that measured ecosystems follow Gaussian resource curves. This is a self-review, not independent validation. Wider historical results on mode changes under uniform convolution could potentially subsume the theorem and remain a priority risk; an older Gaussian-mixture paper could not be inspected beyond its abstract.

## References
1. E. Gronchi, D. Straile, S. Diehl, K. D. Jöhnk, F. Peeters, “Impact of climate warming on phenological asynchrony of plankton dynamics across Europe,” *Ecology Letters* 26 (2023), 717–728; first published 2023-03-04. https://doi.org/10.1111/ele.14190
2. J. B. Armstrong et al., “Resource waves: phenological diversity enhances foraging opportunities for mobile consumers,” *Ecology* 97 (2016), 1099–1112. https://doi.org/10.1890/15-0554.1
3. J. M. McNamara, Z. Barta, M. Klaassen, S. Bauer, “Cues and the optimal timing of activities under environmental changes,” *Ecology Letters* 14 (2011), 1183–1190. https://doi.org/10.1111/j.1461-0248.2011.01686.x
4. N. N. Aprausheva, S. V. Sorokin, “Exact equation of the boundary of unimodal and bimodal domains of a two-component Gaussian mixture,” *Pattern Recognition and Image Analysis* 23 (2013), 341–347.
5. Y. Li, K.-T. Fang, P. He, H. Peng, “Representative Points from a Mixture of Two Normal Distributions,” *Mathematics* 10 (2022), 3952. https://doi.org/10.3390/math10213952
