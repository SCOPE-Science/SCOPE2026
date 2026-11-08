# Cubic twist–occupation law at saturation grazing and the complete resonant-circle spectrum

## Finding

For the unforced saturated oscillator studied in the forced setting by Ortega and Schliessauf, the first excursion beyond the saturation threshold produces **two different nonanalytic exponents**: the fraction of physical time spent in saturation grows as the square root of excess energy, whereas the full oscillation period changes only as its three-halves power. Their ratio has an exact, parameter-dependent cubic limit. Above the threshold the period is strictly increasing, so every rational stroboscopic rotation number in the permitted open interval corresponds to exactly one energy circle, with an explicit two-thirds-power grazing localization law. The statements concern original physical time, rather than a normal-form time reparametrization.

Precisely, for each integer \(m\ge1\), define \(h(x)=\max\{-1,\min\{x,1\}\}\) and consider
\[
\ddot x+m^2x+h(x)=0.
\]
Put \(\Omega=\sqrt{m^2+1}\) and \(E_c=\Omega^2/2\). The conserved energy is
\[
E=\tfrac12\dot x^2+U(x),\qquad
U(x)=\begin{cases}\Omega^2x^2/2,&|x|\le1,\\m^2x^2/2+|x|-1/2,&|x|\ge1.\end{cases}
\]
For each \(E>0\), let \(T(E)\) be the minimal physical period, and let \(\Theta(E)\) be the proportion of that period with \(|x(t)|>1\). Set \(s=\sqrt{2(E-E_c)}\) when \(E>E_c\). Then
\[
T(E)=\begin{cases}2\pi/\Omega,&0<E\le E_c,\\
4\left[\frac1\Omega\arctan\left(\frac\Omega s\right)+\frac1m\arctan\left(\frac{ms}{\Omega^2}\right)\right],&E>E_c,\end{cases}
\]
and, for \(E>E_c\),
\[
\Theta(E)=\frac{\frac1m\arctan(ms/\Omega^2)}{\frac1\Omega\arctan(\Omega/s)+\frac1m\arctan(ms/\Omega^2)};
\qquad \Theta(E)=0\quad(0<E\le E_c).
\]
The exact twist derivative for \(E>E_c\) is
\[
T'(E)=\frac{4s}{(s^2+\Omega^2)(m^2s^2+\Omega^4)}>0.
\]
At grazing, writing \(\delta=E-E_c\downarrow0\),
\[
T(E)-\frac{2\pi}{\Omega}=\frac{8\sqrt2}{3\Omega^6}\,\delta^{3/2}+O(\delta^{5/2}),\qquad
\Theta(E)=\frac{2\sqrt2}{\pi\Omega}\,\delta^{1/2}+O(\delta^{3/2}),
\]
so the sharp invariant relation is
\[
\boxed{\lim_{E\downarrow E_c}\frac{T(E)-2\pi/\Omega}{\Theta(E)^3}=\frac{\pi^3}{6\Omega^3}.}
\]
In particular, \(T\) is globally \(C^1\) on positive energies, but is not \(C^2\) at \(E_c\), and \(\Theta\) is continuous but not differentiable there. Their singularities are of orders three-halves and one-half respectively.

As \(E\to\infty\), \(T(E)\uparrow 2\pi/m\) and
\[
\frac{2\pi}{m}-T(E)=\frac4{m^2s}+O(s^{-3}),\qquad 1-\Theta(E)=\frac{2m}{\pi s}+O(s^{-2}).
\]
The frequency \(\rho(E)=2\pi/T(E)\) is strictly decreasing from \(\Omega\) to \(m\) on \(E>E_c\). Under the time-\(2\pi\) map, every reduced rational \(p/q\in(m,\Omega)\) (\(p,q\) positive, \(\gcd(p,q)=1\)) determines exactly one energy circle of primitive sampled period \(q\); no other outer energy circle has that rotation number. Every irrational rotation number in this interval likewise determines exactly one quasiperiodic sampled circle. The entire inner harmonic disk has the irrational sampled rotation \(\Omega\). These rational resonance circles are dense among outer energy levels but occupy zero planar area.

Their sharp localization at the endpoints is
\[
E(\rho)-E_c\sim\left(\frac{3\pi\Omega^4}{4\sqrt2}(\Omega-\rho)\right)^{2/3}\quad(\rho\uparrow\Omega),
\qquad E(\rho)\sim\frac{2}{\pi^2(\rho-m)^2}\quad(\rho\downarrow m).
\]

## Assumptions and scope

The model is **unforced** (\(p(t)\equiv0\)) and has the specific continuous saturated restoring force \(h\) above. The parameter \(m\) is an integer at least one, matching the resonance convention of the originating paper. All energies are strictly positive; the equilibrium at \(E=0\) does not have a minimal period. A grazing orbit at \(E=E_c\) touches \(|x|=1\) but spends zero physical time beyond it. The oscillation is a uniquely defined periodic motion because the restoring force is globally Lipschitz and the strictly increasing potential tends to infinity. Both sign branches are included and time spent outside saturation is measured with Lebesgue measure in original time.

A sampled circle's primitive period means that of the time-\(2\pi\) Poincaré/stroboscopic transformation on that circle, not the minimal continuous-time oscillation period. The origin is excluded from statements about sampled-circle rotation.

## Proof

**1. Energy geometry.** The force \(m^2x+h(x)\) is odd and strictly increasing, hence the even potential \(U\) has a unique strict minimum at the origin and tends to infinity. Every nonzero energy level is a simple closed invariant curve in the \((x,\dot x)\)-plane and has four congruent physical-time quarters from \((x,\dot x)=(0,\sqrt{2E})\) to the positive turning point. The outer branch is visited exactly when \(E>E_c=U(1)\).

**2. Exact branch flight times.** The inner branch is harmonic with angular frequency \(\Omega\). For \(E>E_c\) its outward crossing of \(x=1\) has velocity \(s=\sqrt{2(E-E_c)}\). Inner transit time from \(x=0\) to \(x=1\) is
\[
t_i=\frac{1}{\Omega}\arctan\frac{\Omega}{s}.
\]
In the positive outer branch the shifted coordinate \(z=x+1/m^2\) satisfies \(\ddot z+m^2 z=0\). At entry, \(z=\Omega^2/m^2\) and \(\dot z=s\), so the time from entry to maximum displacement is
\[
t_o=\frac1m\arctan\frac{ms}{\Omega^2}.
\]
The quarter period is \(t_i+t_o\). Reflection symmetry gives \(T=4(t_i+t_o)\) and \(\Theta=t_o/(t_i+t_o)\). At or below threshold the entire orbit is harmonic, yielding \(2\pi/\Omega\).

**3. Global strict twist and boundary regularity.** Differentiate the explicit expressions with respect to \(s\) and use \(dE/ds=s\). Cancellation of the constant terms gives
\[
\frac{dT}{ds}=\frac{4s^2}{(s^2+\Omega^2)(m^2s^2+\Omega^4)},
\]
which proves the exact positive derivative and hence strict monotonicity. In particular \(T\) lies strictly between \(2\pi/\Omega\) and \(2\pi/m\) on the outer region. The elementary identity \(\arctan(\Omega/s)=\pi/2-\arctan(s/\Omega)\) shows
\[
T(E)-\frac{2\pi}{\Omega}
=4\left[\frac{\arctan(ms/\Omega^2)}m-\frac{\arctan(s/\Omega)}\Omega\right]
=\frac{4s^3}{3\Omega^6}+O(s^5).
\]
At the same time \(t_o=s/\Omega^2+O(s^3)\) and \(t_i+t_o=\pi/(2\Omega)+O(s^3)\). Substitution of \(s=\sqrt{2\delta}\) yields both claimed boundary laws and the cubic relation. Because \(T'(E)\sim (4\sqrt2/\Omega^6)\sqrt{E-E_c}\), \(T'\) joins continuously to the zero derivative below threshold, whereas \(T''(E)\sim(2\sqrt2/\Omega^6)/\sqrt{E-E_c}\) diverges from above. The square-root law likewise precludes differentiability of \(\Theta\) at the threshold. This establishes the exact claimed regularity (but does not assert higher differentiability at other nonzero energies).

**4. High-energy edges.** Expanding \(\arctan(s/\Omega)\) and \(\arctan(ms/\Omega^2)\) at \(s=\infty\) gives \(t_i=s^{-1}+O(s^{-3})\), \(t_o=\pi/(2m)-\Omega^2/(m^2s)+O(s^{-3})\), and hence \(T=2\pi/m-4/(m^2s)+O(s^{-3})\), since \(1-\Omega^2/m^2=-1/m^2\). Taking \(t_i/(t_i+t_o)\) yields \(1-\Theta=2m/(\pi s)+O(s^{-2})\).

**5. Complete sampled resonance classification.** On any nonzero energy circle, parametrization by elapsed physical time modulo its minimal period gives a circle conjugacy of the flow to rigid uniform motion. Thus the time-\(2\pi\) sampled map has rigid rotation number \(\rho=2\pi/T\) modulo integers. On the outer annulus the exact derivative and endpoint limits give a strictly decreasing bijection \(E\mapsto\rho(E)\) onto \((m,\Omega)\). A rational value \(p/q\) in lowest terms yields primitive sampled period \(q\); an irrational value yields an irrational rotation. The inner disk has \(\rho=\Omega\), irrational because \(m^2<m^2+1<(m+1)^2\) for every positive integer \(m\). Continuity of the inverse map and density of rationals give dense outer resonances. Each energy curve has planar Lebesgue area zero, and there are only countably many rational values; their union therefore has zero area. Finally, inversion of the threshold asymptotic \(\Omega-\rho\sim 4\sqrt2\delta^{3/2}/(3\pi\Omega^4)\) yields the two-thirds-power law. At the far edge \(\rho-m\sim2/(\pi s)\), so \(E=E_c+s^2/2\sim2/[\pi^2(\rho-m)^2]\).

## Verification

`checker.py` is an independent standard-library Python check. It integrates the original piecewise-saturated second-order ODE by fourth-order Runge–Kutta up to the first positive turning point, interpolates the saturation crossing, and compares the observed physical quarter-period and saturation occupation fraction with the proposed exact expressions for 16 parameter/energy cases. It also checks strict ranges, core isochrony, the predicted fractional threshold coefficients at several scales, and the high-energy coefficient. Independent computer algebra differentiated the exact period formula and verified its cubic Taylor coefficient. These finite computations check normalization and boundary constants only; the global assertions are proved above, not inferred by enumeration.

## Relationship to prior work

Ortega and Schliessauf (public version 11 July 2022), Sections 1 and 4, study recurrence for the *forced* saturated oscillator under the Lazer–Leach condition. Their Theorem 1.1 establishes almost-everywhere Poisson stability and their Section 4 derives a high-amplitude twist map. The displayed source text does not state the energy-resolved unforced physical-time period, the two distinct grazing exponents, the cubic twist–occupation relation, or the full energy-indexed stroboscopic resonance spectrum. This result is not a new claim about the forced system. Ortega (1999) previously studied boundedness and small twist for essentially the same forced oscillator; its bibliographic abstract was checked, but the complete older text was not accessible, so an equivalent exact unforced calculation there remains a genuine priority risk.

Classical period-function monotonicity methods (e.g. Chouikha 2005 and Nascimento 2026) can establish monotonicity under separate hypotheses in broad Hamiltonian classes. Their general monotonicity question should not be confused with the exact piecewise-saturated flight-time formula and the fractional threshold/occupation law here. All harmonic flight-time identities, phase conjugacies and Taylor calculations are explicitly derived; none of those classical principles is claimed as new.

## Limitations

The statement applies only to the unforced, continuous saturation law and integer \(m\ge1\). It gives no result for nonzero periodic forcing, discontinuous signum forcing, damping, nonlinear saturation profiles, or separatrix phenomena. Numerical tests are finite. The period formula is an elementary matching calculation, and a reexpression of it may exist in classical mechanical-vibration or earlier oscillator papers not available for full-text comparison; the originality judgement is necessarily conditional on the inspected literature. No independent mathematical audit or publication-priority determination has been performed.

## References

1. R. Ortega and H. Schliessauf, *Recurrent Motions in a Piecewise Linear Oscillator*, Annales Henri Poincaré **24** (2023), 697–715, first published 11 July 2022, DOI 10.1007/s00023-022-01217-6, https://link.springer.com/article/10.1007/s00023-022-01217-6.
2. R. Ortega, *Boundedness in a Piecewise Linear Oscillator and a Variant of the Small Twist Theorem*, Proc. London Math. Soc. **79** (1999), 381–413, DOI 10.1112/S0024611599012034, https://academic.oup.com/plms/article-abstract/79/2/381/1491765 (abstract inspected; full text unavailable).
3. A. R. Chouikha, *Monotonicity of the period function for some planar differential systems. Part I: Conservative and quadratic systems*, Applicationes Mathematicae **32** (2005), 305–325, DOI 10.4064/am32-3-5.
4. F. J. S. Nascimento, *Monotonicity of the Period Function in Planar Separable Hamiltonian Systems: An Extension of Chicone’s Criterion*, Qualitative Theory of Dynamical Systems **25** (2026), article 166, DOI 10.1007/s12346-026-01595-w.
