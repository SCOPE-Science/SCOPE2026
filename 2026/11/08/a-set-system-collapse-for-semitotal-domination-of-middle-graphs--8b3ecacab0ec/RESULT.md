# A set-system collapse for semitotal domination of middle graphs, with exact path-cycle minimizers

## Finding

**Theorem.** Let \(G=(V,E)\) be a finite simple connected graph of order \(n\geq3\). Its middle graph \(M(G)\) has one vertex for each original vertex and one new vertex \(e^*\) for each original edge \(e\); two new vertices are adjacent exactly when their original edges share an endpoint, and \(e^*\) is adjacent to the two endpoints of \(e\). Then **a subset of \(V(M(G))\) is dominating if and only if it is semitotal dominating**. In particular their entire cardinality enumerators coincide, and both equal
\[
\boxed{D_{t2}(M(G);z)=D(M(G);z)=\sum_{F\subseteq E}z^{|F|+n-|V(F)|}(1+z)^{|V(F)|}.}
\]
Here \(V(F)\) denotes the set of original vertices incident with at least one edge of \(F\); the empty set \(F\) is included.

**Complete minimum-set corollary.** For \(P_n\) with \(n\geq3\) or \(C_n\) with \(n\geq3\), every minimum semitotal dominating set of the middle graph is obtained in exactly one of the following ways. When \(n\) is even, use one of the perfect matchings of the original path or cycle, replacing each matching edge by its middle-graph edge-vertex. When \(n\) is odd, either select one original vertex and the edge-vertices of a perfect matching of its complement, or select the edge-vertices of a spanning edge set having degree two at exactly one original vertex and degree one at all others. There are no other minimum sets. Their size is \(\lceil n/2\rceil\), and their respective numbers, on labeled original graphs, are
\[
\boxed{N(P_n)=\begin{cases}1,&n\text{ even},\\ n,&n\text{ odd},\end{cases}\qquad
N(C_n)=\begin{cases}2,&n\text{ even},\\ 2n,&n\text{ odd}.\end{cases}}
\]
The scalar minimum \(\lceil n/2\rceil\) is previously known. The all-set equivalence, all-cardinality formula and complete minimum-set censuses are the asserted extensions.

## Assumptions and scope

All graphs are finite, simple and undirected. For a graph \(H\), a set \(S\subseteq V(H)\) dominates if every vertex outside \(S\) has a neighbor in \(S\). It is semitotal dominating if, additionally, each vertex of \(S\) has a **different** member of \(S\) at graph distance at most two. Thus a singleton cannot be semitotal dominating. The enumerator \(D_{t2}(H;z)\) sums \(z^{|S|}\) over all semitotal dominating sets; \(D(H;z)\) analogously counts all dominating sets. The connectedness and order \(n\ge3\) are required for the all-set statement. In the path-cycle corollary, the original vertices of the path or cycle retain their labels, and there is no division by graph automorphisms.

## Proof

**1. Exact characterization of domination.** Write any selected set in \(M(G)\) uniquely as \(S=A\cup\{e^*:e\in F\}\), with \(A\subseteq V\) and \(F\subseteq E\). An original vertex \(v\notin A\) has neighbors only among the edge-vertices corresponding to original edges incident with \(v\). Consequently it is dominated precisely when \(v\in V(F)\). Thus domination of all original vertices is equivalent to
\[
V\setminus V(F)\subseteq A.
\]
This condition also dominates every middle-graph edge-vertex not in \(S\). Indeed, if \(e^*=uv\notin S\), either an endpoint lies in \(A\), or both endpoints lie in \(V(F)\); in the latter case an edge of \(F\), necessarily different from \(e\), shares an endpoint with \(e\). Such a selected vertex is adjacent to \(e^*\). Hence the displayed containment is necessary and sufficient for domination of \(M(G)\).

**2. The automatic semitotal property.** Suppose \(S\) dominates \(M(G)\). First let \(u\in S\cap V\) be an original selected vertex, and choose any neighbor \(w\) in connected \(G\). If \(w\in S\), the two selected original vertices lie at distance two via \((uw)^*\). Otherwise \(w\notin S\), so some edge \(f\in F\) is incident with \(w\). If \(f=uw\), its selected vertex \(f^*\) is adjacent to \(u\). Otherwise the path \(u,(uw)^*,f^*\) has length two. Thus every selected original vertex has a second selected vertex within distance two.

Now let \(e^*\in S\) correspond to \(e=uv\). Since \(G\) is connected and \(n\ge3\), there exists an original edge \(h=uw\) with \(w\notin\{u,v\}\), after possibly interchanging \(u,v\). The middle vertices \(e^*\) and \(h^*\) are adjacent. If \(h^*\in S\), it is a suitable second selected vertex. If \(h^*\notin S\) but \(w\in S\), then \(e^*,h^*,w\) is a path of length two. Otherwise \(w\notin S\), and domination of \(w\) supplies a selected edge-vertex \(f^*\) for some edge \(f\) incident with \(w\). When \(f=h\), this is the adjacent selected vertex \(h^*\); when \(f\ne h\), the path \(e^*,h^*,f^*\) has length two. In every case \(e^*\) has a distinct selected vertex within distance two. Therefore every dominating set is semitotal. The converse holds by definition.

**3. Exact cardinality enumerator.** Fix the selected middle edge-vertices \(F\subseteq E\). By Step 1, all \(n-|V(F)|\) uncovered original vertices are forced into \(A\); the \(|V(F)|\) covered original vertices may be selected independently. The corresponding generating function is \(z^{|F|+n-|V(F)|}(1+z)^{|V(F)|}\). Distinct edge subsets \(F\) produce disjoint classes of dominating sets. Summing over \(F\subseteq E\) and applying Step 2 proves the displayed polynomial identity.

**4. Optimal paths and cycles.** Every selected original vertex covers only itself among the original vertices; every selected edge-vertex covers only its two original endpoints. Thus a dominating set of the middle graph of \(P_n\) or \(C_n\) has at least \(\lceil n/2\rceil\) members. Selecting edge-vertices from a minimum edge cover of the path or cycle meets the bound. By Step 2 it is semitotal.

For \(n=2k\), a selected set of size \(k\) has capacity at most \(2k=n\) original vertices, so equality forces \(k\) pairwise disjoint selected original edges and no selected original vertices. These edges constitute a perfect matching. The labeled path has one perfect matching; the labeled even cycle has two.

For \(n=2k+1\), a selected set of size \(k+1\) has total original-vertex coverage capacity \(2k+2-r=n+1-r\) if it contains \(r\) original vertices. Therefore \(r\le1\). If \(r=1\), every incidence is needed: the remaining selected edge-vertices form a perfect matching on the other \(2k\) original vertices. Deleting a vertex from the odd path leaves such a matching if and only if its position is odd (\(k+1\) choices); deleting any one vertex from the odd cycle leaves a path with a unique perfect matching (\(n\) choices). If \(r=0\), the \(k+1\) selected original edges cover all vertices with exactly one repeated endpoint. Thus their spanning subgraph has degree two at exactly one vertex and degree one elsewhere. The repeated vertex must have an even position in the odd path (\(k\) choices); its position is arbitrary in the odd cycle (\(n\) choices). Once the repeated vertex is fixed, every edge in the cover is forced by alternation. The two types are disjoint, yielding \(k+(k+1)=n\) for odd paths and \(n+n=2n\) for odd cycles. All configurations dominate by Step 1 and are semitotal by Step 2, completing the classification.

## Verification

The accompanying standard-library Python 3 program `verify.py` enumerates all dominating sets of middle graphs for every connected labeled simple root on three, four, and five vertices (\(4+38+728=770\) roots), plus 234 further connected roots on six or seven vertices. For each root it checks the semitotal condition separately and checks every cardinality coefficient against Step 3, totalling 1,004 connected root instances. It independently exhausts all candidate minimum-size selected sets for paths and cycles with \(3\le n\le12\), comparing them to the structural classification. It checks the excluded two-vertex boundary \(M(K_2)\), where the middle edge-vertex by itself dominates but has no semitotal partner. The program terminates with `VERIFY_OK` when all assertions pass. This finite verification corroborates but does not replace the proof for all orders.

## Relationship to prior work

Kazemnejad, Pahlavsay, Palezzato and Torielli, *Domination number of middle graphs* (arXiv:2008.02975, first submitted 2020-08-07), prove the scalar identity between middle-graph domination and original-graph edge-cover number, and give scalar values for paths and cycles. Their inspected manuscript does not present the all-set semitotal equivalence, the cardinality enumerator above, or the complete minimum-set counts. Cabrera-Martínez, López-Carmona, Rios-Villamar and Serrano-Díaz, *On the (independent) semitotal domination in subdivision, middle, and central graphs* (arXiv:2609.33932, first submitted 2026-09-27), prove that **minimum independent dominating sets** of a middle graph are semitotal and establish the corresponding scalar minimum. Their Theorem 2.2 does not assert that **every, possibly nonindependent, dominating set** is semitotal, nor enumerate all sets. Their published proof motivates, but does not logically supply, Step 2 for arbitrary dominating sets. The earlier classical literature on independent domination and middle graphs was considered; some plausible older sources were not available in full text, so priority remains provisional.

## Limitations

The all-set collapse requires connected simple roots with at least three vertices. It fails for \(G=K_2\): the unique middle edge-vertex by itself dominates \(M(K_2)\) but is not semitotal. The polynomial expression is a finite sum over edge subsets, not a claim of a polynomial-time algorithm for general roots. The explicit minimum-set counts concern paths and cycles; other families may require further analysis. The scalar domination parameters and the path-cycle minimum sizes were previously known. The result has not received independent mathematical validation. Possible unindexed or inaccessible earlier all-set identities remain a historical-priority risk.

## References

1. A. Cabrera-Martínez, J. L. López-Carmona, I. Rios-Villamar and A. Serrano-Díaz, *On the (independent) semitotal domination in subdivision, middle, and central graphs*, arXiv:2609.33932 (2026), https://arxiv.org/abs/2609.33932.
2. F. Kazemnejad, B. Pahlavsay, E. Palezzato and M. Torielli, *Domination number of middle graphs*, arXiv:2008.02975 (2020), https://arxiv.org/abs/2008.02975.
3. R. B. Allan and R. C. Laskar, *On domination and independent domination numbers of a graph*, Discrete Mathematics (1978), https://doi.org/10.1016/0012-365X(78)90105-X (bibliographic record; full text not inspected).
4. E. J. Cockayne, S. T. Hedetniemi and D. J. Miller, *Properties of Hereditary Hypergraphs and Middle Graphs*, Canadian Mathematical Bulletin (1978), https://doi.org/10.4153/CMB-1978-079-5 (bibliographic/abstract only; full text not inspected).
