# Two bulk velocity covariances determine both boundary reset rates in a harmonic chain

## Finding

Consider the stationary, thermodynamic-bulk equal-time velocity covariance at integer spatial separation \(d\geq 0\), denoted by \(C_d\), in the boundary-reset harmonic chain specified below. Let \(K=Dk/\gamma\) be known, and define the dimensionless observed pair
\[
s=C_0/K,\qquad t=C_1/K.
\]
**Theorem (sharp two-covariance identifiability and attainable-data region).** The unordered pair of finite positive boundary resetting rates is determined uniquely by \((C_0,C_1)\). More precisely, \((s,t)\) arises from some such pair if and only if
\[
\boxed{s>0,\qquad \sqrt{1+s^2}-1\leq t<\frac{\sqrt{1+4s^2}-1}{2}.}
\]
Both inequalities are sharp. The lower equality holds exactly when the two rates agree. The strict upper boundary is approached when one reset rate tends to infinity with the other adjusted to keep \(s\) fixed; it cannot be attained by two finite rates. For every admissible pair set
\[
c=\operatorname{artanh}\!\left(\frac{s}{1+t}\right),\quad
h=\operatorname{arcosh}\!\left(\sqrt{(1+t)^2-s^2}\right),\quad
\lambda_{\pm}=\tanh\!\left(\frac{c\pm h}{2}\right).
\]
Then \(0<\lambda_-\leq\lambda_+<1\), and the reset rates, unordered, are exactly
\[
\boxed{\left\{\sqrt{\frac{k}{m}}\,\frac{1-\lambda_-}{\sqrt{\lambda_-}},\quad
\sqrt{\frac{k}{m}}\,\frac{1-\lambda_+}{\sqrt{\lambda_+}}\right\}.}
\]
One scalar covariance alone never identifies both rates: for every \(C_0>0\) there is a continuum of different unordered positive pairs with that value. Thus two adjacent equal-time bulk covariances are a **minimal** exact data set in the calibrated equal-diffusivity model.

## Assumptions and scope

There are \(N\) equal-mass particles, with \(m>0\), connected in an open nearest-neighbor harmonic chain of spring stiffness \(k>0\). The interior dynamics are \(m\ddot x_j=-k(2x_j-x_{j-1}-x_{j+1})\). The endpoint equations include identical viscous damping \(-\gamma\dot x_j\), \(\gamma>0\), and spring forces \(kX_1\) and \(kX_N\), respectively, from independent Brownian walls. Both walls diffuse with the same *known* constant \(D>0\), independently reset to zero at their respective finite rates \(r_1,r_N>0\), and have stationary forcing covariance
\[
\mathbb E[kX_i(t)kX_i(t')]=\frac{2Dk^2}{r_i}e^{-r_i|t-t'|}.
\]
The thermal Langevin noise strength is zero; endpoint damping remains positive. Take the stationary distribution first, then \(N\to\infty\) with the observed sites at \(N/2\) and \(N/2+d\) for a fixed nonnegative integer \(d\). The limiting covariance is \(C_d=\lim_{N\to\infty}\operatorname{Cov}(\dot x_{N/2},\dot x_{N/2+d})\), for even \(N\). All thermodynamic-limit and stationarity assumptions are the same as the established Green-function calculation of Sarkar and Roy (2023). This theorem does not assert exact inversion from finite-\(N\) or noisy measurements.

## Proof

**1. Bulk covariance and its decay parameter.** The stationary Green-function expression for the equal-time bulk spatial covariance (obtained by resolving the boundary force spectra) reduces, for every fixed integer \(d\geq0\), to
\[
C_d=\frac{Dk^2}{\pi\gamma}\sum_{i\in\{1,N\}}
\int_0^\pi\frac{\cos(dq)}{mr_i^2+2k-2k\cos q}\,dq.
\]
To evaluate the integral, use the Poisson-kernel identity, valid when \(a>b>0\):
\[
\frac1\pi\int_0^\pi\frac{\cos(dq)}{a-b\cos q}\,dq
=\frac{\rho^d}{\sqrt{a^2-b^2}},\qquad
\rho=\frac{a-\sqrt{a^2-b^2}}{b}\in(0,1).
\]
It follows either by expanding \((1-2\rho\cos q+\rho^2)^{-1}\) as an absolutely convergent Poisson series or by a single-contour residue calculation. Apply it with \(a=mr^2+2k\) and \(b=2k\), and introduce
\[
\lambda(r)=\frac{\sqrt{r^2+4k/m}-r}{\sqrt{r^2+4k/m}+r}\in(0,1).
\]
The exact covariance becomes
\[
C_d=\sum_{i\in\{1,N\}}\frac{Dk^2}{\gamma m r_i\sqrt{r_i^2+4k/m}}\,\lambda(r_i)^d
=K\sum_{i\in\{1,N\}}\frac{\lambda(r_i)^{d+1}}{1-\lambda(r_i)^2}.
\]
The second identity uses the bijective inverse \(r=\sqrt{k/m}(1-\lambda)/\sqrt\lambda\). The coefficients are positive. No Gaussian assumption about the resetting walls has been made: the chain's second moments depend only on their exact two-time force covariance.

**2. Hyperbolic reduction.** There exist unique \(\theta_i>0\) such that \(\lambda(r_i)=\tanh(\theta_i/2)\). Elementary hyperbolic identities yield
\[
\frac{\lambda}{1-\lambda^2}=\frac{\sinh\theta}{2},\qquad
\frac{\lambda^2}{1-\lambda^2}=\frac{\cosh\theta-1}{2}.
\]
Consequently,
\[
s=\frac{\sinh\theta_1+\sinh\theta_N}{2},\qquad
1+t=\frac{\cosh\theta_1+\cosh\theta_N}{2}.
\]
After swapping the two indistinguishable ends if needed, write \(c=(\theta_1+\theta_N)/2>0\) and \(h=(\theta_1-\theta_N)/2\geq0\). Both rates finite and positive precisely when \(c>h\), while
\[
s=\sinh c\cosh h,\qquad1+t=\cosh c\cosh h.
\]
Thus \((1+t)^2-s^2=\cosh^2 h\) and \(s/(1+t)=\tanh c\), proving the proposed inversion whenever its arguments are feasible.

**3. Exact image, sharp endpoints, and uniqueness.** Fix any \(s>0\). Along the constraint \(s=\sinh c\cosh h\), one has \(c=\operatorname{arsinh}(s/\cosh h)\). The condition \(c>h\) is equivalent to
\[
0\leq h<\tfrac12\operatorname{arsinh}(2s).
\]
Moreover \(1+t=\sqrt{s^2+\cosh^2 h}\) is strictly increasing as \(h\) increases from zero. At \(h=0\), \(t=\sqrt{1+s^2}-1\); as \(h\uparrow\tfrac12\operatorname{arsinh}(2s)\), \(t\uparrow(\sqrt{1+4s^2}-1)/2\). Continuity yields every intermediate value, with unique \(h\); the preceding identities then yield the unique \(c\), hence the unique unordered rates. At \(h=0\), the two rates coincide. At the unattained upper endpoint, one \(\theta_i\downarrow0\), so \(\lambda_i\downarrow0\) and \(r_i\to\infty\). All stated strictness and equality claims follow.

**4. Minimality.** With only the given \(s>0\), choose any \(\theta_1\) in the interval \((0,\operatorname{arsinh}(2s))\) and uniquely choose \(\theta_N=\operatorname{arsinh}(2s-\sinh\theta_1)>0\). This continuum includes infinitely many distinct unordered pairs of reset rates, all yielding the same \(C_0=Ks\). The adjacent covariance \(C_1\) is therefore necessary in addition to \(C_0\).

## Verification

The provided standalone \(verify.py\) checks the Fourier-integral evaluation, the hyperbolic image and inversion on 42 distinct positive rate pairs (including equal rates), and the sharp boundary values. With NumPy and SciPy installed it additionally solves a finite-chain stationary Lyapunov equation **independently** and compares bulk covariances for separations \(0,1,2,3,5,8\) in a chain of 50 particles to the infinite-chain formula; discrepancies are below \(10^{-6}\) for the indicated parameters. Exact rational checks of the two-exponential coefficient formula are included. These finite checks corroborate but do not substitute for the analytical proof.

For a concrete numerical example, at \(m=k=\gamma=D=1\), with hidden wall rates \(r_1=1.2\) and \(r_N=3.7\), the two observed bulk covariances are \(C_0=0.42154777774493\ldots\) and \(C_1=0.11864891224676\ldots\). The formula recovers the unordered pair \(\{1.2,3.7\}\). At \(s=0.42154777774493\ldots\), the exact admissible interval for \(t\) begins at \(0.08522003709924\ldots\) and ends strictly before \(0.15398970092937\ldots\).

## Relationship to prior work

Sarkar and Roy (2023) derived the stationary wall-force covariance, the harmonic-chain Green-function representation, and the bulk spatial velocity correlations, expressed using Fourier integrals and a regularized hypergeometric function; these foundational results are credited and are **not** claimed as new. The new result solves the physically constrained *inverse* question: the sharp two-observation image, an explicit unique inversion, the coincident-rate boundary, and proof of two-measurement minimality. The classical Prony method recovers general finite exponential sums from multiple samples but does not by itself give this special two-sample image or inversion: here the modal amplitudes and decay factors are tied together by a shared known wall diffusivity. Sarkar, Santra and Basu (2024) derived two spatial-correlation lengths for *active Rubin baths*, with a different reservoir model and noise kernel; this does not supply the claimed boundary-reset inverse theorem.

## Limitations

The output is an **unordered** rate pair: interior bulk stationary equal-time correlations are reflection-symmetric and cannot label which wall has which rate. The common diffusion constant, mass, spring stiffness and endpoint damping are assumed known and both reset rates strictly positive and finite. The inequalities are noiseless consistency tests for the thermodynamic limit, not tolerance bands for finite-data inference. Near the equal-rate and infinite-rate edges, inversion may be poorly conditioned; no stability guarantee or estimator confidence interval is asserted. The assertion does not extend to unequal unknown wall diffusivities, anharmonic or disordered chains, thermal boundary noise, or finite-size covariances. Independent scientific audit has not been performed.

## References

1. R. Sarkar and P. Roy, *Stationary state of harmonic chains driven by boundary resetting*, arXiv:2307.06127, first public version 12 July 2023; full revised text arXiv:2307.06127v3, Sections 2, 4.2 and Appendix B.2. https://arxiv.org/abs/2307.06127 ; https://arxiv.org/html/2307.06127v3
2. R. Sarkar, I. Santra and U. Basu, *Stationary states of activity-driven harmonic chains*, arXiv:2210.09035 (2022). https://arxiv.org/abs/2210.09035
3. R. Sarkar, I. Santra and U. Basu, *Harmonic chain driven by active Rubin bath: transport properties and steady-state correlations*, arXiv:2404.00615 (2024), especially Section III.2.1. https://arxiv.org/abs/2404.00615
4. G. Plonka, *Prony methods for recovery of structured functions*, GAMM-Mitteilungen 37 (2014), 239–258. https://doi.org/10.1002/gamm.201410011
