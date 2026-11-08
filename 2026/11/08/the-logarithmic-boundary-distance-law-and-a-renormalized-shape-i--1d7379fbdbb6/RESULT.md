# The logarithmic boundary-distance law and a renormalized shape invariant for ideal hyperbolic polygons

## Finding

Let \(P\) be a convex ideal \(n\)-gon in the complete curvature-\(-1\) hyperbolic plane, with \(n\ge3\) pairwise distinct ideal vertices \(v_1,\dots,v_n\) in cyclic order; indices are cyclic. Let \(X\) have uniform hyperbolic area distribution on \(P\), whose area is \((n-2)\pi\), and define \(D_P=d_{\mathbb H}(X,\partial P)\). For boundary points represented in the disk model as unit complex numbers, set

\[
\mathcal L(P)=2\log\!\left(\frac{\prod_{i=1}^n|v_{i-1}-v_{i+1}|}{\prod_{i=1}^n|v_i-v_{i+1}|}\right).
\]

Then the logarithmic and finite coefficients of the boundary-distance distribution are both exact:

\[
\boxed{\Pr(D_P\le s)=\frac{2n}{(n-2)\pi}\,s\log(1/s)+\frac{\mathcal L(P)+2n(1-\log 2)}{(n-2)\pi}\,s+O_P(s^2),\quad s\downarrow0.}
\]

The real number \(\mathcal L(P)\) is invariant under every hyperbolic isometry and is a finite, horocycle-independent renormalized perimeter. Thus the first term only detects the number of ideal vertices, whereas the second term detects polygon shape.

For every ideal quadrilateral \(Q\),
\[
\boxed{\mathcal L(Q)\ge4\log2,}
\]
with equality precisely for the regular ideal quadrilateral up to hyperbolic isometry. Therefore the regular ideal quadrilateral uniquely minimizes the second-order boundary occupation coefficient among ideal quadrilaterals.

In the ideal triangle case the complete law is also explicit. Set \(\rho=\operatorname{arsinh}(1/\sqrt3)=\frac12\log3\). For \(0<s<\rho\),
\[
\boxed{\Pr(D_P\le s)=\frac6\pi\bigl[\arctan(\sinh s)-\sinh s\log(2\tanh s)\bigr],}
\]
with CDF zero for \(s\le0\), one for \(s\ge\rho\), and density
\[
\boxed{f_{D_P}(s)=\frac6\pi\cosh s\log\frac1{2\tanh s}.}
\]
The maximal-distance tail satisfies
\[
\boxed{\Pr(D_P>\rho-\varepsilon)\sim\frac{3\sqrt3}{\pi}\varepsilon^2,\quad \varepsilon\downarrow0.}
\]
These assertions are one cohesive boundary-distance theorem, with the quadrilateral and ideal-triangle statements as geometric consequences and a solvable benchmark.

## Assumptions and scope

All distances are intrinsic hyperbolic distances in curvature \(-1\). Every side of \(P\) is a complete geodesic with ideal endpoints; the boundary means the union of these geodesic sides (ideal endpoints themselves are not interior points). Area-uniform sampling is legitimate because the area of every ideal \(n\)-gon is finite, \((n-2)\pi\). The constants implicit in \(O_P(s^2)\) depend on the fixed polygon; no uniformity under degeneration is claimed. Chords in the definition of \(\mathcal L(P)\) are *Euclidean* distances between distinct points on the boundary of any disk model, not hyperbolic side lengths. The displayed expression is independent of the chosen disk chart.

## Proof

### 1. Horocyclic decomposition and the universal logarithm

Take pairwise disjoint horoball neighborhoods \(H_i\) at the ideal vertices, each disjoint from the nonincident sides. The complement \(K=P\setminus\bigcup_i H_i\) is compact. Let \(L_0\) denote the sum of the true hyperbolic lengths of its truncated geodesic side portions. Map a neighborhood of each cusp isometrically to \(\{(x,y):0<x<w_i,\ y\ge Y_i\}\) in the upper half-plane \(ds^2=(dx^2+dy^2)/y^2\). Its horocyclic width is \(h_i=w_i/Y_i\).

Set \(k=\sinh s\). Inside the cusp the distance to the nearest of the two adjacent vertical sides is \(\operatorname{arsinh}(\min\{x,w_i-x\}/y)\). For sufficiently small \(s\), all other sides stay farther away in these cusp regions. Since \(2kY_i<w_i\), the exact cusp contribution to the \(s\)-boundary layer is

\[
I_i(s)=\int_{Y_i}^{\infty}\frac{\min(w_i,2ky)}{y^2}\,dy=2k\bigl(1+\log(h_i/(2k))\bigr).
\]

Within the compact complement, hyperbolic Fermi coordinates \((u,t)\) along each geodesic side have area element \(\cosh(t)\,du\,dt\). Ignoring the finitely many endpoints of artificial horocycle cuts, the inward normal strips therefore contribute exactly \(L_0\sinh s\). Each artificial-cut endpoint changes the strip area by at most \(O_P(s^2)\): the horocycle and geodesic meet at a nonzero fixed angle, so the discrepancy is contained in finitely many diameter-\(O(s)\) neighborhoods in the compact region. Distinct side strips are disjoint outside these endpoint regions for sufficiently small \(s\). Hence the total boundary-layer area \(B_P(s)\) satisfies

\[
B_P(s)=2nk\log(1/k)+k\bigl[L_0+2\sum_i\log h_i+2n(1-\log2)\bigr]+O_P(s^2).
\]

Since \(k=s+O(s^3)\), dividing by \(\operatorname{Area}(P)=(n-2)\pi\) gives the asserted expansion with \(\mathcal L(P)=L_0+2\sum_i\log h_i\).

### 2. Renormalized perimeter and the chord product

Changing the truncation horoball at vertex \(i\) by a fixed height factor changes its two adjacent truncated side lengths by the compensating amount and changes \(\log h_i\) by the opposite factor, proving that \(L_0+2\sum_i\log h_i\) is independent of the truncation.

To compute it, use the upper-half-plane model and an isometry moving all ideal vertices to finite real values \(a_i\) (possible by choosing the pole away from their finite set). Let \(d_i\) be the Euclidean diameter of a sufficiently small horoball at \(a_i\). The geodesic from \(a_i\) to \(a_{i+1}\) between its two horoball cuts has hyperbolic length

\[
\ell_{i,i+1}=\log\frac{|a_i-a_{i+1}|^2}{d_i d_{i+1}}.
\]

The horocyclic width at vertex \(i\), obtained by mapping \(a_i\) to infinity, equals

\[
h_i=\frac{d_i|a_{i-1}-a_{i+1}|}{|a_i-a_{i-1}|\,|a_i-a_{i+1}|}.
\]

On summation all \(d_i\) cancel, and each neighbor chord occurs with multiplicity two, giving exactly

\[
L_0+2\sum_i\log h_i=2\log\frac{\prod_i|a_{i-1}-a_{i+1}|}{\prod_i|a_i-a_{i+1}|}.
\]

Under a fractional linear transformation, each boundary chord length gains a factor that is the product of one factor at each endpoint. Every vertex appears twice in the numerator and twice in the denominator. The quotient is therefore Möbius invariant and agrees with the disk-model formula.

### 3. Quadrilateral minimizer

For ideal quadrilateral vertices \(v_1,v_2,v_3,v_4\), let \(x=|v_1-v_2||v_3-v_4|\) and \(y=|v_2-v_3||v_4-v_1|\). By Ptolemy's theorem for the four concyclic points, \(|v_1-v_3||v_2-v_4|=x+y\), and hence

\[
\mathcal L(Q)=2\log\frac{(x+y)^2}{xy}\ge2\log4=4\log2.
\]

Equality holds exactly when \(x=y\). The positive cross-ratio ratio \(x/y\) parametrizes ideal quadrilateral shape up to hyperbolic isometry, and its value \(1\) is represented by the regular ideal quadrilateral. This proves uniqueness up to isometry. The coefficient comparison follows because all ideal quadrilaterals have the same leading \(s\log(1/s)\) coefficient and area \(2\pi\).

### 4. Exact ideal-triangle distribution

All ideal triangles are congruent. Choose vertices \(0,1,\infty\). Then \(P=\{0<x<1,\ y^2>x(1-x)\}\). Put \(v=x/y\), \(w=(1-x)/y\). The hyperbolic area form is \(dv\,dw/(v+w)\), and the hyperbolic sines of the distances to the three sides are, respectively, \(v\), \(w\), and \((1-vw)/(v+w)\).

For \(k=\sinh s>0\), the distance condition \(D_P\ge s\) is therefore

\[
v\ge k,\qquad w\ge k,\qquad (v+k)(w+k)\le1+k^2.
\]

The region is empty if \(k>1/\sqrt3\); hence the inradius is \(\rho=\operatorname{arsinh}(1/\sqrt3)\). For \(0<k<1/\sqrt3\), its area is

\[
A_s=\int_{k}^{(1-k^2)/(2k)}\log\frac{1+v^2}{(v+k)^2}\,dv
=\pi-6\arctan k+6k\log\frac{2k}{\sqrt{1+k^2}}.
\]

Since \(\operatorname{Area}(P)=\pi\), the CDF is \(1-A_s/\pi\). Using \(k/\sqrt{1+k^2}=\tanh s\) gives the formula above, and differentiation yields the displayed density. Finally, expanding this density around \(\rho\), where it vanishes to first order, gives \(\Pr(D_P>\rho-\varepsilon)=\frac{3\sqrt3}{\pi}\varepsilon^2+O(\varepsilon^3)\); equivalently this follows from the shrinking triangular region in \((v,w)\)-coordinates.

## Verification

An independent computational implementation is embedded at `checks/ideal_polygon_checks.py`. It integrates the triangular survival-probability formula numerically and compares it with the elementary CDF across seven thresholds, obtaining absolute errors less than \(2\times10^{-13}\). In three ideal-quadrilateral shapes (cross-ratio representatives \(0,1,t,\infty\) with \(t=2,3,5\)), a low-discrepancy area-uniform sample of \(2^{19}\) points per shape confirms the predicted two-term asymptotic at three small thresholds; the largest observed difference is less than \(1.3\times10^{-5}\). The quadrilateral invariant is independently calculated from the chord/cross-ratio expression. Tests support but cannot establish infinite-domain or asymptotic correctness; the proof above supplies that argument.

To reproduce, use Python 3 with NumPy and SciPy and run `python checks/ideal_polygon_checks.py` after extraction into a common directory. All randomization uses a fixed Sobol seed.

## Relationship to prior work

Gallego and Solanes (2001) examine perimeter, diameter, area, and parallel constructions for compact hyperbolic convex sets. Their results do not give a finite-area ideal-polygon boundary-distance distribution or its second-order renormalized coefficient. Binbin Xu (2014), building on Bridgeman and Dumas, determines *Liouville-geodesic chord-length distributions* for ideal triangles and quadrilaterals; that experiment chooses a geodesic, not an area-uniform point, and does not imply the nearest-side distance law. Arnold, Fuchs, Izmestiev and Tabachnikov (2018) describe decorated ideal polygons and an alternating signed perimeter, rather than the unsigned boundary-layer renormalization or its quadrilateral inequality. Lutz (2022) develops horocyclic decorations and generalized lengths for canonical tessellations; those ingredients provide pertinent geometric context but not the boundary occupation theorem.

The classical ideal-triangle area \(\pi\), inradius \(\frac12\log3\), the hyperbolic Fermi area element, and Ptolemy's theorem are established background, not proposed new discoveries. The claimed contribution is their explicit combination in a universal shape-sensitive two-term boundary-distance theorem, with the sharp quadrilateral extremizer and exact point-sampling triangle law.

## Limitations

The result concerns fixed finite-sided convex ideal polygons in the complete curvature-\(-1\) plane. No uniform error bound is asserted when vertices coalesce, the side number grows, or curvature changes. The exact global CDF is stated only for ideal triangles, not arbitrary ideal polygons. Numerical experiments are finite and do not prove any infinite claim. Historical priority has been checked against the named full-text sources and relevant available records but cannot be guaranteed exhaustive; a previously overlooked general renormalized tube formula could imply part of this theorem. Independent mathematical validation has not been conducted.

## References

- E. Gallego and G. Solanes, *Perimeter, Diameter and Area of Convex Sets in the Hyperbolic Plane*, Journal of the London Mathematical Society 64 (2001), 161–178. DOI: `10.1112/S002461070100223X`. Original author-hosted text: `https://mat.uab.cat/~egallego/papers/Diperen3%20.pdf`. Published online 2001-08-24.
- B. Xu, *On the Ambartzumian-Pleijel identity in hyperbolic geometry*, arXiv:1410.4052 (first submitted 2014-10-15); `https://arxiv.org/abs/1410.4052`.
- Martin Bridgeman and David Dumas, *Distribution of intersection lengths of a random geodesic with a geodesic lamination*, Ergodic Theory and Dynamical Systems 27 (2007), 1055–1072, as cited and compared in Xu.
- D. Arnold, D. Fuchs, I. Izmestiev, and S. Tabachnikov, *Cross-ratio dynamics on ideal polygons*, arXiv:1812.05337 (first submitted 2018-12-13); `https://arxiv.org/abs/1812.05337`.
- C. O. R. Lutz, *Canonical tessellations of decorated hyperbolic surfaces*, Geometriae Dedicata (2022). DOI: `10.1007/s10711-022-00746-y`.
