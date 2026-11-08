# A reciprocal-height law and complete width–brightness covariance phase for right prisms

## Finding

Let \(B\subset\mathbb R^2\) be any compact planar convex body with nonempty interior and Euclidean area \(A>0\). Denote its directional width by \(w(\phi)\), and define the finite, positive statistics
\[
\beta=\frac1{2\pi}\int_0^{2\pi}w(\phi)\,d\phi,\qquad
c=\frac1{2\pi}\int_0^{2\pi}w(\phi)w(\phi+\pi/2)\,d\phi.
\]
For \(H>0\), consider the right prism \(K_H=B\times[-H/2,H/2]\). With one shared Haar-uniform normal \(U\in S^2\), let \(W_H(U)\) denote its Euclidean directional width and \(P_H(U)\) the Euclidean area of its orthogonal projection onto \(U^\perp\). Set
\[
k=\frac\pi8-\frac13>0,\quad L=\frac A{12}+\frac{2c}3-\frac{\pi^2\beta^2}{16}.
\]
Then the exact covariance \(C_B(H)=\operatorname{Cov}(W_H,P_H)\) is
\[
\boxed{C_B(H)=-k\beta(H^2+A)+LH.}
\]
It obeys the reciprocal-height identity
\[
\boxed{C_B(A/H)=\frac{A}{H^2}C_B(H)\quad(H>0).}
\]
There is a complete trichotomy with no shape-regularity assumptions:

- If \(L<2k\beta\sqrt A\), then \(C_B(H)<0\) at every positive height.
- If \(L=2k\beta\sqrt A\), then \(C_B(H)\le0\), with equality only for \(H=\sqrt A\).
- If \(L>2k\beta\sqrt A\), the covariance is positive exactly on \((H_-,H_+)\), where
  \[
  H_\pm=\frac{L\pm\sqrt{L^2-4k^2\beta^2 A}}{2k\beta},\qquad H_-H_+=A.
  \]
  It is zero at the two endpoints and negative at all other positive heights.

Every planar base of constant Euclidean width belongs to the third regime. Conversely, an axis-aligned rectangle with sides \(1\) and \(\varepsilon\), \(0<\varepsilon\le1/10\), belongs to the first regime. A continuous deformation from the square to such a narrow rectangle gives an intermediate rectangle with the double-zero regime. These examples show all three regimes occur among convex bases.

## Assumptions and scope

The normal \(U\) is uniform on the complete sphere and the **same** normal is used for both measurements, not two independent normals. The prism base has no smoothness, strict-convexity, symmetry or polygonal assumption. Horizontal translation and vertical placement do not affect the theorem. All areas and widths use ordinary Euclidean normalization, without any surface-area normalization. Angle \(\phi\) is an ordinary azimuth, and \(w(\phi+\pi/2)\) is the width along the perpendicular horizontal azimuth. The orthogonal-width correlation \(c\), rather than the mean squared width, is essential.

## Proof

**Exact projection formulas.** Write a sphere direction \(U=(s\cos\phi,s\sin\phi,z)\), where \(t=|z|\in[0,1]\) and \(s=\sqrt{1-t^2}\). Let \(v=(\cos\phi,\sin\phi)\) and \(v^\perp=(-\sin\phi,\cos\phi)\). By additivity of support functions under Minkowski sums, the width is
\[
W_H(U)=Ht+s\,w(\phi).
\]
The projection of \(B\) to \(U^\perp\) has area \(At\). The projection of the vertical segment has length \(Hs\); the planar width of the projected base perpendicular to that projected segment equals \(w(\phi+\pi/2)\). The elementary planar identity \(\operatorname{area}(E+[0,a])=\operatorname{area}(E)+|a|\operatorname{width}_{a^\perp}(E)\), valid for every compact convex planar \(E\), therefore gives
\[
P_H(U)=At+Hs\,w(\phi+\pi/2).
\]
The formulas hold by continuity for the exceptional axial and equatorial directions as well.

**Spherical moments.** For Haar-uniform \(U\), \(t=|U_3|\) is uniform on \([0,1]\), independently of the uniform azimuth \(\phi\). Direct integration yields
\[
\mathbb E t=\frac12,\quad\mathbb E s=\frac\pi4,\quad
\mathbb E t^2=\frac13,\quad\mathbb E s^2=\frac23,\quad\mathbb E(ts)=\frac13.
\]
Using \(\mathbb Ew(\phi)=\mathbb Ew(\phi+\pi/2)=\beta\) and \(\mathbb E[w(\phi)w(\phi+\pi/2)]=c\), we get
\[
\mathbb EW_H=\frac H2+\frac{\pi\beta}4,\qquad
\mathbb EP_H=\frac A2+\frac{\pi H\beta}4,
\]
\[
\mathbb E(W_HP_H)=\frac{AH}3+\frac{(A+H^2)\beta}3+\frac{2Hc}3.
\]
Subtracting the product of the two means proves the exact covariance formula.

**All heights and reciprocity.** Divide by \(H>0\):
\[
\frac{C_B(H)}H=L-k\beta\left(H+\frac AH\right).
\]
The arithmetic–geometric mean inequality gives \(H+A/H\ge2\sqrt A\), with equality only at \(H=\sqrt A\). This proves the three sign cases, including the exact equality case. Solving the resulting quadratic gives the displayed roots and their product; replacing \(H\) by \(A/H\) proves reciprocity directly. In particular, the covariance is negative for sufficiently small and sufficiently large heights for every base.

**Constant-width bases.** If \(w(\phi)\equiv\beta\), then \(c=\beta^2\). Put \(a=A/\beta^2>0\). Completing the square gives
\[
\frac{L-2k\beta\sqrt A}{\beta^2}
=\frac{(\sqrt a-12k)^2}{12}+\delta,\quad
\delta=\pi-\frac{\pi^2}4-\frac23>0.
\]
For the strict last inequality, \(x-x^2/4-2/3\) decreases on \((2,\infty)\) and, using the classical bound \(\pi<22/7\), it is greater at \(\pi\) than its value \(1/147\) at \(22/7\). Hence the strict positive regime holds for every constant-width body, including nonsmooth noncircular ones.

**Narrow rectangles and all three regimes.** For a rectangle of horizontal side lengths \(1\) and \(\varepsilon\), the width formula \(w(\phi)=|\cos\phi|+\varepsilon|\sin\phi|\) gives exactly
\[
A=\varepsilon,\quad\beta=\frac{2(1+\varepsilon)}\pi,\quad
c=\frac{1+\varepsilon^2}\pi+\varepsilon,
\]
\[
L=\frac\varepsilon4-\left(\frac14-\frac2{3\pi}\right)(1+\varepsilon^2).
\]
Since \(\pi>3\), the parenthesized coefficient exceeds \(1/36\), whereas \(\varepsilon/4\le1/40\) when \(\varepsilon\le1/10\). Thus \(L<0<2k\beta\sqrt A\) for every such thin rectangle, so covariance is strictly negative at all heights. For the square \(\varepsilon=1\), direct substitution yields \(L>2k\beta\sqrt A\) (numerically, \(L=0.1744131815\ldots\) versus \(2k\beta\sqrt A=0.151170\ldots\)); the exact inequality is \(4/\pi-5/4>0\), valid because \(\pi<22/7<16/5\). By continuity of \(\varepsilon\mapsto L-2k\beta\sqrt A\), some intermediate rectangle is in the equality regime. All claims follow.

## Verification

The bundled `verify_prism_covariance.py` reconstructs projections of actual three-dimensional polygonal prisms, computes their planar convex-hull areas and widths, and compares covariance estimates over shared isotropic directions with the exact formula. Shapes tested include a square, a thin rectangle, an equilateral triangle, and a regular 32-gon. The executable also verifies exact rectangle angular integrals by high-resolution quadrature, the two-root product identity, and the circular constant-width example. It runs with the Python 3 standard library alone and prints `ALL_SAME_NORMAL_PRISM_COVARIANCE_CHECKS_PASSED`. The finite calculations are corroboration, not a proof for all convex bases.

## Relationship to prior work

Horváth's 2019 survey treats directional width and brightness in its Sections 2.2–2.3 and proves that equal planar brightness and area can be lifted to prisms with equal three-dimensional brightness (Theorem 5). It does not give a same-normal *mixed covariance*, a positive-height interval, or the reciprocal-height identity. An earlier complete orthotope result gives the same-normal covariance and a sharp aspect-ratio phase diagram for rectangular boxes in all dimensions; **the box result, including its special cases, is prior work, not a novelty claim**. The statement here applies to every planar convex base (including nonpolygonal constant-width sets) and identifies the perpendicular-width moment controlling the universal three-case height law. Results limited to a marginal width moment or marginal brightness variance do not imply this mixed moment. A 2026 preprint on random width and brightness studies general marginal laws and inverse moments, but a complete manuscript could not be inspected in the available reading route; potential broader coverage remains a historical-priority risk.

## Limitations

The theorem concerns orthogonal projections and widths sampled with a single uniform normal and prisms with a right (not oblique) axis. It classifies the sign of the covariance, not the entire joint law, the shape of the base, or all possible covariance matrices. The simple mixed moment identity follows from classical projection geometry; the structural content is the height reciprocity, complete sign classification, and contrasting constant-width versus elongated-base regimes. Historical priority is provisional pending independent source review. No independent mathematical validation is claimed.

## References

1. Á. G. Horváth, *On convex bodies that are characterizable by volume function*, arXiv:1908.03196v1, first publicly submitted 2019-08-08. https://arxiv.org/abs/1908.03196 ; full HTML text https://arxiv.org/html/1908.03196v1 .
2. *Sharp aspect-ratio phase diagram for width–brightness covariance of orthotopes*, publicly available research result, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-aspect-ratio-phase-diagram-for-width-brightness-covariance--ef50d44d3e36 ; the full `RESULT.md` was compared.
3. O. Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202, 2026, https://arxiv.org/abs/2609.26202 ; abstract accessible, complete manuscript not inspected.
