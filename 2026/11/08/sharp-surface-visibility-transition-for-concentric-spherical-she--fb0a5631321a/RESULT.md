# Sharp surface-visibility transition for concentric spherical shells

## Finding
Let \(d\ge 2\) be an integer, \(0<\rho<1\), and
\[
A_{d,\rho}=\{x\in\mathbb R^d:\rho\le\lVert x\rVert_2\le 1\}.
\]
Choose \(X,Y\) independently from the **normalized \((d-1)\)-dimensional surface-area measure** on the *entire* boundary \(\partial A_{d,\rho}\), including both spheres. Define the visibility probability
\[
V_d(\rho)=\mathbb P([X,Y]\subseteq A_{d,\rho}).
\]
For \(-1\le z\le1\), let \(Q_d(z)=\mathbb P(U\cdot W\ge z)\), where \(U,W\) are independent Haar-uniform unit vectors in \(\mathbb R^d\). Set
\[
 c_d=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)},\qquad
 Q_d(z)=c_d\int_z^1(1-u^2)^{(d-3)/2}\,du.
\]
**Exact visibility and inverse classification.** For every \(d\ge2\) and \(0<\rho<1\),
\[
\boxed{V_d(\rho)=
\frac{Q_d(2\rho^2-1)+2\rho^{d-1}Q_d(\rho)}{(1+\rho^{d-1})^2}.}
\]
The function \(V_d\) is continuous and strictly decreasing from the limit \(1\) at \(\rho\downarrow0\) to the limit \(0\) at \(\rho\uparrow1\). Thus the *one* population visibility probability determines the inner/outer-radius ratio uniquely when \(d\) is known. In dimensions two and three, respectively,
\[
\boxed{V_2(\rho)=\frac{2\arccos\rho}{\pi(1+\rho)},\qquad
V_3(\rho)=\frac{1-\rho^3}{(1+\rho^2)^2}.}
\]
**Sharp high-dimensional transition.** Put \(\rho_*=1/\sqrt2\). For every fixed \(0<\rho<1\),
\[
\boxed{\lim_{d\to\infty}V_d(\rho)=
\begin{cases}1&0<\rho<\rho_*,\\
\frac12&\rho=\rho_*,\\
0&\rho_*<\rho<1.
\end{cases}}
\]
In the unique critical \(d^{-1/2}\) window, for each real \(\lambda\) and
\(\rho_d=\sqrt{(1+\lambda/\sqrt d)/2}\) (defined for all sufficiently large \(d\)),
\[
\boxed{\lim_{d\to\infty}V_d(\rho_d)=\Phi(-\lambda),}
\]
where \(\Phi\) is the standard Gaussian distribution function. Consequently, for each \(p\in(0,1)\), the unique solution \(V_d(\rho_d(p))=p\) obeys
\[
\boxed{\sqrt d\bigl(2\rho_d(p)^2-1\bigr)\longrightarrow\Phi^{-1}(1-p).}
\]
For every *fixed* \(\rho\ne\rho_*\), define the rare-event probability \(E_d(\rho)=1-V_d(\rho)\) below the threshold, and \(E_d(\rho)=V_d(\rho)\) above it. There is the **sharp equivalent**, including its prefactor,
\[
\boxed{E_d(\rho)\sim
\frac{[4\rho^2(1-\rho^2)]^{(d-1)/2}}
{|2\rho^2-1|\sqrt{2\pi d}}\quad(d\to\infty).}
\]
It yields a complementary-radius rare-event duality: for every fixed \(0<\rho<1/\sqrt2\),
\[
\boxed{\frac{1-V_d(\rho)}{V_d(\sqrt{1-\rho^2})}\longrightarrow1.}
\]
In contrast, for every finite \(d\ge2\) and \(0<\rho<1\), the *strict* inequality
\[
\boxed{V_d(\rho)+V_d(\sqrt{1-\rho^2})<1}
\]
holds.

**Thin-shell scaling.** For fixed \(d\ge2\), as \(\rho\uparrow1\),
\[
\boxed{V_d(\rho)\sim
\frac{c_d\,2^{(d-1)/2}(2^{d-1}+2)}{4(d-1)}
(1-\rho)^{(d-1)/2}.}
\]
The dimension-dependent coefficient is strictly positive and differs from the volume-sampling coefficient. All limits are taken in the order specified; no uniformity across growing \(d\) and vanishing shell thickness is asserted.

## Assumptions and scope
The region \(A_{d,\rho}\) is a closed Euclidean shell. The boundary sampling measure is proportional to Hausdorff surface measure: its outer-sphere weight is \((1+\rho^{d-1})^{-1}\), and its inner-sphere weight is \(\rho^{d-1}/(1+\rho^{d-1})\). Conditional on a chosen sphere, directions are independent Haar-uniform vectors. The entire *straight* segment must lie in the shell; intrinsic shortest paths are not considered. Tangencies and coincident endpoints have sampling probability zero for the relevant comparisons. The outer radius is normalized to one; scaling by any positive radius leaves the visibility probability unchanged.

## Proof
**1. Angular and surface decomposition.** Fix unit vectors \(U,W\), let \(Z=U\cdot W\), and condition on which two spheres supply the endpoints. If both endpoints are outer, they are \(U,W\); their segment has minimum squared radius \((1+Z)/2\). Hence it avoids the open inner ball exactly when \(Z\ge2\rho^2-1\). If one endpoint is inner, write the segment from \(\rho U\) to \(W\). Its squared distance from the origin is convex in the segment parameter; it never decreases below its initial value \(\rho^2\) exactly when its right derivative at the inner endpoint is nonnegative, equivalently \(\rho U\cdot(W-\rho U)\ge0\), i.e. \(Z\ge\rho\). Two distinct inner-sphere endpoints have a segment that enters the open inner ball. The outer ball is convex, so no segment can leave its exterior boundary. The dot product \(Z\) has density \(c_d(1-z^2)^{(d-3)/2}\). Combining the outer/outer, two mixed, and inner/inner probabilities proves the exact formula.

**2. Strict monotonicity and inversion.** Couple all radius ratios using independent uniform \([0,1]\) random numbers to select each component and keep fixed endpoint directions. The probability of selecting the inner sphere, \(\rho^{d-1}/(1+\rho^{d-1})\), increases strictly with \(\rho\); under the coupling a component can change only from outer to inner. For fixed component types the angular visibility thresholds \(2\rho^2-1\) and \(\rho\) increase. When an outer/outer pair becomes mixed, the new threshold \(\rho_2\) exceeds the old threshold \(2\rho_1^2-1\) whenever \(\rho_2>\rho_1\), and mixed-to-inner/inner turns visibility off. Thus the indicator is pointwise nonincreasing in \(\rho\). It is *strictly* decreasing in expectation because with positive probability the two endpoints remain outer for both ratios while \(Z\) lies strictly between their distinct outer/outer thresholds. Continuity and the two endpoint limits follow from the formula. For \(d=2\), \(Q_2(z)=\arccos(z)/\pi\); for \(d=3\), \(Q_3(z)=(1-z)/2\), giving the displayed specializations.

**3. High-dimensional threshold and Gaussian window.** By rotational invariance, \(Z\) has the law of the first coordinate of a uniform unit vector. If \(G_1,\ldots,G_d\) are independent standard Gaussians, then \(Z\) has the law of \(G_1/(G_1^2+\cdots+G_d^2)^{1/2}\). The law of large numbers and Slutsky's theorem give \(\sqrt d Z\Rightarrow N(0,1)\). For any fixed \(\rho<1\), \(\rho^{d-1}\to0\), so the exact formula differs from \(Q_d(2\rho^2-1)\) by a quantity tending to zero. This proves the threshold and, with \(2\rho_d^2-1=\lambda/\sqrt d\), the Gaussian critical window. Strict monotonicity lets us bracket each inverse quantile between fixed \(\lambda\pm\varepsilon\) windows, proving the quantile limit.

**4. Sharp rare-event rate, including the prefactor.** For fixed \(z\in(0,1)\), integration by parts gives
\[
\int_z^1(1-u^2)^{(d-3)/2}\,du
=\frac{(1-z^2)^{(d-1)/2}}{(d-1)z}
-\frac1{d-1}\int_z^1\frac{(1-u^2)^{(d-1)/2}}{u^2}\,du.
\]
The second term is a relative \(O_z(d^{-1})\) correction (for example by bounding \(u^{-2}\le z^{-2}\) and applying the same endpoint concentration). The gamma ratio gives \(c_d\sim\sqrt{d/(2\pi)}\). Therefore
\[
Q_d(z)\sim\frac{(1-z^2)^{(d-1)/2}}{z\sqrt{2\pi d}}.
\]
Write \(s=2\rho^2-1\) and \(B=\sqrt{1-s^2}=2\rho\sqrt{1-\rho^2}\). For \(s>0\), the outer/outer term is \(Q_d(s)\); its mixed contribution is negligible because \(\rho^{d-1}Q_d(\rho)/Q_d(s)=O_\rho(2^{-(d-1)})\). For \(s<0\), symmetry gives \(1-Q_d(s)=Q_d(|s|)\), and
\[
1-V_d(\rho)=\frac{Q_d(|s|)+2\rho^{d-1}(1-Q_d(\rho))+\rho^{2(d-1)}}{(1+\rho^{d-1})^2}.
\]
Here \(\rho^{d-1}/Q_d(|s|)\to0\), since \(B>\rho\) for \(\rho<1/\sqrt2\). Hence the same tail equivalent holds on both sides. Because replacing \(\rho\) with \(\sqrt{1-\rho^2}\) sends \(s\) to \(-s\) and leaves \(B\) invariant, the rare-event duality follows.

For the strict finite-dimensional inequality, the exact formula and \(2\rho^2-1<\rho\) imply \(V_d(\rho)<Q_d(2\rho^2-1)\): on mixed pairs the threshold is stricter, and on inner/inner pairs visibility is impossible. Applying the same inequality at the complementary radius and using \(Q_d(z)+Q_d(-z)=1\) proves the claim.

**5. Thin-shell coefficient.** For fixed \(d\), as \(z\uparrow1\),
\[
Q_d(z)\sim\frac{c_d2^{(d-1)/2}}{d-1}(1-z)^{(d-1)/2}.
\]
With \(\rho=1-\varepsilon\), the outer/outer threshold is \(2\rho^2-1=1-4\varepsilon+O(\varepsilon^2)\), while the mixed threshold is \(\rho=1-\varepsilon\). The surface weight \(\rho^{d-1}\to1\). Substitution into the exact formula gives precisely the stated coefficient; the outer/outer contribution is \(2^{d-1}\) times the one-mixed-pair angular tail at leading order.

## Verification
Run `python verify_surface_shell_visibility.py` using Python 3 and only the standard library. The checker independently integrates the angular density, carries out exact rational polynomial integrations in odd dimensions, checks the planar and spatial special cases, and compares the proposed formula with *direct minimization of distance to the origin along random sampled segments* (eight fixed-seed simulation cases). It also exercises representative thin-shell constants, Gaussian windows, large-deviation equivalents, and monotonicity/duality inequalities. The analytic proof, not simulation or finite checks, supplies the quantifiers over all dimensions, radii, and asymptotic regimes.

## Relationship to prior work
Sidiropoulos [1], inspected through its complete publicly readable paper, derives the chord-length and dot-product distributions of independently sampled points on a **single** hypersphere and their concentration as dimension increases. The angular probability \(Q_d\) is accordingly prior knowledge, not a new finding. That paper does not study a shell with two boundary components or visibility of mixed-radius pairs, and does not state the two-component visibility formula or its transition, duality, and thin-shell consequences.

Balko, Jelínek, Valtr, and Walczak [2] define and analyze the **volume-uniform** Beer index and its higher-order variants, rather than a boundary-surface index. Their full available manuscript concerns global inequalities relating convexity measures. An additional published research result [3] explicitly computes *volume-uniform* shell visibility, with odd-dimensional rational laws and thin-shell behavior; its source text likewise does not give the present surface-area law. The different sampling weights and endpoint geometry preclude using those volume formulas as the present result. The exact cross-sphere event and the sharp high-dimensional rare-event and inverse-quantile laws are the distinguishing content. The original formula is not claimed to hold for volume-uniform sampling.

## Limitations
The geometric model is restricted to **concentric** Euclidean spheres and normalized boundary surface measure; it does not cover off-center holes, general convex shells, or volume-uniform sampling. The outer radius itself cannot be reconstructed from visibility, which is scale invariant. The thin-shell limit fixes dimension, while the large-dimensional equivalences fix the radius ratio or specify the Gaussian window; these statements do not imply a uniform two-parameter approximation. The displayed numerical checks are reproducibility diagnostics, not exhaustive or independent certification. Historical originality remains subject to possible inaccessible or unindexed prior formulas.

## References
1. P. Sidiropoulos, *N-sphere chord length distribution*, arXiv:1411.5639v1, first public 2014-11-20, https://arxiv.org/abs/1411.5639.
2. M. Balko, V. Jelínek, P. Valtr, B. Walczak, *On the Beer index of convexity and its variants*, arXiv:1412.1769v1, first public 2014-12-04, https://arxiv.org/abs/1412.1769.
3. *Exact visibility laws for concentric spherical shells in odd dimensions*, published research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-visibility-laws-for-concentric-spherical-shells-in-odd-dim--611519ee4958.
