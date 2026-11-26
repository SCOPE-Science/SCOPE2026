# A gcd-controlled rotational mixed-area law for pairs of regular polygons

## Finding
For integers \(n,m\geq 3\), circumradii \(R,S>0\), and a relative rotation \(\theta\in\mathbb R\), let \(P_n(R)\) be the centered regular \(n\)-gon with vertices at angles \(2\pi j/n\), and define
\[
K_\theta=P_n(R)+\mathcal R_\theta P_m(S).
\]
Here \(+\) is the Minkowski sum and \(\mathcal R_\theta\) is the planar rotation. Set
\[
d=\gcd(n,m),\quad \delta=\frac{\pi d}{nm},\quad
B=\frac{nR^2}{2}\sin\frac{2\pi}{n}+\frac{mS^2}{2}\sin\frac{2\pi}{m},\quad
C=\frac{dRS\sin(\pi/n)\sin(\pi/m)}{\sin\delta}.
\]
Let \(x(\theta)\in[-\delta,\delta)\) be the representative modulo \(2\delta\) of
\(\pi/n-\theta+(n/d-1)\delta\). Then, **for every** \(\theta\),
\[
\boxed{\operatorname{area}(K_\theta)=B+2C\cos x(\theta).}
\]
Consequently the exact minimum and maximum areas are, respectively,
\[
\boxed{B+2C\cos\delta,\qquad B+2C.}
\]
Equality at the maximum holds exactly when \(\theta\equiv \pi/n+(n/d-1)\delta\pmod {2\delta}\); equality at the minimum holds exactly when \(\theta\equiv\pi/n+(n/d)\delta\pmod {2\delta}\). The maximizing sums have exactly \(n+m\) sides; the minimizing sums have exactly \(n+m-d\) sides. All other orientations have exactly \(n+m\) sides.

If \(\Theta\) is uniform modulo \(2\pi\), then \(X=x(\Theta)\) is uniform on \([ -\delta,\delta]\) (endpoint identification is immaterial), so the random area \(Y=\operatorname{area}(K_\Theta)\) has the **complete truncated-arccosine law**
\[
\Pr(Y\le y)=1-\frac1\delta\arccos\left(\frac{y-B}{2C}\right),\qquad
B+2C\cos\delta\le y\le B+2C.
\]
Its mean and variance are
\[
\mathbb E Y=B+\frac{2nmRS}{\pi}\sin\frac\pi n\sin\frac\pi m,
\qquad
\operatorname{Var}(Y)=4C^2\left(\frac12+\frac{\sin(2\delta)}{4\delta}-\left(\frac{\sin\delta}{\delta}\right)^2\right).
\]
The normalized law \((Y-Y_{\min})/(Y_{\max}-Y_{\min})\) depends on the two side counts **only through** \(\delta\). Along any sequence with \(\delta\to0\), it converges in distribution to \(1-U^2\), where \(U\) is uniform on \([0,1]\).

## Assumptions and scope
Only Euclidean plane area is used. The polygons are filled closed convex polygons, their rotation centers coincide, and \(R,S\) are positive. The formula covers all integer pairs, including equal side counts, coprime pairs, and edge-parallel orientations. No optimization over translations is required because translating either Minkowski summand only translates their sum and preserves area.

## Proof
First, the perimeter-normal mixed-area formula states that, for a convex polygon \(P\) with oriented side lengths \(\ell_j\) and exterior unit normals \(u_j\), and any planar convex body \(Q\),
\[
\operatorname{area}(P+Q)=\operatorname{area}(P)+\operatorname{area}(Q)+\sum_j\ell_j h_Q(u_j).
\]
It follows either by the planar mixed-area formula \(2V(P,Q)=\int h_Q\,dS_P\) or by decomposing the mixed-area polynomial. For \(P=P_n(R)\), the \(n\) lengths are \(2R\sin(\pi/n)\), and normal angles are \(\nu_j=(2j+1)\pi/n\). For \(Q=\mathcal R_\theta P_m(S)\), its support value at angle \(\nu\) is \(S\cos r\), where \(r\in[-\pi/m,\pi/m]\) is the difference \(\nu-\theta\) from the nearest vertex direction of \(Q\), reduced modulo \(2\pi/m\). Boundary ties give the same cosine.

Because \(d=\gcd(n,m)\), the multiset of these reduced differences consists of \(d\) copies of a grid of \(N=n/d\) distinct points. The grid step is \(2\delta=2\pi/(mN)\). Its center representative is precisely \(x(\theta)\): after sorting cyclically, its values can be chosen as
\[
r_k=x(\theta)+\left(k-\frac{N-1}{2}\right)2\delta,\qquad k=0,\ldots,N-1.
\]
All \(r_k\) lie in \([-\pi/m,\pi/m]\), including the possible equality at endpoints. The finite cosine sum is exactly
\[
\sum_{j=0}^{n-1}\cos r_j
=d\sum_{k=0}^{N-1}\cos r_k
=d\frac{\sin(N\delta)}{\sin\delta}\cos x(\theta)
=d\frac{\sin(\pi/m)}{\sin\delta}\cos x(\theta).
\]
Multiplying by the common polygon side length \(2R\sin(\pi/n)\) and the radius \(S\) gives the area formula. Since \(C>0\) and \(0<\delta\le\pi/3\), cosine is strictly decreasing in \(|x|\) on \([0,\delta]\). This proves the sharp bounds and precisely the stated equality orientations.

For planar polygons, outward-normal directions of the Minkowski sum are the union of those of its two summands, merging a coincident normal into one edge. An edge of \(P_n(R)\) is parallel to an edge of the rotated \(P_m(S)\) precisely when one reduced difference equals \(\pm\pi/m\). In the displayed evenly spaced grid this occurs exactly at \(|x|=\delta\), then at exactly \(d\) coincident normal directions. At \(x=0\) all reduced differences lie strictly inside the vertex-normal cells. Thus every nonminimizing sum has \(n+m\) sides, while each minimizer has \(n+m-d\).

As \(\theta\) ranges uniformly over a full period, its affine phase modulo \(2\delta\) is uniform, yielding the displayed distribution by \(\Pr(\cos X\le z)=1-\arccos(z)/\delta\) for \(\cos\delta\le z\le 1\). Integrating \(\cos X\) and \(\cos^2X\) over \([-\delta,\delta]\) gives the mean and variance. Substituting \(C\sin\delta/\delta=(nmRS/\pi)\sin(\pi/n)\sin(\pi/m)\) gives the simplified mean. Finally, with \(U=|X|/\delta\) uniform on \([0,1]\), the normalized area equals \((\cos(\delta U)-\cos\delta)/(1-\cos\delta)\), converging pointwise to \(1-U^2\). This proves distributional convergence.

## Verification
The accompanying standard-library Python script `verify_polygon_sum.py` independently constructs the convex hull of every pairwise vertex sum and compares its shoelace area to the closed formula for \(3\le n,m\le18\), two unequal radii, 15 noncritical relative angles per pair, and both extremal orientations. It additionally checks the predicted hull side counts at extrema. The recorded run returned `VERIFY_OK pair_counts= 256 cases= 4352`. The finite tests are supplementary; the proof is the normal-grid identity above.

For example, when \((n,m,R,S)=(3,4,1,1)\), then \(\delta=\pi/12\), \(B=2+3\sqrt3/4\), and \(C=(3+\sqrt3)/2\). Therefore \(\operatorname{area}_{\max}=5+7\sqrt3/4\), the maximizer has seven sides, and the minimizer has six sides.

## Relationship to prior work
Planar mixed-area bilinearity and edge-normal support formulas are classical and are used here as tools, not claimed as new. Karavelas and Tzanaki (2011; 2015) address upper bounds on the face numbers of general Minkowski sums; this addresses a different objective from the exact rotation-dependent area function. Tuzikov, Roerdink and Heijmans (2000) study rotational critical configurations and piecewise concavity for three-dimensional Minkowski addition, but do not give the general two-integer planar area normal form or its exact random-angle distribution in the inspected text. The specific structural synthesis here is the gcd-governed single cosine arch, global equality orientations, degeneracy-linked edge counts, and complete orientation law. The regularity of both summands is essential.

## Limitations
This does not classify arbitrary polygon pairs or Minkowski sums of three or more summands. The two polygon counts are integer parameters and the rotational position is one-dimensional. Claims of publication priority are limited to the inspected accessible works and semantic search results; unavailable or unindexed sources could contain an equivalent formula. Numerical checking cannot establish the infinite-parameter statement independently.

## References
1. M. I. Karavelas and E. Tzanaki, *The maximum number of faces of the Minkowski sum of two convex polytopes*, arXiv:1106.6254v1 (first submitted 2011-06-30), https://arxiv.org/abs/1106.6254.
2. M. I. Karavelas and E. Tzanaki, *A Geometric Approach for the Upper Bound Theorem for Minkowski Sums of Convex Polytopes*, SoCG 2015, DOI 10.4230/LIPIcs.SOCG.2015.81, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SOCG.2015.81.
3. A. V. Tuzikov, J. B. T. M. Roerdink and H. J. A. M. Heijmans, *Similarity measures for convex polyhedra based on Minkowski addition*, Pattern Recognition 33 (2000), 979–995.
