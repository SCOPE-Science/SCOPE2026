# A sharp fifteen-vertex thickness transition for complete-graph associahedra

## Finding

For integers \(n\ge3\) and \(2\le k\le n\), let \(\Delta_I=\operatorname{conv}\{e_i:i\in I\}\subset\mathbb R^n\), and consider the complete-graph truncated nestohedron
\[
Q_{n,k}=\sum_{\substack{\varnothing\ne I\subseteq[n]\\|I|\le k}}\Delta_I.
\]
All widths below are ambient Euclidean widths in the affine span \(\sum_i x_i=\sum_{j=1}^k \binom nj\). For \(1\le s\le n-1\), define
\[
C_{n,k}(s)=\sum_{j=2}^{k}\left[\binom nj-\binom sj-\binom{n-s}j\right],\qquad
\nu_S=\frac{\mathbf1_S-(|S|/n)\mathbf1}{\sqrt{|S|(n-|S|)/n}}.
\]
Then the exact minimum Euclidean width is
\[
\boxed{\operatorname{width}_{\min}(Q_{n,k})=
\min_{1\le s\le\lfloor n/2\rfloor}
\sqrt{\frac n{s(n-s)}}\,C_{n,k}(s).}
\]
Every minimizing unit direction is exactly a cut direction \(\nu_S\), or its negative, whose cardinality attains this finite minimum. Thus this expression also determines **all** narrowest orientations of every intermediate member of the complete-graph interpolation.

At the complete graph-associahedron stage \(k=n\), the cardinality minimum has a sharp dimension-only solution. Let \(m=\lfloor n/2\rfloor\). Then
\[
\boxed{\operatorname{width}_{\min}(Q_{n,n})=
\begin{cases}
\sqrt{\dfrac n{n-1}}(2^{n-1}-1),&3\le n\le14,\\[2mm]
\sqrt{\dfrac n{m(n-m)}}(2^m-1)(2^{n-m}-1),&n\ge15.
\end{cases}}
\]
For \(3\le n\le14\), the narrowest unit directions are exactly the \(2n\) oriented singleton-cut directions. For every \(n\ge15\), they are exactly the balanced-cut directions: \(|S|\in\{m,n-m\}\). In particular, the number of unoriented narrowest axes is \(n\) below the transition, \(\binom n{n/2}/2\) when \(n\ge16\) is even, and \(\binom n{(n-1)/2}\) when \(n\ge15\) is odd. There is no tie at the transition.

The limiting minimum width satisfies \(\operatorname{width}_{\min}(Q_{n,n})\sim 2^{n+1}/\sqrt n\).

## Assumptions and scope

The normalizations use one unscaled standard coordinate simplex per nonempty eligible set, including the singleton summands (which only translate the polytope). The primary geometric object has affine dimension \(n-1\), and all Euclidean lengths use the metric induced from \(\mathbb R^n\). The complete graph on \([n]\) has every nonempty set connected, so \(Q_{n,k}\) is the \((k-1)\)-graph polytope of Pešović–Stojadinović. No claim is made about other realizations, arbitrary graph families, or a closed-form minimizing cardinality for every \(k<n\).

## Proof

**Step 1: the permutation-coordinate realization.** Sort a generic supporting direction strictly increasingly. The maximizer on each \(\Delta_I\) is the basis vector corresponding to the largest-ranked element in \(I\). Therefore the resulting vertex has, at rank \(i\), coordinate
\[
a_i(k)=\sum_{j=1}^k\binom{i-1}{j-1}\qquad(1\le i\le n),
\]
with out-of-range binomial coefficients zero. Since \(a_{i+1}(k)>a_i(k)\) for \(k\ge2\), the polytope is the full permutation-orbit hull of this strictly increasing vector. Its difference body \(D_{n,k}=Q_{n,k}-Q_{n,k}\) is the centered permutohedron with strictly increasing orbit vector
\[
d_i(k)=a_i(k)-a_{n+1-i}(k).
\]
Indeed, \(Q_{n,k}\) and \(-Q_{n,k}\) have the same braid normal fan, and their ordered maximizing coordinates add. The difference body is centrally symmetric, full-dimensional in \(\mathbf1^\perp\), and its facets are exactly the proper nonempty subset-sum facets.

**Step 2: cut-distance reduction and all equality cases.** For a subset \(S\) of size \(s\), the two-level normal \(\mathbf1_S-(s/n)\mathbf1\) produces width one from exactly those simplex summands \(\Delta_I\) meeting both \(S\) and \(S^c\); the other summands produce zero width. The number of these crossing sets is exactly \(C_{n,k}(s)\). Hence
\[
h_{D_{n,k}}(\nu_S)=\sqrt{\frac n{s(n-s)}}\,C_{n,k}(s).
\]
For a convex polytope containing the origin in its relative interior, the minimum of its support function over intrinsic unit directions equals the radius of its origin-centered largest ball, which equals the minimum distance to its facet hyperplanes. The subset facets of \(D_{n,k}\) therefore give the displayed finite minimum. At a minimizing direction the inscribed ball must touch a tangent facet; conversely, a tangent facet's unit normal is minimizing. A ball cannot touch a proper lower-dimensional intersection of distinct tangent facets because the sphere has a unique supporting tangent hyperplane there. Consequently there are no additional non-cut minimizing directions.

**Step 3: the full-stage scalar formula.** Summing over all cardinalities gives
\[
C_{n,n}(s)=(2^s-1)(2^{n-s}-1).
\]
By the symmetry in \(s,n-s\), it remains to minimize
\[
f_n(s)=\frac{(2^s-1)(2^{n-s}-1)}{\sqrt{s(n-s)}}
\quad (1\le s\le\lfloor n/2\rfloor).
\]
For integers \(3\le n\le14\), direct **exact integer** comparison shows \(f_n(s)>f_n(1)\) for every \(2\le s\le\lfloor n/2\rfloor\). Specifically, for each such pair, the checked positive integer is
\[
[(2^s-1)(2^{n-s}-1)]^2(n-1)
-(2^{n-1}-1)^2s(n-s).
\]
There are 36 inequalities, and their complete finite enumeration is in `verify_width.py`. This is a complete finite base, not an extrapolation from samples.

For the infinite tail \(n\ge15\), write \(L=\log2\) and
\[
h(t)=\frac{L}{1-2^{-t}}-\frac1{2t}.
\]
A derivative calculation gives
\[
\frac{d}{ds}\log f_n(s)=h(s)-h(n-s),\qquad
h'(t)=\frac1{2t^2}-\frac{L^2}{4\sinh^2(Lt/2)}.
\]
For \(t\ge5\), letting \(y=Lt/2\), the elementary estimates \(L>2/3\) and
\(\sinh(y)/y\ge1+y^2/6\ge79/54>\sqrt2\) show \(h'(t)>0\). Thus \(f_n(s)\) is strictly decreasing on the real interval \([5,n/2]\). The small candidate \(s=4\) is also dominated by \(s=5\), because for \(n\ge15\)
\[
\frac{f_n(4)}{f_n(5)}
=\frac{15}{31}\frac{2^{n-4}-1}{2^{n-5}-1}
\sqrt{\frac{5(n-5)}{4(n-4)}}
>\frac{150}{31\sqrt{22}}>1.
\]
Also \(f_n(2)>f_n(1)\) and \(f_n(3)>f_n(1)\): the respective unnormalized numerator ratios are bounded below by \(45/31>\sqrt2\) (valid already for \(n\ge6\)) and \(1785/1023>\sqrt3\) (valid for \(n\ge11\)), whereas the normalized denominator ratios are strictly smaller than \(\sqrt2\) and \(\sqrt3\). Therefore **only** \(s=1\) and \(s=m\) can minimize for \(n\ge15\).

At \(n=15\), the exact squared comparison for \(s=7\) against \(s=1\), with positive common denominators removed, is \(-347515434<0\). For even \(n\ge16\), one has the strict upper bound
\[
\frac{f_n(n/2)}{f_n(1)}
<\frac{4\sqrt{n-1}}{n(1-2^{-(n-1)})}<1.
\]
The last inequality holds at \(n=16\), and its right-hand bound decreases thereafter. For odd \(n\ge17\), similarly
\[
\frac{f_n((n-1)/2)}{f_n(1)}
<\frac4{\sqrt{n+1}(1-2^{-(n-1)})}<1.
\]
Again the displayed upper bound is less than one already at \(n=17\) and decreases. Hence the balanced cardinality is the unique minimizing cardinality up to complementation in every dimension \(n\ge15\). Combining with Step 2 gives the complete direction classification. Taking \(n\to\infty\) in the exact expression proves the asymptotic.

## Verification

Run `python3 verify_width.py` using only the Python standard library. It checks all 36 integer comparisons needed for the finite base, the sharp comparison at \(n=15\), the complete cardinality classification through \(n=120\), 139 independent cut-support identities across truncated stages, and 14 direct Minkowski-summand vertex constructions. The infinite-dimensional tail is justified by the preceding derivative and inequality proof, not by the finite checks. The script does not call external services.

## Relationship to prior work

Pešović and Stojadinović (2022, Definition 2.1) introduce graph-polytopal interpolants \(Q_{\Gamma,m}\), including the complete-graph instance considered here, and study combinatorial and quasisymmetric invariants. Postnikov (2005, Sections 2 and 6–8) gives the orbit and simplex-sum frameworks for permutohedra and nestohedra. The current minimum-width reduction uses these established descriptions but establishes the precise metric cut formula and the strict change of all optimal widths at \(n=15\) by a separate inequality argument.

A related public mathematical research record on **complete-bipartite** graph associahedra reports a dimension-fifteen change from singleton to balanced cuts. Its graph contains no edges within either color class and is not the complete graph \(K_n\); consequently neither its particular cut counts nor its theorem directly imply the complete-graph formulas here. Nevertheless, the equal numerical threshold is a substantive priority risk and merits human comparison against the full related record.

## Limitations

This theorem does not characterize which cardinality minimizes the intermediate formula for every \(k<n\), and it does not classify metric behavior for general graphs or rescaled simplex summands. Historical priority is provisional: mathematical-record searches cannot rule out unindexed equivalent results.

## References

1. M. Pešović and T. Stojadinović, *Between graphical zonotope and graph-associahedron*, arXiv:2209.12053v1, first posted September 24, 2022, https://arxiv.org/abs/2209.12053.
2. A. Postnikov, *Permutohedra, associahedra, and beyond*, arXiv:math/0507163v1, first posted July 7, 2005, https://arxiv.org/abs/math/0507163.
3. A. Postnikov, V. Reiner and L. Williams, *Faces of generalized permutohedra*, arXiv:math/0609184, https://arxiv.org/abs/math/0609184.
