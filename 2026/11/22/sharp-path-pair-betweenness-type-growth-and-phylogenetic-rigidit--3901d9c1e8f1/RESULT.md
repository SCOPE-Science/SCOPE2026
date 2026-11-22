# Sharp path-pair betweenness type growth and phylogenetic rigidity

## Finding

For a finite nonempty simple tree \(T\), a set \(A\subseteq V(T)\) of \(m\) distinctly named marked vertices, and a vertex \(x\), put
\[
P_{T,A}(x)=\{\{a,b\}\in\tbinom A2:x\text{ lies on the unique }a\text{--}b\text{ path}\}.
\]
Endpoints are included in the path. This is the truth-pattern of the one-free-variable, two-parameter inclusive tree-betweenness formula \(\beta(a,x,b)\). Define \(q(T,A)=|\{P_{T,A}(x):x\in V(T)\}|\).

**Sharp finite-size growth.** For every \(n\ge m\ge3\),
\[
\max_{|V(T)|=n,\ |A|=m}q(T,A)=\min\{n,3m-4\}.
\]
For \(m=2\), the maximum is \(1\) at \(n=2\) and \(2\) for \(n\ge3\). For \(m=1\), it is \(1\).

**Exact structural formula.** Assume \(m\ge3\) and let \(H\) be the minimal connected subtree of \(T\) containing \(A\). Write \(b\) for the number of unmarked vertices of degree at least three in \(H\). Call a vertex *essential* if it is marked or has degree at least three in \(H\). Compress each path of \(H\) whose internal vertices are nonessential to an essential edge. Let \(s\) be the number of compressed edges with at least one internal vertex in the original path and with neither endpoint of degree one in \(H\). Set \(\varepsilon=1\) if \(V(T)\setminus V(H)\ne\varnothing\), and \(\varepsilon=0\) otherwise. Then
\[
\boxed{q(T,A)=m+b+s+\varepsilon.}
\]

**Rigidity and census at equality.** For \(m\ge3\), equality \(q(T,A)=3m-4\) holds exactly when the minimal marked subtree \(H\) has all marked vertices as leaves, has precisely \(m-2\) unmarked degree-three branch vertices, has an unmarked degree-two vertex on each internal branch-to-branch path, and \(T\) contains at least one vertex outside \(H\). The resulting set of signatures uniquely determines the reduced unrooted binary phylogenetic tree on labelled leaf set \(A\). Exactly \((2m-5)!!\) distinct labelled maximal signature families occur. The smallest host attaining the maximum has exactly \(3m-4\) vertices.

## Assumptions and scope

Trees are finite, connected, simple, loopless and unweighted. The signature is only the Boolean truth vector of \(\beta(a,x,b)\) on unordered *distinct* marked pairs, not a complete first-order type and not the strict-betweenness relation by itself. The marked vertices may lie anywhere in the tree, including at internal vertices. All cardinality maxima range over all such trees and marked sets of the stated sizes. The count \((2m-5)!!\) distinguishes named-leaf signature families rather than host-graph isomorphism classes or extension-realization multiplicities.

## Proof

**1. Partition normal form and exact local formula.** Fix \(m\ge3\). For \(x\in H\), delete \(x\) from \(H\). Each resulting component contains a marked vertex: if not, \(H\) would not be minimal. Partition \(A\) into these nonempty marked-component sets; if \(x\in A\), adjoin the singleton part \(\{x\}\). Two distinct marks \(a,b\) have \(\{a,b\}\in P_{T,A}(x)\) precisely when they lie in different parts. Thus \(P_{T,A}(x)\), regarded as the edge set of a graph on \(A\), is the complete multipartite graph of this partition.

Every vertex outside \(H\) produces the empty signature. A nonessential vertex inside an essential-to-essential segment produces the complete bipartite graph defined by the two nonempty shores of the corresponding edge split. An essential leaf is necessarily a marked leaf and has the identical bipartite signature to all nonessential points on its incident compressed segment. Conversely, the signatures of distinct essential vertices are distinct, and the signatures of distinct nonpendant compressed segments are distinct: the partition parts recover the equivalence relation of nonadjacency in the complete multipartite graph, and two distinct essential positions or compressed edges cannot induce the same partition of \(A\) unless they lie along one pendant edge without another essential position. In more detail, different interior vertices are separated by a marked-to-marked path passing through exactly one of them; the only failure of this argument is at an essential marked leaf and points on its incident empty-mark interior segment. Every nonleaf essential vertex yields at least three nonempty parts, hence a triangle, while every segment point yields exactly two parts and a bipartite graph. Distinct nonpendant compressed segments correspond to distinct nontrivial splits. The number of signatures from \(H\) is therefore exactly \(m+b+s\), and the external empty type contributes \(\varepsilon\). This proves the structural formula.

**2. Global upper bound.** Let \(l\) be the number of marked leaves of \(H\). All leaves of \(H\) are marked and \(l\ge2\). The degree-sum identity \(\sum_{v\in H}(\deg_H(v)-2)=-2\) implies \(b\le l-2\). There are \(m+b-1\) compressed edges, of which \(l\) are pendant, so \(s\le m+b-1-l\). Therefore
\[
q(T,A)\le m+b+(m+b-1-l)+1=2m+2b-l\le2m+l-4\le3m-4.
\]
The trivial \(q(T,A)\le n\) gives the asserted upper bound.

**3. Equality and host construction.** Equality forces \(l=m\), \(b=m-2\), \(s=m+b-1-l=m-3\), and \(\varepsilon=1\). Since the excess degrees of the branch vertices sum to precisely \(m-2\), each has degree exactly three; every internal compressed edge must contain an unmarked degree-two subdivision vertex. Conversely these conditions yield \(q=3m-4\) by Step 1. Choose any unrooted full binary tree with \(m\) distinct labelled leaves, subdivide each of its \(m-3\) internal edges once, and add one extra pendant vertex beyond its marked hull. This construction has \(m+(m-2)+(m-3)+1=3m-4\) vertices and pairwise different signatures.

**4. Attaining every order.** With \(n=m\), mark every vertex of an \(m\)-vertex path; its \(m\) signatures are distinct. For every \(1\le j\le m-2\), choose an unrooted tree with all \(m\) marks as leaves and exactly \(j\) unmarked branching vertices (contract \(m-2-j\) interior edges of a full binary tree); without subdivisions its \(m+j\) essential vertex signatures are distinct. Starting at \(n=2m-2\), subdivide \(0,1,\ldots,m-3\) distinct interior branch-to-branch edges to attain every order through \(n=3m-5\), with all signatures still distinct. At \(n=3m-4\), add an exterior vertex as above; for larger \(n\), attach extra vertices outside the marked hull, which repeat the empty type. Therefore every \(n\ge m\) attains \(\min\{n,3m-4\}\). If \(m=2\), every vertex within the marked path has the same single-pair signature and all other vertices have the empty signature, establishing the exceptional formula. If \(m=1\), every signature is empty.

**5. Reconstructing maximal families.** At equality, each signature is either empty, a marked-leaf star, a complete bipartite edge-split graph, or a complete tripartite branch graph. The complete bipartite signatures, recognized by their nonempty bipartite edge graphs, recover *all* marked-leaf bipartitions induced by the edges of the reduced binary tree, including pendant splits. A compatible collection of tree edge splits uniquely determines its labelled unrooted tree: for example, repeatedly identify cherries and contract one leaf, or use the classical tree-split reconstruction theorem. Conversely every labelled binary unrooted tree produces such a maximal family by Step 3. Adding a new labelled leaf to an existing labelled binary tree entails subdividing precisely one of its \(2m-5\) edges and attaching the leaf. Starting with the unique three-leaf tree gives \((2m-5)!!\) families. Finally no tree with fewer than \(3m-4\) vertices can realize \(3m-4\) signatures, and Step 3 attains that count.

## Verification

The accompanying standard-library Python checker `verify_betweenness.py` independently computes every marked-pair path-membership signature and the compressed-hull formula. It checked 89,629 labelled-tree/marked-size cases arising from all labelled trees on three through seven vertices with the marked set fixed to the first \(m\) labels (equivalent to all marked sets by relabelling), with no discrepancy. It also generated every unrooted binary labelled tree for \(m=3,4,5,6,7\), verified the complete maximal trace families, and obtained respectively \(1,3,15,105,945\) different families. Run: `python3 verify_betweenness.py`. These are finite consistency checks; Steps 1–5 establish the universal statements.

## Relationship to prior work

Courcelle, *Axiomatizations of betweenness in order-theoretic trees* (original public preprint 2020), develops the betweenness structures, their logical characterization and induced substructures, not this finite-parameter pair-incidence profile. Bradley-Williams and Truss, *On limits of betweenness relations* (2021), classify one-point extension operations in a more general amalgamation setting, not the sharp pair-trace count for a single finite simple tree. Hellmuth, Lindeberg and Moulton, *Encoding Phylogenetic Networks with Least Common Ancestor Constraints* (first posted June 15, 2026), reconstruct network topology from ancestor-comparisons of pairs of leaves; its pair-pair LCA relation is different from the query asking whether an arbitrary vertex lies on a marked pair's undirected path. Standard compatible-split reconstruction yields the last part of Step 5 once the newly characterized maximal family is known; it does not supply the sharp \(n,m\) type-growth formula or the exact formula for nonextremal host trees.

## Limitations

The result is for finite simple trees, for distinct unordered marked pairs, and inclusive geodesic betweenness. It does not assert the same bound for general graphs, for a path-choice relation when geodesics are nonunique, or for the full first-order type in an expanded language. The census counts maximal *signature families*, not every possible host. A full independent review and a global historical-priority guarantee have not been supplied; there may be older specialized phylogenetic or graph-betweenness statements phrased differently.

## References

1. Bruno Courcelle, *Axiomatizations of betweenness in order-theoretic trees*, Logical Methods in Computer Science 17(1), 2021, arXiv:2004.10127, https://arxiv.org/pdf/2004.10127 (first preprint April 22, 2020).
2. David Bradley-Williams and John K. Truss, *On limits of betweenness relations*, arXiv:2108.12904, https://arxiv.org/pdf/2108.12904 (first preprint August 29, 2021).
3. Marc Hellmuth, Anna Lindeberg, Vincent Moulton, *Encoding Phylogenetic Networks with Least Common Ancestor Constraints*, arXiv:2606.16963, https://pdfs.assets.alphaxiv.org/2606.16963v1.pdf (first posted June 15, 2026).
4. Classical tree split compatibility and labelled binary tree enumeration, used only for the reconstruction and counting part after characterizing maximal traces.
