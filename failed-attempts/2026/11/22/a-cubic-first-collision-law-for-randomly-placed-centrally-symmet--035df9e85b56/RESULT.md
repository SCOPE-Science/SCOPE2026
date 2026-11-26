# A cubic first-collision law for randomly placed centrally symmetric polygons

## Finding
Let \(P\subset\mathbb R^2\) be a nondegenerate centrally symmetric convex polygon normalized to Euclidean diameter one. Rotate \(K_\varepsilon=(1+\varepsilon)P\) uniformly by \(\Theta\in[0,2\pi)\), and independently translate it by Haar-uniform \(T\in\mathbb R^2/\mathbb Z^2\). Write \(N_\varepsilon=\#((R_\Theta K_\varepsilon+T)\cap\mathbb Z^2)\). All results below concern fixed \(P\) as \(\varepsilon\downarrow0\).

Let \(\mathcal D\) denote the finite set of unordered antipodal pairs of vertices \(\{-v_j,v_j\}\) with \(\|2v_j\|=1\). At \(-v_j\), orient the first local axis toward \(v_j\). The two inward edge rays have slopes \(m_j^-<m_j^+\) relative to that axis. They have positive first coordinates; define their dimensionless slope gap \(h_j=m_j^+-m_j^->0\). Then
\[
\boxed{\Pr(N_\varepsilon=2)=\frac{\varepsilon^3}{3\pi}\sum_{j\in\mathcal D}h_j^2+O_P(\varepsilon^4).}
\]
For sufficiently small positive \(\varepsilon\), the entire lattice-point-count distribution is exactly supported on \(\{0,1,2\}\). If \(p_2(\varepsilon)=\Pr(N_\varepsilon=2)\) and \(A=\operatorname{area}(P)\), then
\[
\Pr(N_\varepsilon=1)=(1+\varepsilon)^2A-2p_2(\varepsilon),\qquad
\Pr(N_\varepsilon=0)=1-(1+\varepsilon)^2A+p_2(\varepsilon).
\]
The exact three-atom identity is previously known in greater generality; the new assertion is the sharp polygonal cubic coefficient and its angular mark.

Specifically, choose any one of the finitely many alignment neighborhoods associated with a specified antipodal diameter pair and a signed unit lattice direction. Let \(\alpha\) denote the small signed relative angle in that neighborhood and set \(u_\varepsilon=(\alpha/\varepsilon+m_j^+)/h_j\). Conditional on a two-point encounter through that neighborhood, \(u_\varepsilon\) converges in distribution to the density \(6u(1-u)\) on \([0,1]\), the \(\operatorname{Beta}(2,2)\) law. The sign convention for \(\alpha\) is chosen so the local displacement is \(\varepsilon(1,-\alpha/\varepsilon)+O(\varepsilon^2)\); reversing this convention replaces \(u\) with \(1-u\), leaving the law unchanged.

For a regular even \(n\)-gon of circumradius \(1/2\), with \(n\ge4\), there are \(n/2\) diameter pairs, each with \(h=2\cot(\pi/n)\), hence
\[
\boxed{p_2(\varepsilon)=\frac{2n}{3\pi}\cot^2(\pi/n)\varepsilon^3+O_n(\varepsilon^4).}
\]

## Assumptions and scope
The polygon must have nonempty area, central symmetry, and a fixed finite number of edges. Euclidean diameter is exactly one. Diameter vertices are precisely the vertices lying on the radius-\(1/2\) circumscribed circle about the symmetry center. Every such vertex is strictly exposed in its radial direction, which guarantees that its two inward edge rays have strictly positive components along the inward diameter axis and finite slope gap. The probability measure is product Haar measure for planar orientation and lattice translation. The asymptotic constants and error bound can depend on the fixed polygon; neither is claimed uniform under polygon-to-circle limits.

## Proof
**1. Exact low-occupancy identity.** Any three distinct points of the square lattice contain two at Euclidean distance at least \(\sqrt2\): otherwise all three mutual distances would be one, contradicting bipartiteness of the lattice's unit-edge graph. Thus \(N_\varepsilon\le2\) when \(1+\varepsilon<\sqrt2\). Any two present lattice points must differ by one of the four signed coordinate unit vectors. For \(g_K(z)=\operatorname{area}(K\cap(K+z))\), translational unfolding yields
\[
\Pr(N_\varepsilon=2)=\frac1{2\pi}\int_0^{2\pi}\!\big[g_{R_\theta K_\varepsilon}(e_1)+g_{R_\theta K_\varepsilon}(e_2)\big]d\theta.
\]
Also \(\mathbb EN_\varepsilon=(1+\varepsilon)^2A\), giving the other atoms. This covariogram identity is background, not the priority claim.

**2. Localization at extreme vertices.** Since \(P=-P\), its diameter equals \(2\max_{x\in P}\|x\|\). Equality in the triangle inequality shows all diameter pairs are antipodal and have endpoints of norm \(1/2\); strict convexity of the squared Euclidean norm over polygon edges shows these are vertices. A unit difference vector can be contained in \((1+\varepsilon)(P-P)\) only in orientation neighborhoods approaching those diameter directions as \(\varepsilon\to0\). Compactness and finiteness of vertex pairs separate these neighborhoods. The inward tangent cone \(C_j\) of \(P\) at \(-v_j\) is the wedge
\[
C_j=\{(x,y):x\ge0,\ m_j^-x\le y\le m_j^+x\}.
\]
Its opposite vertex has cone \(-C_j\) by central symmetry. Since all nonadjacent polygon constraints have strictly positive slack in a fixed neighborhood of the contact vertices, the small intersection is exactly that of the translated endpoint wedges whenever the overlap is nonempty and sufficiently small.

**3. Exact wedge calculation and angular scaling.** In local diameter-aligned coordinates, the displacement between the opposite apexes is
\[
b_\varepsilon(\alpha)=\big((1+\varepsilon)-\cos\alpha,-\sin\alpha\big).
\]
For any \(b=(b_x,b_y)\) inside \(C_j\), direct integration over the intersection of the two opposite cones gives the exact parallelogram area
\[
\operatorname{area}\big(C_j\cap(b-C_j)\big)=
\frac{(m_j^+b_x-b_y)(b_y-m_j^-b_x)}{m_j^+-m_j^-},
\]
with area zero outside \(C_j\). (Integrate the vertical section between the four boundary lines, or compute the determinant of two independent edge vectors.) For \(\alpha=\varepsilon t\), the area is uniformly
\[
\varepsilon^2\frac{(m_j^++t)(-m_j^--t)}{h_j}+O_P(\varepsilon^3)
\]
for \(-m_j^+\le t\le-m_j^-\), and zero outside a window with endpoints shifted by \(O_P(\varepsilon)\) in \(t\). Indeed \(b_x=\varepsilon+O(\varepsilon^2)\), \(b_y=-\varepsilon t+O(\varepsilon^3)\). The window is compact for each fixed polygon, so the error is uniform. Integrating gives
\[
\int_{\mathrm{one\ branch}}g_{R_\theta K_\varepsilon}(e_i)d\theta
=\varepsilon^3\int_{-m_j^+}^{-m_j^-}
\frac{(m_j^++t)(-m_j^--t)}{h_j}dt+O_P(\varepsilon^4)
=\frac{h_j^2}{6}\varepsilon^3+O_P(\varepsilon^4).
\]
The extra factor \((1+\varepsilon)\) in the scaled cone opening is already captured by the apex separation above; scaling \(C_j\) itself does not alter a homogeneous cone.

**4. Counting distinct branches.** For every unordered antipodal diameter pair, two independent unoriented square-lattice difference directions contribute, each with two antipodal angular alignments. Thus the covariogram integral in step 1 has four disjoint orientation branches per diameter pair. Each carries mass \(h_j^2\varepsilon^3/6+O_P(\varepsilon^4)\), and the Haar angular prefactor is \(1/(2\pi)\). Therefore the total is \(h_j^2\varepsilon^3/(3\pi)+O_P(\varepsilon^4)\) per pair, as claimed. The half-integral pair-count identity in step 1 already accounts for signed lattice directions; no additional factor is inserted.

**5. The marked law and regular examples.** Within one branch put \(u=(t+m_j^+)/h_j\). The leading angular mass becomes \(h_j^2u(1-u)du\), whose integral equals \(h_j^2/6\). Dividing yields \(6u(1-u)du\). Uniformity and dominated convergence prove the conditional weak convergence. In a regular even \(n\)-gon, each vertex's inward wedge has slopes \(\pm\cot(\pi/n)\), and the count of unordered antipodal diameter pairs is \(n/2\); substitution gives the explicit family formula.

## Verification
An accompanying standalone standard-library script `check_polygon_contact.py` computes convex-polygon intersection areas by independent half-plane clipping, compares them with the exact wedge parallelogram area, and integrates over near-contact angles. It checks regular even polygons of orders \(4,6,8,12\) at \(\varepsilon=0.01,0.005\). The maximum sampled absolute discrepancy between independently computed intersection areas and the wedge formula is below \(6\times10^{-18}\). The ratio between the numerical cubic coefficient and the analytic coefficient tends toward one as \(\varepsilon\) decreases. These are finite corroborating calculations; the proof of the universal asymptotic and the conditional law is analytic and does not rely on numerical enumeration.

## Relationship to prior work
Schlie (arXiv:2611.16769v1, 12 November 2026) surveys translation-and-rotation lattice counts and emphasizes challenges for variance and boundary regularity; its reviewed asymptotic results chiefly concern large dilates, not the first diameter-critical collision of polygonal bodies. De Bruijn's 1965 random thin-rectangle analysis addresses a different thin/long scaling; it does not establish the class-wide diameter-vertex cone coefficient or angular mark. The published 2026 smooth-body first-collision theorem, available as `2026/11/17/SCOPE-the-first-two-point-threshold-for-random-lattice-encounters-with--cf0bb3fe7c4c`, gives an exact three-atom covariogram identity for any convex body and an exponent-two curvature law under positive smoothness assumptions; it separately treats the disk exponent \(3/2\). Its full statement, hypotheses and proof were examined. Its smoothness assumptions fail at polygon vertices, and no formula for polygonal diameter cones or the marked \(\operatorname{Beta}(2,2)\) law is implied by its smooth curvature coefficient. Exact distribution and covariance unfolding are treated as established background rather than new claims.

## Limitations
The error estimate is for each fixed polygon; no uniformity in number of edges or near-degenerate angles is asserted. The result excludes noncentrally symmetric polygons and smooth bodies. Arbitrary lattice bases and non-Haar rotations are not covered. Earlier literature on small random convex bodies, oblique rectangles, and covariograms may contain unindexed equivalent special cases. The full text of Rosen's 1989 oblique-rectangle coverage note was not available for a conclusive statement-level comparison; its accessible abstract is narrower than the general shape and mark result. An independent mathematical review has not been performed.

## References
- S. Schlie, *On the randomized lattice-point count problem*, arXiv:2611.16769v1, first publicly posted 2026-11-12. https://arxiv.org/html/2611.16769v1.
- N. G. de Bruijn, *Solution to Problem 63-6: Asymptotic distribution of lattice points in a random rectangle*, SIAM Review 7 (1965), 274–276. https://pure.tue.nl/ws/portalfiles/portal/1955437/Metis196132.pdf.
- D. Rosen, *Coverage of a square lattice by an inclined rectangle*, Advances in Applied Probability 21 (1989), 705–707. DOI: 10.2307/1427644.
- I. Bárány, *The chance that a convex body is lattice-point free: A relative of Buffon's needle problem*, Random Structures & Algorithms 30 (2007), 414–426, first online 2006-09-26. DOI: 10.1002/rsa.20138.
- *The first two-point threshold for random lattice encounters with smooth convex bodies*, 2026, public mathematical record: https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-the-first-two-point-threshold-for-random-lattice-encounters-with--cf0bb3fe7c4c.
