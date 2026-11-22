# Two adult-census ranking reversals in declining two-stage habitats: a sharp feasible phase diagram

## Finding
For any two positive, subcritical juvenile–adult demographic systems initially containing one adult and no juveniles, the expected adult abundances either agree identically or exchange strict rank **at most twice** at positive times. Two rank exchanges are achievable even though both adult abundances decrease strictly throughout. If the adult-loss rates are equal, at most one positive-time exchange is possible.

A fully feasible one-parameter-per-habitat family with adult spectral decay rates \(\{1,3\}\) and \(\{2,4\}\) yields an exact complete two-reversal window: with slow-mode adult weights \(p,q\in(0,1)\), precisely two positive-time rank reversals occur if and only if
\[
0<p<\frac14,\qquad 2\sqrt p-p<q<p+\frac12.
\]
On the lower boundary the two crossings merge into a tangency; the upper boundary sends the earlier crossing to time zero. For \(p=1/10\) and \(q=11/20\), the two positive crossing times are exactly \(\log(3/2)\) and \(\log3\), with habitat 1 having the greater adult abundance at both early and late times but the smaller abundance between those crossings.

## Assumptions and scope
For habitat \(i\), let \(J_i(t)\) and \(A_i(t)\) be the **expected** juvenile and adult numbers per initial adult, governed for \(t\ge0\) by
\[
\dot J_i=\beta_i A_i-\gamma_iJ_i,\qquad \dot A_i=\kappa_iJ_i-\alpha_i A_i,\qquad J_i(0)=0,\ A_i(0)=1.
\]
All four rates are strictly positive, and \(\alpha_i\gamma_i>\beta_i\kappa_i\) (negative spectral growth). Births produce juveniles; juveniles mature at \(\kappa_i\) and are otherwise lost at rate \(\gamma_i-\kappa_i>0\) in the explicit family below, although the general theorem requires only the stated positive matrix entries. Adult losses occur at \(\alpha_i\). These are expected linear census trajectories, not deterministic integer animal counts. A **strict rank reversal** means a sign-changing zero of \(A_1(t)-A_2(t)\) at \(t>0\); tangencies are not counted.

For the fully feasible equally spaced spectral family, choose the same maturation rate \(\kappa_1=\kappa_2=1\) and set
\[
\begin{aligned}
&\alpha_1=3-2p,\ \gamma_1=1+2p,\ \beta_1=4p(1-p),\\
&\alpha_2=4-2q,\ \gamma_2=2+2q,\ \beta_2=4q(1-q).
\end{aligned}
\]
All rates and juvenile nonmaturation losses are strictly positive for \(0<p,q<1\), and the two characteristic decay-rate pairs are precisely \(\{1,3\}\) and \(\{2,4\}\).

## Proof
**Spectral reduction.** Eliminating juveniles gives
\[
\ddot A+(\alpha+\gamma)\dot A+(\alpha\gamma-\beta\kappa)A=0,\quad A(0)=1,\quad\dot A(0)=-\alpha.
\]
Its distinct negative characteristic roots are \(-r\) and \(-s\), with \(0<r<s\). Since \(\beta\kappa>0\), we have \(r<\alpha<s\), so
\[
A(t)=w e^{-rt}+(1-w)e^{-st},\qquad w=\frac{s-\alpha}{s-r}\in(0,1).
\]
In particular \(A'(t)<0\) for all \(t\ge0\). The difference of two adult trajectories is a sum of at most four distinct real exponentials. A nonzero linear combination of \(m\) distinct real exponentials has at most \(m-1\) real zeros, with multiplicities: multiply by the reciprocal of the smallest exponential and apply Rolle's theorem inductively to its derivative, which has at most \(m-1\) terms. Since \(A_1(0)-A_2(0)=0\), there can be at most two further positive zeros. If \(\alpha_1=\alpha_2\), the time-zero zero has multiplicity at least two, leaving at most one positive zero. Coincident modes only reduce the upper bound.

**Exact realization and phase diagram.** Direct substitution gives
\[
A_1(t)=p e^{-t}+(1-p)e^{-3t},\qquad A_2(t)=q e^{-2t}+(1-q)e^{-4t}.
\]
Set \(x=e^{-t}\in(0,1)\). The difference factors exactly as
\[
A_1(t)-A_2(t)=x(1-x)\left[p+(p-q)x+(1-q)x^2\right].
\]
The quadratic vanishes precisely when
\[
q=g_p(x):=\frac p{x}+\frac{x}{1+x}.
\]
As \(x\downarrow0\), \(g_p(x)\to\infty\); and \(g_p(1)=p+1/2\). Its derivative is
\[
g_p'(x)=-\frac p{x^2}+\frac1{(1+x)^2}.
\]
If \(0<p<1/4\), there is exactly one minimum in \((0,1)\), at \(x_*=\sqrt p/(1-\sqrt p)\), with value \(g_p(x_*)=2\sqrt p-p\). Thus the level \(q\) meets the graph at two distinct points in \((0,1)\) exactly for \(2\sqrt p-p<q<p+1/2\). At the lower boundary the quadratic is tangent; at the upper boundary one intersection is at \(x=1\). If \(p\ge1/4\), the function is decreasing on \((0,1)\), so two intersections cannot occur. The sign is positive outside the two crossing points and negative between them.

**Exact witness.** With \(p=1/10,q=11/20\), the two juvenile–adult parameter quadruples \((\alpha,\beta,\gamma,\kappa)\) are
\[
(14/5,9/25,6/5,1),\qquad (29/10,99/100,31/10,1).
\]
Their positive matrix entries and strictly negative eigenvalues satisfy all assumptions, and
\[
A_1(t)-A_2(t)=\frac{x(1-x)(3x-1)(3x-2)}{20},\qquad x=e^{-t}.
\]
There are exactly two positive-time simple zeros, \(t=\log(3/2)\) and \(t=\log3\), with signs positive, negative, positive in that order. This proves sharpness of the general bound under strictly positive biological rates and strictly decreasing adult censuses.

## Verification
The standalone \(\texttt{checker.py}\) recomputes the exact symbolic factorization, both characteristic polynomials, initial derivatives, and rational sign tests. It also makes 2,000 reproducibly seeded numerical comparisons between the exact two-crossing criterion and the quadratic-root characterization. This sampling is supplementary; the universal zero bound and full parameter-window classification are proved analytically above.

## Relationship to prior work
Crispim-Mendes et al. (2024) motivate the ecological significance of patch lifespan and transient source–sink assessments using an individual-based model; they do **not** supply this simple continuous-time two-stage phase diagram. Giaimo and Traulsen (2022) address stage-structured transient sensitivity, not this exact comparison of two distinct positive two-stage systems. The classical variation-diminishing theory of Boland, Proschan and Tong (1989), together with the exponential Chebyshev property, already provides general bounds on crossings of exponential mixtures. **The exponential crossing bound itself is not claimed to be a newly discovered general principle.** The contribution assessed here is the positivity-constrained two-stage ecological realization, strict-decline sharpness, equal-adult-loss obstruction and full feasible two-reversal weight window.

## Limitations
The trajectories are expected adult counts in a linear, density-independent two-stage model. Their decline does not assert monotone behavior of juveniles, full populations, or stochastic sample paths. Rank comparisons are conditional on a common one-adult, zero-juvenile initial state. The equally spaced spectral example is an exact analytical benchmark, not a calibrated model of any specific habitat. General exponential-mixture crossing bounds are classical; the extent to which earlier specialized demographic or mixture articles already imply the exact feasible two-stage window needs further historical verification. The 1989 mixture paper's full text was not accessible for a page-level comparison.

## References
1. Crispim-Mendes, T., et al. (2024). *Patch spatial attributes and time to disturbance affect the emergence of source local populations within ephemeral habitats*. Ecological Modelling 496, 110839. First public availability 2024-08-21. https://doi.org/10.1016/j.ecolmodel.2024.110839
2. Giaimo, S., and Traulsen, A. (2022). *Age-specific sensitivity analysis of stable, stochastic and transient growth for stage-classified populations*. Ecology and Evolution 12, e9561. https://doi.org/10.1002/ece3.9561
3. Boland, P. J., Proschan, F., and Tong, Y. L. (1989). *Crossing properties of mixture distributions*. Probability in the Engineering and Informational Sciences 3, 355–366. https://doi.org/10.1017/S0269964800001224
