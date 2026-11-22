# A grazing-angle fingerprint in thin-slit run-and-tumble pressure

## Finding

For a zero-temperature run-and-tumble swimmer with uniformly renewed headings and sticky hard walls, the dimensionless stationary force on one wall has an orientation-independent linear response and a sharply classifiable next-order response. Set \(s=L/(v_0\tau)\), \(P(s)=\mu F(L)/v_0\), and let \(p(u)=p(-u)\) be the normalized, nonnegative density of the wall-normal component \(U\in(-1,1)\), with no atom at zero. Write \(m_+=\int_0^1 up(u)\,du\). Then for all \(s>0\),

\[
P(s)=m_+-\frac{s}{4}+\frac12\int_0^s(s-t)g(t)\,dt+\mathcal E(s),\qquad
 g(t)=\int_0^1\frac{p(u)}{u}e^{-t/u}\,du,
\]
\[
|\mathcal E(s)|\le H(s)\int_0^s H(t)\,dt,\qquad H(t)=\int_0^t g(a)\,da.
\]

In particular \(P'(0+)=-1/4\), independent of the heading law. The next-order behavior has three distinct classes:

* If \(p(u)\sim c u^\alpha\) as \(u\downarrow0\), with \(-1<\alpha<0\) and \(c>0\), then
\[
P(s)=m_+-\frac{s}{4}+\frac{c\Gamma(-\alpha)}{2(1+\alpha)(2+\alpha)}s^{2+\alpha}+o(s^{2+\alpha}).
\]
* If \(p(0)=c>0\), and \(\int_0^1|p(u)-c|/u\,du<\infty\), then, with Euler's constant \(\gamma\) and \(I=\int_0^1(p(u)-c)/u\,du\),
\[
P(s)=m_+-\frac{s}{4}+\frac{s^2}{4}\{c\log(1/s)+c(3/2-\gamma)+I\}+o(s^2).
\]
  Consequently, the coefficient of \(s^2\log(1/s)\) equals precisely \(p(0)/4\), identifying the grazing-angle density from mechanical pressure.
* If \(J=\int_0^1 p(u)/u\,du<\infty\), then
\[
P(s)=m_+-\frac{s}{4}+\frac{J}{4}s^2+o(s^2).
\]

For isotropic reorientation on the unit sphere in dimensions \(d=2\) and \(d=3\), these formulas reduce to
\[
P_2(s)=\frac1\pi-\frac s4+\frac{s^2}{4\pi}\bigl[\log(1/s)+3/2-\gamma+\log2\bigr]+o(s^2),
\]
\[
P_3(s)=\frac14-\frac s4+\frac{s^2}{8}\bigl[\log(1/s)+3/2-\gamma\bigr]+o(s^2).
\]
For the two-heading one-dimensional model, \(P_1(s)=1/(2+s)\) exactly, recovering a regular quadratic term \(s^2/8\). These are statements about mean force *per swimmer*, not pressure at fixed volume density.

## Assumptions and scope

A particle moves normal to two impermeable planar walls at positions \(0,L\), with intrinsic speed \(v_0>0\) and deterministic normal velocity \(v_0U\) between reorientations. Reorientations occur at independent Poisson times of rate \(1/\tau>0\), and draw a fresh independent symmetric orientation with density \(p\). At a wall its normal displacement is blocked while it pushes inward until a subsequent reorientation permits departure. The force on a blocked right wall is \(v_0 U_+/\mu\), where \(\mu>0\) is the mobility. No translational Brownian diffusion, torques, interactions or wall-specific change of the reorientation law are present. The two-heading model is the evident symmetric measure-valued extension with \(U\in\{-1,1\}\). If \(p\) vanishes or diverges near zero in another way, the exact integral and error bound still apply but none of the three asymptotic templates need apply.

## Proof

**1. Embedded renewal chain.** Use length unit \(v_0\tau\) and time unit \(\tau\); let \(E_n\) be iid unit exponential run durations. Immediately after each tumble, the normal position follows
\[
X_{n+1}=\min\{s,\max\{0,X_n+U_n E_n\}\}.
\]
The increment law is symmetric with strictly positive density for any fixed displacement if the orientation law assigns positive mass to positive speeds. The induced Markov chain on \([0,s]\) has a strictly positive transition density into any nonempty interior subinterval and therefore admits a unique stationary probability \(\nu_s\), invariant under \(x\mapsto s-x\). This stationary law is also the position law observed at a Poisson reorientation time, by independence of the tumble clock.

Set, for \(t\ge0\),
\[
Q(t)=\int_0^1p(u)e^{-t/u}\,du,\qquad H(t)=\frac12-Q(t).
\]
The probability that one run, initiated at \(x\), ends at the right wall is \(Q(s-x)\), hence its stationary boundary atom is \(a_s=\int Q(s-x)\,\nu_s(dx)\). Reflection gives the same atom on the left. The stationary interior mass is \(1-2a_s=2\int H(s-x)\,\nu_s(dx)\le2H(s)\). Write \(C_s(x)=\nu_s([0,x])\) for \(0<x<s\). By symmetry, \(\int_0^s C_s(x)\,dx=s/2\); because both boundary atoms are \(a_s\),
\[
\sup_{0<x<s}|C_s(x)-1/2|\le(1-2a_s)/2\le H(s).
\]

**2. Exact mechanical reward.** Given an initial position \(x\) and an outward normal speed \(u>0\), the stationary right-wall impulse in one exponentially terminated run, in the dimensionless units, is \(u(E-(s-x)/u)_+\). Its conditional expectation is \(u e^{-(s-x)/u}\). The renewal-reward theorem and unit mean run time yield
\[
P(s)=\int_{[0,s]}W(s-x)\,\nu_s(dx),\qquad
W(t)=\int_0^1u p(u)e^{-t/u}\,du.
\]
Since \(W'(t)=-Q(t)\), elementary Stieltjes integration gives
\[
P(s)=m_+-\frac{s}{4}+\int_0^s C_s(x)H(s-x)\,dx.
\]
Replacing \(C_s\) by \(1/2\) and using its uniform deviation bound proves the exact identity and quantified error. Also \(H(0)=0\), \(H'=g\) for positive arguments, hence \(\frac12\int_0^sH(t)\,dt=\frac12\int_0^s(s-t)g(t)\,dt\).

**3. Grazing-angle asymptotics.** For \(-1<\alpha<0\) and \(p(u)\sim cu^\alpha\), substitute \(z=t/u\) in \(g\) to obtain \(g(t)\sim c\Gamma(-\alpha)t^\alpha\); integrate twice. Since \(H(s)=O(s^{1+\alpha})\), the remainder is \(O(s^{3+2\alpha})=o(s^{2+\alpha})\). If \(p(0)=c\) with integrable \((p-c)/u\), decompose
\[
g(t)=cE_1(t)+\int_0^1\frac{p(u)-c}{u}e^{-t/u}\,du
=c\log(1/t)-c\gamma+I+o(1).
\]
The remainder is \(O(s^3\log^2(1/s))=o(s^2)\); integrating \(\int_0^s(s-t)\log(1/t)dt=(s^2/2)\log(1/s)+3s^2/4\) gives the asserted coefficient. If \(J<\infty\), dominated convergence gives \(g(t)\to J\), with remainder \(O(s^3)\). All asymptotic statements are at fixed heading law as \(s\downarrow0\).

**4. Uniformly distributed sphere headings.** The normal marginal in dimension \(d\ge2\) is \(p_d(u)=c_d(1-u^2)^{(d-3)/2}\), with \(c_d=\Gamma(d/2)/(\sqrt\pi\Gamma((d-1)/2))\). Integration gives \(m_+=c_d/(d-1)\) and \(I_d=-c_d[\psi((d-1)/2)+\gamma]/2\). Substitute for \(d=2,3\). For the two-heading case, the stationary two boundary atoms are \(1/(2+s)\), yielding \(P_1(s)=1/(2+s)\).

## Verification

Run `python checker.py` with NumPy and SciPy. Its 98 deterministic assertions independently evaluate the exact run-displacement kernel, solve a cell-integrated Fredholm equation for the stationary splitting probability in dimensions one through three, compare the mechanical wall impulse with the splitting formula, verify mirror symmetry and positivity, reproduce the exact one-dimensional pressure and verify the displayed two-dimensional and three-dimensional asymptotic accuracy at shrinking widths. The analytical renewal representation and estimates, not these finite computations, establish the continuum and asymptotic claims.

## Relationship to prior work

Frydel (2024), arXiv:2410.06393, establishes the jump/splitting-probability formulation, the stationary wall-force integral (Eq. 48), dimension-dependent jump kernels, and adsorption expansions; these are prior results, not claimed as new here. Its §VIII compares force curves numerically and does not state the three-class pressure-correction theorem or the recovery of \(p(0)\) from the logarithmic coefficient. Ezhilan, Alonso-Matilla and Saintillan (2015), arXiv:1507.06379, derive the narrow-gap *leading* pressure and near-wall grazing-orientation singularities by kinetic theory, without the stated second-order logarithmic or fractional pressure response. This finding concerns the explicit leading correction beyond linear order for general renewal heading densities, and a bound on the approximation error. Prior exact splitting kernels and the elementary one-dimensional case remain acknowledged inputs/benchmarks.

## Limitations

The result is for independent Poisson reorientation with a single fixed speed, no translational diffusion, symmetric iid headings, and ideal sticky hard walls. It addresses normal mean force per swimmer; converting to pressure at fixed number density introduces an additional factor of channel width. The angular density is fixed as the slit narrows. The theorem does not establish a crossover for heading laws varying with slit width, finite tumble times, multi-particle hydrodynamics, anisotropic wall interactions, or all slowly varying singular densities. Possible previously unindexed equivalent asymptotic consequences of the published exact integral equations remain a priority risk; a literature search is not a proof of unique priority.

## References

1. D. Frydel, *Run-and-tumble particles in slit geometry as a splitting probability problem* (first arXiv version 8 October 2024), https://arxiv.org/html/2410.06393v1 ; https://arxiv.org/abs/2410.06393 .
2. B. Ezhilan, R. Alonso-Matilla and D. Saintillan, *On the distribution and swim pressure of run-and-tumble particles in confinement* (first arXiv version 23 July 2015), https://arxiv.org/html/1507.06379v1 ; https://arxiv.org/abs/1507.06379 .
3. T. Pietrangeli, C. Ybert, C. Cottin-Bizonne and F. Detcheverry, *Optimal run-and-tumble in slit-like confinement* (arXiv 11 April 2024), https://arxiv.org/abs/2404.07680 . This work studies tangential diffusivity, not the present normal pressure asymptotics.
