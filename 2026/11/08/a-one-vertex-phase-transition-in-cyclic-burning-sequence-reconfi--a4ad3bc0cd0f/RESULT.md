# A one-vertex phase transition in cyclic burning-sequence reconfiguration

## Finding

For every integer \(k\ge 2\), write \(C_n\) for the cycle on \(n\) vertices, and let \(\mathcal R_{n,k}\) be the **source-slide graph of optimal strict burning sequences** defined below. Then

\[
\mathcal R_{k^2,k}\cong k^2(k-1)!\,K_1,
\qquad
\mathcal R_{k^2-1,k}\cong (k-1)!\,C_{k(k^2-1)}.
\]

Here a coefficient before a graph denotes that many disjoint copies. Thus at the perfect square every optimal sequence is isolated, while deletion of one cycle vertex yields a disjoint union of long cycles. The one-short graph has \((k^2-1)k!\) vertices, the same number of edges, exactly \((k-1)!\) components, and component diameter \(\lfloor k(k^2-1)/2\rfloor\). The square graph has \(k^2(k-1)!\) vertices and no edges. These assertions include \(k=2\), when the graphs are respectively four isolated vertices and \(C_6\).

## Assumptions and scope

Label the vertices of \(C_n\) by \(\mathbb Z/n\mathbb Z\), adjacent when their difference is \(\pm1\). A **strict burning sequence of length \(k\)** is an ordered tuple \((x_1,\ldots,x_k)\) such that (i) for all \(1\le i<j\le k\), \(d(x_i,x_j)\ge j-i\), so a source has not burned before its designated ignition round; and (ii) \(\bigcup_{i=1}^{k} B(x_i,k-i)=V(C_n)\), where \(B(x,r)=\{v:d(v,x)\le r\}\). Each source is selected from currently unburned vertices; sources are time-labelled and not treated as an unordered set. An edge of \(\mathcal R_{n,k}\) replaces exactly one \(x_i\) by a neighboring vertex of \(C_n\) while preserving both strict conditions; all other coordinates and their ignition times stay fixed. This operation is **not** the order-swap operation of the fixed-source burning-schedule model.

The known cycle burning number is \(b(C_n)=\lceil\sqrt n\rceil\), so all sequences considered here are optimal. The result applies only to the two cycle lengths \(k^2\) and \(k^2-1\), to strict ignition, and to one-coordinate adjacent relocation.

## Proof

**1. Arc excess.** For \(k\ge3\) each ball \(I_i=B(x_i,k-i)\) is a proper cyclic interval of length \(\ell_i=2(k-i)+1\); their total lengths sum to \(k^2\). In a covering of a cycle of \(n=k^2\) vertices, all \(I_i\) must be pairwise disjoint, so they tile the circle. For \(n=k^2-1\), the sum of all multiplicities above one is exactly one: one vertex is in exactly two intervals and every other vertex is in exactly one. In particular, no triple intersection and no two different intersection vertices are possible.

**2. All cyclic tilings are valid.** Let \(i<j\) and put \(r_i=k-i\), \(r_j=k-j\). The maximum sum of two distinct radii is \(2k-3 < (k^2-1)/2\) for \(k\ge3\). Therefore, if two cyclic balls intersect in at most one vertex, their centers have graph distance at least \(r_i+r_j\) (intersection in one vertex occurs at the extreme endpoints); if disjoint, their distance is at least \(r_i+r_j+1\). Since \(r_i+r_j\ge j-i\), the strict ignition inequalities are automatic. Conversely, each strict burning sequence has the covering property by definition. Thus the full state spaces are precisely the labelled cyclic arc tilings of the specified lengths with zero or one shared vertex.

**3. The perfect square.** Each state is obtained by choosing the cyclic order of \(k\) distinct time labels, modulo cyclic rotation (\((k-1)!\) choices), and the initial vertex of a distinguished labelled arc (\(n\) choices); arc centers are then fixed. Moving one center one step shifts both endpoints of its interval, creating a previously uncovered vertex at its former outer boundary. The other intervals stay in place and were disjoint, so no source slide is legal. The square graph is \(n(k-1)!\) isolated vertices.

**4. The one-short cycle and its unique cyclic-order encoding.** Each covering has exactly one one-vertex intersection, shared by exactly two intervals. Walking clockwise around the cycle identifies their cyclic order unambiguously: every interval of length at least three has an interior vertex unique to itself, and the sole singleton interval is located at an endpoint shared with a uniquely adjacent interval. Hence there are \((k-1)!\) cyclic orders. Given an order, choose one of the \(k\) boundaries at which the single overlap occurs and the starting vertex of a distinguished arc (\(n\) choices). Consecutive arc lengths, overlapping by one vertex at that boundary only, then determine all centers. By Step 2 every such tiling is a strict optimal sequence. There are \(n k!\) states.

**5. Exactly two source slides.** In a one-overlap tiling, shifting a cyclic interval one vertex clockwise or counterclockwise changes only its two ends. If it does not touch the unique overlap interface, it leaves a one-vertex gap at one end; the pre-existing overlap elsewhere cannot repair that gap. At the overlap between consecutive intervals \(A\) and \(B\) in clockwise order, exactly two operations preserve coverage: shift the center of \(A\) one step counterclockwise, transferring the overlap to the boundary immediately before \(A\); or shift the center of \(B\) one step clockwise, transferring it to the boundary immediately after \(B\). Both stay strict by Step 2. No other single-coordinate shift is admissible. This remains true if one interval is the singleton ball: a move that instead places it in the interior of an earlier ball either loses coverage at an endpoint or violates the strict inequality, while the two specified interface moves stay admissible. Consequently the source-slide graph is 2-regular, and neither legal move changes cyclic label order.

**6. Winding and components.** Repeatedly choose the clockwise move of Step 5. The unique overlap interface advances by one position in the cyclic list. After exactly \(k\) moves each labelled interval has shifted by one graph vertex clockwise; the overlap interface is the same but its position in \(C_n\) has advanced by one. Thus a return to the original state requires a multiple of \(n\) such \(k\)-move rounds. These \(kn\) clockwise moves visit every state of the fixed cyclic order, as there are precisely \(kn\) of them. Hence each order contributes a single connected cycle of length \(kn\). Different orders cannot be connected. This yields \((k-1)!\) disjoint cycles as claimed.

**7. Small boundary.** For \(k=2\), on \(C_4\) the two arcs have lengths 3 and 1; they must be disjoint, so each initial source determines the opposite second source and all four configurations are isolated. On \(C_3\), the radius-one ball covers the entire graph; any ordered pair of distinct sources is strict and optimal. The six pairs, linked by moving one source to its other unoccupied adjacent vertex, form \(C_6\).

## Verification

Two standalone programs below were run from this package's source paths. A C++17 exhaustive enumeration directly forms all ordered \(k\)-tuples satisfying the strict metric inequalities and the final ball coverage, constructs every adjacent single-coordinate replacement, and tests all degrees, counts and component sizes for \(2\le k\le5\) and both lengths. An independently written Python program repeats the construction with set-valued balls and checks \(2\le k\le4\). Their outputs are included. These are finite corroborations; the proof above establishes every \(k\ge2\).

To reproduce from this directory, run `g++ -O2 -std=c++17 check_reconfig.cpp -o check_reconfig && ./check_reconfig` and `python3 check_python_reconfig.py`. The C++ implementation uses 64-bit bitmasks only for the tested graphs of order at most 25; no general result is inferred from that numerical representation.

## Relationship to prior work

Bonato, Janssen and Roshanbin introduce strict burning and prove the final-radius covering criterion together with the cycle burning number \(\lceil\sqrt n\rceil\), but neither their published optimal-length result nor its covering argument enumerates the source-slide graph or establishes its component architecture. Nagao and Ogawa investigate burning-schedule reconfiguration on path forests with a **fixed source set** and swaps of **ignition ordering**, distinct from moving a time-labelled source by one host edge on a cycle. The present explicit source-slide operation must not be conflated with their standard order-swap problem. No prior source identified in the checked literature gives the asserted two exact graph isomorphisms. Searches do not establish global priority.

## Limitations

Only the specified two near-square cycle lengths and strict ignition are covered; arbitrary burning sequences, source-set swaps, relaxed ignition, and path or noncycle hosts are outside the theorem. The later full-length publication of Nagao–Ogawa could not be inspected; the available complete 2022 two-page conference version defines a materially different move model. Historical unindexed equivalences remain possible, and independent scholarly assessment has not been performed.

## References

1. A. Bonato, J. Janssen, E. Roshanbin, *How to burn a graph*, arXiv:1507.06524, first publicly posted July 23, 2015. https://arxiv.org/abs/1507.06524 (definitions, condition (1), Corollary 11).
2. A. Nagao, S. Ogawa, *Algorithms for Burning Schedule Reconfiguration Problem on Path Forests*, JCDCG³ 2022 conference proceedings, pp. 25–26, especially the definition of BSRP. https://www.rs.tus.ac.jp/jcdcggg/JCDCG3-2022Proceedings%28r2%29.pdf
3. A. Nagao, S. Ogawa, later book-chapter version of the same title, DOI:10.1007/978-3-032-00281-5_21 (full text not inspected).
