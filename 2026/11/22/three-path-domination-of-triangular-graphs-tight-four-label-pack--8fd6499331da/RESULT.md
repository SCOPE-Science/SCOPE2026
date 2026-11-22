# Three-path domination of triangular graphs: tight four-label packings and regular exchange

## Finding
For every integer \(n\ge3\), the triangular graph \(T_n=J(n,2)=L(K_n)\) has three-path domination number
\[
\gamma_{P_3}(T_n)=\left\lceil\frac{n-1}{4}\right\rceil.
\]
Here a *three-path* is an **edge-defined subgraph** isomorphic to \(P_3\), with a designated middle vertex and two unordered endpoints; the endpoints may also be adjacent in the ambient graph. A three-path dominating configuration is an unordered set of such paths whose collective vertices dominate \(T_n\).

At every tight order \(n=4k+1\), \(k\ge1\), all optimal configurations are characterized as follows. Exactly one ground label of \(K_n\) is unused. The other \(4k\) labels split into \(k\) disjoint four-label blocks; each block supports exactly one three-path of \(T_n\), whose three vertices represent either a three-edge star or a three-edge ordinary path in the underlying \(K_n\). Conversely, every such choice is an optimum. Their number on fixed, distinctly labelled ground points is
\[
\boxed{N_{4k+1}=\frac{(4k+1)!}{k!}.}
\]

Join two optimal configurations if one entire three-path can be replaced by another while all other paths remain fixed and domination remains optimal. This exchange graph is connected and regular of degree \(119k\). In particular its number of edges is
\[
\boxed{|E(\mathcal R_k)|=\frac{119k(4k+1)!}{2k!}.}
\]
Its first orders are \((n,k,N,\deg)=(5,1,120,119),(9,2,181440,238),(13,3,1037836800,357)\).

## Assumptions and scope
All graphs are finite, simple and undirected. The ground vertices \([n]\) of \(K_n\) are individually labelled. A vertex of \(T_n\) is a two-element subset of \([n]\); two such vertices are adjacent precisely when the subsets intersect. A three-path \(Q\) has three **distinct** vertices \((e_1,e_2,e_3)\), with \(e_1\sim e_2\sim e_3\); reversing endpoints does not distinguish paths, but changing the middle vertex does. Thus a triangle in \(T_n\) contains three distinct three-path subgraphs. This explicitly fixes the path-object convention, as opposed to counting only their three-vertex supports.

A collection \(\mathcal D\) of three-paths dominates when \(\bigcup_{Q\in\mathcal D}V(Q)\) is an ordinary closed-neighborhood dominating set. Its cardinality is the number of paths, not the number of selected vertices. In \(\mathcal R_k\), one move exchanges exactly one **whole path** (not one vertex of \(T_n\)) and retains cardinality \(k\). The universal minimum formula holds for \(n\ge3\); the census and reconfiguration theorem hold only for \(n=4k+1\), \(k\ge1\).

## Proof
**1. Edge-incidence translation.** A set \(S\subseteq V(T_n)\) is an edge set of \(K_n\). Let \(U(S)\subseteq[n]\) be the union of endpoints of its edges. Then
\[
S\text{ dominates }T_n\quad\Longleftrightarrow\quad |[n]\setminus U(S)|\le1.
\]
If two ground labels \(a,b\) are missing, the vertex \(ab\) of \(T_n\) has no neighbor in \(S\) and is not selected. Conversely, if at most one label is missing, each ground edge either is selected or intersects a selected ground edge; the corresponding vertex of \(T_n\) is dominated.

**2. Four-label capacity of one three-path.** Take \(Q=(e_1,e_2,e_3)\) with \(e_1\cap e_2\ne\varnothing\) and \(e_2\cap e_3\ne\varnothing\). Since each ground edge has two endpoints, and each of the two subsequent edges must meet the preceding connected component, the three-edge ground graph has at most four distinct vertices. If it has exactly four, it is a connected three-edge tree on four vertices, hence either \(K_{1,3}\) or \(P_4\). Every three-edge star and every \(P_4\) supports a three-path in \(T_n\): for the star choose any of the three edges as its middle, and for \(P_4\) take its unique middle edge.

With \(q\) three-paths, at most \(4q\) ground labels occur. By Step 1, domination requires \(4q\ge n-1\), giving \(q\ge\lceil(n-1)/4\rceil\).

**3. Attainment for all orders.** Put \(q=\lceil(n-1)/4\rceil\). For \(n=3,4,5\), a single three-path exists that uses at least \(n-1\) ground labels: a three-edge triangle for \(n=3\), or a three-edge tree on four labels for \(n=4,5\). For \(n\ge6\), assign four different labels to each of \(q-1\) disjoint blocks and put a three-edge path or star on each block. There remain \(r=n-1-4(q-1)\in\{1,2,3,4\}\) labels that must be covered. Choose a last three-edge tree using all those \(r\) labels and, if \(r<3\), enough labels already used in an earlier block to reach at least three ground labels; if \(r=4\), use exactly those four new labels. When \(r=1,2\), a triangle on three ground labels yields a three-path of \(T_n\); when \(r=3\), use a three-edge triangle; when \(r=4\), use a three-edge tree. (For \(r=1\) choose two old labels, for \(r=2\) choose one old label.) Every last path contains a previously uncovered label, so all \(q\) paths are distinct. At least \(n-1\) ground labels are covered and the configuration dominates. Combined with Step 2 this proves the minimum formula.

**4. Tight-order rigidity.** Suppose \(n=4k+1\) and \(k\) paths dominate. Their ground supports must cover at least \(4k\) labels (Step 1), but the sum of the individual support sizes is at most \(4k\) (Step 2). Equality forces exactly one unused ground label, every path to use four ground labels, and these four-element supports to be pairwise disjoint. Consequently each path represents a three-edge star or a three-edge \(P_4\) on its own four-label block. Conversely, all configurations of this form dominate because only one label is omitted.

**5. Enumeration.** On four given ground labels, there are \(4\) choices of star center and \(3\) choices of its line-graph path middle, hence \(12\) star-type three-path subgraphs. There are \(4!/2=12\) unoriented three-edge ordinary paths, each with a unique middle edge, hence \(24\) admissible path objects on a four-label block. Choose the unused label, partition the remaining \(4k\) into \(k\) unordered blocks of four, then choose one of these \(24\) path objects independently per block:
\[
N_{4k+1}=(4k+1)\frac{(4k)!}{(4!)^k k!}\,24^k=\frac{(4k+1)!}{k!}.
\]
All choices are different configurations, because each path's unique four-label support recovers its block. This also explains why counting just the three selected vertices per path would lead to a different total: stars have three possible middle-edge choices under the stated path definition.

**6. Exact exchange degree.** Fix an optimum with unique unused label \(h\), and choose any one of its \(k\) paths. The other \(k-1\) paths occupy \(4k-4\) labels; only the four labels of the removed path together with \(h\) are available for its replacement if the resulting configuration is still optimal, by the rigidity just proved. The replacement path may use any of the five possible four-element subsets of this five-label set, with \(24\) possible path objects for each. One of these \(5\cdot24=120\) choices is the original path. Thus there are exactly \(119\) nontrivial replacements per removed path. Replacing different paths produces different neighboring configurations, since their disjoint supports identify the unchanged paths. Hence the graph is \(119k\)-regular, and its edge count follows by the handshake lemma.

**7. Connectivity.** A move can change the chosen three-path on any fixed four-label block to any other on that same support. A move can also swap the unused label \(h\) with an arbitrary label \(a\) of any block: replace that block's path by any path on the new four-label support. To exchange two block labels \(a,b\) while restoring the original hole label \(h\), perform three successive hole exchanges \(h\leftrightarrow a\), \(a\leftrightarrow b\), and \(b\leftrightarrow h\). At each step the currently unused label is exchanged with a label in a block by replacing the single path on that block. Thus any two labels in distinct blocks may be interchanged while restoring the hole. Therefore these moves connect all partitions into unordered four-blocks with one hole. Finally alter path structures within blocks as needed. The exchange graph is connected.

## Verification
Two independent standalone verifiers accompany this result. Compile `verify_direct.cpp` using a C++17 compiler, then run it. It directly constructs the line graph \(T_n\), enumerates all subgraph three-paths as middle-edge/end-vertex pairs, builds their closed-neighborhood masks and checks every two-path collection for \(n=8,9\) and all one-path collections for \(n=5\). It confirms \(120\) minima at \(n=5\) and \(181440\) at \(n=9\), and that every one of the \(181440\) winning pairs at \(n=9\) has disjoint four-label supports. It also samples 30 of the \(n=9\) solutions and checks their exchange degrees \(238\) by direct replacement enumeration.

Run `python3 verify_support.py` for independent four-block/path-object enumeration. It verifies the \(12+12=24\) local star/path count, explicitly enumerates all unordered four-block partitions at \(n=5,9\), and checks their products against the factorial formula. It checks integrality of the formulas for further tight orders. Executed outputs are included in `CHECKS.txt`. The infinite-order conclusions follow from Steps 1–7, not from the finite tests.

## Relationship to prior work
Ibrahim, Jackson and King introduced three-path domination and established its NP-completeness and the exact parameter for paths and cycles in 2024. The proof and full accessible article do not treat triangular graphs or enumerate three-path objects on them.

Related classifications of ordinary total dominating and paired-dominating sets in triangular graphs work with vertex subsets, not collections of three-vertex paths. Their tight families use two-edge connected components occupying three ground labels, rather than the present three-edge/four-label units. A published liar's vertex-edge domination classification also involves four-vertex trees, but its selection constraints differ: at \(n=4k+1\) the present configurations have one isolated ground label and therefore do not meet that stronger triple-incidence condition. None of those statements implies the exact path-object count or the whole-path exchange graph asserted here. The incidence translation and four-label capacity are elementary ingredients, not independently claimed as novel.

## Limitations
The exact optimizer census and exchange graph are asserted only for \(n\equiv1\pmod4\). At other orders the minimum formula still holds but overlapping path supports can occur, and their optimizer counts are not given. Three-paths are edge-defined; identifying all possible middle choices on a three-vertex clique changes the enumeration. The exchange is a whole-path replacement, not a one-vertex token slide. Exhaustive enumeration is limited to the stated small orders, and publication-priority clearance is provisional; independent mathematical review has not been performed.

## References
1. R. Ibrahim, R. Jackson and E. L. C. King, *Introducing 3-Path Domination in Graphs*, Journal of Combinatorial Mathematics and Combinatorial Computing **121** (2024), 97–106; publicly dated 2024-06-30. DOI: `10.61091/jcmcc121-10`. `https://combinatorialpress.com/jcmcc-articles/volume-121/introducing-3-path-domination-in-graphs/`.
2. N. Banerjee and D. A. Hoang, *The Complexity of Distance-\(r\) Dominating Set Reconfiguration*, arXiv:2310.00241, first posted 2023-09-30. `https://arxiv.org/abs/2310.00241`. This discusses a different reconfiguration object.
