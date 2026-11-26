# The square is a two-negative-mode saddle for polygonal width deviation

## Finding

For the width \(W_Q(U)\) of a strictly convex planar quadrilateral \(Q\) projected onto a Haar-uniform unoriented line \(U\), define its squared width-deviation rate by
\[
F(Q)=\frac{\operatorname{Var}(W_Q(U))}{(\mathbb E W_Q(U))^2}.
\]
Near a Euclidean square, the complete four-dimensional local moduli of quadrilaterals modulo translations, rotations and positive homotheties have an **exactly two-positive/two-negative** second variation. Specifically, in the chart defined below,
\[
\boxed{F(Q)=\frac{\pi^2}{16}+\frac\pi8-1+
\frac{\pi(\pi-2)}{64}s^2+\frac\pi{16}(t-1)^2-
\frac{\pi(\pi-2)}{16}(h^2+k^2)+O(\|q\|^3).}
\]
Its full Hessian, in the order \((s,t-1,h,k)\), is
\[
\boxed{\operatorname{diag}\left(\frac{\pi(\pi-2)}{32},\frac\pi8,
\frac{\pi(2-\pi)}8,\frac{\pi(2-\pi)}8\right).}
\]
Thus the square is a nondegenerate saddle of Morse index two, not a local extremum, and the unstable directions are precisely the two modes that destroy the parallelogram condition. The exact **quadratic** transition between increasing and decreasing leading-order perturbations is
\[
h^2+k^2=\frac{s^2}{4}+\frac{(t-1)^2}{\pi-2}.
\]
This equation does not claim to describe the zero set of the full finite-perturbation deviation difference.

## Assumptions and scope

The four vertices \(A,B,C,D\) occur counterclockwise, and are distinct and strictly convex. Modulo translation, proper rotation and positive scaling, any such *labeled* quadrilateral sufficiently close to the diamond square has a unique chart
\[
A=(1+h,k),\quad B=(s-h,t-k),\quad C=(-1+h,k),\quad D=(-s-h,-t-k),
\]
where \(s,h,k,t-1\) are sufficiently small real parameters. Indeed, translate to make the average of the two diagonal midpoints the origin; rotate the diagonal \(AC\) to the horizontal axis; scale it to length \(2\). The midpoint of \(AC\) then has coordinates \((h,k)\), that of \(BD\) has coordinates \((-h,-k)\), and the second diagonal's half-vector is \((s,t)\). This exhausts precisely four parameters, since the space of ordered planar four-vertex configurations is eight-dimensional and the similarity group removes four dimensions.

The square corresponds to \((s,t,h,k)=(0,1,0,0)\). The body is a parallelogram exactly when \(h=k=0\). The normalized directional measure is uniform on \([0,\pi)\), and \(W_Q(U)\) is maximum projected coordinate minus minimum projected coordinate. The statistic \(F\) is the square of the nonnegative deviation rate considered by Akiyama–Kamae, and has the same extrema because the square root is increasing. All claimed signs are for sufficiently small nonzero perturbations with directions bounded away from the quadratic null cone; pure coordinate axes have the indicated strict signs.

## Proof

**Step 1: an exact moment kernel.** Denote the four directed counterclockwise edge vectors by \(e_i\), their lengths by \(r_i>0\), their orientation angles by \(\theta_i\), and the perimeter by \(P=\sum_i r_i\). For a unit direction \(u\), the projection width equals \(\sum_i(e_i\cdot u)_+\). Hence
\[
\mathbb E W=\frac{P}{\pi},\qquad
\mathbb E W^2=\frac1{4\pi}\sum_{i,j=1}^{4}r_ir_jV(\theta_i-\theta_j),
\]
with \(V(\phi)=(\pi-|\phi|)\cos\phi+\sin|\phi|\) on \([-\pi,\pi]\), continued periodically. This elementary integral also appears as Theorem 1 of Akiyama–Kamae. Therefore \(F=\pi^2(\mathbb E W^2)/P^2-1\).

**Step 2: justification of the local analytic reduction.** The square's four adjacent edge pairs meet at right angles and all four opposite pairs have angle \(\pi\). Each adjacent oriented determinant \(D_i=\det(e_i,e_{i+1})\) is positive near the square and each dot product \(d_i=e_i\cdot e_{i+1}\) vanishes at the square. Their exact pair contribution expands as
\[
r_ir_{i+1}V(\theta_i-\theta_{i+1})
=D_i+\frac\pi2d_i+\frac{d_i^2}{D_i}+O(\|q\|^3).
\]
This follows from \(\pi-\theta=\pi/2+\arcsin(d_i/(r_ir_{i+1}))\), and \(r_ir_{i+1}\sin\theta=D_i\). Opposite-edge contributions are of order \(O(\|q\|^3)\), because for \(\varepsilon\downarrow0\),
\[
V(\pi-\varepsilon)=\varepsilon^3/3+O(\varepsilon^5).
\]
In particular the possible loss of third-order smoothness at antiparallel edges cannot affect the Hessian; the remainder estimate is uniform on a sufficiently small parameter neighborhood.

**Step 3: exact first- and second-order terms.** Substitute the vertices from the chart into \(e_i\), and use \(P=\sum_i\|e_i\|\) and the previous kernel expansion. Direct expansion in \(q=(s,t-1,h,k)\) gives
\[
P=4\sqrt2+2\sqrt2(t-1)+\frac{\sqrt2}2\bigl(s^2+(t-1)^2+4h^2+4k^2\bigr)+O(\|q\|^3),
\]
\[
\mathbb EW^2=2+\frac4\pi+\left(2+\frac4\pi\right)(t-1)
+s^2+\left(1+\frac4\pi\right)(t-1)^2
+\frac8\pi(h^2+k^2)+O(\|q\|^3).
\]
All mixed quadratic terms vanish exactly. Expanding \(\pi^2(\mathbb E W^2)/P^2-1\) yields the boxed expression and the stated exact Hessian. Because \(\pi>2\), two Hessian eigenvalues are strictly positive and two strictly negative. The Hessian is nonsingular, so its signature is invariant under smooth local changes of similarity coordinates, although individual eigenvalue magnitudes depend on this chart. The negative subspace \(h,k\) exactly changes opposite diagonal midpoints; the positive subspace \(s,t-1\) preserves their coincidence.

**Step 4: structural distinction from the parallelogram case.** A parallelogram is the Minkowski sum of segments of lengths \(a,b>0\) at an acute unoriented angle \(\phi\in(0,\pi/2]\). By integrating \(W(u)=a|\cos u|+b|\cos(u-\phi)|\), one gets
\[
F+1=\frac{\pi^2}{8}+
\frac{ab}{(a+b)^2}\left[\frac\pi2G(\phi)-\frac{\pi^2}{4}\right],\quad
G(\phi)=\sin\phi+(\pi/2-\phi)\cos\phi.
\]
Here \(G(\phi)\ge1\), with equality only for \(\phi=\pi/2\), while the bracket is strictly negative for positive \(\phi\). Since \(ab/(a+b)^2\le1/4\), this expression has its unique minimum at the square. The sharp parallelogram statement is contextual and is not claimed original; it highlights that the square's local instability appears only upon moving into genuinely non-parallelogram quadrilaterals. It is consistent with known parallelogram-width moment reconstructions.

## Verification

Run `python3 verify.py` with Python 3 and SymPy installed. The standalone checker constructs the four edge vectors directly, builds the exact adjacent-edge kernel up to second order, symbolically differentiates the perimeter and width second moment, and confirms all sixteen Hessian entries and the constant/gradient. It separately integrates actual maximum-minus-minimum vertex projections over \(8192\) directions for \(56\) seeded nearby quadrilaterals, comparing with the exact full angle kernel and quadratic expansion; an additional \(250\) randomized parallelograms check the known comparison inequality. A successful run prints `VERIFY_OK 306 second-order Hessian and independent width quadratures`. The analytic argument above proves the continuum of claims; finite sampling is not used to infer the Hessian or unrestricted sign classification.

## Relationship to prior work

Akiyama and Kamae, *Width deviation of convex polygons* (first public January 18, 2022, arXiv:2201.06736v1), introduce this same invariant, derive the exact angular edge-pair kernel, prove global extremal results for polygons with side counts not powers of two, and explicitly identify the quadrilateral minimum problem as unresolved (Section 7). Their numerical kite candidate is not a proof of a full local square Hessian. The present claim supplies the **four-dimensional local saddle signature only**, not their open global quadrilateral minimum. Their general moment kernel is used with explicit credit; no claim is made to its discovery.

*Area-calibrated width-moment tomography of parallelograms, with sharp inverse slope* (public result, November 1, 2026) proves reconstruction and variance comparisons for the **two-dimensional subfamily** of parallelograms. *Three unlabeled width statistics reconstruct a parallelogram with sharp stability* (public result, October 11, 2026) supplies exact moments and a different inverse theorem in that same restricted subfamily. These results imply and anticipate positive curvature in the \((s,t-1)\)-plane but do not imply the two negative eigenvalues, the complete four-dimensional Hessian, or the quadratic transition cone on general quadrilaterals. Results on triangle truncation concern the local geometry at a triangle, not the square.

## Limitations

The theorem is local and does not solve the global width-deviation minimization problem over all quadrilaterals. The quadratic cone is only a second-order separator, and near its null directions higher-order behavior matters. Its coordinates require consistently labeled strictly convex quadrilaterals sufficiently close to a square; eigenvalues depend on chart while the signature does not. The result uses exact full-direction moments, not finitely sampled width statistics. Independent priority checking and independent mathematical audit have not been performed; equivalent but unindexed prior local calculations remain possible.

## References

1. S. Akiyama and T. Kamae, *Width deviation of convex polygons*, arXiv:2201.06736v1, January 18, 2022, Theorem 1 and Section 7. https://arxiv.org/html/2201.06736v1 and https://arxiv.org/abs/2201.06736.
2. *Area-calibrated width-moment tomography of parallelograms, with sharp inverse slope*, published mathematical finding, November 1, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-area-calibrated-width-moment-tomography-of-parallelograms-with-s--c79f5c424519.
3. *Three unlabeled width statistics reconstruct a parallelogram with sharp stability*, published mathematical finding, October 11, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-three-unlabeled-width-statistics-reconstruct-a-parallelogram-wit--dcfda0360928.
