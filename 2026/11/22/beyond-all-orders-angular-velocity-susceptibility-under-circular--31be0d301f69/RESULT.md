# Beyond-all-orders angular-velocity susceptibility under circular resetting

## Finding
Consider a two-temperature Brownian gyrator with independent rate-\(r\) Poisson resets to a point chosen uniformly on a circle of radius \(R>0\). For stable coupling \(|u|<1\), put
\[
 d\begin{pmatrix}X_t\\Y_t\end{pmatrix}=-\begin{pmatrix}1&u\\u&1\end{pmatrix}\begin{pmatrix}X_t\\Y_t\end{pmatrix}dt+\begin{pmatrix}\sqrt{2T_x}&0\\0&\sqrt{2T_y}\end{pmatrix}d\begin{pmatrix}B^x_t\\B^y_t\end{pmatrix},
\]
between resets, with \(T_x,T_y>0\). Reset jumps are not included when evaluating the noise-conditional continuous-flight angular velocity
\[
 \overline{\mathcal W}_r(u)=u\,\mathbb E_{r,u}\frac{Y^2-X^2}{X^2+Y^2}.
\]
The susceptibility \(\chi(r)=\lim_{u\to0}\overline{\mathcal W}_r(u)/u\) exists for every \(r>0\). If \(T_x=T_y\), it vanishes identically. Otherwise put \(T_+=\max(T_x,T_y)\), \(T_-=\min(T_x,T_y)\). Then \(\operatorname{sgn}\chi(r)=\operatorname{sgn}(T_y-T_x)\) for every \(r>0\), and the following *sharp* strong-reset asymptotic holds:
\[
\boxed{\displaystyle
\chi(r)\sim\operatorname{sgn}(T_y-T_x)\,
\frac{2T_+}{R\sqrt{T_+-T_-}}
\exp\!\left(\frac{R^2}{4T_+}\right)
\frac{\exp[-R\sqrt{r/T_+}]}{\sqrt r}\qquad(r\to\infty).
}
\]
In contrast, the weak-coupling susceptibility of the mean continuous-flight angular momentum is exactly
\[
 \lim_{u\to0}\frac{\overline{\mathcal L}_r(u)}u
 =\frac{2(T_y-T_x)}{r+2}.
\]
Thus the circular-reset angular *velocity* susceptibility is smaller than every algebraic power of \(r^{-1}\), even while the angular *momentum* susceptibility is of order \(r^{-1}\). The result concerns the order of limits \(u\to0\) followed by \(r\to\infty\), not a fixed nonzero coupling.

## Assumptions and scope
The driving Brownian motions are independent, reset marks are independent uniform angles, Poisson resetting is independent of the Brownian noise, and the stationary process is sampled at an arbitrary time. The noise-averaged velocity follows the forward/Itô discretization, excluding instantaneous reset chords. All asymptotics hold for each **fixed** \(R>0\) and distinct positive temperatures; no uniformity as \(R\downarrow0\) or \(T_x\to T_y\) is asserted. Time and harmonic relaxation are normalized so that the diagonal drift coefficient equals one.

We write \(I_1\) for the modified Bessel function of the first kind of order one. A more general coupling may be used before taking \(u\to0\), as long as \(|u|<1\) so the no-reset harmonic drift is stable. The stationary process exists with the stated parameters.

## Proof
**1. Renewal and weak-coupling reduction.** At stationarity the time \(s>0\) since the previous reset has density \(r e^{-rs}\). At \(u=0\), conditionally on \(s\),
\[
 (X,Y)=(a_s\cos\Theta,a_s\sin\Theta)+(Z_x,Z_y),\qquad
 a_s=Re^{-s},\quad
 Z_i\sim N(0,v_i(s)),\quad
 v_i(s)=T_i(1-e^{-2s}),
\]
where \(\Theta\) is uniform on \([0,2\pi)\) and all variables in this display are independent. The bounded ratio \((Y^2-X^2)/(X^2+Y^2)\) is defined arbitrarily at the origin, a null-probability event. Continuity of the Gaussian propagators in \(u\) and dominated convergence therefore give
\[
 \chi(r)=r\int_0^\infty e^{-rs}A(s)\,ds,\qquad
 A(s)=\mathbb E\frac{Y^2-X^2}{X^2+Y^2}\ \bigg|\ \text{reset age }s,\ u=0.
\]
The expression for \(\overline{\mathcal W}_r(u)\) is the continuous-flight conditional-drift identity in the cited primary gyrator study; its finite-time white-noise terms have mean zero.

**2. Exact circular-angle erasure.** For every \(a>0\) and complex displacement \(z\), the contour identity
\[
 \frac1{2\pi}\int_0^{2\pi}
 \frac{ae^{i\theta}+z}{ae^{-i\theta}+\bar z}\,d\theta
 =\begin{cases}
 0,&|z|\le a,\\
 (1-a^2/|z|^2)\,z/\bar z,&|z|>a
 \end{cases}
\]
holds, with the boundary interpreted by continuity. Indeed, substituting \(w=e^{i\theta}\) converts the angular mean into the contour integral of \((aw+z)/(a+\bar z w)\,dw/(2\pi i)\); it has a pole inside the unit circle exactly when \(|z|>a\), with the displayed residue. Taking negative real parts gives
\[
 A(s)=\mathbb E\left[
 \frac{Z_y^2-Z_x^2}{Z_x^2+Z_y^2}
 \left(1-\frac{a_s^2}{Z_x^2+Z_y^2}\right)_+\right].
\]
In particular, all Gaussian displacements *inside* the reset circle contribute exactly zero to this angular harmonic; only the Gaussian tail crossing the circle is retained. This is stronger than merely vanishing of a finite list of inverse-rate expansion coefficients.

**3. Exact Bessel representation and sign.** Set
\[
 h_s=\tfrac14(v_x(s)^{-1}+v_y(s)^{-1}),\qquad
 b_s=\tfrac14|v_x(s)^{-1}-v_y(s)^{-1}|.
\]
Polar integration of the centered anisotropic Gaussian density, using \(\int_0^{2\pi}e^{z\cos2\phi}\cos2\phi\,d\phi=2\pi I_1(z)\), yields
\[
 \boxed{\displaystyle A(s)=\frac{\operatorname{sgn}(T_y-T_x)}{\sqrt{v_x(s)v_y(s)}}
 \int_{a_s}^{\infty}\rho\left(1-\frac{a_s^2}{\rho^2}\right)
 e^{-h_s\rho^2}I_1(b_s\rho^2)\,d\rho.}
\]
If the temperatures coincide, \(b_s=0\) and \(I_1(0)=0\). If they differ, every factor in the radial integrand is strictly positive for \(\rho>a_s\); hence the sign statement, including the absence of finite-rate sign reversals.

**4. Sharp small-age tail.** Suppose \(T_y>T_x\); exchanging axes gives the opposite sign in the other case. Set \(v_+=v_y(s)\), \(v_-=v_x(s)\). Since \(b_s a_s^2\to\infty\) as \(s\downarrow0\), the uniform large-argument expansion \(I_1(z)\sim e^z/\sqrt{2\pi z}\), combined with a one-sided Laplace expansion at \(\rho=a_s\), gives
\[
 A(s)\sim \frac{2\sqrt{2/\pi}\,v_+(s)^2}{a_s^3\sqrt{v_+(s)-v_-(s)}}
 \exp\!\left[-\frac{a_s^2}{2v_+(s)}\right].
\]
To check the endpoint constant, note that \(h_s-b_s=1/(2v_+)\), and the remaining endpoint integral is
\[
 \int_{a_s}^\infty \left(1-\frac{a_s^2}{\rho^2}\right)
 e^{-\rho^2/(2v_+)}d\rho
 \sim\frac{2v_+^2}{a_s^3}e^{-a_s^2/(2v_+)}.
\]
Uniformity can be justified by splitting the radial integral at \(\rho=a_s+M v_+/a_s\), taking \(s\downarrow0\) first, and then \(M\to\infty\); the excluded tail is exponentially small in \(M\) relative to the displayed main term. Since
\[
 \frac{a_s^2}{2v_+(s)}=\frac{R^2}{2T_y(e^{2s}-1)}
 =\frac{R^2}{4T_y s}-\frac{R^2}{4T_y}+O(s),
\]
we obtain, with \(c=R^2/(4T_y)\),
\[
 A(s)\sim \frac{8T_y^2e^{c}}{R^3\sqrt{\pi(T_y-T_x)}}
 s^{3/2}e^{-c/s}.
\]
The same statement with an overall negative sign and \(T_+\) in place of \(T_y\) holds if \(T_x>T_y\).

**5. Laplace saddle and leading constant.** The dominant reset ages satisfy \(s\asymp\sqrt{c/r}\). Contributions from ages bounded away from zero are \(O(e^{-r\varepsilon})\), negligible on the displayed scale. The standard positive Laplace integral is
\[
 \int_0^\infty s^{3/2}e^{-rs-c/s}\,ds
 =2(c/r)^{5/4}K_{5/2}(2\sqrt{cr})
 \sim\sqrt\pi\,c\,r^{-3/2}e^{-2\sqrt{cr}}.
\]
Insert the small-age equivalent into the renewal integral, use saddle localization, and simplify \(2\sqrt{cr}=R\sqrt{r/T_+}\). This gives exactly the announced \(r^{-1/2}\) prefactor and exponent. The same derivation shows why a formal Taylor expansion of the angular observable around the reset circle would miss the entire effect.

**6. Contrast with angular momentum.** At \(u=0\), angular averaging gives \(\mathbb E[Y^2-X^2\mid s]=(T_y-T_x)(1-e^{-2s})\). Integration against \(re^{-rs}\) gives \(2(T_y-T_x)/(r+2)\). Since the continuous-flight mean angular momentum is \(u\mathbb E(Y^2-X^2)\), taking its weak-coupling limit proves the comparison.

## Verification
The standalone numerical checker is `checks/verify.py` (Python with NumPy/SciPy); run `python checks/verify.py` from the directory containing this file. It checks the contour identity directly against angular trapezoidal integration, compares the Bessel representation against an independent polar Gaussian integral at several positive ages, tests exchange symmetry and temperature equality, and compares the exact renewal-Bessel quadrature with the complete asymptotic (including its exponential prefactor) up to reset rate \(200000\). These finite checks support, but do not substitute for, the analytic proof.

## Relationship to prior work
Majumdar, Schehr, Viot and Oshanin (arXiv:2611.06322, 2026) derive the full Brownian-gyrator renewal propagator, exact angular-momentum formula for circular resetting and a double integral for mean angular velocity. Their work supplies the model and conditional-drift normalization. The present result does **not** claim those formulas; it supplies an exact cancellation mechanism and the sharp singular, weak-coupling, high-reset asymptotic with its prefactor, together with an explicit distinction between momentum and angular velocity. Chaki, Olsen and Löwen (arXiv:2406.17550, 2024) treat other spatial/orientational resetting protocols for anisotropic colloids. Singh, Górska and Sandev (Phys. Rev. E 105, 064133, 2022) provide a broader framework for renewal resetting. A general renewal representation does not itself supply the angular contour cancellation or sharp rare-event saddle.

## Limitations
The statement concerns the linear susceptibility at \(u=0\) and does not imply the same asymptotic for a fixed nonzero coupling. Temperature equality is a singular boundary for the prefactor; no uniform double limit is proved. The limit \(R\downarrow0\) is excluded. The angular velocity excludes reset-jump impulses. Although the explicit asymptotic was not identified in inspected sources, unindexed or implicitly equivalent prior work is possible, without a full-literature uniqueness guarantee. The exact Bessel representation is an integral rather than a closed elementary finite-rate expression.

## References
1. S. N. Majumdar, G. Schehr, P. Viot and G. Oshanin, *Brownian gyrator model with stochastic resetting*, arXiv:2611.06322v1 (first publicly submitted 2026-11-04), https://arxiv.org/abs/2611.06322 . In particular, their circular-reset angular momentum and mean angular-velocity representations.
2. S. Chaki, K. S. Olsen and H. Löwen, *Anisotropic Brownian particles under resetting*, arXiv:2406.17550v1 (2024), https://arxiv.org/abs/2406.17550 .
3. R. K. Singh, K. Górska and T. Sandev, *General approach to stochastic resetting*, Phys. Rev. E **105**, 064133 (2022), https://doi.org/10.1103/PhysRevE.105.064133 .
