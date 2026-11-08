# Geodetic bases of triangular graphs: parity, exact counts, and slide mobility

## Finding
For every integer \(n\ge3\), let \(T_n=L(K_n)\), with each vertex of \(T_n\) identified with one unordered pair from \([n]\). A geodetic set is a vertex subset whose pairwise shortest-path intervals cover \(V(T_n)\).

**All-set criterion.** A set \(S\subseteq V(T_n)\) is geodetic if and only if its corresponding edge set \(F\subseteq E(K_n)\) spans all \(n\) ground vertices, has no isolated vertex, and no ground vertex is adjacent in \(([n],F)\) to two or more vertices of degree one. Equivalently, the graph \(([n],F)\) has minimum degree at least one and contains no two leaves with a common neighbor.

**Exact minimum and complete classification.** For even \(n\ge4\), the minimum size is \(n/2\), and the minimum sets correspond exactly to the perfect matchings of \(K_n\). For odd \(n\ge3\), the minimum size is \((n+3)/2\), and the minimum sets correspond exactly to the edge-disjoint unions
\[
K_3\sqcup\frac{n-3}{2}K_2
\quad\text{and, if }n\ge5,\quad
P_5\sqcup\frac{n-5}{2}K_2,
\]
with all components on disjoint ground-vertex sets. Consequently the number \(b_n\) of minimum sets is
\[
b_n=\begin{cases}
\dfrac{n!}{2^{n/2}(n/2)!},&n\text{ even},\\[4pt]
\binom n3\dfrac{(n-3)!}{2^{(n-3)/2}((n-3)/2)!}
+60\binom n5\dfrac{(n-5)!}{2^{(n-5)/2}((n-5)/2)!},&n\text{ odd},
\end{cases}
\]
where the second summand is zero when \(n=3\).

**Mobility.** Construct the graph of minimum geodetic sets, where an edge represents replacement of one selected vertex by one unselected vertex that preserves minimum geodeticity. Under token *jumping* any replacement is allowed; under token *sliding* the removed and inserted vertices must be adjacent in \(T_n\) (the two corresponding ground edges must intersect). When \(n\) is even, both reconfiguration graphs are edgeless. When \(n\) is odd, both are connected (including the singleton case \(n=3\)). For odd \(n\), the jump degree of each triangle-type state is \(6(n-3)\), and that of each path-type state is \(4n-10\); the corresponding slide degrees are \(6(n-3)\) and \(2n-2\). Thus their total edge counts are exactly half the sums of these degrees weighted by the two type counts above.

## Assumptions and scope
All graphs are finite, simple, undirected, and unweighted. The shortest-path interval \(I(u,v)\) contains every vertex lying on at least one shortest \(u\)-\(v\) path, including endpoints. The label set \([n]\) has distinct elements; counts distinguish labelled configurations. The terms \(K_3\), \(K_2\), and \(P_5\) denote a triangle, one edge, and the path on five vertices, respectively. Components mentioned in the classification are *components of the chosen-edge graph*, not components of \(T_n\).

## Proof
**1. Geodesic criterion.** The graph \(T_n\) has diameter at most two. Two distinct ground edges are adjacent as vertices of \(T_n\) exactly when they intersect. A ground edge \(ab\notin F\) lies in a length-two geodesic between selected edges exactly when there are \(ax,by\in F\) with \(x\ne y\). Such edges are disjoint, and \(ax,ab,by\) is a geodesic. Because \(ab\notin F\), neither \(x=b\) nor \(y=a\). If some ground vertex \(a\) is isolated in \(([n],F)\), every omitted edge at \(a\) fails this test. If every vertex has positive degree, the test fails for an omitted edge \(ab\) only when \(N_F(a)=N_F(b)=\{x\}\), i.e., \(a\) and \(b\) are distinct degree-one vertices attached to the same neighbor. This proves the all-set equivalence in both directions.

**2. Minimum size.** The absence of isolated ground vertices gives the edge-cover lower bound \(|F|\ge\lceil n/2\rceil\). For even \(n\), equality forces a perfect matching, which meets the criterion. For odd \(n=2k+1\), equality at \(k+1\) edges would force an edge cover consisting of a single three-vertex path and \(k-1\) isolated edges: its two path leaves share a neighbor, so it is not geodetic. Thus \(|F|\ge k+2\). A triangle plus \(k-1\) disjoint edges meets the criterion and has \(k+2\) edges.

**3. Every odd-order equality case.** Let \(n=2k+1\), \(|F|=k+2\), and \(c\) be the number of nontrivial connected components of \(([n],F)\). Because components have at least two vertices, \(c\le k\); because the cycle rank \(|F|-n+c\) is nonnegative, \(c\ge k-1\). If \(c=k\), the cycle rank is one and the sum of component vertex surpluses \(\sum_C(|V(C)|-2)\) is one. Therefore one component is a triangle and all others are isolated edges. If \(c=k-1\), the graph is a forest and that sum is three. Any three-vertex tree component is forbidden, because its two leaves share their neighbor. Hence all the surplus three belongs to one five-vertex tree, which must be a five-vertex path: the other trees on five vertices each contain a vertex with at least two leaf neighbors. Every other component is an edge. These are exactly the stated types; the triangle case also covers \(n=3\).

**4. Count.** An even-order perfect matching has \(n!/(2^{n/2}(n/2)!)\) possible labelled realizations. For odd \(n\), choose three ground vertices for the unique triangle, then perfectly match the remainder. Alternatively choose five vertices for the unique path, choose one of the \(5!/2=60\) unoriented Hamilton paths on them, and perfectly match the remainder. The two types are disjoint and each realization is unique, proving the formula.

**5. Reconfiguration and degrees.** For even \(n\), deleting an edge of a perfect matching isolates its two endpoints, and inserting a different single edge cannot cover both. Every minimum configuration is frozen for either rule. For odd \(n\), let \(m=(n-3)/2\) be the number of disjoint edge components outside a triangle. A legal move must delete one triangle edge; its deletion creates two leaves with a common neighbor. Inserting an edge between one of these two leaves and either endpoint of one of the \(m\) external edge components produces a five-vertex path. There are \(3\cdot2\cdot2m=12m=6(n-3)\) choices, all slides.

For a path-type configuration with selected path edges \(12,23,34,45\) and \((n-5)/2\) additional disjoint edges, direct inspection within the path's five vertices gives exactly ten legal one-edge replacements, eight of which replace an edge by an incident edge. The ten replacements for this labelled path are: \(12\to15\), \(23\to13,15,25,35\), \(34\to13,14,15,35\), and \(45\to15\); precisely the two replacements \(23\to15\) and \(34\to15\) are jumps but not slides. Involving one external edge component \(ab\), the only possible deletions are \(23\) and \(34\): the three-vertex path left on one side of the deletion must be joined from one of its two leaves to \(a\) or \(b\). This gives eight jumps per external edge, four of which are slides. Consequently the jump and slide degrees are \(10+8(n-5)/2=4n-10\) and \(8+4(n-5)/2=2n-2\).

**6. Slide connectivity for all odd orders.** Every path-type configuration slides to a triangle-type one: for a path \(a-b-c-d-e\), replace \(bc\) by \(ce\), obtaining the triangle on \(c,d,e\) and edge \(ab\). To move one triangle vertex \(a\) into a matched pair \(de\), keeping other components fixed, perform these three slides:
\[
\{ab,bc,ac,de\}
\to\{ab,bc,cd,de\}
\to\{ae,bc,cd,de\}
\to\{ae,bc,cd,bd\}.
\]
The initial five-ground-vertex configuration is \(K_3\sqcup K_2\), both middle states are \(P_5\), and the final state is \(K_3\sqcup K_2\) with triangle \(bcd\) and matched pair \(ae\). Thus any chosen member of the triangle may be transposed with any member of any matched pair. These transpositions allow the triangle to be moved to any ground triple and, using a triangle vertex as a temporary buffer, allow endpoints of two distinct matching edges to be swapped while restoring the triangle. Hence every triangle-plus-matching partition is reachable from every other. Token-sliding connectivity follows; token-jumping connectivity follows because every slide is a jump. The unique \(n=3\) configuration is trivially connected.

## Verification
The independent program `check_direct.py` builds graph distances and shortest-path intervals in \(T_n\), tests every vertex subset of size below the asserted minimum, and checks both the geodetic criterion and exact basis counts for all \(3\le n\le8\). The separate program `check_structure.py` constructs the described matchings, triangles and five-vertex paths without using shortest-path intervals, confirms the labelled counts through \(n=9\), and enumerates every jump/slide neighbor and connected component for \(3\le n\le7\). Both programs use only Python's standard library. Expected exact outputs are provided with the two scripts, and are not substituted for executing them.

## Relationship to prior work
The classical notion of a geodetic set is due to Chartrand, Harary, and Zhang and related earlier work. Chartrand, Harary, and Zhang (2002, first online 2001) give general bounds and constructions for geodetic numbers, not this classification. Goudar, Ashalatha, Venkatesha, and Muddebihal (2012), Theorem 3.12, discuss \(L(K_n)\) explicitly but give a much larger general upper bound; their paper supplies neither the sharp parity-dependent minimum nor the complete state census. Ashalatha, Goudar, and Venkatesha (2013) treat *non-split* geodetic sets, requiring extra connectivity of the complement of the selected set; their Theorem 3.11 again supplies an upper bound for \(L(K_n)\), not the present minimum-set or reconfiguration theorem. Strong-geodetic variants and geodetic sets of complete multipartite graphs are different graph/condition pairs, so their bounds do not imply the conclusions here.

## Limitations
The theorem concerns exactly the ordinary vertex-geodetic condition on triangular graphs \(L(K_n)\) and the two specified single-token replacement rules; it does not determine diameters of the odd-order relocation graphs or classify edge-geodetic and strong-geodetic bases. The finite programs verify only the labelled ranges stated; the infinite-family claims rest on the written structural proof. Literature and database searches cannot exclude every unpublished, unindexed, or hard-to-access earlier observation, so priority should be independently assessed before publication.

## References
- G. Chartrand, F. Harary and P. Zhang, “Geodetic sets in graphs,” *Discussiones Mathematicae Graph Theory* 20 (2000), 129–138, DOI 10.7151/dmgt.1112. The available metadata verifies the year but not a first-public calendar day.
- G. Chartrand, F. Harary and P. Zhang, “On the geodetic number of a graph,” *Networks* 39 (2002), 1–6, DOI 10.1002/net.10007, first published online 2001-11-16.
- V. M. Goudar, K. S. Ashalatha, Venkatesha and M. H. Muddebihal, “On the Geodetic Number of Line Graph,” *International Journal of Contemporary Mathematical Sciences* 7 (2012), 2289–2295, https://m-hikari.com/ijcms/ijcms-2012/45-48-2012/goudarIJCMS45-48-2012.pdf.
- K. S. Ashalatha, V. M. Goudar and Venkatesha, “Non Split Geodetic Number of a Line Graph,” *Global Journal of Science Frontier Research* 13 (2013), https://journalofscience.org/index.php/GJSFR/article/view/103300; page states published 2013-10-30.
