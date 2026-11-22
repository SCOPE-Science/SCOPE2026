# Three contact regimes of the minimum-area ellipse enclosing a circular sector

## Finding

Let \(0<\theta\le\pi/2\), let \(m=\cos\theta\), \(s=\sin\theta\), and let the unit circular sector be
\[
K_\theta=\{(r\cos\varphi,r\sin\varphi):0\le r\le1,\;|\varphi|\le\theta\}.
\]
Among **all** Euclidean ellipses containing \(K_\theta\), allowing arbitrary center, orientation and eccentricity, the unique minimum-area ellipse is
\[
E_m=\left\{(x,y):\frac{(x-c_m)^2}{a_m^2}+\frac{y^2}{b_m^2}\le1\right\},
\]
where its center and positive semiaxes obey the following exact three-regime law:
\[
(c_m,a_m,b_m)=
\begin{cases}
\left(\frac{1+2m}{3},\frac{2(1-m)}3,\frac{2\sqrt{1-m^2}}{\sqrt3}\right),&0\le m\le\frac14,\\[4pt]
\left(\frac12,\frac12,\frac12\sqrt{\frac{1+m}{m}}\right),&\frac14\le m\le\frac34,\\[4pt]
\left(\frac{2m}3,\frac{2m}3,\frac{2\sqrt{1-m^2}}{\sqrt3}\right),&\frac34\le m<1.
\end{cases}
\]
Consequently its sharp minimum area \(M(m)=\pi a_mb_m\) is
\[
M(m)=\begin{cases}
\displaystyle\frac{4\pi(1-m)\sqrt{1-m^2}}{3\sqrt3},&0\le m\le1/4,\\[5pt]
\displaystyle\frac\pi4\sqrt{\frac{1+m}{m}},&1/4\le m\le3/4,\\[5pt]
\displaystyle\frac{4\pi m\sqrt{1-m^2}}{3\sqrt3},&3/4\le m<1.
\end{cases}
\]
For \(0<m<1/4\), the contacts are exactly the circular tip \((1,0)\) and the two circular-arc endpoints \((m,\pm s)\). For \(1/4<m<3/4\), exactly four points touch: those three plus the origin. For \(3/4<m<1\), exactly the origin and the two arc endpoints touch; the circular tip is strictly interior. At either transition all four listed points lie on the ellipse, while one contact-certificate weight becomes zero.

The minimum-area profile is continuously differentiable, but not twice differentiable, across both contact transitions. In the variable \(m\), its right-minus-left second-derivative jumps are, respectively,
\[
M''(1/4+)-M''(1/4-)=\frac{8\pi\sqrt5}{3},\qquad
M''(3/4+)-M''(3/4-)=-\frac{8\pi\sqrt{21}}9.
\]
The continuously curved sector therefore has exactly the same minimum enclosing ellipse as the four-point set \(\{(0,0),(1,0),(m,s),(m,-s)\}\), for every aperture in the asserted range.

## Assumptions and scope

Angles are in radians; the sector opening is \(2\theta\) and the disk radius is one. Reflection symmetry does not restrict competitors: all positive-definite affine images of a disk, including translated and rotated ellipses, are considered. The endpoint \(\theta=\pi/2\) is permitted; \(\theta=0\) is excluded because the sector loses interior. Scaling the disk radius by \(R>0\) multiplies all displayed center/axis lengths by \(R\) and all areas by \(R^2\).

## Proof

**1. Feasibility against the entire circular arc.** For a candidate with parameters \((c,a,b)\), points of the unit circular arc have abscissa \(x\in[m,1]\), ordinate satisfying \(y^2=1-x^2\). Define
\[
q(x)=\frac{(x-c)^2}{a^2}+\frac{1-x^2}{b^2}.
\]
It suffices to prove \(q(x)\le1\) on \([m,1]\), together with origin containment, since the sector is the convex hull of its arc and the origin. In the first regime, \(q(m)=q(1)=1\), \(q''(x)=2(a^{-2}-b^{-2})>0\), and \(q(0,0)\) evaluated in the ellipse is \((c/a)^2\le1\) exactly when \(m\le1/4\). In the middle regime, \(q(m)=q(1)=1\), \(q''(x)=8/(1+m)>0\), and the origin lies on the ellipse. In the last regime, \(q(m)=1\), the origin lies on the ellipse, and \(q(1)=(3-2m)^2/(4m^2)\le1\) exactly for \(m\ge3/4\). For \(3/4\le m\le\sqrt3/2\), \(q\) is convex, so these endpoint values imply containment. For \(m\ge\sqrt3/2\), \(q\) is concave and
\[
q'(m)=\frac{3(1-2m^2)}{2m(1-m^2)}<0,
\]
so \(q\) strictly decreases on \([m,1]\). Thus every candidate contains the whole sector. Strict convexity/decrease also proves the claimed arc contact sets.

**2. Global optimality without assuming symmetry.** Use the affine map \(u=((x-c)/a,y/b)\) to send the candidate ellipse to the Euclidean unit disk. The following boundary contact points \(u_i\) admit nonnegative weights \(w_i\) satisfying
\[
\sum_iw_i=1,\qquad \sum_iw_iu_i=0,\qquad
\sum_iw_iu_iu_i^{\mathsf T}=\frac12I_2.
\]
In the first regime, \(u_i=(1,0),(-1/2,\pm\sqrt3/2)\), each with weight \(1/3\). In the last regime, \(u_i=(-1,0),(1/2,\pm\sqrt3/2)\), again each with weight \(1/3\). In the middle regime, the four transformed points and their weights are
\[
\begin{array}{c|c}
 u_i & w_i\\\hline
 (1,0)&\displaystyle\frac{3-4m}{8(1-m)}\\[3pt]
 (-1,0)&\displaystyle\frac{4m-1}{8m}\\[3pt]
 (2m-1,\;2\sqrt{m(1-m)})&\displaystyle\frac1{16m(1-m)}\\[3pt]
 (2m-1,-2\sqrt{m(1-m)})&\displaystyle\frac1{16m(1-m)}
\end{array}
\]
All weights are nonnegative exactly on the indicated closed parameter intervals. Direct substitution verifies all three moment identities, including at endpoints where a weight may vanish.

Here is a self-contained proof of why these identities certify *global* optimality. Let any competing enclosing ellipse be the image of the unit disk under \(u=z+T v\) with invertible matrix \(T\). Each contact satisfies \(\|T^{-1}(u_i-z)\|^2\le1\). Weighted averaging and the three identities give
\[
\frac12\operatorname{tr}\bigl((TT^{\mathsf T})^{-1}\bigr)
+\|T^{-1}z\|^2\le1.
\]
If \(\sigma_1,\sigma_2\) are the positive singular values of \(T\), then \(\sigma_1^{-2}+\sigma_2^{-2}\le2\), whence \(\sigma_1\sigma_2\ge1\) by arithmetic-geometric mean. Thus the competitor's area is at least that of the unit disk. Equality forces \(z=0\) and \(TT^{\mathsf T}=I_2\), proving uniqueness. Undoing the initial affine map proves optimality and uniqueness for every sector.

**3. Area and sharp transitions.** The area is \(\pi ab\), giving the three displayed expressions. Substituting \(m=1/4\) and \(m=3/4\) shows value and first derivative agree on adjoining branches. Two further explicit differentiations yield the stated, nonzero right-minus-left second-derivative jumps. The contact multiplicities follow from step 1 and the origin/tip equalities in each case.

## Verification

The standalone `checker.py` evaluates the complete contact moment identities, exact endpoint contacts, sampled circle-arc inclusion, radial-edge inclusion and parameter continuity at both transitions across all three regimes. Run `python checker.py` with Python 3.10 or later. These finite diagnostics are cross-checks, not substitutes for the exact feasibility and optimality argument. Independent manual algebra checks of the contact weights and symbolic second-derivative jumps support the stated formulas.

Benchmarks: for a half-disk \(\theta=\pi/2\), the result gives \((c,a,b)=(1/3,2/3,2/\sqrt3)\), area \(4\pi/(3\sqrt3)\). For a \(120^\circ\) sector \(\theta=\pi/3\), it gives \((c,a,b)=(1/2,1/2,\sqrt3/2)\), area \(\pi\sqrt3/4\). These two individual benchmark ellipses are available in the cited circular-covering discussion; the theorem concerns the full variable-aperture classification and sharp thresholds.

## Relationship to prior work

The affine contact-moment criterion for a minimum-volume enclosing ellipse is classical; the proof above reconstructs its sufficient direction. Rublev and Petunin's 1998 work gives finite-polygon minimum-area ellipse methods; Horwitz's 2007 preprint proves existence and uniqueness of the minimum-area ellipse **through all four vertices** of a quadrilateral and explicitly distinguishes it from a quadrilateral's unrestricted minimum enclosing ellipse. Neither source identifies why an entire circular sector is covered by the four-point kite's optimal ellipse or provides the three sector contact regimes and the two sharp thresholds. A separately available circular-covering problem gives the specific half-disk and \(120^\circ\)-sector solutions but no continuous phase diagram. The inscribed John ellipsoid of spherical sectors is a different optimization problem and does not imply the enclosing result.

## Limitations

The complete classification is for planar circular sectors with opening at most \(\pi\), radius one up to scaling. It does not establish the enclosing ellipsoid of nonconvex major sectors or dimensions above two. The result is not an independent historical-priority certification: prior sources may exist beyond the searchable and inspected literature. The four-point reduction and all formulas are proved, but numerical comparisons alone would not establish them.

## References

- A. Horwitz, *Ellipses of minimal area and of minimal eccentricity circumscribed about a convex quadrilateral*, arXiv:0707.2092, first public preprint 2007-07-13. https://arxiv.org/abs/0707.2092
- B. V. Rublev and Yu. I. Petunin, *Minimum-Area Ellipse Containing a Finite Set of Points. II*, Ukrainian Mathematical Journal 50 (1998), no. 8, 1253–1261. https://www.mit.edu/~hlb/ellipse-paper.pdf
- E. W. Weisstein, *Löwner Ellipsoid*, MathWorld (reference for classical enclosing-ellipse terminology and contact criterion). https://mathworld.wolfram.com/LoewnerEllipsoid.html
- V. Jandhyala, *Can You Eclipse via Ellipse?*, mathematical puzzle solution, benchmark half-disk and \(120^\circ\)-sector cases. https://vamshij.com/books/fiddler/read/120/
