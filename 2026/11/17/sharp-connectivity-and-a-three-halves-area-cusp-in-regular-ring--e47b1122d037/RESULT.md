# Sharp connectivity and a three-halves area cusp in regular-ring weighted Voronoi cells

## Finding
For each integer \(n\ge3\), radius \(R>0\), and multiplicative distance factor \(\lambda>1\), place a site at the origin with distance \(d_0(x)=\lVert x\rVert\), and place \(n\) competitors at the regular-ring sites \(v_j=R(\cos(2\pi j/n),\sin(2\pi j/n))\), with distances \(d_j(x)=\lambda\lVert x-v_j\rVert\). Let the **closed central Voronoi cell** be
\[
V_{n,\lambda}=\{x\in\mathbb R^2:d_0(x)\le d_j(x)\text{ for every }j\}.
\]
Set \(\beta=\pi/n\), \(s=\sin\beta\), \(h=\cos\beta\), and \(\lambda_*=1/s\). Then:

1. For \(1<\lambda<\lambda_*\), the central cell has **exactly two connected components**, a bounded disk-like central island \(K_{n,\lambda}\) containing the origin and an unbounded component. For \(\lambda\ge\lambda_*\), the central cell is connected; for \(\lambda>\lambda_*\), it is the complement of \(n\) pairwise disjoint open disks and has \(n\) bounded holes. At equality the excluded open disks touch at boundary points, which belong to the closed central cell.
2. Put \(C=\lambda^2R/(\lambda^2-1)\), \(r=\lambda R/(\lambda^2-1)\), and \(z=\lambda s\). For \(1<\lambda<\lambda_*\), the **exact central-island area** is
\[
\mathcal A_n(\lambda)=n\left[C^2sh+r^2\left(\beta-\arcsin z-z\sqrt{1-z^2}\right)\right].
\]
Its two endpoint limits are
\[
\lim_{\lambda\downarrow1}\mathcal A_n(\lambda)=\frac{nR^2}{4}\tan\beta,
\quad
\lim_{\lambda\uparrow\lambda_*}\mathcal A_n(\lambda)=\frac{nR^2}{h^4}\left[sh-s^2\left(\frac\pi2-\beta\right)\right]>0.
\]
3. Let \(H_n(\lambda)=n[C(\lambda)^2sh+r(\lambda)^2(\beta-\pi/2)]\), an analytic function near \(\lambda_*\). There is an exact **three-halves cusp** in the surviving bounded-island area as the two components merge:
\[
\mathcal A_n(\lambda)-H_n(\lambda)=
\frac{2n}{3}\left(\frac{Rs}{h^2}\right)^2(2s)^{3/2}
(\lambda_*-\lambda)^{3/2}+O_{n,R}((\lambda_*-\lambda)^{5/2}).
\]
For example, for a square ring with \(R=1\), the connectivity threshold is \(\lambda_*=\sqrt2\) and the limiting bounded-island area is \(8-2\pi\).

## Assumptions and scope
All distances are Euclidean and all sites lie in the entire plane. The factor \(\lambda\) **multiplies** a competitor's Euclidean distance rather than dividing it. Equivalently, the usual site weight assigned to every competitor is \(1/\lambda\), and the origin weight is one. Distinct sites are exactly the origin and the regular-ring sites. Ties belong to the central cell. The unbounded component's area is infinite, so \(\mathcal A_n\) refers only to the bounded connected component for \(1<\lambda<\lambda_*\); the critical limiting area is not a positive-area connected component in isolation at equality.

## Proof
**Disk representation.** Squaring the inequalities (all distances are nonnegative) gives
\[
(\lambda^2-1)\lVert x\rVert^2-2\lambda^2\langle x,v_j\rangle+\lambda^2R^2\ge0.
\]
Completing the square yields the exact equality
\[
V_{n,\lambda}=\mathbb R^2\setminus\bigcup_{j=0}^{n-1}B(Cu_j,r),
\quad u_j=v_j/R,
\]
where \(B(y,r)\) denotes the **open** Euclidean disk. Because \(C/r=\lambda>1\), the origin lies outside every excluded disk. The distance between adjacent exclusion-disk centers is \(2C\sin\beta\), whereas all nonadjacent center distances are no smaller. Thus consecutive disks overlap as open sets exactly when \(r>C\sin\beta\), equivalently \(\lambda<\lambda_*\).

**Every radial section and connectivity.** Write \(x=t(\cos\theta,\sin\theta)\) with \(t\ge0\). Choose the nearest ring direction \(u_j\); its angular separation \(\delta\) satisfies \(|\delta|\le\beta<\pi/2\). At fixed \(t\), that disk center is the nearest of all ring centers, since squared distance is \(t^2+C^2-2Ct\cos\delta\). Consequently the union of excluded disks meets the ray precisely in the set of nonnegative \(t\) satisfying
\[
t^2-2Ct\cos\delta+C^2-r^2<0.
\]
For \(\lambda<\lambda_*\) the discriminant is strictly positive for every \(|\delta|\le\beta\), and the excluded interval has endpoints
\[
\rho_\pm(\delta)=C\cos\delta\pm\sqrt{r^2-C^2\sin^2\delta}.
\]
Both endpoints are positive and continuous in the angular variable, including sector boundaries. Hence the central cell consists of exactly the closed radial subgraph \(0\le t\le\rho_-(\delta)\) and the closed radial epigraph \(t\ge\rho_+(\delta)\). A positive separation exists uniformly over angles by compactness, so these are two distinct connected components, each path connected. When \(\lambda\ge\lambda_*\), all open excluded disks have mutually disjoint interiors. The complement of finitely many pairwise interior-disjoint open disks in the plane is path connected (tangent boundary points remain available); hence the central cell has one component. If \(\lambda>\lambda_*\), all closed disks are disjoint and the complement has exactly \(n\) bounded complementary components. For every \(\lambda>1\), the cell is not star-shaped at the origin: it contains the origin and all sufficiently distant points on a ring-site ray, but excludes an intermediate interval.

**Exact area.** By \(n\)-fold rotational symmetry and the polar area element,
\[
\mathcal A_n(\lambda)=n\int_0^\beta\rho_-(\delta)^2\,d\delta.
\]
The squared integrand expands as
\[
\rho_-^2=C^2\cos(2\delta)+r^2
-2C\cos\delta\sqrt{r^2-C^2\sin^2\delta}.
\]
Use \(y=C\sin\delta\) and the elementary antiderivative
\[
\int\sqrt{r^2-y^2}\,dy
=\frac12\bigl(y\sqrt{r^2-y^2}+r^2\arcsin(y/r)\bigr).
\]
Since \(Cs/r=\lambda s=z<1\), the stated exact area follows with no approximations.

**Limits and nonanalytic term.** As \(\lambda\downarrow1\), the radial first-contact distance \(\rho_-(\delta)\) tends uniformly on \([-\beta,\beta]\) to \(R/(2\cos\delta)\), giving the area of the regular \(n\)-gonal ordinary Voronoi cell, namely \(nR^2\tan\beta/4\). At \(\lambda_*\), direct substitution of \(C_*=R/h^2\) and \(r_*=Rs/h^2\) in the area formula gives the positive second limit. Positivity also follows because the limiting radial first-contact distance is positive for a full set of angles.

Finally write \(z=\lambda s\). The analytic part is \(H_n\); the remainder is exactly
\[
\mathcal A_n-H_n=n r^2\left[\arccos z-z\sqrt{1-z^2}\right].
\]
For \(z\uparrow1\), set \(w=\sqrt{1-z^2}\). Taylor's theorem applied to \(\arcsin w\) and \(\sqrt{1-w^2}\) gives
\[
\arccos z-z\sqrt{1-z^2}=\arcsin w-w\sqrt{1-w^2}
=\frac23 w^3+O(w^5).
\]
Also \(1-z^2=2s(\lambda_*-\lambda)+O((\lambda_*-\lambda)^2)\) and \(r=r_*+O(\lambda_*-\lambda)\). Substitution proves the explicit positive \(3/2\)-cusp coefficient and remainder for each fixed \(n\) and \(R\).

## Verification
The reproducible standard-library program `verify.py` compares the exact area formula against independent radial Simpson quadrature on 30 parameter triples, confirms exclusion-circle adjacency conditions in 18 cases, compares radial membership with the defining weighted-distance inequalities on 520 test points, and checks the limiting cusp amplitude in eight near-critical cases. It passed all 576 comparisons. These finite checks corroborate the formula but do not replace the all-parameter proof above.

## Relationship to prior work
The weighted Voronoi distance model, circular bisectors, and possible disconnected cells or holes are established prior theory, not new claims. Gudmundsson, Seybold and Wong (2024) describe general multiplicatively weighted Voronoi diagrams, Apollonian bisectors, and holes, with a focus on approximation algorithms rather than this rotationally symmetric exact connectivity/area law. Venkovic and Anzt (2026) treat planar site-dependent anisotropic Voronoi geometry through contact-function Minkowski tensors for cells star-convex at their nucleation points. The present equal-isotropic-metric competitor configuration is inside the wider site-dependent-metric setting but lies outside its star-convex-at-the-site hypothesis. The novelty sought here is the exact all-\(n\) transition, central-island area, and quantified cusp, not the existence of holes or the general circular-bisector representation.

## Limitations
The 2026 motivating paper was inspected through its dated abstract; the full text was not accessible in this review. General weighted diagrams have extensive historical literature, and the complete ring-specific statement might be derivable from prior circle-union computations without being recorded with these parameters. The result is for one central site and a regular ring of equal competitor weights in the plane; no claim is made for irregular sites or arbitrary positive-definite metrics. The exterior component has infinite area. No independent mathematical audit has been performed.

## References
1. N. Venkovic and H. Anzt, *Minkowski Tensors of Planar Anisotropic Voronoi Diagrams*, publicly posted 2026-10-06, https://arxiv.org/abs/2610.08656.
2. J. Gudmundsson, M. P. Seybold, and S. Wong, *Approximating Multiplicatively Weighted Voronoi Diagrams: Efficient Construction with Linear Size*, SoCG 2024, https://doi.org/10.4230/LIPIcs.SoCG.2024.62 (open full text: https://drops.dagstuhl.de/storage/00lipics/lipics-vol293-socg2024/LIPIcs.SoCG.2024.62/LIPIcs.SoCG.2024.62.pdf).
3. P. F. Ash and E. D. Bolker, *Generalized Dirichlet Tessellations*, Geometriae Dedicata 20 (1986), https://doi.org/10.1007/BF00164401; historical background only, original full text not inspected.
