# A universal logarithmic small-area law for polygon-boundary triangles

## Finding

Let \(K\) be a convex Euclidean polygon with \(m\ge4\) genuine sides (no collinear consecutive sides), side lengths \(\ell_1,\ldots,\ell_m>0\), total perimeter \(P=\sum_i\ell_i\), and interior angles \(\alpha_i\in(0,\pi)\), indexed so that side \(i-1\) and side \(i\) meet at vertex \(i\). Sample \(X_1,X_2,X_3\) independently from normalized boundary arclength on \(\partial K\), and write \(A=\operatorname{Area}[X_1,X_2,X_3]\). Then

\[
\Pr(A=0)=\sum_{i=1}^m(\ell_i/P)^3
\]

and, as \(s\downarrow0\),

\[
\boxed{\Pr(0<A/P^2\le s)=C(K)s\log(1/s)+O_K(s),\qquad
C(K)=\frac{12}{P}\sum_{i=1}^m\frac{\ell_{i-1}+\ell_i}{\sin\alpha_i}.}
\]

The sharp shape inequality is \(C(K)\ge24\), with equality if and only if \(K\) is a rectangle, with no restriction on aspect ratio. In particular, any rectangle has the same leading nonzero small-area probability after scaling area by squared perimeter. For a unit square, \(\Pr(A=0)=1/16\) and \(\Pr(0<A\le t)=\tfrac32t\log(1/t)+O(t)\). The triangular host is excluded because its boundary-area distribution was previously determined.

There is also a limiting geometric description. Condition on \(0<A\le t\), and put \(s=t/P^2\). With conditional probability tending to one, precisely two sampled points lie on a common side \(i\), and the third lies on an adjacent side \(j\). The pattern \((i,i;j)\) specifies which side is repeated and which is the singleton, without specifying the sample labels. Its limiting probability is

\[
\frac{\ell_i/\sin\alpha_v}{\sum_w(\ell_{w-1}+\ell_w)/\sin\alpha_w},
\]

where \(v\) is the shared vertex. Given this pattern, let \(u\) be the arclength gap on side \(i\) and \(b\) the smaller of the two arclength coordinates measured from any fixed endpoint. Put

\[
Q_t=\frac{\log(u/\ell_i)}{\log(t/P^2)},\qquad Z_t=A/t,\qquad B_t=b/\ell_i.
\]

Jointly, the pattern, \(Q_t\), \(Z_t\), and \(B_t\) converge to the stated discrete pattern law times three independent uniform laws on \([0,1]\). The marks may be defined arbitrarily on the other patterns, whose conditional mass vanishes.

## Assumptions and scope

The polygon is fixed while \(t\downarrow0\). Boundary sampling is by ordinary Euclidean arclength, not uniform selection of a side or sampling from the polygon interior. The ownership of a vertex by one or the other of its incident sides is irrelevant to sampling probabilities; in the estimates below, nevertheless, endpoints are included in the compact arclength boxes. The error constant need not be uniform under degeneration of the polygon.

## Proof

**1. Zero-area atom.** A line intersects the boundary of a convex polygon in at most two points unless it contains a side. Coinciding samples have probability zero, and a sample at a vertex has probability zero. Three samples are therefore collinear, up to null events, precisely when all are on one side. The mutually exclusive events have probabilities \((\ell_i/P)^3\).

**2. Adjacent-side contribution.** For a fixed assignment of side \(i\) to two sample labels and adjacent side \(j\) to the other, let \(x,y\in[0,\ell_i]\) be coordinates on side \(i\) and \(r\in[0,\ell_j]\) the arclength from the common vertex along side \(j\). If the common angle is \(\alpha\), then

\[
A=\tfrac12 |x-y|r\sin\alpha.
\]

The condition \(A=0\) has arclength-coordinate volume zero in this box. Splitting the following integral at \(\delta=2t/(\ell_j\sin\alpha)\) gives, for \(0<t<\ell_i\ell_j\sin\alpha/2\),

\[
\begin{aligned}
I_{i,j}(t)&=2\int_0^{\ell_i}(\ell_i-u)\min\left\{\ell_j,\frac{2t}{u\sin\alpha}\right\}\,du\\
&=\frac{4\ell_i t}{\sin\alpha}\log\frac{\ell_i\ell_j\sin\alpha}{2t}
+\frac{4t^2}{\ell_j\sin^2\alpha}.
\end{aligned}
\]

There are three choices of singleton sample label. The two choices of which incident side is repeated at each vertex \(i\) give the combined coefficient \(12(\ell_{i-1}+\ell_i)/(P^3\sin\alpha_i)\) at \(t\log(1/t)\).

**3. Other patterns contribute \(O_K(t)\) to the positive tail.** All points on one side have zero area. For two points on one side and a third on a nonneighboring side, the third point has a positive minimum distance from the repeated side's supporting line: the intersection of the polygon with that line is just the repeated side. Area at most \(t\) then requires a repeated-side gap of size \(O_K(t)\), a set of volume \(O_K(t)\).

For three distinct sides, let \(F=\det(X_2-X_1,X_3-X_1)\) on their compact arclength-coordinate box. It is affine in each coordinate separately. At every zero it has a nonzero coordinate partial derivative, as follows.

* If two samples coincide, they coincide at the common vertex \(V\) of their two sides. The third sample \(W\) differs from \(V\) because exactly two sides meet at any vertex. The derivatives in the two coincident samples' coordinates are, up to sign, \(\det(e_1,W-V)\) and \(\det(e_2,W-V)\), where the two incident unit directions \(e_1,e_2\) are linearly independent. They cannot both vanish.
* If the three collinear samples are distinct, the line contains a side of \(K\). Since its intersection with the boundary is just that side, the three distinct samples consist of its endpoints and one point strictly between them. The sample in the relative interior is assigned to that side; each endpoint sample is assigned to the other side incident at its vertex because the three assigned sides are distinct. Moving either endpoint sample along its assigned side differentiates \(F\), up to sign, to the determinant of that side's unit direction with the difference of the other two samples. The latter is a nonzero vector parallel to the supporting line, while the assigned direction is not parallel to it. Thus the derivative is nonzero. The derivatives here are taken using the polynomial extension of \(F\) to the full coordinate space, so this applies at endpoints as well.

Compactness gives a finite cover of the zero set by coordinate boxes in each of which one coordinate partial derivative has absolute value bounded below by a positive constant. In such a box, the section \(|F|\le2t\) at fixed other coordinates has length \(O_K(t)\) in that coordinate, by monotonicity and the derivative bound. The complement of these boxes in the arclength box is bounded away from zero. Fubini gives the desired estimate for each three-distinct-side pattern, including zeros on the boundary of the box.

Combining the finitely many patterns and dividing volumes by \(P^3\) gives the claimed unscaled expansion. Substituting \(t=P^2s\) yields the stated \(C(K)\) and changes only the \(O_K(s)\) term beyond it.

**4. Shape inequality.** Since \(\sin\alpha_i\le1\),

\[
C(K)\ge\frac{12}{P}\sum_i(\ell_{i-1}+\ell_i)=24.
\]

All lengths are positive, so equality forces every interior angle to be a right angle. The angle sum then forces four sides, and a quadrilateral with four right angles is a rectangle. Conversely every rectangle realizes equality.

**5. Marked limit.** Only adjacent-side patterns retain positive conditional mass, by Steps 2 and 3. Their relative coefficients give the stated weights. Fix such a pattern and write \(L=\ell_i\), \(M=\ell_j\), \(S=\sin\alpha\) and \(s=t/P^2<1\). The change from \((x,y,r)\) to \((b,u,z)\), where \(u=|x-y|\), \(b=\min(x,y)\) and \(z=urS/(2t)\), gives volume element \(4t\,db\,du\,dz/(uS)\) accounting for both orders of \(x,y\). Set \(q=\log(u/L)/\log s\) and \(v=b/L\). The volume on the event \(0<A\le t\) is \(4tL\log(1/s)/S\) times Lebesgue measure in \((q,v,z)\) restricted to

\[
q\ge0,\qquad 0\le v\le1-s^q,\qquad
0<z\le\min\left(1,\frac{LMS}{2P^2}s^{q-1}\right).
\]

On \(0<q<1\) the indicator of this set tends almost everywhere to the indicator of the unit cube, and is dominated by that indicator restricted to \(q\in(0,1)\). The mass in \(q>1\) after removing the prefactor is at most \((LMS/(2P^2))\int_1^\infty s^{q-1}\,dq=O(1/\log(1/s))\). Thus the conditional density of the three marks converges in \(L^1\) to the unit-cube density after normalization. Apart from sets of zero measure the same computation holds whichever endpoint was used to measure \(b\). Since there are finitely many patterns and all have the same limiting law of the marks, the marks and pattern are asymptotically independent.

## Verification

The accompanying `check_small_area.py` compares the adjacent-side integral with logarithmic quadrature, checks geometric determinants and the coefficient for several fixed polygons, and simulates square-boundary sampling at one finite threshold. It can be run with `python3 check_small_area.py`. Its success marker is `POLYGON_BOUNDARY_SMALL_AREA_CHECKS_OK`. The bound for all three-distinct-side configurations and the limiting marked law are analytical, not certified by these finite tests.

## Relationship to prior work

*Sharp area-law ordering and shape reconstruction for triangles sampled by boundary arclength* gives the unconditional area distribution for a triangular host. Its mixture formula already gives the atom and a logarithmic lower tail for that host; those specializations are not claimed here. Maesumi's area distribution for one point sampled per side gives the three-distinct-sides component of that mixture.

*Logarithmic dust and angular rigidity for random polygon-boundary cuts* gives an exact corner-product integral, a logarithmic lower tail and a marked law for the smaller piece cut off by a chord through **two** arclength samples. The same local product geometry occurs in Step 2: the gap \(u\) plays the role of one corner distance, but has triangular density and a free lower coordinate, rather than being a uniform endpoint distance. The chord result does not bound the distinct-side configurations for three samples or give the length-weighted triangle coefficient and its rectangular minimizers. The contribution here is the three-sample law with those bounds and shape comparison, and its additional location mark.

Bárány and Steiger study hulls of interior-uniform samples. Bäsel studies invariant random-line chord lengths and interior point distances. Reitzner, Schütt, and Werner study hulls formed by many random points on the boundary of a simple polytope. The cited square-boundary question asks about a fixed positive area threshold. These comparisons delimit the claim; they do not certify historical priority.

## Limitations

These results are for each fixed convex polygon with at least four genuine sides. The marked limit is for the positive-area tail, excluding the atom. The rectangle criterion optimizes the leading continuous coefficient, not the atom or the entire area distribution. No uniform statement for a degenerating family of polygons is asserted.

## References

1. I. Bárány and W. Steiger, *On the variance of random polygons*, Computational Geometry (2013), DOI: https://doi.org/10.1016/j.comgeo.2012.01.003.
2. U. Bäsel, *Random chords and point distances in regular polygons*, Acta Math. Univ. Comenianae 83 (2014), 1–18, https://www.kurims.kyoto-u.ac.jp/EMIS/journals/AC/vol-83-1/14-basel.pdf.
3. M. Reitzner, C. Schütt, and E. M. Werner, *The Convex Hull of Random Points on the Boundary of a Simple Polytope*, Discrete Comput. Geom. 69 (2023), 453–504; https://arxiv.org/abs/1911.05917.
4. *Probability that a triangle inscribed in a square comprises at least one quarter of the square*, Mathematics Stack Exchange, https://math.stackexchange.com/questions/4877892/probability-that-a-triangle-inscribed-in-a-square-comprises-at-least-frac14 (2024).
5. *Sharp area-law ordering and shape reconstruction for triangles sampled by boundary arclength*, October 25, 2026, https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-sharp-area-law-ordering-and-shape-reconstruction-for-triangles-s--b972c9513f97/RESULT.md.
6. M. Maesumi, *Triangle Inscribed-Triangle Picking*, https://arxiv.org/abs/1804.11007.
7. *Logarithmic dust and angular rigidity for random polygon-boundary cuts*, November 17, 2026, https://github.com/Resultary/2026/blob/main/2026/11/17/SCOPE-logarithmic-dust-and-angular-rigidity-for-random-polygon-boundar--a82d823c1b3b/RESULT.md.
