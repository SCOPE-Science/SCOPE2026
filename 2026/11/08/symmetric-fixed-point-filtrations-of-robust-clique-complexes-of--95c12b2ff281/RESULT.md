# Symmetric fixed-point filtrations of robust clique complexes of clique prisms

## Finding

Let \(H\) be any finite simple graph on \(m\ge2\) vertices, let \(r\ge2\), and let \(G=H\mathbin{\square}K_r\) be the Cartesian product. Let \(\Gamma\le S_r\) be **any transitive** permutation group acting on the \(K_r\)-coordinate. For each integer \(k\ge2\), define the robust clique complex
\[
R_k(G)=\{W\subseteq V(G):\alpha(G[W])<k\},
\]
where \(\alpha\) denotes the independence number. For \(S\subseteq V(H)\), define
\[
b_r(S)=\max\{|T|:T\subseteq S,\ \chi(H[T])\le r\},
\]
with \(b_r(\varnothing)=0\). The **entire geometric fixed-point filtration**, with the inclusion maps as \(k\) grows, has a canonical levelwise PL-isomorphism
\[
\boxed{\ |R_k(G)|^\Gamma\ \cong_{\mathrm{PL}}\
\left|\{S\subseteq V(H):b_r(S)<k\}\right|\quad(k\ge2).\ }
\]
Here the right side is the realization of an abstract simplicial complex on the \(m\) vertices of \(H\), and the isomorphisms commute with the filtration inclusions.

In particular, if \(\chi(H)\le r\), then for \(2\le k\le m\),
\[
\boxed{\ |R_k(G)|^\Gamma\cong_{\mathrm{PL}}|\operatorname{skel}_{k-2}\Delta^{m-1}|
\simeq\bigvee^{\binom{m-1}{k-1}}S^{k-2}.\ }
\]
For \(k>m\) the fixed space is contractible. The full reduced integral persistent homology of this fixed filtration consists of \(\binom{m-1}{k-1}\) intervals \([k,k+1)\) in degree \(k-2\), for \(k=2,\ldots,m\), and no other intervals; in particular every inclusion-induced map on reduced integral homology vanishes.

No colorability assumption is needed for the following sharp boundary test at \(k=m\):
\[
\boxed{\ |R_m(H\mathbin{\square}K_r)|^\Gamma\cong_{\mathrm{PL}}
\begin{cases}
|\partial\Delta^{m-1}|\cong S^{m-2},&\chi(H)\le r,\\
|\Delta^{m-1}|,&\chi(H)>r.
\end{cases}\ }
\]
Thus the fixed space at this one natural level detects \(r\)-colorability as a sphere-versus-ball dichotomy. If \(H\) is minimally non-\(r\)-colorable under vertex deletions, the skeleton formula persists for \(2\le k<m\) but the terminal sphere is filled at \(k=m\), one filtration step earlier than for an \(r\)-colorable graph.

## Assumptions and scope

All graphs are finite, simple, undirected. The Cartesian product has vertices \((v,i)\), with \((v,i)\sim(w,j)\) exactly when \(v=w\) and \(i\ne j\), or when \(i=j\) and \(v\sim_H w\). A transitive subgroup \(\Gamma\le S_r\) acts by \((v,i)\mapsto(v,\gamma i)\). The fixed points are **pointwise geometric fixed points** in the realization, including barycenters of invariant simplex orbits; they are not merely fixed vertices. The integer \(k\) starts at \(2\), and the formula covers all \(m\ge2\), \(r\ge2\), and transitive \(\Gamma\), including disconnected \(H\) and the boundary cases \(k=m\) and \(k>m\). The reduced homology convention is used when \(k=2\): a wedge of \(m-1\) zero-spheres is a discrete set of \(m\) points.

## Proof

**1. Geometric fixed points and orbit simplices.** For any simplicial complex with a finite group acting by vertex permutations, the geometric fixed space has the following canonical simplicial model. Its candidate vertices are the orbits \(O\) of vertices that are themselves faces; a collection of orbits spans a simplex exactly when their union is a face of the original complex. Map each orbit vertex to the barycenter of that orbit. In a geometric fixed point, barycentric coefficients must be constant on each orbit because the point is group-fixed. Its positive support is a face, hence a union of full vertex orbits. The point is therefore uniquely a convex combination of the indicated orbit barycenters. Conversely, every such combination is group-fixed. The barycenters of disjoint vertex orbits are affinely independent, making this a simplicial PL homeomorphism, compatible with inclusions. In \(G\), transitivity of \(\Gamma\) says that the vertex orbits are precisely the full \(r\)-cliques \(O_v=\{(v,i):1\le i\le r\}\), one for each \(v\in V(H)\).

**2. Exact orbit-face criterion.** For each \(S\subseteq V(H)\), the union of the orbits indexed by \(S\) is \(S\times[r]\). In an independent set of the induced product graph \(G[S\times[r]]\), at most one vertex may be selected from each clique \(O_v\). A selection of \(t\) such vertices determines \(t\) distinct base vertices and assigns to each its chosen coordinate in \([r]\). The selection is independent exactly when this coordinate assignment is a proper \(r\)-coloring of the induced base graph on those \(t\) vertices: edges within one coordinate layer coincide with edges of \(H\). Conversely, each proper \(r\)-coloring of \(H[T]\) selects the corresponding independent set \(\{(v,c(v)):v\in T\}\). Maximizing \(t\) proves the **exact equality**
\[
\alpha\bigl(G[S\times[r]]\bigr)=b_r(S).
\]
By the definition of \(R_k\), the orbit union is a face if and only if \(b_r(S)<k\). Substituting this in step 1 proves the PL statement at every level, including compatibility of the inclusions.

**3. Colorable bases and homotopy.** If \(\chi(H)\le r\), every induced subgraph \(H[S]\) is \(r\)-colorable. Thus \(b_r(S)=|S|\), and the fixed complex contains exactly those \(S\) with \(|S|\le k-1\); for \(k\le m\) this is \(\operatorname{skel}_{k-2}\Delta^{m-1}\). For completeness, the standard simplex-skeleton wedge count admits an explicit discrete-Morse matching. Fix a vertex \(v_0\). Pair each nonempty face avoiding \(v_0\), of size at most \(k-2\), with the face obtained by adjoining \(v_0\). The matching is acyclic: after traversing a matched edge upward by adding \(v_0\), any different downward edge deletes a different vertex and leaves \(v_0\) present, so it cannot begin another matched upward edge. The unmatched faces are the single vertex \(\{v_0\}\) and the \(\binom{m-1}{k-1}\) faces of size \(k-1\) avoiding \(v_0\). The resulting Morse CW complex has one zero-cell and only cells of dimension \(k-2\); all attaching maps are constant in this CW model. This yields the stated sphere wedge, for \(k=2\) read as the discrete \(m\)-point space. The reduced homology has one nonzero degree per \(k\), and the next level has no reduced homology in that degree. Hence every transition map is zero and the claimed integral persistence intervals follow. At \(k>m\), all orbit unions qualify and the fixed complex is a simplex.

**4. Chromatic sharpness at \(k=m\).** Regardless of the graph, for each proper \(S\subsetneq V(H)\), \(b_r(S)\le |S|\le m-1< m\), so all proper faces of \(\Delta^{m-1}\) occur in the fixed model at \(k=m\). The full face occurs if and only if \(b_r(V(H))<m\), which means that no proper \(r\)-coloring exists on all \(m\) vertices, equivalently \(\chi(H)>r\). This proves the sphere-versus-ball dichotomy. If \(H\) is minimally non-\(r\)-colorable under vertex deletion, every proper induced subgraph is \(r\)-colorable; thus \(b_r(S)=|S|\) for proper \(S\), giving all earlier skeleton stages and filling the final simplex at \(k=m\). No converse about general homotopy equivalence is claimed.

## Verification

The independent verifier `verify_prism_fixed.py` uses exact adjacency-based enumeration of independent sets in the full Cartesian product, separately backtracks proper colorings of induced base subsets, and compares their maxima on every union of orbit fibers. It checks all 75 labeled graphs on at most four vertices for each of \(r=2,3\), twelve targeted cases on five vertices, 416 direct invariant-face instances in smaller graphs, and simplex-skeleton Euler identities through eight vertices. Its recorded output is in `verification_output.txt` and ends with `PRISM_FIXED_COMPLEX_AND_COLORABILITY_TESTS_OK`. These finite tests corroborate steps 1–4. The theorem for arbitrary graph order, group order, and robustness level is proved by the exact arguments above, not by finite extrapolation.

## Relationship to prior work

Kim and Lew introduced complexes of graph subsets with bounded independence number and studied their collapsibility (arXiv:1912.12605, first submitted 2019-12-29). Filakovský's 2026 work develops the robust-clique terminology and determines ordinary homotopy types for grid and square-sequence graphs, particularly at levels two and three (arXiv:2602.11365, first submitted 2026-02-11). The present statement instead determines **geometric group-fixed filtrations**, including their integral persistent homology, for arbitrary complete-clique Cartesian factors and any base graph; it also relates the terminal fixed-space topology exactly to base-graph colorability. The cited ordinary homotopy classifications and collapsibility estimates do not themselves supply the fixed-orbit PL model or its chromatic criterion. Related published work on equivariant Euler characters treats alternating homology traces, a weaker invariant than the explicit geometric fixed-space classification. Potential unindexed equivalent formulations remain a limitation.

## Limitations

This result describes pointwise geometric fixed spaces for a transitive action on the clique-coordinate factor, not individual fixed spaces of nontransitive subgroups and not the ambient equivariant homotopy type. For arbitrary non-\(r\)-colorable \(H\), the exact fixed complex is given by the coloring-deletion statistic \(b_r(S)\); its homotopy type is not classified uniformly at intermediate \(k\). The integral homotopy and barcode formula requires \(\chi(H)\le r\), apart from the all-graphs boundary criterion at \(k=m\). Originality is assessed against inspected accessible results, not certified against all possible literature; independent external validation has not occurred.

## References

1. Minki Kim and Alan Lew, *Complexes of graphs with bounded independence number*, arXiv:1912.12605 (first public submission 2019-12-29), https://arxiv.org/abs/1912.12605.
2. Marek Filakovský, *The Topology of \(k\)-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365 (first public submission 2026-02-11), https://arxiv.org/html/2602.11365.
3. Standard simplicial discrete-Morse theory and homology of simplex skeleta are used only for the explicit final wedge calculation; the orbit-fixed identification and graph-product reduction are proved here.
