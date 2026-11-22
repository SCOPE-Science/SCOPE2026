# An exponentially hidden negative-correlation signal in weakly biased double-dot transport

## Finding
For a Coulomb-blockaded classical double quantum dot with equal dot-reservoir coupling \(\gamma>0\), fix a reference Fermi occupancy \(0<m<1\), a contrast \(0<\delta<\min(m,1-m)\), and reservoir Fermi functions \(f_L=m+\delta\), \(f_R=m-\delta\). Tune the symmetric interdot hopping to \(g_{\mathrm{eff}}=\gamma m\). For the stationary binary left-dot occupancy \(N_L(t)\), define its lagged connected correlation \(C_\delta(t)=\mathbb E[N_L(0)N_L(t)]-\mathbb E[N_L]^2\).

For every positive contrast, \(C_\delta\) changes sign infinitely often. Its first zero is at \(t_0\), and the maximum negative excursion is \(M_\delta=-\inf_{t\ge0}C_\delta(t)>0\). Both obey the sharp weak-contrast limits
\[
\lim_{\delta\downarrow0}\gamma\delta t_0=\frac\pi2+\arctan m,\qquad
\lim_{\delta\downarrow0}\delta\log M_\delta=-(1+m)\left(\frac\pi2+\arctan m\right).
\]
Thus genuinely oscillatory correlations occur for arbitrarily weak driving, but their first negative signal appears at a lag of order \(1/\delta\) and is smaller than every power of \(\delta\). The stated hopping choice maximizes the damped oscillation frequency over hopping rates for these fixed reservoir occupations.

## Assumptions and scope
The state space is exactly \(\{0,L,R\}\): empty, left occupied, or right occupied. Infinite repulsion excludes double occupation. Injection from reservoir \(j\) has rate \(\gamma f_j\), extraction has rate \(\gamma(1-f_j)\), and hopping \(L\leftrightarrow R\) has rate \(g_{\mathrm{eff}}\). No coherent tunneling, spin degrees of freedom, or hidden states are assumed. Rates and \(m\) stay fixed as \(\delta\downarrow0\); only the Fermi-function contrast vanishes. Natural logarithms are used. This is a time-lagged occupancy covariance, not an equal-time correlation between the two dots and not an electric-current noise spectrum.

For orientation, with arbitrary \(0<a,b<1\) and \(\kappa=g_{\mathrm{eff}}/\gamma>0\), the dimensionless column generator is
\[
Q/\gamma=\begin{pmatrix}
-a-b&1-a&1-b\\
a&-(1-a+\kappa)&\kappa\\
b&\kappa&-(1-b+\kappa)
\end{pmatrix}.
\]
The nonzero eigenvalues are \(-\gamma[1+\kappa\pm\sqrt{(\kappa-a)(\kappa-b)}]\). Their complex-conjugate regime is exactly \(\min(a,b)<\kappa<\max(a,b)\). For fixed \(a=m+\delta\), \(b=m-\delta\), the imaginary-part magnitude \(\gamma\sqrt{\delta^2-(\kappa-m)^2}\) is uniquely maximized at \(\kappa=m\); this motivates the specified tuning rather than an arbitrary parameter slice. The general spectral criterion itself is not proposed as new.

## Proof
Write \(H=(1+m)^2+\delta^2\). Stationarity of the three-state generator gives
\[
p=\mathbb P(N_L=1)=\frac{\delta^2+\delta+m^2+m}{H},\qquad
A=p(1-p)=\frac{(1+m-\delta)(\delta^2+\delta+m^2+m)}{H^2}.
\]
The characteristic polynomial, normalized by \(\gamma\), is \(z[(z+1+\kappa)^2-(\kappa-a)(\kappa-b)]\). At \(a=m+\delta\), \(b=m-\delta\), \(\kappa=m\), the eigenvalues are \(0\) and \(-\gamma(1+m)\pm i\gamma\delta\). The centered stationary autocovariance is therefore the real two-mode combination
\[
C_\delta(t)=e^{-\gamma(1+m)t}\left[A\cos(\gamma\delta t)+B\sin(\gamma\delta t)\right].
\]
Indeed, \(C_\delta(0)=A\) and the Markov generator gives \(C_\delta'(0)=-\gamma(1-m-\delta+m)p=-\gamma(1-\delta)p\). Matching that derivative yields
\[
B=\frac{p[(m+\delta)-(1+m)p]}\delta
=\frac{(\delta^2-\delta+m^2+m)(\delta^2+\delta+m^2+m)}{H^2}.
\]
Both \(A,B\) are strictly positive because \(0<\delta<m\), and
\[
\frac BA=\frac{\delta^2-\delta+m^2+m}{1+m-\delta}\ \longrightarrow\ m.
\]
Let \(R=\sqrt{A^2+B^2}\), \(\phi=\arctan(B/A)\in(0,\pi/2)\), \(\Gamma=\gamma(1+m)\), and \(\omega=\gamma\delta\). Then \(C_\delta(t)=R e^{-\Gamma t}\cos(\omega t-\phi)\). Its first positive zero is exactly
\[
t_0=\frac{\pi/2+\phi}{\omega}.
\]
It has infinitely many further alternating sign intervals. On the first negative interval, the unique local minimum occurs at
\[
t_*=\frac{\pi/2+\phi+\arctan(\omega/\Gamma)}{\omega}.
\]
Subsequent negative minima are separated by \(2\pi/\omega\), and their magnitudes decrease strictly by \(e^{-2\pi\Gamma/\omega}\); thus this first negative minimum is the global one. Direct evaluation gives the exact identity
\[
M_\delta=R\frac{\omega}{\sqrt{\Gamma^2+\omega^2}}
\exp\left[-\frac\Gamma\omega\left(\frac\pi2+\phi+\arctan\frac\omega\Gamma\right)\right].
\]
Now \(A\to m/(1+m)^2>0\), \(B/A\to m\), \(R\to m\sqrt{1+m^2}/(1+m)^2>0\), and \(\delta\log\!\big(R\omega/\sqrt{\Gamma^2+\omega^2}\big)\to0\). Also \(\arctan(\omega/\Gamma)\to0\) and \(\phi\to\arctan m\). Multiplying the logarithm of the exact identity by \(\delta\) establishes the second claimed limit; the zero formula establishes the first. No numerical finite-contrast extrapolation enters this proof.

## Verification
The accompanying `check.py` reconstructs the full generator and stationary law by exact symbolic algebra, verifies the characteristic polynomial and every amplitude identity, evaluates the stationary covariance from matrix exponentials at several parameter choices, and uses arbitrary-precision calculations to test convergence to the proved limit. Run with `python check.py` using SymPy, NumPy, SciPy and mpmath. All assertions passed. Numerical convergence tests corroborate rather than prove the \(\delta\downarrow0\) limit; the proof above is analytical.

## Relationship to prior work
Fiusa et al. [1] introduce the classical four-state double-dot transport generator, its Coulomb-blockade three-state limit, and exact steady-state populations; [1] focuses on excursion and current statistics, not this weak-contrast stationary lag-correlation visibility law. The generic fact that oscillatory correlation signals can distinguish irreversible three-state Markov systems and the general two-mode spectral machinery are established well before [1], including Amann, Schmiedl, and Seifert [2]. Therefore the eigenvalue criterion and damped cosine formula are credited ingredients, not independent novelty claims. The contribution here is the specific, sharply quantified \(\exp(-c(m)/\delta)\) invisibility mechanism at the frequency-maximizing physical hopping choice, with exact first-zero and global-minimum formulas. Chen [3] gives general three-state correlation and noise formulae; only its abstract was available for direct comparison. The possibility that [3] or unexamined literature implicitly subsumes this asymptotic remains a priority risk.

## Limitations
The result is a sharp mathematical limit for a three-state incoherent jump model. It is not a statement about a fully coherent quantum device or experimental measurement precision at finite sampling size. Physical energy and chemical-potential settings must realize the chosen Fermi parameters, and the hopping rate must be tuned as stated. A nonzero bias does not guarantee experimentally resolvable negative correlation. No stronger optimality over all driving and hopping protocols is proved. Independent scientific validation and complete priority assessment have not been performed.

## References
[1] G. Fiusa, P. E. Harunari, A. J. B. Rosal, J. M. Nichol and G. T. Landi, *Stochastic trajectories and excursions in a double quantum dot system*, arXiv:2605.20166v1 (first public release 19 May 2026), https://arxiv.org/html/2605.20166v1 . In particular its model Eq. (4) and Coulomb-blockade stationary populations, Appendix A.

[2] C. P. Amann, T. Schmiedl and U. Seifert, *Can one identify non-equilibrium in a three-state system by analyzing two-state trajectories?*, arXiv:1001.0528 (4 January 2010), https://arxiv.org/html/1001.0528v1 . In particular its generic two-mode three-state relaxation Eq. (9) and its discussion of oscillatory correlations as a known nonequilibrium diagnostic.

[3] Y. Chen, *On the monotonicity of fluctuation spectra for three-state Markov processes*, Fluctuation and Noise Letters 7 (2007) L181–L192, https://doi.org/10.1142/S0219477507003830 . General correlation and spectrum formulas according to the available abstract; complete text not inspected.
