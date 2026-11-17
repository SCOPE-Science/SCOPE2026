# A sharp eight-edge bound and a uniform separation law for side disks of equiangular pentagons

## Finding
Let \(P\) be any strictly convex equiangular Euclidean pentagon, with sides \(s_0,\ldots,s_4\) in counterclockwise order, side lengths \(\ell_i>0\), perimeter \(L=\sum_{i=0}^{4}\ell_i\), and closed diameter disks \(D_i\) whose diameters are the sides \(s_i\). Define the signed distance between the two nonadjacent disks indexed by \(i\) and \(i+2\) as
\[
\Delta_i=|m_{i+2}-m_i|-\frac{\ell_i+\ell_{i+2}}2,
\]
where \(m_i\) is the midpoint of \(s_i\) and subscripts are modulo five. Set \(q=\cos(2\pi/5)=(\sqrt5-1)/4\).

**Theorem.** At least two different indices \(i\) satisfy
\[
\Delta_i\ge\frac{qL}{12}=\frac{(\sqrt5-1)L}{48}>0.
\]
Consequently at least two nonadjacent pairs of side disks are disjoint; the intersection graph of the five diameter disks has at most eight edges. The eight-edge bound is attained by a strictly convex equiangular pentagon. The numerical factor in the separation assertion is explicit, not claimed optimal.

The general planar bound on side-disk intersection graphs gives nine edges for five vertices; the extra forbidden edge here is a consequence of the equiangular condition.

## Assumptions and scope
The five sides are nonzero, the polygon is simple and strictly convex, and its five interior angles are all \(3\pi/5\). Diameter disks are **closed**, so adjacent side disks always intersect at their shared polygon vertex. No inradius normalization or cyclicity assumption is imposed. A nonadjacent disk pair is disjoint precisely when its signed gap \(\Delta_i\) is positive.

Up to a Euclidean rotation, the unit vectors along the directed edges are
\[
e_j=(\cos(2\pi j/5),\sin(2\pi j/5)),\qquad
\sum_{j=0}^4\ell_j e_j=0.
\]
These directions close to a strictly convex equiangular pentagon whenever all \(\ell_j>0\) and the closure equation holds.

## Proof
Write \(\delta=(1-q)/2\) and
\[
g_i=\ell_{i+1}-\delta(\ell_i+\ell_{i+2}).
\]
The vector joining the centers of two nonadjacent diameter disks is
\[
m_{i+2}-m_i=\frac{\ell_i}{2}e_i+\ell_{i+1}e_{i+1}+\frac{\ell_{i+2}}2e_{i+2}.
\]
Its scalar projection on \(e_{i+1}\) is \(\ell_{i+1}+q(\ell_i+\ell_{i+2})/2\). Since a vector norm is at least its projection, subtracting the sum of the two disk radii yields the **directional separation lemma**
\[
\Delta_i\ge g_i.\tag{1}
\]

Put \(r=\cos(4\pi/5)=-q-1/2\). The horizontal component of polygon closure reads
\[
\ell_0+q(\ell_1+\ell_4)+r(\ell_2+\ell_3)=0.\tag{2}
\]
Straight expansion using \(\delta=(1-q)/2\) gives the exact positive-coefficient identity
\[
\begin{aligned}
&g_0+2g_1+2g_2+g_3\\
&\quad+\ell_0+q(\ell_1+\ell_4)+r(\ell_2+\ell_3)\\
&=q\left(\ell_0+2\ell_1+\frac{\ell_2+\ell_3}{2}+2\ell_4\right).
\end{aligned}\tag{3}
\]
By (2), the second line on the left vanishes. The right side is at least \(qL/2\), because each coefficient inside the parentheses is at least \(1/2\). The weights \(1,2,2,1\) total six, so one of \(g_0,g_1,g_2,g_3\) is at least \(qL/12\), and by (1) its disk pair has this much separation. Cyclic rotation of the index origins shows that **among any four** of the five nonadjacent pairs, one has separation at least \(qL/12\). If only one pair had that property, choosing the four others would contradict this statement. Therefore at least two pairs do, proving the quantified nonintersection and the upper bound of eight graph edges.

For sharpness, set \(t=1/100\) and
\[
(\ell_0,\ell_1,\ell_2,\ell_3,\ell_4)=(t,1,b,b,1),\qquad
b=\frac{t+2q}{1+2q}=\frac{299-99\sqrt5}{200}>0.
\]
The imaginary part of the closure equation vanishes by reflection symmetry, and its real part vanishes by the definition of \(b\). Thus the five positive directed edge lengths define a strictly convex equiangular pentagon.

To decide disk intersections exactly, define
\[
H_i=|m_{i+2}-m_i|^2-\left(\frac{\ell_i+\ell_{i+2}}2\right)^2
=\ell_{i+1}^2+q\ell_{i+1}(\ell_i+\ell_{i+2})
+\frac{r-1}{2}\ell_i\ell_{i+2}.
\]
For these lengths, direct exact simplification yields
\[
\begin{aligned}
H_0=H_3&=\frac{20049\sqrt5-50}{40000}>0,\\
H_1=H_2&=\frac{7500\sqrt5-17449}{20000}<0,\\
H_4&=-\frac{6299}{10000}-\frac{3\sqrt5}{25}<0.
\end{aligned}
\]
For example the middle inequality follows by comparing positive squares: \(45\cdot20000^2<64\cdot17449^2\). Exactly the three nonadjacent pairs indexed \(1,2,4\) therefore intersect; the pairs indexed \(0,3\) are disjoint. All five adjacent pairs intersect. Hence the graph has exactly \(5+3=8\) edges.

For contrast, an unrestricted strictly convex pentagon with vertices
\[
(-997,-99),\ (689,-897),\ (227,240),\ (55,381),\ (-10,414)
\]
in that cyclic order has four intersecting nonadjacent disk pairs: \((0,2),(0,3),(1,4),(2,4)\). Direct integer-square comparisons verify this statement and all five strictly positive consecutive cross products. Thus the equiangular assumption genuinely excludes a graph with nine edges, which is possible without it.

## Verification
The standalone script `check_side_disks.py` checks the five exact radical sign identities, the four-inequality positive certificate, closure of the explicit extremizer, and the integer-coordinate nine-edge contrast using exact arithmetic; it also tests the quantitative bound on thousands of independently chosen positive-length equiangular pentagons. Running `python check_side_disks.py` with SymPy available prints `EQUIANGULAR_PENTAGON_DISK_CHECKS_OK`. The infinite theorem is proved by equations (1)–(3), not inferred from the finite checks.

## Relationship to prior work
Huemer and Pérez-Lantero, *The intersection graph of the disks with diameters the sides of a convex \(n\)-gon* (arXiv:1410.4126, initially public on 2014-10-14), prove planarity of the side-disk graph for arbitrary convex polygons. In particular their theorem forces at least one nonedge for pentagons and an upper bound of nine edges, but not the stated two separated nonedges or sharp eight-edge bound restricted to equiangular pentagons. Herrera and Pérez-Lantero, *On the intersection graph of the disks with diameters the sides of a convex \(n\)-gon* (arXiv:1805.10847, 2018), establish treewidth at most three and several graph-realizability statements, but do not identify this fixed-angle quantitative obstruction. The relevant full-text mathematical statements were compared, not merely their titles.

## Limitations
The conclusion is specific to five sides with equal turning angles and does not assert an eight-edge upper bound for arbitrary pentagons; the given integer witness shows that stronger unrestricted statement is false. The explicit separation coefficient is not optimized. The result does not classify all realizable side-disk graphs of equiangular pentagons, and historical originality remains subject to independent literature review.

## References
1. C. Huemer and P. Pérez-Lantero, *The intersection graph of the disks with diameters the sides of a convex n-gon*, arXiv:1410.4126, initial submission 2014-10-14. https://arxiv.org/abs/1410.4126
2. L. H. Herrera and P. Pérez-Lantero, *On the intersection graph of the disks with diameters the sides of a convex n-gon*, arXiv:1805.10847, initial submission 2018-05-28. https://arxiv.org/abs/1805.10847
