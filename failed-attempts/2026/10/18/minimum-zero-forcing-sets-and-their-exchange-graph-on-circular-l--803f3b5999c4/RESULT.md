# Minimum zero-forcing sets and their exchange graph on circular ladders

## Finding

For every integer \(n\ge 6\), let \(L_n=C_n\square K_2\) be the circular ladder with upper vertices \(u_i\), lower vertices \(v_i\), and edges \(u_i u_{i+1}\), \(v_i v_{i+1}\), \(u_i v_i\), with every subscript in \(\mathbb Z/n\mathbb Z\). A zero-forcing set is an initially black set from which the following rule blackens every vertex: a black vertex having exactly one white neighbor may turn that neighbor black.

**Theorem.** The zero-forcing number is \(Z(L_n)=4\). Moreover, **all** minimum zero-forcing sets, with each graph vertex distinguished, are the disjoint families below. Write \(a_i\) for a vertex in either fixed row and \(b_i\) for the corresponding vertex of the other row.

\[
\begin{array}{ll}
\mathcal A:&\{a_i,a_{i+1},a_{i+2},a_{i+3}\},\\
\mathcal B_{\rm near}:&\{b_i,a_i,a_{i+\varepsilon},a_{i+2\varepsilon}\},\quad\varepsilon\in\{-1,1\},\\
\mathcal B_{\rm far}:&\{b_i,a_i,a_{i+1},a_{i-2}\}\ \text{or}\ \{b_i,a_i,a_{i-1},a_{i+2}\},\\
\mathcal C_{\rm align}:&\{u_i,u_{i+1},v_i,v_{i+1}\},\\
\mathcal C_{\rm shift}:&\{u_i,u_{i+1},v_{i+d},v_{i+d+1}\},\quad d\in\{-1,1\}.
\end{array}
\]

The sizes of these families, in the displayed order, are respectively \(2n,4n,4n,n,2n\). In particular there are exactly \(13n\) minimum zero-forcing sets.

Form the **minimum-set exchange graph** \(\mathcal E(L_n)\): its vertices are the minimum zero-forcing sets, and two are adjacent precisely if their symmetric difference has size two (one initially black vertex is replaced by another while remaining minimum). This graph is **connected**, has exactly \(48n\) edges, and has degree enumerator

\[
\sum_{S\in V(\mathcal E(L_n))}t^{\deg(S)}=4nt^5+8nt^8+nt^{12}.
\]

Thus the five pattern families classify every optimal initial infection set and determine the complete local replacement counts for all circular ladders of circumference at least six.

## Assumptions and scope

The graphs are finite, undirected and simple. The graph \(C_n\) has \(n\) distinct vertices, \(K_2\) has two, and \(n\ge6\). Rows and column indices are fixed, so the result counts vertex-labelled subsets, not orbits under rotations, reflections, or layer exchange. The reconfiguration rule is **token jumping** (the replaced vertices need not be adjacent in \(L_n\)); it is not token sliding. Every intermediate configuration must itself be a minimum zero-forcing set. The asserted degree and edge formulas are for \(n\ge6\). The separate value at \(n=5\) is provided only as a computational boundary check under Verification.

## Proof

**1. A sharp lower bound.** The circular ladder is cubic and triangle-free for \(n\ge6\). Suppose three initially black vertices could start a zero-forcing process. Since every vertex has three neighbors, the first forcing vertex must be black and have two black neighbors. As there are only three black vertices and no triangles, these three induce a path of length two. The unique possible first move blackens the third neighbor of the middle vertex. The resulting black set is the closed neighborhood \(N[x]\) of the middle vertex \(x\). No black vertex now has exactly one white neighbor: \(x\) has none, and each of its three neighbors has two white neighbors, by cubicity and triangle-freeness. Thus three initial vertices cannot force the graph. Fewer cannot either, by monotonicity of forcing. Hence \(Z(L_n)\ge4\).

**2. Exhausting possible four-sets.** Let \(S\) have four vertices. Split into the five possible numbers \(0,1,2,3,4\) lying in the upper row; interchange the two rows whenever convenient.

If all four lie in one row, a first force requires three consecutive black vertices in that row. If the fourth does not extend them to four consecutive vertices, the only first force blackens the opposite-row vertex below the middle of the triple. No vertex can then force again: the triple's ends still have two white neighbors; the newly black vertex has two white neighbors; and the separated fourth vertex cannot help. Thus \(S\) must be in \(\mathcal A\).

Suppose instead that three selected vertices lie in the upper row and the single lower selected vertex is \(v_0\). If \(u_0\) is absent, any initial force can only originate from the middle \(u_c\) of three consecutive upper vertices, blackening \(v_c\). As \(u_0\) is absent, \(c\notin\{0,-1,1\}\); the newly black \(v_c\) is nonadjacent to \(v_0\), and every black vertex has zero or at least two white neighbors. The process stops. Therefore \(u_0\) is present. If neither or both of \(u_{-1},u_1\) is initially black, there is no first force. Hence exactly one is black. Reflecting indices, take \(u_1\) black and \(u_{-1}\) white. Then \(u_0\) first forces \(u_{-1}\). Let \(u_j\) be the third initially black upper vertex. Unless \(j\in\{-2,2\}\), every vertex in the resulting set of five black vertices has zero or at least two white neighbors, so propagation stops. Thus the two possibilities with \(u_1\), and their reflections with \(u_{-1}\), give exactly the four upper triples \(\{u_0,u_1,u_2\}\), \(\{u_0,u_1,u_{-2}\}\), \(\{u_0,u_{-1},u_2\}\), \(\{u_0,u_{-1},u_{-2}\}\). These are precisely \(\mathcal B_{\rm near}\) and \(\mathcal B_{\rm far}\).

Finally suppose two vertices lie in each row. A first force requires an adjacent selected pair in some row and a selected vertex in the opposite row in one of the corresponding two columns. If the selected pair in the other row is nonadjacent, the initial force merely extends the first-row pair at one end and then stops: the other row's two vertices are not adjacent, and another advance would need one of them in the newly reached column, which would make the opposite-row pair adjacent to its already occupied column. If both rows have adjacent selected pairs, an initial force exists exactly when the two pairs occupy at least one common column, namely when their starting columns differ by \(-1,0,1\). These give exactly \(\mathcal C_{\rm align}\) and \(\mathcal C_{\rm shift}\). This proves necessity of the five families.

**3. Every listed pattern forces.** The family \(\mathcal C_{\rm align}\) begins with two adjacent columns fully black. A fully black pair of adjacent columns propagates in both directions around the ladder: at either boundary, each boundary vertex sees an already black horizontal neighbor and its black rung mate, leaving only the next horizontal neighbor white. For a shifted pair \(\mathcal C_{\rm shift}\), one initial propagation round produces further black vertices until two adjacent columns are full. Likewise, a row of four consecutive selected vertices in \(\mathcal A\) first forces opposite-row vertices under the middle two columns, and then completes adjacent rungs.

For \(\mathcal B_{\rm near}\), up to reflection and row exchange the initial set is \(\{v_0,u_0,u_1,u_2\}\). Initially \(u_0\to u_{-1}\) and \(u_1\to v_1\). Then \(v_0\to v_{-1}\) and \(v_1\to v_2\), producing multiple consecutive full columns. For \(\mathcal B_{\rm far}\), the representative is \(\{v_0,u_0,u_1,u_{-2}\}\). The sequence \(u_0\to u_{-1}\), \(u_{-1}\to v_{-1}\), followed by \(v_0\to v_1\) and \(v_{-1}\to v_{-2}\), creates a block of adjacent full columns. In every case the two-column propagation completes the graph. Consequently \(Z(L_n)=4\) and the list is both necessary and sufficient.

**4. Counting and local exchanges.** The five displayed families are disjoint for \(n\ge6\): their row-size and column-offset patterns distinguish them. Rotating indices and interchanging rows gives the claimed counts \(2n,4n,4n,n,2n\).

Two size-four configurations are adjacent in the exchange graph if and only if they share exactly three vertices. Directly comparing the five explicit four-element templates gives the following **complete neighbour-count table**. Each entry is the number of neighbors of a configuration of the row type belonging to the column type; it holds for every \(n\ge6\).

| Type | \(\mathcal A\) | \(\mathcal B_{\rm near}\) | \(\mathcal B_{\rm far}\) | \(\mathcal C_{\rm align}\) | \(\mathcal C_{\rm shift}\) | Total |
|---|---:|---:|---:|---:|---:|---:|
| \(\mathcal A\) | 2 | 4 | 2 | 0 | 0 | 8 |
| \(\mathcal B_{\rm near}\) | 2 | 1 | 2 | 1 | 2 | 8 |
| \(\mathcal B_{\rm far}\) | 1 | 2 | 0 | 1 | 1 | 5 |
| \(\mathcal C_{\rm align}\) | 0 | 4 | 4 | 0 | 4 | 12 |
| \(\mathcal C_{\rm shift}\) | 0 | 4 | 2 | 2 | 0 | 8 |

For reproducibility, here is a direct way to reconstruct every entry without relying on a drawing. Use the representatives
\[
\begin{array}{c|l}
\mathcal A&\{u_0,u_1,u_2,u_3\}\\
\mathcal B_{\rm near}&\{v_0,u_0,u_1,u_2\}\\
\mathcal B_{\rm far}&\{v_0,u_0,u_1,u_{-2}\}\\
\mathcal C_{\rm align}&\{u_0,u_1,v_0,v_1\}\\
\mathcal C_{\rm shift}&\{u_0,u_1,v_1,v_2\}.
\end{array}
\]
For each representative, delete each of its four vertices in turn; insert a single vertex from any of the five templates, and retain the resulting configuration if three vertices agree with the representative. For the integer-offset comparison, all five pattern templates use offsets in \([-2,3]\) from their anchor, and the five representatives occupy columns in \([-2,3]\). Any candidate sharing three vertices with a representative shares at least one, so it has an anchor in \([-5,5]\), and all its columns lie in \([-7,8]\). At \(n\ge16\), these sixteen possible integer columns inject into the cyclic residue set and the table is computed without wrap coincidences. For the finite range \(6\le n\le15\), direct cyclic comparisons give exactly the same table; the accompanying symbolic checker explicitly enumerates every template at these boundaries. Reflecting indices or interchanging rows maps any member of a pattern type to the displayed representative. Thus all rows of the table follow by an exhaustive bounded offset comparison, uniformly for \(n\ge6\).

Therefore \(4n\) states have degree five, \(8n\) have degree eight, and \(n\) have degree twelve. The handshake lemma yields
\[
|E(\mathcal E(L_n))|=\tfrac12(5\cdot4n+8\cdot8n+12\cdot n)=48n.
\]

**5. Connectivity.** Every \(\mathcal B\) pattern exchanges one vertex with some \(\mathcal C\) pattern, and every \(\mathcal A\) pattern exchanges one vertex with a \(\mathcal B_{\rm near}\) pattern. It therefore suffices to connect the \(\mathcal C\) configurations. Write \(C_{i,d}=\{u_i,u_{i+1},v_{i+d},v_{i+d+1}\}\) for \(d\in\{-1,0,1\}\). The valid single exchanges give paths
\[
C_{i,0}\longleftrightarrow C_{i,1}\longleftrightarrow C_{i+1,0}
\]
for every \(i\). They connect the aligned configurations around the complete cyclic index set. Also \(C_{i,-1}\) is adjacent to \(C_{i,0}\). Hence every \(\mathcal C\) configuration, and therefore every minimum zero-forcing set, lies in one connected component.

## Verification

Run `python3 verify_direct.py` and `python3 verify_templates.py` with Python 3 and no third-party dependencies. Both read no external files. Each prints structured JSON to standard output. Saved outputs are `direct_results.json` and `template_results.json`.

The first program constructs graph adjacency independently, exhaustively checks all three-element and four-element subsets for \(5\le n\le13\), generates the theorem's five patterns, and tests exact set equality. It also independently constructs the entire one-vertex exchange graph and checks its degree counts, reciprocal edges and connectivity. In particular, for \(n=6\) it finds 78 states and 288 edges, and for \(n=13\) it finds 169 states and 624 edges. The second program starts instead from the five symbolic pattern families and verifies the complete type-to-type neighbor table, state counts, connectivity and edge counts for all \(6\le n\le50\). Their canonical sorted-state SHA-256 digests agree wherever their ranges overlap.

These finite checks are consistency tests only. The general theorem rests on the case analysis and finite template-overlap argument in the Proof section, not on extrapolating the finite computations. The separately enumerated boundary at \(n=5\) has 65 minimum sets, 280 exchange edges and degree frequencies \(7:20\), \(8:30\), \(12:15\), showing why the degree theorem starts at six.

## Relationship to prior work

The ordinary zero-forcing rule and its connection to minimum rank were introduced in the 2008 AIM Minimum Rank–Special Graphs Work Group paper. The sharp number \(Z(C_n\square K_2)=4\) for \(n\ge4\) is **already known**; it is a special case of the Cartesian-product formula reported in Section 3 of Chilakamarri, Dean, Kang and Yi (2011). Their paper studies propagation rounds, not the enumeration or token-jump exchange of all optimal sets.

Geneson, Haas and Hogben (2020, published 2023) introduce the minimum-zero-forcing-set reconfiguration graph and establish results for paths, cycles, complete graphs, forest connectivity and generic constructions with disconnected reconfiguration graphs. Their forest theorem is inapplicable to circular ladders, which contain cycles. No closed infinite-family description of the present prism exchange graph was found in the inspected sources. The new contribution here is the full classification of \(13n\) optimal subsets and the \(48n\)-edge connected exchange graph with its complete degree counts, not the already-established value four or the generic definition of exchange adjacency.

## Limitations

The exact degree enumerator and edge count are proved only for \(n\ge6\). No claim is made about the shortest exchange distance, radius, diameter, or mixing time. Only ordinary zero forcing and unrestricted one-vertex token jumping are considered; positive semidefinite, skew, connected, and leaky forcing are different models. The work is a mathematical analysis with supporting finite checks; it does not establish independent publication priority. Unindexed or inaccessible literature could contain equivalent classifications.

## References

1. AIM Minimum Rank–Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra and its Applications 428 (2008), 1628–1648. DOI: `10.1016/j.laa.2007.10.009`.
2. K. B. Chilakamarri, N. Dean, C. X. Kang and E. Yi, *Iteration Index of a Zero Forcing Set in a Graph*, first publicly posted 2011-05-08, arXiv:`1105.1492v1`; especially Section 3 on Cartesian products. `https://arxiv.org/abs/1105.1492`.
3. J. Geneson, R. Haas and L. Hogben, *Reconfiguration graphs of zero forcing sets*, first posted 2020-09-01, arXiv:`2009.00220v1`; Discrete Applied Mathematics 329 (2023), 126–139. `https://arxiv.org/abs/2009.00220`.
