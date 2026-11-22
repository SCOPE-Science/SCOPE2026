# Exact trapping area and a universal invariant Beta law at a rocking saddle–center

## Finding
For the conservative radial complex-rocking Hamiltonian of Prieto-Castrillo, Pérez-González and Pérez del Río (2026), the entire area of the bounded period annulus has an exact one-dimensional radical integral, decreases **strictly** through the whole confinement interval, and vanishes at the disappearance of the well with an explicit leading coefficient. The normalized invariant Liouville probability on that annulus, after its natural anisotropic rescaling, converges **in total variation** to uniform area on a cubic Hamiltonian lobe; its rescaled radial coordinate is exactly Beta distributed in the limit.

Put \(\beta_*=27/256\) and \(V_\beta(r)=-r^2/2+r+\beta/(2r^2)\). For \(0<\beta<\beta_*\), let \(s\in(3/4,1)\) denote the unique outer saddle radius, characterized by \(\beta=s^3(1-s)\), and set
\[
L=1-s+\sqrt{1-s},\qquad N=1-s-\sqrt{1-s},\qquad E_s=V_\beta(s).
\]
The bounded period annulus and its Liouville area are
\[
\mathcal D_\beta=\bigl\{(r,p):L<r<s,\quad p^2/2+V_\beta(r)<E_s\bigr\},\qquad
\boxed{\mathcal A(\beta)=2\int_L^s\frac{s-r}{r}\sqrt{(r-L)(r-N)}\,dr.}
\]
The area is continuously differentiable and strictly decreasing in \(\beta\), with exact endpoint limits
\[
\lim_{\beta\downarrow0}\mathcal A(\beta)=1,\qquad
\lim_{\beta\uparrow\beta_*}\mathcal A(\beta)=0.
\]
For \(\delta=\beta_*-\beta\), the **sharp** saddle–center coefficient is
\[
\boxed{\mathcal A(\beta)\sim\frac{256\,2^{3/4}}{45}\,\delta^{5/4}.}
\]
More precisely, put \(c=2\sqrt2/3\), \(C=128\sqrt2/81\), and define the scaled canonical coordinates
\[
Z_\delta=\frac{r-3/4}{c\sqrt\delta},\qquad
U_\delta=\frac{p}{\sqrt{2C}\,\delta^{3/4}}.
\]
Let \(\mu_\beta\) be normalized area \(dr\,dp/\mathcal A(\beta)\) restricted to \(\mathcal D_\beta\). Then \(\mu_\beta\) is invariant under the Hamiltonian flow and the joint law of \((Z_\delta,U_\delta)\) converges in total variation, with respect to Lebesgue measure on \(\mathbb R^2\), to the uniform distribution on
\[
\mathcal D_*=\Bigl\{(z,u):-2<z<1,\quad |u|<(1-z)\sqrt{(z+2)/3}\Bigr\}.
\]
The area of \(\mathcal D_*\) is \(24/5\). Equivalently, if \(W_\delta=(Z_\delta+2)/3\), then
\[
\boxed{W_\delta\xrightarrow{\mathrm{TV}}\operatorname{Beta}(3/2,2),\qquad
f(w)=\frac{15}{4}\sqrt w(1-w)\,\mathbf 1_{(0,1)}(w).}
\]
The phrase “converges in total variation” refers to convergence of probability measures on the fixed **rescaled** coordinate space, not to convergence of unscaled area measures.

## Assumptions and scope
The equations are exactly \(r'=p\), \(p'=-V_\beta'(r)\), with \(r>0\) and conserved radial energy \(H_\beta=p^2/2+V_\beta(r)\). They are the \(\gamma=0\) (undamped) radial subsystem in the cited model, in its original dimensionless time. The phase-plane area is the canonical \(dr\,dp\) measure, **not** unweighted area in the polynomial variables \((x,y)=(p/r,1/r)\) or physical rocking angles. The upper energy boundary is the saddle homoclinic loop; its area is zero. The theorem makes no claim for dissipative dynamics, the impulsive rigid-block limit, or the distribution of time spent along a single periodic orbit. Uniform phase-area sampling is a precise choice of invariant ensemble, not a presumed empirical prior.

## Proof
**1. Exact factorization and bounded domain.** The stationary equation is \(\beta=r^3(1-r)\). On \((0,3/4)\) it has the unique well minimum \(r_m\); on \((3/4,1)\) the unique saddle \(s\). At the saddle energy \(E_s\), direct polynomial division using \(\beta=s^3(1-s)\) yields
\[
2r^2(E_s-V_\beta(r))
=(r-s)^2\bigl(r^2+2(s-1)r+s(s-1)\bigr)
=(r-s)^2(r-L)(r-N).
\]
For \(s\in(3/4,1)\), one has \(N<0<L<r_m<s\), so \(L\) is the unique inner turning point at the saddle energy. On \(L<r<s\), the allowed velocity magnitude is
\[
|p|<\frac{s-r}{r}\sqrt{(r-L)(r-N)}.
\]
Integration of this vertical width proves the exact area quadrature. Every interior regular energy component is a periodic orbit about \((r_m,0)\), and \(\mathcal D_\beta\) is invariant as a whole; its complement contains the escape region.

**2. Strict global monotonicity and endpoints.** The outer solution \(s\) decreases strictly as \(\beta\) increases because \(\beta'(s)=s^2(3-4s)<0\); \(L(s)=1-s+\sqrt{1-s}\) decreases as \(s\) increases. Thus the radius interval \((L,s)\) strictly shrinks with increasing \(\beta\). At every fixed \(r<s\) in the interval, the envelope derivative of the available squared-velocity height is
\[
\frac{\partial}{\partial\beta}(E_s-V_\beta(r))
=\frac{1}{2s^2}-\frac{1}{2r^2}<0.
\]
Consequently the nested domains shrink strictly in their cross-section widths, giving strict decrease of their areas. Differentiation under the integral after a squared-endpoint substitution also gives \(C^1\) regularity at all interior parameters. As \(\beta\downarrow0\), \(s\uparrow1\), \(L,N\to0\), and the vertical width converges in area to \(2(1-r)\) on \((0,1)\); bounded convergence after splitting off a small interval at zero yields \(\mathcal A\to1\). At \(\beta\uparrow\beta_*\), both endpoints tend to \(3/4\) and the velocity width tends to zero, so \(\mathcal A\to0\).

**3. Critical scaling with exact constant.** The fold occurs at \(r_*=3/4\), \(\beta_*=27/256\), with \(V'_{\beta_*}(r_*)=V''_{\beta_*}(r_*)=0\). Taylor expansion, uniformly with its first derivative on compact \(z\)-sets, gives
\[
V_{\beta_*-\delta}(r_*+c\sqrt\delta\,z)
-V_{\beta_*-\delta}(r_*)
=C\delta^{3/2}\bigl(z-z^3/3\bigr)+O(\delta^2),
\quad c=2\sqrt2/3,\quad C=128\sqrt2/81.
\]
The stable and saddle critical points become \(z=-1\) and \(z=1\), respectively, and the other homoclinic turning point becomes \(z=-2\); this also follows directly by expanding \(s\) and \(L\). The barrier level in scaled energy tends to \(2C/3\), giving the limiting inequality
\[
U^2<2/3-z+z^3/3=(1-z)^2(z+2)/3.
\]
The scaled interval endpoints and graph heights converge, and both graphs remain inside one fixed compact rectangle. Hence their indicator functions converge in \(L^1(\mathbb R^2)\). The limiting region has area
\[
|\mathcal D_*|=\int_{-2}^1 2(1-z)\sqrt{(z+2)/3}\,dz=24/5.
\]
The physical Jacobian is \(c\sqrt{2C}\,\delta^{5/4}\), so
\[
\mathcal A(\beta)\sim c\sqrt{2C}\,(24/5)\delta^{5/4}
=(256\,2^{3/4}/45)\delta^{5/4}.
\]

**4. Invariant probability and Beta limit.** Hamilton's equations have zero divergence in \((r,p)\), so their flow preserves two-dimensional Lebesgue area (Liouville's theorem). Because \(\mathcal D_\beta\) is invariant and bounded, its normalized area \(\mu_\beta\) is a well-defined invariant probability. The affine rescaling takes it to normalized uniform area on the scaled domains. The \(L^1\)-indicator convergence and convergence of their areas imply total-variation convergence of those probabilities. Integrating out \(u\) from uniform area on \(\mathcal D_*\) gives
\[
f_Z(z)=\frac{5}{12}(1-z)\sqrt{(z+2)/3}\,\mathbf 1_{(-2,1)}(z).
\]
The linear change \(w=(z+2)/3\) yields \(f_W(w)=15\sqrt w(1-w)/4\), which is the normalized \(\operatorname{Beta}(3/2,2)\) density. Total variation contracts under measurable maps, so the marginal convergence is also in total variation. The mean of this limiting radial fraction is \(3/7\).

## Verification
The standalone `verify.py` carries out exact symbolic checks of the quartic saddle-energy factorization, the cubic fold expansion, the universal lobe area, the area coefficient, and the normalization and first moment of the claimed Beta law. Independent high-precision quadrature of the factorized lobe and the unfactorized energy integral was compared at eight parameter values; area monotonicity and limiting asymptotic ratios were also tested. Run `python3 verify.py` with `sympy` and `mpmath` installed. Computations corroborate, but do not substitute for, the all-parameter proof.

## Relationship to prior work
Prieto-Castrillo, Pérez-González and Pérez del Río (2026) give the precise effective potential, the saddle–center threshold, the conservative energy portrait, and the criterion for radial confinement; these are acknowledged premises, not claimed innovations. The distinct contemporaneous mathematical result *Two resonance accumulation scales for conservative complex rocking* derives angular-closure ladders and a cubic normal-form period law for the same Hamiltonian. It does not establish the **full-parameter exact area, strict global capacity monotonicity, or the normalized invariant-area probability law** proved here. A 2017 study of near-fold Hamiltonian area-preserving maps gives a generic fold-lobe area scaling and explicit cubic-normal-form coefficient in a different system; generic \(5/4\) exponents and cubic fold profiles are therefore **not** asserted to be new. The contribution is the combined exact global phase-area description and explicit probability limit for this particular newly introduced radial rocking Hamiltonian.

## Limitations
The result is mathematical phase-space geometry of a conservative **radial** Hamiltonian. The normalized invariant measure is Liouville area inside the radial period annulus, rather than a selected energy shell or the three-dimensional full reconstructed complex flow. No physical impact/capture probability or dissipative basin area is inferred. The local fold exponent and cubic universal density mechanism may be derivable from general normal-form theory; the historical priority of the **specific combined exact all-parameter formula and limit law** is not independently certified. No independent mathematical audit has been performed.

## References
- F. Prieto-Castrillo, S. Pérez-González, and J. S. Pérez del Río, *From Complex Regularization to Polynomial Flow: Capture and Escape in Rocking Dynamics*, arXiv:2611.13861v1 (first public 10 November 2026), https://arxiv.org/html/2611.13861v1, especially Sections 4–6 and equations (33)–(39).
- *Two resonance accumulation scales for conservative complex rocking*, published mathematical record (17 November 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-two-resonance-accumulation-scales-for-conservative-complex-rocki--e2b19f644d44 (full mathematical statement and proof inspected).
- Yu. A. Kubyshin, O. Larreal, R. Ramírez-Ros and T. M. Seara, *Stability of the phase motion in race-track microtrons* (2017, available as `koubishinLRS2017PhysicaDtron.pdf`), https://web.mat.upc.edu/tere.m-seara/articles/koubishinLRS2017PhysicaDtron.pdf, Appendix B: generic Hamiltonian saddle–center scaling and separatrix area for an unrelated area-preserving map.
- F. Prieto and P. B. Lourenço, *On the rocking behavior of rigid objects*, Meccanica 40 (2005), 121–133, https://doi.org/10.1007/s11012-004-5875-z (earlier rocking regularization; full-text comparison unavailable).
