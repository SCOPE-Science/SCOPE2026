# Minimal connected domination of fully subdivided complete graphs

## Finding
For every integer \(n\ge3\), let \(H_n\) be the graph obtained by subdividing each edge of the labelled complete graph \(K_n\) exactly once. Write \(V=\{1,\ldots,n\}\) for the old vertices and \(s_{uv}\) for the degree-two vertex replacing edge \(uv\). A connected dominating set (CDS) is a nonempty set whose induced subgraph is connected and whose closed neighborhood is all of \(V(H_n)\). It is *inclusion-minimal* if no proper subset is also a CDS.

**Classification.** The inclusion-minimal CDSs of \(H_n\) are precisely the sets
\[
D(v,w,T)=(V\setminus\{v\})\cup\{s_{ab}:ab\in E(T)\}\cup\{s_{vw}\},
\]
where \(v\in V\), \(w\in V\setminus\{v\}\), and \(T\) is an arbitrary spanning tree of the complete graph on \(V\setminus\{v\}\). The parametrization is one-to-one. Every inclusion-minimal CDS has exactly \(2n-2\) vertices, and their complete cardinality enumerator is
\[
\boxed{\mathcal M_{H_n}(z)=n(n-1)^{n-2}z^{2n-2}.}
\]
In particular, the minimum and maximum sizes of inclusion-minimal CDSs coincide:
\[
\gamma_c(H_n)=\Gamma_c(H_n)=2n-2.
\]
Here \(\Gamma_c\) denotes the maximum size of an inclusion-minimal CDS (not the maximum size of an arbitrary CDS).

## Assumptions and scope
All graphs are finite, simple and undirected. The labels of old vertices distinguish the members of the families; each subdivision vertex corresponds to a unique unordered pair of old vertices. The theorem covers every \(n\ge3\) and no assertion is made about other base graphs or about subdividing an edge more than once. Since the complete graph has no nonadjacent old vertices, \(H_n\) also equals the *central graph* \(C(K_n)\) under the usual definition of central graph. This equivalence is relevant when comparing sources.

## Proof
Let \(D\) be an arbitrary CDS, \(X=D\cap V\), and \(Y=\{uv:s_{uv}\in D\}\). No singleton dominates \(H_n\) for \(n\ge3\): an old vertex misses every other old vertex, while a subdivision vertex misses all but its two old endpoints and is not adjacent to the other subdivision vertices. Thus \(|D|\ge2\).

**At most one old vertex is omitted.** If distinct old vertices \(u,v\) were outside \(D\), the subdivision vertex \(s_{uv}\), whose only neighbors are \(u,v\), would have to lie in \(D\) to be dominated. It would be isolated in \(H_n[D]\), contradicting connectivity because \(|D|\ge2\). Therefore \(|V\setminus X|\le1\).

**No minimal CDS contains every old vertex.** If \(X=V\), the set \(Y\) must connect all original vertices; otherwise the bipartite induced subgraph \(H_n[D]\) would be disconnected. If \((V,Y)\) has a cycle, deleting the subdivision vertex of any edge of that cycle preserves connectivity and domination, contradicting minimality. If \((V,Y)\) is a tree, choose a leaf \(v\) of that tree. Deleting the original vertex \(v\) preserves connectivity: the unique selected subdivision vertex incident to \(v\) remains attached to its other endpoint. It also preserves domination: \(v\) itself is adjacent to that selected subdivision vertex, and each unselected subdivision vertex incident to \(v\) remains adjacent to its other old endpoint, which is selected. Thus a CDS containing all old vertices is never minimal.

**Exactly one omitted old vertex.** Write \(X=V\setminus\{v\}\). Every selected subdivision vertex has at least one end in \(X\). Those corresponding to edges within \(X\) must connect \(X\), because vertices corresponding to edges incident to the omitted \(v\) are leaves in \(H_n[D]\). Hence \(T'=(X,Y\cap\binom X2)\) is connected. To dominate the omitted old vertex \(v\), \(D\) contains at least one subdivision vertex \(s_{vw}\) with \(w\in X\). If \(T'\) has a cycle, the subdivision vertex on a cycle edge may be deleted. If two distinct subdivision vertices of edges incident to \(v\) are selected, one may be deleted, since both are leaves and the other still dominates \(v\). Inclusion-minimality therefore forces \(T'\) to be a spanning tree and exactly one selected subdivision vertex incident to \(v\). This gives the asserted form.

**Sufficiency and inclusion-minimality.** For any \((v,w,T)\) as specified, \(H_n[D(v,w,T)]\) is the subdivision of the tree \(T\) with one pendant subdivision vertex \(s_{vw}\) attached to \(w\), so is connected. It dominates \(v\) through \(s_{vw}\), and dominates every unselected subdivision vertex because every original edge has at least one endpoint other than \(v\), hence an endpoint in \(X\). Now suppose \(D'\subseteq D(v,w,T)\) were a CDS. By the first paragraph, \(D'\) contains at least \(n-1\) old vertices. Since \(D(v,w,T)\) has exactly those \(n-1\) old vertices, \(D'\) contains all of \(X\). To connect these old vertices, \(D'\) must contain the subdivision vertices of all \(n-2\) edges of \(T\), since \(T\) is their sole selected connecting structure. To dominate \(v\), it must contain \(s_{vw}\), the sole selected neighbor of \(v\). Thus \(D'=D(v,w,T)\), proving inclusion-minimality without assuming that one-vertex deletion checks are sufficient in general.

Finally, the omitted vertex \(v\), pendant endpoint \(w\), and tree \(T\) are recoverable uniquely from \(D\). There are \(n\) choices for \(v\), \(n-1\) choices for \(w\), and, by Cayley's tree formula, \((n-1)^{n-3}\) spanning trees on the \(n-1\) remaining labelled vertices, with the formula valid also when \(n=3\). Hence the number is \(n(n-1)^{n-2}\), and the cardinality is \((n-1)+(n-2)+1=2n-2\). QED.

## Verification
Run the standalone Python 3 program `verify.py` from the same package: `python3 verify.py`. It constructs \(H_n\) directly, checks closed-neighborhood domination, induced-subgraph connectivity, and vertex-deletion minimality independently of the spanning-tree construction, and compares the resulting families with those generated using Prüfer codes. Exhaustive checks cover all nonempty vertex subsets for \(n=3,4,5,6\), a total of \(2{,}131{,}004\) candidate subsets. All \(54{,}432\) classified sets for \(n=7\) additionally pass direct connectivity, domination, and individual-vertex essentiality checks (without an exhaustive converse for \(n=7\)). Counts are respectively \(6,36,320,3750,54432\) for \(n=3,4,5,6,7\). Finite checks are not a proof of the unrestricted claim; the proof above supplies that.

## Relationship to prior work
Abu-Khzam, Fernau, Gras, Liedloff, and Mann (2022) develop general algorithms for enumerating minimal connected dominating sets, including on 2-degenerate graphs, and extremal lower-bound constructions. Those results provide the general context and do not give this exact classification or Cayley-type count for fully subdivided complete graphs in the examined manuscript. Fujita, Kazemnejad, and Pahlavsay (2022) study domination numbers of *central graphs*, which includes \(H_n=C(K_n)\), but their parameter is ordinary domination rather than connected domination or the enumeration of inclusion-minimal connected dominating sets. The star/leaf properties of trees and Cayley's formula are classical ingredients, not presented as new facts. The claim is the derived, exact all-minimal-CDS classification and its cardinality enumerator.

## Limitations
The priority assessment is conditional on accessible literature and does not establish that no unindexed or differently named equivalent result exists. The classification is restricted to once-subdivided complete graphs; it does not imply a general formula for all central graphs, arbitrary subdivisions, or arbitrary incidence graphs. The computational verification checks only finite orders and does not constitute independent mathematical review.

## References
1. F. Abu-Khzam, H. Fernau, B. Gras, M. Liedloff, K. Mann, *Enumerating Connected Dominating Sets*, arXiv:2205.00086, first posted 2022-04-29; conference version *Enumerating Minimal Connected Dominating Sets*, ESA 2022, DOI:10.4230/LIPIcs.ESA.2022.1, published 2022-09-01. https://arxiv.org/abs/2205.00086
2. S. Fujita, F. Kazemnejad, B. Pahlavsay, *New classification of graphs in view of the domination number of central graphs*, arXiv:2204.10292, first posted 2022-04-20. https://arxiv.org/abs/2204.10292
3. F. Kazemnejad, B. Pahlavsay, *Domination Number of Central Graphs*, publicly distributed preprint, 2021; ordinary domination results for \(C(K_n)\). (Historical comparison only; no priority or full-text claim on connected domination.)
4. A. Cayley, *A theorem on trees*, Quarterly Journal of Mathematics 23 (1889), 376–378 (classical labelled spanning-tree count).
