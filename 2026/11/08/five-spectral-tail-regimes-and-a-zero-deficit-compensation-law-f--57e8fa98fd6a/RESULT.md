# Five spectral-tail regimes and a zero-deficit compensation law for Gaussian-spectrogram zeros

## Finding

Let the colored-noise power spectral density be \(S_{\beta,\kappa}(x)=\exp(-\kappa |x|^\beta)\), where \(\kappa>0\) and \(\beta>0\). Write \(\rho_{\beta,\kappa}(R)\) for the population expected density of zeros of the Gaussian-window short-time Fourier transform at frequency \(R\), measured per unit time-frequency area. In the standard \(2\pi\) Fourier convention, \(\rho\) is an even function. The following are the *sharp* limits as \(R\to+\infty\):

\[
\begin{aligned}
0<\beta<1:&\quad \rho(R)-1\sim \frac{\kappa\beta(1-\beta)}{4\pi}R^{\beta-2};\\
\beta=1:&\quad 1-\rho(R)\sim \frac{\kappa\sqrt2}{2\pi}\exp\!\left(-2\pi R^2+\kappa R-\frac{\kappa^2}{8\pi}\right);\\
1<\beta<2:&\quad 1-\rho(R)\sim \frac{\kappa\beta(\beta-1)}{4\pi}R^{\beta-2};\\
\beta=2:&\quad \rho(R)\equiv \frac{2\pi}{2\pi+\kappa};\\
\beta>2:&\quad \rho(R)\sim\frac1{\beta-1}\left(\frac{4\pi}{\kappa\beta}\right)^{1/(\beta-1)}R^{-(\beta-2)/(\beta-1)}.
\end{aligned}
\]

For every parameter choice, \(\rho(0)<1\). If \(0<\beta<1\), then \(\rho(R)>1\) for all sufficiently large \(R\), and the lost central density is compensated *exactly* by the excess in the tails:

\[
\int_0^{\infty}(\rho(R)-1)\,dR=0.
\]

For all \(\beta\ge1\), one instead has \(0<\rho(R)<1\) for every finite \(R\); at \(\beta=1\), \(\int_0^{\infty}(1-\rho(R))\,dR=\kappa/(4\pi)\), while for \(\beta>1\) the integrated deficit is infinite. The Gaussian value at \(\beta=2\) is classical and is recorded only as the dividing case.

## Assumptions and scope

Consider a mean-zero, proper (circular) stationary complex Gaussian generalized process on the line with spectral density \(S_{\beta,\kappa}\). Analyze it using the unit-norm Gaussian window \(g(t)=2^{1/4}e^{-\pi t^2}\) and short-time Fourier transform \(V_g f(t,R)=\langle f,M_R T_tg\rangle\), with \((M_R h)(s)=e^{2\pi i R s}h(s)\). The expected zero intensity is defined with respect to Lebesgue measure \(dt\,dR\); multiplicities are counted and generic zeros are simple. The positive density has full spectral support and all polynomial moments are finite. The parameter \(\kappa\) and frequency variable are dimensional only through the stated normalization; a different Gaussian-window bandwidth rescales the coefficients.

Set

\[
I(R)=\int_{\mathbb R}\exp\left(-2\pi(x-R)^2-\kappa |x|^\beta\right)\,dx,
\quad
P_R(dx)=I(R)^{-1}\exp\left(-2\pi(x-R)^2-\kappa |x|^\beta\right)\,dx,
\]

and let \(m(R)=\int x\,P_R(dx)\). The exact starting identities are

\[
\rho(R)=4\pi\operatorname{Var}_{P_R}(X)
=1+\frac{1}{4\pi}\frac{d^2}{dR^2}\log I(R)
=\frac{dm(R)}{dR}.
\]

These are population first-intensity identities, not claims about individual finite observed zero patterns.

## Proof

**Step 1: intensity and exact mean-transport identity.** The colored-noise covariance after Gaussian analysis is a Gaussian analytic-function covariance multiplied on the diagonal by the Gaussian-smoothed spectral mass \(I(R)\). The Edelman–Kostlan formula gives \(\rho(R)=1+(4\pi)^{-1}(\log I)''\) in the stated normalization (the white-spectrum intensity is \(1\)). Differentiating under the integral yields \(I'/I=4\pi(m-R)\). Differentiating the exponentially tilted expectation gives \(m'=4\pi\operatorname{Var}_{P_R}(X)\). Thus all three formulas above follow, as does \(\int_0^R\rho(t)\,dt=m(R)\), since \(m(0)=0\) by symmetry.

**Step 2: sign and the central deficiency.** Put \(V(x)=\kappa|x|^\beta\). Integration by parts against the smooth, positive posterior density, with the integrable weak derivative \(V'\), gives

\[
\rho(R)=1-\operatorname{Cov}_{P_R}(X,V'(X)).
\]

For \(\beta\ge1\), \(V'\) is monotone increasing, nonconstant, and the covariance is strictly positive by the independent-copy identity \(2\operatorname{Cov}(X,V'(X))=\mathbb E[(X-X')(V'(X)-V'(X'))]\). Hence \(0<\rho(R)<1\) for all finite \(R\). For every \(\beta>0\), \(P_0\) is obtained from the centered Gaussian of variance \(1/(4\pi)\) by strictly downweighting larger \(|X|\) with \(e^{-\kappa|X|^\beta}\). The strict negative covariance of \(X^2\) with this radial decreasing factor gives \(\rho(0)<1\).

**Step 3: powers strictly below two, excluding one.** For \(0<\beta<2\), the mass of \(P_R\) concentrates in a fixed-width Gaussian neighborhood of the positive saddle \(a_R\), where \(a_R/R\to1\) and \(a_R=R-\kappa\beta R^{\beta-1}/(4\pi)(1+o(1))\). In particular, \(\operatorname{Var}_{P_R}(X)\to1/(4\pi)\). Contributions from \(x\le0\) are exponentially small in \(R^2\). Taylor expansion of \(V'\) around \(a_R\) on a growing but \(o(R)\)-width neighborhood, followed by Gaussian tail domination, yields

\[
\operatorname{Cov}_{P_R}(X,V'(X))
=\frac{\kappa\beta(\beta-1)}{4\pi}R^{\beta-2}(1+o(1))
\]

when \(\beta\ne1\). This gives the positive intensity overshoot for \(\beta<1\), and the negative correction for \(1<\beta<2\). The mean identity and integration by parts also give \(m(R)-R=-\kappa\beta R^{\beta-1}/(4\pi)(1+o(1))\).

**Step 4: the cusp \(\beta=1\).** Here the two half-line Gaussian integrals are explicit. With \(c=\kappa/(4\pi)\),

\[
I(R)=\frac{e^{\kappa^2/(8\pi)}}{2\sqrt2}
\left[e^{-\kappa R}\operatorname{erfc}\!\left(\sqrt{2\pi}(c-R)\right)
+e^{\kappa R}\operatorname{erfc}\!\left(\sqrt{2\pi}(c+R)\right)\right].
\]

Relative to the whole-line Gaussian continuation of the positive half-spectrum, the negative half-line contributes the signed correction

\[
\Delta I(R)=-2\int_0^\infty \sinh(\kappa u)e^{-2\pi(R+u)^2}\,du
\sim -\frac{\kappa}{8\pi^2R^2}e^{-2\pi R^2}.
\]

The whole-line term is \(I_0(R)=2^{-1/2}e^{-\kappa R+\kappa^2/(8\pi)}\). Differentiating the displayed exponentially small correction twice (equivalently, differentiating the exact error-function formula, which justifies termwise differentiation) yields

\[
1-\rho(R)\sim\frac{\kappa\sqrt2}{2\pi}\exp\!\left(-2\pi R^2+\kappa R-\frac{\kappa^2}{8\pi}\right).
\]

Moreover \(m(R)-R\to-\kappa/(4\pi)\).

**Step 5: the Gaussian baseline and super-Gaussian saddle.** At \(\beta=2\), the posterior is exactly Gaussian with precision \(4\pi+2\kappa\), giving \(\rho=4\pi/(4\pi+2\kappa)\). For \(\beta>2\), the unique positive saddle minimizes \(2\pi(x-R)^2+\kappa x^\beta\) and solves \(4\pi(R-a_R)=\kappa\beta a_R^{\beta-1}\), so

\[
a_R\sim\left(\frac{4\pi R}{\kappa\beta}\right)^{1/(\beta-1)}.
\]

Its local precision is \(4\pi+\kappa\beta(\beta-1)a_R^{\beta-2}\). The saddle's Gaussian fluctuation width is \(o(a_R)\), and the cubic Taylor term on this width is \(O(a_R^{-\beta/2})\). The standard localized Laplace estimate therefore gives

\[
\operatorname{Var}_{P_R}(X)\sim
\frac{1}{\kappa\beta(\beta-1)a_R^{\beta-2}},
\]

which yields the final tail formula.

**Step 6: deficit compensation.** The identity \(\int_0^R(\rho(t)-1)\,dt=m(R)-R\) is exact. Step 3 makes its limit zero for \(0<\beta<1\) (so its improper integral exists and vanishes), while Step 4 gives the finite negative limit \(-\kappa/(4\pi)\) at \(\beta=1\). For \(1<\beta<2\), Step 3 gives \(m(R)-R\to-\infty\). For \(\beta\ge2\), the explicit Gaussian expression or the super-Gaussian saddle gives the same divergence. This proves the stated global cancellation and non-cancellation laws. No uniqueness of the crossings of \(\rho=1\) is asserted.

## Verification

Run `python CHECK.py` (requires SciPy and mpmath). It integrates the exact exponentially tilted spectral posterior, compares the five predicted asymptotic regimes at multiple parameter choices, verifies the error-function cusp coefficient at 80-plus digits, checks the strict central deficit, and separately finite-differences the tilted mean to test \(m'=\rho\). It is a finite numerical test of an analytic proof, not an exhaustive interval or all-parameter certificate.

## Relationship to prior work

The Edelman–Kostlan covariance formula and Feldheim's stationary Gaussian analytic-function spectral formalism are foundational, not claimed here. Feldheim explicitly treats Gaussian and hyperbolic-secant spectra, neither giving the five-case stretched-exponential intensity asymptotics. Escudero, Koliander and Romero's 2026 colored-spectrogram work establishes the general first-intensity setting and describes asymptotics for colored noise; full primary text could not be inspected at this review, so its exact scope is an explicit originality uncertainty. The new asserted contribution is the sharp *joint* classification of \(\exp(-\kappa|x|^\beta)\) tails, global overshoot for subexponential powers, and exact compensating zero-deficit integral. The \(\beta=2\) constant-intensity case is pre-existing and only marks a phase boundary.

## Limitations

These statements concern expected first intensities for ideal proper complex Gaussian stationary noise and the exact whole-plane Gaussian STFT. They do not establish sampling-robust inference, high-order zero correlations, or recovery from a finite observation window. The cusp and other asymptotics are pointwise as \(R\to\infty\), not uniform as \(\beta\) approaches a boundary. The spectral-tail family is specific; arbitrary colored spectra need not have these regimes. The 2026 paper cited below was only accessible at abstract level; stronger prior coverage remains a publication-priority risk and requires human comparison with its full text.

## References

1. L. A. Escudero, G. Koliander, and J. L. Romero, *Zeros of the Spectrogram of Colored Noise*, arXiv:2609.18689, first public September 16, 2026. https://arxiv.org/abs/2609.18689
2. N. D. Feldheim, *Zeroes of Gaussian Analytic Functions with Translation-Invariant Distribution*, Israel J. Math. 195 (2013), 317–345; arXiv:1105.3929. Authorized openly accessible author manuscript: https://u.cs.biu.ac.il/~feldhen/Papers/zeros%20stat%20GAF.pdf
3. L. A. Escudero, N. Feldheim, G. Koliander, and J. L. Romero, *Efficient Computation of the Zeros of the Bargmann Transform Under Additive White Noise*, Found. Comput. Math. 24 (2024), 279–312 (online September 27, 2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC10879403/
