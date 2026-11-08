# First token-slide fragmentation for minimum locating-total codes on \(C_3\square C_n\)

## Finding
For \(G_n=C_3\square C_n\), \(n\ge3\), let \(\mathcal M_n\) denote the family of minimum locating-total dominating sets. Its token-jump graph exchanges one selected vertex for any unselected vertex; its token-slide graph permits the exchange only across an edge of \(G_n\). Every intermediate set must again be minimum locating-total dominating.

The earliest two members of this family have sharply different minimum-set mobility. For \(n=3\), the minimum size is four, \(|\mathcal M_3|=81\), and the token-slide graph is connected (198 edges, radius five, diameter six). For \(n=4\), the minimum size is five and \(|\mathcal M_4|=120\). Its token-jump graph is connected (468 edges, radius and diameter five), but its token-slide graph has the exact isomorphism type
\[
\mathcal R^{\mathrm{slide}}_4\cong 4(C_3\square C_6)\sqcup6C_8.
\]
Thus \(n=4\) is the smallest parameter in this natural family for which minimum-code token-slide reachability is disconnected while token-jump reachability remains connected. There are ten token-slide components and 192 undirected slide transitions; four components have 18 vertices each and six have eight each.

## Assumptions and scope
Every graph is finite, simple, undirected and vertex-labeled. The vertices of \(G_n\) are pairs \((c,r)\) with \(c\in\mathbb Z/n\mathbb Z\), \(r\in\mathbb Z/3\mathbb Z\); adjacency holds when the column agrees and the row differs, or when the row agrees and columns are consecutive cyclically. A set \(S\) is *locating-total dominating* when \(N(v)\cap S\ne\varnothing\) for all vertices \(v\), and \(N(u)\cap S\ne N(v)\cap S\) for every pair of distinct vertices \(u,v\notin S\). Its minimum cardinality is \(\gamma_t^L(G_n)\). Here a token move replaces exactly one selected vertex by one unselected vertex. A slide additionally requires the removed and added vertices to be adjacent in \(G_n\). All counts refer to labeled sets, with no quotient by automorphisms. Only \(n=3\) and \(n=4\) are asserted.

## Proof
The proof is a finite exhaustive certificate, not an extrapolation to larger cycles. Label \((c,r)\) by the integer \(3c+r\). For a bitmask \(s\) of length \(3n\), take its one-bits to be \(S\), and form the bitmask \(\sigma_s(v)=N(v)\cap S\) for each vertex. A candidate is valid precisely if every \(\sigma_s(v)\) is nonzero and the signatures \(\sigma_s(v)\) for vertices \(v\notin S\) are pairwise distinct. These conditions are equivalent to the definition by direct substitution.

The independent algorithms in `verify_exhaustive.py` and `verify_independent.cpp` enumerate all \(2^{3n}\) masks, increasing cardinality until the first valid size; there are respectively \(512\) and \(4096\) total masks at the two values of \(n\). Both find first valid cardinalities four and five, with respectively 81 and 120 such masks. No set of smaller size is skipped.

For each two distinct minimum masks, the programs insert a token-jump edge exactly when the symmetric difference consists of one bit deleted and one bit inserted; a token-slide edge is inserted when those positions are adjacent in the original graph. Connected components are found by complete graph traversal. Exhaustive shortest-path searches from every vertex establish the stated radii and diameters; the machine-readable certificate is checked against all 120 states and all 192 slide edges.

More precisely, `isomorphism_certificate.json` assigns to each slide-graph vertex a component identifier and a coordinate in either a cyclic eight-vertex system or the Cartesian coordinate set \(\mathbb Z/3\mathbb Z\times\mathbb Z/6\mathbb Z\). The checker verifies (i) a bijection in every component; (ii) every slide transition maps to an edge of the specified model; and (iii) the edge total is 192, equal to the model total \(6\cdot8+4\cdot36\). Since all model edges have images and no others occur, these are graph isomorphisms. The four 18-vertex models are \(C_3\square C_6\), while the remaining six are \(C_8\). The independent implementation confirms the state counts, transitions, connectivity, and component edge sizes without using that certificate.

## Verification
Run `python3 verify_exhaustive.py` in the directory containing its coordinate certificate. Compile `verify_independent.cpp` with `c++ -std=c++17 -O2 verify_independent.cpp -o check` and execute `./check`. No external Python packages are needed. `verify_exhaustive.log` and `verify_independent.log` capture the actual outputs. The two programs use independent state representations: Python combinations and set intersections versus C++ bit masks and vertex-neighborhood integer operations. The final isomorphism mappings are finite checkable witnesses rather than references to hidden computations.

## Relationship to prior work
Xing and Sohn's 2014 study gives the previously known locating-total domination number of \(C_3\square C_n\): it equals \(n\) for multiples of six and \(n+1\) otherwise. In particular, the scalar answers four and five used here are not new. Its illustrated constructions and arguments determine minimum size, whereas the present statement evaluates the complete optimal-state mobility graph at the first two values, including the exact graph isomorphism types. The first theorem on general realizability of locating-total reconfiguration graphs by Mynhardt and Teshima does not imply which graph occurs for a fixed Cartesian product. Both the general jump/slide model and the minimum-size parameter predate this computation. Search evidence is described in the review artifact. The claim does not include any general formula for \(n\ge5\).

## Limitations
The finite enumeration proves exactly the graph assertions for the two stated inputs. It gives no complete formula for future values of \(n\). The two implementations share mathematical definitions, so they are not independent scholarly certification. Historical priority may be affected by unindexed computations. A few pages of a relevant 2014 primary article were retrievable only as images, and one internal page was unavailable during inspection; no assertion of complete noncoverage from unread material is made.

## References
1. H. Xing and M. Y. Sohn, “Bounds on locating-total domination number of the Cartesian product of cycles,” *Ars Combinatoria* 113A (2014), 139–146. Public full-text PDF: https://combinatorialpress.com/article/ars/Volume%20113-A/volume-113-A-paper-12.pdf .
2. M. Y. Sohn, “Bounds on Locating total Domination Number of the Cartesian Product Graphs,” ICNAO2013 public conference abstract (meeting December 20–22, 2013): https://icnao2013-math.nsysu.edu.tw/var/file/190/1190/img/1727/Abstracts_ICNAO2013.pdf .
3. C. M. Mynhardt and L. E. Teshima, “A note on some variations of the \(\gamma\)-graph,” arXiv:1707.02039 (2017), Section 3: https://arxiv.org/abs/1707.02039 .
4. M. A. Henning and N. Jafari Rad, “Locating-total domination in graphs,” *Discrete Applied Mathematics* 160 (2012), 1986–1993. https://doi.org/10.1016/j.dam.2012.04.004 .
