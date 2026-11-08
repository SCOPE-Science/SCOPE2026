# A one-crossing law for fair-rate threshold versus Poisson resetting

## Finding

For a symmetric diffusion in natural scale, threshold resets at the first exit from a symmetric interval produce a stationary absolute position strictly smaller in first-order stochastic order than Poisson resetting **when the reset-event frequencies are matched**. This universal comparison holds even if diffusivity depends on position and yields an exact single-crossing theorem for the two radial densities.

Let \(a>0\), let \(R_T\) and \(R_P\) be stationary absolute positions under threshold and Poisson resetting, respectively, and choose the Poisson rate
\[
r=\left(\int_0^a(a-x)w(x)\,dx\right)^{-1}.
\]
Then there is a unique \(x_*\in(0,a)\) such that, writing \(f_T\) and \(f_P\) for radial densities,
\[
f_T(x)>f_P(x)\quad(0<x<x_*),\qquad
f_T(x)<f_P(x)\quad(x>x_*),
\]
and for every \(t>0\),
\[
\boxed{\Pr(R_T>t)<\Pr(R_P>t).}
\]
Thus for every nondecreasing measurable \(g:[0,\infty)\to[0,\infty)\), \(\mathbb E[g(R_T)]\le\mathbb E[g(R_P)]\) in the extended sense. For strictly increasing \(g\) with both expectations finite the inequality is strict.

For the sluggish family \(D(x)=|x|^{-\alpha}\), \(\alpha\ge0\), the matching rate is \(r=(\alpha+1)(\alpha+2)/a^{\alpha+2}\). For \(\alpha=0\), \(a=1\), the densities meet once at \(x_*=0.7579006016\ldots\), while the radial means are \(\mathbb E[R_T]=1/3\) and \(\mathbb E[R_P]=1/\sqrt 2\).

## Assumptions and scope

Take an even continuous function \(w:\mathbb R\to[0,\infty)\) that is strictly positive away from zero. Construct the generalized regular diffusion \(X\) by starting standard Brownian motion \(B\) with generator \(\partial_x^2\) at zero and applying the inverse of the physical-time clock \(A_s=\int_0^s w(B_u)\,du\). Recurrence of Brownian motion and positivity of \(w\) on every nontrivial interval ensure \(A_s\to\infty\) almost surely, giving a conservative time-changed process. Where \(w(x)>0\), its generator is \(Lf(x)=w(x)^{-1}f''(x)\). This construction includes \(w(x)=|x|^\alpha\) for \(\alpha\ge0\), including the harmless zero of the speed density at the origin when \(\alpha>0\).

In the threshold protocol each excursion starts at zero and ends at its first hit of either \(-a\) or \(a\), followed immediately by a reset to zero. In the Poisson protocol an independent exponential clock of rate \(r\) resets to zero, regardless of position. Reset events are counted in either case. The comparison concerns stationary position at an ordinary observation time, **not** position immediately before reset, reset-work expenditure, mean target-search time, or nonequilibrium entropy production.

## Proof

**Step 1 (fair rate and threshold potential).** Denote by \(\tau_a\) the first exit from \((-a,a)\) for the free diffusion started at zero. The Brownian Green kernel on that interval, evaluated at the starting point, is \((a-|x|)/2\) for the generator \(\partial_x^2\). Applying the time change yields
\[
\mathbb E_0\tau_a=\frac12\int_{-a}^a(a-|x|)w(x)\,dx
=\int_0^a(a-x)w(x)\,dx=:m_a\in(0,\infty).
\]
The renewal-reward theorem makes the long-run threshold-reset frequency \(1/m_a\). Set \(r=1/m_a\), which equals the rate of independent Poisson reset events. The same killed Green kernel gives the normalized threshold stationary density
\[
p_T(x)=\frac r2 w(x)(a-|x|)_+,
\quad f_T(x)=r w(x)(a-x)\mathbf1_{(0,a)}(x),\quad
2\int_0^\infty p_T(x)\,dx=1.
\]

**Step 2 (Poisson potential).** Renewal at exponentially distributed intervals produces
\[
p_P(x)=r\int_0^\infty e^{-rt}p_t(0,x)\,dt,
\]
where \(p_t\) is the free transition density with respect to Lebesgue measure. Write \(p_P(x)=w(x)h(|x|)\) for \(x\ne0\). The resolvent forward equation \((w^{-1}p_P)''-r p_P+r\delta_0=0\) implies, for \(x>0\),
\[
h''(x)=r w(x)h(x),\qquad h'(0+)=-r/2.
\]
Positivity of the free heat kernel gives \(h(x)>0\) for every \(x\ge0\); the resolvent has total mass one. In particular, \(h''(x)>0\) for \(x>0\) and hence \(h'(x)>-r/2\) there. These identities can also be read in the weak/distributional sense near a zero of \(w\); the assumptions make \(h\) continuously differentiable at zero.

**Step 3 (exactly one crossing).** On \([0,a]\), compare the two speed-normalized potentials via
\[
F(x)=h(x)-\frac r2(a-x).
\]
The strict convexity from Step 2 yields \(F'(x)=h'(x)+r/2>0\) for every \(x>0\), and \(F(a)=h(a)>0\). Necessarily \(F(0)<0\): otherwise \(p_P(x)\ge p_T(x)\) throughout \((0,a)\), strictly for positive \(x\), and \(p_P(x)>p_T(x)=0\) throughout \((a,\infty)\). Integrating both even densities would contradict that both have total mass one. Hence \(F\) is strictly increasing through exactly one zero \(x_*\in(0,a)\). Since \(w(x)>0\) for positive \(x\), its sign is precisely that of \(p_P-p_T\) inside \((0,a)\); outside, only the Poisson density remains.

**Step 4 (stochastic order).** By the unique crossing and normalization, the radial cumulative difference \(\int_0^t(f_T-f_P)\,dx\) is positive for \(0<t\le x_*\), and for \(t>x_*\) it equals the strictly positive remaining integral \(\int_t^\infty(f_P-f_T)\,dx\). Thus \(\Pr(R_T>t)<\Pr(R_P>t)\) for every \(t>0\). Integration against the positive Stieltjes measure of a nondecreasing cost function gives the expectation comparison; strictness for strictly increasing integrable functions follows from positive survival gaps on all positive radii.

**Step 5 (sluggish instance).** Taking \(w(x)=|x|^\alpha\) gives \(m_a=a^{\alpha+2}/[(\alpha+1)(\alpha+2)]\), the stated fair rate, and the radial threshold moment identity
\[
\mathbb E[R_T^q]
=a^q\frac{(\alpha+1)(\alpha+2)}{(\alpha+q+1)(\alpha+q+2)}\quad(q>0).
\]
For the Brownian case \(w\equiv1\), \(a=1\), \(r=2\), the two radial densities are \(f_T(x)=2(1-x)\mathbf1_{(0,1)}(x)\) and \(f_P(x)=\sqrt2\,e^{-\sqrt2 x}\). The unique crossing solves \(1-x=e^{-\sqrt2 x}/\sqrt2\), and the stated two means follow by direct integration.

## Verification

The accompanying `verify_reset_comparison.py` independently computes the matched rates, solves the Poisson stationary boundary-value equation with its jump condition, checks mass normalization and the unique crossing, and compares survival probabilities on a test mesh for Brownian and several heterogeneous/sluggish speed densities. It is a finite numerical consistency test only. The universal order and uniqueness follow from the analytical argument in Steps 1–4, not from mesh coverage. Run with `python verify_reset_comparison.py` in a Python environment containing NumPy and SciPy.

## Relationship to prior work

Frimpong, Bresque and Roldán (2026) derive the separate Poisson and threshold stationary laws for sluggish diffusion and investigate first-passage, occupation-fraction and resetting-cost statistics. This work credits those separate laws as antecedents. It adds an explicitly fair reset-frequency calibration, a universal **single-crossing comparison** not restricted to a power-law diffusivity, and strict first-order stochastic dominance for every radial threshold rather than comparison of selected moments or costs. The fair-frequency result is not asserted by those separate stationary formulas without the comparison argument above.

De Bruyne, Randon-Furling and Redner (2020) study first-passage resetting and growth/optimization for threshold-driven particles, with a different question and geometry. More general Green-potential and renewal theory are standard; the novelty claim is the exact protocol comparison, not the underlying kernel identities. A yet-unlocated general theorem implying the comparison remains a priority risk.

## Limitations

This is a continuous-space diffusion theorem for symmetric driftless natural-scale dynamics with immediate zero resets. It does not extend without further argument to asymmetric drift, asymmetric boundaries, discrete lattice walks with overshoot, or multivariate diffusions. Reset events are equally frequent **on average**, not equal-time coupled. The bound compares stationary occupation penalties; it does not imply that one protocol has lower per-reset transport work, lower entropy production, or better first-passage search performance. Positivity/continuity of the speed density away from the origin and the time-change construction are essential to the stated class. 

## References

1. T. D. Frimpong, L. Bresque and E. Roldán, *Sluggish random walks with resetting: nonequilibrium aspects*, arXiv:2610.21962, first posted October 15, 2026, https://arxiv.org/abs/2610.21962.
2. B. De Bruyne, A. Randon-Furling and S. Redner, *Optimization and Growth in First-Passage Resetting*, arXiv:2009.03419, https://arxiv.org/abs/2009.03419.
3. M. R. Evans, S. N. Majumdar and G. Schehr, *Stochastic Resetting and Applications*, Journal of Physics A 53 (2020), https://doi.org/10.1088/1751-8121/ab7cfe.
