# The eleven-cycle Petersen graph-Hom complex has 64 circles and 2,640 rigid maps

## Finding
Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph on the ten two-subsets of \([5]\), with edges between disjoint subsets, and let \(C_{11}\) be the eleven-cycle. For the ordinary graph-Hom polyhedral CW complex,
\[
\operatorname{Hom}(C_{11},P)\simeq
\left(\coprod^{64}S^1\right)\sqcup
\left(\coprod^{2640}\{\mathrm{pt}\}\right).
\]
Thus \(H_0\cong\mathbb Z^{2704}\), \(H_1\cong\mathbb Z^{64}\), and all higher integral homology vanishes. The 168,960 vertices partition into 2,640 isolated vertices, 40 connected components of size 198, and 24 connected components of size 6,600. The smallest odd-source case with these two different positive-dimensional component-size families is exhibited here, compared with the three earlier determined lengths five, seven and nine.

## Assumptions and scope
A vertex of \(\operatorname{Hom}(C_{11},P)\) is a graph homomorphism from \(C_{11}\) to \(P\), equivalently a closed walk of length eleven with a marked initial vertex. A CW cell is a tuple \((A_0,\ldots,A_{10})\) of nonempty vertex subsets such that every member of \(A_i\) is adjacent in \(P\) to every member of \(A_{i+1}\), with cyclic indices. This cell is \(\prod_i\Delta(A_i)\), of dimension \(\sum_i(|A_i|-1)\). All connected components of this CW complex are determined by its one-skeleton. We work with the Petersen graph and no arbitrary target or longer source-cycle parameter.

## Proof
**Vertices and connected components.** Let \(V(P)\) be all two-element subsets of \([5]\) and \(N(u)\) its three-element neighbor set. Enumerate walks \(w=(w_0,\ldots,w_{10})\) such that \(w_{i+1}\in N(w_i)\) cyclically. Exact recursive enumeration gives 168,960 vertices. Independently the Petersen adjacency spectrum is \(3,1^5,(-2)^4\), so the closed-walk formula yields \(3^{11}+5+4(-2)^{11}=168960\). Two such vertices share a one-cell precisely if they differ at one coordinate \(i\), whose two possible values lie in \(N(w_{i-1})\cap N(w_{i+1})\). Exhaustively generating these incidences and applying a disjoint-set union algorithm yields 2,640 singleton components, 40 components with 198 zero-cells each, and 24 components with 6,600 zero-cells each. This partitions all vertices, since \(2640+40\cdot198+24\cdot6600=168960\). The standalone code enumerates all allowable values by the defining disjointness relation rather than consulting a stored list of edges.

**An independent Euler-characteristic certificate.** Each coordinate value set of any graph-Hom cell must be a nonempty subset of one Petersen neighborhood. Exactly fifty distinct nonempty masks occur. The two masks \(A,B\) are compatible precisely if every element of \(A\) is adjacent to every element of \(B\); there are exactly 110 ordered compatible pairs. A transfer-state walk of length eleven with cyclic closure enumerates every labeled CW cell exactly once: its degree is \(\sum_i(|A_i|-1)\). Starting at each of the fifty possible first masks and multiplying transitions while tracking the degree produces the full cell vector, in degrees zero through six,
\[
(168960,\ 582120,\ 859320,\ 693000,\ 323400,\ 83160,\ 9240).
\]
There are no cells in higher degrees, as the recurrence enumerates all possible mask walks. Its alternating sum is
\[
\chi=168960-582120+859320-693000+323400-83160+9240=2640.
\]
The transfer algorithm is separate from the walk/one-skeleton union-find enumeration; both operate on explicit finite definitions and all integer counts are checked by the supplied executable.

**Recovering the homotopy type.** Fujii–Kimura–Nozaki's square-free-target theorem (Theorem 1.2 of arXiv:2412.19039) states that when source and target are connected and nonbipartite, and the target is square-free, every connected component of the Hom complex is homotopy equivalent to a point or a circle. The Petersen graph has girth five, so is square-free and nonbipartite; \(C_{11}\) is also connected and nonbipartite. Each of the 2,640 singleton components is a point with Euler characteristic one. Any other component has Euler characteristic zero or one by that theorem. The total Euler characteristic equals exactly 2,640, exhausted by the singletons, so every one of the remaining \(40+24=64\) components has Euler characteristic zero and is homotopy equivalent to a circle. This determines integral homology and proves the claimed classification.

**Rigid noninjective maps.** Because the Petersen graph has no four-cycles, distinct neighbors of any pair of vertices have at most one common neighbor. A closed walk admits a one-coordinate recoloring exactly when it makes an immediate backtrack: if the adjacent images coincide, all three neighbors are possible choices; if distinct, their common neighbor is unique. Hence singleton components are exactly nonbacktracking closed eleven-step walks. Such walks cannot be injective because the target has only ten vertices. This distinguishes the rigid maps from the injective nine-cycle traversals at source length nine.

## Verification
Run `python3 verify.py` with Python 3.9 or later; only the standard library is needed. The implementation independently enumerates all 168,960 zero-cells and their reconfiguration connections, then calculates all CW cell counts by a fifty-mask transfer dynamic program. It asserts the complete component-size distribution, cell vector and alternating Euler characteristic; `expected_output.txt` is a standalone exact transcript of the asserted conclusions. The topological point-or-circle premise is the cited general theorem and is not claimed to be established by finite experimentation.

## Relationship to prior work
Fujii, Kimura and Nozaki, arXiv:2412.19039 (first public December 26, 2024; 2026 journal), prove the square-free-target point-or-circle theorem used here, including a general component algorithm, but do not state these eleven-cycle Petersen counts in the inspected text. Matsushita, arXiv:2412.19144 (first public December 26, 2024), independently provides an equivalent point-or-circle theorem. A published three-length Petersen classification at the linked published-finding corpus record determines \(C_5,C_7,C_9\) with 120 points, 24 circles, and 24 circles plus 360 points, respectively; that finite range cannot imply the present \(C_{11}\) enumeration. General component-type theorems do not supply the exact component sizes or CW Euler characteristic required here. Equivalent worked computations might exist outside the checked sources.

## Limitations
Only the source cycle of length eleven and the Petersen target are classified. No all-odd-length formula, equivariant homotopy decomposition, or extension to other square-free targets is claimed. The topological inference relies on a published theorem, while numerical premises are exhaustive finite certificates, not Monte Carlo experiments. Unindexed priority overlap and independent checking remain open.

## References
1. S. Fujii, K. Kimura, Y. Nozaki, *Homotopy types of Hom complexes of graph homomorphisms whose codomains are square-free*, arXiv:2412.19039 (first public 2024-12-26), Theorem 1.2. https://arxiv.org/abs/2412.19039.
2. T. Matsushita, *Hom complexes of graphs whose codomains are square-free*, arXiv:2412.19144 (first public 2024-12-26). https://arxiv.org/abs/2412.19144.
3. *Odd-cycle graph-Hom complexes into the Petersen graph: twenty-four circles and rigid nine-cycles*, published 2026-11-01. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-odd-cycle-graph-hom-complexes-into-the-petersen-graph-twenty-fou--ce6537190eb4.
