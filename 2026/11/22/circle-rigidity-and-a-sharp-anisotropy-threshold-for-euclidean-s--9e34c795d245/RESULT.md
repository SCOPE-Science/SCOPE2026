# Circle rigidity and a sharp anisotropy threshold for Euclidean spanning trees of antipodal ellipse quadruples

## Finding

For a centrally symmetric strictly convex planar oval, consider Euclidean minimum spanning trees of the four boundary points formed by any two antipodal pairs. The circle is characterized by the existence of a boundary-only minimum spanning tree for **every** such quadruple. On every noncircular smooth centrally symmetric oval, an open set of pairs instead forces an antipodal edge in **every** minimum spanning tree.

For ellipses this qualitative distinction admits a complete quantitative probability law, a sharp positive-measure all-separation phase transition at axis ratio \(\sqrt 3\), and an exact first variation away from circularity.

Let \(k=a/b\ge1\), and for \(t\in[0,\pi)\) set
\[
 r_k^2=k^2\cos^2t+\sin^2t,\qquad
 q_k^2=k^2\sin^2t+\cos^2t,\qquad
 h_k=\tfrac12(k^2-1)|\sin2t|.
\]
Define
\[
 F_k(t)=\min\!\left\{1,\frac2\pi\left[
 \arctan\frac{2h_k}{r_k^2}+\arctan\frac{2h_k}{q_k^2}
 \right]\right\}.
\]
For two independent eccentric-anomaly parameters uniform modulo antipodes, the probability that every Euclidean minimum spanning tree has an antipodal edge is exactly
\[
 \mathcal P(k)=\frac1\pi\int_0^\pi F_k(t)\,dt.
\]
It is strictly increasing on \([1,\infty)\), has \(\mathcal P(1)=0\), and tends to one. Moreover,
\[
 \mathcal P(1+\varepsilon)=\frac{16}{\pi^2}\varepsilon+O(\varepsilon^2)
 \qquad(\varepsilon\downarrow0).
\]

The fraction of mid-orientations for which **every** nondegenerate separation forces an antipodal edge is zero for \(1\le k\le\sqrt3\). For \(k>\sqrt3\) it is
\[
 H(k)=1-\frac2\pi\arcsin\frac{2k}{\sqrt3(k^2-1)}.
\]
Statements about every separation are understood away from the finite set of tied edge lengths. The probability law is unaffected by these zero-measure exceptions.

## Assumptions and scope

The oval is the boundary of a compact strictly convex planar body, has a continuous regular tangent, is centrally symmetric about the origin, and is \(C^1\); the circle theorem requires no prescribed probability measure. Given two distinct antipodal pairs \(\{u,-u\}\), \(\{v,-v\}\), their cyclic order is \(u,v,-u,-v\) up to reversal. The four boundary edges connect consecutive vertices, while the two antipodal edges connect \(u\) to \(-u\) and \(v\) to \(-v\). A minimum spanning tree (MST) is a minimum-total-Euclidean-length spanning tree of the complete graph on these vertices. It need not be unique when the boundary has repeated side lengths. Call a quadruple *shortcut-forcing* if **every** MST includes at least one antipodal edge.

For the probability formula, use the ellipse parametrization \(P(\theta)=(a\cos\theta,b\sin\theta)\) with \(a\ge b>0\). The two independent parameters are uniform on \([0,\pi)\), selecting antipodal pairs, not arclength-uniform boundary points or four independent boundary points. The event of equality between a diagonal and a boundary edge has probability zero for \(a>b\); the circle is handled directly. All quantities depend only on \(k=a/b\).

## Proof

**1. Four-point MST lemma.** For any nondegenerate centered parallelogram with vertices in cyclic order \(u,v,-u,-v\), the four boundary edges have alternating lengths \(s=|u-v|\) and \(T=|u+v|\); the two diagonals have lengths \(2|u|\) and \(2|v|\). Put \(d=2\min(|u|,|v|)\). Away from equalities, the quadruple is shortcut-forcing if and only if
\[
 d>0\quad\text{and}\quad d<\max(s,T).
\]
Indeed, if both diagonals exceed the longer boundary-side length, three boundary edges realize an MST and no diagonal can improve it by the cycle property. Otherwise, the two copies of the shorter side connect two disjoint pairs; the least edge joining those two components is the shorter diagonal when \(d<\max(s,T)\), rather than either copy of the longer side. This remains true when the diagonal is even shorter than the nominal short side: Kruskal's ordering still includes the diagonal and suitable boundary edges. At equality, the claimed strict dichotomy is replaced by possible ties. In particular, any strict inequality \(d<\max(s,T)\) forces a diagonal in every MST.

**2. Circle rigidity.** If all four points lie on a radius-\(R\) circle, both diagonals have length \(2R\), strictly larger than either boundary side for distinct noncoincident antipodal pairs. Hence boundary-only MSTs exist. Conversely, if a centrally symmetric \(C^1\) oval is not a circle, its radial function is not constant. Along a smoothly parametrized oriented arc there is a point where its radial distance strictly increases, so one may choose arbitrarily close boundary points \(u,v\) in positive cyclic order with \(|v|-|u|\) positive and of first order in their separation. Then \(|u-v|\) tends to zero, while
\[
 |u+v|-2|u|=|v|-|u|+O(|u-v|^2)>0
\]
for sufficiently close points. Thus \(2|u|<|u+v|\), and the lemma forces an antipodal edge. The strict inequality persists on an open neighborhood of the chosen pair.

**3. Independent mid-angle and half-gap.** Let \(\alpha=(\psi-\phi)\bmod\pi\in[0,\pi)\), \(t=(\phi+\alpha/2)\bmod\pi\), and \(\delta=\alpha/2\in[0,\pi/2)\). Translation invariance of uniform measure modulo \(\pi\) makes \(t\) and \(\delta\) independent and uniform on these intervals. The two sampled representatives are
\[
 u=P(t-\delta)=w\cos\delta-v\sin\delta,\qquad
 u'=P(t+\delta)=w\cos\delta+v\sin\delta,
\]
where \(w=P(t)\) and \(v=P'(t)\). Scale \(b\) to one; then \(|w|^2=r_k^2\), \(|v|^2=q_k^2\), \(|w\cdot v|=h_k\), and \(r_k^2q_k^2-h_k^2=k^2\). The boundary sides have lengths \(2|v|\sin\delta\) and \(2|w|\cos\delta\); the shorter antipodal diagonal has squared length
\[
 d^2=4\bigl(r_k^2\cos^2\delta+q_k^2\sin^2\delta-2h_k\sin\delta\cos\delta\bigr).
\]
Set \(z=\tan\delta\). The lemma and the exact comparison with the longer boundary side show that **no** shortcut is forced precisely when
\[
 \frac{2h_k}{q_k^2}\le z\le\frac{r_k^2}{2h_k}.
\]
For \(h_k=0\) interpret this as the whole positive half-line. If the lower bound exceeds the upper bound the nonshortcut interval is empty. Since \(z=\tan\delta\) and \(\delta\) is uniform on \([0,\pi/2)\), taking the complementary probability gives exactly \(F_k(t)\) and integration over uniform \(t\) gives \(\mathcal P(k)\).

**4. Rigorous threshold.** The no-shortcut interval is empty exactly when \(4h_k^2>r_k^2q_k^2\). From the determinant identity this is equivalent to \(3h_k^2>k^2\), or
\[
 |\sin2t|>\frac{2k}{\sqrt3(k^2-1)}.
\]
Such orientations have positive measure precisely when \(k>\sqrt3\). Their fraction is the stated \(H(k)\), obtained by measuring a superlevel set of \(|\sin2t|\) on \([0,\pi)\). The boundary equality has measure zero in orientation.

**5. Monotonicity and endpoint limits.** Write \(x=k^2-1\ge0\). For fixed \(t\) off the axes, the two arctangent arguments are
\[
 \frac{x|\sin2t|}{1+x\cos^2t},\qquad
 \frac{x|\sin2t|}{1+x\sin^2t},
\]
each strictly increasing in \(x\). Thus \(F_k(t)\) is nondecreasing and strictly increasing on a positive-measure set for every finite increment \(k_1<k_2\); hence \(\mathcal P\) increases strictly. For fixed nonaxial \(t\), the product of the two arguments exceeds one for all sufficiently large \(k\), so \(F_k(t)\to1\). Dominated convergence yields \(\mathcal P(k)\to1\).

At \(k=1+\varepsilon\), uniformly in \(t\) and before clipping,
\[
 h_k=\varepsilon|\sin2t|+O(\varepsilon^2),\qquad
 F_k(t)=\frac8\pi\varepsilon|\sin2t|+O(\varepsilon^2).
\]
Using \(\pi^{-1}\int_0^\pi|\sin2t|\,dt=2/\pi\) gives the stated coefficient \(16/\pi^2\).

## Verification

The included `CHECK.py` independently enumerates all six distances and runs Kruskal's algorithm on deterministic random four-point samples, comparing the presence of an antipodal edge with the analytic inequality (strict cases only). It also evaluates the one-dimensional probability integral, checks the \(\sqrt3\) phase boundary, verifies its near-circle coefficient, and compares against direct random geometric sampling. These finite numerical checks are supporting evidence; the all-ellipse claim and rigidity follow from the analytic steps above, not finite enumeration.

## Relationship to prior work

The Euclidean MST and proximity-graph inclusions are classical. Toussaint's work on relative neighborhood graphs gives a general framework for Euclidean MST edge screening; the present event is more precise than general graph inclusion. Bose, De Carufel, Shaikhet and Smid give graph-theoretic algorithmic results on constrained proximity graphs, not a shape-specific antipodal-pair probability law. The new conclusion here is the exact four-point circular rigidity, the complete ellipse shortcut probability, and a sharp nontrivial anisotropy threshold, not the MST algorithm or basic cycle/cut properties.

## Limitations

The quantitative law assumes independent **uniform eccentric-anomaly** antipodal pair samples on planar ellipses. It is not an arclength-uniform law, not a law for four independently sampled points, and not an MST statement on all possible sample sizes. The circle rigidity requires central symmetry and regular smooth strict convexity. The measure-zero edge-tie cases do not determine the probability but require the weaker nonuniqueness convention. The formula involves a one-dimensional integral rather than a claimed elementary antiderivative. Historical priority beyond the inspected published sources is not definitively established; independent mathematical validation has not been carried out.

## References

1. G. T. Toussaint, *The Relative Neighbourhood Graph of a Finite Planar Set*, Pattern Recognition 12 (1980), 261–268, DOI: 10.1016/0031-3203(80)90066-7, full text: https://cgm.cs.mcgill.ca/~godfried/teaching/mir-reading-assignments/RNG.pdf.
2. P. Bose, J.-L. De Carufel, S. Shaikhet and M. Smid, *Essential Constraints of Edge-Constrained Proximity Graphs*, original public preprint dated 2016-07-05, https://arxiv.org/abs/1607.01294.
3. General edge-optimality framework: minimum spanning tree cycle and cut properties, https://en.wikipedia.org/wiki/Minimum_spanning_tree.
