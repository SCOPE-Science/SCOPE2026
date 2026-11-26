# Universal Hopf-period softening and predator-mean reversal in a strong-Allee predator–prey model

## Finding

For every fixed \(0<a<1\) and \(\varepsilon>0\), set
\[
\phi_H=\frac1{2-a},\qquad
\omega_H=\frac{1-a}{\sqrt{\varepsilon(2-a)}},\qquad
\Delta=\phi_H-\phi.
\]
In the frozen predator–prey model defined below, a **nondegenerate supercritical Hopf bifurcation** occurs at \(\phi=\phi_H\). For each sufficiently small positive \(\Delta\), there is one small positive periodic orbit near coexistence, unique among sufficiently small cycles and orbitally asymptotically stable. In the dimensionless slow time \(\tau\), its fundamental prey amplitude is
\[
A_u=(2-a)\sqrt{2\Delta}+O(\Delta).
\]
Its frequency is
\[
\Omega(\Delta)=\omega_H-C(a,\varepsilon)\Delta+O(\Delta^2),\qquad
C(a,\varepsilon)=\frac{(2-a)^2\varepsilon^2+(6-4a+4a^2-a^3)\varepsilon+4}{12\varepsilon^2\omega_H}>0.
\]
Consequently \(T(\Delta)=2\pi/\Omega(\Delta)\) satisfies
\[
T'(0+)=\frac{2\pi C(a,\varepsilon)}{\omega_H^2}>0.
\]
Moreover the mean prey density on the cycle is exactly one, while its mean predator density obeys
\[
\overline v=\frac{(1-a)^2}{2-a}-\Delta+O(\Delta^2).
\]
Thus onset of a stable oscillation simultaneously **lengthens the period** and **reduces average predator abundance**, even though lowering \(\phi\) increases the prey carrying capacity.

## Assumptions and scope

Use the dimensionaless equations in the original slow time \(\tau\):
\[
\varepsilon\frac{du}{d\tau}=u[(1-\phi u)(u-a)-v],\qquad
\frac{dv}{d\tau}=v(u-1),
\]
with \(u>0\), \(v>0\), \(0<a<1\), \(\varepsilon>0\), and frozen \(0<\phi<1\). The limit \(\Delta\downarrow0\) is taken with \(a\) and \(\varepsilon\) **fixed**. Define \(f_\phi(u)=(1-\phi u)(u-a)\). The positive equilibrium is
\[
E_\phi=(1,v_\phi),\qquad v_\phi=(1-a)(1-\phi).
\]
The extinction equilibrium \((0,0)\) is also locally asymptotically stable, hence for positive small \(\Delta\) extinction and the emerging stable cycle have disjoint open local attraction regions. No global basin classification is asserted.

## Proof

**Step 1: exact Hopf point and transversality.** At \(E_\phi\), the Jacobian is
\[
J_\phi=\begin{pmatrix} f'_\phi(1)/\varepsilon&-1/\varepsilon\\v_\phi&0\end{pmatrix},\quad
f'_\phi(1)=1-(2-a)\phi,\quad \det J_\phi=v_\phi/\varepsilon>0.
\]
At \(\phi_H=(2-a)^{-1}\) the eigenvalues are \(\pm i\omega_H\). The derivative of their real part with respect to \(\phi\) at the crossing is \(-(2-a)/(2\varepsilon)\ne0\). The origin has eigenvalues \(-a/\varepsilon\) and \(-1\), so extinction remains locally attracting.

**Step 2: fixed normalization and cubic Hopf coefficient.** Write \(x=u-1\), \(y=(v-v_\phi)/(\varepsilon\omega_H)\), and initially set \(\phi=\phi_H\). Then the vector field is *exactly*
\[
\dot x=-\omega_H y-\frac{\phi_H}{\varepsilon}x^2-\omega_Hxy-\frac{\phi_H}{\varepsilon}x^3,\qquad
\dot y=\omega_H x+xy.
\]
For a planar field \(\dot x=-\omega y+F\), \(\dot y=\omega x+G\), the real radial cubic coefficient in these coordinates is
\[
\ell=\frac{F_{xxx}+F_{xyy}+G_{xxy}+G_{yyy}}{16}+
\frac{F_{xy}(F_{xx}+F_{yy})-G_{xy}(G_{xx}+G_{yy})-F_{xx}G_{xx}+F_{yy}G_{yy}}{16\omega}.
\]
The derivatives at the origin are \(F_{xxx}=-6\phi_H/\varepsilon\), \(F_{xx}=-2\phi_H/\varepsilon\), \(F_{xy}=-\omega_H\), and \(G_{xy}=1\); all other listed derivatives vanish. Therefore
\[
\ell=-\frac{\phi_H}{4\varepsilon}<0.
\]
The real eigenvalue drift is \(\mu=(2-a)\Delta/(2\varepsilon)\). The planar Hopf theorem yields a unique small stable cycle for \(\Delta>0\) with normalized squared radius
\[
\rho^2=-\frac{\mu}{\ell}+O(\Delta^2)=2(2-a)^2\Delta+O(\Delta^2).
\]
This proves the first-harmonic amplitude and supercriticality. The positive equilibrium is unstable for \(\Delta>0\), and all local solutions starting sufficiently near the attracting cycle remain in the positive quadrant.

**Step 3: full period correction.** To compute frequency rather than assume it is \(\omega_H\), rescale the phase \(\theta=\omega_H\tau\) and abbreviate
\[
\alpha=-\frac{\phi_H}{\varepsilon\omega_H},\qquad \eta=\frac1{\omega_H}.
\]
At the critical parameter, the two equations become
\[
x_\theta=-y+\alpha x^2-xy+\alpha x^3,\qquad y_\theta=x+\eta xy.
\]
For first harmonic \(x=\rho\cos\theta+\rho^2 X_2(\theta)+O(\rho^3)\), \(y=\rho\sin\theta+\rho^2 Y_2(\theta)+O(\rho^3)\), the nonresonant second-order terms are **exactly**
\[
\begin{aligned}
X_2(\theta)&=\tfrac13\cos2\theta+\tfrac{\eta+2\alpha}{6}\sin2\theta,\\
Y_2(\theta)&=\tfrac\alpha2-\tfrac{\alpha+2\eta}{6}\cos2\theta+\tfrac16\sin2\theta.
\end{aligned}
\]
Directly averaging the cubic forcing against the tangential vector \((-\sin\theta,\cos\theta)\) gives the nonlinear phase coefficient in \(\theta\)-time
\[
P=-\frac{\alpha^2}{6}+\frac{5\alpha\eta}{24}-\frac{1+\eta^2}{24}.
\]
The parameter perturbation adds \((1-a)\Delta/(2\varepsilon\omega_H)\) to the frequency in the original \(\tau\)-time at first order. The total frequency correction is therefore
\[
\Omega=\omega_H+\left[\frac{1-a}{2\varepsilon\omega_H}+2(2-a)^2\omega_HP\right]\Delta+O(\Delta^2).
\]
Substitution of \(\alpha\), \(\eta\), and \(\omega_H^2=(1-a)^2/[\varepsilon(2-a)]\), followed by exact simplification, yields the negative coefficient \(-C(a,\varepsilon)\) stated above. Its numerator is strictly positive since \(0<a<1\) implies \(6-4a+4a^2-a^3>0\). Standard smooth Hopf branch expansions justify the remainders for each fixed \((a,\varepsilon)\). Thus the newly generated cycle is strictly slower in frequency than the Hopf oscillation.

**Step 4: exact cycle moments.** On every positive periodic orbit, integration of \(\dot v/v=u-1\) over one period gives \(\overline u=1\). Integration of \(\varepsilon\dot u/u=f_\phi(u)-v\) and the quadratic identity
\[
f_\phi(u)=-\phi u^2+(1+a\phi)u-a
\]
give the exact formula
\[
\overline v=v_\phi-\phi\,\operatorname{Var}_\tau(u).
\]
The first-harmonic amplitude from Step 2 implies
\(\operatorname{Var}_\tau(u)=(2-a)^2\Delta+O(\Delta^2)\). Hence
\[
\overline v=(1-a)(1-\phi_H+\Delta)-\phi_H(2-a)^2\Delta+O(\Delta^2)
=\frac{(1-a)^2}{2-a}-\Delta+O(\Delta^2).
\]
No finite computation is used as proof of the infinitely many parameter instances.

## Verification

A standalone Python checker, `verify_hopf.py`, is included. It uses exact SymPy algebra to reconstruct the 2nd-order Fourier terms, the cubic radial and phase coefficients, the frequency simplification, and the sign polynomial for arbitrary symbolic parameters. It also performs independently integrated ODE checks at representative parameters; those finite trajectories are consistency tests only. All formulas are based on this document's specified slow-time equations, not on transformations of earlier numerical logs.

## Relationship to prior work

Hennessy, Popović and Sattar, *A minimal model for rate-induced tipping to extinction*, arXiv:2610.12319v1 (posted 2026-10-08), introduce the strong-Allee/type-I predator–prey model, locate the singular Hopf/fold, and study rate-induced extinction using folded-saddle canards. Their full preprint sections 2–6 and Appendix A do not establish the fixed-positive-\(\varepsilon\) oscillatory branch's **first nonlinear period derivative** or the mean-predator reversal law.

Zhuo et al., *Stability and Bifurcation Analysis of a Predator–Prey Model With Generalized Allee Effect on the Prey Population*, *Journal of Mathematics* (2025), DOI 10.1155/jom/7899943, derive general Hopf and first-Lyapunov formulas for a related generalized-Allee ecological system. The present work does **not** claim that computing a Lyapunov coefficient is new; it identifies the exact parameter-uniform period softening and mean response for the newly motivated frozen model. The general paper does not provide this model-specific frequency slope, and its printed assumption of positivity of the Allee function on all positive subcapacity densities is incompatible with a strong Allee threshold.

Banerjee, Sasmal and Layek, *Supercritical and subcritical Hopf-bifurcations in a two-delayed prey–predator system with density-dependent mortality of predator and strong Allee effect in prey*, *BioSystems* 180 (2019), DOI 10.1016/j.biosystems.2019.02.011, report supercritical Hopf bifurcation without predator self-competition in a related model. Thus qualitative supercriticality alone is not asserted as novel here. Complete text was unavailable for a definitive equation-by-equation comparison, and overlap in period asymptotics remains a residual literature risk.

## Limitations

The theorem is strictly local near the positive equilibrium and applies for each fixed \(\varepsilon>0\); the \(O(\Delta^2)\) estimates need not be uniform as \(\varepsilon\to0\). The local Hopf theorem does not exclude remote cycles, canards, or additional global basin boundaries. The scalar \(\phi\) is held constant; ramping, stochasticity, delayed predation, and other functional responses are outside scope. No ecological experiment or independent mathematical audit is claimed.

## References

1. B. Hennessy, N. Popović, Z. Sattar (2026), *A minimal model for rate-induced tipping to extinction*, arXiv:2610.12319v1, https://arxiv.org/abs/2610.12319 (first public version 2026-10-08).
2. G. Zhuo et al. (2025), *Stability and Bifurcation Analysis of a Predator–Prey Model With Generalized Allee Effect on the Prey Population*, *Journal of Mathematics*, DOI:10.1155/jom/7899943, https://doi.org/10.1155/jom/7899943.
3. J. Banerjee, S. K. Sasmal, R. K. Layek (2019), *Supercritical and subcritical Hopf-bifurcations in a two-delayed prey–predator system with density-dependent mortality of predator and strong Allee effect in prey*, *BioSystems* 180, 19–37, DOI:10.1016/j.biosystems.2019.02.011.
