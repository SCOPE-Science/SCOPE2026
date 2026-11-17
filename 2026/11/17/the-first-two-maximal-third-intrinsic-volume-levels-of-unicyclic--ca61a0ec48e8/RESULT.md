# The first two maximal third-intrinsic-volume levels of unicyclic graphical zonotopes

## Finding
For each integer \(n\ge5\), consider all connected simple unicyclic graphs on \(n\) vertices. Under the standard unweighted Euclidean graphical-zonotope construction, the unique maximal third intrinsic volume belongs to the cycle \(C_n\). The unique second-largest value belongs to \(H_n\), the cycle \(C_{n-1}\) with one pendant edge attached to a cycle vertex. The exact values are
\[
V_3(Z_{C_n})=2\sqrt2\left[\binom n3-n(n-3)\right]+\sqrt6\,n(n-4)+2n,
\]
and
\[
V_3(Z_{H_n})=V_3(Z_{C_n})-\delta_n,\qquad
\delta_n=(2\sqrt2-\sqrt6)(n-2)+7\sqrt6-10\sqrt2-4>0.
\]
No other unicyclic graph realizes either level. These are intrinsic volumes in the Steiner normalization, rather than volumes normalized by a unit-diameter requirement.

## Assumptions and scope
Let \(G=(V,E)\) be a finite connected simple undirected graph with \(|V|=|E|=n\ge5\). The equality of edge and vertex counts makes \(G\) unicyclic. Set
\[
Z_G=\sum_{\{i,j\}\in E}[0,e_i-e_j]\subset H=\{x\in\mathbb R^n:\sum_i x_i=0\}.
\]
The choice of orientation of each edge only translates \(Z_G\). All intrinsic volumes refer to the inherited Euclidean metric on \(H\), with \(V_3\) defined by Steiner's formula \(\operatorname{vol}_{n-1}(Z_G+tB_H)=\sum_{k=0}^{n-1}\kappa_{n-1-k}V_k(Z_G)t^{n-1-k}\). In particular, the generating segments are the full root segments (not half-length roots); replacing them by half-length generators rescales \(V_3\) cubically.

Write \(H_n\) for \(C_{n-1}\) with one extra leaf attached at one cycle vertex. Graph uniqueness means up to isomorphism.

## Proof
**Step 1: The third intrinsic volume as an edge-triple statistic.** The intrinsic-volume formula for zonotopes expresses \(V_3(Z_G)\) as the sum of the Euclidean three-parallelotope volumes for all three-edge subsets (Joós--Lángi, Corollary 1). The Gram determinant of a set of graph-incidence vectors equals the product of the sizes of the nontrivial tree components if the chosen edges form a forest, and vanishes otherwise. For three edges the exhaustive possibilities are: three disjoint edges with volume \(2\sqrt2\); a two-edge path disjoint from an edge with volume \(\sqrt6\); a connected three-edge tree (a path on four vertices or a three-star) with volume \(2\); or a triangle, which contributes zero.

Let \(M\) be the number of three-edge matchings, \(D\) the number of subsets consisting of a two-edge path plus an independent edge, \(P\) the number of length-three undirected paths, \(S\) the number of three-stars, and \(T\) the number of triangles. Then
\[
V_3(Z_G)=2\sqrt2\,M+\sqrt6\,D+2(P+S),\qquad
\binom n3=M+D+P+S+T.
\]
Define the wedge count \(W=\sum_{v\in V}\binom{d_v}{2}\), where \(d_v\) denotes vertex degree. Counting pairs of incident edges within three-edge selections in two ways yields
\[
(n-2)W=D+2P+3S+3T.
\]
Eliminating \(M,D\) and putting
\[
a=2\sqrt2-\sqrt6,\quad b=2+4\sqrt2-3\sqrt6,\quad
c=2\sqrt6-2-2\sqrt2,\quad d=3\sqrt6-4\sqrt2,
\]
all of which are positive, gives the exact identity
\[
\boxed{V_3(Z_G)=2\sqrt2\binom n3-a(n-2)W-cP+bS-dT.}\tag{1}
\]
For the cycle \(C_n\), these statistics are \(W=P=n\) and \(S=T=0\). Hence (1) gives its advertised value.

**Step 2: A quantitative branching bound.** Since every vertex has positive degree and \(\sum_v d_v=2n\),
\[
h:=W-n=\sum_v\binom{d_v-1}{2}\ge0.
\]
Equality holds exactly when every vertex has degree two, i.e. precisely for \(C_n\). Moreover,
\[
S=\sum_v\binom{d_v}{3}
=\frac13\sum_v d_v\binom{d_v-1}{2}
\le\frac{n-1}{3}h,
\]
using simplicity, which gives \(d_v\le n-1\). Subtracting (1) from the cycle value gives the exact deficit
\[
\Delta(G):=V_3(Z_{C_n})-V_3(Z_G)
=a(n-2)h+c(P-n)-bS+dT.
\tag{2}
\]
Define \(D_n=a(n-2)-b(n-1)/3\). The identities
\[
D_n=\sqrt6-2+\frac{2(n-4)(\sqrt2-1)}3>0,
\qquad \Delta(G)\ge D_n h-cn
\tag{3}
\]
follow from \(P,T\ge0\) and the star bound. In particular, whenever \(h\ge2\), the lower bound exceeds the candidate second-level gap \(\delta_n=a(n-2)+c-b\), because
\[
2D_n-cn-\delta_n=\frac{n-4}{3}b+8+10\sqrt2-9\sqrt6>0.
\tag{4}
\]
For the final positivity, \(b>0\), and squaring the positive sides shows \(8+10\sqrt2>9\sqrt6\) (equivalently \(160\sqrt2>222\)). Thus no graph with \(h\ge2\) can reach the proposed second level.

**Step 3: The entire one-branching case.** If \(h=1\), the degree multiset has exactly one degree-three vertex, one leaf and every other vertex of degree two. In a connected unicyclic graph this forces a cycle of length \(\ell\ge3\) with a single pendant path of length \(t=n-\ell\ge1\) attached at a cycle vertex. Here \(W=n+1\) and \(S=1\). A length-three path has a unique middle edge, so
\[
P=\sum_{uv\in E}(d_u-1)(d_v-1)-3T.
\]
For \(\ell\ge4\), we have \(T=0\), and \(P=n+1\) if \(t=1\), while \(P=n+2\) if \(t\ge2\). For \(\ell=3\), the permitted \(n\ge5\) forces \(t\ge2\), giving \(T=1\) and \(P=n-1\). Substitution into (2) produces three respective deficits:
\[
\delta_n,\qquad \delta_n+c,\qquad \delta_n+(d-2c).
\]
Here \(c>0\) and \(d-2c=4-\sqrt6>0\). Thus the unique smallest positive deficit is \(\delta_n\), attained only by \(\ell=n-1,t=1\), which is \(H_n\). Since \(D_n>0\), (3)--(4) exclude all graphs with \(h\ge2\). The asserted strict first- and second-level classification follows. The formula \(\delta_n>0\) follows directly from \(a(n-2)+c-b>0\) for \(n\ge5\), with \(a>0\) and the explicit identity \(\delta_n=2(\sqrt6-2)+(n-5)a\), whose terms are positive for \(n\ge5\).

## Verification
Run `python3 artifacts/verify.py` from the package root. The standard-library-only program independently enumerates every labeled connected unicyclic simple graph on \(n=4,5,6,7\) vertices, checks edge-triple configurations and equality cases, and tests 1,300 deterministically generated larger unicyclic graphs. It also verifies Gram determinants of the edge-triple incidence matrices for all enumerated examples through \(n=6\). The recorded successful output was:

`UNICYCLIC_THIRD_INTRINSIC_CHECKS_PASSED exhaustive_graphs=72192 random_graphs=1300`

The infinite theorem is proved by the preceding identities and inequalities, not by the finite enumeration.

## Relationship to prior work
Joós and Lángi provide the general intrinsic-volume formula for arbitrary zonotopes and investigate isoperimetric extrema for zonotopes with prescribed numbers of generators; Brazitikos and McIntyre consider vector-valued Maclaurin inequalities for such wedge-product sums. Those general results justify the starting formula but do not explicitly compare the first two **maximal** third-intrinsic-volume levels across the connected unicyclic graphical family, nor provide the degree-branching rigidity in (2)--(4). The graph restriction and first/second extremal classification are the contribution assessed here.

## Limitations
The result is restricted to simple, connected, unweighted unicyclic graphs and the third intrinsic volume. It does not classify minimal values, unequal segment lengths, or higher intrinsic-volume orders. The historical literature search cannot guarantee the absence of an alternative formulation of the same extremal classification; particularly, the general zonotope inequalities merit continued comparison.

## References
1. A. Joós and Zs. Lángi, *Isoperimetric problems for zonotopes*, arXiv:2206.03204, initially submitted 7 June 2022, particularly Corollary 1 and Sections 3--4. https://arxiv.org/abs/2206.03204
2. S. Brazitikos and F. McIntyre, *Vector-Valued Maclaurin Inequalities*, arXiv:2102.05900, initially submitted 11 February 2021, particularly Section 1 and its intrinsic-volume discussion. https://arxiv.org/abs/2102.05900
