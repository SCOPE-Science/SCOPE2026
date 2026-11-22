# Every-harmonic phase sensitivity under two-level periodic lake reoxygenation

## Finding
Consider a periodically mixed, spatially aggregated oxygen store whose reoxygenation rate alternates strictly between two positive values, while oxygen demand contains one freely phase-shifted harmonic. **For every positive harmonic number, every nondegenerate duty cycle, and every strict rate contrast, the period-mean oxygen is a nonconstant sinusoid of demand phase**. It has exactly one minimum and one maximum modulo a full cycle, separated by half a cycle. The entire positive gap is determined by an explicit Fourier coefficient that can never vanish.

In particular, at 50% high-mixing duty the *wind/mixing rate itself* has zero even Fourier harmonics, but **all even harmonics of the effective oxygen-residence response are nonzero**: a semidiurnal demand can change mean oxygen even when the idealized mixing signal contains no semidiurnal harmonic. This is a theorem for the stipulated reduced model, not an assertion about measured lake oxygen.

## Assumptions and scope
Let \(T>0\), \(0<h<T\), \(m_H>m_L>0\), integer \(n\ge1\), and \(\nu=2\pi n/T\). Define \(m(t+T)=m(t)\) with \(m(t)=m_H\) for \(0\le t<h\), and \(m(t)=m_L\) for \(h\le t<T\). Let \(C>(r_0+r_1)/m_L\), \(r_0>r_1>0\), and \(\phi\in\mathbb R\). The idealized bottom-layer oxygen proxy obeys

\[
\dot O_\phi(t)=m(t)\bigl(C-O_\phi(t)\bigr)-\bigl[r_0+r_1\cos(\nu t+\phi)\bigr].
\]

Here \(C\) is a constant oxygen supply level, \(m\) is an effective replenishment rate and the bracketed term is oxygen demand. The positive constraint on \(C\) keeps the unique periodic oxygen solution strictly positive; the dynamics are linear and do not include concentration-limited respiration, stratification, or spatial transport. Let \(\overline O_\phi=T^{-1}\int_0^T O_\phi(t)\,dt\) denote its period mean.

For an exact response formula set

\[
E_H=e^{-m_Hh},\quad E_L=e^{-m_L(T-h)},\quad
\Delta=\frac{m_L^{-1}-m_H^{-1}}{1-E_HE_L}>0,
\]

\[
R=m_Hm_L(1-E_HE_L),\quad
\nu_u=m_H(1-E_L)+m_LE_L(1-E_H),\quad
\nu_v=m_HE_H(1-E_L)+m_L(1-E_H),
\]

where the subscripts on \(\nu_u,\nu_v\) are merely labels (the harmonic angular frequency is \(\nu\)). Set \(z=e^{i\nu h}\) and define

\[
W_n=-\frac{\Delta\{z(R+i\nu\nu_u)-(R+i\nu\nu_v)\}}{i\nu T(m_H+i\nu)(m_L+i\nu)}.
\]

Then \(W_n\ne0\), and for the unique periodic solution

\[
\overline O_\phi=C-r_0\overline w-r_1\operatorname{Re}(e^{i\phi}W_n),
\]

where \(\overline w\) is the explicit positive period mean given below, independent of demand phase. Consequently, the unique minimizing phase is \(\phi_{\min}=-\arg W_n\pmod{2\pi}\), the unique maximizing phase is \(\phi_{\max}=\phi_{\min}+\pi\pmod{2\pi}\), and

\[
\max_\phi\overline O_\phi-\min_\phi\overline O_\phi=2r_1|W_n|>0.
\]

The conclusion holds simultaneously for every integer \(n\ge1\), including arbitrarily large harmonics; no uniform positive lower bound independent of \(n\) is claimed.

## Proof
Writing \(x=C-O\) gives the deficit equation \(\dot x=r(t)-m(t)x\). Its one-period homogeneous multiplier is \(E_HE_L\in(0,1)\), so it has a unique globally attracting periodic solution. Positive demand gives positive deficit. Since \(r(t)<m_LC\), the constant barrier \(x=C\) points strictly inward, hence the periodic oxygen concentration is positive.

Define \(w\) as the unique periodic solution of the adjoint equation \(\dot w=m(t)w-1\), equivalently

\[
w(t)=\int_t^\infty\exp\!\left(-\int_t^s m(q)\,dq\right)\,ds.
\]

The formula shows that \(w\) is positive, and periodicity follows from periodic \(m\). The identity \((wx)'=wr-x\) implies, by integration over a period, \(\overline x=T^{-1}\int_0^T w(t)r(t)\,dt\). Therefore a single harmonic in demand makes \(\overline x=r_0\overline w+r_1\operatorname{Re}(e^{i\phi}W_n)\) with \(W_n=T^{-1}\int_0^T w(t)e^{i\nu t}\,dt\).

Let \(w_h=m_H^{-1}+\Delta(1-E_L)\) and \(w_0=m_H^{-1}+E_H\Delta(1-E_L)\). Direct backward integration of the adjoint equation yields

\[
w(t)=\begin{cases}
m_H^{-1}+(w_h-m_H^{-1})e^{-m_H(h-t)},&0\le t\le h,\\
m_L^{-1}+(w_0-m_L^{-1})e^{-m_L(T-t)},&h\le t\le T.
\end{cases}
\]

Both expressions join continuously and periodically, since \(w_0-m_L^{-1}=-\Delta(1-E_H)\). Integrating them gives an independently reproducible expression

\[
\overline w=\frac{h/m_H+(T-h)/m_L+\Delta(1-E_H)(1-E_L)(m_H^{-1}-m_L^{-1})}{T}.
\]

Indeed the exponential correction in the first segment is \(\Delta(1-E_L)(1-E_H)/m_H\) and in the second segment it is \(-\Delta(1-E_H)(1-E_L)/m_L\).

For any \(\nu=2\pi n/T\ne0\), the boundary term in integration by parts vanishes and \(i\nu T W_n=-\int_0^T w'(t)e^{i\nu t}\,dt\). Substituting the displayed exponential pieces and combining fractions produces precisely the formula for \(W_n\) above. A key strict factorization is

\[
\nu_u-\nu_v=(m_H-m_L)(1-E_H)(1-E_L)>0.
\]

If \(W_n=0\), the formula would force \(z=(R+i\nu\nu_v)/(R+i\nu\nu_u)\). Because \(R>0\), \(0<\nu_v<\nu_u\), and \(\nu>0\), the right-hand side has modulus strictly smaller than one, contrary to \(|z|=1\). Thus \(W_n\ne0\) for every positive integer \(n\). Maximization/minimization of the resulting nonconstant sinusoid gives the stated phase classification and strict gap.

At equal duty \(h=T/2\), every even \(n\) satisfies \(z=1\). The coefficient reduces to

\[
W_n=-\frac{\Delta(\nu_u-\nu_v)}{T(m_H+i\nu)(m_L+i\nu)}\ne0.
\]

By contrast the corresponding complex Fourier coefficient of the raw two-level mixing signal is \((m_H-m_L)(z-1)/(i\nu T)=0\). The nonlinear dependence of the *memory kernel* on mixing therefore generates phase sensitivity where direct harmonic matching would predict none. This proves the final assertion.

## Verification
A standalone standard-library script `CHECK.py` evaluates exact segment solutions, Fourier coefficients, the mean-deficit identity, period closure and equal-duty even harmonics. It passed 1,110 deterministic diagnostic assertions, including 220 independent random positive parameter sets and five equal-duty even-harmonic cases. These numerical tests corroborate formulas; the universal nonvanishing statement follows from the strict modulus contradiction in the proof, not from finite sampling.

For \(T=2\), \(h=1\), \(m_H=2\), \(m_L=1\), \(n=2\), \(r_0=1\), \(r_1=1/2\), and \(C=3\), the model gives \(W_2\approx0.003062321017609+0.001540176852728i\). Despite exactly zero second Fourier coefficient of the mixing rate, the max-minus-min period-mean oxygen gap is \(2r_1|W_2|\approx0.003427820700178\). This example is dimensionless and does not estimate the oxygen level of any particular lake.

## Relationship to prior work
Shinohara et al. (2023) use field measurements and a spatial diffusion/convection model to demonstrate the joint influence of weak winds and heat-wave forcing on shallow-lake bottom oxygen. Their model motivates distinguishing time-varying replenishment from oxygen demand; the present two-regime scalar equation is a deliberately reduced and uncalibrated benchmark, not a theorem about their numerical model. Holgerson, Zappa and Raymond (2016) document short convective reoxygenation episodes in ponds. Schwefel et al. (2023) analyze measured oxygen depletion and convection in seasonally ice-covered lakes. Lorke et al. (2003) document periodic turbulent transport and a phase lag in sediment oxygen fluxes. These works establish physical motivation and timing effects, but the inspected available texts did not supply the all-harmonic nonvanishing law for the switched scalar replenishment equation.

The Fourier and variation-of-constants steps used in the proof are classical. The distinctive assertion being assessed is the strict *all-harmonic* noncancellation despite a two-level rate schedule, including suppressed even harmonics at equal duty. General linear-system Fourier theory alone does not assert that individual coefficients must be nonzero; the explicit strict modulus inequality establishes it for this specific model.

## Limitations
The model assumes one well-mixed oxygen store, constant saturation level, constant positive demand baseline, additive harmonic respiration and exactly two replenishment rates with sharp switching. It omits realistic photosynthesis, nonlinear sediment oxygen demand, vertical stratification and uncertain drivers. The spectral effect concerns phase dependence of the *period mean*, not the threshold-crossing duration of hypoxia. An observational oxygen response may depart substantially from this benchmark. The originality assessment relies on accessible literature and published mathematical record comparisons, not a comprehensive historical priority determination. No external independent audit has been performed.

## References
1. Shinohara, R., et al. (2023). "Heat Waves Can Cause Hypoxia in Shallow Lakes." *Geophysical Research Letters* 50, e2023GL102967. First published 2023-04-16. https://doi.org/10.1029/2023GL102967
2. Holgerson, M. A., Zappa, C. J., and Raymond, P. A. (2016). "Substantial overnight reaeration by convective cooling discovered in pond ecosystems." *Geophysical Research Letters* 43, 8044–8051. https://doi.org/10.1002/2016GL070206
3. Schwefel, R., et al. (2023). "Oxygen depletion and sediment respiration in ice-covered arctic lakes." *Limnology and Oceanography* 68, 1470–1489. https://doi.org/10.1002/lno.12357
4. Lorke, A., Müller, B., Maerki, M., and Wüest, A. (2003). "Breathing sediments: The control of diffusive transport across the sediment–water interface by periodic boundary-layer turbulence." *Limnology and Oceanography* 48, 2077–2085. https://doi.org/10.4319/lo.2003.48.6.2077
