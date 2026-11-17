# Exact singular-funnel action for an adaptive pitchfork

## Finding
Consider the adaptive pitchfork differential equation with a slow parameter, as specified below. The left branch of the stable manifold of its positive saddle intersects every horizontal section \(\mu=\mu_0\), \(\mu_0>r^2\), at exactly one positive coordinate \(x_\varepsilon(\mu_0)\). The exact exponentially small section threshold is
\[
\lim_{\varepsilon\downarrow0}-\varepsilon\log x_\varepsilon(\mu_0)
=\mathcal A(\mu_0)
=\mu_0-r^2-b\log\!\left(\frac{\mu_0+b}{r^2+b}\right)>0.
\]
For all fixed \(r^2<\mu_1<\mu_2\), the relative funnel attenuation obeys
\[
\lim_{\varepsilon\downarrow0}\varepsilon\log\frac{x_\varepsilon(\mu_2)}{x_\varepsilon(\mu_1)}
=-(\mu_2-\mu_1)+b\log\!\left(\frac{\mu_2+b}{\mu_1+b}\right).
\]
The second rate is independent of the feedback coefficient \(a\) whenever both sections are above the saddle for the parameters being compared. This is a fixed-section, small-\(\varepsilon\) limit; it is not the fixed-\(\varepsilon\), large-height limit.

## Assumptions and scope
Let \(a,b\) be real constants satisfying \(b>0\) and \(a>2\sqrt b\). For any \(\varepsilon>0\), consider the smooth planar system on \(x\ge0\):
\[
\dot x=x(\mu-x^2),\qquad
\dot\mu=\varepsilon(-\mu+ax-b).
\]
Set \(r=(a-\sqrt{a^2-4b})/2\), so \(r>0\), \(r^2+b=ar\) and \(a>2r\). Its equilibrium \(e_-=(r,r^2)\) is a hyperbolic saddle; the other two equilibria are \((0,-b)\) and \((r_+,r_+^2)\) with \(r_+=(a+\sqrt{a^2-4b})/2\). For each \(\varepsilon>0\) and each fixed \(\mu_0>r^2\), define \(x_\varepsilon(\mu_0)\) as the \(x\)-coordinate of the unique intersection of the left stable-manifold branch of \(e_-\) with \(\mu=\mu_0\). Existence, positivity and uniqueness for every such section are proved below. The fixed-parameter limit takes \(\varepsilon\downarrow0\) with \(a,b,\mu_0\) held fixed.

## Proof
**1. The saddle and invariant backward branch.** At \(e_-\) the Jacobian in \((x,\mu)\) coordinates is
\[
J_\varepsilon=\begin{pmatrix}-2r^2&r\\\varepsilon a&-\varepsilon\end{pmatrix},
\qquad\det J_\varepsilon=\varepsilon r(2r-a)<0.
\]
For its negative eigenvalue \(\lambda_s<0\), the stable eigenvector has \(d\mu/dx=\varepsilon a/(\lambda_s+\varepsilon)<0\). The branch leaving the saddle backward toward smaller \(x\) therefore enters \(0<x<r\), \(\mu>r^2\). This region is backward invariant: throughout it \(\dot x=x(\mu-x^2)>0\), whereas \(\dot\mu=-\varepsilon(\mu+b-ax)<0\), since \(\mu+b>r^2+b=ar>ax\). Moving backward, \(x\) strictly decreases and \(\mu\) strictly increases. No backward finite-time blowup is possible because \(x\in[0,r]\) and \(|\dot\mu|\le\varepsilon(\mu+b+ar)\). The backward orbit cannot have a finite limiting \(\mu\): a finite limit forces \(x\to0\) and then \(\dot\mu\to-\varepsilon(\mu+b)<0\), contradicting bounded backward approach to a stationary limit. Thus \(\mu\to+\infty\) backward, and every section \(\mu>r^2\) is crossed exactly once at a strictly positive \(x\). The branch is globally a decreasing graph \(x=x_\varepsilon(\mu)\).

**2. Uniform control from a fixed interior point.** Parametrize this branch alternatively by \(\mu=\mu_\varepsilon(x)\) for \(0<x<r\). Using \(r^2+b=ar\),
\[
-\frac{d\mu_\varepsilon}{dx}=
\frac{\varepsilon}{x}
\frac{(\mu_\varepsilon-r^2)+a(r-x)}
{(\mu_\varepsilon-r^2)+(r-x)(r+x)}.
\]
Because \(\mu_\varepsilon\ge r^2\) and \(a>2r\ge r+x\), the last fraction is positive and at most \(a/(r+x)\le a/r\). Integrating from \(x=r\) to each fixed \(0<\eta<r\) gives
\[
0\le\mu_\varepsilon(\eta)-r^2
\le\frac{a\varepsilon}{r}\log\frac r\eta.
\]
In particular, \(\mu_\varepsilon(\eta)\to r^2\) for fixed \(\eta\) as \(\varepsilon\downarrow0\).

**3. An exact logarithmic integral and its limit.** For fixed \(\mu_0>r^2\) and sufficiently small \(\varepsilon\), the preceding estimate ensures \(\mu_\varepsilon(\eta)<\mu_0\). In the interval \(\mu\in[\mu_\varepsilon(\eta),\mu_0]\), the decreasing graph has \(0<x_\varepsilon(\mu)\le\eta\), and direct division of the differential equations gives
\[
-\varepsilon\log x_\varepsilon(\mu_0)
=-\varepsilon\log\eta
+\int_{\mu_\varepsilon(\eta)}^{\mu_0}
\frac{\mu-x_\varepsilon(\mu)^2}{\mu+b-a x_\varepsilon(\mu)}\,d\mu.
\]
Here the denominator is at least \(a(r-\eta)>0\). On the compact \(\mu\)-interval \([r^2,\mu_0]\), the integrand converges to \(\mu/(\mu+b)\) uniformly as \(\eta\downarrow0\), with a bound independent of \(\varepsilon\) whenever \(0<x\le\eta<r/2\). First let \(\varepsilon\downarrow0\) with \(\eta\) fixed. The lower limit tends to \(r^2\), the additive term \(-\varepsilon\log\eta\) tends to zero, and the remaining difference from the integral of \(\mu/(\mu+b)\) is bounded in magnitude by a constant times \(\eta\). Next let \(\eta\downarrow0\). Both liminf and limsup of the left side therefore equal
\[
\int_{r^2}^{\mu_0}\frac{\mu}{\mu+b}\,d\mu
=\mu_0-r^2-b\log\!\left(\frac{\mu_0+b}{r^2+b}\right).
\]
The integral is strictly positive. Subtracting this limit at two distinct fixed sections proves the relative-attenuation statement. Because the derivative \(\mathcal A'(\mu)=\mu/(\mu+b)\) contains no \(a\), the section-to-section rate has the asserted independence. All limits quantify fixed sections, not moving sections or unspecified pre-exponential factors. \(\square\)

## Verification
The standalone script `verification/check_funnel.py` evaluates the exact stable eigenvector, integrates the left stable-separatrix equation in logarithmic \(x\) coordinates, and compares values of \(-\varepsilon\log x_\varepsilon(\mu)\) against the closed-form action at two sections and three positive \(\varepsilon\) values. Run from the package root with `python verification/check_funnel.py` (requires NumPy and SciPy). These finite numerical checks illustrate the formula; the proof above independently establishes the limit for every allowed real parameter and fixed section. For \(a=3\), \(b=2\), one has \(r=1\), \(\mathcal A(2)=1-2\log(4/3)\approx0.4246358551\), and \(\mathcal A(5)=4-2\log(7/3)\approx2.3054042792\).

## Relationship to prior work
Yanchuk, Wieczorek, Jardón-Kojakhmetov and Alkhayuon construct the adaptive pitchfork, identify the separating stable manifold and describe exponentially narrow singular funnels at small timescale ratios; their main text and supplementary section II do not give the closed fixed-section small-\(\varepsilon\) action above or the feedback-independent relative rate. Their supplementary analysis of a distinct adaptive phase rotator derives exponential scaling with another integral. General slow-fast entry–exit analysis, including work of Kaklamanos, Kuehn, Popović and Sensi, studies related asymptotic mechanisms but does not state the present pitchfork section formula. The present calculation is a quantitative specialization to the established geometric separatrix, not a new discovery of the singular funnel itself.

## Limitations
The result concerns one planar adaptive pitchfork, its left saddle stable branch and sections strictly above the saddle with \(a,b\) fixed. It does not give a sharp multiplicative prefactor, uniformity for section heights depending on \(\varepsilon\), or corresponding formulas for other fast–slow systems. The exponential rate is model-specific; its possible derivation from more general published asymptotic theory is a historical-priority risk. The basin-boundary interpretation uses the phase portrait established by the motivating work, while the existence and action of the section curve are proved directly here. Independent mathematical validation has not been performed.

## References
1. S. Yanchuk, S. Wieczorek, H. Jardón-Kojakhmetov and H. Alkhayuon, *Singular basins in multiscale systems*, arXiv:2601.02001v1 (January 5, 2026), https://arxiv.org/html/2601.02001v1; including supplementary section II.
2. P. Kaklamanos, C. Kuehn, N. Popović and M. Sensi, *Entry–Exit Functions in Fast–Slow Systems with Intersecting Eigenvalues*, arXiv:2208.11559 (2022), https://arxiv.org/abs/2208.11559; Journal of Dynamics and Differential Equations 37 (2025), 559–576.
