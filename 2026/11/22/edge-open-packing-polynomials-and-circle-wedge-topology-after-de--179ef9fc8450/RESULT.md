# Edge-open packing polynomials and circle-wedge topology after deleting a matching from a biclique

## Finding
For integers \(m,n\ge3\) and \(0\le t\le\min\{m,n\}\), let \(G_{m,n,t}\) be the graph obtained from \(K_{m,n}\) by deleting \(t\) pairwise disjoint edges. An *edge-open packing* is a set of graph edges such that no two of its members have a third, distinct graph edge joining an endpoint of one to an endpoint of the other. Write \(P_{m,n,t}(z)\) for the cardinality polynomial of all such sets (including the empty set) and \(F_{m,n,t}(z)\) for the polynomial of inclusion-maximal such sets. Define
\[
A_d(z)=(1+z)^d-1-dz.
\]
Then the complete, labeled-graph enumerators are
\[
\boxed{\begin{aligned}
P_{m,n,t}(z)={}&1+(mn-t)z+tA_{n-1}(z)+(m-t)A_n(z)\\
 &+tA_{m-1}(z)+(n-t)A_m(z)+\binom t2z^2,\\
F_{m,n,t}(z)={}&t z^{n-1}+(m-t)z^n+t z^{m-1}+(n-t)z^m+\binom t2z^2.
\end{aligned}}
\]
Every inclusion-maximal set is either an entire edge star or a reciprocal two-edge set associated with two deleted matching edges. The maximum size is \(\max\{m,n\}\) when \(t<\min\{m,n\}\), and \(\max\{m,n\}-1\) when \(t=\min\{m,n\}\).

Let \(\Delta_{m,n,t}\) be the simplicial complex with the *edges of* \(G_{m,n,t}\) as vertices and edge-open packings as faces. Its full integral homotopy type is
\[
\boxed{\Delta_{m,n,t}\simeq\bigvee^{(m-1)(n-1)-t+\binom t2}S^1.}
\]
In particular, the reduced integral first homology is free of rank \((m-1)(n-1)-t+\binom t2\), and all other reduced integral homology vanishes.

For balanced shores \(m=n=k\ge6\) and \(2\le t\le k\), inclusion-maximal edge-open packings occur only in sizes \(2,k-1,k\), with whichever of the last two sizes have nonzero coefficients. Thus no size from \(3\) to \(k-2\) occurs: an interval of \(k-4\) missing sizes. The second disjoint edge deletion introduces the first maximal two-edge packing, although maximal stars remain of sizes at least \(k-1\). The first integral Betti number changes by \(t-2\) on passing from \(t-1\) to \(t\) deleted matching edges.

## Assumptions and scope
All graphs are finite, simple, undirected and labelled; all counting treats the original graph-edge identities as distinguishable and does not quotient by automorphisms. Write the shores as \(X=\{x_1,\ldots,x_m\}\) and \(Y=\{y_1,\ldots,y_n\}\), and delete exactly \(x_i y_i\) for \(1\le i\le t\). The graph remains connected and has minimum degree at least two. An inclusion-maximal set need not have maximum cardinality. The empty set is included in \(P\), as standard for a simplicial-complex face polynomial, even though some graph-theoretic definitions require nonempty packings.

A common joining edge must be distinct from both tested packing edges. If tested edges share an endpoint, no third edge of a bipartite graph completes a triangle, so such edges are compatible. If they are disjoint, a joining edge may connect either cross-pair of their endpoints. The homotopy assertion concerns geometric realization of the abstract simplicial complex and uses ordinary (not reduced) \(S^1\) in the wedge notation.

## Proof
**Pair compatibility.** Take distinct edges \(e=x_i y_j\) and \(f=x_k y_\ell\). When \(i=k\) or \(j=\ell\), these edges share an endpoint and, because \(G_{m,n,t}\) is bipartite, have no third distinct edge joining their endpoints: any such edge would form a triangle. When \(i\ne k\) and \(j\ne\ell\), the only potential joining edges are \(x_i y_\ell\) and \(x_k y_j\). Both must be absent for compatibility. Since the only missing edges form the diagonal matching, this happens precisely when \(i=\ell\le t\) and \(k=j\le t\). Thus the *only* compatible disjoint edge pairs are
\[
\{x_i y_j,x_j y_i\}\qquad(1\le i<j\le t).
\]

**Classification.** Any edge-open packing containing a disjoint pair necessarily contains one such reciprocal pair. A third edge compatible with the first must either intersect it or be its unique reciprocal, namely the second edge. If a distinct third edge were compatible with both, it would have to intersect both disjoint edges, and would therefore join their endpoints. The only possible such third edges are the two deleted diagonal edges, which are absent. Hence a packing containing a disjoint pair consists of exactly that pair. Otherwise all packing edges pairwise intersect. In a bipartite graph, a family of two or more pairwise intersecting edges has one common endpoint: after two edges meet at a vertex, any edge meeting both but avoiding that vertex would have to join their other endpoints in the same shore, which is impossible. Thus the packing lies in one vertex star. One-edge sets are also contained in stars.

**Two polynomials.** There are \(mn-t\) distinct one-edge sets. A vertex of the first shore has degree \(n-1\) at the \(t\) matched indices and degree \(n\) otherwise; the analogous degrees of second-shore vertices are \(m-1\) and \(m\). Every star subset of size at least two has a *unique* center and is therefore counted once by the corresponding \(A_d(z)\) term. There are exactly \(\binom t2\) reciprocal two-edge sets; being disjoint, these are distinct from star subsets. This gives \(P\).

A proper subset of a vertex star extends inside that star; a singleton extends because every vertex degree is at least two. Conversely a full star is maximal, as the pair-compatibility classification forbids adding any edge outside it. Reciprocal pairs are already maximal by the preceding argument. The number and sizes of full stars and reciprocal pairs give \(F\). Maximizing their cardinalities yields the stated maximum-size formula. For \(m=n=k\ge6\), the displayed support of \(F\) supplies the claimed missing-size interval, while subtraction of the two Betti formulas gives \(t-2\).

**Integral homotopy.** Let \(\Sigma\) be the subcomplex consisting of all star-subset faces. It is covered by the simplices \(\sigma_v\) indexed by the vertices \(v\) of \(G_{m,n,t}\), where \(\sigma_v\) is the simplex on the edges incident with \(v\). Every \(\sigma_v\) is nonempty and contractible. For two distinct graph vertices, \(\sigma_v\cap\sigma_w\) is a one-vertex simplex exactly when \(vw\) is a graph edge; otherwise it is empty. Every triple intersection is empty, because a graph edge has only two endpoints. The simplicial nerve lemma identifies \(\Sigma\) up to homotopy with the one-dimensional nerve, which is exactly \(G_{m,n,t}\). This graph is connected, with \(mn-t\) edges and \(m+n\) vertices, so
\[
\Sigma\simeq\bigvee^{mn-t-m-n+1}S^1.
\]
Each reciprocal pair contributes precisely one additional one-simplex, whose two endpoint vertices already lie in \(\Sigma\). No face of dimension at least two contains such a pair, by the classification, and the distinct reciprocal pairs give different one-simplices. Attaching a one-simplex between two vertices in a path-connected space adds a free circle up to homotopy. Repeating \(\binom t2\) times therefore gives
\[
\Delta_{m,n,t}\simeq\bigvee^{mn-t-m-n+1+\binom t2}S^1
=\bigvee^{(m-1)(n-1)-t+\binom t2}S^1.
\]
The nerve lemma and edge attachment are homotopy equivalences, not merely rational-homology calculations, so the conclusion is integral.

## Verification
The accompanying `artifacts/check_small.py` enumerates *actual third joining edges* for each candidate pair, then tests every subset of graph edges and each one-edge extension. It checks both polynomial coefficient arrays for 17 parameter triples, independently of the structural classification. The accompanying `artifacts/check_fast.cpp` implements a different subset dynamic program on pair incompatibilities and checks both polynomials for 33 parameter triples; compile with `c++ -O3 -std=c++17 artifacts/check_fast.cpp -o check_fast` and run it. The independent `artifacts/check_topology.py` constructs the small simplicial complexes directly and computes all boundary-matrix ranks over \(\mathbb F_2\), confirming the asserted homology dimensions for six parameter triples. The corresponding `artifacts/*.log` files contain the actual run outputs. These finite experiments do not prove the unrestricted formulas or integral homotopy; those follow from the pair classification and the nerve-lemma argument above.

For an accessible example, \(G_{5,5,2}\) has 225 edge-open packings, 11 inclusion-maximal packings and first Betti number 15. Its maximal packing polynomial is \(z^2+4z^4+6z^5\). For \(G_{k,k,0}\), every inclusion-maximal packing has size \(k\); for \(G_{k,k,2}\), a maximal reciprocal pair of size two appears alongside the large stars.

## Relationship to prior work
Chelladurai, Kalimuthu and Soundararajan introduced edge-open packing and calculated the maximum cardinality for complete multipartite graphs, including \(\rho_e^o(K_{m,n})=\max\{m,n\}\). Their scalar maximum for the undeleted graph is recovered at \(t=0\), but does not specify the deletion-sensitive full set distribution, maximality spectrum or topology. The 2024 work of Brešar and Samadi studies complexity, trees and general one-edge-deletion bounds; those bounds do not determine the cardinality polynomials or the effect of an entire deleted matching. The companion 2024 paper of Brešar, Dravec, Hedžet and Samadi treats trees and graph products, not the matching-deficient biclique packing complex.

A published injective-edge-chromatic result for complete multipartite graphs analyzes partitions into edge-open packing *color classes* for the undeleted class. It gives neither the complete EOP independence polynomial nor the deleted-matching reciprocal faces. An exact dissociation-set classification for the same matching-deleted bicliques imposes an induced-degree condition on selected *vertices*, not edge-open packing on selected *edges*; its polynomials and simplicial complex are different objects. Results for rook graphs and full graph subdivisions address different graph families and are not reductions giving the present theorem. Literature searches under edge-open packing, injective edge-color classes, crown graph, deleted matching, maximal sets and simplicial homotopy did not identify stronger coverage. This search-based assessment is not a proof of historical uniqueness.

## Limitations
Both shores must contain at least three vertices and deleted edges must form a matching. The proofs do not describe arbitrary patterns of missing bipartite edges. The polynomial coefficients count subsets of identifiable graph edges, not isomorphism classes; the homotopy type does not include an equivariant symmetry classification. Finite code checks corroborate, rather than replace, the general proof. Priority remains provisional because scholarly search and repository indexing may omit equivalent unpublished or differently titled work. There has been no independent mathematical validation.

## References
1. G. Chelladurai, K. Kalimuthu and S. Soundararajan, “Edge Open Packing Sets in Graphs,” *RAIRO Operations Research* **56** (2022), 3765–3776, DOI:10.1051/ro/2022171. https://doi.org/10.1051/ro/2022171
2. B. Brešar and B. Samadi, “Edge open packing: complexity, algorithmic aspects, and bounds,” arXiv:2403.00750v1, first posted 2024-03-01. https://arxiv.org/html/2403.00750v1
3. B. Brešar, T. Dravec, J. Hedžet and B. Samadi, “Induced matching vs edge open packing: trees and product graphs,” arXiv:2406.04020v1, first posted 2024-06-06. https://arxiv.org/abs/2406.04020
4. “Correct injective edge chromatic index of complete multipartite graphs,” publicly available mathematical research note (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-correct-injective-edge-chromatic-index-of-complete-multipartite--9f3e4c6f19b5
5. “Dissociation and maximal-set polynomials of bicliques with a deleted matching,” publicly available mathematical research note (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-dissociation-and-maximal-set-polynomials-of-bicliques-with-a-del--ea494ab50b5c
