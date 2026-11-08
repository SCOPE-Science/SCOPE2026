# Path-free complexes of complete split graphs: integral homotopy and symmetry

## Finding

Fix integers \(r,n\geq2\) and \(t\geq5\). Let \(G=K_r\vee\overline K_n\), the *complete split graph* with a clique \(H\) of \(r\) vertices and an independent set \(L\) of \(n\) vertices, all edges between the two sets present. Let \(X=\operatorname{PF}_t(G)\) be the abstract simplicial complex whose faces are subsets of vertices whose induced subgraphs contain **no simple path on \(t\) distinct vertices**, whether induced or not. Interpret binomial coefficients outside their ordinary range as zero. Put

\[
 B(r,n,t)=\sum_{p=\lceil(t-1)/2\rceil}^{\min(r,t-1)}\binom rp\binom{n-1}{t-1-p}.
\]

**Theorem.** There is a nonequivariant homotopy equivalence
\[
 |X|\simeq\bigvee^{B(r,n,t)}S^{t-2},
\]
where an empty wedge is a point. In particular, its only possibly nonzero reduced integral homology is
\[
 \widetilde H_{t-2}(X;\mathbb Z)\cong\mathbb Z^{B(r,n,t)}.
\]
Fix a specified leaf \(v\in L\) and let \(\Gamma_v=S_r\times S_{n-1}\), the subgroup of part-preserving automorphisms fixing \(v\). There is a natural isomorphism of **integral** \(\Gamma_v\)-modules
\[
 \widetilde H_{t-2}(X;\mathbb Z)
 \cong \bigoplus_{p=\lceil(t-1)/2\rceil}^{\min(r,t-1)}
  \bigwedge^p\mathbb Z^r\otimes_{\mathbb Z}
  \bigwedge^{t-1-p}\mathbb Z^{n-1}.
\]
The exterior powers carry the usual permutation actions and are interpreted as zero when their degrees exceed their ranks.

For the **entire** part-preserving automorphism group \(\Gamma=S_r\times S_n\), an arbitrary \(\gamma=(\sigma,\tau)\) has the explicit rational homology character
\[
\operatorname{tr}\!\left(\gamma\mid\widetilde H_{t-2}(X;\mathbb Q)\right)
=(-1)^{t-1}\!\sum_{\substack{0\le p\le r,\ 0\le q\le n\\\min(p+q,2p+1)<t}}
[z^p]\!\prod_{C\in\operatorname{cyc}(\sigma)}(1-z^{|C|})\;
[w^q]\!\prod_{D\in\operatorname{cyc}(\tau)}(1-w^{|D|}),
\]
where \(\operatorname{cyc}(\sigma)\) and \(\operatorname{cyc}(\tau)\) denote the permutation cycles, and \([z^p]\) and \([w^q]\) denote coefficient extraction. Moreover,
\[
 \widetilde H_{t-2}(X;\mathbb Z)^{\Gamma}=0.
\]
The characteristic-zero invariants also vanish.

For example, \(r=n=3\), \(t=5\) gives five three-spheres, but no nonzero homology class fixed by every automorphism. The result remains valid when \(B(r,n,t)=0\), including \(t>r+n\).

## Assumptions and scope

The graph is finite, simple, and unfilled. A path is a not-necessarily-induced simple subgraph; the induced graph on a candidate vertex set may have extra edges. Every \(r,n\geq2\) and every integer \(t\geq5\) is covered. The part-preserving automorphism group is \(S_r\times S_n\), and the indicated leaf-stabilizer is \(S_r\times S_{n-1}\). The homotopy equivalence is **nonequivariant**; only the stated homology-module and character conclusions are equivariant. No equivariant wedge splitting for the full group is asserted.

## Proof

**1. Longest paths.** A face has \(p\) selected clique vertices and \(q\) selected independent vertices. Every two selected independent vertices must be separated along a simple path by a selected clique vertex, so a path has at most \(2p+1\) vertices and at most \(p+q\) vertices. Conversely, when \(q\leq p+1\), alternate the independent vertices with clique vertices and insert unused clique vertices consecutively; this realizes a path of order \(p+q\). When \(q>p+1\), alternate all \(p\) clique vertices with \(p+1\) independent vertices to realize \(2p+1\). For \(p=0\), any nonempty independent induced graph has longest path of order one. Thus the longest path order (with the empty-set convention) is
\[
 \ell(p,q)=\min\{p+q,2p+1\}
\]
for nonempty sets, and consequently a vertex subset is a face precisely when \(\min(p+q,2p+1)<t\).

**2. A contractible subcomplex.** Select a leaf \(v\in L\). Define its (closed) simplicial star \(A=\operatorname{st}_X(v)=\{F\in X:F\cup\{v\}\in X\}\). This is a cone with apex \(v\), hence it is contractible. Consider any face \(F\in X\setminus A\). Necessarily \(v\notin F\). Let \(p\) and \(q\) be the counts of clique and independent vertices in \(F\). The two conditions \(F\in X\) and \(F\cup\{v\}\notin X\) give
\[
\min(p+q,2p+1)<t\leq\min(p+q+1,2p+1).
\]
The second inequality forces \(2p+1\geq t\), and the first then forces \(p+q<t\). Together they imply \(p+q=t-1\) and \(p\geq\lceil(t-1)/2\rceil\). Conversely, every face on exactly \(t-1\) vertices with this clique count, excluding \(v\), satisfies the two conditions and lies outside \(A\).

**3. Attaching maps and homotopy.** Every proper subface of any \(F\in X\setminus A\) has at most \(t-2\) vertices, so adding \(v\) yields at most \(t-1\) vertices; therefore every proper subface lies in \(A\). Hence \(X\) is obtained from the contractible subcomplex \(A\) by attaching exactly \(B(r,n,t)\) simplices of dimension \(t-2\), all along their complete boundaries. As \(|A|\hookrightarrow|X|\) is a CW-cofibration and \(|A|\) is contractible, the quotient \(|X|/|A|\) has the homotopy type of \(|X|\). This quotient is exactly a wedge of \(B(r,n,t)\) spheres of dimension \(t-2\). This proves the integral homotopy and homology assertions, including the zero-sphere-count case.

**4. Integral stabilizer representation.** The subgroup \(\Gamma_v\) preserves the cone \(A\) and acts by permuting the relative \((t-2)\)-simplices \(F\in X\setminus A\), with the usual orientation sign. The relative chain complex \(C_*(X,A;\mathbb Z)\) has precisely these generators in degree \(t-2\), zero relative differentials, and no other generators. Their decomposition by the clique count \(p\), with signs dictated by permuting the selected hub vertices and the selected other leaves, is exactly the displayed direct sum of exterior-power tensor products. Since \(A\) is contractible, the long exact sequence of the pair identifies this relative module naturally with \(\widetilde H_{t-2}(X;\mathbb Z)\). No division or field extension is used.

**5. Full character.** The leaf-fixed cone \(A\) is not preserved by a general element of \(S_n\), so use the Hopf trace formula on the **augmented** simplicial chain complex instead. A \(\gamma=(\sigma,\tau)\)-fixed face is a union of cycles of the two permutations. If it contains \(a\) selected permutation cycles and has \(p\) hubs and \(q\) leaves, its contribution to the alternating reduced chain trace is \((-1)^{a+1}\). Indeed the orientation sign on its \(p+q\) vertices is \((-1)^{p+q-a}\), and its simplicial degree is \(p+q-1\). Including the empty augmented face, the reduced Lefschetz number is minus the sum of \((-1)^a\) over all fixed permitted faces. The generating functions for these signed fixed-face counts are \(\prod_C(1-z^{|C|})\) and \(\prod_D(1-w^{|D|})\), and the permitted pairs satisfy \(\min(p+q,2p+1)<t\). Since the only reduced rational homology can occur in degree \(t-2\), the reduced Lefschetz number equals \((-1)^{t-2}\) times its character. Rearranging gives the displayed formula.

**6. Vanishing global invariants.** Because \(t\geq5\), all exterior degrees \(p\) occurring in Step 4 are at least two. An \(S_r\)-invariant element of \(\bigwedge^p\mathbb Q^r\) must have zero coefficient on each standard wedge basis element: the transposition of any two indices in its selected \(p\)-subset fixes that subset and reverses its orientation. Hence every \(S_r\)-invariant vector in the direct sum vanishes, even after tensoring with the independent-leaf modules. The full-group invariants are a subgroup of those for \(S_r\), so they vanish over \(\mathbb Q\), and therefore over \(\mathbb Z\) as well.

## Verification

The supplied standalone standard-library Python program `verify.py` reconstructs the complete split-graph adjacency list, uses an independent depth-first search for forbidden \(t\)-vertex paths, enumerates faces, checks the star-relative exceptional-simplex criterion and the boundary containment, and computes mod-two simplicial homology. It separately computes the signed Lefschetz character by enumerating fixed oriented faces, comparing it with the cycle-polynomial formula and (when a leaf is fixed) the signed relative-facet trace. It also averages characters over several full automorphism groups to check vanishing invariants. Running `python verify.py` produces `verify_output.txt` containing `ALL_VERIFY_OK`.

The finite check covers 41 parameter triples, 7,591 tested vertex subsets, 880 automorphisms, 310 leaf-stabilizer character tests and five full-invariant group averages. These are independent finite consistency checks, not a proof for infinitely many parameters. Steps 1–6 supply the general proof.

## Relationship to prior work

Deshpande, Goyal and Sawant introduced systematic decompositions and decomposability criteria for path-free complexes of complete multipartite graphs in their July 2026 preprint [1]. Its publicly accessible abstract states an explicit full wedge classification for complete **bipartite** graphs, not this complete split-graph formula, integral stabilizer module, or full cycle-type character. The present theorem instead specializes to graphs whose multipartition consists of one large independent class and \(r\) singleton classes and treats all path lengths \(t\geq5\). Results for the four-vertex-path case do not imply a classification for variable larger path length and are excluded from the stated parameter range. The general principle that shifted complexes often have wedge-of-spheres homotopy types is classical; the contribution is the precise multiplicity and integral and full-group symmetry data for this particular natural path-free family, established here directly rather than quoted from a shifting theorem.

The full 19-page primary preprint was not available for text-level inspection through the accessible routes; it remains possible that its body or another unindexed source contains equivalent specializations, particularly for the nonequivariant sphere count. This is a real originality limit, not evidence of priority.

## Limitations

Only complete split graphs, path lengths \(t\geq5\), and their part-preserving automorphisms are covered. The statement does not assert an equivariant homotopy wedge decomposition for the full group. The first public date below is that of the **motivating paper**, not a claimed publication date for this theorem. Finite computations do not establish the infinite-range theorem or independent certification. A plausible primary full-text overlap remains unresolved as noted above.

## References

[1] P. Deshpande, S. Goyal, and R. Sawant, *On a complete characterization of path-free complexes associated with complete multipartite graphs*, arXiv:2607.05358, first submitted July 6, 2026, https://arxiv.org/abs/2607.05358.

[2] J. Grbić and S. Theriault, *The homotopy type of the polyhedral product for shifted complexes* (2013), https://eprints.soton.ac.uk/356515/. This reference supplies general shifted-complex context, not the asserted split-graph or equivariant formulas.
