# Integral homotopy and Klein-four reflection character of the five-robust \(4\times5\) grid

## Finding

For the Cartesian grid \(G=P_4\square P_5\), define the five-robust clique complex
\[
K=\mathsf{Cliq}_5(G)=\{W\subseteq V(G):\alpha(G[W])<5\}.
\]
The geometric realization has the **integral homotopy type**
\[
|K|\simeq\bigvee^{489}S^7.
\]
Let \(\rho_r\) reverse the four rows and \(\rho_c\) reverse the five columns. On \(\widetilde H_7(K;\mathbb Q)\), the character of their Klein-four group, in order \((1,\rho_r,\rho_c,\rho_r\rho_c)\), equals \((489,31,13,15)\). The decomposition into simultaneous one-dimensional eigenspaces with eigenvalue signs \((+,+),(+,-),(-,+),(-,-)\) has respective dimensions \((137,123,114,115)\).

The dimension 489 was already published as a Betti number for the Alexander-dual total five-cut complex. This finding does **not** claim that numerical rank as new: it establishes an explicit integral homotopy classification and the full rational reflection representation.

## Assumptions and scope

The grid is finite, undirected, and simple. Its vertices are \((r,c)\), where \(0\le r\le3\), \(0\le c\le4\), with an edge precisely when Manhattan distance is one. The bit label of a vertex is \(5r+c\). The induced graph independence number \(\alpha(G[W])\) is the largest size of a subset of \(W\) having no internal edges. The empty set is a face, and the Morse face poset contains all nonempty faces. Rows and columns are reflected by \(\rho_r(r,c)=(3-r,c)\) and \(\rho_c(r,c)=(r,4-c)\). All unsigned homotopy and integral homology statements use \(\mathbb Z\); only the stated representation uses \(\mathbb Q\).

No claim is made for other rectangular grids, parameters, or integral isomorphism types of the symmetry representation. The Morse matching is not claimed to be symmetry-equivariant.

## Proof

**Exact face recognition.** For each vertex-subset bitmask \(s\), let \(a(s)\) be the induced independence number. For its least set bit \(v\), with closed-neighborhood mask \(N[v]\), the exhaustive recurrence is
\[
a(0)=0,\qquad a(s)=\max\{a(s\setminus\{v\}),\;1+a(s\setminus N[v])\}.
\]
Both arguments are strict submasks, so a loop over the \(2^{20}=1,048,576\) masks computes \(a(s)\) exactly. An **independent second face test** enumerates all independent five-subsets directly by adjacency tests, and propagates each forbidden five-set to all of its supersets using a Boolean subset-zeta sweep. The two resulting face predicates agree for every mask. There are exactly 1,998 independent five-subsets, and the 72,568 nonempty faces have face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6,f_7)
=(20,190,1140,4845,13506,22831,21374,8662).
\]
The ordinary Euler characteristic is \(-488\). The dimension is seven because each bipartition color class is an independent set, so an admissible face has at most four vertices of each color, and there are eight-element admissible faces.

**Complete discrete-Morse matching.** Begin with all nonempty faces unmatched. At each pivot vertex in bit order \(v=0,\dots,19\), for every still-unmatched face \(s\) lacking that vertex, pair it with \(s\cup\{v\}\) exactly when the latter is also unmatched; remove both from later stages. This forms a matching of codimension-one cover incidences. The verifier implements this construction verbatim on the complete face set, yielding 36,039 matched pairs, exactly one unmatched zero-face, and 489 unmatched seven-faces, with no other unmatched faces.

To prove rather than assume acyclicity, orient every codimension-one face inclusion downward except the matched incidences, which are reversed. The standalone code visits all **446,610** cover incidences, forms the directed indegree of all 72,568 nonempty faces, and runs a complete topological sort. All 72,568 faces are removed, so this full directed Hasse graph is acyclic. Forman's finite discrete-Morse theorem thus gives a CW complex with one zero-cell and 489 seven-cells and no intermediate cells. Every seven-cell attaches to the single point in the six-skeleton. The CW complex, hence \(|K|\), is a wedge of 489 seven-spheres, with no torsion or unverified attaching maps.

**Reflection character.** For any of the four specified symmetries \(g\), orient a simplex by increasing bit label, and put
\[
L(g)=\sum_{\emptyset\ne\sigma\in K,\,g\sigma=\sigma}
(-1)^{|\sigma|-1}\operatorname{sgn}(g|_\sigma).
\]
This is the ordinary Lefschetz number of the simplicial chain action. The complete face enumeration gives invariant-face counts \((72568,252,444,212)\) and Lefschetz numbers \((-488,-30,-12,-14)\), respectively. Since \(H_0(K;\mathbb Q)\cong\mathbb Q\) has trivial action and the only positive-degree homology is in odd degree seven, the degree-seven trace is \(1-L(g)\), namely \((489,31,13,15)\). The Klein-four character-orthogonality formula gives multiplicity
\[
m_{\epsilon_r,\epsilon_c}=
\frac{489+31\epsilon_r+13\epsilon_c+15\epsilon_r\epsilon_c}{4},
\quad \epsilon_r,\epsilon_c\in\{\pm1\},
\]
namely \(137,123,114,115\), all nonnegative integers summing to 489. The character is a homotopy invariant of the actual symmetry action, even though the specified Morse matching need not respect it.

## Verification

Run `python3 verify_grid45_robust.py` with standard Python 3. The code independently evaluates both exact face predicates over all \(2^{20}\) masks; checks all asserted face counts and the Euler characteristic; constructs every Morse pair; verifies all critical cells and all oriented Hasse incidences by a complete directed topological sort; and computes every reflection-fixed face with its orientation sign. A successful run prints `VERIFY_OK`. `CHECK_OUTPUT.txt` contains the expected actual output of an execution on the embedded source. No approximate numerical linear algebra, samples, or stored binary certificates are required. Forman's finite theorem turns the exhaustively checked acyclic matching into the claimed infinite homotopy statement *for this fixed finite complex*.

## Relationship to prior work

Filakovský [1], first publicly posted February 11, 2026, proves the robust-clique homotopy formula for parameters two and three on arbitrary rectangular grids and for all parameters under edge-only square attachments; Conjecture 5 asks for a sphere-wedge type when corner attachments occur. The four-by-five grid at parameter five falls outside those proven cases.

Bayer and coauthors [2], Table 3, **already tabulate the number 489** as the degree-ten Betti rank of the **total five-cut complex** on the four-by-five grid. Its Alexander dual is the current robust clique complex; integral Alexander duality predicts the corresponding rank in degree seven, but **does not specify an integral unstable homotopy equivalence or the four reflection traces**. The source describes the use of Morse-element calculations; it may have implicit unpublished matching information. The exact numerical rank is not a novelty claim.

Chandrakar and coauthors [3], Theorem 1.1, classify total cut complexes for two-row grids and the total three-cut complex for three-row grids, but do not classify the present five-robust four-row object. Related exact finite homotopy results for the four-by-four grid and the parameter-four four-by-five grid establish different objects or thresholds [4–6]; their statements do not entail this parameter-five homotopy or its reflection representation.

## Limitations

This is an exact finite-instance classification, not a uniform theorem in grid width. It does not provide a symmetry-equivariant homotopy equivalence or an integral decomposition of the Klein-four lattice; the character calculation is rational. The previously published rank 489 is explicitly excluded from novelty. The published older use of Morse computations and possibly unindexed appendices, software, or computations leave residual priority risk for an exact matching or equivalent reflection statement. No independent mathematical audit has been performed.

## References

[1] Marek Filakovský, *The Topology of \(k\)-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365, first publicly submitted 2026-02-11, Theorem 1, Corollary 3, Conjecture 5, Example 10. https://arxiv.org/html/2602.11365

[2] Margaret Bayer, Mark Denker, Marija Jelić Milutinović, Rowan Rowlands, Sheila Sundaram, and Lei Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503, first publicly submitted 2022-09-27, Section 5, Table 3, and Appendix Theorem 7.2. https://arxiv.org/pdf/2209.13503

[3] Himanshu Chandrakar, Nisith Ranjan Hazra, Debotosh Rout, and Anurag Singh, *Topology of Total Cut Complexes and Cut Complexes of Grid Graphs*, arXiv:2408.07646, first publicly submitted 2024-08-14, Theorem 1.1. https://arxiv.org/html/2408.07646v3

[4] *Integral homotopy classification of robust clique complexes on the \(4\times4\) grid*, published research record, 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-integral-homotopy-classification-of-robust-clique-complexes-on-t--ad24e6739c28

[5] *Sharp binomial breakdown in the robust-clique homotopy of two width-three grids*, published research record, 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sharp-binomial-breakdown-in-the-robust-clique-homotopy-of-two-wi--695baded869f

[6] *Four-robust clique homotopy on the first two-dimensional grid range and its square-symmetry characters*, published research record, 2026-10-18. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-four-robust-clique-homotopy-on-the-first-two-dimensional-grid-ra--a723a1190e9a
