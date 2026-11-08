# Orbit-count fixed-point spheres for the dissociation complexes of three-edge spiders

## Finding

For each integer \(m\ge 2\), let \(T_m\) be the tree with hub \(c\) and \(m\) internally disjoint arms \(c-a_i-b_i-d_i\), \(1\le i\le m\). Let \(X_m=\operatorname{Ind}_2(T_m)\) be the simplicial complex of vertex subsets whose induced connected components have at most two vertices (the dissociation or three-vertex-path-free complex). The group \(S_m\) acts by permuting the arms.

**Theorem.** There is an \(S_m\)-equivariant homotopy equivalence
\[
 |X_m|\simeq_{S_m}\bigl|\partial\Delta^2*\cdots*\partial\Delta^2\bigr|
 \cong_{S_m} S(\mathbb R^2\otimes\mathbb R^m),
\]
where the join contains \(m\) factors and \(S_m\) permutes them, while \(S(V)\) denotes the unit sphere of a real representation \(V\). Therefore for **every** subgroup \(H\le S_m\), with \(o(H)\) orbits on the arms,
\[
 \boxed{\quad |X_m|^H\simeq S^{2o(H)-1}.\quad}
\]
In particular, the nonequivariant type is \(S^{2m-1}\); the entire \(S_m\) fixes a subspace homotopy equivalent to \(S^1\); and each arm permutation acts trivially on \(\widetilde H_{2m-1}(X_m;\mathbb Z)\cong\mathbb Z\), despite the orbit-dependent dimensions of subgroup fixed spaces.

## Assumptions and scope

The graph is finite, undirected, simple and has exactly the given \(3m+1\) vertices and \(3m\) edges. No geometric realization is confused with the complex of individually fixed vertices: the fixed points allow equal barycentric coordinates on entire permuted vertex orbits. The sphere convention is the standard unit sphere in the specified real vector space. All homotopy equivalences are ordinary topological equivalences on geometric realizations; the displayed \(S_m\)-equivalence is simultaneous for all subgroups.

## Proof

**1. Deleting the hub.** Set \(X=X_m\), \(K=\operatorname{del}_X(c)\), and \(L=\operatorname{lk}_X(c)\). Then \(X=K\cup(c*L)\) and \(K\cap(c*L)=L\), and all three subcomplexes are \(S_m\)-invariant. In the absence of \(c\), the induced graph is the disjoint union of \(m\) copies of the three-vertex path \(a_i-b_i-d_i\). Every proper subset of each such path is admissible, whereas its full triple is forbidden. Hence
\[
 K=\mathop{*}_{i=1}^m\partial\Delta(\{a_i,b_i,d_i\}).
\]
This is an exact equality of simplicial complexes, not merely a homological equivalence.

**2. Equivariant contractibility of the hub link.** Put \(B=\{b_1,d_1,\ldots,b_m,d_m\}\), and write \(\Delta(B)\) for its full simplex. For a face containing \(c\), there can be at most one \(a_i\): two such vertices would make a connected component with at least three vertices. If \(a_i\) occurs, then \(b_i\) cannot occur because \(c,a_i,b_i\) form a forbidden three-vertex path. Conversely, these are all constraints, since for any other arm, a subset of \(\{b_j,d_j\}\) induces at most a two-vertex component, and \(d_i\) is isolated whenever \(a_i\) is present and \(b_i\) absent. Consequently the link has the exact facet description
\[
 L=\Delta(B)\ \cup\ \bigcup_{i=1}^m\bigl(a_i*\Delta(B\setminus\{b_i\})\bigr).
\]
Define a simplicial map \(p:L\to\Delta(B)\) by \(p(a_i)=d_i\) and \(p(b_i)=b_i\), \(p(d_i)=d_i\). The map is \(S_m\)-equivariant and restricts to the identity on \(\Delta(B)\). For each simplex \(\sigma\) of \(L\), the union \(\sigma\cup p(\sigma)\) is again a simplex of \(L\): a simplex contains at most one \(a_i\), and in that case adding \(d_i\) remains admissible. The straight-line contiguity homotopy from the identity to \(p\) is therefore \(S_m\)-equivariant and stays inside the unique indicated simplex. Hence \(|L|\) \(S_m\)-equivariantly deformation retracts onto \(|\Delta(B)|\). A further straight-line contraction to the barycenter of \(\Delta(B)\), which is fixed by \(S_m\), shows that \(|L|^H\) is nonempty and contractible for every \(H\le S_m\).

**3. Gluing the cone.** For every subgroup \(H\), the invariant subcomplexes provide a closed cover of fixed-point spaces
\[
 |X|^H=|K|^H\cup\bigl(c*|L|^H\bigr),\qquad |K|^H\cap(c*|L|^H)=|L|^H.
\]
The inclusion \(|L|^H\hookrightarrow c*|L|^H\) is a homotopy equivalence because both spaces are contractible. It is a cofibration of triangulable spaces after barycentric subdivision, so the gluing lemma gives a homotopy equivalence \(|K|^H\hookrightarrow |X|^H\). Alternatively, the equivariant gluing lemma gives the equivalence \(|K|\simeq_{S_m}|X|\), since the contraction in Step 2 holds simultaneously for every isotropy subgroup.

**4. Fixed spheres.** Identify the geometric boundary of each \(2\)-simplex with the unit circle \(S(\mathbb R^2)\) by the same PL/radial homeomorphism on all arms. The standard join-to-unit-sphere homeomorphism gives an \(S_m\)-equivariant homeomorphism
\[
 |K|\cong S\!\left(\bigoplus_{i=1}^m\mathbb R^2\right).
\]
For an arbitrary subgroup \(H\le S_m\), a vector is fixed precisely when its \(\mathbb R^2\)-coordinates agree along each \(H\)-orbit. The fixed linear subspace has dimension \(2o(H)\), so its unit sphere is \(S^{2o(H)-1}\). Step 3 transfers this homotopy type to \(|X|^H\), proving the theorem. Finally, each transposition of two \(2\)-dimensional summands has determinant \((-1)^{2\cdot2}=+1\); thus all arm permutations act by degree \(+1\) on the top integral sphere homology. \(\square\)

## Verification

The standalone `VERIFY.py` constructs the graph adjacency, enumerates every candidate face by checking *all induced connected-component sizes*, forms the fixed-point orbit complexes by expanding arm-orbit supports, and independently computes their reduced simplicial Betti numbers over \(\mathbb F_2\) using augmented chain complexes. It checks every integer partition of \(m\) for \(2\le m\le5\): there are 17 orbit-size patterns, including the identity and transitive subgroups. It processes 28,959 admissible faces in total and finds exactly one reduced Betti number, in degree \(2o-1\), for each case. Run `python3 VERIFY.py` from the extracted package directory; the recorded output is in `verification_output.txt`. The unrestricted homotopy and integral claims are established by the preceding proof, **not** by finite enumeration or mod-two computation.

## Relationship to prior work

Sawant's 2026 tree theorem proves that every \(r\)-independence complex of a tree is vertex decomposable, and specifically identifies \(\operatorname{Ind}_2\) with a three-vertex-path-free complex; it does not identify the geometric fixed spaces of arbitrary branch-permutation subgroups. Deshpande and Singh (2020/2021) compute exact nonequivariant homotopy types of fully whiskered graphs and graphs with a pendant leaf at each non-leaf vertex. The tree here is neither: its hub has no adjacent pendant leaf. Their general formula cannot be specialized to the present graph, and its nonequivariant conclusions alone do not determine fixed-point spaces. Prior work on uniform two-edge spiders also does not cover the three-edge-arm regime; these are different graph families with different \(r=2\) homotopy behavior. The new statement is an explicit **equivariant** identification, substantially stronger than knowing the ordinary sphere type or orientation character.

## Limitations

This theorem treats only \(r=2\), arms of exactly three edges, and the natural group of arm permutations. It does not classify all higher-independence parameters, heterogeneous arm lengths, or fixed spaces for arbitrary graph automorphisms beyond this action. The verification is finite and over \(\mathbb F_2\); the integral and all-subgroup conclusions depend on the proof. No independent audit has been performed.

## References

1. Rutuja Sawant, *On the Vertex Decomposability of r-Independence Complexes of Trees*, arXiv:2605.25150 (first public version May 24, 2026), https://arxiv.org/abs/2605.25150.
2. Priyavrat Deshpande and Anurag Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448 (first public version January 15, 2020), https://arxiv.org/abs/2001.05448; see Theorems 3.8 and 3.10.
3. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863 (first public version June 21, 2021), https://arxiv.org/abs/2106.10863.
