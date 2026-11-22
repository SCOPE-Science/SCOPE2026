# One-edge robustness of higher-independence complexes of complete multipartite graphs

## Finding

The deletion of one cross-edge from a complete multipartite graph preserves the single-dimensional sphere-wedge homotopy pattern of **every** higher-independence complex. It decreases the sphere multiplicity by an explicit binomial amount, and the inclusion induces a split integral homology surjection with precisely that primitive kernel.

Let \(G=K_{m_1,\ldots,m_s}\), with \(s\ge2\) and \(m_i\ge1\); put \(N=\sum_{i=1}^s m_i\). Choose \(u\) in the first part and \(v\) in the second part, and set \(H=G-uv\). For every integer \(r\ge2\),

\[
\operatorname{Ind}_r(H)\simeq\bigvee^{\beta_r(H)}S^{r-1},\qquad
\beta_r(H)=\binom{N-1}{r}-\binom{m_1}{r}-\binom{m_2}{r}-\sum_{i=3}^s\binom{m_i-1}{r}.
\]

The induced homology map from \(\operatorname{Ind}_r(G)\) to \(\operatorname{Ind}_r(H)\) is a split surjection in degree \(r-1\), with a primitive free kernel of rank

\[
t_r=\binom{m_1-1}{r-1}+\binom{m_2-1}{r-1}.
\]

All other reduced integral homology groups of both complexes vanish. The formulas include zero multiplicities and all boundary values of \(r\).

## Assumptions and scope

For a finite simple graph \(F\), \(\operatorname{Ind}_r(F)\) is the abstract simplicial complex consisting of vertex subsets \(S\) for which every connected component of \(F[S]\) has at most \(r\) vertices. Every part of \(G\) is nonempty. The graph \(H\) is obtained by deleting only the edge \(uv\). We interpret \(\binom ab=0\) when \(b<0\) or \(b>a\), and \(\bigvee^0 S^d\) as a point. The complexes include the empty face. The range \(r\ge N\) is covered: both complexes are simplices.

## Proof

**1. Identify every changed face.** Write \(V_1,\ldots,V_s\) for the independent parts. If a set is mixed (meets at least two parts), its induced subgraph in \(G\) is connected. Hence a set is in \(X=\operatorname{Ind}_r(G)\) precisely when it has at most \(r\) vertices or lies entirely in a single part. For \(Y=\operatorname{Ind}_r(H)\), a previously forbidden mixed subset can become allowed only when deletion of \(uv\) disconnects its induced graph. As every other cross-edge is present, the only such subsets are \(\{u,v\}\cup R\), with \(R\subseteq V_1\setminus\{u\}\) of cardinality \(r-1\), or \(\{u,v\}\cup Q\), with \(Q\subseteq V_2\setminus\{v\}\) of cardinality \(r-1\). Every one of these subsets consists of an isolated endpoint and a connected component of exactly \(r\) vertices after deleting \(uv\). They are the entire difference \(Y\setminus X\); they are \(r\)-simplices. Their number is \(t_r\).

**2. Elementary collapse.** Each new simplex \(\sigma=\{u,v\}\cup R\) with \(R\subseteq V_1\setminus\{u\}\) has a unique free codimension-one face \(\sigma\setminus\{u\}=\{v\}\cup R\); for a second-part simplex \(\tau=\{u,v\}\cup Q\), use \(\tau\setminus\{v\}=\{u\}\cup Q\). Each marked face is mixed of cardinality \(r\) and belongs to no other \(r\)-simplex (the pure-part \(r\)-simplices cannot contain it). Collapsing these pairs removes every added simplex.

For each part \(V_i\), choose an anchor \(c_i\). Enumerate all subsets \(S\subseteq V_i\setminus\{c_i\}\) of size at least \(r\) in descending cardinality; pair \(S\) with \(S\cup\{c_i\}\). At its turn, \(S\) has exactly one remaining proper coface, the indicated partner: all larger pure-part cofaces were already removed, and there are no remaining mixed faces of size greater than \(r\). These are elementary free-face collapses. The resulting complex has dimension at most \(r-1\).

**3. Deduce the homotopy type.** Both \(X\) and \(Y\) originally contain the full \((r-1)\)-skeleton of the simplex on \(N\) vertices, and are therefore \((r-2)\)-connected when \(2\le r<N\). The collapses show both are homotopy equivalent to CW complexes of dimension at most \(r-1\). A connected, \((r-2)\)-connected CW complex of dimension \(r-1\) is a wedge of \((r-1)\)-spheres (for \(r=2\), a connected graph; for \(r\ge3\), use Hurewicz and Whitehead). For \(r\ge N\), both are simplices and the formulas give zero spheres.

**4. Compute the integer ranks.** The original complete-multipartite result gives
\[
\beta_r(G)=\binom{N-1}{r}-\sum_{i=1}^s\binom{m_i-1}{r}.
\]
It also follows directly from the full skeleton together with the disjoint higher-dimensional pure-part faces, using Euler characteristic and the collapse of step 2. Each of the \(t_r\) new \(r\)-simplices contributes \((-1)^r\) to the Euler characteristic of \(Y\) relative to \(X\). Since all reduced homology is in degree \(r-1\), \(\beta_r(H)=\beta_r(G)-t_r\). Pascal's identity \(\binom{m-1}{r}+\binom{m-1}{r-1}=\binom mr\) gives the displayed formula.

**5. Determine the inclusion map integrally.** The relative simplicial chain complex \(C_*(Y,X;\mathbb Z)\) consists solely of \(C_r(Y,X;\mathbb Z)=\mathbb Z^{t_r}\) and zero groups in all other degrees, because the only new faces are the listed \(r\)-simplices. Thus \(H_r(Y,X;\mathbb Z)=\mathbb Z^{t_r}\). Since \(H_r(Y;\mathbb Z)=0\) and \(H_{r-2}(X;\mathbb Z)=0\), the long exact sequence yields
\[
0\longrightarrow \mathbb Z^{t_r}\longrightarrow
\widetilde H_{r-1}(X;\mathbb Z)\longrightarrow
\widetilde H_{r-1}(Y;\mathbb Z)\longrightarrow 0.
\]
The right group is free abelian by the sphere-wedge result, so this sequence splits. Accordingly the kernel is primitive and has the claimed exact rank.

## Verification

`verify.py` constructs directly the graphs and all induced-component-limited faces for every multipartite tuple of two through four parts, each of size one through four and total order at most nine, for every \(2\le r\le N\). It checks the exact new-face characterization, every individual elementary collapse using unique surviving cofaces, the retained low skeleton, every mod-two reduced Betti number and both binomial formulas. All 1,111 test cases passed, encompassing 224,180 enumerated faces and 1,177 free-face pairs. The machine's mod-two calculations do not certify integral topology; the preceding elementary-collapse proof does.

## Relationship to prior work

Deshpande and Singh determined the higher-independence homotopy types of intact complete multipartite graphs, including the \(\beta_r(G)\) formula. The present statement concerns the different graphs obtained by deleting one selected edge and proves the induced map on integral homology. A separate previously published classification of the second-independence complexes of complete bipartite graphs after deleting a matching covers the \(s=2,r=2\) specialization. That special case is prior work, not an original assertion here. The general all-threshold, arbitrary-part-number edge-punctured theorem and primitive kernel conclusion are not consequences of those stated classifications.

## Limitations

The result treats one deleted cross-edge and arbitrary positive part sizes, not two intersecting deleted edges or arbitrary edge-deletion patterns. The sphere-wedge equivalence is not claimed equivariant, canonical, or an elementary collapse directly onto a wedge. Novelty is relative to the sources actually inspected; an unindexed equivalent theorem remains possible. Finite verification supplements but does not replace the universal proof.

## References

1. P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448 (first public 2020-01-15), https://arxiv.org/abs/2001.05448. See the complete multipartite theorem.
2. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy and A. Singh, *Chordal Graphs, Higher Independence and Vertex Decomposable Complexes*, arXiv:2106.10863 (2021), https://arxiv.org/abs/2106.10863. Related higher-independence work on chordal graphs.
3. *Homotopy of Second Independence Complexes After Deleting a Bipartite Matching*, research record `2026/11/8/SCOPE-homotopy-of-second-independence-complexes-after-deleting-a-bipar--223b7506ca23`, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-homotopy-of-second-independence-complexes-after-deleting-a-bipar--223b7506ca23. Previously covers the bipartite \(r=2\) subcase.
