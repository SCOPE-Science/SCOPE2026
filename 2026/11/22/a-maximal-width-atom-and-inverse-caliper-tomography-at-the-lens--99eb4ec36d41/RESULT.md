# A maximal-width atom and inverse caliper tomography at the lens–lune transition

## Finding
Let \(R\ge r>0\), \(R-r<d<R+r\), and consider the proper Euclidean intersection
\[
K=B((0,0),R)\cap B((d,0),r).
\]
For a uniformly distributed unoriented unit vector \(U\in S^1/\{\pm1\}\), define the **caliper width** \(W=h_K(U)+h_K(-U)\), where \(h_K(u)=\sup_{z\in K}z\cdot u\). This is a random **projection width**, not the chord length cut by a random affine line. Put
\[
q=\frac{d^2+R^2-r^2}{2d},\quad H=\sqrt{R^2-q^2},\quad a=\frac qR,\quad b=\frac{d-q}{r},\quad X=|U_1|.
\]
Thus \(0<a<1\), \(-1<b<1\), and \(a\ge |b|\). The following is the complete almost-sure directional law:
\[
W=\begin{cases}
2r,& b<0,\quad 0\le X\le-b,\\
2H\sqrt{1-X^2},&b\ge0,\quad0\le X\le b,\\
r+H\sqrt{1-X^2}-rbX,&|b|\le X\le a,\\
R+r-dX,&a\le X\le1.
\end{cases}
\tag{1}
\]
Empty or zero-length branches are omitted; in particular \(R=r\) gives \(a=b\). The map is nonincreasing, strictly decreasing outside a possible first plateau. Write \(m=R+r-d\) and
\[
M=\begin{cases}2H,& b>0,\\2r,&b\le0.\end{cases}
\]
Its law is supported on \([m,M]\), has no atom except possibly at \(M\), and satisfies the **sharp atom criterion**
\[
\boxed{\Pr(W=M)=\begin{cases}
\dfrac2\pi\arcsin\!\left(\dfrac{R^2-r^2-d^2}{2dr}\right),&R>r,\quad R-r<d<\sqrt{R^2-r^2},\\
0,&\sqrt{R^2-r^2}\le d<R+r\ \text{or}\ R=r.
\end{cases}}
\tag{2}
\]
In the atomic regime \(M=2r\): an open range of directions fits a complete diameter of the smaller disk inside the larger disk. With \(R>r\) fixed, the atom is born linearly at \(d_c=\sqrt{R^2-r^2}\):
\[
\Pr(W=M)=\frac{2}{\pi r}(d_c-d)+O((d_c-d)^2),\qquad d\uparrow d_c.
\tag{3}
\]
The entire CDF is elementary. For \(m<w<M\), set \(w_a=R+r-da\), and if \(b>0\), \(w_b=2H^2/r\). Define \(x(w)\) by
\[
x(w)=\begin{cases}
\dfrac{R+r-w}{d},&m<w\le w_a,\\
\dfrac{-rb(w-r)+H\sqrt{r^2-(w-r)^2}}{r^2},&w_a<w<M\ \text{and}\ (b\le0\ \text{or}\ w<w_b),\\
\sqrt{1-\bigl(w/(2H)\bigr)^2},&b>0,\quad w_b\le w<M.
\end{cases}
\tag{4}
\]
Then \(F_W(w)=0\) for \(w<m\), \(F_W(w)=1\) for \(w\ge M\), and
\[
\boxed{F_W(w)=1-\frac2\pi\arcsin x(w),\qquad m\le w<M.}
\tag{5}
\]
At \(m\), the CDF is zero. At \(M\) the jump is precisely (2).

**Sharp endpoint behavior.** For \(0\le\varepsilon\le d(1-a)\) the exact lower-edge law is
\[
\boxed{\Pr(W\le m+\varepsilon)=\frac2\pi\arccos(1-\varepsilon/d)}.
\tag{6}
\]
Hence, for \(\varepsilon\downarrow0\),
\[
\Pr(W\le m+\varepsilon)\sim \frac2\pi\sqrt{\frac{2\varepsilon}{d}}.
\tag{7}
\]
At the upper edge, with \(p=\Pr(W=M)\),
\[
\boxed{\Pr(W\ge M-\varepsilon)=p+C_+\sqrt\varepsilon+O(\varepsilon),\quad
C_+=\begin{cases}\dfrac{2}{\pi\sqrt H},&b>0,\\\dfrac2\pi\sqrt{\dfrac2r},&b\le0.\end{cases}}
\tag{8}
\]
The square-root coefficient at the critical boundary \(b=0\) differs by a factor of \(\sqrt2\) from its limit on the opposite-center side \(b\downarrow0^+\); these are different orders of limits, not a discontinuity of the distributions themselves.

**Inverse rigidity.** The unlabeled probability law of \(W\) uniquely determines the complete triple \((R,r,d)\) up to the given radius ordering. In fact only its lower endpoint \(m\), upper endpoint \(M\), lower-tail coefficient \(c=\lim_{\varepsilon\downarrow0} F_W(m+\varepsilon)/\sqrt\varepsilon\), and whether \(\Pr(W=M)>0\) are needed. Set
\[
d=\frac8{\pi^2c^2},\qquad S=m+d.
\]
If the upper atom is positive, take \(r=M/2\), \(R=S-r\). If the atom is zero, put \(H=M/2\) and compute
\[
\Delta=\sqrt{d^2-\frac{4d^2H^2}{S^2-d^2}},\qquad
R=\frac{S+\Delta}{2},\quad r=\frac{S-\Delta}{2}.
\tag{9}
\]
Every radicand and denominator is valid under the stated proper-intersection assumptions; thus there is no ambiguity even at \(b=0\) or \(R=r\).

## Assumptions and scope
The geometry is planar and Euclidean. Radii and separation are finite and positive, the smaller radius is labeled \(r\), and the disks cross in exactly two points: \(R-r<d<R+r\). Tangencies, containment, and disjointness are excluded. Directions are Haar-uniform modulo sign; there is no independent random offset, no line-conditioned sampling and no randomness in the disks. The terms *lens regime* and *lune regime* refer to the circle centers lying on opposite or the same side of their common chord, respectively; equation (1) also covers the separating configuration where the smaller circle's center lies on the chord.

## Proof
**Intersection geometry and branch ordering.** Subtracting the two circle equations shows that the common boundary points are \((q,\pm H)\). The signed cosine values \(a=q/R\) and \(b=(d-q)/r\) obey
\[
a-b=\frac{(R-r)((R+r)^2-d^2)}{2dRr}\ge0,\qquad
a+b=\frac{(R+r)(d^2-(R-r)^2)}{2dRr}>0.
\]
Therefore \(a\ge |b|\), with equality only in the equal-radius case on the first comparison. Moreover \(H^2=r^2(1-b^2)\).

**Two support directions.** For \(u=(x,\sqrt{1-x^2})\), \(0\le x\le1\), the maximizer on the small disk is \((d,0)+ru\); it lies in the large disk precisely if \(x\le-b\). The maximizer on the large disk is \(Ru\); it lies in the small disk precisely if \(x\ge a\). Otherwise the supporting point is the upper intersection point \((q,H)\). Consequently
\[
h_K(u)=\begin{cases}dx+r,&0\le x\le-b\quad(b<0),\\qx+H\sqrt{1-x^2},&\max(0,-b)\le x\le a,\\R,&a\le x\le1.\end{cases}
\]
For the opposite direction, the small-disk maximizer \((d,0)-ru\) is admissible if and only if \(x\ge b\). The large-disk opposite maximizer is never admissible because \(R\ge r\) and \(d>0\). Hence
\[
h_K(-u)=\begin{cases}-qx+H\sqrt{1-x^2},&0\le x\le b\quad(b>0),\\r-dx,&\max(0,b)\le x\le1.\end{cases}
\]
The two formulas add to (1). The widths depend only on \(|u_1|\), by reflection about the center line and reversal of direction.

**Monotonicity, atom and CDF.** The first branch is constant when \(b<0\). In the other case it is strictly decreasing for \(x>0\). The middle-branch derivative is \(-rb-Hx/\sqrt{1-x^2}\); it is strictly negative when \(b\ge0\), and when \(b<0\) it vanishes at \(x=-b\) and is strictly negative thereafter. The last branch has slope \(-d\). These observations prove the extrema and the only possible plateau. For a uniform angle, \(X=|\cos\Theta|\) has \(\Pr(X\le x)=2\arcsin x/\pi\). Applying this to the plateau gives (2), and to the decreasing branches gives (5). Solving the linear, circular-corner, and double-corner branch equations yields (4): on the middle branch solve
\[
H\sqrt{1-x^2}=w-r+rbx,
\]
using \(H^2+r^2b^2=r^2\). The nonnegative root in the stated interval gives the middle line of (4). Both adjacent branch formulas agree at the joins.

**Endpoint expansions.** At \(x=1\), the exact final branch gives \(W=m+d(1-x)\) and (6); arccosine expansion gives (7). At \(b>0\), near \(x=0\), \(M-W=Hx^2+O(x^4)\). At \(b=0\), \(M-W=(r/2)x^2+O(x^4)\). At \(b<0\), the plateau ends at \(x=-b\); the first nonzero Taylor term on the following branch is \((r^3/(2H^2))(x+b)^2\), while the density of \(X\) at \(-b\) equals \(2r/(\pi H)\). These give exactly the coefficients in (8). Since \(-b=(d_c^2-d^2)/(2dr)\sim(d_c-d)/r\), the arcsine expansion proves (3).

**Inverse.** By (6), \(c=(2/\pi)\sqrt{2/d}\), hence \(d=8/(\pi^2c^2)\). The lower endpoint gives \(S=R+r=m+d\). A positive atom implies \(M=2r\) and directly recovers both radii. In the zero-atom case \(M=2H\); writing \(\Delta=R-r\), the triangle-area identity for the two radii and the center separation is
\[
4d^2H^2=(S^2-d^2)(d^2-\Delta^2).
\]
Thus equation (9) recovers \(\Delta\ge0\) and both radii. This includes the boundary \(b=0\). All algebraic steps are reversible on the stated parameter domain.

## Verification
The bundled `check_lens.py` independently samples the two admissible circular boundary arcs and the intersection points to compare direct support maxima against (1), checks branch inverses and CDF consistency for equal-radius, opposite-center, critical, and same-side-center regimes, and tests reconstruction from four distributional features. It passed 2,434 deterministic assertions. Additional local numerical checks of (8) at deficits \(10^{-4}\) and \(10^{-6}\) agreed with its specified coefficient in all three regimes. Such finite diagnostics corroborate, but do not replace, the analytic proof above.

## Relationship to prior work
Harutyunyan's 2011 primary paper computes the **motion-invariant random-line chord-length distribution**, integrating over both line orientation and offset; its variable differs from the present *maximal supporting-line separation at a random direction*. Its displayed general-lens geometry takes positive distances of both circle centers from the common chord and does not classify the same-side-center plateau or inverse angular-width recovery. Finch (2013) calculates mean width of **equal-radius three-dimensional** spherical lenses. A later published exact formula for mean width of two congruent balls in arbitrary dimensions includes the equal-radius planar support function, but not the unequal-radius two-disk atom, full law, or reconstruction. The general asymmetric kite width-inversion result concerns a piecewise-linear polygon with no width atoms, not a two-circle intersection. Eisele's 2016 circle-intersection study and the MathWorld *Lens* entry provide the standard intersection geometry and area, not random-direction widths. No searched or materially inspected source was found to imply the complete theorem stated here; this is a best-knowledge comparison, not a guarantee of historical priority.

## Limitations
Only proper intersections of two Euclidean planar disks are covered. The mathematical boundary cases of tangency and containment require separate definitions: at full containment the width is constant, but the proof above uses two distinct circle intersections. The directional-width law does not determine the absolute position or angle of the entire shape, only its intrinsic radii and center distance. The exact formulas concern the continuous Haar distribution, not discretely sampled directions. Hidden earlier derivations in the classical integral-geometry literature remain a historical-priority risk, and no independent audit has been performed.

## References
1. H. S. Harutyunyan, *Chord Length Distribution Function for Lens*, Proceedings of the Yerevan State University, Physical and Mathematical Sciences 45(3), 17–22 (2011), DOI: 10.46991/PYSUA.2011.45.3.017, first published online 2011-10-17, https://journals.ysu.am/proceedings-phys-math/article/view/vol45_no3_2011_pp017-022.
2. Steven R. Finch, *Mutually Equidistant Spheres that Intersect*, arXiv:1301.5515v1, first public 2013-01-23, https://arxiv.org/html/1301.5515v1.
3. Robert Eisele, *Intersection Area of Two Circles*, 2016-07-14, https://raw.org/math/geometry/intersection-area-of-two-circles/.
4. Eric W. Weisstein, *Lens*, MathWorld, https://mathworld.wolfram.com/Lens.html.
5. *Mean width of a symmetric lens in every dimension*, published published-finding corpus finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-mean-width-of-a-symmetric-lens-in-every-dimension--80ec085cfff6.
6. *Three spectral singularities reconstruct asymmetric kites from random widths*, published published-finding corpus finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-three-spectral-singularities-reconstruct-asymmetric-kites-from-r--0fca3299603f.
