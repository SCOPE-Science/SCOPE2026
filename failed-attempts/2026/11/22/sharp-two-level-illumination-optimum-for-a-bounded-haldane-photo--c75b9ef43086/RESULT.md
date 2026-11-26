# Sharp two-level illumination optimum for a bounded Haldane photosynthesis response

## Finding

For any photoinhibition parameter \(c>0\), any irradiance ceiling \(L>0\), and any prescribed mean irradiance \(m\in[0,L]\), maximize
\[
\mathcal{P}(\nu)=\int_{[0,L]}\frac{u}{1+u+cu^2}\,d\nu(u),\qquad \int_{[0,L]}u\,d\nu(u)=m,
\]
where \(\nu\) is an arbitrary Borel probability law. The light level \(u\) is dimensionless. The response is the steady-state Haldane growth law; the model does not incorporate finite switching transients.

Let \(r_c\) be the unique positive zero of \(c^2r_c^3-3cr_c-1=0\). If \(L\le r_c\), the unique optimum for every \(m\) is constant light \(\nu=\delta_m\).

If \(L>r_c\), define
\[
q=q(c,L)=\frac{1+\sqrt{1+L+cL^2}}{cL},\qquad 0<q<r_c<L.
\]
For \(0\le m\le q\), the unique optimum remains \(\nu=\delta_m\). For \(q<m<L\), the **unique** optimum alternates between \(q\) and the equipment ceiling \(L\), with weights
\[
\nu_* = \frac{L-m}{L-q}\,\delta_q+\frac{m-q}{L-q}\,\delta_L.
\]
At \(m=L\), the only admissible law is \(\delta_L\). In particular, the low-light setpoint \(q\) is independent of mean intensity throughout the nonconstant regime; only the duty fraction changes.

This is a complete classification among **all** bounded irradiance laws, not only two-level candidates. The optimal value is the upper concave envelope of the Haldane curve evaluated at \(m\). When \(q<m<L\), every competing law has an exact nonnegative *performance deficit* expressed below, which vanishes only for the stated two-level optimum.

## Assumptions and scope

Define \(f_c(u)=u/(1+u+cu^2)\). Assume \(c,L>0\), \(0\le m\le L\), and an arbitrary probability measure \(\nu\) on \([0,L]\) with first moment \(m\). Growth is the instantaneous **equilibrium** response at each applied light level, averaged over exposure fractions; no constraints on the number, ordering, or durations of exposures are imposed. Constant multiplicative productivity factors are irrelevant to maximizing \(\mathcal P\).

The steady-state Han model appearing as equation (4) of Fierro Ulloa, Lu and Bernard (2023) is
\[
\mu_S(I)=\frac{K\sigma I}{1+\tau\sigma I+(k_d/k_r)\tau(\sigma I)^2},
\]
with positive parameters. The change of variables \(u=\tau\sigma I\), \(c=k_d/(k_r\tau)\) identifies \(\mu_S(I)=(K/\tau)f_c(u)\). Thus \(L=\tau\sigma I_{\mathrm{cap}}\) and \(m=\tau\sigma\bar I\). We optimize normalized equilibrium productivity \(\mathcal P\), not finite-frequency growth, harvested biomass, or yield after hydrodynamic attenuation.

## Proof

**1. Curvature.** Write \(d(u)=1+u+cu^2>0\). Direct differentiation gives
\[
f_c'(u)=\frac{1-cu^2}{d(u)^2},\qquad
f_c''(u)=\frac{2(c^2u^3-3cu-1)}{d(u)^3}.
\]
The cubic \(Q(u)=c^2u^3-3cu-1\) starts negative, decreases until \(u=1/\sqrt c\), then increases strictly to infinity. It therefore has precisely one positive zero \(r_c\). The response is strictly concave on \([0,r_c]\) and strictly convex for \(u>r_c\). Hence if \(L\le r_c\), strict Jensen inequality forces the unique maximizer \(\delta_m\) (including the degenerate endpoint cases).

**2. An exact supporting line for \(L>r_c\).** The proposed \(q\) is the positive solution of
\[
c^2Lq^2-2cq-cL-1=0.
\]
This equation is equivalent to \(f_c'(q)=(f_c(L)-f_c(q))/(L-q)\), and its positive solution is the stated radical. The inequality \(q<L\) is equivalent to \(Q(L)>0\), which holds exactly when \(L>r_c\). Moreover, substituting the defining quadratic into \(Q(q)\) gives
\[
Q(q)=(2cq+1)(q/L-1)<0,
\]
so \(0<q<r_c\). Let \(\ell(u)=f_c(q)+f_c'(q)(u-q)\). An exact common-denominator factorization, using the quadratic equation for \(q\), yields
\[
\boxed{\ell(u)-f_c(u)=\frac{(2cq+1)(u-q)^2(L-u)}{L(1+q+cq^2)^2(1+u+cu^2)}}
\quad (0\le u\le L).
\]
It is strictly positive except at \(u=q\) and \(u=L\). In particular \(\ell(L)=f_c(L)\) and \(\ell\) majorizes the response globally on the allowed interval.

**3. Global upper envelope and equality.** Set \(g(u)=f_c(u)\) for \(0\le u\le q\) and \(g(u)=\ell(u)\) for \(q\le u\le L\). Because \(f_c''<0\) before \(q\) and the two pieces have the same first derivative at \(q\), \(g\) is concave; the factorization gives \(g\ge f_c\). Thus for every admissible \(\nu\),
\[
\mathcal P(\nu)=\mathbb E f_c(U)\le\mathbb E g(U)\le g(\mathbb E U)=g(m).
\]
When \(m\le q\), the constant law achieves equality; strict concavity on \([0,q]\), together with the upper support-line inequality on \((q,L]\), forces equality only for \(U=m\) almost surely. When \(q<m<L\), equality first requires the law to be supported on the exact contact set \(\{q,L\}\); the mean constraint fixes its weights uniquely as stated. This law attains \(g(m)\). For \(m=L\) the mean and cap force \(U=L\) a.s. This proves global optimality, uniqueness, and all boundary cases.

**4. Exact loss identity.** When \(m\ge q\), \(g(m)=\ell(m)=\mathbb E\ell(U)\). Consequently every admissible law obeys
\[
\boxed{g(m)-\mathcal P(\nu)=
\frac{2cq+1}{L(1+q+cq^2)^2}
\int_{[0,L]}\frac{(u-q)^2(L-u)}{1+u+cu^2}\,d\nu(u).}
\]
The integrand is nonnegative and has precisely the two permitted zeros \(q,L\). In particular this identity proves quantitatively that no three-or-more-level distribution, and no different two-level distribution, can match the optimum for \(q<m<L\). The formula also holds at \(m=q\) and \(m=L\).

## Verification

The embedded `verify.py` uses the Python standard library. It checks an exact rational polynomial identity: before imposing the tangency quadratic, the residual after clearing denominators is exactly \(-u(u-q)^2[c^2Lq^2-2cq-cL-1]\). It independently brackets the unique inflection point, verifies the tangency equation to high Decimal precision for several parameter sets, checks the slack factorization pointwise, and tests the global envelope inequality against deterministic random three-atom distributions. These finite tests **do not replace** the preceding global proof. Running `python verify.py` produces 11,188 successful assertions.

For the dimensionless illustration \(c=1\), \(L=10\), \(m=4\), the optimal lower setpoint is \(q=(1+\sqrt{111})/10=1.153565375285\ldots\), and the high-setpoint exposure fraction is \(0.321760657877\ldots\). Optimal normalized rate is \(0.253537072175\ldots\), compared with \(4/21=0.190476190476\ldots\) at constant light, an increase of approximately 33.107% in this idealized calculation. These are hypothetical, not fitted photobioreactor parameters.

## Relationship to prior work

Fierro Ulloa, Lu and Bernard (2023) derive the Haldane response in their equation (4), prove its unique concave-to-convex inflection in Lemma 3, and establish a slow-switching average under fixed high and low light levels (Theorem 1). Their Theorem 3 selects the duty cycle to maximize the **improvement relative to constant light**, holding both high and low intensities fixed and assuming both exceed the inflection. The present claim instead maximizes **absolute equilibrium mean growth over all light-level laws**, subject to a fixed mean and hardware cap; the unique optimal lower intensity lies **below** the inflection. Their established theorems therefore motivate and inform this result but do not state or directly entail the classification, radical contact point, unique support, or sharp loss identity.

Bernard and Lu (2022 preprint) optimize a Beer–Lambert depth-dependent reactor and biomass-dependent optical extinction; that is a different constrained family and objective. More general concave-envelope and moment-problem principles are established mathematical tools, not claimed as new here. The specific closed-form global Haldane envelope, sharp low-level/cap structure, and equality certificate constitute the finding.

## Limitations

The optimization ignores transitional photochemistry, recovery times, switching costs, thermal constraints, photobleaching kinetics, depth gradients, and the coupling of biomass to absorbed light. In the full Han model, the finite-frequency rate differs from the averaged steady-state objective; the source study proves convergence only in the appropriate slow-switching limit for fixed two-level patterns. Consequently the theorem is not a claim of finite-period optimal control or improved experimental yield. The free-distribution constraint treats incident light mean as a budget; real absorbed photon budgets can differ. Established concave-envelope theory might subsume the abstract optimization method; historical priority of this exact specialization has not been independently certified.

## References

1. J. I. Fierro Ulloa, L.-D. Lu, and O. Bernard, *Theoretical growth rate of microalgae under high/low-flashing light*, Journal of Mathematical Biology **86**, article 48 (first online February 21, 2023), DOI: https://doi.org/10.1007/s00285-023-01871-2. Author-accessible full text: https://liudi-lu.github.io/publication/jmb-flashlight/JMB-FlashLight.pdf.
2. O. Bernard and L.-D. Lu, *Optimal optical conditions for Microalgal production in photobioreactors* (author preprint, March 31, 2022), https://liudi-lu.github.io/publication/jpc-optical/JPC-Optical.pdf.
3. *Identifying Opportunities for Improving the Light Utilization Efficiency of Microalgae in a Flashing Light Regime*, Industrial & Engineering Chemistry Research (published online July 24, 2023), https://doi.org/10.1021/acs.iecr.3c00850 (abstract consulted; full article not inspected).
