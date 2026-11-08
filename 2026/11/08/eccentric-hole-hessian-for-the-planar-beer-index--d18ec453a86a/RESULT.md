# Eccentric-hole Hessian for the planar Beer index

## Finding
For \(0<a<1\) and a displacement vector \(z\in\mathbb R^2\) with \(\lVert z\rVert<1-a\), define the planar circularly punctured domain
\[
A_{a,z}=\{x\in\mathbb R^2:\lVert x\rVert\le1,\ \lVert x-z\rVert\ge a\}.
\]
For independent normalized-area-uniform points \(X,Y\) in this domain, let
\[
b(a,z)=\Pr\bigl([X,Y]\subseteq A_{a,z}\bigr)
\]
be its Beer index (straight-segment visibility probability). For every fixed \(a\in(0,1)\), as \(z\to0\),
\[
\boxed{\ b(a,z)=\frac{2\bigl(\arccos a-a\sqrt{1-a^2}\bigr)}{\pi(1-a^2)}
+\frac{5a}{\pi(1-a^2)^{3/2}}\lVert z\rVert^2+O_a(\lVert z\rVert^4).\ }
\]
In particular, the concentric placement is a **strict, nondegenerate local minimum** of the visibility probability at every positive hole radius. The full two-coordinate Hessian is the scalar matrix
\[
\boxed{\ D_z^2 b(a,0)=\frac{10a}{\pi(1-a^2)^{3/2}}I_2.\ }
\]
The coefficient tends to zero as \(a\downarrow0\) and diverges as \(a\uparrow1\), quantifying the local instability of thin concentric annuli under hole displacement. No global-in-displacement extremality is asserted.

## Assumptions and scope
The outer disk has radius one, and the inner removed open disk has radius \(a\); \(\lVert z\rVert<1-a\) ensures strict containment. Points are sampled independently by two-dimensional Lebesgue area, not by boundary arclength. Segment visibility means the entire Euclidean straight segment avoids the *open* inner disk; tangencies and boundary point choices have probability zero. Scaling gives the same theorem for any outer radius \(R\) with dimensionless parameters \(a=r/R\), \(z=w/R\). The asymptotic is for each fixed \(a\in(0,1)\), with no claim of an error bound uniform as \(a\) approaches zero or one.

## Proof
**1. Line-coordinate identity.** For an unoriented line parameterized by normal \(n_\theta=(\cos\theta,\sin\theta)\), tangent \(t_\theta=(-\sin\theta,\cos\theta)\), and signed offset \(p\), any ordered pair of distinct points on this line can be written \(x=pn_\theta+st_\theta\), \(y=pn_\theta+ut_\theta\). The direct change-of-variables determinant is \(\lvert s-u\rvert\), so
\[
\int_{\mathbb R^2}\!\int_{\mathbb R^2}F(x,y)\,dx\,dy
=\int_0^\pi\!\int_{\mathbb R}\!\int_{\mathbb R}\!\int_{\mathbb R}F(pn_\theta+st_\theta,pn_\theta+ut_\theta)\lvert s-u\rvert\,ds\,du\,dp\,d\theta.
\]
The exceptional diagonal has measure zero. This identity also fixes the normalization: the total integral over \(A_{a,z}^2\) is \(\pi^2(1-a^2)^2\).

**2. Crossing pairs on each line.** Rotational invariance permits \(z=(e,0)\) with \(e=\lVert z\rVert\). Put \(q=p-e\cos\theta\), \(L=\sqrt{1-(q+e\cos\theta)^2}\), and \(h=\sqrt{a^2-q^2}\), for \(\lvert q\rvert<a\). The outer disk cuts the line in \([-L,L]\), while the inner disk cuts it in \([-e\sin\theta-h,-e\sin\theta+h]\). Thus the surviving left and right intervals have respective lengths
\[
\ell=L-h-e\sin\theta,\qquad r=L-h+e\sin\theta.
\]
They are nonnegative because the hole lies in the outer disk. Exactly the pairs with endpoints on opposite surviving intervals are nonvisible. Their ordered \(\lvert s-u\rvert\)-weighted integral is
\[
2\ell r(L+h)=2\left[(L-h)^2-e^2\sin^2\theta\right](L+h),
\]
since the difference of the intervals' mean coordinates is \(L+h\). Consequently the *exact* nonvisibility probability is
\[
P_a(e)=1-b(a,e)=\frac{1}{\pi^2(1-a^2)^2}
\int_0^\pi\!\int_{-a}^a 2\bigl[(L-h)^2-e^2\sin^2\theta\bigr](L+h)\,dq\,d\theta.
\tag{1}
\]

**3. The concentric term.** Setting \(e=0\), let \(L_0(q)=\sqrt{1-q^2}\). Direct elementary integration gives
\[
\int_{-a}^a2(L_0-h)^2(L_0+h)\,dq
=2(1-a^2)\left[a\sqrt{1-a^2}+\arcsin a-\frac{\pi a^2}{2}\right].
\]
Using \(\arcsin a+\arccos a=\pi/2\) in (1) yields
\[
b(a,0)=\frac{2(\arccos a-a\sqrt{1-a^2})}{\pi(1-a^2)}.
\]
This concentric value is an established published formula, not a new claim.

**4. Exact second variation.** With \(h\) held fixed during differentiation, define \(F(L,h)=2(L-h)^2(L+h)\). For \(0\le e<1-a\), all square-root arguments for \(L\) remain uniformly positive near \(e=0\), and differentiation under both integrals in (1) is legitimate. Angular averaging eliminates the linear term and gives the coefficient of \(e^2\) in the numerator's \(\theta\)-average as
\[
G_a(q)=\frac14\left.\frac{\partial^2}{\partial p^2}F(\sqrt{1-p^2},h)\right\rvert_{p=q}-(L_0+h).
\]
Elementary differentiation and \(h^2=a^2-q^2\) simplify this to
\[
G_a(q)=\frac{4q^2-5/2}{\sqrt{1-q^2}}+\frac{a^2-q^2}{2(1-q^2)^{3/2}}.
\]
The three exact integration identities
\[
\int_{-a}^a\!\frac{dq}{\sqrt{1-q^2}}=2\arcsin a,\qquad
\int_{-a}^a\!\frac{q^2\,dq}{\sqrt{1-q^2}}=\arcsin a-a\sqrt{1-a^2},
\]
\[
\int_{-a}^a\!\frac{a^2-q^2}{(1-q^2)^{3/2}}\,dq=2\arcsin a-2a\sqrt{1-a^2}
\]
therefore imply
\[
\int_{-a}^aG_a(q)\,dq=-5a\sqrt{1-a^2}.
\]
Substitution into (1) proves the claimed positive coefficient of \(e^2\). Changing \(e\) to \(-e\) is the rotation \(x\mapsto-x\). The integrand in (1) is real-analytic in \(e\) near zero for each fixed \(a<1\), uniformly on the compact integration domain, so the entire probability is even real-analytic and the next error term is \(O_a(e^4)\). Rotational invariance upgrades this scalar expansion to the stated two-coordinate Hessian. Positivity of the coefficient proves strict local minimality.

## Verification
A dependency-free standard-library Python implementation, `verify_eccentric_visibility.py`, evaluates (1) by two midpoint quadratures after the smooth substitution \(q=a\sin u\), \(u\in[-\pi/2,\pi/2]\). It compares the centered probability with the known closed formula and numerical small-displacement differences with the analytically derived coefficient for \(a=0.2,0.5,0.8\). An *independent* finite-sample test samples endpoint pairs directly by area and checks the minimum squared distance of each segment to the displaced-hole center. Run `python verify_eccentric_visibility.py`; the expected final line is `ECCENTRIC_BEER_LOCAL_HESSIAN_AND_DIRECT_SEGMENTS_OK`. Finite quadrature and Monte Carlo are diagnostics, not substitutes for the analytic proof.

## Relationship to prior work
The Beer index is the two-point visibility functional introduced by Beer and studied in detail by Balko, Jelínek, Valtr, and Walczak. Hodge, Marshall, and Patterson explicitly computed the concentric-annulus formula used as the baseline above. The published exact shell-visibility results for concentric spherical shells cover a different, nontranslated family and likewise acknowledge the prior planar formula. None of those inspected statements determines the Hessian with respect to *displacing the inner disk while fixing its radius and the outer boundary*. In particular, varying the radius in the known concentric expression is not equivalent to translating the inner disk, because the latter changes the domain without changing its area. The new contribution is solely the full, sharp positive-definite translational Hessian and its local-minimality consequence.

## Limitations
No claim of global minimality for arbitrary \(0<e<1-a\), higher-dimensional shells, multiply punctured domains, or boundary-sampled endpoints is made. The positive quadratic form governs small displacements at a fixed hole radius only. The coefficient becomes singular in the thin-annulus limit; the asymptotic remainder here is not uniform in that limit. Historical-priority searches cannot establish novelty, and independent mathematical audit remains outstanding.

## References
1. G. A. Beer, “The index of convexity and the visibility function,” *Pacific Journal of Mathematics* 44 (1973), 59–67.
2. J. K. Hodge, E. A. Marshall, G. Patterson, “Gerrymandering and Convexity,” *College Mathematics Journal* 41 (2010), 312–324, DOI:10.4169/074683410X510317. Accessible text: https://paperzz.com/doc/7735005/gerrymandering-and-convexity---mathematical-association-o...
3. M. Balko, V. Jelínek, P. Valtr, B. Walczak, “On the Beer index of convexity and its variants,” first publicly posted 2014-12-04, arXiv:1412.1769v1, https://arxiv.org/abs/1412.1769; subsequently *Discrete & Computational Geometry* 57 (2017), 179–214, DOI:10.1007/s00454-016-9821-3. Its published primary MSC classification is 52A27.
4. “Exact visibility laws for concentric spherical shells in odd dimensions,” published 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-visibility-laws-for-concentric-spherical-shells-in-odd-dim--611519ee4958. The full scientific result was examined; it explicitly credits [2] for the planar concentric calculation.
