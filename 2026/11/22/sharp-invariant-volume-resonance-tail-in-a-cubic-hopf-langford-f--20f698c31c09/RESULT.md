# Sharp invariant-volume resonance tail in a cubic Hopf–Langford flow

## Finding
Consider, for every \(\beta>0\), the polynomial flow
\[
\dot u=(z-\tfrac12)u-\beta v,\quad
\dot v=\beta u+(z-\tfrac12)v,\quad
\dot z=z-z^2-u^2-v^2.
\]
Write \(q=u^2+v^2\), \(A(z)=z(1-z)\), and let \(\Omega=\{0<z<1,\ 0<q<2A(z)\}\). This forward-and-backward invariant region has ordinary Euclidean volume \(\pi/3\). The flow has zero divergence, so normalized three-dimensional Lebesgue volume on \(\Omega\) is an invariant probability measure.

For \(0<h<1/16\), the level \(h=q(2A(z)-q)\) is a smooth invariant two-torus, and every nonexceptional point of \(\Omega\) lies on exactly one such torus. Let \(P(h)\) denote the least period of its reduced \((z,q)\) oscillation in **original physical time**, and let \(\mathcal R=\beta P(h)/(2\pi)\) be the number of turns in the \((u,v)\)-angle per reduced oscillation. With the complete elliptic integral in parameter convention
\[
\mathbf K(m)=\int_0^{\pi/2}\frac{d\phi}{\sqrt{1-m\sin^2\phi}},
\]
the exact period is
\[
P(h)=\frac4{\sqrt{\tfrac14+\sqrt h}}\,
\mathbf K\!\left(\frac{\tfrac14-\sqrt h}{\tfrac14+\sqrt h}\right).
\]
It decreases strictly from infinity to \(2\pi\sqrt2\) as \(h\) increases from zero to \(1/16\). Thus every rational winding ratio \(r>\beta\sqrt2\) occurs on exactly one resonant torus; irrational ratios give dense orbits on their tori, and resonant tori have zero invariant volume.

**Principal new quantitative law.** If \((U,V,Z)\) is sampled from normalized Euclidean volume on \(\Omega\), its winding ratio \(\mathcal R\) has the **sharp exponential-with-linear-prefactor tail**
\[
\boxed{\lim_{R\to\infty}\frac{e^{\pi R/\beta}}{R}\,
\Pr(\mathcal R>R)=\frac{12\pi}{\beta}.}
\]
Equivalently \(\Pr(\mathcal R>R)\sim(12\pi/\beta)R e^{-\pi R/\beta}\). This concerns an exactly invariant physical volume ensemble, not sampling uniformly in the first-integral parameter or in one orbit's time.

## Assumptions and scope
The coefficient \(\beta\) is any positive real. This is the \(\alpha=-1/2,\mu=\delta=\gamma=\eta=1,\epsilon=0\) subfamily of the cubic Hopf–Langford system of Vassilev and Nikolov (2024). Time is never reparameterized. The torus-level parameter \(h\) is the first integral \(q(2z(1-z)-q)\), not the Euclidean radius or total Hamiltonian energy. The axes \(q=0\), outer separatrix \(q=2A(z)\), and central circular orbit \((z,q)=(1/2,1/4)\) have three-dimensional volume zero and are excluded from the torus ensemble. The orbit classification is stated only inside \(\Omega\).

## Proof
**Volume-preserving integral and invariant region.** Direct differentiation gives
\[
\dot z=A(z)-q,\quad\dot q=(2z-1)q,\quad\dot\theta=\beta,
\qquad H=q(2A(z)-q),\quad\dot H=0.
\]
Indeed \(\dot H=2(A-q)[\dot q+A'(z)q]=0\), since \(A'=1-2z\). The vector field's divergence is \(2(z-1/2)+(1-2z)=0\). At each fixed \(0<z<1\), the planar \((u,v)\)-disk \(0<q<2A(z)\) has Euclidean area \(2\pi A(z)\); therefore
\[
\operatorname{Vol}(\Omega)=2\pi\int_0^1z(1-z)\,dz=\pi/3.
\]
On \(H=h>0\), the quadratic identity \(H=A(z)^2-(A(z)-q)^2\) shows that the allowed \((z,q)\) locus is a closed oval, with \(z\in[z_-(h),z_+(h)]\),
\[
z_\pm(h)=\frac{1\pm\sqrt{1-4\sqrt h}}2,
\quad q_\pm(z,h)=A(z)\pm\sqrt{A(z)^2-h}.
\]
These satisfy \(q_->0\), so revolving the oval through the independent angle \(\theta\) produces a smooth embedded torus. The maximal integral \(1/16\) occurs precisely at \(z=1/2,q=1/4\), a one-dimensional periodic circle. The nonvanishing reduced vector field on each oval makes the reduced motion periodic, and compactness gives forward-and-backward completeness. The continuous conserved \(H\) confines all such motions inside \(\Omega\).

**Exact period and monotonicity.** Because \(\dot z=A(z)-q=\pm\sqrt{A(z)^2-h}\), one reduced period equals
\[
P(h)=2\int_{z_-}^{z_+}\frac{dz}{\sqrt{A(z)^2-h}}.
\]
Putting \(s=z-1/2\), \(a_h^2=1/4-\sqrt h\), \(b_h^2=1/4+\sqrt h\), the denominator is \(\sqrt{(a_h^2-s^2)(b_h^2-s^2)}\). The substitution \(s=a_h\sin\phi\) gives the stated elliptic formula. As \(h\) increases, the prefactor \(4/b_h\) decreases strictly and the elliptic parameter \(a_h^2/b_h^2\) decreases strictly; \(\mathbf K\) increases strictly in its argument. Hence \(P\) strictly decreases. At \(h\uparrow1/16\), \(a_h\to0\), \(b_h\to1/\sqrt2\), giving \(P\to2\pi\sqrt2\). At \(h\downarrow0\), the standard elliptic endpoint asymptotic \(\mathbf K(m)=\log(4/\sqrt{1-m})+O((1-m)\log(1/(1-m)))\), with \(1-m=2\sqrt h/(1/4+\sqrt h)\), yields the additive **sharp** expansion
\[
P(h)=2\log(4/h)+o(1).
\]
The product flow on each torus is conjugate by the normalized reduced phase coordinate to \((\varphi,\theta)\mapsto(\varphi+2\pi t/P(h),\theta+\beta t)\), proving the resonance statements. Every torus is a codimension-one smooth surface, so the countable family of rational-ratio tori has zero Euclidean volume.

**Exact volume-action relation and tail.** Let \(V(h)=\operatorname{Vol}\{(u,v,z)\in\Omega:H\ge h\}\). Integrating each circular annulus in the \((u,v)\)-plane gives
\[
V(h)=2\pi\int_{z_-}^{z_+}\sqrt{A(z)^2-h}\,dz,
\qquad V'(h)=-\frac\pi2 P(h).
\]
The derivative follows by differentiating under the integral: both endpoint integrands vanish and the derivative's square-root singularities are integrable. Since \(V(0)=\pi/3\), the sharp period expansion yields
\[
V(0)-V(h)=\frac\pi2\int_0^hP(s)\,ds
=\pi h[\log(4/h)+1]+o(h).
\]
Let \(h_R\) be the unique solution \(\beta P(h_R)/(2\pi)=R\), for \(R>\beta\sqrt2\). The additive period constant is essential: it implies
\[
h_R=4e^{-\pi R/\beta}(1+o(1)).
\]
As \(P\) is decreasing, \(\{\mathcal R>R\}=\{0<H<h_R\}\) up to zero-volume boundaries. Dividing the preceding lost-volume formula by \(V(0)=\pi/3\) gives
\[
\Pr(\mathcal R>R)
=3h_R[\log(4/h_R)+1]+o(h_R)
=\frac{12\pi}{\beta}R e^{-\pi R/\beta}(1+o(1)),
\]
which proves the principal claim. This argument uses Lebesgue volume in the **original** three-dimensional coordinates; no Jacobian of a nonphysical measure has been omitted.

## Verification
The optional standard-library `check.py` checks the cubic-flow derivative identity, divergence and representative elliptic period values; it numerically integrates the volume derivative with a nonsingular change of variable and verifies approach to the tail prefactor for shrinking \(h\). The checker is finite numerical corroboration only. The proof above, including endpoint control and inverse monotonicity, is analytic and establishes all infinite quantifiers.

## Relationship to prior work
Vassilev and Nikolov (posted 2024-11-11) explicitly exhibit the integrable parameter locus and the planar first integral underlying \(H\). Their reductions, the existence of first integrals and center-type closed ovals are prior mathematical work, **not claimed as new here**. Zhong and Liang (2023), in a closely related generalized Hopf–Langford system including these coefficients, analyze invariant tori and resonance periods; torus existence and rational/irrational suspension geometry are likewise not new in themselves. The new statement is the sharp **invariant Euclidean-volume distribution** of the torus winding number and its exact \(R e^{-\pi R/\beta}\) tail constant on this specified 3D invariant lobe. Published exact-period and area-sampling studies for other integrable flows, including the four-center Kolmogorov Hamiltonian and a cubic global center, establish general conceptual precedents but do not imply this system's Euclidean-volume pushforward law without the present coordinate-volume identity and separatrix asymptotics. A 2023 closely related source was accessible only as a publisher preview; see limitations.

## Limitations
This is a theorem for the displayed volume-preserving parameter slice and invariant region, not an assertion of global dynamics outside \(\Omega\), a physical model of turbulence, or generic persistence under perturbation. The exact period and invariant curves are derived from known integrability, rather than presented as novel. Although accessible literature and indexed comparisons did not exhibit the specific invariant-volume tail, the full 2023 Zhong–Liang article could not be inspected because only a preview was available and the complete manuscript was not retrievable; it is a material publication-priority risk. The result has had no independent expert audit.

## References
1. V. M. Vassilev and S. G. Nikolov, *First and Second Integrals of Hopf–Langford Type Systems*, preprint, first publicly posted 2024-11-11, https://www.preprints.org/manuscript/202411.0668 (full readable HTML, especially §§2,3,5).
2. J. Zhong and Y. Liang, *Invariant Tori and Heteroclinic Invariant Ellipsoids of a Generalized Hopf–Langford System*, *International Journal of Bifurcation and Chaos* 33 (2023), 2350153, https://doi.org/10.1142/S0218127423501535 (publisher-preview material examined, full text inaccessible).
3. *Complete monotonicity of the period on four cubic Kolmogorov Hamiltonian centers*, indexed published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-monotonicity-of-the-period-on-four-cubic-kolmogorov-ham--4339a649dd41 (full RESULT.md consulted).
4. *A Pareto law and logarithmically divergent mean for area-sampled periods of a cubic global center*, indexed published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-pareto-law-and-logarithmically-divergent-mean-for-area-sampled--fc9209c4b63d (full RESULT.md consulted).
