# A sharp symmetry-breaking phase diagram for three equally sized fractions under competing exponential repair

## Finding

For three equal, instantaneous dose events at times \(0,t,T\) and a weighted difference of two linear-quadratic repair responses, the globally optimal middle-event time exhibits **exactly three regimes**: equal spacing, two asymmetric interior times, and an endpoint doublet. Define \(0<a<b\), \(A,B,T>0\), and \(r=A/B\). The timing-dependent score is

\[
G(t)=A\bigl(e^{-at}+e^{-a(T-t)}\bigr)-B\bigl(e^{-bt}+e^{-b(T-t)}\bigr),\quad 0\le t\le T.
\]

Put \(L=T/2\) and

\[
r_0=\left(\frac ba\right)^2e^{-(b-a)L},\qquad
r_1=\frac ba\frac{1-e^{-bT}}{1-e^{-aT}}.
\]

Then \(0<r_0<r_1\), and the complete global maximizer set is

1. \(\{T/2\}\) if \(0<r\le r_0\);
2. \(\{T/2-x_*,\ T/2+x_*\}\) if \(r_0<r<r_1\), with the **unique** \(x_*\in(0,L)\) solving
   \[
   r=\frac ba e^{-(b-a)L}\frac{\sinh(bx_*)}{\sinh(ax_*)};
   \]
3. \(\{0,T\}\) if \(r\ge r_1\).

At the equal-spacing transition, \(x_*\sim\sqrt{6(r/r_0-1)/(b^2-a^2)}\) as \(r\downarrow r_0\). At the other transition the interior branch reaches the endpoints continuously. With an enforced separation \(\delta\in(0,T/2)\) between adjacent events, replace the endpoint pair by \(\{\delta,T-\delta\}\), and replace \(r_1\) by the strictly smaller cutoff \(r_\delta=(b/a)e^{-(b-a)L}\sinh(b(L-\delta))/\sinh(a(L-\delta))\); the other two regimes remain unchanged.

## Assumptions and scope

Let \(d>0\) denote the common dose of each fraction. For two idealized tissue-response components \(j\in\{u,v\}\), let \(\alpha_j,\beta_j>0\) and \(\mu_j>0\), with instantaneous-fraction log damage

\[
Q_j(t)=3\alpha_jd+\beta_jd^2\left[3+2\left(e^{-\mu_jt}+e^{-\mu_j(T-t)}+e^{-\mu_jT}\right)\right].
\]

This is the classical single-exponential incomplete-repair quadratic interaction model, not a claim of new radiobiology. Fix positive preferences \(w_u,w_v\) and maximize the surrogate contrast \(w_uQ_u(t)-w_vQ_v(t)\). Assume \(\mu_u=a<b=\mu_v\), \(A=2w_u\beta_ud^2\), and \(B=2w_v\beta_vd^2\). The contrast differs from \(G(t)\) by a constant independent of \(t\), so their maximizers agree. The ordering of repair rates is conditional, not a universal statement about healthy and malignant tissue. All fractions have the same fixed dose; only the middle time is free, with first and last times anchored. Simultaneous fractions are permitted as mathematical endpoint limits; the optional separation constraint removes that idealization.

## Proof

By symmetry \(G(L+x)=G(L-x)\). For \(x\in[0,L]\), define

\[
F(x)=G(L+x)=2Ae^{-aL}\cosh(ax)-2Be^{-bL}\cosh(bx).
\]

For \(x>0\), differentiation and positive-factor extraction give

\[
F'(x)=2Ba e^{-aL}\sinh(ax)\left[r-R(x)\right],\qquad
R(x)=\frac ba e^{-(b-a)L}\frac{\sinh(bx)}{\sinh(ax)}.
\]

The map \(z\mapsto z\coth z\) is strictly increasing on \((0,\infty)\), since its derivative has the sign of \(\sinh z\cosh z-z>0\). Therefore

\[
\frac{d}{dx}\log\frac{\sinh(bx)}{\sinh(ax)}=b\coth(bx)-a\coth(ax)>0
\]

when \(b>a>0\). Consequently \(R\) strictly increases on \((0,L]\). Its continuous endpoint values satisfy \(R(0)=r_0\) by \(\sinh(cx)\sim cx\), and \(R(L)=r_1\) by elementary exponential simplification. This proves \(0<r_0<r_1\).

If \(r\le r_0\), then \(F'(x)<0\) for every \(x\in(0,L]\); the unique maximum is \(x=0\). If \(r_0<r<r_1\), strict monotonicity supplies precisely one crossing \(R(x_*)=r\), with \(F'>0\) before and \(F'<0\) after; thus \(x_*\) alone is the global maximizer on \([0,L]\), producing exactly two times under reflection. If \(r\ge r_1\), then \(F'(x)>0\) for every \(x\in(0,L)\); only \(x=L\) maximizes. The endpoint-equality cases are included because the inequalities remain strict in the open interval. This proves the full classification, not merely a stationary-point test.

The Taylor expansion \(R(x)/r_0=1+(b^2-a^2)x^2/6+O(x^4)\) gives the square-root onset. Because \(R'(L)>0\), the other branch approaches \(L\) linearly in \(r_1-r\). Under the separation constraint, simply restrict \(x\) to \([0,L-\delta]\); the identical derivative argument replaces the upper threshold by \(R(L-\delta)\), proving the constrained version.

## Verification

The accompanying standalone `checker.py` performs deterministic numerical checks of the strictly increasing cutoff function and of every regime against 81-point candidate comparisons for each of 400 parameter triples and five weight ratios. It also reproduces a worked numerical case. The checker reports **195,602 passed assertions**. These finite checks verify implementation and examples only; the universal conclusions follow from the analytical proof above.

For \(a=0.3\), \(b=1.5\), \(T=6\), \(A/B=3\), the threshold ratios are approximately \(r_0=0.683093061182\) and \(r_1=5.989428887099\). The unique positive offset is \(x_*=2.340217821317\), yielding \(t=0.659782178683\) or \(5.340217821317\). After dividing the score by \(B\), the optimum is approximately \(2.693680142431\), versus \(2.417199965367\) at equal spacing and \(2.495773254861\) at an endpoint.

## Relationship to prior work

The exponential incomplete-repair term and competing tumor/normal response objectives are well established. Yang and Xing (first published 2005-11-17) optimize general radiotherapy dose-time fractionation, rather than the stated exact equal-three-dose, fixed-endpoint contrast and all-ratio closed phase classification. Wein, Cohen, and Wu analyze dynamic dose-size optimization with interval effects; their accessible summary and 1999 working-paper record do not establish the exact statement, but the complete working paper could not be inspected. Altman and colleagues examine permutations of dose-pattern segments **within one fraction** for a single-tissue cell-kill objective, rather than this two-tissue continuous timing contrast. Bertuzzi and colleagues study weekly dose-size optimization subject to normal-tissue constraints; their general nonlinear model is related but not the present fixed-dose timing theorem. Putora and colleagues provide a complete accessible analysis of compensatory radiotherapy after treatment interruptions, including numerical preference choices, not a three-event competing exponential timing phase diagram. The 2020 Bertuzzi et al. review presents optimal **dose sizes** for arbitrarily fixed treatment lengths; it does not state the two critical timing ratios in the accessible abstract.

This is a narrowly specified, independently proved structural fact inside a known model, not a claim of priority for the repair model, for optimal radiotherapy in general, or for the general principle of symmetry breaking in competing exponential functions.

## Limitations

The score is a selected weighted **surrogate**, not tumor-control probability or normal-tissue complication probability, and its weights are not calibrated here. It ignores physical treatment-delivery constraints except an optional minimum gap, patient variability, multirate repair, dose-rate dependence, repopulation, reoxygenation, adaptation and organ-specific limits. Co-timed fractions on the boundary are mathematical idealizations. The repair-rate ordering \(a<b\) is essential; reversing it can change the preferred timing. No clinical recommendation is made. Priority against inaccessible full papers and broader optimal-timing literature is not conclusively established; independent scientific validation has not been performed.

## References

- Yang, Y., and Xing, L. (2005). *Optimization of radiotherapy dose-time fractionation with consideration of tumor specific biology*. Medical Physics 32, 3666–3677. First published 2005-11-17. https://doi.org/10.1118/1.2126167
- Wein, L. M., Cohen, J. E., and Wu, J. T. (2000). *Dynamic optimization of a linear-quadratic model with incomplete repair and volume-dependent sensitivity and repopulation*. International Journal of Radiation Oncology Biology Physics 47, 1073–1083. https://doi.org/10.1016/S0360-3016(00)00534-4. MIT working paper, June 1999: https://hdl.handle.net/1721.1/2749
- Altman, M. B., Chmura, S. J., Deasy, J. O., and Roeske, J. C. (2006). *Optimization of the temporal pattern of radiation: An IMRT based study*. International Journal of Radiation Oncology Biology Physics 66, 898–905. https://doi.org/10.1016/j.ijrobp.2006.07.002
- Bertuzzi, A., Bruni, C., Papa, F., and Sinisgalli, C. (2012, online). *Optimal solution for a cancer radiotherapy problem*. Journal of Mathematical Biology 66, 311–349. https://doi.org/10.1007/s00285-012-0512-2
- Putora, P. M., et al. (2012). *Compensability index for compensation radiotherapy after treatment interruptions*. Radiation Oncology 7, 208. https://doi.org/10.1186/1748-717X-7-208
- Bertuzzi, A., Conte, F., Papa, F., and Sinisgalli, C. (2020). *Applications of Nonlinear Programming to the Optimization of Fractionated Protocols in Cancer Radiotherapy*. Information 11, 313. https://doi.org/10.3390/info11060313
