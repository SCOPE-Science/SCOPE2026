# Dual mutual-visibility colorings of cycle–clique Cartesian products

## Finding

For each integer \(n\ge5\) and \(m\ge1\), let \(G_{n,m}=C_n\square K_m\). With \(\mathcal V_{\mathrm d}(G;z)=\sum_{M}z^{|M|}\) over all dual mutual-visibility vertex subsets \(M\), including the empty set, one has
\[
\mathcal V_{\mathrm d}(G_{n,m};z)=
\begin{cases}
1+5mz^2,&n=5,\\
1+6mz^2+6\binom m2z^4,&n=6,\\
1,&n\ge7.
\end{cases}
\]
The dual mutual-visibility chromatic number, defined by partition into nonempty dual sets, is
\[
\chi_{\mu_{\mathrm d}}(G_{n,m})=
\begin{cases}
3\lceil m/2\rceil,&n=6,\\
\infty,&n=5\text{ or }n\ge7.
\end{cases}
\]
For \(n=6\), the number of *unordered* optimal partitions of the labelled vertex set into dual sets is
\[
A_m=
\begin{cases}
\binom{2s}{s}(s!)^3,&m=2s,\ s\ge1,\\
2\binom{2s+1}{s}((s+1)!)^3,&m=2s+1,\ s\ge0.
\end{cases}
\]
Consequently the number of optimal assignments using exactly \(3\lceil m/2\rceil\) named colours is \(A_m(3\lceil m/2\rceil)!\).

## Assumptions and scope

All graphs are finite, simple, undirected and unweighted. Write vertices of \(G_{n,m}\) as \((a,i)\), where \(0\le a<m\) is a layer and \(i\in\mathbb Z/n\mathbb Z\) is its cyclic coordinate. Edges are \((a,i)(a,i+1)\) and \((a,i)(b,i)\) for distinct \(a,b\). Thus distances are
\[
d((a,i),(b,j))=d_{C_n}(i,j)+\mathbf1_{a\ne b}.
\]
Vertices \(u,v\) are \(M\)-visible if some *shortest* \(u,v\)-path has no internal vertex in \(M\). A subset \(M\) is **dual mutual-visible** if every pair both in \(M\), and every pair both outside \(M\), is \(M\)-visible. The empty set is dual; a dual colouring partitions all vertices into nonempty dual sets. An empty colour class is never counted. The coefficient of \(z^k\) counts \(k\)-element dual sets, not colours.

## Proof

**1. Cycle restriction.** Each individual \(C_n\) layer is a convex subgraph: two endpoints in the same layer have geodesics using zero interlayer moves. Every two-layer subgraph \(C_n\square K_2\) is also convex: a geodesic between two different layers uses exactly one interlayer move, while any walk through a third layer uses at least two. Restricting a dual set to a convex subgraph preserves the dual property [2, Lemma 2.4]: its relevant shortest paths already lie in the subgraph.

For completeness, the necessary single-cycle classification can be checked directly. If \(x\) belongs to a dual set of \(C_n\) with \(n\ge5\), the unique two-edge geodesic between \(x-1\) and \(x+1\) means at least one of these neighbours must belong to the set; the same geodesic, when both endpoints belong to the set, forbids both. Therefore exactly one cycle neighbour of each selected vertex is selected. Selected vertices form disjoint adjacent pairs. For \(n\ge7\), the exterior vertices \(x-1\) and \(x+2\) around any selected pair \(x,x+1\) have a unique length-three geodesic, containing the selected pair internally, a contradiction. For \(n=5\), two disjoint selected pairs cannot fit with the required two gaps. For \(n=6\), two selected pairs must be separated by single unselected vertices; those two exterior vertices are opposite and both of their geodesics pass through selected vertices. Thus at most one pair remains. Conversely, any adjacent pair is dual in \(C_5,C_6\): deleting it leaves an induced path of \(n-2\) vertices on which the original distances between the remaining vertices are realized. We recover the published spectra [2, Section 4]. Therefore each occupied layer contains exactly one adjacent horizontal pair if \(n=5,6\), and no layer is occupied if \(n\ge7\).

**2. Two-layer compatibility.** In two selected layers call the first cyclic pair \(E_0=\{0,1\}\) and the second \(E_j=\{j,j+1\}\). A cycle reflection \(i\mapsto 1-i\) sends \(j\) to \(-j\), so it suffices to examine \(j=0,1,2\) and, for \(n=6\), \(j=3\). All of \(j=0,1,2\) fail:
- \(j=0\): the selected vertices \((a,0)\) and \((b,1)\) have two length-two geodesics, via \((a,1)\) or \((b,0)\), each with a selected internal vertex.
- \(j=1\): the selected vertices \((a,0)\) and \((b,2)\) have length-three geodesics only through the selected vertices \((a,1)\) or \((b,1)\).
- \(j=2\): the unselected vertices \((a,2)\) and \((b,0)\) have length-three geodesics only through the selected vertices \((a,1)\), \((a,0)\) or \((b,2)\).

For \(n=5\), the reflected cases exhaust all offsets, hence no two layers can be occupied. For \(n=6\), the remaining offset \(j=3\) is valid. This is a fixed twelve-vertex finite lemma supported by the complete **34-row** shortest-path certificate in `prism_certificate.tsv`: with selected set \(\{(a,0),(a,1),(b,3),(b,4)\}\), every pair both inside or both outside the set has a shortest path listed with no selected internal vertices. The length of each listed path equals \(d_{C_6}(i,j)+\mathbf1_{a\ne b}\). There are exactly \(\binom42+\binom82=34\) required pairs, so the certificate is exhaustive. `verify.py` rebuilds the graph from its adjacency definition and checks every row. It also tests the excluded five offsets directly.

**3. Global classification.** Three occupied layers would force the cyclic pair of each of the second and third layers to be antipodal to that of the first, and hence equal to one another, contrary to the two-layer compatibility criterion. Thus a nonempty dual set has at most two occupied layers.

Conversely, a single adjacent pair in one layer, or the compatible four-set in two layers, remains dual after adjoining any number of other complete-factor layers. For vertices of the one or two occupied layers, the requisite geodesic exists inside the convex occupied subgraph by the preceding cases. If exactly one endpoint is in an unoccupied layer, move between layers at the endpoint in an occupied layer and route the cyclic portion entirely within the unoccupied layer. This avoids all selected internal vertices. If endpoints lie in two unoccupied layers, the same argument applies. This exhausts the pairs that require visibility.

There are \(nm\) horizontal adjacent pairs when \(n=5,6\); when \(n=6\), choose two layers and one of six cyclic pairs in the first layer to determine uniquely the antipodal pair in the second. Thus precisely \(6\binom m2\) four-sets appear. No other nonempty dual sets occur, proving the three polynomial formulas.

**4. Colorings and counts.** For \(n\ne6\), the classification prevents a partition: \(n\ge7\) has no nonempty dual set, while at \(n=5\) every class is a horizontal pair and the five vertices of any one layer cannot be covered by disjoint pairs.

For \(n=6\), every partition into dual sets induces a perfect matching by adjacent edges in each cycle layer. There are exactly **two** such matchings, the even phase \(\{01,23,45\}\) and odd phase \(\{12,34,50\}\). A four-element dual colour class joins an edge of one phase with its antipodal edge (shift by three) of the other phase; each edge has one permitted opposite-phase partner in each other layer. If \(a\) layers use the even phase and \(b=m-a\) use the odd phase, at most \(3\min(a,b)\) pairs of edge-tokens can be joined. Each of the \(3m\) initial edge-tokens is a class unless a joining saves one class, so the number of classes is at least
\[
3m-3\min(a,b)=3\max(a,b)\ge3\lceil m/2\rceil.
\]
Choose phases as equally as possible and, separately for each of three antipodal edge types, match every token on a minority-phase layer to a distinct token on a majority-phase layer. This realizes equality.

To count *all* equality partitions, if \(m=2s\) both phases have exactly \(s\) layers; choose the even layers in \(\binom{2s}s\) ways and biject the two phase layer sets independently for each of the three edge types, \((s!)^3\) ways. If \(m=2s+1\), choose which phase has \(s\) layers (two choices), choose those layers in \(\binom{2s+1}s\) ways, and independently inject the \(s\) minority tokens into the \(s+1\) majority tokens in each of three types, \(((s+1)!)^3\) ways. Each choice determines a different unordered vertex-class partition and every optimal partition determines exactly one choice. Multiplying by the factorial of the number of classes gives the named-colour count.

## Verification

The standalone, dependency-free Python file `verify.py` performs graph construction, shortest paths, the dual condition and exact-cover counting from their definitions. Its checks are:
1. For the 12-vertex two-layer \(C_6\) prism, all 34 selected-selected and unselected-unselected pairs are checked against the independent `prism_certificate.tsv` shortest-path witness paths; all six offsets for \(C_6\) and all five offsets for \(C_5\) are tested.
2. Exhaustive enumeration of *all nonempty vertex subsets* for \(n=5,m=1,2,3\); \(n=6,m=1,2,3\); and \(n=7,m=1,2\) agrees with the three formulas, with 36 dual sets in \(C_6\square K_3\).
3. An independently constructed exact-cover recursion over the predicted dual sets yields minimal class counts and unordered optimal partitions for \(m=1,2,3,4,5\), respectively \((3,2),(3,2),(6,48),(6,48),(9,4320)\).

Execute `python3 verify.py prism_certificate.tsv`. The finite checks directly verify the auxiliary prism lemma and sample profiles; the unlimited \(m,n\) conclusions rely on the structural arguments above.

## Relationship to prior work

Babu et al. [1] introduce the dual mutual-visibility chromatic parameter, solve families including complete multipartite block graphs, two-factor Hamming graphs \(K_r\square K_s\), and strong grids, and ask for further finite/infinite classifications. Their inspected preprint does not cover \(C_n\square K_m\). Bujtás, Klavžar and Tian [2] establish the **already known** single-cycle spectra and convex-restriction lemma, which are explicitly used here; those are not claimed as new. The new comparison of selected pairs across distinct complete-factor layers, the restricted nonzero four-set term, the chromatic threshold, and the exact optimal-colouring counts do not follow from the individual-cycle spectra alone. Korže and Vesel [3] treat *ordinary* mutual-visibility sets in Cartesian products of paths and cycles, a weaker property and a different Cartesian factor family.

## Limitations

The theorem concerns only \(n\ge5\) and \(m\ge1\), not triangles/four-cycles or general graph products. Unordered optimal partitions and assignments to distinct named colours have different counts. Literature priority is provisional because searches cannot establish uniqueness and not every historical source is exhaustively indexed. Finite enumeration is not presented as a substitute for the infinite-parameter argument. No independent mathematical audit has been performed.

## References

[1] S. Babu, M. Jakovac, D. Kuziak, A. Lakshmanan S., I. G. Yero, *A variety of the mutual-visibility coloring problem for graphs*, arXiv:2609.31427v1, first submitted 2026-09-25. https://arxiv.org/abs/2609.31427

[2] C. Bujtás, S. Klavžar, J. Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, Aequationes Mathematicae 99 (2025), 1883–1901, DOI 10.1007/s00010-025-01197-y. https://doi.org/10.1007/s00010-025-01197-y

[3] D. Korže, A. Vesel, *Mutual-Visibility Sets in Cartesian Products of Paths and Cycles*, Results in Mathematics 79 (2024), article 116, DOI 10.1007/s00025-024-02139-x. https://doi.org/10.1007/s00025-024-02139-x
