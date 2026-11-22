# Fixed-radius tree spheres: a three-type obstruction and sharp \(3r+5\) witness size

## Finding

Let \(T\) be a finite nonempty simple undirected tree, let \(r\geq1\) be an integer, and let
\[
S_r(x)=\{y\in V(T):d_T(x,y)=r\},\qquad
\mathcal S_r(T)=\{S_r(x):x\in V(T)\}.
\]
A set \(A\subseteq V(T)\) is *shattered* when \(\{A\cap S_r(x):x\in V(T)\}=2^A\). This is the set of one-point Boolean traces of the exact-distance predicate \(d_T(x,a)=r\).

**Theorem (triple characterization and sharp threshold).** Every \(\mathcal S_r(T)\) has VC dimension at most three. When \(r=1\), it has VC dimension at most two, and the five-vertex path attains two. For every \(r\geq2\), the smallest tree whose exact-radius-\(r\) sphere family has VC dimension three has precisely
\[
3r+5
\]
vertices.

More precisely, for three distinct vertices \(a,b,c\), shattering is equivalent to the following single-median conditions, where \(h,t\) are integers satisfying \(1\leq h<r\) and \(t=r-h\):

1. There is a vertex \(m\) such that \(a,b,c\) occupy three different components of \(T-m\) and \(d_T(m,a)=d_T(m,b)=d_T(m,c)=h\).
2. A fourth component of \(T-m\) contains a vertex at distance \(t\) from \(m\).
3. For each \(s\in\{a,b,c\}\), there are a vertex \(u\) on the path from \(m\) to \(s\), at positive distance \(j=d_T(m,u)\), and a vertex \(w\) reached from \(u\) by a path whose first edge does **not** belong to the path from \(m\) to \(s\), with \(d_T(u,w)=t+j\). An extension past \(s\) is allowed by taking \(u=s\).

For the three singleton conditions, the respective witness paths can be taken inside the three distinct support branches; no shared extra vertices are required.

## Assumptions and scope

All edges have unit length, centers \(x\) must be vertices of the *same* finite tree, and the radius is fixed in advance. A sphere is the equality-distance shell, not the ball \(\{y:d_T(x,y)\leq r\}\), and not a sphere with freely chosen radius. The graph need not be rooted and is not assumed binary. The count \(3r+5\) is a *minimum vertex count across all such trees*, not a formula for the number of shattered triples in a particular tree.

## Proof

**1. Equal-distance center lemma.** Given distinct vertices \(a,b,c\), let \(m\) be their median (the unique common vertex on the three pairwise geodesics), and let the three arm lengths be \(\alpha,\beta,\gamma\). If one arm has length zero, say \(\beta=0\), no vertex is equally distant from all three: the projection of any vertex on the \(a\)-to-\(c\) path that makes its distances to \(a\) and \(c\) equal is the midpoint, where the distance to the interior vertex \(b\) is strictly smaller.

Otherwise suppose some \(x\) has equal distance \(r\) from \(a,b,c\). Project \(x\) onto the three-arm subtree. If the projection is \(m\), then necessarily \(\alpha=\beta=\gamma=h\) and \(r\geq h\). If its projection lies at depth \(j>0\) on the \(a\)-arm, then \(\beta=\gamma=h\) and \(\alpha=h+2j\). Let \(p\) be the midpoint of the \(a\)-to-\(b\) geodesic; here \(p\) is the depth-\(j\) point. We have \(d_T(p,a)=d_T(p,b)=d_T(p,c)=h+j\). Every vertex equidistant from \(a\) and \(b\), at any common integer radius \(r\), projects to \(p\) on the \(a\)-to-\(b\) path. Its distance to \(c\) is therefore also \(r\). Thus no center can include exactly \(a,b\) while omitting \(c\): such a triple cannot be shattered. The analogous argument applies to projections on the other arms.

Therefore any shattered triple has a median \(m\) and three equal, positive arm lengths \(h\). For an equilateral triple, every center equidistant from any two of \(a,b,c\) projects onto the midpoint \(m\) of their connecting path, and is distance \(r-h\) from \(m\) in a component different from the two chosen arms. If \(r=h\), the only such center is \(m\), which includes all three; the two-positive traces are impossible. Hence \(t=r-h\geq1\).

**2. Necessity and sufficiency of the three conditions.** An all-positive center for an equal-arm triple must be in a component other than the three support branches, at distance \(t\) from \(m\): this proves condition 2. The center realizing the positive pair \(\{a,b\}\) must lie at distance \(t\) from \(m\) in the \(c\)-component, and similarly for the other pairs. A center realizing only \(a\) must lie in the \(a\)-component, as centers in either of the other two support components have equal distances to the remaining two support vertices, and an extra component gives equal distances to all three. Project this singleton center onto the path from \(m\) to \(a\) at \(u\), distance \(j>0\) from \(m\). If the projection-to-center length is \(v\), then
\[
d_T(x,a)=h-j+v=h+t \quad\Longleftrightarrow\quad v=t+j.
\]
This is condition 3. It also implies \(d_T(x,b)=d_T(x,c)=h+j+v=r+2j\ne r\).

Conversely, condition 2 supplies an all-positive center. For each omitted vertex \(s\), its condition-3 witness lies at distance \(j+(t+j)=t+2j\ge t\) from \(m\) inside its own component. The vertex at distance exactly \(t\) along that path realizes the other two support vertices and omits \(s\): its path to \(s\) shares a positive initial segment, so its distance to \(s\) is strictly below \(h+t=r\). Condition 3 supplies each singleton trace as calculated above; \(m\) realizes the empty trace because its distance to each support point is \(h<r\). Thus all eight traces occur.

**3. No four-point shattering.** Suppose four distinct vertices \(a,b,c,d\) are shattered. Every triple among them is shattered, hence has the equal-arm median described above. The triples \(a,b,c\) and \(b,c,d\) have the same median \(m\), the midpoint of the \(b\)-to-\(c\) geodesic, and all four vertices lie at the same distance \(h\) from \(m\). If \(a\) and \(d\) lie in the same component of \(T-m\), their three-point median with \(b\) lies strictly inside that component, with distances \(h-u,h-u,h+u\) for some \(u>0\); this violates the equal-arm necessity for the shattered triple \(a,b,d\). Therefore all four vertices occupy different components of \(T-m\).

Any vertex at distance \(r\) from both \(a\) and \(b\) lies in a component of \(T-m\) other than the \(a\)- and \(b\)-components, at distance \(t=r-h\) from \(m\). If it lies in the \(c\)-component, its distance to \(d\) is exactly \(h+t=r\); otherwise, its distance to \(c\) is exactly \(r\). Thus no sphere trace can include precisely \(a,b\) among the four, contradicting shattering. This also excludes every larger shattered set.

**4. Sharp minimum tree order.** Let a triple be shattered with median \(m\), support-arm length \(h\), and \(t=r-h\geq1\). Its three disjoint support paths use \(3h\) vertices besides \(m\). The all-positive witness requires a fourth component with at least \(t\) vertices. For each of the three singleton centers, its branch outside the respective support path has length at least \(t+j\geq t+1\). Those three branch paths are disjoint from the support paths, from the fourth component, and from one another. Consequently
\[
|V(T)|\geq1+3h+t+3(t+1)=3r+t+4\geq3r+5.
\]
For equality, start from a hub \(m\) and attach three disjoint paths of length \(r-1\), with their endpoints serving as \(a,b,c\). At depth one along each path attach an additional path of length two. Finally attach a fourth path of length one at the hub. This tree has exactly \(1+3(r-1)+6+1=3r+5\) vertices, and satisfies the three conditions with \(h=r-1\) and \(t=1\). It therefore shatters \(\{a,b,c\}\). For \(r=1\), the equal-arm lemma precludes triples; the five-vertex path \(P_5\) shatters a pair, for example its vertices in positions two and four (positions numbered one through five).

## Verification

The standalone standard-library script `verify.py` checks the structural triple criterion directly against all eight distance traces on every labeled tree of size two through six, excludes four-shattering on those trees, and compares the two characterizations on 250 seeded random trees of sizes seven through forty-four. It separately checks explicit extremizers for each radius \(2\leq r\leq15\) and the radius-one boundary. Running `python3 verify.py` returned `VERIFY_OK 237075`. No finite computation is being used to infer the universal quantifiers; the preceding tree-geodesic proof establishes them.

## Relationship to prior work

Dreier, Mählmann and Toruńczyk [1] develop a general first-order type-counting theory on monadically dependent graph classes; the present object is the concrete quantifier-free trace of the definable exact-distance predicate on trees, not their general model-checking theorem. Ducoffe, Habib and Viennot [2] study VC dimension for graph *balls* of variable radius, a different family from exact-distance shells of a fixed radius. A previously considered exact-distance-two tree case gives the radius-two minimum eleven; the new result is the all-radius triple criterion and the sharp parameter-dependent minimum. Related finite-ultrametric sphere work concerns ultrametrics, not path metrics of arbitrary unweighted trees.

## Limitations

The result is for finite unweighted trees and vertex centers. It does not assert the same cutoff for weighted real trees, unrestricted radius, balls, graphs with cycles, or independent centers in a larger ambient space. It does not count the number of shattered triples in every individual tree. Historical priority under alternative terms such as *distance-shell range spaces* or *equilateral tripod traces* remains unverified independently.

## References

[1] J. Dreier, N. Mählmann and S. Toruńczyk, *First-Order Model Checking on Monadically Dependent Graph Classes*, arXiv:2611.08143v1, first posted November 5, 2026, https://arxiv.org/abs/2611.08143. Relevant full text: Sections 1.1, 3 and 10.

[2] G. Ducoffe, M. Habib and L. Viennot, *Diameter, Eccentricities and Distance Oracle Computations on H-Minor Free Graphs and Graphs of Bounded (Distance) Vapnik–Chervonenkis Dimension*, SIAM Journal on Computing, DOI:10.1137/20M136551X, https://epubs.siam.org/doi/10.1137/20M136551X. The range system is based on balls with all radii.

[3] A. de Lima, M. da Silva and A. Vignatti, *A Range Space with Constant VC Dimension for All-pairs Shortest Paths in Graphs*, Journal of Graph Algorithms and Applications 27 (2023), 603–619, DOI:10.7155/jgaa.00636, https://www.jgaa.info/index.php/jgaa/article/view/paper636. Its concepts are sets defined by path occurrence, not exact-distance vertex shells.
