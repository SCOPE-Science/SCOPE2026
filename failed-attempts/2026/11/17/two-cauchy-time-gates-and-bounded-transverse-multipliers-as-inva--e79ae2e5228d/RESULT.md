# Two Cauchy time gates and bounded transverse multipliers as invariant circles approach tangency

## Finding
For the non-collinear three-circle quartic vector fields classified by Cao and Llibre, external tangency of two otherwise periodic invariant circles creates two distinct divergent physical-time clocks but no divergent transverse logarithmic Floquet multiplier. Each clock has an inverse-square-root period law and a universal Cauchy concentration profile. The ratio of the clocks depends only on the two circle radii and their local angular factors at the prospective tangency point.

Specifically, let \(C_1=(0,0)\), \(C_2=(1,0)\), \(C_3=(u,v)\), with \(v>0\), and let \(f_i(x,y)=| (x,y)-C_i|^2-r_i^2\). Write \(r_1(\varepsilon)+r_2(\varepsilon)=1-\varepsilon\), with positive limits \(R_1+R_2=1\). Suppose circle 3 remains uniformly separated from the other two, and let the angular factors \(A_i\) from (1) below be nowhere zero on their respective circles for small positive \(\varepsilon\), with nonzero limits at the limiting contact for \(i=1,2\). Put \(P=(R_1,0)\). With \(T_i\) the original physical-time period of circle \(i\),
\[
T_i(\varepsilon)\sim \frac{\pi}{\lvert A_i(P) f_3(P)\rvert\sqrt{2R_1R_2\varepsilon}}\quad(i=1,2),\qquad
\lim_{\varepsilon\downarrow0}\frac{T_2}{T_1}=\frac{\lvert A_1(P)\rvert}{\lvert A_2(P)\rvert}.
\]
The third circle's period converges to a finite positive value. For both approaching circles, the contact-centered angle in the physical-time invariant probability measure, multiplied by the circle-specific scale \(\sqrt{R_i/(2R_j\varepsilon)}\), where \(j\) is the other approaching circle, converges weakly on the real line to the density \(1/[\pi(1+z^2)]\). Both transverse logarithmic Floquet exponents have finite limits, hence their physical-time transverse Lyapunov rates are \(O(\sqrt\varepsilon)\).

## Assumptions and scope
All time, limits, and multipliers refer to the deterministic planar flow rather than a time-normalized orbit parametrization. The source's normal form is
\[
\begin{aligned}
\dot x&=-y A_1f_2f_3-yA_2f_1f_3-(y-v)A_3f_1f_2,\\
\dot y&=x A_1f_2f_3+(x-1)A_2f_1f_3+(x-u)A_3f_1f_2,
\end{aligned}\tag{1}
\]
where
\[
A_1=-\lambda-\mu+\kappa[-vx+(u-1)y-v],\quad A_2=\lambda+\kappa(vx-uy),\quad A_3=\mu+\kappa y.
\]
The real coefficients \((\lambda,\mu,\kappa)\ne(0,0,0)\) are fixed. For all small positive \(\varepsilon\), all three circles are assumed pairwise disjoint and each \(A_i\) is bounded away from zero on its corresponding circle, uniformly through the limiting family. The varying positive radii \(r_1,r_2\) have positive limits \(R_1,R_2\), and \(r_3\) is fixed. The general result does not assert that the periodic circles are hyperbolic limit cycles; the transverse statements hold whether their multipliers equal one or not. Uniform separation of circle 3 implies \(f_3(P)\ne0\).

For the explicit realization take
\[
(u,v,r_3,\lambda,\mu,\kappa)=(0,2,1/10,-4,-3,1),\quad
r_1=r_2=(1-\varepsilon)/2,\quad 0<\varepsilon<1.
\]
Here the affine factors are \(A_1=5-2x-y\), \(A_2=-4+2x\), \(A_3=-3+y\). They have fixed nonzero signs on their respective circles, so all three circles are genuine periodic orbits. The first two turn in opposite orientations.

## Proof
**1. Tangential factorization.** On the first circle, parametrize \((x,y)=(r_1\cos\theta,r_1\sin\theta)\). The field (1) reduces exactly to \(\dot\theta=A_1 f_2f_3\). On the second, write \((x,y)=(1+r_2\cos\phi,r_2\sin\phi)\) and obtain \(\dot\phi=A_2f_1f_3\). The third analogously has \(\dot\psi=A_3f_1f_2\). The source's hypotheses ensure none vanishes on the corresponding circle.

**2. Exact gap identity and period asymptotics.** Direct substitution gives
\[
f_2|_{C_1}=\varepsilon(2r_2+\varepsilon)+2r_1(1-\cos\theta),\qquad
f_1|_{C_2}=\varepsilon(2r_1+\varepsilon)+2r_2(1+\cos\phi).
\tag{2}
\]
Both functions have a single quadratic minimum; the first occurs at \(\theta=0\), the second at \(\phi=\pi\). For \(\{i,j\}=\{1,2\}\), in an angular window shrinking toward the minimum, (2) equals \((2R_j\varepsilon+R_i\vartheta^2)(1+o(1))\) in the scaling \(\vartheta=\sqrt{2R_j\varepsilon/R_i}\,z\) with \(z\) bounded. The remaining factor \(\lvert A_i f_3\rvert\) converges uniformly to \(\lvert A_i(P)f_3(P)\rvert\) near contact. The integral over the complementary arc is bounded, and standard two-sided quadratic bounds for \(1-\cos\vartheta\) justify dominated convergence after rescaling. Since \(\int_{\mathbb R}(1+z^2)^{-1}dz=\pi\),
\[
\sqrt\varepsilon\,T_i\to\frac{\pi}{\sqrt{2R_1R_2}\lvert A_i(P)f_3(P)\rvert}.
\]
The third angular speed is bounded away from zero on its circle uniformly and converges to its limiting nonzero speed; its period therefore converges finitely.

**3. Physical-time concentration.** On each circle, a uniform time sample has angular density proportional to \(1/|\dot\vartheta|\). In the contact-centered coordinate \(Z=\vartheta\sqrt{R_i/(2R_j\varepsilon)}\), its normalized density, restricted to each bounded \(Z\)-interval, converges to \(1/[\pi(1+Z^2)]\). The same period bounds show the probability mass outside a fixed contact neighborhood tends to zero. For every \(M\ge1\), the normalized time in \(\lvert\varthetavert>M\sqrt{2\varepsilon}\) is at most \(C/M+C\sqrt\varepsilon\), with \(C\) uniform for sufficiently small \(\varepsilon\); this proves tightness of the scaled family. Thus both rescaled phase measures converge weakly to the standard Cauchy law.

**4. Bounded transverse multipliers.** Differentiate \(f_1,f_2\) along (1) to obtain the exact cofactors
\[
K_1=-2yA_2f_3+2(vx-uy)A_3f_2,\qquad
K_2=2yA_1f_3+2[v(x-1)+(1-u)y]A_3f_1.
\]
By the cofactor identity, each transverse logarithmic multiplier is the positive-time integral of \(K_i\). With the sign of the angular speed included, the circle-one angular integrand is
\[
\frac{K_1}{A_1f_2f_3}=-\frac{2yA_2}{A_1f_2}+\frac{2(vx-uy)A_3}{A_1f_3},
\]
and the circle-two counterpart is
\[
\frac{K_2}{A_2f_1f_3}=\frac{2yA_1}{A_2f_1}+\frac{2[v(x-1)+(1-u)y]A_3}{A_2f_3}.
\]
The terms without \(1/f_1\) or \(1/f_2\) converge uniformly. For each potentially singular term, center angle at the contact and pair the values at \(\vartheta\) and \(-\vartheta\). The numerator vanishes linearly and its even part vanishes quadratically, uniformly in \(\varepsilon\), because \(y=r_i\sin\vartheta\) or its negative. The denominator has a uniform lower bound proportional to \(\varepsilon+\vartheta^2\). Consequently the paired integrands are uniformly bounded and converge pointwise outside the contact. Dominated convergence proves finite limits for both positive-time logarithmic multipliers. Dividing by periods of order \(\varepsilon^{-1/2}\) gives the asserted physical-time rate bound.

**5. Exact constants in the realization.** At \(\varepsilon=0\), the contact is \(P=(1/2,0)\), \(R_1=R_2=1/2\), \(f_3(P)=106/25\), \(A_1(P)=4\), and \(A_2(P)=-3\). Substitution in the general result yields
\[
\lim_{\varepsilon\downarrow0}\sqrt\varepsilon T_1=\frac{25\pi\sqrt2}{424},\quad
\lim_{\varepsilon\downarrow0}\sqrt\varepsilon T_2=\frac{25\pi\sqrt2}{318},\quad
\lim_{\varepsilon\downarrow0}T_2/T_1=\frac43.
\]
This is a singular-limit statement: at actual tangency the two circles cease to be disjoint and the hypotheses of the theorem do not apply.

## Verification
An accompanying standalone Python checker uses symbolic polynomial identities to verify that the displayed field has total degree four, that all three prescribed circles are invariant, and that the first two cofactors, both unequal-radius gap identities, and contact constants agree with the formulas. Finite quadratures at \(\varepsilon=10^{-3}\) and \(\varepsilon=10^{-4}\) verify the convergence trend of both rescaled periods, boundedness of the two log multipliers, and the standard Cauchy mass \(\Pr(|Z|\le1)=1/2\). Numerical checks do not replace the uniform analytic bounds above.

## Relationship to prior work
Cao and Llibre, *Quartic polynomial differential systems with three disjoint invariant circles* (2026, arXiv:2611.05696v1), establish the complete quartic normal forms, the angular-factor nonvanishing criteria for periodicity, and transverse hyperbolicity conditions for positive separations. The present result uses their non-collinear normal form but studies a different question: **joint singular physical-time limits** as two circles approach an excluded geometric boundary, including weak convergence of time measures and the simultaneous finite transverse-multiplier limit. The source's general formulas are foundational here and are not claimed to be new. Similar inverse-square-root time gates and Cauchy profiles occur in other planar polynomial dynamics, but those do not classify the two-circle tangency within this quartic three-circle family.

## Limitations
The analysis assumes an isolated *external* tangency, uniform nondegeneracy of angular factors, and strict separation of the third circle. It does not cover internal tangency, simultaneous multiple contacts, vanishing angular factor at contact, or the limiting singular flow at \(\varepsilon=0\). Finite transverse logarithmic multipliers need not imply hyperbolicity at all parameter values. The result makes no claim about additional noncircular periodic orbits or basin geometry. Independent mathematical validation and exhaustive historical priority review remain outstanding.

## References
1. C. Cao and J. Llibre, *Quartic polynomial differential systems with three disjoint invariant circles*, arXiv:2611.05696v1 (first public 2026-11-03), https://arxiv.org/abs/2611.05696 . See Theorem D, Sections 2.2 and 6.
2. Classical positive-time Floquet and invariant-curve cofactor identities, as presented and sourced in Section 2.2 of Cao and Llibre, loc. cit.
