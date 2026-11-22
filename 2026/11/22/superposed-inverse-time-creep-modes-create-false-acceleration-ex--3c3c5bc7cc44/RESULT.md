# Superposed inverse-time creep modes create false acceleration exponents and late failure forecasts

## Finding

Consider a measured velocity obtained by adding positive precursor velocities with possibly different finite singular times. Although each constituent follows an exact constant-exponent inverse-velocity law with acceleration exponent \(2\), the composite generally appears to have a *larger, changing* exponent, and every two-point inverse-velocity extrapolation forecasts an event strictly later than the earliest constituent singularity. For two constituents, both the forecast bias and the unique intermediate maximum of the apparent acceleration exponent have sharp formulas.

**Theorem.** Let \(m\geq 2\), \(c_i>0\), and \(T_i\in\mathbb R\) for \(1\leq i\leq m\); put \(T_*=\min_iT_i\). For every \(t<T_*\) define
\[
V(t)=\sum_{i=1}^m\frac{c_i}{T_i-t},\qquad R(t)=\frac1{V(t)},\qquad
\alpha_{\mathrm{app}}(t)=\frac{V(t)V''(t)}{V'(t)^2}.
\]
Then \(R''(t)\leq0\) and \(\alpha_{\mathrm{app}}(t)\geq2\), with strict inequalities at every such \(t\) exactly when the \(T_i\) are not all equal. If the \(T_i\) are not all equal, the zero \(\widehat T\) of the secant through \((t_1,R(t_1))\) and \((t_2,R(t_2))\), for *every* \(t_1<t_2<T_*\), obeys \(\widehat T>T_*\). If all singular times coincide, both inequalities are equalities and every such secant predicts \(T_*\) exactly.

For two modes, write \(T_1<T_2\), \(a=c_1\), \(b=c_2\), \(\Delta=T_2-T_1\), and \(x_j=T_1-t_j\), so \(x_1>x_2>0\). Then the forecast delay is exactly
\[
\boxed{\widehat T-T_1=
\frac{b\Delta x_1x_2}{a\Delta^2+a\Delta(x_1+x_2)+(a+b)x_1x_2}},
\qquad 0<\widehat T-T_1<\frac{b\Delta}{a+b}.
\]
For fixed parameters the delay is strictly increasing in each positive \(x_j\) (among ordered samples), tends to zero as the final observation approaches \(T_1\), and approaches the sharp upper bound when both observations recede to the remote past.

Set \(z=(T_1-t)/(T_2-t)\in(0,1)\). The apparent exponent obeys
\[
\boxed{\alpha_{\mathrm{app}}(t)=2+
\frac{2abz(1-z)^2}{(a+bz^2)^2}}.
\]
Its excess over \(2\) has exactly one strict maximum, attained when \(z=z_*\in(0,1/3)\) is the unique root of
\[
a(1-3z_*)=bz_*^2(3-z_*).
\]
At equal amplitudes \(a=b\), the maximum is exactly \(9/4\), occurring at \(z_*=2-\sqrt3\). More generally, as \(b/a\to\infty\),
\[
z_*\sim\sqrt{\frac{a}{3b}},\qquad
\max_{t<T_1}\alpha_{\mathrm{app}}(t)=2+\frac{9}{8\sqrt3}\sqrt{\frac ba}+O(1).
\]
Thus no universal upper bound on the *apparent* acceleration exponent exists, despite every component having true exponent \(2\).

## Assumptions and scope

The measured scalar displacement is an additive sum of modal displacements, so its derivative is the **sum of velocities**; this is neither the sum of inverse velocities nor an average of independently analyzed sensors. All amplitudes are strictly positive and all constituent singular times finite. The analysis is limited to \(t<T_*\), before any singularity. The exponent \(\alpha_{\mathrm{app}}\) is the instantaneous log-slope \(d\log V'/d\log V\), which is well defined because \(V>0\), \(V'>0\). The extrapolation is the unique straight line through two *exact*, noise-free reciprocal-velocity observations. There are no assumptions about spatial location, mechanical coupling, calibration, noise, or post-failure motion.

The positive mode \(v_i(t)=c_i/(T_i-t)\) satisfies \(v_i'=v_i^2/c_i\) and therefore has constant local acceleration exponent exactly \(2\). These premises describe a deliberately idealized version of the classic inverse-velocity singularity model, not a mechanically identified multi-plane slope.

## Proof

**1. Arbitrarily many modes: strict concavity and exponent inflation.** For \(k=1,2,3\) put \(S_k(t)=\sum_{i=1}^m c_i/(T_i-t)^k\). Differentiating gives \(V=S_1\), \(V'=S_2\), and \(V''=2S_3\). Thus
\[
R''=\frac{2(S_2^2-S_1S_3)}{S_1^3},\qquad
\alpha_{\mathrm{app}}=\frac{2S_1S_3}{S_2^2}.
\]
The Cauchy–Schwarz inequality applied to the vectors with entries \(\sqrt{c_i}/\sqrt{T_i-t}\) and \(\sqrt{c_i}/(T_i-t)^{3/2}\) gives \(S_2^2\leq S_1S_3\). Since every \(c_i\) is positive, equality holds if and only if all \(T_i-t\), hence all \(T_i\), are equal. This proves the curvature and exponent statements with their exact equality cases.

**2. General strict forecast delay.** The function \(R\) is positive and strictly decreasing on \(( -\infty,T_*)\), with continuous extension \(R(T_*)=0\); the latter follows by isolating the modes having \(T_i=T_*\). When two singular times differ, \(R\) is strictly concave. For \(t_1<t_2<T_*\), strict concavity yields
\[
\frac{R(t_2)-R(t_1)}{t_2-t_1}>
\frac{R(T_*)-R(t_2)}{T_*-t_2}=-\frac{R(t_2)}{T_*-t_2}.
\]
Both slopes are negative. Consequently the two-observation secant remains positive at \(T_*\) and its zero lies strictly later. If all \(T_i=T_*\), direct summation gives \(R=(T_*-t)/(\sum_i c_i)\) and the forecast is exact.

**3. Two-mode exact delay.** Take \(x=T_1-t\), \(A=a+b\). Direct algebra gives
\[
R(t)=\frac{x(x+\Delta)}{Ax+a\Delta}
=\frac{x}{A}+\frac{b\Delta}{A^2}
-\frac{ab\Delta^2}{A^2(Ax+a\Delta)},
\quad
R''(t)=-\frac{2ab\Delta^2}{(Ax+a\Delta)^3}<0.
\]
The secant slope with respect to the variable \(x\) is
\[
\frac{R(x_1)-R(x_2)}{x_1-x_2}
=\frac{a\Delta^2+a\Delta(x_1+x_2)+Ax_1x_2}
{(Ax_1+a\Delta)(Ax_2+a\Delta)}.
\]
Its extrapolated intercept at \(x=0\) is
\[
\frac{b\Delta x_1x_2}{(Ax_1+a\Delta)(Ax_2+a\Delta)}.
\]
Dividing intercept by positive slope yields the claimed positive time delay. The denominator exceeds \(Ax_1x_2\), yielding the strict upper bound. Differentiating the rational expression with respect to either \(x_j\) gives a positive derivative (for \(x_1\), its unsigned numerator simplifies to a positive factor proportional to \(a\Delta(\Delta+x_2)\)); symmetry handles \(x_2\). The two endpoint limits prove sharpness and the limit of vanishing bias near failure. For instance, with \(a=b=1\), \(\Delta=2\), \(x_1=2\), \(x_2=1\), the exact bias is \(2/7\).

**4. Exact exponent and unique hump.** From the two-mode formulas for \(V,V',V''\), factoring powers of \(x\) and \(x+\Delta\) gives \(\alpha_{\mathrm{app}}=2+2abz(1-z)^2/(a+bz^2)^2\). The derivative of its positive excess with respect to \(z\) has the same sign as
\[
H(z)=a(1-3z)-bz^2(3-z).
\]
Indeed all omitted factors are strictly positive for \(0<z<1\). Here
\[
H'(z)=-3a-6bz+3bz^2<0,
\]
while \(H(0)=a>0\) and \(H(1/3)=-8b/27<0\). There is exactly one root in \((0,1/3)\), which gives the sole maximum. The excess vanishes as \(z\downarrow0\) or \(z\uparrow1\), so the maximum is global. For \(a=b\), the cubic factors to give the only admissible root \(2-\sqrt3\); substitution gives \(1/4\) excess. For \(r=b/a\to\infty\), dividing \(H(z_*)=0\) by \(a\) and balancing its leading constant against \(3rz_*^2\) gives \(z_*=(3r)^{-1/2}(1+O(r^{-1/2}))\). Substitution in the exponent gives excess \(9\sqrt r/(8\sqrt3)+O(1)\), proving the asymptotic and absence of a universal upper bound.

## Verification

The accompanying standalone Python file `verify.py` re-evaluates the exact secant-intercept identity against direct reciprocal velocities for 1,800 seeded random parameter sets, checks strict bias bounds and monotonicity, directly computes \(VV''/(V')^2\) and compares it with the rational exponent formula, bisects the critical cubic, checks equal-amplitude constants and large-ratio asymptotics, and checks positive Cauchy–Schwarz gaps for several higher-mode mixtures. The program uses the Python standard library only. It prints `PASS: 14809 deterministic numerical checks` on success. These finite diagnostics support algebraic reproducibility; the statements for all positive real parameters are proved above, not inferred from finite tests.

## Relationship to prior work

Fukuzono (1985) formulated the inverse-velocity failure-time method from accelerating slope displacement and discussed a constant acceleration exponent. The present result keeps exact exponent \(2\) in *every* component but investigates a sum of components with *different* singular times. The mixture's curved reciprocal-velocity graph and fictitious exponent hump therefore do not require changing any component's exponent. Carlà et al. (first online July 2016) studied practical smoothing, noise and choice of regression lines; those sources motivate why an exact deterministic bias diagnosis matters, but the examined article does not give this additive two-clock classification. Ren et al. (2025) use multiple radar measurement points and per-point inverse-velocity approaches; separately analyzing locations is not the sum-of-velocities observation model here.

The elementary Cauchy–Schwarz step is general mathematical background, rather than a claimed new inequality. Novelty is claimed only for the combined *geophysical interpretation and precise two-clock bias/unique-hump classification* relative to the sources examined; broader independent historical searching remains necessary.

## Limitations

This is an exact theorem for a stipulated additive-velocity observation mechanism. It does not establish that two physical slip planes superpose in this way or that all observed inverse-velocity curvature is caused by mixing. It does not handle noisy estimation, unknown physical coupling, finite observation resolution, variable strength, unequal component exponents, or continuing dynamics beyond the earliest mathematical singularity. Time-to-failure extrapolation in the presence of field uncertainty must not be treated as operationally reliable on the strength of these formulas. The results do not imply that a real slope will fail at the singularity. Historical originality has not been independently audited, and apparently relevant inaccessible or unlocated material could contain earlier equivalent statements.

## References

1. T. Fukuzono, “A Method to Predict the Time of Slope Failure Caused by Rainfall Using the Inverse Number of Velocity of Surface Displacement,” *Landslides* **22**(2), 8–13 (first published September 15, 1985), https://doi.org/10.3313/jls1964.22.2_8 . Public article and PDF: https://www.jstage.jst.go.jp/article/jls1964/22/2/22_2_8/_article/-char/en .
2. T. Carlà et al., “Guidelines on the use of inverse velocity method as a tool for setting alarm thresholds and forecasting landslides and structure collapses,” *Landslides* **14**, 517–534 (first online July 5, 2016), https://doi.org/10.1007/s10346-016-0731-5 . Full text: https://link.springer.com/article/10.1007/s10346-016-0731-5 .
3. Ren et al., “Progressive Landslide Prediction Using an Inverse Velocity Method with Multiple Monitoring Points of Synthetic Aperture Radar,” *Applied Sciences* **15**(13), 7449 (2025), https://doi.org/10.3390/app15137449 . Full text: https://www.mdpi.com/2076-3417/15/13/7449 .
4. “An improvement velocity inverse method for predicting the slope imminent failure time” (2023), https://doi.org/10.1080/19475705.2023.2239991 . Search-indexed abstract and sections considered; complete publisher text was not accessible during this assessment.
