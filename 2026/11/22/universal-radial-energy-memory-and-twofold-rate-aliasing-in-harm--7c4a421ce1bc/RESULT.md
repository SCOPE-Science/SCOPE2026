# Universal radial-energy memory and twofold rate aliasing in harmonic active transport

## Finding
Consider a stationary, constant-speed active particle in an isotropic harmonic trap, whose heading is independently refreshed at Poisson times from any centered probability distribution on the unit sphere. Let the trap relaxation rate be \(\mu>0\), the heading-redraw rate be \(\gamma>0\), the propulsion speed be \(v>0\), and the spatial dimension be an integer \(d\ge2\). For its squared radius \(U_t=\|\mathbf r_t\|^2\), write \(\Sigma=\mathbb E[\mathbf n\mathbf n^\top]\) for the redraw covariance and \(s=\operatorname{tr}(\Sigma^2)\). In the stationary state,
\[
\mathbb E U_t=\frac{v^2}{\mu(\mu+\gamma)},\qquad
\operatorname{Var}(U_t)=\frac{2v^4\gamma[\mu+s(\mu+\gamma)]}{\mu^2(\mu+\gamma)^2(\gamma+2\mu)(\gamma+3\mu)}.
\]
For every lag \(t\ge0\), the **complete normalized radial-energy autocovariance**, \(K(t)=\operatorname{Cov}(U_0,U_t)/\operatorname{Var}(U_0)\), is exactly
\[
\boxed{K(t)=\begin{cases}
\displaystyle\frac{(\mu+\gamma)e^{-2\mu t}-2\mu e^{-(\mu+\gamma)t}}{\gamma-\mu},&\gamma\ne\mu,\\[7pt]
(1+2\mu t)e^{-2\mu t},&\gamma=\mu.
\end{cases}}
\]
Thus neither the dimension nor any higher angular feature, nor even the anisotropy statistic \(s\), changes the **shape** of radial-energy relaxation. The stationary variance, by contrast, increases strictly with \(s\). At fixed \(\mu,\gamma,v,d\), its attainable interval has the displayed formula evaluated at \(s=1/d\) and \(s=1\) as its sharp endpoints; isotropic redraws attain the lower endpoint and antipodal one-axis redraws attain the upper.

There is an exact inverse-observation obstruction. Define the positive-rate transformation
\[
\boxed{(\mu,\gamma)\longmapsto(\mu',\gamma')
=\left(\frac{\mu+\gamma}{2},\frac{3\mu-\gamma}{2}\right).}
\]
When \(0<\gamma<3\mu\), both parameter pairs have identical \(\mathbb E U\) **and** identical \(K(t)\) at every lag, for the same calibrated \(v\) and the same redraw law. They are different exactly when \(\gamma\ne\mu\). Conversely, these are the **only** positive parameter pairs sharing \(K\): a nontrivial second pair exists exactly for \(0<\gamma<3\mu\) and \(\gamma\ne\mu\); at \(\gamma=\mu\) there is one double-rate solution; for \(\gamma\ge3\mu\) the positive solution is unique. Furthermore, **one stationary variance measurement resolves every nontrivial pair**, since
\[
\boxed{\begin{aligned}
&\operatorname{Var}_{\mu,\gamma}(U)-\operatorname{Var}_{\mu',\gamma'}(U)\\
&\quad=\frac{v^4(\gamma-\mu)
[\gamma^2+3\gamma\mu+6\mu^2+s(2\gamma^2+18\gamma\mu+24\mu^2)]}
{\mu^2(\gamma+\mu)^2(\gamma+2\mu)(\gamma+3\mu)(\gamma+5\mu)}.
\end{aligned}}
\]
Every factor other than \(\gamma-\mu\) is strictly positive. For instance, in dimension two with isotropic heading refresh and \(v=1\), the distinct pairs \((\mu,\gamma)=(1,2)\) and \((3/2,1/2)\) both give \(\mathbb E U=1/3\) and \(K(t)=3e^{-2t}-2e^{-3t}\), but their variances are, respectively, \(1/18\) and \(1/63\).

## Assumptions and scope
Let \(d\ge2\) be an integer. Fix \(v,\mu,\gamma>0\). The propulsion heading \(\mathbf n_t\in S^{d-1}\) is piecewise constant and independently resampled at every event of a rate-\(\gamma\) Poisson process from a fixed probability law \(\nu\) on \(S^{d-1}\), with \(\mathbb E_\nu\mathbf n=0\). The law need not be rotation invariant or have a density. The position evolves continuously between tumbles by
\[
\frac{d\mathbf r_t}{dt}=-\mu\mathbf r_t+v\mathbf n_t.
\]
The stationary solution is the almost surely convergent exponentially weighted integral of past headings; hence \(\|\mathbf r_t\|\le v/\mu\). The heading redraws are independent of the current position and all past headings. There is no thermal Brownian forcing, velocity magnitude randomness, finite tumbling duration, correlated redraw or asymmetric trapping stiffness. In inverse comparisons, the same known speed \(v\), the same centered law \(\nu\), and the same physical time units are held fixed, while \(\mu\) and \(\gamma\) vary.

Because \(\Sigma\) is positive semidefinite with trace one, \(1/d\le s\le1\). Equality at the lower bound is equivalent to \(\Sigma=I/d\); equality at the upper bound is equivalent to one-dimensional support, which centering and constant speed force to be antipodal with equal probabilities. Every intermediate value is attained by a mixture of a uniform-sphere law and an antipodal one-axis law. The result describes the positive-time stationary **connected covariance of the squared radius**, rather than the position-coordinate covariance or a finite-time conditional energy distribution.

## Proof
**1. Stationary generator moments.** Rescale position and time by \(\mathbf X=(\mu/v)\mathbf r\), \(\tau=\mu t\), and set \(\alpha=\gamma/\mu>0\). Between redraws, \(\dot{\mathbf X}=-\mathbf X+\mathbf n\). Define bounded polynomials \(R=\|\mathbf X\|^2\), \(H=\mathbf X\cdot\mathbf n\), \(Q=\mathbf X^\top\Sigma\mathbf X\), and \(M=\mathbf X^\top\Sigma\mathbf n\). The stationary generator satisfies
\[
\mathcal LR=-2R+2H,\quad \mathcal LH=-(1+\alpha)H+1,\quad
\mathcal LQ=-2Q+2M,\quad \mathcal LM=-(1+\alpha)M+\mathbf n^\top\Sigma\mathbf n.
\]
The last identity uses the centered redraw law, while \(\mathbb E_\nu(\mathbf n^\top\Sigma\mathbf n)=\operatorname{tr}\Sigma^2=s\). Therefore stationarity yields
\[
\mathbb E R=\mathbb EH=\frac1{1+\alpha},\qquad \mathbb EQ=\mathbb EM=\frac{s}{1+\alpha}.
\]
In addition,
\[
\mathcal LH^2=-(2+\alpha)H^2+2H+\alpha Q,\quad
\mathcal L(RH)=-(3+\alpha)RH+R+2H^2,\quad
\mathcal LR^2=-4R^2+4RH.
\]
Solving the corresponding three stationary linear equations in order gives
\[
\mathbb EH^2=\frac{2+\alpha s}{(1+\alpha)(2+\alpha)},\quad
\mathbb E(RH)=\mathbb ER^2=\frac{6+\alpha+2\alpha s}{(1+\alpha)(2+\alpha)(3+\alpha)}.
\]
Consequently,
\[
\operatorname{Var}(R)=\frac{2\alpha[1+(1+\alpha)s]}{(1+\alpha)^2(2+\alpha)(3+\alpha)}>0.
\]
Restoring units proves the stated mean and variance for \(U=(v/\mu)^2R\). These identities use only \(\|\mathbf n\|=1\), centered full redraw, and \(\Sigma\), not angular isotropy or higher angular moments.

**2. Two-time covariance.** Let \(C(\tau)=\operatorname{Cov}(R_0,R_\tau)\) and \(J(\tau)=\operatorname{Cov}(R_0,H_\tau)\) in stationary normalized time. The same generator identities and the Markov property give, for every \(\tau\ge0\),
\[
C'(\tau)=-2C(\tau)+2J(\tau),\qquad J'(\tau)=-(1+\alpha)J(\tau).
\]
The equal-time identities above give \(C(0)=J(0)=\operatorname{Var}(R)\). Hence
\[
J(\tau)=\operatorname{Var}(R)e^{-(1+\alpha)\tau}
\]
and variation of constants gives
\[
\frac{C(\tau)}{C(0)}=
\begin{cases}
\displaystyle\frac{(1+\alpha)e^{-2\tau}-2e^{-(1+\alpha)\tau}}{\alpha-1},&\alpha\ne1,\\[6pt]
(1+2\tau)e^{-2\tau},&\alpha=1.
\end{cases}
\]
The resonant expression is its continuous limit. Undoing the time rescaling proves \(K\). Its two-sided Fourier transform also has the positive factorization
\[
\int_{-\infty}^{\infty}e^{-i\omega t}K(|t|)\,dt
=\frac{2ab(a+b)}{(a^2+\omega^2)(b^2+\omega^2)},
\qquad a=2\mu,\quad b=\mu+\gamma.
\]

**3. All positive inverse fibers.** Taylor expansion of the exact covariance at zero gives
\[
K(0)=1,\quad K'(0+)=0,\quad K''(0+)=-ab,
\quad K'''(0+)=ab(a+b).
\]
Thus the observed full \(K\) uniquely determines \(ab\) and \(a+b\), and hence the unordered positive pair \(\{a,b\}\). Conversely \(K\) is symmetric in those two roots. The first assignment \(a=2\mu\), \(b=\mu+\gamma\) gives the original rates; interchanging them gives \(\mu'=b/2=(\mu+\gamma)/2\) and \(\gamma'=a-b/2=(3\mu-\gamma)/2\). The second assignment has positive \(\gamma'\) exactly when \(\gamma<3\mu\), and coincides with the first exactly when \(\gamma=\mu\). There can be no third positive assignment. Since \(\mathbb E U=2v^2/(ab)\), the stationary mean is also unchanged; it supplies no further separation. The double-root case \(\gamma=\mu\) is covered without division by zero.

**4. Strict variance distinction and angular endpoints.** Substitute \((\mu',\gamma')\) into the rational variance in part 1 and reduce to a common denominator. Direct factorization yields the stated difference, whose sign is exactly the sign of \(\gamma-\mu\), for every \(s\ge1/d\). Hence variance strictly separates every pair with distinct positive rate assignments. The variance coefficient of \(s\) is strictly positive for every \(\alpha>0\); its endpoint values follow from the spectral trace bounds. A centered mixture \(\nu_w=(1-w)\,\mathrm{Unif}(S^{d-1})+\frac w2(\delta_{\mathbf e_1}+\delta_{-\mathbf e_1})\) has \(\Sigma=(1-w)I/d+w\mathbf e_1\mathbf e_1^\top\) and \(s=1/d+(1-1/d)w^2\) for \(0\le w\le1\), proving every intermediate variance is attainable without changing \(K\).

## Verification
The supplied standard-library `checker.py` independently solves the complete stationary polynomial moment-generator recursion through degree four for two-dimensional four-direction and antipodal redraw laws at multiple exact rational rates and anisotropies. This independently reconstructs \(\mathbb E R\), \(\mathbb E R^2\) and the displayed stationary variance. It separately evaluates the transformed inverse rates, equality of unordered relaxation exponents, and strict stationary-variance separation using rational arithmetic; it checks the resonant and nonresonant temporal kernels numerically. Executing `python3 checker.py` produced `PASS: 319 exact-rational and analytic-kernel checks plus 1 seeded path check`. The latter used 40,000 independently generated stationary trajectories with exact exponential holding intervals: at lag \(0.7\), the normalized empirical correlation was \(0.489660005\) versus exact \(0.494878035\). The continuum quantifiers, uniqueness and arbitrary-sphere-law statement rely on the generator proof, **not** on finite tests. The package requires Python 3 only.

## Relationship to prior work
Guéneau, Majumdar and Schehr, *Exact Stationary State of a \(d\)-dimensional Run-and-Tumble Particle in a Harmonic Potential* (first public February 9, 2026; arXiv:2602.08436), establish the stationary isotropic model, stick-breaking representation, arbitrary scalar velocity projection and stationary moment machinery. Their stationary second and fourth moments are prior results and imply the \(s=1/d\) equal-time specialization here; the claim of this note is instead the arbitrary-centered-heading **all-lag normalized radial-energy law**, complete inverse-fiber obstruction, variance resolution and sharp angular-envelope formulation. Their inspected full preprint treats stationary laws and does not state those time-lag/inverse conclusions.

Garcia-Millan and Pruessner, *Run-and-tumble motion in a harmonic potential: field theory and entropy production* (arXiv:2012.02900, first public December 4, 2020), calculate one-dimensional **position** two-time correlations. A position covariance is a distinct, second-order observable and does not determine the four-position connected observable \(\operatorname{Cov}(\|\mathbf r_0\|^2,\|\mathbf r_t\|^2)\) for non-Gaussian propulsion. Sun, Ye and Podgornik, *Exact moments for a run-and-tumble particle with a finite tumble time in a harmonic trap* (arXiv:2409.00578, first public September 2024), provide higher-moment machinery with nonzero tumble durations; their inspected full v1 preprint develops a recursion for single-time moments and time-Laplace transformed transient moments, but does not state this stationary two-time radial-energy inverse classification. Existing results on anisotropic **trap** cross-coordinate squared moments concern a different perturbation than a fixed isotropic trap with anisotropic iid redraws. General Markov-generator and spectral tools are classical, and the theorem does not claim those tools as new. Relevant adjacent results remain potential sources of stronger implicit coverage; no exhaustive novelty certification is claimed.

## Limitations
The universal two-time formula assumes a full *independent* heading redraw from a centered constant-speed sphere law, and exactly linear isotropic deterministic trapping. Persistent-angle turning, noncentered heading laws, speed fluctuations, finite tumbling durations, independent translational diffusion and nonharmonic traps are outside the theorem. Its covariance shape concerns the **squared radius**, not an arbitrary Cartesian quadratic form. The inverse-twin statement assumes common known propulsion speed, unchanged angular law, calibrated time, and perfect stationary observations. It does not assert that finite noisy data can recover third right derivatives stably or distinguish nearly coincident rate pairs. The angular variance envelope uses a different redraw law at its endpoints; its equality of normalized \(K\) does not imply identical full position laws. Originality rests on the inspected sources and accessible index; missing or unindexed literature could contain equivalent results. Independent external scientific review has not been conducted.

## References
1. M. Guéneau, S. N. Majumdar and G. Schehr, *Exact Stationary State of a \(d\)-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436v1, first public 2026-02-09, https://arxiv.org/html/2602.08436v1 .
2. R. Garcia-Millan and G. Pruessner, *Run-and-tumble motion in a harmonic potential: field theory and entropy production*, arXiv:2012.02900, 2020, https://arxiv.org/abs/2012.02900 .
3. A. Sun, F. Ye and R. Podgornik, *Exact moments for a run-and-tumble particle with a finite tumble time in a harmonic trap*, arXiv:2409.00578, 2024, https://arxiv.org/abs/2409.00578 .
