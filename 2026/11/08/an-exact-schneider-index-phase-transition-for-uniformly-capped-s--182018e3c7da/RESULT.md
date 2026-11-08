# An exact Schneider-index phase transition for uniformly capped simplices

## Finding

For each integer \(d\ge3\) and each real \(1/2\le t\le1\), define
\[
P_{d,t}=\left\{x\in\mathbb R^{d+1}: \sum_{i=1}^{d+1}x_i=1,\quad0\le x_i\le t\text{ for all }i\right\},
\qquad V_{d,t}=\operatorname{vert}(P_{d,t}).
\]
For any finite set \(V\) with convex hull \(P\), the Schneider nonconvexity index is
\[
c(V):=\inf\{\lambda\ge0:V+\lambda P\text{ is convex}\}.
\]
The precise formula, including attainment, is
\[
\boxed{c(V_{d,t})=\max\{d-1,(d+1)t-1\}}.
\]
Equivalently, the largest coefficient \(\alpha\) for which \(P_{d,t}=\alpha V_{d,t}+(1-\alpha)P_{d,t}\) is
\(\alpha=1/(1+c(V_{d,t}))\).
The index has a plateau of height \(d-1\) for \(1/2\le t\le d/(d+1)\), followed by a strictly increasing linear regime to the simplex endpoint \(t=1\).

## Assumptions and scope

The statement concerns the intrinsic \(d\)-dimensional geometry of the affine hyperplane \(\sum_i x_i=1\). For \(t<1\), the vertices are exactly the distinct coordinate permutations of \((t,1-t,0,\ldots,0)\). This includes the degeneracy \(t=1/2\), where permutations with the two equal nonzero coordinates are identified. For \(t=1\), the body is the standard \(d\)-simplex. No restriction on rationality of \(t\) is imposed.

## Proof

Write \(P=P_{d,t}\), \(V=V_{d,t}\), \(n=d+1\), and \(U_\lambda=V+\lambda P\). Since \(\operatorname{conv}V=P\), one has \(\operatorname{conv} U_\lambda=(1+\lambda)P\). We prove equality precisely when \(\lambda\ge L:=\max\{d-1,nt-1\}\).

**A simplex-facet obstruction.** Suppose first \(t<1\). For any index \(i\), the cap facet \(F_i=P\cap\{x_i=t\}\) is the simplex of dimension \(d-1\) with the other \(d\) nonnegative coordinates summing to \(1-t\). An exposed-face argument shows
\[
U_\lambda\cap (1+\lambda)F_i
=V(F_i)+\lambda F_i.
\]
At the facet centroid, each of its \(d\) barycentric coordinates is \(1/d\), so membership in any single vertex translate requires \(\lambda\ge d-1\). Thus convexity of \(U_\lambda\) requires \(\lambda\ge d-1\).

**A central-point obstruction.** The uniform point \(b=(1/n,\ldots,1/n)\) belongs to \(P\), so \((1+\lambda)b\) must belong to \(U_\lambda\) if the latter is convex. Each \(v\in V\) has one coordinate equal to \(t\). Nonnegativity of the corresponding coordinate of \(((1+\lambda)b-v)/\lambda\) forces \(1+\lambda\ge nt\). Therefore \(\lambda\ge nt-1\).

**Facet coverage at \(\lambda\ge L\).** Any facet of \(P\) is defined by either \(x_i=t\) or \(x_i=0\). Each cap facet is a \((d-1)\)-simplex. Every face \(F\) of affine dimension \(r\) satisfies \(V(F)+rF=(r+1)F\): indeed any point of \(F\) is a convex combination of at most \(r+1\) vertices, one with coefficient at least \(1/(r+1)\). Hence for all facets \(F\), their index is at most \(d-1\), and for \(\lambda\ge d-1\),
\[
(1+\lambda)F=V(F)+\lambda F\subseteq U_\lambda.
\]
Consequently \(\partial((1+\lambda)P)\subseteq U_\lambda\).

**A common star center.** Put \(z=(1+\lambda)b\). For any vertex \(v\) of the stated form, the coordinates of \(y=(z-v)/\lambda\) are one of each of
\[
y_t=\frac{1+\lambda-nt}{n\lambda},
\qquad y_{1-t}=\frac{\lambda-d+nt}{n\lambda},
\]
and \(d-1\) copies of
\[
y_0=\frac{1+\lambda}{n\lambda}.
\]
Their sum is one. Under \(\lambda\ge L\), \(y_t\ge0\) and \(y_{1-t}\ge0\). Because \(1/2\le t\), one has \(y_t\le y_{1-t}\le y_0\); moreover
\[
y_0\le\frac{d}{(d-1)(d+1)}\le\frac12\le t\qquad(d\ge3).
\]
Thus \(y\in P\), i.e. \(z\in v+\lambda P\) for **every** \(v\in V\). The union \(U_\lambda\) is therefore star-shaped about \(z\). For each point \(x\in(1+\lambda)P\), the ray from \(z\) through \(x\) meets the boundary at \(w\), which belongs to some convex translate \(v+\lambda P\). That same translate contains \(z\), hence the segment \([z,w]\) and \(x\). Therefore \(U_\lambda=(1+\lambda)P\).

At \(t=1\), \(P\) is a \(d\)-simplex, whose vertex-set index is exactly \(d\) by the barycentric-centroid lower bound and Carathéodory upper bound. This agrees with the formula and completes the proof.

## Verification

The standalone exact-rational enumeration script `verify_capped_simplex.py` confirms the proposed boundary-cover construction, common-center coordinates, and strict lower-bound witnesses for \(3\le d\le7\), for rational parameters including the degenerate cap and phase transition. It reports `CAPPED_SIMPLEX_EXACT_OK 19385`. All-dimensional correctness follows from the proof; the finite tests are supplementary and do not certify historical novelty.

## Relationship to prior work

Meyer [1] investigates the general convexification threshold for arbitrary compact-plus-convex Minkowski sums and connects it to exposed-face covering. Artstein-Avidan, Falah, and Slomka [2] develop the vertex-generated parameter and facial restrictions. Those general tools motivate the question, but neither of the inspected texts states this capped-simplex closed form or its switch at \(t=d/(d+1)\). The endpoint \(t=1/2\) is a scaled second hypersimplex, whose index can be treated separately by a hypersimplex formula; the continuum and transition are the present assertion.

## Limitations

The formula assumes the symmetric cap \(x_i\le t\) on every coordinate, \(d\ge3\), and \(1/2\le t\le1\). It does not provide values for unequal cap heights, lower \(t\) (where a different vertex structure occurs), or arbitrary truncations of simplices. Priority relative to all historical literature cannot be certified by available searches.

## References

[1] M. Meyer, *Finite convexification by Minkowski summation*, arXiv:2610.26744, first posted 2026-10-19. https://arxiv.org/abs/2610.26744

[2] S. Artstein-Avidan, T. Falah, B. A. Slomka, *Vertex generated polytopes*, arXiv:2407.20604, first posted 2024-07-30. https://arxiv.org/abs/2407.20604
