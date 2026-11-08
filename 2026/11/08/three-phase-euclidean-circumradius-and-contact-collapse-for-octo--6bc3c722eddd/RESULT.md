# Three-phase Euclidean circumradius and contact collapse for octopus arbor polytopes

## Finding

For integers \(n\ge3\) and \(1\le k<n\), define the polytope
\[
Q_{n,k}=\left\{x\in\mathbb R_{\ge0}^{n}:\sum_{i=1}^{n}x_i\le n,\quad x_i\le1\ (1\le i\le k)\right\}.
\]
Put \(\ell=n-k\), and let \(r(Q_{n,k})\) be the Euclidean radius of its unique minimum enclosing closed ball. The ball center, radius, and its **complete** set of contact points have exactly three regimes:

* **One uncapped coordinate, \(\ell=1\).** The center is \(c=(\tfrac12\mathbf1_k,n/2)\), and
\[
r(Q_{n,k})^2=\frac{n^2+k}{4}.
\]
  The contacts are all \(2^k\) vertices \((\mathbf1_S,0)\), \(S\subseteq[k]\), together with \(n e_n\): exactly \(2^k+1\) contacts.

* **Two uncapped coordinates, \(\ell=2\).** Define \(D=n^2+2k\), \(a=k/D\), \(b=n(1-a)/2\). The center is \(c=(a\mathbf1_k,b,b)\), and
\[
r(Q_{n,k})^2=\frac{(n^2+k)^2}{2(n^2+2k)}=\frac{(n-1)^2(n+2)^2}{2(n^2+2n-4)}.
\]
  Exactly three points contact: \((\mathbf1_k,0,0)\), \(n e_{k+1}\), and \(n e_{k+2}\).

* **At least three uncapped coordinates, \(\ell\ge3\).** The center is \(c=(0\cdot\mathbf1_k,\frac n\ell\mathbf1_{\ell})\), and
\[
r(Q_{n,k})^2=\frac{n^2(\ell-1)}{\ell}.
\]
  Exactly the \(\ell\) coordinate vertices \(n e_t\), \(k+1\le t\le n\), contact.

In particular, releasing the second capped coordinate in fixed ambient dimension changes the contact count from \(2^{n-1}+1\) to exactly three, while the minimum enclosing radius increases. For \(\ell\ge3\), the extremal ball is already determined solely by the uncapped coordinate-simplex vertices, even though the full polytope contains exponentially many other vertices.

## Assumptions and scope

All norms, distances, and spheres use the **standard Euclidean metric** in \(\mathbb R^n\); no affine change of metric is made. The theorem concerns \(n\ge3\), \(1\le k\le n-1\) and the exact inequality realization above. The class is the octopus special case of the arbor polytopes described by Athanasiadis, Xiao, and Yan (arXiv:2603.11654). Endpoints \(k=0\) and \(k=n\) are not included in the three-regime statement. The enclosing ball contains the entire convex body, not merely its lattice points.

Write \([k]=\{1,\ldots,k\}\), \(W=\{k+1,\ldots,n\}\), and \(\mathbf1_S\) for the indicator of \(S\subseteq[k]\), extended by zero in uncapped coordinates.

## Proof

**1. Vertex classification.** Every vertex is exactly one of
\[
v_S=\mathbf1_S\quad(S\subseteq[k]),\qquad
w_{S,t}=\mathbf1_S+(n-|S|)e_t\quad(S\subseteq[k],\ t\in W).
\]
All displayed points are feasible vertices: the first family has all coordinate bounds active; the second has all capped bounds, all but one uncapped nonnegativity bounds, and the full-sum bound active. Conversely, at a vertex at most one uncapped coordinate is positive, because two positive uncapped coordinates admit a two-sided opposite perturbation. If there is none, the sum inequality is slack since \(k<n\), so every capped coordinate is at a bound. If there is one, then the sum inequality must be active and every capped coordinate must be at a bound, or a feasible nonzero perturbation would remain. Thus the displayed list is exhaustive.

For any candidate center \(c=(a\mathbf1_k,b\mathbf1_{\ell})\), squared distances depend only on \(j=|S|\):
\[
\begin{aligned}
D_{\rm cube}(j)&=k a^2+j(1-2a)+\ell b^2,\\
D_{\rm spike}(j)&=D_{\rm cube}(j)+(n-j)^2-2b(n-j).
\end{aligned}
\]
The spike expression is a strictly convex quadratic function of real \(j\), so for integer \(0\le j\le k\), its maximum lies at \(j=0\) or \(j=k\). Because squared distance is strictly convex, a nonvertex point cannot contact a ball that contains all vertices: any proper convex combination of distinct vertices has strictly smaller squared distance than the corresponding convex combination of vertex squared distances.

**2. One uncapped coordinate.** Put \(a=1/2\), \(b=n/2\). Every cube vertex has squared distance \((k+n^2)/4\). For any spike with \(j\) occupied capped coordinates,
\[
D_{\rm spike}(j)=\frac{k+n^2}{4}-j(n-j).
\]
It equals the proposed squared radius exactly at \(j=0\), since \(1\le j\le k=n-1\) gives \(j(n-j)>0\). These are precisely the stated contacts.

**3. Two uncapped coordinates.** Put \(D=n^2+2k\), \(a=k/D\), \(b=n(1-a)/2\). The all-ones cube vertex \(A=\mathbf1_{[k]}\) and the two points \(B_t=ne_t\), \(t\in W\), have the same squared distance, since
\[
D_{\rm cube}(k)-D_{\rm spike}(0)=k(1-2a)-n^2+2nb=0.
\]
Their common value is \((k+n^2/2)(1-a)^2=(n^2+k)^2/[2(n^2+2k)]\). Since \(0<a<1/2\), no other cube vertex contacts. Since \(a<1/n\) and \(n\ge3\), one has \(b>1\). Hence the opposite spike endpoint satisfies
\[
D_{\rm spike}(k)=D_{\rm cube}(k)+4-4b<D_{\rm cube}(k).
\]
Strict convexity in \(j\) now excludes every spike with \(1\le j\le k\). This yields exactly the three stated contacts.

**4. At least three uncapped coordinates.** Put \(a=0\), \(b=n/\ell\). The points \(B_t=ne_t\), \(t\in W\), all have squared distance \(n^2(\ell-1)/\ell\). A cube vertex with \(j\le k=n-\ell\) ones has squared distance \(j+n^2/\ell\), strictly less because
\[
j\le k=n-\ell<n(\ell-2)\le\frac{n^2(\ell-2)}\ell
\qquad(\ell\ge3).
\]
A spike vertex with \(j\ge1\) occupied capped coordinates has difference from the candidate squared radius
\[
D_{\rm spike}(j)-\frac{n^2(\ell-1)}\ell
=j\left(j+1-2n(1-1/\ell)\right)<0,
\]
since \(j+1\le n-\ell+1\le n-2<2n(1-1/\ell)\). Thus precisely the \(\ell\) points \(B_t\) contact.

**5. Global optimality and uniqueness.** In each regime the proposed center is a convex combination of the exhibited contacts: for \(\ell=1\), it is the midpoint of \(\mathbf1_{[k]}\) and \(ne_n\); for \(\ell=2\),
\[
c=a\mathbf1_{[k]}+\frac{1-a}{2}(ne_{k+1}+ne_{k+2});
\]
and for \(\ell\ge3\), it is the arithmetic mean of \(\{ne_t:t\in W\}\). If these contacts are \(p_i\) with nonnegative weights \(\lambda_i\) totaling one, then for every other candidate center \(z\),
\[
\sum_i\lambda_i\|p_i-z\|_2^2
=\sum_i\lambda_i\|p_i-c\|_2^2+\|z-c\|_2^2
=r(Q_{n,k})^2+\|z-c\|_2^2.
\]
Therefore any ball covering the contact points, hence the polytope, has squared radius at least this quantity. The candidate ball is optimal and its center uniquely determined. This proves all claims.

## Verification

The companion file `verify_arbor_circumball.py` uses exact rational arithmetic. It directly generates all \(12{,}102\) vertices for \(54\) cases \(3\le n\le11\), \(1\le k<n\), evaluates every squared distance, checks the stated contact set, and checks convex-combination optimality certificates. It also checks all orbit-distance inequalities for every \(12\le n\le150\) and \(1\le k<n\). Run with `python verify_arbor_circumball.py`. The observed output is `PASS cases 54 enumerated_vertices 12102 exact_assertions 2307483`. This finite calculation is not a proof of the theorem for arbitrary \(n\); the preceding symbolic argument is.

## Relationship to prior work

Athanasiadis, Xiao, and Yan, *Lattice point enumeration of some arbor polytopes*, arXiv:2603.11654 (first publicly available March 12, 2026), defines exactly \(Q_{n,k}\), proves enumerative positivity and describes its lattice-point structure. This source is the motivation and establishes the objects, not the metric claim. Chapoton, *On posets and polytopes attached to arbors*, arXiv:2503.04247, supplies the broader arbor construction and vertex and combinatorial theory. The minimum enclosing ball is also called a Chebyshev ball or Euclidean one-center; general results for these centers (e.g. Vrahatis, arXiv:2402.06629) do not give this family-specific three-phase radius and complete contact classification.

Targeted searches across the cited manuscripts, bibliographic resources, mathematical finding records, and available preceding geometry claims found no statement implying these formulas. This is a conditional literature assessment, **not** an assertion of globally established novelty; independently checking historical priority remains necessary. Related exact circumball theorems for partial permutohedra, parking-function polytopes, and sparse Cayley sums concern different vertex families and do not imply the distance inequalities proved here.

## Limitations

No claim is made for more general parameters \(\mathcal Q_{n,d,k}\), for arbitrary arbors, or for a nonstandard Euclidean embedding. The theorem does not compute minimum-volume ellipsoids, John ellipsoids, or inballs. The contact count refers to points of the entire polytope on the unique minimum enclosing sphere, not the minimum support size for an optimality certificate. A numerical finite check cannot establish the infinite statement. Independent mathematical audit and global priority verification have not been performed.

## References

1. C. A. Athanasiadis, Q. Xiao, X. Yan, *Lattice point enumeration of some arbor polytopes*, arXiv:2603.11654, March 12, 2026, https://arxiv.org/abs/2603.11654.
2. F. Chapoton, *On posets and polytopes attached to arbors*, arXiv:2503.04247, March 6, 2025, https://arxiv.org/abs/2503.04247.
3. M. N. Vrahatis, *Towards the mathematical foundation of the minimum enclosing ball and related problems*, arXiv:2402.06629, January 2024, https://arxiv.org/abs/2402.06629.
