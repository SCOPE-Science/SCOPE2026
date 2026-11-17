# Two-angle ridge curvature and a sharp area–count reversal in parity halfcubes

## Finding
For every integer \(n\ge5\), the standard Euclidean parity halfcube
\[
H_n=\operatorname{conv}\left\{v\in\{0,1\}^n:\sum_{i=1}^n v_i\equiv0\pmod2\right\}
\]
has exactly two geometric ridge classes. Their complete metric data are:

| Ridge class | Number | Euclidean \((n-2)\)-measure of each | Exterior normal angle |
|---|---:|---:|---:|
| Coordinate–coordinate | \(2n(n-1)\) | \(1-2^{n-3}/(n-2)!\) | \(\pi/2\) |
| Coordinate–simplex | \(n2^{n-1}\) | \(\sqrt{n-1}/(n-2)!\) | \(\arccos(1/\sqrt n)\) |

There are no simplex–simplex ridges. For the intrinsic-volume convention below, the resulting second Steiner coefficient is
\[
\boxed{V_{n-2}(H_n)=\binom n2\left(1-\frac{2^{n-3}}{(n-2)!}\right)
+\frac{n2^{n-1}\sqrt{n-1}}{2\pi(n-2)!}
\arccos\left(\frac1{\sqrt n}\right).}
\]

A uniform ridge and a Euclidean-measure-weighted ridge have opposite limiting angular behavior. The ratio of total coordinate–simplex to coordinate–coordinate ridge measure is
\[
R_n=\frac{2^{n-2}}{\sqrt{n-1}\big((n-2)!-2^{n-3}\big)}.
\]
It strictly decreases for integers \(n\ge5\), passing from \(R_5=2\) to \(R_6=1/\sqrt5\) and tending to zero. But their ridge *count* ratio equals \(2^{n-2}/(n-1)\), which tends to infinity. Hence the right-angle probability tends to zero under uniform ridge sampling and to one under ridge-volume sampling; the dominant ridge-volume class switches sharply between dimensions five and six.

The unit halfcube also has exact volume and boundary area
\[
\operatorname{Vol}_n(H_n)=1-\frac{2^{n-1}}{n!},\qquad
\operatorname{Area}_{n-1}(\partial H_n)=2n\left(1-\frac{2^{n-2}}{(n-1)!}\right)+\frac{2^{n-1}\sqrt n}{(n-1)!}.
\]
For the exceptional four-dimensional halfcube, the coordinate–coordinate face intersections are only segments (not ridges); its \(32\) coordinate–simplex ridges give \(V_2(H_4)=8\sqrt3/3\).

## Assumptions and scope
The ambient metric is the inherited ordinary Euclidean metric on \(\mathbb R^n\), with cube edge length one. For a full-dimensional convex body \(K\subset\mathbb R^n\) and Euclidean unit ball \(B_n\), define the intrinsic volumes by the Steiner normalization
\[
\operatorname{Vol}_n(K+tB_n)=\sum_{j=0}^n\kappa_{n-j}V_j(K)t^{n-j},\qquad t\ge0,
\]
where \(\kappa_m\) is the unit \(m\)-ball volume. In particular \(V_n\) is ordinary volume, \(2V_{n-1}\) is boundary area, and a ridge of \((n-2)\)-measure \(a\) with exterior dihedral angle \(\theta\) contributes \(a\theta/(2\pi)\) to \(V_{n-2}\). Claims for the complete ridge classification are made for all integers \(n\ge5\), with \(n=4\) treated separately. No claim is made for \(n\le3\).

## Proof
**Facet classification.** For each odd-parity binary vector \(w\), define its Hamming-distance affine functional on the cube
\[
d_w(x)=\sum_{i:w_i=0}x_i+\sum_{i:w_i=1}(1-x_i).
\]
The halfcube equals the intersection of the coordinate bounds \(0\le x_i\le1\) and all inequalities \(d_w(x)\ge1\). This is the classical parity-polytope facet description; it also follows by removing from each odd cube corner the open unit coordinate simplex, without producing new vertices. Thus there are \(2n\) coordinate facets \(C_{i,b}=\{x_i=b\}\cap H_n\) and \(2^{n-1}\) simplex facets \(F_w=\{d_w(x)=1\}\cap H_n\). Each coordinate facet is congruent to \(H_{n-1}\), and each simplex facet consists of the \(n\) even binary neighbors of \(w\), forming a regular \((n-1)\)-simplex of edge length \(\sqrt2\).

**Ridge exhaustion.** Distinct coordinate facets on different coordinate axes meet in a codimension-two face congruent, after possible reflections, to \(H_{n-2}\). For \(n\ge5\), this has full dimension \(n-2\), yielding exactly \(4\binom n2=2n(n-1)\) such ridges. Equal-axis opposite-coordinate facets do not intersect. A simplex facet \(F_w\) meets the coordinate facet \(C_{i,w_i}\) in the regular \((n-2)\)-simplex spanned by all neighbors of \(w\) except the neighbor differing at coordinate \(i\). It meets the opposite coordinate facet only at that one neighbor, hence produces exactly \(n2^{n-1}\) coordinate–simplex ridges. Two distinct odd words have Hamming distance at least two; their sets of one-coordinate even neighbors share at most two points, so their simplex facets intersect in dimension at most one. This is smaller than \(n-2\) for \(n\ge4\). Every ridge lies in two facets, so these cases exhaust all ridges. At \(n=4\), intersections of two coordinate facets are merely one-dimensional halfcubes \(H_2\), and are not ridges.

**Euclidean measures and angles.** The unit halfcube in dimension \(m\ge3\) is obtained from the unit cube by removing \(2^{m-1}\) mutually interior-disjoint orthogonal corner simplices of volume \(1/m!\). Consequently
\[
W_m:=\operatorname{Vol}_m(H_m)=1-\frac{2^{m-1}}{m!}.
\]
An \(m\)-simplex with vertices \(e_1,\ldots,e_{m+1}\), viewed in Euclidean dimension \(m+1\), has Gram determinant \(m+1\), hence \(m\)-volume \(\sqrt{m+1}/m!\). Therefore coordinate–coordinate ridges have measure \(W_{n-2}\), coordinate–simplex ridges have measure \(\sqrt{n-1}/(n-2)!\), coordinate facets have measure \(W_{n-1}\), and simplex facets have measure \(\sqrt n/(n-1)!\). Coordinate outward normals on distinct axes are orthogonal. At \(w=0\), the slanted facet outward normal is proportional to \(-\mathbf1\) and an incident coordinate facet outward normal is \(-e_i\). Their cosine is exactly \(1/\sqrt n\), invariant under coordinate reflections, giving the second angle.

**Steiner calculation.** The exterior angle of a codimension-two normal cone is \(\theta/(2\pi)\). Summing \((n-2)\)-measures times these angles over all ridges gives the displayed \(V_{n-2}\) formula. Summing all facet measures gives the surface-area formula. In dimension four, only \(32\) ridges occur; each has length-area \(\sqrt3/2\) and exterior normal angle \(\arccos(1/2)=\pi/3\), giving \(32(\sqrt3/2)(1/6)=8\sqrt3/3\).

**Sharp finite crossover and asymptotics.** Dividing the two total ridge measures gives \(R_n\). Direct substitution gives \(R_5=2\) and \(R_6=1/\sqrt5\). Setting \(D_n=(n-2)!-2^{n-3}\), one has \(D_{n+1}-2D_n=(n-3)(n-2)!>0\) for \(n\ge5\). Hence
\[
\frac{R_{n+1}}{R_n}=2\sqrt{\frac{n-1}{n}}\frac{D_n}{D_{n+1}}<1.
\]
Factorial growth gives \(R_n\to0\). The coordinate–simplex to coordinate–coordinate *count* ratio equals \(2^{n-2}/(n-1)\to\infty\). The two contrasting sampling limits now follow. No numerical experiment is used to infer the infinite-dimensional assertions.

## Verification
The included standalone Python checker enumerates all even binary vertices and the full supporting-facet list for dimensions \(4,5,6,7\). For every facet, it computes intrinsic Euclidean volume in orthonormal affine coordinates and compares it with the closed formula. For every facet pair, it determines whether the intersection has full ridge dimension, computes the ridge measure by independent Euclidean convex-hull integration, checks the normalized normal dot product, and compares the resulting angle-weighted sum with the closed Steiner coefficient. It also verifies total \(n\)-dimensional volume by convex-hull integration. This is finite cross-checking only; the proof above handles all dimensions. Output ends with `HALFCUBE_STEINER_PASS`.

## Relationship to prior work
Manecke, Sanyal, and So establish the halfcube as a special \(S\)-hypersimplex and give the defining coordinate and simplex facet families; their Theorem 2.7 and Section 3 are inputs to the facet classification. Their main results concern facial structure, pulling triangulations, and monotone path polytopes, not Euclidean ridge measures, exterior dihedral angle spectra, the second Steiner coefficient, or the contrasting area-versus-count sampling limits. General Euclidean Steiner theory supplies the angle-weighted sum rule but not the family-specific ridge classification and exact evaluation. Previous work on uniform-volume covariance of parity halfcubes addresses a different metric statistic and does not imply this ridge-angle law. No claim of globally verified historical priority is made.

## Limitations
The area–count reversal depends on the standard Euclidean \(0/1\) realization and need not survive arbitrary affine transformations. The full two-class ridge formula excludes dimension four, which is handled separately. The opposite sampling limits refer to ridges selected by their intrinsic Euclidean \((n-2)\)-measures, not by exterior-angle-weighted curvature. The checker covers dimensions four through seven only. There may be earlier equivalent formulas in unindexed polytope tables or classical Coxeter-type sources; an independent literature and proof audit remains outstanding.

## References
1. S. Manecke, R. Sanyal, and J. So, *S-hypersimplices, pulling triangulations, and monotone paths*, arXiv:1812.07491 (first public preprint December 18, 2018), especially Theorem 2.7 and Section 3; published *Electronic Journal of Combinatorics* 27(3), P3.16 (2020). https://arxiv.org/pdf/1812.07491
2. R. Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, second expanded edition, Cambridge University Press (2014), standard Steiner formula and polyhedral intrinsic-volume face-angle representation.
3. *Exact isotropic defect and the unique exceptional dimension of parity halfcubes*, public mathematical finding (2026), concerning covariance and isotropic constants rather than ridge curvature: https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-isotropic-defect-and-the-unique-exceptional-dimension-of-p--b9bae71b2cb8
