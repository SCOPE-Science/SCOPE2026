# Quadrupole-scale logarithmic winding in the center drift of half-plane three-vortex collapse

## Finding
For each exact interior-collapse solution constructed in Theorem 5.3 of Yang [1], write the weighted vortex center as \(C(t)=\sum_{k=1}^{3}\Gamma_kz_k(t)/G\), where \(G=\sum_{k=1}^{3}\Gamma_k\), and its collision point as \(C_*=X_*+iY_*\) with \(Y_*>0\). Let \(\tau=T-t\), let \(W^*=(W_1^*,W_2^*,W_3^*)\) be its non-equilateral Gröbli profile, let \(\Omega\in\mathbb R\) be the associated rotation rate, and define \(Q_*=\sum_k\Gamma_k(W_k^*)^2\). The weighted-center height is constant, \(\operatorname{Im}C(t)=Y_*\), and the horizontal position obeys
\[
\operatorname{Re}C(t)=X_*-\frac{G}{4\pi Y_*}\tau+\frac{1}{8\pi Y_*^3}\operatorname{Re}\!\left(\frac{Q_*\tau^{2+2i\Omega}}{2+2i\Omega}\right)+O(\tau^{5/2}).
\]
Here \(\tau^{2+2i\Omega}=\exp((2+2i\Omega)\log\tau)\) for \(\tau>0\). Consequently, when \(\Omega\ne0\), the normalized horizontal-center residual
\[
\mathcal R(\tau)=\frac{\operatorname{Re}C(T-\tau)-X_*+G\tau/(4\pi Y_*)}{\tau^2}
\]
has the exact extremal limits
\[
\limsup_{\tau\downarrow0}\mathcal R(\tau)=\frac{|Q_*|}{16\pi Y_*^3\sqrt{1+\Omega^2}},\qquad
\liminf_{\tau\downarrow0}\mathcal R(\tau)=-\frac{|Q_*|}{16\pi Y_*^3\sqrt{1+\Omega^2}}.
\]
In particular, for a nonzero quadrupole \(Q_*\), the second-order residual has no ordinary limit. When \(\Omega=0\), that residual converges to \(\operatorname{Re}(Q_*)/(16\pi Y_*^3)\). The theorem is for the distinguished collapsing trajectories, not all nearby initial states.

## Assumptions and scope
The governing half-plane point-vortex equation is the classical image-vortex system, with three distinct positions \(z_k(t)\) in the open upper half-plane and fixed real nonzero circulations:
\[
\frac{d\bar z_k}{dt}=\frac{1}{2\pi i}\sum_{j\ne k}\frac{\Gamma_j}{z_k-z_j}-\frac{1}{2\pi i}\sum_{j=1}^3\frac{\Gamma_j}{z_k-\bar z_j}.
\]
Assume \(\sum_{i<j}\Gamma_i\Gamma_j=0\). Since \(G^2=\sum_i\Gamma_i^2>0\), the weighted center is defined. The exact solutions considered obey Yang's strong-stable-manifold asymptotics, with \(s=-\log\tau\):
\[
\zeta_k(t):=z_k(t)-C(t)=\sqrt\tau\,e^{-i\Omega s}(W_k^*+O(\tau)),\qquad C(t)\to C_*.
\]
The point \(C_*\) is prescribed in the upper half-plane, so the image denominators stay uniformly away from zero for sufficiently late times. All big-O constants can depend on this fixed solution, profile, and collision point. The expansion does not describe other collapsing branches or collisions with the boundary.

## Proof
**1. Exact center drift and constant height.** Multiply the displayed vortex equations by \(\Gamma_k\), sum in \(k\), and divide by \(G\). Direct mutual-vortex terms cancel pairwise. With \(\zeta_k=z_k-C\),
\[
\frac{d\overline C}{dt}=-\frac{1}{2\pi iG}\sum_{k,j=1}^3\frac{\Gamma_k\Gamma_j}{2i\operatorname{Im}C+\zeta_k-\overline{\zeta_j}}.
\]
The double sum is purely imaginary, since complex conjugation exchanges the two indices and introduces a negative sign. Therefore \(\dot C\) is real and \(\operatorname{Im}C\equiv Y_*\). Centering also gives \(\sum_k\Gamma_k\zeta_k=0\) exactly.

**2. The dipole cancellation and quadratic image correction.** Put \(Q_2(t)=\sum_k\Gamma_k\zeta_k(t)^2\). As \(\zeta_k=O(\sqrt\tau)\) and \(Y_*>0\), expand the image denominator about \(2iY_*\). The constant term of the weighted double sum is \(G^2/(2iY_*)\), while its linear term vanishes because \(\sum_k\Gamma_k\zeta_k=0\). The quadratic numerator satisfies the exact identity
\[
\sum_{k,j}\Gamma_k\Gamma_j(\zeta_k-\overline{\zeta_j})^2
=G(Q_2+\overline{Q_2})=2G\operatorname{Re}Q_2.
\]
The cubic-and-higher remainder is \(O(\tau^{3/2})\), uniformly near the fixed positive height. Consequently,
\[
\frac{d\operatorname{Re}C}{dt}
=\frac{G}{4\pi Y_*}-\frac{\operatorname{Re}Q_2(t)}{8\pi Y_*^3}+O(\tau^{3/2}).
\]
The coefficient signs follow directly from \((2iY_*)^{-3}=i/(8Y_*^3)\).

**3. The rotating quadrupole and integration.** From the stated shape estimate,
\[
Q_2(t)=\tau^{1+2i\Omega}(Q_*+O(\tau))
=\tau^{1+2i\Omega}Q_*+O(\tau^2).
\]
Thus the horizontal velocity equals the constant leading drift minus \(\tau\operatorname{Re}(Q_*e^{2i\Omega\log\tau})/(8\pi Y_*^3)\), with remainder \(O(\tau^{3/2})\). Since \(\operatorname{Re}C(T-\tau)\to X_*\), integrate from \(t=T-\tau\) to \(T\), using \(\int_0^\tau u^{1+2i\Omega}du=\tau^{2+2i\Omega}/(2+2i\Omega)\). The integrated error is \(O(\tau^{5/2})\), giving the formula. Divide the residual by \(\tau^2\). For \(\Omega\ne0\), the angle \(2\Omega\log\tau\) traverses arbitrarily many full turns as \(\tau\downarrow0\); its cosine has full limsup and liminf, and the remainder is \(O(\tau^{1/2})\). The amplitude is \(|Q_*|/[16\pi Y_*^3\sqrt{1+\Omega^2}]\), as asserted.

**4. A genuinely oscillatory profile.** Choose \(\boldsymbol\Gamma=(2,2,-1)\), \(a^2=\sqrt3/(14\pi)\), and \(W^*=a(1,-2-i\sqrt3,-2-2i\sqrt3)\). The three entries are distinct and their pairwise distances are not all equal. Direct substitution gives \(\sum_k\Gamma_kW_k^*=0\) and
\[
\frac{1}{2\pi i}\sum_{j\ne k}\frac{\Gamma_j}{W_k^*-W_j^*}
=\left(-\frac12+i\Omega\right)\overline{W_k^*},\qquad \Omega=-\frac{5\sqrt3}{6},
\]
for each index. It also gives \(Q_*=6\sqrt3/(7\pi)\ne0\). Yang's theorem supplies an exact half-plane collapsing solution for this admissible non-equilateral profile at any prescribed height, so the oscillatory case occurs.

## Verification
Run the standalone standard-library Python script with `python3 checker.py`. It verifies the explicit three-vortex Gröbli profile equations and weighted moment identities and evaluates the exact mirrored-vortex center velocity at four small scales. The comparison tests the predicted constant and rotating quadratic terms, including cancellation of vertical velocity. Its finite numerical checks corroborate the expansion but do not establish the asymptotic theorem; the proof above supplies the quantifiers and bounds.

## Relationship to prior work
Yang [1, Sections 2, 5.1–5.3 and Appendix A] provides the half-plane equations, exact center equation, a collapsing strong-stable branch, and its leading \(O(\tau)\) center estimate; these are essential premises. The new result computes the universal linear drift, the first shape-dependent correction, its sharp log-periodic amplitude, and a concrete nonzero example. The source does not state this order-two center expansion. Drivas, Khanikati and Khanikati [2] analyze collapse on curved surfaces rather than the method-of-images half-plane; their abstract does not settle this center correction. Earlier work on self-similar Gröbli collapse in the full plane is compatible with, but cannot alone determine, a boundary-induced center drift. Related general multipole asymptotics could conceivably imply parts of this statement, and exhaustive historical priority is not claimed.

## Limitations
The theorem assumes one of Yang's specially constructed interior collapsing solutions and a fixed positive collision height. It does not establish robustness of that collapsing branch, a neighborhood basin of attraction, higher-order asymptotic coefficients, or a corresponding law for curved or multiple-boundary domains. The normalized second-order oscillation requires \(\Omega\ne0\) and \(Q_*\ne0\); zero quadrupole gives a smaller residual. Independent mathematical validation has not been performed.

## References
[1] Cheng Yang, *On the Finite-Time Singularities of Point-Vortex Systems I: The Half-Plane*, arXiv:2611.01014v1, first publicly posted 2026-10-31. https://arxiv.org/html/2611.01014v1

[2] Theodore D. Drivas, Boris A. Khanikati and Valeriya A. Khanikati, *On the collapse of three point vortices on surfaces*, arXiv:2607.16490 (2026). https://arxiv.org/abs/2607.16490
