# Three universal transit-depth cancellation chords for a nonquadratic stellar limb profile

## Finding

For a positive stellar radial intensity law consisting of a quadratic polynomial in \(\mu\) plus a nonzero \(\mu^{3/2}\) coefficient, approximate the intensity by its **disk-area-weighted least-squares quadratic projection**, with a freely fitted normalization. Although the quadratic law is misspecified, the leading small-planet normalized transit-depth error vanishes at exactly **three universal impact parameters**, independent of every coefficient of the true profile:

\[
 b_1=0.427061711434893\ldots,\quad b_2=0.824600903594316\ldots,\quad b_3=0.981794616711549\ldots.
\]

These are the three numbers \(b=\sqrt{1-t^4}\) for the three roots \(t\in(0,1)\) of

\[
120t^4-231t^3+120t^2-8=0.
\]

For a positive coefficient of \(\mu^{3/2}\), the signed normalized model-minus-true transit depth changes sign at each of these values. These exact cancellations concern the leading infinitesimal-planet term, not a finite-size occultation or a transit-fitted model.

## Assumptions and scope

Take a circular stellar disk of unit projected radius. Put \(\mu=\sqrt{1-r^2}\), where \(r\in[0,1]\) is projected radial distance. A rotationally symmetric stellar intensity is

\[
I(\mu)=a_0+a_1\mu+a_2\mu^2+c\mu^{3/2},\quad 0\le\mu\le1,\quad c\ne0,
\]

with \(I(\mu)>0\) throughout. Let \(Q\) minimize

\[
 \int_0^1 2\mu\,[I(\mu)-Q(\mu)]^2\,d\mu
\]

among **all** real polynomials of degree at most two (an unconstrained three-coefficient fit). Assume also \(Q>0\) when interpreting the fit as a physical stellar model. This is attainable, for example for \(I(\mu)=1+\mu^{3/2}/10\). Both laws are normalized by their own disk-average intensities \(\bar I=\int_0^1 2\mu I(\mu)\,d\mu\) and \(\bar Q=\int_0^1 2\mu Q(\mu)\,d\mu\). At non-grazing impact parameter \(b\in[0,1)\), a sufficiently small opaque planet of radius ratio \(\rho\) produces a leading midtransit fractional loss \(\rho^2I(\sqrt{1-b^2})/\bar I\); similarly for \(Q\). The impact parameter is regarded as known and is **not** refitted, and no observational noise is introduced.

## Proof

The weighted Gram matrix for monomials \(\mu^i\), \(i=0,1,2\), is \(H_{ij}=2/(i+j+2)\), positive definite because the weight is positive almost everywhere. The weighted moments of \(\mu^{3/2}\) are \(v_i=4/(2i+7)\). Solving the three exact normal equations gives

\[
P_2(\mu^{3/2})=-\frac8{231}+\frac{40}{77}\mu+\frac{40}{77}\mu^2.
\]

By linearity, \(Q=a_0+a_1\mu+a_2\mu^2+cP_2(\mu^{3/2})\). Define the nonzero projection residual

\[
R(\mu)=\mu^{3/2}+\frac8{231}-\frac{40}{77}(\mu+\mu^2).
\]

It is orthogonal to each of \(1,\mu,\mu^2\) under \(2\mu\,d\mu\). In particular, orthogonality to \(1\) proves \(\bar I=\bar Q>0\) **exactly**, not just asymptotically. Consequently the true-minus-fitted leading normalized midtransit depth is

\[
\lim_{\rho\downarrow0}\rho^{-2}(\Delta_{\rm true}(b,\rho)-\Delta_{\rm quad}(b,\rho))
 =\frac{cR(\sqrt{1-b^2})}{\bar I}.
\]

To count its zeros without numerical root-finding, note that any nonzero continuous function orthogonal to \(1,\mu,\mu^2\) under a strictly positive weight must change sign at least three times: with at most two changes, multiplying by the polynomial whose roots are exactly the sign-change points (degree at most two) gives a fixed-sign, nonzero weighted integral, a contradiction. On the other hand, for \(\mu>0\),

\[
 R^{(3)}(\mu)=-\frac{3}{8\mu^{3/2}}<0.
\]

Four distinct zeros in \((0,1)\) would force a zero of \(R^{(3)}\) by three applications of Rolle's theorem. Hence there are exactly three distinct interior roots. They are simple: a multiple root together with three sign-changing roots would again contradict the zero count under derivative multiplicity, or directly the strictly negative third derivative. Replacing \(\mu\) with \(t^2\) yields

\[
231R(t^2)=-\bigl(120t^4-231t^3+120t^2-8\bigr).
\]

Exact rational sign evaluations bracket the three positive roots in \((435/1000,437/1000)\), \((751/1000,753/1000)\), and \((950/1000,952/1000)\). The map \(b=\sqrt{1-t^4}\) is strictly decreasing. Their numerical values give the three stated impact parameters, with no additional zero for \(0\le b<1\). For \(c>0\), the true-minus-fitted depth has successive signs negative, positive, negative, positive as \(b\) increases through the three roots (reverse the signs for \(c<0\)). Since \(R(1)=-1/231\), this also fixes the initial sign. The same quadratic coefficients and roots apply to every polynomial baseline and every nonzero coefficient \(c\).

## Verification

Run the standalone standard-library Python file `checker.py`. It verifies the normal equations, Gram positivity, rational interval signs, absence of an extra positive quartic root, the exact average equality for sample profiles, and the positivity of one admissible physical profile. These finite checks supplement, but do not replace, the proof by orthogonality and Rolle's theorem. The code prints the three roots and impact parameters.

## Relationship to prior work

Keers and coauthors introduced and tested a three-parameter stellar limb-darkening law containing a \(\mu^{3/2}\) term, and showed that quadratic-law fitting can bias transit inference (arXiv:2410.18617v1, first public version 2024-10-24). Espinoza and Jordán studied quadratic-law biases and how limb coefficients depend on the fitting method (2015, 2016). Heller provides analytic disk-averaged and transit-depth formulas for common stellar intensity laws (2019). The present claim is **not** the classical existence of least-squares normal equations or an empirical claim that quadratic fits are universally safe; it computes and proves the three precise, coefficient-independent zero-error chords for the stated area-weighted projection. It does not assert that the same roots occur under other calibrations or jointly fitted transit geometries.

## Limitations

The result holds only for a full-disk \(2\mu\)-weighted intensity fit with a free constant term, a single omitted \(\mu^{3/2}\) basis term, exact radial symmetry, an infinitesimally small opaque planet, and fixed known geometry. Finite-sized planets average over an occulted region; noise, surface heterogeneity, different limb-darkening exponents, different least-squares weights, and joint light-curve fits can shift or eliminate the cancellations. Their utility as observational design points requires additional finite-radius and uncertainty analysis. The literature comparison is not an exhaustive proof of historical priority.

## References

1. Keers, R. E., et al., *Reliable Transmission Spectrum Extraction with a Three-Parameter Limb Darkening Law*, arXiv:2410.18617v1 (2024-10-24), https://arxiv.org/abs/2410.18617.
2. Espinoza, N., and Jordán, A., *Limb darkening and exoplanets: testing stellar model atmospheres and identifying biases in transit parameters*, MNRAS 450 (2015), https://doi.org/10.1093/mnras/stv744.
3. Espinoza, N., and Jordán, A., *Limb darkening and exoplanets – II. Choosing the best law for optimal retrieval of transit parameters*, MNRAS 457 (2016), https://doi.org/10.1093/mnras/stw224.
4. Heller, R., *Analytic solutions to the maximum and average exoplanet transit depth for common stellar limb darkening laws* (2019), https://doi.org/10.1051/0004-6361/201834620.
