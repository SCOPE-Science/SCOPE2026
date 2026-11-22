# A sharp simultaneous-to-staggered threshold for two moisture pulses under cooperative saturation

## Finding

Fix two **equal** instantaneous inputs of moisture, one at the beginning of a finite observation horizon and one at a controllable delay. The moisture store drains exponentially. Its cumulative response is assumed to be a cooperative, Hill-exponent-two saturating function of the current store. The globally optimal delay is characterized for every positive parameter value.

Let \(a=R/K\), where \(R\) is each input size and \(K\) is the half-response concentration. If \(a\le1/\sqrt2\), both inputs should be simultaneous for every finite horizon. If \(a>1/\sqrt2\), define

\[
T_c=\frac{1}{2k}\log\frac{14a^2+2}{2a^2-1}.
\]

The unique optimizer is simultaneous for \(T\le T_c\) and has a strictly positive delay for \(T>T_c\). In the latter regime, let \(q=e^{-kT}\), and define

\[
D_a(x)=a^2(3x^3+6x^2+4x+1)+x+1,\qquad
N_a(x)=x^3[a^2x(x+1)-1].
\]

The unique optimizer is \(\tau_*=-k^{-1}\log x_*\), where \(x_*\in(0,1)\) is the unique solution of \(N_a(x_*)=q^2D_a(x_*)\) with \(x_*>\rho_a\), for

\[
\rho_a=\frac{\sqrt{1+4/a^2}-1}{2}.
\]

In fact \(q<x_*<1\). The optimal delay increases strictly with the horizon and approaches the finite limit \(-k^{-1}\log\rho_a\). For equal input and half-response scales (\(a=1\)), this gives \(kT_c=\log4\) and \(\lim_{T\to\infty}k\tau_* = \log((1+\sqrt5)/2)\).

## Assumptions and scope

Every parameter \(R,K,k,T\) is strictly positive, and the second input time obeys \(0\le\tau\le T\). The scalar store is initially empty, jumps upward by \(R\) at times zero and \(\tau\), and otherwise obeys \(\dot M=-kM\). Simultaneous inputs therefore give one jump of size \(2R\). The closed-form score and controls are

\[
M_\tau(t)=Re^{-kt}+R\mathbf1_{t\ge\tau}e^{-k(t-\tau)},\qquad
J_T(\tau)=\int_0^T\frac{M_\tau(t)^2}{K^2+M_\tau(t)^2}\,dt.
\]

The exponent two represents a *postulated* cooperative threshold-response curve; it is neither estimated from the cited field experiments nor asserted to fit a particular plant species. This is a deterministic finite-horizon scheduling theorem, not a stochastic rainfall process or a water-balance simulation.

## Proof

**1. Exact integral.** Put \(x=e^{-k\tau}\in[q,1]\) and \(q=e^{-kT}\in(0,1)\). On the first interval the normalized store is \(ae^{-kt}\); on the second it is \(a(1+x^{-1})e^{-kt}\). Because an antiderivative of \((ce^{-kt})^2/(1+(ce^{-kt})^2)\) equals \(-(2k)^{-1}\log(1+c^2e^{-2kt})\),

\[
2kJ_T(\tau)=H_{a,q}(x)
=\log(1+a^2)-\log(1+a^2x^2)
+\log(1+a^2(1+x)^2)
-\log(1+a^2q^2(1+x^{-1})^2).
\]

**2. Exact derivative and its sign.** Direct differentiation and expansion give

\[
H'_{a,q}(x)=
\frac{2a^2\bigl(q^2D_a(x)-N_a(x)\bigr)}
{x(1+a^2x^2)(1+a^2(1+x)^2)(x^2+a^2q^2(1+x)^2)}.
\]

Every factor in the denominator is positive. At the lower domain endpoint \(x=q\),

\[
q^2D_a(q)-N_a(q)
=q^2(2q+1)\bigl[1+a^2(q+1)^2\bigr]>0.
\]

**3. Weak-pulse regime.** If \(a^2\le1/2\), then \(a^2x(x+1)\le2a^2\le1\) for all \(0<x\le1\). Thus \(N_a(x)\le0\) and \(H'>0\) throughout \([q,1]\). There is precisely one maximum, at \(x=1\), corresponding to \(\tau=0\).

**4. Strong-pulse regime and uniqueness.** If \(a^2>1/2\), the polynomial \(g(x)=a^2x(x+1)-1\) has exactly one positive zero \(\rho_a\in(0,1)\). The numerator \(N_a(x)=x^3g(x)\) is negative for \(x<\rho_a\), zero at \(\rho_a\), and positive for \(x>\rho_a\). On \((\rho_a,1]\), the ratio \(F_a(x)=N_a(x)/D_a(x)\) increases **strictly**: here \(xN'_a/N_a=3+xg'/g>3\); whereas \(D_a\) has strictly positive coefficients only of degrees zero through three, so \(0<xD'_a/D_a<3\). Therefore \(xF'_a/F_a>0\). It follows that \(q^2D_a-N_a\) can change sign at most once, and only from positive to negative as \(x\) increases. Since \(H'(q)>0\), an interior stationary point, if present, is automatically the **unique global maximum**.

At the right endpoint,

\[
F_a(1)=\frac{2a^2-1}{14a^2+2}=:q_c^2.
\]

If \(q\ge q_c\), the derivative is positive in the interior and at worst zero at \(x=1\); hence \(x=1\) is uniquely optimal. If \(q<q_c\), the derivative starts positive at \(x=q\) and is negative at \(x=1\). A unique interior maximizing root \(x_*\in(\max\{q,\rho_a\},1)\) exists. The inequality \(q<q_c\) is equivalent to \(T>T_c\), proving the exact transition, including equality cases.

**5. Horizon monotonicity and sharp infinite-time boundary.** For \(T>T_c\), the optimizer satisfies \(F_a(x_*)=q^2\). The positive function \(F_a\) is strictly increasing, while \(q^2=e^{-2kT}\) decreases strictly as \(T\) grows. Hence \(x_*\) decreases and \(\tau_*=-k^{-1}\log x_*\) increases strictly. As \(T\to\infty\), \(q^2\downarrow0\), forcing \(x_*\downarrow\rho_a\), so the limit is finite and positive. When \(a=1\), \(\rho_1=(\sqrt5-1)/2\) and \(q_c=1/4\), establishing the displayed golden-ratio limit and \(kT_c=\log4\).

This derivative proof covers all real positive parameters and every allowed delay; no finite grid search is used to certify uniqueness.

## Verification

A standalone supplementary file `check.py` recomputes the symbolic derivative identity using SymPy; compares exact integration with numerical quadrature over 1,500 generated parameter cases; compares the proved optimizer with a numerical scalar optimizer over 1,500 cases; and tests 6,000 additional candidate delays. It also checks the \(a=1\) threshold and limiting lag numerically. The executable prints `PASS 7500 quadratures and optimization comparisons` when successful. These computations are supplementary evidence, not a proof of universal statements. Run `python check.py` with Python, SymPy and SciPy installed.

For example, with \(a=k=1\), the exact threshold is \(T_c=\log4\); at \(T=2\), numerical evaluation gives \(\tau_*\approx0.2353562\), improving the cumulative normalized score from approximately \(0.7693674\) to \(0.7771920\).

## Relationship to prior work

Ma and collaborators (posted 22 May 2024) investigate physiological and soil-water-potential responses to real rainfall pulses with different magnitudes and durations. Feldman and collaborators (2021) measure pulse-dependent plant rehydration and growth timescales, while Ogle and Reynolds (2004) place pulses, thresholds and delayed responses within a dryland ecological modeling framework. These works motivate the timing question, but their inspected formulations do not derive the stated two-equal-pulse, Hill-exponent-two finite-horizon optimization theorem. In mathematical terms, this is a cooperative saturation response under a controllable second *input time*, rather than a field-calibrated hydraulic model. Similar single-pulse response effects and general schedule dependence do not imply the dual thresholds and unique global optimizer without an additional derivation.

## Limitations

The store is linear and has no depletion by plant uptake, infiltration delay, evaporation nonlinearities, storage cap, background moisture, rainfall stochasticity, or biological feedback. Both pulse sizes are fixed and equal; it does not optimize pulse doses. A cooperative Hill response with exponent two is stipulated, not empirically fitted. Cumulative response is a proxy and does not directly predict plant survival, yield, or ecosystem management outcomes. The literature comparison does not establish exhaustive historical priority. No independent external audit has been performed.

## References

1. Ma, Y. et al., *Responses of Soil Water Potential and Plant Physiological Status to Pulsed Rainfall Events in Arid Northwestern China: Implications for Disclosing the Water-use Strategies of Desert Plants*. Research Square preprint, posted 22 May 2024, DOI: https://doi.org/10.21203/rs.3.rs-4096548/v1. A later journal version appeared 30 October 2024, DOI: https://doi.org/10.1002/eco.2728.
2. Feldman, A. F. et al., *Patterns of plant rehydration and growth following pulses of soil moisture availability*. Biogeosciences 18 (2021), 831–847, https://doi.org/10.5194/bg-18-831-2021.
3. Ogle, K. and Reynolds, J. F., *Plant responses to precipitation in desert ecosystems: integrating functional types, pulses, thresholds, and delays*. Oecologia 141 (2004), 282–294, https://doi.org/10.1007/s00442-004-1507-5.
4. Wright, D. F. B., Winter, H. R. and Duffull, S. B., *Understanding the time course of pharmacological effect: a PKPD approach*. British Journal of Clinical Pharmacology 72 (2011), https://doi.org/10.1111/j.1365-2125.2011.03925.x. A mathematical comparison for nonlinear response scheduling, not ecological evidence.
