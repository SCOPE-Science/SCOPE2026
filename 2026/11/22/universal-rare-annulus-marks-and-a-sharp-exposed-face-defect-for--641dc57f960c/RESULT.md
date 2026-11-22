# Universal rare-annulus marks and a sharp exposed-face defect for thin convex-meridian toroids

## Finding
Let \(L\subset\mathbb R^2\) be a compact convex body with nonempty interior, symmetric about the horizontal and vertical axes in coordinates \((x,z)\). Let \(a=\max_{(x,z)\in L}|x|\) and \(b=\max_{(x,z)\in L}z>0\). Write
\[
q=\max\{x:(x,b)\in L\}\in[0,a],
\]
so the top exposed horizontal face of \(L\) is \([-q,q]\times\{b\}\). For each \(R>a\), revolve the translate \((R,0)+L\) around the vertical axis to obtain a solid toroid \(T_R(L)\). Choose an unoriented affine plane with Euclidean-motion-invariant measure, conditioned on intersecting the solid in positive area, and condition further on an *annular* section.

Denote by \(\theta\in[0,\pi/2]\) the angle between its unit normal and the vertical axis, and by \(m\ge0\) its unsigned distance from the origin. The scaled annular marks are
\[
X_R=\frac{R\sin\theta}{b},\qquad Y_R=\frac{m}{b}.
\]
Let \(\nu\) be the probability law on \(\mathbb R^2\) with density
\[
 f(x,y)=6x\,\mathbf 1_{\{x>0,\ y>0,\ x+y<1\}}.
\]
Then, as \(R\to\infty\),
\[
\mathcal L((X_R,Y_R)\mid\text{annular section})\xrightarrow{\mathrm{TV}}\nu,
\qquad
\boxed{\lim_{R\to\infty}R\,d_{\mathrm{TV}}\bigl(\mathcal L((X_R,Y_R)\mid\mathrm{annulus}),\nu\bigr)=2q.}
\]
In the limiting law, \(X\) has the \(\operatorname{Beta}(2,2)\) distribution and, conditionally on \(X=x\), \(Y\) is uniform on \((0,1-x)\). Thus the universal limiting mark law is independent of the meridian shape, while its *first-order total-variation defect* measures exactly the width of the meridian's exposed top face. The annulus event itself has the asymptotic probability
\[
 \Pr(\mathrm{annulus}\mid\mathrm{hit})\sim\frac{2b^3}{3\pi R^3}.
\]
The probability asymptotic is included to normalize the conditional law, not claimed as the main novelty.

If the meridian support function is twice continuously differentiable near the vertical direction, then \(q=0\) and the total-variation error improves to \(O(R^{-2})\). For the unit circular meridian, the latter has the sharp explicit constant
\[
\boxed{d_{\mathrm{TV}}\bigl(\mathcal L((X_R,Y_R)\mid\mathrm{annulus}),\nu\bigr)
=\left(\frac{27}{400}-\frac{9\sqrt{30}}{2500}\right)R^{-2}+O(R^{-4}).}
\]

## Assumptions and scope
The probability space is the standard motion-invariant measure on affine, unoriented planes, normalized after restricting to planes with positive-area intersection with \(T_R(L)\). Equivalently, a normal is Haar-uniform up to sign and the signed offset is distributed according to Lebesgue measure, followed by conditioning. The absolute offset \(m\) and the unsigned vertical normal coordinate define the marks without selecting an arbitrary orientation. The conditions \(L\) convex, compact, two-dimensional, axis-symmetric and \(R>a\) rule out self-intersections at the revolution axis and ensure the usual three generic section topologies. Tangent and transitional sections have invariant measure zero.

The horizontal and vertical meridian semiextents \(a,b\) are *fixed* as \(R\) increases. The exposed top-face half-width \(q\) may vanish, as for a strictly convex meridian, or be positive, as for a rectangle or a stadium with a horizontal cap. All convergence and \(o(\cdot)\), \(O(\cdot)\) statements hold for each fixed meridian; no uniformity over arbitrary changing meridians is asserted. The sharp circular formula is for a meridian disk of radius one, so \(b=1\).

## Proof
**1. Previously established fiber criterion and the correct invariant-plane density.** Write
\[
H(\theta)=h_L(\sin\theta,\cos\theta)
=\max_{(x,z)\in L}(x\sin\theta+z\cos\theta).
\]
Symmetry and convexity of the meridian imply that at a given inclination \(\theta\), the offsets giving an annular plane section are exactly
\[
0<m<H(\theta)-R\sin\theta,\qquad H(\theta)>R\sin\theta.\tag{1}
\]
This is the annular case of the fiber-topology classification in the published convex-meridian Crofton law (reference 2); for a circle it also follows from the two-coin slicing lemma in Finch (reference 1). To recall why, intersect the plane with the revolved meridian fibers indexed by azimuth. As the revolution radius exceeds every horizontal semiextent, the lower and upper support levels are strictly increasing in the azimuth cosine. Their extremal levels are \(\pm R\sin\theta\pm H(\theta)\). All azimuths are feasible precisely when the absolute offset lies below \(H(\theta)-R\sin\theta\), and the convex fibers then form an annulus. No new classification of the unmarked topologies is asserted.

For a Haar-uniform unoriented plane normal, \(u=|n_z|=\cos\theta\) has constant density on \([0,1]\); conditional on \(u\), Lebesgue offset measure is \(dm\). Hence the unnormalized plane measure in the \((u,m)\) coordinates is \(du\,dm\). This is essential: choosing the inclination angle uniformly would give a different sampling model.

**2. Exact density of the annular marks.** Put \(x=R\sin\theta/b\), \(y=m/b\), and
\[
G_R(x)=\frac{H(\arcsin(bx/R))}{b},\qquad
W_R(x)=\left(1-\frac{b^2x^2}{R^2}\right)^{-1/2}.
\]
The functions are used only for \(0\le bx/R\le1\). The change of variables gives
\[
|du\,dm|=\frac{b^3}{R^2}xW_R(x)\,dx\,dy.
\]
Define the finite positive normalizer
\[
J_R=\int_0^{R/b}xW_R(x)\,[G_R(x)-x]_+\,dx.
\tag{2}
\]
Then (1) yields the exact joint conditional density
\[
f_R(x,y)=\frac{xW_R(x)}{J_R}\,
\mathbf1_{\{x>0,\ y>0,\ y<G_R(x)-x\}}.
\tag{3}
\]
Every point in this support has \(bx=R\sin\theta<H(\theta)\le M\), where \(M=\max_{(x,z)\in L}\sqrt{x^2+z^2}\). Thus its \(x\)-coordinate lies in the fixed compact interval \([0,M/b]\) for all sufficiently large \(R\); there \(W_R(x)=1+O(R^{-2})\) uniformly.

**3. Exposed-face differentiation and the exact first-order defect.** The support function has the right derivative
\[
H(0)=b,\qquad H'(0+)=q.\tag{4}
\]
Indeed, supporting maximizers of \(x\sin\theta+z\cos\theta\) have accumulation points on the exposed face \(z=b\) as \(\theta\downarrow0\), and the maximal first-order horizontal coordinate on that face is \(q\). This gives the matching lower and upper directional derivatives. Consequently, uniformly for \(x\) in any bounded interval,
\[
G_R(x)=1+\frac{qx}{R}+o(R^{-1}).\tag{5}
\]
Uniformity follows from the definition of the right derivative: \(\arcsin(bx/R)=bx/R+O(R^{-3})\) on bounded intervals, and the support-function error is \(o(\theta)\) uniformly as \(\theta\downarrow0\).

Insert (5) and \(W_R=1+O(R^{-2})\) into (2). The positive-part map is Lipschitz. Since the limiting boundary is \(x=1\), and its displacement is \(O(R^{-1})\), the contribution of the short moving-endpoint interval is \(O(R^{-2})\). On \([0,1]\), integrate \(x(1-x+qx/R)\) to obtain
\[
J_R=\frac16+\frac{q}{3R}+o(R^{-1}).\tag{6}
\]
Equations (3)–(6) and compact support imply total-variation convergence to \(f(x,y)=6x\mathbf1_{\{x,y>0,x+y<1\}}\). Integrating \(f\) in \(y\) yields the \(\operatorname{Beta}(2,2)\) marginal and uniform conditional offset.

For \(q=0\), (5)–(6) and the finite support show directly that the \(L^1\) density discrepancy is \(o(R^{-1})\), giving the stated limit zero after multiplication by \(R\). If \(q>0\), then \(H(\theta)>b\) for all sufficiently small positive \(\theta\). Accordingly the entire limiting triangle \(\Delta=\{x>0,y>0,x+y<1\}\) lies in the support of \(f_R\) for sufficiently large \(R\). Furthermore, on \(\Delta\), equations (3) and (6) give \(f_R(x,y)<6x=f(x,y)\) for all sufficiently large \(R\), because \(W_R=1+O(R^{-2})\) and \(J_R=1/6+q/(3R)+o(R^{-1})\). Since both densities have mass one, their total-variation distance is exactly the \(f_R\)-mass outside \(\Delta\). The part with \(0<x<1\) has mass
\[
\frac1{J_R}\int_0^1xW_R(x)[G_R(x)-1]dx
=\frac{6q}{R}\int_0^1x^2dx+o(R^{-1})
=\frac{2q}{R}+o(R^{-1}).
\]
The small sliver with \(x>1\) contributes \(O(R^{-2})\). Therefore \(R\,d_{\mathrm{TV}}(f_R,f)\to2q\), including the \(q=0\) case.

**4. Annular probability and the smooth regime.** Before conditioning on the annular event, the total hit-plane measure is
\[
Z_R=\int_0^{\pi/2}(H(\theta)+R\sin\theta)\sin\theta\,d\theta
=C_L+\frac{\pi R}{4},
\]
where \(C_L=\int_0^{\pi/2}H(\theta)\sin\theta\,d\theta\) is fixed. The annular measure is \(b^3J_R/R^2\), so (6) gives \(\Pr(\mathrm{annulus}\mid\mathrm{hit})\sim2b^3/(3\pi R^3)\). This scalar asymptotic is already within reach of the earlier exact Crofton integral; its role here is to check conditional normalization. If \(H\) is \(C^2\) near zero, axial reflection forces \(H'(0)=0\), and Taylor expansion strengthens (5) to \(G_R(x)=1+O(R^{-2})\) on bounded \(x\)-intervals. In (2)–(3), all density and boundary discrepancies are then \(O(R^{-2})\), proving the claimed improved total-variation bound.

**5. Sharp circular coefficient.** For the disk meridian of radius one, \(H(\theta)=b=1\). In (2), the support is the fixed triangle \(\Delta\), and
\[
J_R=\int_0^1\frac{x(1-x)}{\sqrt{1-x^2/R^2}}dx
=\frac16+\frac1{40R^2}+O(R^{-4}).
\]
Therefore uniformly for \((x,y)\in\Delta\),
\[
\frac{f_R(x,y)}{f(x,y)}=1+\frac{x^2-3/10}{2R^2}+O(R^{-4}).
\]
As the marginal density of \(X\) is \(6x(1-x)\), the \(L^1\) identity for total variation and the Lipschitz property of absolute value give
\[
 d_{\mathrm{TV}}(f_R,f)=\frac{1}{4R^2}
 \int_0^1 6x(1-x)\left|x^2-\frac3{10}\right|dx+O(R^{-4})
=\left(\frac{27}{400}-\frac{9\sqrt{30}}{2500}\right)R^{-2}+O(R^{-4}).
\]
The positive coefficient is exact, and this calculation analytically establishes the next order where the exposed top face is a point.

## Verification
The standalone file `check_marks.py` independently integrates the circular marked density, recomputes the support-normalization identity and its total-variation coefficient, and numerically evaluates the general convex-meridian density for rectangles and ellipses with distinct semiaxes. It checks the observed approach \(R\,d_{\mathrm{TV}}\to2q\) for rectangles and the faster \(O(R^{-2})\) behavior for ellipses, using quadrature rather than simulation alone. The executed checker reported 109 successful assertions (Python 3, SciPy and SymPy). The numerical tests corroborate finite examples; the proof in this document, not those tests, covers every compact convex axis-symmetric meridian in the stated domain.

## Relationship to prior work
Finch's *Slicing a Doughnut at Random* (arXiv:2611.15546v1) proves the disk-section probability for a circular torus under the correct Haar–Crofton convention, gives the two-circle slicing classification and exercises for the unmarked topology probabilities. An earlier published published-finding corpus theorem, *A three-topology Crofton law and inverse support tomography for convex-meridian toroids* (reference 2), already establishes the full scalar topology law for axis-symmetric convex meridians, including the criterion (1) and the possibility of reconstructing a smooth meridian from the complete radius-dependent topology profile. The scalar probabilities, invariant-plane normalization, and topology criterion are deliberately credited rather than claimed as new.

The distinguishing statement here is the conditional *two-coordinate annular mark law* and its **sharp facial-width coefficient** \(\lim R\,d_{\mathrm{TV}}=2q\), valid even when the meridian has a nonsmooth exposed top face, plus the circular sharp second-order coefficient. The cited scalar theorems do not state these distributional limits or compare smooth and faceted meridians by their total-variation rates. Boukharfane's 2015 two-page solution addresses the aggregate disk probability with a uniform inclination integral; Finch explains why that weighting differs from the motion-invariant spatial-plane law. A separate central-plane area singularity result (reference 4) concerns zero-offset sections and does not determine affine annulus marks.

## Limitations
Exhaustive historical-priority certification is outside the scope of the theorem. The primary annular event is very rare, of order \(R^{-3}\); unconditional estimates cannot replace its correctly normalized conditional law. No uniform error bound is claimed over varying meridian families, and a one-point top face \(q=0\) only implies \(o(R^{-1})\) without further regularity. The sharper \(O(R^{-2})\) bound requires the specified local \(C^2\) support condition, and the explicit second-order constant is established only for a circular unit meridian. The top-face coefficient is not an assertion about general conditional laws for disk or two-disk sections. Overlap with older specialized stereological literature remains possible. Finite quadrature checks cannot certify the infinite-dimensional family.

## References
1. Steven R. Finch, *Slicing a Doughnut at Random*, arXiv:2611.15546v1, first made public 2026-11-11, https://arxiv.org/abs/2611.15546 . Relevant full text: §§4–7, especially Lemmas 15–16, formula (3) and Exercise 3.
2. *A three-topology Crofton law and inverse support tomography for convex-meridian toroids*, published-finding corpus (published 2026-10-18), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-three-topology-crofton-law-and-inverse-support-tomography-for--8cf34e87984a . The prior exact topology classification is used as input.
3. Radouan Boukharfane, *Slicing a Torus*, solution to Problem 11687, *American Mathematical Monthly* **122** (2015), pp. 177–178, https://doi.org/10.4169/amer.math.monthly.122.02.175 .
4. *Logarithmic area cusp and Haar topology law at the Villarceau transition*, published-finding corpus (published 2026-11-01), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-logarithmic-area-cusp-and-haar-topology-law-at-the-villarceau-tr--3f2e0b5e194a .
