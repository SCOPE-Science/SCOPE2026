# Unique transverse kurtosis reversal for a completely reset trapped active swimmer

## Finding

Consider a two-dimensional active Brownian swimmer with a fixed resetting heading. Its stationary coordinate perpendicular to the heading has a unique, globally sharp change from negative to positive fourth cumulant as the full-state reset rate increases. Define dimensionless angular diffusivity \(\delta=D_r/\kappa\) and reset rate \(\rho=\lambda/\kappa\). For every \(\delta>0\), the critical rate is the unique positive root of the explicit polynomial below, and it obeys
\[\rho_*(\delta)\sim8\delta\quad(\delta\downarrow0),\qquad\rho_*(\delta)\sim7/\delta\quad(\delta\to\infty).\]
At arbitrarily rapid resetting, the transverse standardized excess kurtosis approaches \(57\), although the absolute coordinate moments vanish.

## Assumptions and scope

Let \(\kappa,v,D_r,\lambda>0\), and let \(W\) be standard Brownian motion. Between complete resets, the stochastic evolution is
\[dX=(-\kappa X+v\cos\Theta)\,dt,\quad dY=(-\kappa Y+v\sin\Theta)\,dt,\quad d\Theta=\sqrt{2D_r}\,dW.\]
Independent Poisson resets of rate \(\lambda\) restore \((X,Y,\Theta)=(0,0,0)\). The angular coordinate is considered modulo \(2\pi\). There is no translational thermal noise. All assertions concern the unique stationary distribution, and \(Y\) is the transverse coordinate. Define \(\delta=D_r/\kappa>0\), \(\rho=\lambda/\kappa>0\). Standardized transverse excess kurtosis means \(\mathbb EY^4/(\mathbb EY^2)^2-3\), not radial kurtosis.

## Proof

Scale time by \(\kappa^{-1}\) and space by \(v/\kappa\). Write \(y\) for normalized transverse coordinate and \(\theta\) for heading. The stationary generator on smooth test functions is
\[Lf=(-y+\sin\theta)\partial_yf+\delta\partial_{\theta}^2f+\rho[f(0,0)-f(y,\theta)].\]
Stationarity is guaranteed by the exponential-age renewal representation, since all normalized displacements are bounded by one. Let \(Z_{n,k}=\mathbb E[y^n e^{ik\theta}]\), for integers \(n\ge0\), \(k\in\mathbb Z\). Complete resetting gives the exact triangular recursion
\[Z_{0,k}=\frac{\rho}{\rho+\delta k^2},\qquad (n+\rho+\delta k^2)Z_{n,k}=\frac{n}{2i}(Z_{n-1,k+1}-Z_{n-1,k-1}),\quad n\ge1.\]
The symmetry \(\theta\mapsto-\theta\), \(y\mapsto-y\) implies \(\mathbb Ey=0\). Iterating only through total order four yields
\[\mathbb Ey^2=\frac{4\delta}{(4\delta+\rho)(\rho+2)(\delta+\rho+1)},\]
and
\[\mathbb Ey^4=\frac{96\delta^2(144\delta^2+79\delta\rho+124\delta+10\rho^2+25\rho+12)}{(4\delta+\rho)(16\delta+\rho)(\rho+2)(\rho+4)(\delta+\rho+1)(\delta+\rho+3)(4\delta+\rho+2)(9\delta+\rho+1)}.\]
Taking the fourth cumulant and factoring gives
\[\operatorname{cum}_4(Y)=\left(\frac{v}{\kappa}\right)^4\frac{48\delta^2Q_\delta(\rho)}{H_\delta(\rho)}.\]
The exact numerator and denominator are
\[
Q_\delta(\rho)=19\rho^5+(100+228\delta)\rho^4+(179+972\delta+885\delta^2)\rho^3
+(122+1156\delta+2430\delta^2+1252\delta^3)\rho^2
+(24+160\delta+104\delta^2+928\delta^3+576\delta^4)\rho
-(192\delta+2176\delta^2+4032\delta^3).
\]
\[
H_\delta(\rho)=(4\delta+\rho)^2(16\delta+\rho)(\rho+2)^2(\rho+4)
(\delta+\rho+1)^2(\delta+\rho+3)(4\delta+\rho+2)(9\delta+\rho+1).
\]
Every factor of \(H_\delta(\rho)\) is positive for positive parameters. For fixed \(\delta>0\), the constant term of \(Q_\delta\) is strictly negative, while all coefficients of positive powers of \(\rho\) are strictly positive. Thus Descartes' rule of signs gives at most one positive root; the signs at zero and at infinity give existence and establish the strict negative-to-positive sign change. The nonzero variance makes the fourth cumulant and standardized excess-kurtosis signs identical.

For \(\delta\downarrow0\), insert \(\rho=c\delta\) into \(Q_\delta\); the leading term is \(\delta(24c-192)\), yielding \(c=8\). For \(\delta\to\infty\), insert \(\rho=c/\delta\) and divide \(Q_\delta\) by \(\delta^3\); the limit is \(576c-4032\), yielding \(c=7\). Uniqueness and strict sign change justify these asymptotic root limits. The displayed moments give \(\mathbb Ey^4/(\mathbb Ey^2)^2\to60\) as \(\rho\to\infty\), so excess kurtosis tends to \(57\). Finally, restore the factor \(v/\kappa\) in all moments.

## Verification

The accompanying dependency-free `checker.py` independently iterates the exact Fourier moment recursion using rational numbers and compares it with the two closed-form moments and factored cumulant for thirty positive rational parameter pairs. It verifies 94 exact assertions, including the strict coefficient signs responsible for uniqueness. For \(\delta=1\), the critical root is approximately \(0.841109899088457\). The asymptotic, all-parameter, and uniqueness statements follow from the proof, not from numerical checks.

## Relationship to prior work

Shee (2024), arXiv:2409.06920, derives the complete-reset active-Brownian model, the mean-squared displacement, the total radial fourth moment and its radial kurtosis phase diagram. The present result is specifically an exact *transverse Cartesian* fourth cumulant with the strict all-diffusivity, one-reset-rate root theorem and two endpoint scaling laws. The earlier radial fourth moment and mean-squared radius do not determine the anisotropic transverse fourth moment. Closely related published results on a transverse mixed **third** cumulant, stationary second-order transverse covariance reconstruction, and far-tail angular asymptotics concern different observables and do not provide the polynomial sign classification. A generating-function or moment-hierarchy approach is shared, so the distinction is a theorem on the new observable and its universal root, not a claim of a new method.

## Limitations

The conclusion is restricted to athermal planar propulsion, isotropic harmonic relaxation, rotational Brownian diffusion and simultaneous complete Poisson resetting to a fixed orientation. It makes no assertion for nonzero translational thermal noise, partial resets, non-Poisson clocks or nonharmonic confinement. No independent scientific audit has been performed, and unindexed equivalent prior statements may exist. Positive excess kurtosis alone is not an assertion of a globally heavier distribution tail.

## References

- A. Shee, *Active Brownian particle under stochastic position and orientation resetting in a harmonic trap*, arXiv:2409.06920, first posted 11 September 2024, https://arxiv.org/abs/2409.06920.
- Related published mathematical results: *A unique transverse third-cumulant reversal under complete resetting of a trapped active Brownian swimmer*, published-finding corpus, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-unique-transverse-third-cumulant-reversal-under-complete-reset--554b8e1b368c; *Four covariance coefficients identify three relaxation rates in an actively reset harmonic particle*, published-finding corpus, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-four-covariance-coefficients-identify-three-relaxation-rates-in--846dab8f4f22.
