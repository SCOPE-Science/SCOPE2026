# Sharp height-dependent reversal of matched bulk and surface deposition in an indoor aerosol slab

## Finding

A height-independent aerosol-removal approximation can **underpredict the vertically averaged steady concentration and the central breathing-zone concentration while simultaneously overpredicting concentration next to both depositing boundaries**, even when its bulk loss rate is calibrated by the correct surface-to-volume factor. This occurs, with exactly two sharp crossover heights, for every choice of positive parameters in the symmetric slab model below.

**Theorem.** Let \(D,r,\kappa,L,Q>0\). Let \(c\) be the stationary aerosol concentration from a laterally uniform, infinitesimally thin source at the centre \(z=L/2\) of a slab of height \(L\), subject to bulk deactivation/ventilation \(r\), vertical diffusivity \(D\), and identical floor and ceiling deposition with Robin parameter \(\kappa\). Compare it with a vertically mixed model having the *same integrated source* and global deposition rate \(2D\kappa/L\). Then the local-to-global difference has exactly two zeros at \(z=z_*\) and \(z=L-z_*\), with \(0<z_*<L/2\). The local model predicts smaller concentration for \(0\le z<z_*\) and \(L-z_*<z\le L\), and greater concentration for \(z_*<z<L-z_*\). The height-averaged local concentration is **strictly greater** than the global model's prediction.

More precisely, write
\[
 k=\sqrt{r/D},\qquad a=kL/2,\qquad t=\kappa/k,
 \qquad B=\frac{\sinh a+t\cosh a}{a+t}.
\]
The unique lower crossover is
\[
 z_*=\frac1k\log\left(\frac{B+\sqrt{B^2+t^2-1}}{1+t}\right).
\]
No additional parameter restriction or numerical tuning is needed. A steady inhalation-risk model with monotonically increasing dose response consequently gives the same strict ordering of risk at each fixed receiver height off the crossover levels for all sufficiently long finite exposures after a source is switched on, provided equal breathing and dose-response parameters are used in both models.

## Assumptions and scope

We use the one-dimensional, horizontally translationally invariant reduction of an indoor three-dimensional diffusion model, not a general three-dimensional room. The source has total production \(Q\) **per unit horizontal area** and lies on the horizontal midplane. Its vertical profile is a Dirac sheet source. All parameters are strictly positive; no horizontal airflow, furniture, moving agents, local ventilation, or inhalation sinks are included. The model is deterministic and linear.

For \(0<z<L\), the steady concentration solves in distributions
\[
 -D c''(z)+r c(z)=Q\,\delta_{L/2}(z),
 \qquad c'(0)=\kappa c(0),\quad c'(L)=-\kappa c(L).
\]
Here the deposition velocity is \(D\kappa\), and \(r\) includes any other spatially homogeneous removal rate. At the middle the solution is continuous and has jump \(-D[c'(L/2+)-c'(L/2-)]=Q\).

A height-independent, vertically averaged source \(Q/L\) with surface-to-volume matched deposition \(\gamma_{\mathrm{bulk}}=2D\kappa/L\) has stationary concentration
\[
 \widehat c=\frac{Q/L}{r+\gamma_{\mathrm{bulk}}}=
 \frac{Q}{2Dk(a+t)}.
\]
This calibration is defined here and **need not equal the numerical calibration used in a published two-dimensional model**, which also incorporates other geometry and physical assumptions. Only the floor and ceiling contribute reactive surface in this idealized slab.

## Proof

**1. Exact Robin Green profile and uniqueness.** Set \(d(z)=\min\{z,L-z\}\) and \(F(y)=\cosh(ky)+t\sinh(ky)\). Since the stationary operator \(-D\partial_{zz}+r\) has strictly positive quadratic form with Robin boundary conditions, it is invertible. The symmetric distributional solution is
\[
 c(z)=\frac{Q\,F(d(z))}{2Dk[\sinh a+t\cosh a]}.
\]
On each half-interval it solves the homogeneous equation. At the floor, \(F'(0)=kt=\kappa F(0)\), which verifies the Robin boundary condition, and the ceiling condition follows by reflection. The derivative jumps from \(+Q/(2D)\) to \(-Q/(2D)\) at the central sheet, so the displayed formula has exactly the prescribed source. Positivity and uniqueness follow also by multiplying the homogeneous zero-source equation by its solution and integrating: the resulting sum of \(D\int|u'|^2\), \(r\int|u|^2\), and \(D\kappa(|u(0)|^2+|u(L)|^2)\) must vanish.

**2. A universal two-crossing inequality.** Dividing by the global concentration yields
\[
 \frac{c(z)}{\widehat c}
 =\frac{(a+t)F(d(z))}{\sinh a+t\cosh a}
 =\frac{F(d(z))}{B}.
\]
For all \(a,t>0\),
\[
 (a+t)(B-1)=(\sinh a-a)+t(\cosh a-1)>0,
\]
and
\[
 (a+t)(F(L/2)-B)
 =a\cosh a-\sinh a+t(a+t)\sinh a>0.
\]
The final inequality uses the positive derivative \(d[\,a\cosh a-\sinh a\,]/da=a\sinh a>0\) and its zero limit at \(a=0\). Thus \(1<B<F(L/2)\). Since \(F'(y)=k[\sinh(ky)+t\cosh(ky)]>0\) for \(0\le y\le L/2\), the equation \(F(y)=B\) has exactly one solution on that half-interval. Solving this equation as a quadratic in \(\exp(ky)>0\) gives the specified formula for \(z_*\); the second crossing follows by symmetry. The strict sign statements include both endpoint regions and the central source plane. At the crossings the concentrations are equal.

**3. Strict height-mean bias.** The exact vertical mean is
\[
 \langle c\rangle=\frac1L\int_0^L c(z)\,dz
 =\frac{Q[\sinh a+t(\cosh a-1)]}
 {2Dk\,a[\sinh a+t\cosh a]}.
\]
Consequently,
\[
 \frac{\langle c\rangle}{\widehat c}-1
 =\frac{t[\sinh a+t\cosh a-a-t]}{a[\sinh a+t\cosh a]}>0,
\]
by \(\sinh a>a\) and \(\cosh a>1\). The mean is underestimated even though deposition-adjacent point concentrations are overestimated. Equivalently, integrating the steady PDE shows \(rL\langle c\rangle+2D\kappa c(0)=Q\), while the global model substitutes its uniform value for depleted wall concentrations.

**4. Long-exposure implication, with stated limit.** Consider zero initial aerosol and a constant source switched on at time zero. The local solution is \(c_T=c-\exp(-T A)c\) for the positive Robin operator \(A=-D\partial_{zz}+r\), where the semigroup has \(L^\infty\) contraction bounded by \(e^{-rT}\). Therefore for each height \(z\),
\[
 \int_0^T c_s(z)\,ds=T c(z)+O(1),\qquad
 \int_0^T\widehat c_s\,ds=T\widehat c+O(1).
\]
The implicit error can be bounded by \((\|c\|_\infty+\widehat c)/r\), independently of \(T\). At any fixed height strictly outside the two crossings the coefficient \(c(z)-\widehat c\) is nonzero, so the sign of the integrated dose difference eventually agrees with the stated stationary sign. Applying the same strictly increasing dose-response function to both doses preserves their ordering. **No assertion about a universal finite crossover time, moving receiver, or equality exactly at the stationary crossing heights is made.**

## Verification

The included standalone Python script `checker.py` checks the precise Green function, positivity of the crossover brackets, height-average relation, Robin endpoint flux, central-source jump, and integrated mass balance. It passed one exact elementary case and 504 positive-parameter floating-point configurations. These finite numerical checks illustrate but do not replace the all-parameter inequalities above.

For \(D=r=\kappa=Q=1\) and \(L=2\), the formulas simplify exactly to
\[
 c(z)=\tfrac12 e^{-|z-1|},\qquad \widehat c=\tfrac14,
 \qquad z_*=1-\log2.
\]
In particular, \(c(0)=1/(2e)<1/4<c(1)=1/2\). The second crossing is \(1+\log2\).

Reproduction: run `python checker.py` with a Python 3 standard-library installation. The mathematical proof needs no computation and contains the complete quantifiers and boundary conditions.

## Relationship to prior work

Bansal, Kaouri and Woolley (arXiv:2611.13372, initially public 9 November 2026) explicitly contrast a vertically uniform, globally depleted aerosol model with a three-dimensional Robin-wall model. Their Sections 2–4 and Appendix B give model definitions, numerical concentration profiles and risk comparisons in a courtroom, care home and supermarket. They report lower simulated breathing-zone risks from the global model in those scenarios, but do not state the universal **two-height** reversal or strict **height-mean** inequality for the surface-to-volume-matched symmetric slab considered here. The present result is an idealized analytic complement, not a correction of their computed infection risks.

Xue, Jabi, Woolley and Kaouri (2024, arXiv:2408.11772) developed the original globally removed indoor aerosol model; this does not supply the matched Robin slab classification. Pretty, Griffiths, Lau and Kaouri (arXiv:2309.16332; journal publication 2026) studied *local ventilation* versus equivalent global ventilation and already showed spatial sign reversals under some air-flow geometries; the mere existence of nonuniform model-comparison errors is therefore **not claimed as new**. Aquino (2024) derives Robin-wall transport/equilibrium profiles for advective channel transport, not the present centrally driven steady source against a calibrated global deposition sink. The Robin Green-function technique itself is standard; the asserted contribution is its complete parameter-independent, geometrically located *comparative bias classification* for this specific, epidemiologically motivated model pair, including the simultaneous strict mean inequality.

## Limitations

The emitting sheet and laterally infinite or periodic domain are strong idealizations; no genuine single-point emitter, complex room, advection, breathing sinks, turbulent intermittent concentration, furniture, or human behavior is included. The bulk-removal model is calibrated by a precise surface-to-volume formula that need not coincide with an empirical or published model's choice of rate. No quantitative outbreak prediction, experimental validation, universal high/low infection-risk direction for real rooms, or nonlinear epidemiological dynamics follows. Historical equivalence to a previously published Green-function comparison is still possible; the available primary-literature and research-record comparison did not find an identical theorem, which is not a proof of novelty. Independent validation has not been performed.

## References

1. N. Bansal, K. Kaouri and T. E. Woolley, *Extending indoor airborne infection risk modelling to 3D, with local surface deposition*, arXiv:2611.13372 (first public 9 November 2026; consulted full HTML version 2), https://arxiv.org/html/2611.13372v2 .
2. Y. Xue, W. Jabi, T. E. Woolley and K. Kaouri, *VIRIS: Simulating indoor airborne transmission combining architectural design and people movement*, arXiv:2408.11772 (2024), https://arxiv.org/html/2408.11772v1 .
3. A. Pretty, I. M. Griffiths, Z. Lau and K. Kaouri, *The effect of local ventilation on a spatiotemporal model of airborne disease transmission in indoor spaces*, arXiv:2309.16332 (2023 preprint; journal online 15 July 2026), https://www.cambridge.org/core/journals/european-journal-of-applied-mathematics/article/effect-of-local-ventilation-on-a-spatiotemporal-model-of-airborne-disease-transmission-in-indoor-spaces/0F6DB4366935013FF9D19DC5DAE49414 .
4. T. Aquino, *Equilibrium distributions under advection–diffusion in laminar channel flow with partially absorbing boundaries*, Journal of Fluid Mechanics 985 (2024), DOI 10.1017/jfm.2024.294, https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/equilibrium-distributions-under-advectiondiffusion-in-laminar-channel-flow-with-partially-absorbing-boundaries/5E209E68B5CE4C6452CEA88951C231C4 .
