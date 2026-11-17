# Sharp kinetic–potential energy anticorrelation boundary in a telegraph-driven inertial oscillator

## Finding
Consider the stationary real-valued process
\[
\dot X=V,\qquad \dot V=-2aV-\omega^2X+f\sigma_t,
\]
where \(a,\omega,\nu>0\), \(f\ne0\), and \(\sigma_t\in\{-1,1\}\) is the stationary symmetric continuous-time Markov chain with transitions at rate \(\nu\) in either direction. Let
\[
k=\frac{\omega^2}{a^2}>0,\quad g=\frac{\nu}{a}>0,\quad
D_0=4g^2+4g+k,\quad D_9=4g^2+12g+9k,\quad D_8=4g^2+12g+k+8.
\]
For the normalized stationary variables \(\xi=a^2X/f\) and \(u=aV/f\), set
\[\mathcal C(k,g)=\operatorname{Cov}(\xi^2,u^2).\]
Then
\[
\boxed{\mathcal C(k,g)=-\frac{gP_k(g)}{2(k+3)D_0^2D_9D_8}}
\]
with the quartic
\[
P_k(g)=48g^4+384g^3+(104k+1152)g^2+(272k+1104)g-3(k-24)(3k+4).
\]
The following classification is exact for every \(k,g>0\):

- If \(0<k\le24\), then \(\mathcal C(k,g)<0\) for all \(g>0\).
- If \(k>24\), exactly one \(g_*(k)>0\) satisfies \(\mathcal C(k,g_*(k))=0\). The covariance is strictly positive for \(0<g<g_*(k)\) and strictly negative for \(g>g_*(k)\).
- The crossover is strictly increasing in \(k\), and its endpoint asymptotics are
\[
\lim_{k\downarrow24}\frac{g_*(k)}{k-24}=\frac{19}{636},\qquad
\lim_{k\to\infty}\frac{g_*(k)}{\sqrt{k}}=\frac1{\sqrt{12}}.
\]

The same sign classification applies to the stationary covariance of potential and kinetic energies, since
\[
\operatorname{Cov}\left(\frac{\omega^2X^2}{2},\frac{V^2}{2}\right)
=\frac{\omega^2f^4}{4a^6}\,\mathcal C(k,g).
\]
It remains valid if an independent centered stationary Gaussian driving force is added to the velocity equation, provided the resulting stationary position and velocity have finite second moments: the additional Gaussian stationary contribution has zero fourth joint cumulant and vanishing equal-time position–velocity covariance.

## Assumptions and scope
The physical damping, trap frequency, and telegraph flip rate are strictly positive; the force amplitude is nonzero. There is no spatial reset, stiffness switching, or multiplicative noise. For the basic formula no thermal white noise is present. The final Gaussian-robustness statement allows independent additive stationary Gaussian forcing, including ordinary thermal white acceleration noise; it is not a claim about non-Gaussian or dependent additives. At \(\nu=0\) the invariant measure need not be unique, so the sign assertion assumes \(\nu>0\), though one-sided limits exist.

The deterministic drift matrix \(\begin{psmallmatrix}0&1\\-\omega^2&-2a\end{psmallmatrix}\) is Hurwitz for every \(a,\omega>0\). Convolution of its exponentially decaying impulse response against a two-sided stationary telegraph chain constructs a unique attracting stationary solution with bounded moments of every order. Stationarity and simultaneous sign reversal \((X,V,\sigma)\mapsto(-X,-V,-\sigma)\) imply centered odd moments vanish. Differentiating \(\mathbb E[X^2]\) gives \(\mathbb E[XV]=0\).

## Proof
Rescale time by \(\tau=at\). Then the normalized dynamics are
\[
\xi'=u,\qquad u'=-k\xi-2u+\sigma,\qquad \sigma\mapsto-\sigma\text{ at rate }g.
\]
For integers \(i,j\ge0\) and \(e\in\{0,1\}\), write \(M_{ij}^{(e)}=\mathbb E[\xi^i u^j\sigma^e]\). The stationary Markov generator, with \(\sigma^2=1\), gives the complete recurrence
\[
(2j+2ge)M_{ij}^{(e)}-iM_{i-1,j+1}^{(e)}+jkM_{i+1,j-1}^{(e)}
=jM_{i,j-1}^{(1-e)},
\]
where terms with negative indices are zero. Start with \(M_{00}^{(0)}=1\) and \(M_{00}^{(1)}=0\). Sign symmetry eliminates \(M_{ij}^{(e)}\) whenever \(i+j+e\) is odd. At each total degree the remaining linear system has a unique solution, by the stationary construction and stability of its finite-dimensional polynomial generator.

At degree two, direct elimination gives
\[
M_{20}^{(0)}=\frac{g+1}{kD_0},\qquad M_{02}^{(0)}=\frac g{D_0},\qquad M_{11}^{(0)}=0.
\]
At degree four, the same recurrence gives
\[
M_{22}^{(0)}=\frac{gH_k(g)}{2k(k+3)D_0D_9D_8},
\]
where
\[
H_k(g)=8(k+3)g^3+36(k+4)g^2+(18k^2+58k+264)g+27k^2-6k+144.
\]
Subtracting \(M_{20}^{(0)}M_{02}^{(0)}\), bringing both terms to the common positive denominator, and expanding yields the displayed exact \(\mathcal C(k,g)\) and \(P_k(g)\). This algebra is checked against independently solved exact-rational generator systems in `verify.py`.

All denominator factors are positive for \(k,g>0\). The coefficients of the positive powers of \(g\) in \(P_k\) are strictly positive. For \(k\le24\), its constant coefficient is nonnegative, so \(P_k(g)>0\) for \(g>0\). For \(k>24\), the constant is negative, while \(P_k'(g)>0\) for \(g\ge0\) and \(P_k(g)\to\infty\). Thus a unique positive root exists, with the asserted signs.

For monotonicity, rewrite \(P_k(g)\) as a quadratic in \(k\):
\[
P_k(g)=-9k^2+B(g)k+C(g),
\]
where \(B(g)=104g^2+272g+204\) and \(C(g)=48g^4+384g^3+1152g^2+1104g+288\). Both are strictly increasing for \(g>0\). The unique positive \(k\)-root
\[
k_*(g)=\frac{B(g)+\sqrt{B(g)^2+36C(g)}}{18}
\]
is therefore strictly increasing; it is the inverse of \(g_*(k)\). At \((k,g)=(24,0)\), implicit differentiation of \(P_k(g)=0\) yields \(g_*'(24^+)=228/7632=19/636\). For large \(k\), the unique root has \(g_*(k)\) of order \(\sqrt{k}\); writing \(g=c\sqrt{k}\) and dividing by \(k^2\) gives \(48c^4+104c^2-9=0\), whose unique positive solution is \(c=1/\sqrt{12}\). Monotonicity of the quartic and comparison at \(c\pm\varepsilon\) make this asymptotic rigorous.

Finally the fourth joint cumulant satisfies
\[
\kappa_4(\xi,\xi,u,u)=\operatorname{Cov}(\xi^2,u^2)-2\operatorname{Cov}(\xi,u)^2
=\mathcal C(k,g).
\]
A centered Gaussian vector has no fourth cumulant. Independent additive Gaussian forcing supplies an independent Gaussian stationary vector. Cumulants of independent sums add, and stationarity gives zero equal-time position–velocity covariance for each component and the sum. Hence the stated covariance is unchanged.

## Verification
The standalone Python 3 standard-library program `verify.py` solves the stationary generator's rational linear systems afresh for all degrees up to four, rather than substituting the fourth-moment formula into itself. It tests a grid of 63 strictly positive rational parameter pairs, compares exact second and mixed fourth moments with the analytic expressions, verifies sign assertions, and checks two explicit rational witnesses. Its recorded execution result is `PASS: 418 exact-rational checks of the independent generator system and closed form`.

At \(k=36\), the covariance is exactly \(5795375/30528348533124>0\) for \(g=1/10\), but is \(-127/32089200<0\) for \(g=1\). The unique crossover is approximately \(g_*(36)=0.3221774006\). These examples illustrate the theorem but do not replace the universal sign proof.

## Relationship to prior work
Dutta, Kundu, Sabhapandit and Basu (2024), arXiv:2406.06120, treat precisely this inertial run-and-tumble oscillator, prove a general stationary moment recurrence, and analyze marginal distributions and second moments. Consequently, the mixed fourth moment can in principle be obtained by carrying out their recurrence; the calculation method is not claimed as new. Their inspected main text and relevant appendix passages do not state the exact potential–kinetic energy covariance sign boundary, its unique switching-rate transition, the stiffness constant \(24\), or the boundary asymptotics. A marginal position-kurtosis calculation concerns a different tensor component and does not by itself imply the cross-energy sign or Gaussian-additive invariance.

Pawula (1987) develops more general output-moment methods for dichotomous-noise-driven oscillators. Méndez, Campos and Horsthemke (2013) treat stationary oscillator energy statistics under Gaussian noise; for a stationary harmonic Gaussian oscillator, equal-time position and velocity are independent and the mixed fourth cumulant vanishes. The present sign transition arises specifically from non-Gaussian telegraph forcing. Older general moment methods may implicitly yield the rational function without stating the sharp global sign theorem.

## Limitations
This is a stationary, linear, one-dimensional, additive-telegraph result, not an assertion about transient energy exchange, nonlinear potentials, arbitrary active forcing, or non-Gaussian independent additions. The 1987 primary paper's full text was not accessible in this inspection; its moment framework remains a publication-priority risk. The 2024 paper supplies a general recurrence sufficient to calculate the expression, so the claim of distinct contribution is the globally proved sign classification and thermal Gaussian robustness, not algorithmic priority over that recurrence. No independent scientific audit or external experimental validation has been performed.

## References
1. D. Dutta, A. Kundu, S. Sabhapandit, U. Basu, *Harmonically trapped inertial run-and-tumble particle in one dimension*, arXiv:2406.06120 (first public 2024-06-10), https://arxiv.org/abs/2406.06120 .
2. R. F. Pawula, *Dichotomous-noise-driven oscillators*, Physical Review A **35**, 3102 (1987), https://doi.org/10.1103/PhysRevA.35.3102 .
3. V. Méndez, D. Campos, W. Horsthemke, *Stationary energy probability density of oscillators driven by a random external force*, Physical Review E **87**, 062132 (2013), https://doi.org/10.1103/PhysRevE.87.062132 .
4. L. Caprini and U. Marini Bettolo Marconi, *Inertial self-propelled particles*, arXiv:2009.14032 (2020), https://arxiv.org/abs/2009.14032 .
