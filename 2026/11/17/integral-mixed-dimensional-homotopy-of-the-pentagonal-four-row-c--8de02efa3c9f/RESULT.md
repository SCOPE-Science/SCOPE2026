# Integral mixed-dimensional homotopy of the pentagonal four-row cylinder matching complex

## Finding
Let \(G=P_4\square C_5\), with \(P_4\) the path on four vertices and \(C_5\) the cycle on five vertices. Its ordinary edge-matching simplicial complex has the exact integral homotopy type
\[
\boxed{|\mathcal M(G)|\simeq\bigvee^{141}S^6\vee\bigvee^5S^7.}
\]
In particular, the only nonzero reduced integral homology groups are \(\widetilde H_6\cong\mathbb Z^{141}\) and \(\widetilde H_7\cong\mathbb Z^5\). This is a classification of a fixed finite cylinder, not an asserted formula for all cylinder lengths.

## Assumptions and scope
The graph has vertex set \(\{(r,c):0\le r<4,\ 0\le c<5\}\). Its 35 edges are the 15 vertical edges \(\{(r,c),(r+1,c)\}\) with \(r<3\) and the 20 circumferential edges \(\{(r,c),(r,c+1\bmod5)\}\). A simplex of \(\mathcal M(G)\) is an arbitrary collection of edges of \(G\) with pairwise disjoint endpoints; the empty simplex is included in the augmented face poset.

## Proof
**Exhaustive face-poset matching.** Number graph edges in row-major order, visiting first the vertical edge from each vertex when present and then its circumferential edge. Enumerate all bit masks of pairwise disjoint graph edges by exhaustive include/exclude recursion. For a permutation of the 35 edge positions obtained using a Mersenne Twister with seed 138 and the C++17 standard-library shuffle, repeatedly pair each currently unmatched face \(F\) not containing the chosen edge \(e\) with \(F\cup\{e\}\) whenever the latter remains unmatched. The complete algorithm and an independent directed-cover acyclicity checker are supplied. There are precisely 253,880 augmented faces and 1,574,120 face-poset cover relations. The matching has 126,859 pairs; all 253,880 faces admit a topological ordering under the directed Hasse orientation, certifying no gradient cycle. Its unpaired augmented faces number one in dimension five, 149 in dimension six, and 12 in dimension seven. Delete the matching pair containing the empty face; the ordinary matching then also has one critical zero-cell, without changing its positive-dimensional Morse differential. No other critical faces occur.

**Exact Morse boundary.** Apply the signed simplicial boundary (vertices ordered by the edge indices) and algebraic gradient-path elimination: a lower matched facet is replaced by the signed sum of the other facets of its matched coface, an upper matched face projects to zero, and a critical facet projects to itself. Acyclicity makes this recursion finite. The resulting integral Morse chain groups in dimensions five, six and seven have respective ranks \(1,149,12\). Their consecutive boundary matrices have sizes \(1\times149\) and \(149\times12\) and satisfy \(\partial_6\partial_7=0\). Exact Smith normal forms show that \(\partial_6\) has one nonzero invariant factor, equal to one, and \(\partial_7\) has seven, all equal to one. Consequently
\[
\widetilde H_5=0,\qquad
\widetilde H_6\cong\mathbb Z^{149-1-7}=\mathbb Z^{141},\qquad
\widetilde H_7\cong\mathbb Z^{12-7}=\mathbb Z^5.
\]
There is no torsion, and all other reduced integral homology vanishes.

**Upgrade from homology to homotopy.** The acyclic matching gives a CW model with one zero-cell and cells only in dimensions five, six and seven. The unit invariant factor in \(\partial_6\) allows cancellation of the five-cell with a six-cell, leaving a wedge of 148 six-spheres with twelve seven-cells attached. Their attaching maps lie in \(\pi_6(\bigvee^{148}S^6)\cong\mathbb Z^{148}\) and are completely specified by integral degrees. Since the original \(\partial_7\) has primitive rank seven and its image lies in \(\ker\partial_6\), the induced seven-cell attaching matrix after cancellation is also primitive of rank seven. Integral basis changes followed by seven elementary cell cancellations leave exactly 141 six-spheres and five unattached seven-spheres. This proves the displayed integral homotopy equivalence.

## Verification
Run `python verify.py` with Python 3, SymPy and a C++17 compiler (`g++`). The verifier independently reconstructs all matching faces, checks the full directed Hasse graph for acyclicity, builds the exact signed Morse matrices, computes integral Smith factors, checks \(\partial^2=0\), and repeats everything for a second edge order (seed 1). The second matching has critical counts \((9,172,27)\) in dimensions \((5,6,7)\), and exact unit Smith ranks \((9,22)\), giving the same integral homology.

The exhaustive augmented face counts by dimension \(-1,0,\ldots,9\) are \((1,35,505,3910,17725,48193,77405,69510,31060,5360,176)\). They yield reduced Euler characteristic \(136=141-5\), independently checking the resulting alternating sum. The generated certificate is finite and exhaustive for the specified graph only.

## Relationship to prior work
Chauhan, Sharma and Shukla's 2026 study concerns ordinary matching complexes of *rectangular three-row* grids \(P_3\square P_n\), not the four-row pentagonal cylinder. The earlier Goyal–Shukla–Singh treatment of three-row rectangular grids carries a published retraction/correction, so its assertions do not serve as a proof here. Braun–Hough and Matsushita study small rectangular strip complexes. Gupta–Sarkar–Sawant–Shukla study the categorical, rather than Cartesian, product of paths.

The nearest publicly recorded finite calculations concern \(P_4\square C_4\), \(P_3\square C_5\), and \(P_4\square P_5\). Those graphs are nonisomorphic to \(P_4\square C_5\) and their homotopy classifications do not imply this result. In particular, closing the five-column rectangular strip changes its known wedge of 41 six-spheres into a complex with 141 six-spheres and five seven-spheres. Searches of matching-complex synonyms, line-graph independence complexes and more general cylindrical formulas disclosed no direct prior classification; these searches do not prove historical uniqueness.

## Limitations
This proves only the fixed 20-vertex, 35-edge graph \(P_4\square C_5\). No infinite-family recurrence, symmetry representation, or general torsion-freeness theorem is claimed. The complete text of the particularly relevant September 2026 three-row-grid article could not be retrieved; its available abstract specifies a different graph family. A separate equivalent result not indexed by the consulted sources remains possible. The mathematics has not undergone independent audit.

## References
1. P. Chauhan, A. Sharma, S. Shukla, *Homology of matching complexes of \(3\times n\) grid graphs*, arXiv:2609.27366, publicly posted 2026-09-23, https://arxiv.org/abs/2609.27366.
2. S. Goyal, S. Shukla, A. Singh, *Matching complexes of \(3\times n\) grid graphs*, Electronic Journal of Combinatorics 28 (2021), P4.16; retraction/corrigendum at https://doi.org/10.37236/10496.
3. B. Braun, W. Hough, *Matching and Independence Complexes Related to Small Grids*, Electronic Journal of Combinatorics 24 (2017), P4.18, https://doi.org/10.37236/6212.
4. T. Matsushita, *Matching Complexes of Small Grids*, Electronic Journal of Combinatorics 26 (2019), P3.1, https://doi.org/10.37236/8480.
5. R. K. Gupta, S. Sarkar, S. S. Sawant, S. Shukla, *On the matching complexes of categorical product of path graphs*, arXiv:2403.15298, https://arxiv.org/abs/2403.15298.
