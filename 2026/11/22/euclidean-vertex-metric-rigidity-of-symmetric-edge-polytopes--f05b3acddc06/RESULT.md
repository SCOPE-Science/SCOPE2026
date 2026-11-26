# Euclidean vertex-metric rigidity of symmetric edge polytopes

## Finding

**Theorem (distance-table decoder and stability).** Let \(G\) be a finite simple undirected graph with at least one edge, and write \(G^+\) for the graph obtained by deleting its isolated vertices. In standard orthonormal vertex coordinates set
\[
P_G=\operatorname{conv}\{\pm(e_u-e_v):\{u,v\}\in E(G)\}\subseteq\mathbb R^{V(G)}.
\]
There is an exact coordinate-free inverse algorithm from the squared-distance table on the polytope vertices. Distance squared \(8\) identifies the unique antipode of each vertex. Collapse these opposite pairs into graph-edge candidates. For two different pairs the set of squared cross-distances is \(\{2,6\}\) when the original graph edges meet and \(\{4\}\) when they are disjoint. This recovers the original line graph. Whitney's only nonunique connected line-graph inversion, the triangle versus the three-leaf star, is resolved by the rank of the centered Gram matrix \(-JDJ/2\), where \(D\) is the corresponding six-point squared-distance submatrix and \(J=I-\mathbf1\mathbf1^{\mathsf T}/6\). These Gram ranks are respectively \(2\) and \(3\); the ranks of the raw squared-distance submatrices are \(3\) and \(4\). Finally invert each line-graph component and take their disjoint union.

**Uniform stability corollary.** Suppose every off-diagonal squared distance in the unlabeled table is given with absolute error strictly less than \(1\), and that table entries consistently index the same points. Rounding each entry to its nearest even integer gives the exact table; the same graph is then recovered. No ambient coordinates or point labels are needed.

**Congruence consequence.** The following are equivalent for two graphs \(G,H\) in scope: \(G^+\cong H^+\); their full Euclidean vertex metrics are isometric; and \(P_G,P_H\) are congruent in their affine hulls. The connected-case congruence classification was established by Cuchilla et al. [6, Theorem 3.8]; the result here is the distance-table decoder, including its triangle–claw step and recovery guarantee, rather than a new connected-case classification.

## Assumptions and scope

All graphs are finite and simple, with no loops or multiple edges, and have at least one edge. The Euclidean metric is the unweighted standard inner product on the indicated vertex-coordinate space. Graphs may be disconnected. Isolated graph vertices are invisible to this intrinsic point metric and are explicitly deleted in the conclusion; if their number is independently supplied it may of course be restored. Congruence is intrinsic, not equality of ambient coordinate dimensions. In particular, **unimodular** or affine equivalence is not being mistaken for Euclidean congruence.

The finite metric space includes **all** extreme points of \(P_G\), not merely some subset and not the one-skeleton's shortest-path metric. Its cardinality is exactly twice the edge count. Input squared-distance errors in the stability statement are absolute, entrywise and deterministic, not a claim of recovery with missing points or unknown pair correspondences.

## Proof

**All indicated roots are vertices.** Each root \(r=e_u-e_v\) has squared norm \(2\), and all these signed roots are distinct for a simple graph. The functional \(x\mapsto\langle r,x\rangle\) attains its unique maximum over the finite root set at \(r\) by Cauchy--Schwarz and strict inequality for different roots of equal norm. Thus each is an extreme vertex of their convex hull; no additional vertices exist.

**Identify opposite pairs metrically.** For signed roots \(r,s\),
\[
\|r-s\|^2=4-2\langle r,s\rangle.
\]
For \(s=-r\) this is \(8\). Two nonopposite roots have inner product \(-1\), \(0\), or \(1\), except for identical points, and their squared distance is respectively \(6\), \(4\), or \(2\). Hence the unique squared-distance-\(8\) partner of every vertex is its negative. This pairing is preserved by every isometry of finite vertex metrics.

**Recover graph-edge incidence.** Write \(R_e=\{r_e,-r_e\}\) for the opposite pair corresponding to the undirected edge \(e\). For distinct graph edges \(e,f\), the chosen root vectors satisfy \(|\langle r_e,r_f\rangle|=1\) precisely when \(e,f\) have a common endpoint, and the inner product is zero precisely when they are vertex-disjoint. Consequently,
\[
\{\|x-y\|^2:x\in R_e,\ y\in R_f\}
=\begin{cases}
\{2,6\},&e\cap f\ne\varnothing,\\
\{4\},&e\cap f=\varnothing.
\end{cases}
\]
The metric therefore defines the line graph \(L(G^+)\): one vertex per opposite pair, with an edge exactly for the cross-distance class \(\{2,6\}\). The connected components of this line graph correspond exactly to the nontrivial connected components of \(G^+\).

**Resolve the sole line-graph ambiguity.** Whitney's line-graph isomorphism theorem [5] states that every connected finite simple graph is determined by its line graph, apart from the two distinct graphs \(K_3\) and \(K_{1,3}\), both with line graph \(K_3\). The intrinsic Euclidean affine rank of the six roots belonging to one such line-graph component is determined by its squared-distance submatrix: for \(N\) points and their squared-distance matrix \(D\), the centered Gram matrix \(-JDJ/2\) has exactly the affine rank of the points, where \(J=I-\mathbf1\mathbf1^{\mathsf T}/N\). Since the six points are antipodally paired, their centroid is zero. The incidence-root span of a connected component with \(v\) vertices has dimension \(v-1\): its orthogonal complement in the component coordinates consists of vectors constant on the component, since orthogonality to \(e_u-e_v\) forces equality of the coordinates at each edge. The Gram rank is therefore \(2\) for \(K_3\) and \(3\) for \(K_{1,3}\). For the raw distance matrix, \(D=4\mathbf1\mathbf1^{\mathsf T}-2G\) with \(G=-JDJ/2\) and \(G\mathbf1=0\), so the raw rank is one greater. This distinguishes the sole exception without coordinates. Line-graph inversion component by component thus reconstructs \(G^+\) uniquely.

**Equivalence of graph and polytope claims.** An isometry of the finite vertex metrics gives the same reconstruction, so it forces \(G^+\cong H^+\). Conversely, a graph isomorphism between \(G^+\) and \(H^+\) induces a permutation of their standard coordinate axes, taking each signed root of one graph to the corresponding signed root of the other and thereby giving an intrinsic Euclidean congruence of the polytopes. Congruence automatically gives a bijective vertex isometry. Also, a finite distance-preserving bijection extends to an affine isometry of the point configurations by equality of their centered Gram matrices, even without knowing the graph coordinates.

**Noise margin.** Every off-diagonal squared distance belongs to \(\{2,4,6,8\}\). If its recorded value differs from truth by less than \(1\), that exact even integer is the unique nearest even integer; there are no ties. The preceding reconstruction therefore applies verbatim after rounding. This proves the claimed stability without any probabilistic or large-dimension hypothesis.

## Verification

The included standalone standard-library script `sep_metric_reconstruction_check.py` constructs signed incidence roots, calculates squared distances using integer coordinates, recovers every opposite pair and every line-graph adjacency, and compares the latter with direct graph-edge incidence. It exhausts all labeled simple graphs with \(2\le n\le5\), samples \(601\) deterministic graph masks with \(n=6\), checks the triangle/claw rank distinction using exact integer elimination, and confirms representative perturbations strictly inside the stated tolerance. It completes with `SEP_METRIC_RECONSTRUCTION_EXACT_PASS`; the test count is `1694` nonempty graph instances.

A separate full graph-atlas check (allowing disconnected components) covered \(1245\) nonempty no-isolate graphs up to seven vertices and recovered their line graphs exactly. These finite checks support the implementation and boundary cases only. The proof above is valid for **all** finite simple graphs in scope and does not infer infinite correctness from enumeration.

## Relationship to prior work

Cuchilla, Hound, Plepel, Vindas-Meléndez and Ye [6, Theorem 3.8] establish the equivalence between graph isomorphism and unitary equivalence of canonical symmetric edge polytopes for connected graphs. For such polytopes, an intrinsic congruence takes center to center and extends to an orthogonal map of the vertex-coordinate spaces, whose dimensions agree because the intrinsic dimension is one less than the number of graph vertices. Thus their classification also covers the connected vertex-metric uniqueness consequence. In fact, one can apply that theorem componentwise once the edge sets of the connected components are recovered from the metric: among the antipodal pairs, distinct edges have nonzero mutual inner-product magnitude precisely when incident. The new content isolated here is a direct distance-table inverse using line-graph inversion and a six-point rank test, with a deterministic recovery guarantee for rounded input; it does not require constructing an ambient lattice or realizing the distances as coordinates.

D'Alì, Juhnke-Kubitzke and Koch [1, Theorem 4.6] prove that symmetric edge polytopes are **unimodularly** equivalent exactly for isomorphic graphic matroids; their Corollary 4.7 gives a graph-isomorphism consequence under three-connectivity. Their explicit nonisomorphic, two-connected Whitney-twist pair shows why matroid equivalence is strictly weaker than graph isomorphism. For instance, the four-vertex path and three-leaf star yield unimodularly equivalent crosspolytopes but distinct line graphs and hence different Euclidean vertex metrics.

D'Alì, Delucchi and Michałek [2] establish polytope/graph constructions and various enumerative equivalences. Winter [3] studies reconstruction of a *given* polytope from its polytope edge graph and auxiliary metric data; that data and its conclusion differ from recovering the original input graph from the full metric of signed incidence roots. Rembado [4] studies root **subsystems** and colored graph encodings; arbitrary edge-selected symmetric type-A root sets need not be root subsystems. The classical Whitney line-graph theorem [5] is used directly rather than claimed as new.

## Limitations

The claim is restricted to the canonical unweighted Euclidean realization. It makes no assertion that the combinatorial face lattice, unimodular equivalence, an arbitrary linear realization, an unlabeled *histogram* of distances (rather than the full distance matrix), or incomplete distance measurements recover the graph. Isolated vertices cannot be detected in the intrinsic metric. The noisy-data assertion assumes a complete indexed table of approximate squared distances with correct point correspondences and a strict error bound. Historical priority remains subject to unindexed equivalent literature; no independent external mathematical validation is claimed.

## References

1. A. D'Alì, M. Juhnke-Kubitzke, M. Koch, *On a generalization of symmetric edge polytopes to regular matroids*, arXiv:2307.04933v1 (first public 2023-07-10), Theorem 4.6, Corollary 4.7, Remark 4.8. https://arxiv.org/abs/2307.04933
2. A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193 (2019); *Electronic Journal of Combinatorics* 29(3), P3.24 (2022). https://doi.org/10.37236/10387
3. M. Winter, *Rigidity, tensegrity and reconstruction of polytopes under metric constraints*, arXiv:2302.14194 (2023). https://arxiv.org/abs/2302.14194
4. G. Rembado, *A colourful classification of (quasi) root systems and hyperplane arrangements*, arXiv:2206.03779 (2022), Sections 1--2. https://arxiv.org/abs/2206.03779
5. H. Whitney, *Congruent graphs and the connectivity of graphs*, *American Journal of Mathematics* 54 (1932), 150--168. https://doi.org/10.2307/2371086
6. T. A. Cuchilla, J. Hound, C. Plepel, A. R. Vindas-Meléndez and L. Ye, *Unitary Actions and Equivariant Volumes of Symmetric Edge Polytopes*, arXiv:2507.18846v2 (2025), Theorem 3.8. https://arxiv.org/abs/2507.18846v2
