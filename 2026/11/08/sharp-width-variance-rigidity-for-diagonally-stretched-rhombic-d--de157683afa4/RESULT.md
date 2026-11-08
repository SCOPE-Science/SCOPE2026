# Sharp width-variance rigidity for diagonally stretched rhombic dodecahedra

## Finding
Let
\[
R=\operatorname{conv}\bigl(\{(\pm2,0,0),(0,\pm2,0),(0,0,\pm2)\}\cup\{(\pm1,\pm1,\pm1)\}\bigr)\subset\mathbb R^3.
\]
Here the last set contains all eight sign combinations. This is the regular rhombic dodecahedron, the standard shape of the face-centered cubic (FCC) Voronoi cell. For arbitrary positive axial factors \(a,b,c\), consider \(R_{a,b,c}=\operatorname{diag}(a,b,c)R\) and write \(S=a^2+b^2+c^2\). Let \(U\) be uniform on the unit sphere and \(W=h_{R_{a,b,c}}(U)+h_{R_{a,b,c}}(-U)\).

Define
\[
\rho_a=\frac{2a^2}{S}-1,\quad \rho_b=\frac{2b^2}{S}-1,\quad\rho_c=\frac{2c^2}{S}-1,\qquad
\Phi(t)=\sqrt{1-t^2}+t\arcsin t.
\]
**Theorem (exact moments, sharp extrema and rigidity).** For every \(a,b,c>0\),
\[
\boxed{\mathbb EW=2\sqrt S,\qquad
\mathbb E W^2=\frac{4S}3+\frac{8S}{3\pi}
\bigl[\Phi(\rho_a)+\Phi(\rho_b)+\Phi(\rho_c)\bigr].}
\]
At fixed \(S>0\), the mean width is independent of anisotropy, whereas the variance has the sharp range
\[
\boxed{V_*\le\operatorname{Var}(W)<\frac{4S}3},\qquad
V_*=\frac S3\left[\frac{16}\pi\left(\sqrt2-\arcsin\frac1{\sqrt3}\right)-4\right].
\]
The lower equality holds **if and only if** \(a=b=c=\sqrt{S/3}\). The upper endpoint is an unattained supremum, approached as two axes shrink toward zero. Every intermediate value of variance is attained. Moreover, for all positive triples,
\[
\boxed{\operatorname{Var}(W)-V_*\ge\frac{16}{3\pi S}
\left[(a^2-S/3)^2+(b^2-S/3)^2+(c^2-S/3)^2\right].}
\]
The stability inequality is strict except at the regular shape. For the unscaled regular cell \(a=b=c=1\), the mean is \(2\sqrt3\), its exact squared width mean is \(8+(16/\pi)(\sqrt2-\arcsin(1/\sqrt3))\), and its variance is approximately \(0.067918113012\).

## Assumptions and scope
The three scaling factors are arbitrary strictly positive real numbers. Fixed scale means the sum of their squares \(S\), not fixed volume or surface area. Directional width uses Euclidean supporting planes in the uniformly random **normal** direction. This is the usual rotationally invariant probability on the sphere. The theorem addresses the three-axis diagonal affine family of the specified rhombic dodecahedron; it does not encompass arbitrary shears or all rhombic dodecahedra.

## Proof
**1. Four-segment representation.** Let \(t_1=(1,1,1)\), \(t_2=(1,-1,-1)\), \(t_3=(-1,1,-1)\), \(t_4=(-1,-1,1)\). Consider the centered zonotope
\[
Z=\sum_{i=1}^4[-t_i/2,t_i/2].
\]
Its sixteen endpoint sums \(\frac12\sum_i\varepsilon_i t_i\), for \(\varepsilon_i\in\{-1,1\}\), are precisely the fourteen displayed vertices of \(R\) together with the origin (appearing twice). Hence \(Z=R\). Support functions add under Minkowski sums, so
\[
W(u)=\sum_{i=1}^4 |\langle \operatorname{diag}(a,b,c)t_i,u\rangle|.
\tag{1}
\]
This is independently checked against the fourteen-vertex support function by the companion program.

**2. Two-point absolute-moment kernel.** Put \(v_i=\operatorname{diag}(a,b,c)t_i\), with common squared length \(\|v_i\|^2=S\). A uniformly oriented vector on \(S^2\) satisfies \(\mathbb E|\langle U,v_i\rangle|=\|v_i\|/2\), so summing (1) gives \(\mathbb EW=2\sqrt S\). If \(G\) is standard Gaussian in \(\mathbb R^3\), then \(G=TU\), where the radius is independent of \(U\) and \(\mathbb ET^2=3\). For two vectors of equal squared length \(S\) and correlation \(\rho=(v_i\cdot v_j)/S\), the standard planar Gaussian absolute-product integral yields
\[
\mathbb E|\langle G,v_i\rangle\langle G,v_j\rangle|
=\frac{2S}\pi\left(\sqrt{1-\rho^2}+\rho\arcsin\rho\right)
=\frac{2S}\pi\Phi(\rho).
\]
For completeness, represent a correlated Gaussian pair as \((T_2\cos\theta,T_2\cos(\theta-\arccos\rho))\) with uniform planar angle \(\theta\) and \(\mathbb ET_2^2=2\); integrating the absolute product on the circle gives \(2\Phi(\rho)/\pi\). Dividing by \(3\) gives the spherical cross-moment \(2S\Phi(\rho)/(3\pi)\). The diagonal moments are \(S/3\).

For the six unordered pairs of distinct generators \(v_i\), the three correlations
\[
\rho_a=\frac{a^2-b^2-c^2}S,\qquad
\rho_b=\frac{b^2-a^2-c^2}S,\qquad
\rho_c=\frac{c^2-a^2-b^2}S
\]
each occur exactly twice. Expanding the square of (1), collecting four diagonal and twelve cross terms, proves the stated exact second moment. Subtracting \((\mathbb EW)^2=4S\) gives
\[
\operatorname{Var}(W)=\frac{8S}{3\pi}\sum_{q\in\{a,b,c\}}\Phi(\rho_q)-\frac{8S}3.
\tag{2}
\]

**3. Rigidity and quantitative stability.** Observe that \(\rho_a+\rho_b+\rho_c=-1\). For \(-1<t<1\),
\[
\Phi'(t)=\arcsin t,\qquad
\Phi''(t)=\frac1{\sqrt{1-t^2}}\ge1.
\]
Strict convexity and Jensen's inequality imply that the sum in (2) is uniquely minimized at the common correlation \(-1/3\), equivalent to \(a^2=b^2=c^2=S/3\). The tangent inequality
\[
\Phi(t)\ge\Phi(-1/3)+\Phi'(-1/3)(t+1/3)+\frac12(t+1/3)^2
\]
combined with \(\sum(\rho_q+1/3)=0\) and \(\rho_q+1/3=2(q^2-S/3)/S\) proves the stated variance stability coefficient. Equality in the sum can hold only when all three axes agree. Substituting \(\Phi(-1/3)=2\sqrt2/3+\arcsin(1/3)/3\), and the elementary identity \(\arcsin(1/3)+2\arcsin(1/\sqrt3)=\pi/2\), yields the closed formula for \(V_*\).

**4. Sharp unattained upper bound.** For all \(t\in[-1,1]\), \(\Phi(t)\le\pi/2\), with equality only at \(|t|=1\), since \(\Phi'(t)=\arcsin t\) and \(\Phi\) is even and increasing on \([0,1]\). Strict positivity of the three axes forces \(-1<\rho_a,\rho_b,\rho_c<1\). Thus (2) yields \(\operatorname{Var}(W)<4S/3\). Along the positive-axis family with squares \(a^2=S(1-2\varepsilon)\), \(b^2=c^2=S\varepsilon\), \(0<\varepsilon<1/2\), \(\varepsilon\downarrow0\) gives correlations tending to \((1,-1,-1)\) and the variance tending to \(4S/3\). The equal-axis point gives \(V_*\); continuity along paths in the connected fixed-\(S\) positive octant supplies every intermediate variance. \(\square\)

## Verification
Run the standalone Python 3 program `verify_rhombic_width.py`. It enumerates all four-generator sign sums, verifies the fourteen nonzero vertices, compares the generator and direct-vertex width formulas at 9,000 random orientations, compares exact moments against uniform-sphere Monte Carlo at three anisotropies (80,000 orientations each), tests the stability and upper bounds at 30,000 random scale triples, and checks the trigonometric closed form for the regular case. Its observed final marker is `RHOMBIC_WIDTH_OK`. These finite checks support but do not replace the exact proof.

## Relationship to prior work
Lucarini [1] identifies the rhombic dodecahedron as the Voronoi cell of the FCC lattice and analyzes random positional perturbations of crystal lattices; it neither computes directional-width moments nor optimizes their variance under deterministic diagonal stretching. Finch [2] computed squared width moments of the regular tetrahedron and cube, not the rhombic dodecahedron. Kabluchko--Litvak--Zaporozhets [3] give general random-projection moment machinery and evaluate the cube, simplex, and crosspolytope, but not the fixed-mean variance extremum for this FCC-cell affine family. The standard bivariate-Gaussian absolute-product identity is an acknowledged ingredient, not new. Existing exact formulas for widths of the five Platonic solids do not include this non-Platonic cell, and published tree graphical-zonotope variance extremizers concern an unweighted graph-root family in a different Euclidean space; their combinatorial extremal comparison does not imply (2) or its diagonal-shape rigidity. The distinct assertion here is the complete anisotropic moment profile, strict isometric-axis extremality, sharp upper boundary, and quantitative variance stability in the three-parameter FCC-cell family.

## Limitations
The proof does not claim a new general Gaussian absolute-moment identity or general zonotope moment formula. The normalization fixes the sum of squared axial factors, not the determinant, area, or an arbitrary affine-invariant size. The upper supremum is approached only by degenerating axis triples and is not attained in the positive three-axis class. The quadratic stability coefficient is uniform and valid but is **not** asserted to be the best possible coefficient. An unindexed equivalent classical width-variance inequality for tetrahedral zonohedra remains a historical-priority risk. Numerical checks do not independently certify the all-parameter claim.

## References
1. V. Lucarini, *Symmetry-Break in Voronoi Tessellations*, Symmetry 1 (2009), 21–54, published 20 August 2009, https://doi.org/10.3390/sym1010021. A dated University of Reading preprint is available as MPS_2009-07 (dated 4 August 2009); this dated cover alone does not establish an earlier public upload.
2. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671, original public version 4 October 2011, https://arxiv.org/abs/1110.0671.
3. Z. Kabluchko, A. E. Litvak and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479, original public version 26 November 2015, https://arxiv.org/abs/1511.08479.
