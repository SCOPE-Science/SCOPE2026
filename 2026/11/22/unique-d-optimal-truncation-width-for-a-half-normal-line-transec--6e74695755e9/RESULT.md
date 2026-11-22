# Unique D-optimal truncation width for a half-normal line transect with width-dependent survey cost

## Finding
Consider a Poisson population surveyed by a line transect under a half-normal detection function, when both the population intensity and detection scale must be estimated from fully recorded detection distances. For every nonnegative fixed-to-width cost ratio, there is precisely one global D-optimal truncation half-width. In dimensionless units it increases strictly with that cost ratio and is never smaller than \(2.48340322946\ldots\) detection-scale units.

More precisely, define \(J_j(a)=\int_0^a t^j e^{-t^2/2}\,dt\), \(F(a)=J_0(a)J_4(a)-J_2(a)^2\), and \(E(a)=aF'(a)/F(a)\). Then for every \(\kappa\geq0\), the unique optimum \(a_\kappa>0\) is the unique solution of
\[
 E(a_\kappa)=\frac{2a_\kappa}{a_\kappa+\kappa}.
\]
The function \(E\) decreases strictly from \(6\) to \(0\), and \(a_\kappa\) increases strictly in \(\kappa\); in particular, \(a_0=2.4834032294617\ldots\), and \(a_\kappa\to\infty\) as \(\kappa\to\infty\). The limiting minimum-width design retains detections only as far as an edge detection probability \(e^{-a_0^2/2}=0.045792\ldots\), approximately \(4.58\%\).

## Assumptions and scope
Animals or ecological objects have unknown constant intensity \(\lambda>0\) in a homogeneous planar Poisson point process. Along a nonoverlapping straight transect of length \(L>0\), an object at absolute perpendicular distance \(x\leq w\) is independently detected with probability \(\exp(-x^2/(2\sigma^2))\), for unknown scale \(\sigma>0\); there are no detections beyond the truncation half-width \(w>0\). Every detected perpendicular distance is observed exactly, and detections are independent conditional on the population. Ignore end effects and overlapping strips. The detected distances form a Poisson point process on \([0,w]\) with intensity \(2L\lambda\exp(-x^2/(2\sigma^2))\,dx\).

A fixed survey budget \(B>0\) buys transect length \(L=B/(c_0+c_1w)\), with base cost \(c_0\geq0\) and width cost \(c_1>0\). This is a local D-optimal problem at nominal \(\sigma\), for the joint parameter vector \((\log\lambda,\log\sigma)\) and the complete marked point-process likelihood. Set \(a=w/\sigma\) and \(\kappa=c_0/(c_1\sigma)\); both are nonnegative, with \(a>0\). No limit on field-area size is imposed within the model.

## Proof
**1. Exact information determinant.** The score of one detected distance with respect to \((\log\lambda,\log\sigma)\), in the Poisson point-process likelihood, is the intensity's log-derivative \((1,(x/\sigma)^2)\). Integrating its outer product against the detected-point intensity gives
\[
 I(a)=2L\lambda\sigma\begin{pmatrix}J_0(a)&J_2(a)\\J_2(a)&J_4(a)\end{pmatrix}.
\]
Thus \(\det I(a)=4L^2\lambda^2\sigma^2F(a)\). The budget identity cancels all factors independent of the design, so maximizing \(\det I\) is exactly maximizing
\[
 Q_\kappa(a)=\frac{F(a)}{(a+\kappa)^2}\quad(a>0).
\]
The determinant \(F(a)\) is strictly positive for every \(a>0\), since it is the strictly positive variance Gram determinant of the linearly independent functions \(1\) and \(t^2\) under positive weight \(e^{-t^2/2}\) on \((0,a)\).

**2. Strictly decreasing elasticity.** Differentiation gives the nonstandard but elementary identity
\[
 F'(a)=e^{-a^2/2}\int_0^a(a^2-s^2)^2e^{-s^2/2}\,ds
 =a^5\int_0^1(1-u^2)^2e^{-a^2(1+u^2)/2}\,du>0.
\]
Here is a global proof, not a numerical monotonicity inference. Put \(a=e^x\) and define \(G(x)=e^xF'(e^x)\). Apart from a positive factor independent of \(x\), \(G\) is the integral over \(0<u<1\) of the exponential of
\[
 \Phi(x,u)=6x+2\log(1-u^2)-\tfrac12e^{2x}(1+u^2).
\]
The term \(2\log(1-u^2)\) is concave in \(u\), and \(-e^{2x}(1+u^2)/2\) is jointly strictly concave for \(0<u<1\): its Hessian has negative diagonal entries and determinant \(2e^{4x}(1-u^2)>0\). Consequently \(\Phi\) is jointly concave in \((x,u)\). By the Prékopa marginal log-concavity theorem, \(G(x)\) is log-concave. Moreover
\[
 F(e^x)=\int_{-\infty}^{x}G(y)\,dy,
\]
which is log-concave as the cumulative integral of a log-concave function. Therefore
\[
 E(e^x)=\frac{d}{dx}\log F(e^x)
\]
is nonincreasing in \(x\). It is actually *strictly* decreasing: \(F\) is positive analytic on \((0,\infty)\), so a constant interval for its analytic elasticity would force a global constant, which conflicts with the two endpoint limits below. From the Taylor expansions of the defining integrals,
\[
 F(a)=\frac4{45}a^6+O(a^8),\qquad E(a)\longrightarrow6\quad(a\downarrow0).
\]
As \(a\to\infty\), the Gaussian moments tend to \(J_0=J_2=\sqrt{\pi/2}\) and \(J_4=3\sqrt{\pi/2}\), giving \(F(a)\to\pi\), while \(aF'(a)\to0\). Hence \(E(a)\to0\).

**3. Global optimum and sensitivity.** Logarithmic differentiation gives
\[
 a\frac{d}{da}\log Q_\kappa(a)=E(a)-\frac{2a}{a+\kappa}.
\]
The first term decreases strictly from \(6\) to \(0\). The second term is nondecreasing in \(a\), tends to \(2\) at infinity, and equals \(2\) for all \(a>0\) when \(\kappa=0\). Thus there is exactly one zero, with strictly positive derivative before it and strictly negative derivative afterward. Also \(Q_\kappa(a)\to0\) at both endpoints by the above asymptotics. The zero is therefore the unique global maximum. At any fixed \(a>0\), the comparison term decreases strictly with increasing \(\kappa\), so the unique zero moves strictly right. Finally, if \(a_\kappa\) stayed bounded as \(\kappa\to\infty\), the right side of the defining equation would tend to zero while \(E\) remained strictly positive; hence \(a_\kappa\to\infty\). Solving the unique zero at \(\kappa=0\) gives the stated constant and edge probability.

## Verification
Run `python checker.py` using Python's standard library. It checks moment recurrences, the derivative identity against finite differences, positivity, elasticity monotonicity on a diagnostic grid, five independently specified optimal roots, and strictly smaller objective values at off-optimal alternatives. The bundled checker passed 1258 deterministic assertions. The proof of global uniqueness depends on the concavity and analytic arguments above, *not* finite grid diagnostics.

For reference, numerical solutions are \(a_0=2.4834032294617\ldots\), \(a_1=2.7441753329137\ldots\), and \(a_5=3.1663319905717\ldots\). The unit-width calculation is dimensionless, and the physical optimal half-width is \(w_*=\sigma a_\kappa\).

## Relationship to prior work
The thinned spatial Poisson observation framework and simultaneous detection/intensity inference are established in Johnson, Laake, and Ver Hoef (2009 online/2010 issue), not new here. Clark (2016) analyzes efficiency of conventional distance-sampling versus strip-transect estimators, including an MSE-optimal truncation for a different, biased strip-estimation objective. Knights and collaborators (2021) optimize the fraction of distances to measure under high encounter rates, not the physical truncation width under a joint-density-and-scale information determinant. This theorem differs in its entire cost family, explicit joint information criterion, rigorous unique-optimum proof, and strict monotone law for all admissible cost ratios. General log-concavity results used in the proof are existing mathematical tools, not claimed as discoveries.

## Limitations
The result is local, idealized design theory and is not a field recommendation independent of prior detection-scale calibration. Independent detection, homogeneous Poisson abundance, known half-normal functional form, exact measured distances, strip-width-dependent survey cost, and no overlapping/end effects are essential assumptions. Maximizing joint Fisher determinant need not minimize variance of density alone or actual finite-sample error. Historical-priority risk remains: the full 2009/2010 thinned-point-process article was not accessible for whole-document comparison, and the broader optimal-design literature could contain a mathematically equivalent general theorem. No independent scientific audit has been performed.

## References
1. Johnson, D. S., Laake, J. L., and Ver Hoef, J. M. (2009 online; 2010 issue). *A model-based approach for making ecological inference from distance sampling data.* *Biometrics* 66, 310–318. https://doi.org/10.1111/j.1541-0420.2009.01265.x (version of record online 2009-05-13 per publisher history).
2. Clark, R. G. (2016). *Statistical Efficiency in Distance Sampling.* *PLOS ONE* 11, e0149298. https://doi.org/10.1371/journal.pone.0149298 (published 2016-03-07).
3. Knights, K., and collaborators (2021). *Efficient effort allocation in line-transect distance sampling of high-density species: When to walk further, measure less-often and gain precision.* *Methods in Ecology and Evolution*. https://doi.org/10.1111/2041-210X.13589.
4. Prékopa, A. (1973). *On logarithmic concave measures and functions.* *Acta Scientiarum Mathematicarum* 34, 335–343 (marginal and cumulative log-concavity theorem used in the proof).
