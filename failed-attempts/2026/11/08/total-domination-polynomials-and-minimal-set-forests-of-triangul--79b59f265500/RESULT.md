# Total-domination polynomials and minimal-set forests of triangular graphs

## Finding

For every integer \(n\ge3\), write \(T_n=L(K_n)=J(n,2)\) for the triangular graph. Let \(A_n(z)\) count all total dominating vertex sets of \(T_n\) by cardinality, and let \(M_n(z)\) count those that are inclusion-minimal. A total dominating set requires every vertex, including every selected vertex, to have a distinct neighbor in the set. Set

\[
H(x,z)=x\bigl(e^{zx+z^2x^2}-1-zx-z^2x^2\bigr)-\frac12z^3x^4.
\]

Then the following identities hold as formal power series in \(x\) with polynomial coefficients in \(z\):

\[
\boxed{M_n(z)=n![x^n]\left(e^{z^2x^3/2}+x e^{H(x,z)}\right)}
\]

and

\[
\boxed{A_n(z)=n![x^n](1+x)e^{-x-zx^2/2}
\sum_{j\ge0}(1+z)^{\binom j2}\frac{x^j}{j!}.}
\]

Every inclusion-minimal total dominating set has an exact structural description. Identify its selected vertices with an edge set \(F\subseteq E(K_n)\). The selected-edge graph \(([n],F)\) is either (i) a vertex-spanning disjoint union of three-vertex paths, or (ii) a forest with precisely one isolated vertex, whose other components are trees obtained from one center by attaching paths of length one or two, with at least two arms. The representations of a four-vertex path by a center are not unique, but the unrooted forest classification is unique.

For \(n\ge4\), the attainable sizes of inclusion-minimal total dominating sets are exactly

\[
\boxed{\operatorname{supp}M_n=\left\{\left\lfloor\frac{2n}{3}\right\rfloor,
\left\lfloor\frac{2n}{3}\right\rfloor+1,\ldots,n-2\right\}.}
\]

For \(n=3\), the support is \(\{2\}\). Consequently the lower total domination number, previously known, is \(\lfloor2n/3\rfloor\), while the upper total domination number is \(n-2\) for \(n\ge4\). For \(n\ge7\), the number of inclusion-minimal total dominating sets attaining the upper value is

\[
\boxed{[z^{n-2}]M_n(z)=n![t^{n-2}]e^{t+t^2}
= n!\sum_{q=0}^{\lfloor(n-2)/2\rfloor}\frac{1}{q!\,(n-2-2q)!}.}
\]

For example, \(M_6(z)=840z^4\), \(M_7(z)=630z^4+3402z^5\), \(M_8(z)=13440z^5+18536z^6\), and \(M_9(z)=277200z^6+93816z^7\).

## Assumptions and scope

Graphs are finite, undirected, simple, and labeled. Two selected vertices of \(T_n\) are adjacent precisely when their corresponding base edges of \(K_n\) share an endpoint. Inclusion-minimality means deletion of any single selected vertex destroys total domination; the condition is monotone, so this is equivalent to inclusion-minimality among all total dominating sets. The displayed generating functions count labeled subsets, not isomorphism classes. The coefficient operator \([x^n]\) extracts the ordinary coefficient in the indicated formal series.

## Proof

**1. Feasibility in the base graph.** Associate to a selected vertex set of \(T_n\) the selected-edge graph \(G_F=([n],F)\). Every edge of \(K_n\) has a selected *distinct* adjacent edge if and only if (a) at most one base vertex is isolated in \(G_F\), and (b) \(G_F\) has no connected component isomorphic to \(K_2\). Indeed, two isolated base vertices create an undominated edge joining them. A \(K_2\)-component supplies a selected edge with no selected neighboring edge. Conversely, if these obstructions are absent, every unselected edge has at least one endpoint incident with a selected edge, and every selected edge has a distinct selected edge meeting one endpoint.

**2. A minimal feasible edge graph is a forest.** If \(G_F\) contained a cycle, deleting any edge of that cycle would preserve the set of nonisolated base vertices and the connectedness of its former component. This produces neither an additional isolated base vertex nor a \(K_2\)-component, contradicting inclusion-minimality. Hence every minimal \(G_F\) is a forest.

**3. No unused base vertex.** All tree components have at least three vertices, by feasibility. If one component has at least four vertices, deleting a leaf edge isolates at most one base vertex and leaves each nontrivial component with at least two edges, so feasibility persists. Therefore all components are three-vertex paths. Conversely, deleting either edge of any such path creates a \(K_2\)-component, so their union is inclusion-minimal. Such a union exists precisely when \(3\mid n\).

**4. Exactly one unused base vertex.** Deleting a leaf edge from any other component creates a second isolated base vertex, so every leaf edge is essential. Deleting an internal (nonleaf) edge produces no new isolated base vertices; it destroys feasibility precisely when it produces a \(K_2\)-component. In a tree this occurs if and only if one endpoint of the deleted edge has degree two and its other neighbor is a leaf. Call such an endpoint a bud. Thus every internal edge must be incident with a bud.

The subgraph induced by nonleaf vertices of a tree is connected. Every bud has at most one neighbor in that subgraph; when that subgraph has more than one vertex, the bud is its leaf. Since every edge of this subgraph touches a bud, its non-bud vertices are pairwise nonadjacent, and there is at most one such vertex unless the entire subgraph is a single edge with both endpoints buds. Accordingly, the original tree consists of a center with arms of lengths one or two. The only ambiguity in the choice of center occurs for the four-vertex path, whose two internal vertices both qualify. Reversing these observations proves sufficiency as well as necessity.

**5. Counting the minimal structures.** A three-vertex path has three labeled realizations, so its connected-component contribution to a labeled exponential generating function is \(3z^2x^3/3!=z^2x^3/2\). An arbitrary set of these components yields the first term \(e^{z^2x^3/2}\). A centered subdivided star contributes a factor \(x\) for its center. Each length-one arm contributes \(zx\), and each length-two arm contributes \(z^2x^2\): its two new labels occupy distinguishable positions along the arm. The arms form an unordered set containing at least two arms, giving \(x(e^{zx+z^2x^2}-1-zx-z^2x^2)\). The four-vertex path is counted twice; since there are \(4!/2\) labeled copies, subtracting exactly one copy contributes \(-z^3x^4/2\). This is \(H(x,z)\). A set of such tree components together with one isolated base vertex has generating function \(x e^{H(x,z)}\), proving the formula for \(M_n\).

**6. Counting all feasible structures.** The labeled exponential generating function of all simple graphs, where \(x\) records vertices and \(z\) edges, is \(\sum_{j\ge0}(1+z)^{\binom j2}x^j/j!\). Decomposing into connected components, then forbidding singleton components and two-vertex edge components, multiplies this function by \(e^{-x-zx^2/2}\). Restoring the possibility of exactly one singleton multiplies by \(1+x\). Step 1 proves the stated formula for \(A_n\).

**7. Sizes and upper coefficient.** In case (ii), if \(c\) nontrivial tree components cover \(n-1\) vertices, then \(|F|=(n-1)-c\), where \(1\le c\le\lfloor(n-1)/3\rfloor\). Every such \(c\) occurs: take \(c-1\) disjoint three-vertex paths and one star on the remaining at least three vertices. Thus all integers from \(n-1-\lfloor(n-1)/3\rfloor=\lfloor2n/3\rfloor\) to \(n-2\) occur. When \(3\mid n\), the vertex-spanning three-vertex-path case contributes cardinality \(2n/3\), the already attained lower endpoint for \(n\ge6\); for \(n=3\) it is the sole case. Finally, for \(n\ge7\), cardinality \(n-2\) forces exactly one nontrivial tree on \(n-1\ge6\) vertices and one isolated vertex. The center is then unique, and its arm decomposition is counted by \(n![t^{n-2}]e^{t+t^2}\), as claimed.

## Verification

The standalone file `verify.py` independently constructs the adjacency graph \(L(K_n)\), tests the open-neighborhood total-domination predicate on edge-subset bit masks, and checks inclusion-minimality by deleting every selected vertex. Its separate labeled-component recurrence evaluates both displayed polynomials. All subsets were tested for \(3\le n\le7\), and every candidate up to the rigorously proved upper minimal size was checked for \(n=8\). In total 2,630,165 subsets were tested. The full and minimal polynomials agree on their overlapping tested domains; an exact-arithmetic recurrence also checks the size spectrum and upper coefficient through order 30. Run `python3 verify.py` from the directory containing the supplied file.

## Relationship to prior work

Total edge domination of \(K_n\) is equivalent to total vertex domination of its line graph \(T_n\). The scalar minimum \(\lfloor2n/3\rfloor\) already appears in Velammal and Arumugam (2012), Theorem 2.3, and is not claimed to be new. Pan, Yang, Li, and Xu (2019) study complexity and tree algorithms; Henning, Pandey, Sharma, and Tripathi (2024) study further graph-class algorithms. General minimal-total-domination enumeration methods are known, including Kanté, Limouzy, Mary, and Nourine (2014). A prior special-order calculation also gives a number of minimum total dominating sets when \(n\equiv1\pmod3\); that special coefficient is recovered here, not claimed separately. The contribution here is the complete component classification and all-cardinality exponential generating functions, along with the entire upper-size distribution and consecutive support description.

## Limitations

This is an exact statement for triangular graphs, not a characterization of minimal total dominating sets of arbitrary line graphs. Computational checks at finitely many orders support but do not prove the infinite identities; the arguments above provide the proof. A literature search did not identify an equivalent complete census, but does not establish publication priority; unindexed or inaccessible sources remain a risk. No independent mathematical audit has been carried out.

## References

1. S. Velammal and S. Arumugam, “Total edge domination in graphs,” *Elixir Discrete Mathematics* 44 (2012), 7213–7217; https://www.elixirpublishers.com/articles/1681456907_201203027.pdf, Theorem 2.3.
2. Z. Pan, Y. Yang, X. Li, and S.-J. Xu, “The complexity of total edge domination and some related results on trees,” arXiv:1910.02431, first version 2019-10-06; https://arxiv.org/abs/1910.02431.
3. M. A. Henning, A. Pandey, G. Sharma, and V. Tripathi, “Algorithms and hardness results for edge total domination problem in graphs,” *Theoretical Computer Science* 982 (2024), 114270; DOI:10.1016/j.tcs.2023.114270.
4. M. M. Kanté, V. Limouzy, A. Mary, and L. Nourine, “On the Enumeration of Minimal Dominating Sets and Related Notions,” *SIAM Journal on Discrete Mathematics* 28 (2014), 1916–1929; DOI:10.1137/120862612.
5. O. Favaron and M. A. Henning, “Upper total domination in claw-free graphs,” *Journal of Graph Theory* 44 (2003), 148–158; DOI:10.1002/jgt.10134.
