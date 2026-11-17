# Exact directional illumination and optimizer rigidity of simplex difference bodies

## Finding

For each integer \(n\ge3\), let \(H_n=\{x\in\mathbb R^n:\sum_{i=1}^n x_i=0\}\) and let
\[
P_n=\operatorname{conv}\{e_i-e_j:1\le i\ne j\le n\}\subset H_n.
\]
Thus \(P_n\) is the complete-graph symmetric edge polytope, equivalently the difference body \(\Delta-\Delta\) of the standard \((n-1)\)-simplex \(\Delta=\operatorname{conv}\{e_1,\ldots,e_n\}\). Write \(I(P)\) for the least number of directional illuminators of the entire boundary, and \(I^*(P)\) for the infimum total weight of finitely supported nonnegative directional illuminators whose illuminated weight is at least one at every boundary point. Then
\[
I(P_n)=I^*(P_n)=n.
\]
Every individual direction illuminates at most \(n-1\) vertices of \(P_n\); the illuminated directed edges \((i,j)\) either all have one common tail \(i\), or all have one common head \(j\). Equality \(n-1\) is possible precisely when the direction, expressed in \(H_n\), has exactly one negative coordinate and all others positive, or exactly one positive coordinate and all others negative. Its illuminated vertices then constitute the full corresponding tail or head star.

The \(n\) directions \(v^{(i)}=\mathbf 1-ne_i\) illuminate precisely the \(n-1\) vertices \(e_i-e_j\), \(j\ne i\), and partition the vertex set. All optimal ordinary collections of \(n\) directions are (up to positive scaling and permutation) either a full collection of tail-star directions or a full collection of head-star directions. For every optimal finite fractional illumination, the aggregate weights at the tail stars and head stars have the form
\[
\alpha_i=t,\qquad\beta_j=1-t\quad(1\le i,j\le n)
\]
for one \(t\in[0,1]\); conversely such star weights are optimal. The conclusions hold, by affine invariance, for the difference body of every nondegenerate \((n-1)\)-simplex.

## Assumptions and scope

Illumination means that for a boundary point \(x\) and a nonzero direction \(v\in H_n\), the point \(x+\varepsilon v\) lies in the relative interior of the polytope for every sufficiently small positive \(\varepsilon\). For finite fractional illumination, each direction has nonnegative weight and the weight sum of all directions illuminating each boundary point is at least one; coincident directions may be merged. Fractional rigidity concerns aggregate weights of **full-star** directions, not the exact vectors within their open sign cones. We assume \(n\ge3\); the one-dimensional segment case is not included in the rigidity classification.

## Proof

**1. Facets and vertices.** The zero-sum hyperplane is the affine hull of \(P_n\). An exact inequality description is
\[
P_n=\left\{x\in H_n:\sum_{k\in S}x_k\le1\text{ for every }\varnothing\ne S\subsetneq[n]\right\}.
\]
Indeed, for \(x\in H_n\), these inequalities are equivalent to \(\sum_{x_k>0}x_k\le1\), or \(\|x\|_1\le2\). Such an \(x\) is a difference of two probability vectors: writing positive and negative parts \(x=x^+-x^-\), of common mass \(m\le1\), gives \(x=(x^++(1-m)r)-(x^-+(1-m)r)\) for any probability vector \(r\). Hence \(x\in\Delta-\Delta=P_n\). The listed \(e_i-e_j\) are exactly its \(n(n-1)\) vertices, each exposed for example by the functional \(x\mapsto x_i-x_j\). For every nonempty proper \(S\), equality is realized by the face \(\operatorname{conv}\{e_i-e_j:i\in S,j\notin S\}\), whose dimension is \(n-2\), so the displayed inequalities define all facets. At the vertex \(e_i-e_j\), active facets are exactly the subsets \(S\) containing \(i\) and excluding \(j\).

**2. Exact single-vertex illumination criterion.** A direction \(v\in H_n\) illuminates \(e_i-e_j\) if and only if \(\sum_{k\in S}v_k<0\) for every \(S\) containing \(i\) and excluding \(j\). Let \(T(v)=\sum_{v_k>0}v_k=\sum_{v_k<0}(-v_k)\). Taking \(S=\{i\}\) and \(S=[n]\setminus\{j\}\) forces \(v_i<0<v_j\). Conversely, under these signs, the maximum of \(\sum_{k\in S}v_k\) over the active subsets is attained by adjoining every positive coordinate except \(j\) to \(i\), and equals \(v_i+T(v)-v_j\). Thus the exact criterion is
\[
 v_i<0<v_j\quad\text{and}\quad -v_i+v_j>T(v).\tag{1}
\]
Zero coordinates cannot be an illuminated tail or head.

**3. Every illuminated graph is a directed star.** Suppose one direction illuminates roots \((i,j)\) and \((k,\ell)\) with \(i\ne k\) and \(j\ne\ell\). Criterion (1) gives \(-v_i+v_j>T\) and \(-v_k+v_\ell>T\). The distinct negative tails have total absolute value at most \(T\), and the distinct positive heads have total value at most \(T\); adding yields a contradiction. Hence any two illuminated edges share an endpoint in the bipartite graph (tail labels on one side, head labels on the other). Every pairwise-intersecting edge family in a bipartite graph is a star (a single edge being trivial). Therefore at most \(n-1\) vertices are illuminated. Equality means all possible edges of one full star are illuminated: for a tail star at \(i\), criterion (1) forces \(v_i<0\) and \(v_j>0\) for all \(j\ne i\); conversely, then \(T=-v_i\), so (1) holds for all \(j\ne i\). The head-star case is the sign-reversed analogue.

**4. Sharp integral and fractional counts.** The explicit \(v^{(i)}=\mathbf1-ne_i\) have sum zero and illuminate exactly the \(n-1\) roots with tail \(i\). Every face of \(P_n\) contains a vertex; a direction strictly inward on every facet active at that vertex is strictly inward on every facet active at any relative-interior point of the same face. Therefore illuminating all vertices illuminates the whole boundary. These \(n\) directions give \(I(P_n)\le n\) and \(I^*(P_n)\le n\). For any finite family \((v,w_v)\) with nonnegative weights, sum its illumination inequalities over the \(n(n-1)\) vertices: the left side must be at least \(n(n-1)\), while each direction can contribute to at most \(n-1\) vertices, giving
\[
n(n-1)\le\sum_vw_v\#\{\text{vertices illuminated by }v\}\le(n-1)\sum_vw_v.
\]
Hence total weight is at least \(n\), proving \(I^*(P_n)=n\). The same cardinality argument gives \(I(P_n)=n\).

**5. Rigidity.** At the optimal fractional weight \(n\), both inequalities in the preceding display must be equalities. Thus every positive-weight direction illuminates a full star and the illuminated total weight of each vertex is exactly one. Let \(\alpha_i\) and \(\beta_j\) be the sum of weights of full tail and head stars respectively. Then
\[
\alpha_i+\beta_j=1\qquad\text{for all }i\ne j.\tag{2}
\]
For \(n\ge3\), the bipartite incidence graph of these \(n(n-1)\) equations is connected: it is \(K_{n,n}\) with a matching removed. Thus all \(\alpha_i=t\), all \(\beta_j=1-t\), and nonnegativity gives \(0\le t\le1\). Conversely, these weights satisfy every vertex inequality with equality and hence illuminate the boundary fractionally. For an optimal ordinary set of exactly \(n\) directions, every direction is a full star and the stars partition the \(n(n-1)\) vertices without overlap. If a tail star at \(i\) and a head star at \(j\) occur with \(i\ne j\), they both contain root \(e_i-e_j\), impossible. A mixed choice of at least three stars also necessarily has such a cross-index pair; hence all selected stars are of one type. To cover all roots then requires all \(n\) tails or all \(n\) heads. Finally, any affine isomorphism of simplexes induces an invertible affine map of their difference bodies, preserving directional illumination, all equality statements, and fractional weights. \(\square\)

## Verification

The optional standalone `verify.py` independently forms the active subset inequalities at each vertex, checks them with integer arithmetic against (1), and checks the star bound, equality sign patterns, and all explicit tail-star directions for every zero-sum vector with the first \(n-1\) entries in \(\{-2,-1,0,1,2\}\), for \(3\le n\le7\). Running `python verify.py` yields `ROOT_A_EXACT_OK 764040` (764,040 exact pair/direction checks). The symbolic all-dimensional argument in Steps 1–5, not this finite enumeration, proves the theorem.

## Relationship to prior work

The motivating 2026 work of Donzelmann, Holleben, and Juhnke identifies the graph-incidence symmetric edge-polytope framework and studies facets, triangulations, and reflexivity; specializing the complete graph gives \(P_n\). Its facet theorems do not provide the sharp directional illumination number or full-star optimizer classification. Ivanov (2026) proves a broader illumination upper bound for primitive polytopes, without the claimed exact ordinary/fractional number for this root-polytope family. Naszódi (2009) introduces fractional illumination and obtains general bounds for symmetric bodies; those general bounds do not imply the sharp value here. Živaljević (2013) treats the *polar* of the simplex difference body via topological illumination complexes, which are not directional illuminators and do not imply the present claim. Established low-dimensional cases, including the two-dimensional hexagon and three-dimensional cuboctahedron, are not claimed as new. The new mathematical content claimed is the all-dimensional exact directional and fractional count **together with the complete optimizer rigidity** for difference bodies of simplexes. Literature searches cannot establish historical priority conclusively.

## Limitations

The result applies to simplex difference bodies and their affine images, not to all symmetric edge polytopes of arbitrary graphs, coarsened normal-fan polytopes, or the quantitative illumination functional weighted by Minkowski gauge. The proof concerns finitely supported fractional illumination; an extension to arbitrary measures is not needed for the stated fractional invariant. Only self-review has been performed; historical priority and independent validation remain open.

## References

- T. Donzelmann, T. Holleben, M. Juhnke, *Symmetric (co)homology polytopes*, arXiv:2602.17253v1 (first posted 19 February 2026), https://arxiv.org/html/2602.17253v1 .
- I. Ivanov, *Illuminating Primitive Polytopes*, arXiv:2607.08944 (first posted 9 July 2026), https://arxiv.org/abs/2607.08944 .
- M. Naszódi, *Fractional illumination of convex bodies*, Contributions to Discrete Mathematics 4 (2009), doi:10.55016/ojs/cdm.v4i2.62022, https://cdm.ucalgary.ca/article/view/62022 .
- R. T. Živaljević, *Illumination complexes, Δ-zonotopes, and the polyhedral curtain theorem*, arXiv:1307.5138 (2013), https://arxiv.org/abs/1307.5138 .
- A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic Aspects of Symmetric Edge Polytopes*, Mathematika 65 (2019), doi:10.1112/S0025579319000147 .
