# One-token mobility of optimal paired domination in triangular graphs

## Finding
For every integer \(m\ge1\), put \(n=3m+1\) and let \(T_n=L(K_n)\) be the triangular graph. Its vertices are the two-element subsets of \([n]\); two vertices are adjacent when the subsets intersect. A paired-dominating set is a dominating vertex set whose induced subgraph has a perfect matching. Define \(\mathcal R_m\) to have the minimum paired-dominating sets of \(T_n\) as vertices, with two sets adjacent if one selected vertex is replaced by an **adjacent** unselected vertex of \(T_n\), preserving minimum paired domination.

**Theorem.** The paired-domination number is \(\gamma_{\rm pr}(T_n)=2m\). Every minimum paired-dominating set consists of the \(2m\) edges of \(m\) vertex-disjoint, two-edge paths in \(K_n\), together covering all but one ground vertex. Consequently the number of minimum configurations is
\[
N_m=\frac{(3m+1)!}{2^m m!}.
\]
The one-token-slide reconfiguration graph \(\mathcal R_m\) is connected, vertex-transitive and \(4m\)-regular. It has exactly
\[
|E(\mathcal R_m)|=2mN_m
\quad\text{and}\quad
\#\{\text{triangles of }\mathcal R_m\}=\frac{2mN_m}{3}.
\]
Each configuration lies in exactly \(m\) three-cycles consisting of fixed-triple center changes and exactly \(m\) three-cycles consisting of fixed-center hole changes. These are all triangles.

The optimum-state count and the disjoint-path classification are included to specify the objects, **not asserted as historically new**. The proposed contribution is the exact **one-selected-vertex** slide structure: connectivity under this stricter move, degree, edge count, and two-family triangle census.

## Assumptions and scope
Graphs are finite, undirected, loopless and simple. A selected vertex in \(T_n\) represents one edge of the ground complete graph \(K_n\). A legal token slide changes **one** of the \(2m\) selected vertices of \(T_n\), replacing its corresponding ground edge by an intersecting ground edge. This is different from replacing one whole induced-matching edge of \(T_n\), which changes two selected vertices simultaneously. All counts treat ground labels \([n]\) as distinct and do not identify configurations under automorphisms. The range is precisely \(n\equiv1\pmod3\), \(n\ge4\); no conclusions for other residues are asserted here.

## Proof
**1. Lower bound and equality structure.** Let \(S\) be a paired-dominating set with \(|S|=2r\), and choose a perfect matching of the graph induced by \(S\). Each matched pair comprises two incident edges of \(K_n\), touching exactly three ground vertices. Let \(U\subseteq[n]\) be the set of all ground endpoints used by \(S\). Since \(S\) dominates \(L(K_n)\), at most one ground vertex is outside \(U\): two omitted vertices would define a ground edge with no neighbor in \(S\). Thus \(n-1\le|U|\le3r\), so \(r\ge m\) when \(n=3m+1\). Conversely, select \(m\) disjoint ground triples, choose a center in each triple, and select its two incident edges; leave one ground vertex unused. This set dominates \(T_n\) and induces \(mK_2\), hence is paired-dominating of size \(2m\).

If equality \(r=m\) holds, then \(|U|=3m\), forcing the \(m\) matched pairs to use pairwise disjoint ground triples. Each pair is therefore a two-edge path with a uniquely determined center. In particular, the perfect matching of \(T_n[S]\cong mK_2\) is unique. Choose the unused ground label, partition the remaining \(3m\) labels into unordered triples, then choose a center in each triple. This counts
\[
(3m+1)\frac{(3m)!}{(3!)^m m!}3^m=\frac{(3m+1)!}{2^m m!}=N_m.
\]

**2. Exhaustive classification of legal one-token slides.** Fix an optimum with unused ground vertex \(h\). For each path block let its center be \(c\) and leaves be \(a,b\); the two selected vertices of \(T_n\) are the ground edges \(ca\) and \(cb\). Delete one of these ground edges, say \(ca\). All other path blocks and the retained edge \(cb\) remain selected. Because the new optimum must again be disjoint two-edge paths with one unused ground vertex, the newly inserted edge must share one endpoint with \(cb\), have its other endpoint among \(a,h\), and have no endpoint in any other block. The possibilities other than the old edge are \(ab\), \(ch\), and \(bh\); the first two intersect the deleted edge \(ca\) and are legal one-token slides, whereas \(bh\) does not intersect \(ca\) and is a jump but not a slide. By symmetry the same holds when deleting \(cb\). Therefore each path block gives exactly four legal slides: exchange its center with either leaf (without changing the covered triple), or exchange either leaf with the unused vertex (without changing the center). These four outputs are distinct. Thus \(\mathcal R_m\) is \(4m\)-regular.

**3. Connectivity.** Introduce \(3m+1\) labelled positions: a hole position \(h\), and \((c_i,a_i,b_i)\) for each of the \(m\) blocks. Consider the fixed *position graph* with edges \(c_i a_i,c_i b_i,ha_i,hb_i\) for every \(i\). It is a bouquet of \(m\) four-cycles meeting at \(h\), hence connected. Place the distinct ground labels \([n]\) bijectively on these positions. An adjacent-position swap exchanges either center and leaf or hole and leaf; by Step 2 it induces exactly one legal token slide. Any two bijective position labellings are connected by edge transpositions on a connected graph: these transpositions generate the full symmetric group on the positions (for example, transposition along a path can be obtained by conjugating successive adjacent swaps). Every minimum paired-dominating set has a position labelling, possibly more than one because blocks and their leaves are unlabelled. Hence every two optimum sets are joined by a legal slide path. Permuting the ground labels acts transitively on the optimum configurations and preserves the slide relation, so \(\mathcal R_m\) is vertex-transitive.

**4. Edges and triangles.** The handshake lemma gives \(|E(\mathcal R_m)|=4mN_m/2=2mN_m\). For a fixed block, the three choices of its center on a fixed triple form one three-cycle through the current state; similarly the three choices of the unused vertex among the current two leaves and hole, holding the block center fixed, form one three-cycle through that state. Hence every state belongs to at least \(2m\) triangles.

There are no others: in a triangle of equal-cardinality selected sets, the two neighbors of any one state must either delete the same selected vertex or insert the same new vertex (otherwise the neighbors differ in two deletions and two insertions and cannot be adjacent). The two legal insertions available after deleting a fixed selected ground edge are a leaf-leaf edge and a center-hole edge; they are disjoint ground edges, so the resulting states are not adjacent in \(T_n\). Thus the deletion cannot be common. For a common insertion, it must replace the two different edges of the **same** block; edges in different blocks are disjoint in \(K_n\) and could not be exchanged by a slide. The only ground edges that give two such legal moves are the two leaves joined (a center-change triangle) or the center joined to the hole (a hole-change triangle). Thus each state belongs to exactly \(2m\) triangles, of \(m\) each type. Double-counting their three vertices yields \(2mN_m/3\) triangles.

## Verification
The file `verify_direct.py` independently constructs the triangular graph from ground edges, searches all candidate selected subsets, checks ordinary domination and existence of a perfect matching, and forms the legal **one-vertex** slide graph. It verifies the theorem at \(m=1\) and \(m=2\) (\(n=4,7\)), including the complete triangle count. The file `verify_slots.py` separately traverses the labelled-slot state space by elementary swaps, for \(m=1,2,3\), and checks exact counts, degrees, edge totals, and connectivity. Run with `python3 verify_direct.py` and `python3 verify_slots.py`; expected terminal outputs are included as `verify_direct.out` and `verify_slots.out`.

In particular, the two methods both give \(N_1=12\), \(N_2=630\), and degree \(4\) or \(8\); the slot traversal gives \(N_3=75600\), degree \(12\) and \(453600\) edges. The finite checks illustrate and stress-test the proof, but cannot replace its infinite-family argument.

## Relationship to prior work
Haynes and Slater introduced paired domination. Dutton and Brigham established foundational domination relationships for a graph and its line graph, including bounds and observations for complete-graph line graphs. Mynhardt and Teshima defined and studied slide-adjacency reconfiguration of minimum paired-dominating sets in general graphs. Studer, Haynes and Lawson studied the stronger *induced-paired* condition (not the same condition imposed here).

A previous mathematical classification of maximum induced matchings in triangular graphs already gives the \(m\)-disjoint-triple count and connectivity for **whole-matching-edge** moves, in which both endpoints of one induced matching edge are replaced. We do not claim either the optimal-state count or that prior connectivity as new. Those results do not imply connectivity under the strictly finer **single-selected-vertex** replacement of the present theorem. The proof here directly classifies those moves, identifies a connected position-swap graph, and derives a different degree and triangle census. Searches identified no exact published or indexed covering result for this single-vertex slide graph; this is a qualified priority assessment, not a proof of universal novelty.

## Limitations
The classification is restricted to triangular graphs on \(3m+1\) ground vertices. No exact diameter formula, classification of other congruence classes, or independent scholarly validation is claimed. Some relevant early full texts were unavailable or accessible only as scanned pages; the published priority question remains open to further archival checking. The large-state test at \(m=3\) is a complete traversal of the predicted slot model, whereas direct unstructured subset enumeration was performed only at \(m=1,2\).

## References
1. T. W. Haynes and P. J. Slater, “Paired-domination in graphs,” *Networks* **32** (1998), 199–206. DOI: `10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F`. First online publication: 1998-12-07.
2. R. D. Dutton and R. C. Brigham, “A Note on Relations Between a Graph and Its Line Graph Which Involve Domination Concepts,” *Journal of Combinatorial Mathematics and Combinatorial Computing* **31** (1999), 161–168. `https://combinatorialpress.com/article/jcmcc/Volume%20031/vol-31-paper%2012.pdf`.
3. D. S. Studer, T. W. Haynes, and L. M. Lawson, “Induced-Paired Domination in Graphs,” *Ars Combinatoria* **57** (2000), 111–128. `https://combinatorialpress.com/article/ars/Volume%20057/volume-57-paper-11.pdf`.
4. C. M. Mynhardt and L. E. Teshima, “A note on some variations of the \(\gamma\)-graph,” arXiv:1707.02039 (first submitted 2017-07-07), `https://arxiv.org/pdf/1707.02039`.
