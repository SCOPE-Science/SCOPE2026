# Four consecutive Rips barcode dimensions for mixed three- and five-edge theta graphs

## Finding

For integers \(p\ge2\) and \(q\ge1\), let \(G_{p,q}\) have two poles \(u,v\), exactly \(p\) internally vertex-disjoint paths of length three between the poles, and exactly \(q\) additional internally vertex-disjoint paths of length five. No other edges are present. Equip its \(2+2p+4q\) vertices with intrinsic unweighted graph distance. The **complete inclusive Vietoris–Rips homotopy filtration**, at all real thresholds \(r\ge0\), is

\[
\operatorname{VR}_{\le r}(G_{p,q})\simeq
\begin{cases}
\bigsqcup^{2+2p+4q}\{*\},&0\le r<1,\\
\bigvee^{p+q-1}S^1,&1\le r<2,\\
\bigvee^{p-1}S^2\vee\bigvee^qS^1,&2\le r<3,\\
\bigvee^q S^3,&3\le r<4,\\
\{*\},&r\ge4.
\end{cases}
\]

The **complete reduced integral persistence barcode** is: \(2p+4q+1\) copies of \([0,1)\) in degree zero; \(p-1\) copies of \([1,2)\) and \(q\) copies of \([1,3)\) in degree one; \(p-1\) copies of \([2,3)\) in degree two; and \(q\) copies of \([3,4)\) in degree three. All other reduced homology vanishes, and the listed integral groups have no torsion. In particular, a mixed family of overlapping six- and eight-cycles passes successively through nonzero integral homology in dimensions one, two, and three.

## Assumptions and scope

All input graphs are finite, simple, connected, undirected, and have unit edge lengths. A Rips simplex is a **nonempty set of graph vertices** whose diameter in shortest-path distance is at most the inclusive parameter \(r\), with no factor-of-two scaling. Each of the \(p+q\) pole-to-pole paths is internally disjoint from every other. The two arm lengths are precisely three and five. The theorem does not assert the same barcode for other arm lengths or for continuous metric-graph points on edges.

## Proof

**1. Scales zero and one.** The graph has \(2+2p+4q\) vertices and \(3p+5q\) edges. Its girth is six, so its scale-one Rips complex is the graph itself. Its first Betti number is therefore \((3p+5q)-(2+2p+4q)+1=p+q-1\), and all \(2p+4q+1\) reduced connected-component classes die at scale one. The graph metric takes integer values, so the filtration is constant between integers.

**2. A relative collapse for adjoining a sufficiently long ear at scale two.** We first prove the following structural lemma, which also specifies the relevant homotopy maps. If \(H\) is any finite connected simple graph with distinguished \(u,v\) satisfying \(d_H(u,v)\ge3\), and an internally disjoint \(u\)-to-\(v\) path \(P_\ell\) with \(\ell\ge4\) edges is added, then

\[
\operatorname{VR}_{\le2}(H\cup P_\ell)
\searrow \operatorname{VR}_{\le2}(H)\cup P_\ell
\simeq \operatorname{VR}_{\le2}(H)\vee S^1.
\]

To prove the collapse, label the added path \(x_0=u,x_1,\ldots,x_{\ell-1},x_\ell=v\). No route through its whole length can introduce a threshold-two edge between old vertices. A route between two internal path vertices that uses the old graph through the poles has length at least five, so the induced Rips complex on the path is precisely the clique complex of its square, with maximal faces \(\{x_i,x_{i+1},x_{i+2}\}\). A mixed edge involving an old non-pole vertex must join \(x_1\) to a neighbor of \(u\), or \(x_{\ell-1}\) to a neighbor of \(v\). Consequently the complete Rips complex is the union of the two induced subcomplexes and the two simplices

\[
\Delta(N_H[u]\cup\{x_1\}),\qquad
\Delta(N_H[v]\cup\{x_{\ell-1}\}).
\]

For each nonempty subset \(T\subseteq N_H(u)\), in decreasing order of size, remove the elementary free-face pair \((\{x_1\}\cup T,\{u,x_1\}\cup T)\). Similarly remove the pairs at \(v\). The old closed neighborhoods are disjoint, since \(d_H(u,v)\ge3\), so these collapses have no conflicting cofaces. The remaining complex is the union of the old Rips complex with the path-square clique complex. For \(0\le i\le\ell-2\), remove the free edge \(\{x_i,x_{i+2}\}\) together with its unique triangle \(\{x_i,x_{i+1},x_{i+2}\}\). This leaves exactly the old Rips complex with the ordinary attached path. Since the old complex is connected and the attached path meets it in exactly the two endpoints, adjoining this path adds one circle up to homotopy. All removals are genuine elementary simplicial collapses and preserve the old complex.

**3. Scale two for the mixed theta family.** Begin with the \(p\) length-three paths alone. Put \(A=\{a_i\}\) and \(B=\{b_i\}\) for their first and second internal-vertex layers. The scale-two Rips complex is exactly

\[
S^0*\left(\Delta(A)\cup\Delta(B)\cup\bigcup_{i=1}^p[a_i,b_i]\right),
\]

where \(S^0\) consists of the two poles. The parenthesized complex is homotopy equivalent to two points connected by \(p\) parallel edges, hence to \(\bigvee^{p-1}S^1\); its suspension is \(\bigvee^{p-1}S^2\). Adding the \(q\) length-five paths successively, the old poles remain at distance three, so Step 2 adds exactly \(q\) circles and leaves the old two-dimensional classes intact. Thus the scale-two homotopy type is \(\bigvee^{p-1}S^2\vee\bigvee^qS^1\).

**4. Removing redundant short arms at scale three.** In the third power of \(G_{p,q}\), the closed neighborhoods of every pair \(a_i,a_j\) are identical; the same holds for every pair \(b_i,b_j\). Indeed, all short-arm vertices lie at mutual distance at most three, and distances from any \(a_i\) (respectively any \(b_i\)) to vertices on a long arm depend only on the position within that arm, not on \(i\). The standard dominated-vertex fold therefore gives a simplicial collapse of the scale-three clique complex onto the induced subcomplex with just one length-three arm and all \(q\) long arms. Distances among the remaining vertices coincide with those in this smaller graph, since every omitted short arm provides an alternative pole-to-pole path of the same length three. Write this smaller graph as \(G_{1,q}\).

**5. Removing all interactions between distinct long arms.** Let \(Y_j\) be the eight vertices of the \(j\)-th long arm together with the single retained short arm, and put \(K_j=\operatorname{VR}_{\le3}(Y_j)\), using distances from \(G_{1,q}\). Each induced subgraph on \(Y_j\) is an eight-cycle; its distance-three Rips complex has exactly four missing edges, the disjoint antipodal pairs. Therefore

\[
K_j\cong (S^0)^{*4}\cong S^3.
\]

Every two \(K_j\) intersect in exactly the full tetrahedron on the four short-arm vertices. We claim that the entire scale-three Rips complex of \(G_{1,q}\) **simplicially collapses onto** \(K_1\cup\cdots\cup K_q\).

Label the four internal vertices of long arm \(j\) by \(z_{j,1},\ldots,z_{j,4}\), in pole-to-pole order. Two vertices on *distinct* long arms are within distance three exactly for position pairs

\[
(1,1),(1,2),(2,1),(3,4),(4,3),(4,4).
\]

Hence any face outside the proposed union meets at least two long arms, and all its long-arm vertices lie either in the **near-\(u\)** positions \(1,2\), or in the **near-\(v\)** positions \(3,4\). These alternatives are mutually exclusive. A near-\(u\) face has a position-one vertex and cannot contain \(v\); every one of its vertices, including the short-arm vertices, is within distance three of \(u\). Pair each such face not containing \(u\) with the face obtained by adjoining \(u\). Dually, pair near-\(v\) faces not containing \(v\) with their extensions by \(v\). Every face outside the union appears in exactly one pair, and both members remain outside the union. Process pairs in descending cardinality of the lower face. All other cofaces of a lower face are strictly larger external faces and have already been removed, so each indicated pair is an elementary free-face collapse. The two classes of pairs cannot interfere because a face meeting two long arms cannot mix their near-\(u\) and near-\(v\) regions. This proves the claimed relative collapse for every \(q\ge1\).

The union \(K_1\cup\cdots\cup K_q\) consists of \(q\) three-spheres attached along their common contractible tetrahedron. Collapsing that common tetrahedron to a point is a homotopy equivalence, yielding \(\bigvee^qS^3\). This proves the radius-three homotopy statement **integrally** and for all \(p,q\) in the stated range.

**6. Radius four and complete persistence maps.** A first internal vertex \(a_1\) on any short arm is at distance at most four from every graph vertex: its distances to positions \(1,2,3,4\) on every length-five arm are at most \(2,3,4,3\), respectively. Therefore the threshold-four Rips complex, and every subsequent one, is a cone. The inclusion from threshold one to threshold two is surjective on integral first homology: every distance-two edge can be replaced by an original length-two path across a Rips triangle. Hence precisely \(p-1\) of the \(p+q-1\) original first-homology classes die at two, while \(q\) survive until three; the kernel is primitive since the quotient is free abelian. No degree-two class exists before scale two or after scale two; all \(p-1\) classes there have interval \([2,3)\). All \(q\) degree-three classes first appear at scale three and die at four. Together with Step 1 this proves every claimed integral barcode and the absence of unlisted intervals or torsion.

## Verification

Two standalone scripts, `verify_mixed_theta.py` and `verify_five_arm.py`, use only the Python standard library. The first checks the exact scale-two relative collapse for 63 attachments, with 2,510 validated elementary free-face pairs, and checks 28 mixed-length homology instances over \(\mathbb F_2\). The second independently rebuilds all radius-three simplices in nine mixed three/five-arm cases with \(2\le p\le4\) and \(1\le q\le3\), verifies the short-arm dominated-vertex collapses, checks all external face pairs and their free-face conditions, and confirms the octahedral-boundary decomposition and radius-four cone. The second script checks 768 external cross-arm faces across these nine cases, and independently computes the complete mod-two Betti ranks at radius three. Run both programs in the package directory; outputs appear in `verification_output.txt`. These are finite reproducible checks; the six-step argument is the unrestricted proof.

## Relationship to prior work

The motivating graph-metric Rips classification of torus grids by Adams and collaborators [1] concerns square torus graphs rather than two-terminal theta graphs. Adamaszek [2, Proposition 2.2] proves a stability collapse when girth is at least \(3r+1\); the present graphs have girth six, and the radius-three stage is beyond this condition. His computations for powers of individual cycles do recover the individual eight-cycle factor but do not supply their simultaneous overlapping gluing.

The general metric-gluing theorems of Adamaszek and collaborators [3, Theorems 8 and 10] do not imply the critical radius-three collapse here: taking one long arm as a gluing piece, the Rips triangle \(\{a_1,z_{j,1},z_{j,4}\}\) is pairwise within distance three, but **neither pole** is within distance three of all its vertices. Thus the unique nonempty gluing-intersection-extension hypothesis of Theorem 8 fails. Their Theorem 10 requires a common short path meeting a one-third-loop bound, which the three-edge short path of an eight-cycle does not meet. These are concrete statement-level comparisons, not merely title differences.

An exact published result for the *all-length-three* parallel-path family [4] yields a contractible radius-three complex, whereas the present mixed family has precisely \(q\) independent three-spheres at that radius. The earlier edge-disjoint-hexagon theorem [5] also does not apply to the many six-cycles sharing short arms here. The individual cycle computation [2] covers \(q=1,p=1\), but not the arbitrary \(p\ge2,q\ge1\) mixed-dimensional filtration or the uniform cross-arm collapse. A broader unindexed equivalent theorem remains a possible literature-overlap risk.

## Limitations

The theorem is restricted to the two exact arm lengths three and five, to finite simple unit-weight graph metrics on vertices, and to the inclusive Rips convention. It neither classifies arbitrary mixed path lengths nor describes equivariant representations, non-vertex metric-graph Rips complexes, or other families of girth-six graphs. The literature comparison is best-knowledge rather than a proof of global uniqueness. Independent mathematical audit has not been performed.

## References

[1] H. Adams, A. Y. Adetowubo, H. Barriga-Acosta, Z. Feng, and J. Sterling, *Vietoris–Rips complexes of torus grids*, arXiv:2502.07134, first public 2025-02-10, https://arxiv.org/abs/2502.07134.

[2] M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, https://arxiv.org/abs/1104.0433.

[3] M. Adamaszek and collaborators, *Vietoris–Rips and Čech complexes of metric gluings*, SoCG 2018, DOI:10.4230/LIPIcs.SoCG.2018.3, https://doi.org/10.4230/LIPIcs.SoCG.2018.3.

[4] *Complete Vietoris–Rips persistence and symmetry of three-edge theta graphs*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-vietoris-rips-persistence-and-symmetry-of-three-edge-th--c282838fbdca.

[5] *A hexagon-packing classification of scale-two graph Rips complexes*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-hexagon-packing-classification-of-scale-two-graph-rips-complex--70b9bc9b3abb.
