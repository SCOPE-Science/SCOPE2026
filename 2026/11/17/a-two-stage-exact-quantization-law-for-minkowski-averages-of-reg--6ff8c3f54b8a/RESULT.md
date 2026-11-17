# A two-stage exact quantization law for Minkowski averages of regular hexagon vertices

## Finding
Let \(H\subset\mathbb R^2\) be a regular hexagon of circumradius one centered at the origin and \(V\) its set of six vertices. For an integer \(k\ge1\), define the finite Minkowski average \(A_k=k^{-1}(V+\cdots+V)\) with \(k\) summands. If \(X\) is distributed uniformly with respect to area in \(H\), let \(Y_k=k\,\operatorname{dist}(X,A_k)\). There are exactly two distributions: one for \(k=1\), and one shared by **all** \(k\ge2\).

For \(k=1\), the cumulative distribution function is
\[
 F_1(t)=\begin{cases}
 0,&t\le0,\\
 \frac{4\pi t^2}{3\sqrt3},&0<t\le\frac12,\\
 \frac4{\sqrt3}\left[t^2\left(\arcsin\frac1{2t}-\frac\pi6\right)+\frac{\sqrt{4t^2-1}}4\right],&\frac12<t<1,\\
 1,&t\ge1.
 \end{cases}
\]
For every integer \(k\ge2\), the common cumulative distribution function is
\[
 F_*(t)=\begin{cases}
 0,&t\le0,\\
 \frac{2\pi t^2}{\sqrt3},&0<t\le\frac12,\\
 \frac2{\sqrt3}\left[\pi t^2-6t^2\arccos\frac1{2t}+3\sqrt{t^2-\frac14}\right],&\frac12<t<\frac1{\sqrt3},\\
 1,&t\ge\frac1{\sqrt3}.
 \end{cases}
\]
In particular, the exact Hausdorff distances and mean squared errors are
\[
 d_H(H,A_k)=\begin{cases}1,&k=1,\\1/(k\sqrt3),&k\ge2,\end{cases}
 \qquad \mathbb E\operatorname{dist}(X,A_k)^2=\begin{cases}\frac14,&k=1,\\\frac5{36k^2},&k\ge2.\end{cases}
\]
Also \(|A_1|=6\), whereas \(|A_k|=3k(k+1)+1\) for \(k\ge2\). The equal-law assertion concerns the rescaled distances, not the unscaled distributions.

## Assumptions and scope
All geometry uses the ordinary Euclidean distance and two-dimensional area. A regular hexagon of circumradius one has side length one. Set \(u=(1,0)\), \(v=(1/2,\sqrt3/2)\), and \(L=\mathbb Zu+\mathbb Zv\). The result holds exactly for every integer \(k\ge1\), without an asymptotic limit. The random point \(X\) is drawn from the *filled* hexagon, not its boundary; numerical tests do not serve as infinite proofs.

## Proof
**1. Integer Minkowski averages saturate the lattice hexagon from the second summand onward.** Write a lattice point as \(au+bv\). Its minimal number of nonzero steps from the six vectors \(\pm u,\pm v,\pm(v-u)\) is
\[
 m(a,b)=\max\{|a|,|b|,|a+b|\}.
\]
For example, using the coordinates \((a,b)\), a walk minimizing this maximum is obtained by pairing coordinate increases with the diagonal step \((-1,1)\) where the signs permit; the remaining steps are axial. Equivalently, this is the standard graph-distance formula on the triangular lattice, checked directly in each of its six sign sectors. Consequently \(kH\cap L\) consists precisely of points of word length at most \(k\), and its cardinality is \(1+3k(k+1)\).

For any nonzero lattice point with minimum word length \(m\ge1\), a representation of length \(m+1\) exists: split any of its six unit steps into a sum of two neighboring unit steps (e.g. \(u=v+(u-v)\)). Representations of every length greater than \(m\) then follow by inserting zero-sum antipodal pairs. The origin has representations of every length at least two, as every such integer is a nonnegative combination of \(2\) and \(3\) and zero is representable by an antipodal pair or a three-step loop. Thus
\[
 kA_k=kH\cap L\quad(k\ge2),\qquad A_1=V.
\]
For \(k=1\), the only missing lattice point is the origin.

**2. The universal refined distance law.** The hexagon \(kH\) decomposes into \(6k^2\) congruent equilateral triangles of side length one with vertices in \(kH\cap L\). Within any such small triangle, one of its three corners is a closest triangular-lattice point: this follows by the perpendicular-bisector description of the triangular-lattice Delaunay tessellation. Every closest corner is among the admissible finite set \(kA_k\). Hence the nearest-point distance from a uniform point of \(kH\) has the same distribution as the distance from a uniform point of a single unit equilateral triangle to its three corners. Reflecting the six equilateral triangles at each lattice vertex shows that this is also the distance from a uniformly sampled point of the triangular lattice's regular hexagonal Voronoi cell to its center.

That cell has inradius \(a=1/2\), circumradius \(1/\sqrt3\), and area \(\sqrt3/2\). For \(t\le a\), the disk of radius \(t\) lies wholly in the cell, giving probability \(\pi t^2/(\sqrt3/2)\). For \(a<t<1/\sqrt3\), subtract the six disjoint circular segments exterior to the six cell sides. Each segment has area \(t^2\arccos(a/t)-a\sqrt{t^2-a^2}\). Dividing the remaining disk area by \(\sqrt3/2\) proves the displayed formula for \(F_*\), including both endpoint values. Its support endpoint gives the refined Hausdorff radius.

**3. The exceptional first distribution.** At \(k=1\), the Voronoi partition of \(H\) relative to the six vertices consists of six congruent kites bounded by one original vertex, two incident side midpoints, and the origin. In polar coordinates based at one vertex and pointing inward, with angular deviation \(\phi\in[-\pi/3,\pi/3]\), the radial boundary of its kite is
\[
 \rho(\phi)=\frac1{2\sin(\pi/6+|\phi|)}.
\]
A radius-\(t\) ball meets that kite in area \(\frac12\int_{-\pi/3}^{\pi/3}\min\{t,\rho(\phi)\}^2\,d\phi\). Multiply by six and divide by \(\operatorname{area}(H)=3\sqrt3/2\). For \(t\le1/2\) the integral has no truncation; for \(1/2<t<1\), split at the unique angle solving \(\rho(\phi)=t\) and integrate \(\csc^2\). The resulting expression is exactly \(F_1\). The common origin is distance one from every original vertex, proving the initial Hausdorff distance, and no point can be farther by the kite description.

**4. Moments.** For any nonnegative bounded random variable \(Y\), \(\mathbb EY^2=\int_0^\infty 2t[1-F_Y(t)]\,dt\). Substitution of the two explicit CDFs (or direct polar second-moment integration on the kite and Voronoi hexagon) gives respectively \(1/4\) and \(5/36\). Scaling back by \(k^{-2}\) proves the stated exact mean squared errors.

## Verification
A standalone Python 3 script, `verify.py`, enumerates all lattice sites and all finite vertex sums for \(1\le k\le9\); checks the analytical second moments with independent numerical quadrature; and compares the predicted CDFs and moments with directly computed nearest-site distances of independently sampled uniform points in the hexagon for \(1\le k\le6\). All assertions passed. These finite and numerical checks are supplementary to Steps 1–4 and do not establish the all-\(k\) result.

## Relationship to prior work
The general convexification effect of iterated Minkowski averaging is well established, but general bounds do not specify this two-stage finite-hexagon distribution. Classical triangular-lattice Voronoi geometry already supplies the hexagonal cell and its second moment; no novelty is claimed for that isolated classical fact. Work on optimal conditional quantization with six prescribed hexagon vertices optimizes added sites, whereas this theorem studies the rigid arithmetic site sets produced by equal-weight vertex sums, with no optimization. General results about lattice points in Minkowski sums begin with full lattice-point sets, not only hexagon vertices. The distinctive conclusion here is the exact saturation at two summands and the consequent full finite-configuration quantization law for all subsequent averaging orders.

## Limitations
This theorem is limited to a regular Euclidean hexagon, equal summand weights, uniform area measure, and Euclidean distance. It does not assert optimality among quantizer configurations or generalize automatically to other polygons. It is a self-contained analytical argument with supplementary finite tests; independent mathematical validation and a definitive historical-priority determination have not been performed. Earlier geometric-quantization results may contain equivalent observations under different notation.

## References
- Peter van Hintum, *The sharp threshold for Hausdorff convexification under Minkowski addition*, arXiv:2606.10815 (initial version 2026-06-09), https://arxiv.org/abs/2606.10815.
- Christina Hamilton, Evans Nyanney, Megha Pandey and Mrinal K. Roychowdhury, *Conditional constrained and unconstrained quantization for a uniform distribution on a hexagon*, arXiv:2401.10987 (2024), https://arxiv.org/abs/2401.10987.
- Carl P. Dettmann and Mrinal K. Roychowdhury, *Quantization for uniform distributions on triangles*, arXiv:1508.00498 (2015), https://arxiv.org/abs/1508.00498.
- M. Haimovich and T. L. Magnanti, *Extremum Properties of Hexagonal Partitioning and the Uniform Distribution in Euclidean Location*, SIAM Journal on Discrete Mathematics 1 (1988), 50–64, https://doi.org/10.1137/0401006.
- Christian Haase, Benjamin Nill, Andreas Paffenholz and Francisco Santos, *Lattice Points in Minkowski Sums*, Electron. J. Combin. 15 (2008), #N11, https://doi.org/10.37236/886.
