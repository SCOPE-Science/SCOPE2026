# Exact three-flow reconfiguration sectors of two thin even bicliques

## Finding
For every integer \(t\ge1\), let \(G_a(t)=K_{a,2t}\) with \(a\in\{2,4\}\), with both bipartition classes individually labelled. Let \(\mathcal R_a(t)\) have one vertex for each nowhere-zero \(\mathbb Z_3\)-flow and one edge for each legal single directed-cycle reversal. Put \(d=\lfloor t/3\rfloor\). The number of connected components and the number of flow states are, respectively,
\[
\begin{array}{c|c|c}
 a & \#\operatorname{comp}(\mathcal R_a(t)) & |V(\mathcal R_a(t))|\\
 2 & 2d+1 & (4^t+2)/3\\
 4 & (2d+1)(8d^2+8d+3)/3 & (36^t+14\cdot9^t)/27.
\end{array}
\]
Every component is characterized by its exact left-shore outdegree vector, and no two different vectors communicate. In the four-left-vertex case all possible vectors are \(r_i=t+3s_i\), with \(-d\le s_i\le d\) and \(\sum_{i=1}^4s_i=0\). The component indexed by \((r_1,r_2,r_3,r_4)\) has precisely
\[
[x_1^{r_1}x_2^{r_2}x_3^{r_3}x_4^{r_4}]
\left(\sum_{1\le i<j\le4}x_ix_j\right)^{2t}
\]
states. For two left vertices the component with row sums \((t+3s,t-3s)\) has \(\binom{2t}{t+3s}\) states. There are exactly six isolated flows for \(a=4\), or exactly two for \(a=2\), when \(3\mid t\); there are no isolated flows otherwise. In particular \(K_{4,6}\) has 19 components, of sizes six times 1, twelve times 20 and once 1860, while \(K_{4,4}\) is connected.

## Assumptions and scope
All graphs are finite and simple. A nowhere-zero \(\mathbb Z_3\)-flow is a function from edges oriented in one fixed reference direction to \(\{1,-1\}\subset\mathbb Z_3\), satisfying Kirchhoff conservation at each vertex. We identify the sign with an actual edge orientation, with \(+1\) oriented from the left shore to the right shore. A legal cycle reversal reverses every edge of a consistently directed simple cycle; conservation and nonzero values remain valid. Both shore sizes and all vertex labels are fixed; colour or graph-automorphism quotients are not taken. The formulas hold for all integers \(t\ge1\), not just tested orders.

## Proof
Orient a nonzero \(\mathbb Z_3\)-flow along the sign of its values. Kirchhoff conservation is \(2\operatorname{outdeg}(v)\equiv\deg(v)\pmod3\). For a vertex of the right shore, degree \(a=2\) or \(a=4\), this forces exactly \(a/2\) incoming edges from the left: for degree 2 the only choice is one; for degree 4 the only choice is two. Thus a flow is exactly a binary \(a\)-by-\(2t\) matrix in which every column has sum \(a/2\), while each row sum satisfies \(r_i\equiv t\pmod3\). Conversely those conditions prove conservation on both shores.

The row sums obey \(0\le r_i\le2t\), so \(r_i=t+3s_i\), \(|s_i|\le d\). Counting the total number of ones forces \(\sum_i s_i=0\). Every allowed row vector is realizable. For \(a=2\) this is immediate. For \(a=4\), the Gale–Ryser inequalities for a binary matrix with \(2t\) column sums equal to two reduce, for one row, to \(r_i\le2t\), and for at least two rows to \(\sum r_i\le4t\), already satisfied; thus each row-sum vector is attained. A direct alternative is to regard each column as an edge in a loopless multigraph on the four row labels and realize the specified degrees.

A legal directed four-cycle reversal interchanges a \(2\)-by-\(2\) alternating binary submatrix, maintaining all margins. By the classical binary-matrix interchange theorem, every two binary matrices with identical row and column sums are connected by these interchanges. Conversely, any directed cycle reversal preserves the entire outdegree sequence. Hence the components are exactly the feasible row-sum sectors, with the coefficient formulas in the Finding section.

For \(a=2\), the sector count is \(2d+1\). For \(a=4\), it is the central coefficient \([z^{4d}](1+z+\cdots+z^{2d})^4\), equal by inclusion–exclusion to
\[
\binom{4d+3}{3}-4\binom{2d+2}{3}=
\frac{(2d+1)(8d^2+8d+3)}3.
\]
(The second binomial vanishes at \(d=0\) by the combinatorial convention.) An orientation has no legal four-cycle flip exactly when every column chooses the same set of rows; two distinct same-cardinality columns have a nonempty symmetric difference and yield an alternating \(2\)-by-\(2\) switch. By the interchange theorem an isolated state cannot exist without this property. All-identical columns satisfy the row congruences exactly when \(3\mid t\), giving \(\binom a{a/2}\) isolated flows.

For the total number of flow states, first let \(a=2\): the roots-of-unity filter on the column choices gives \((4^t+2)/3\). For \(a=4\) write \(\omega^2+\omega+1=0\), and \(e_2(x_1,x_2,x_3,x_4)=\sum_{i<j}x_ix_j\). The filter for all four row sums congruent to \(t\) gives
\[
F_4(t)=3^{-4}\sum_{(a_1,\ldots,a_4)\in(\mathbb Z/3)^4}
\left(\omega^{-\sum_i a_i}e_2(\omega^{a_1},\ldots,\omega^{a_4})^2\right)^t.
\]
Simultaneously adding one to all four residues does not change the parenthesized factor, so fix \(a_1=0\) and divide by 27 instead. Among the resulting exactly 27 triples, direct symbolic evaluation in \(\mathbb Z[\omega]\) gives factor 36 once, factor 9 fourteen times, and factor 0 twelve times. For reproducibility, the grouping by multiplicities \((n_0,n_1,n_2)\) of the three residues is: \((4,0,0):36\); \((3,1,0),(3,0,1),(2,2,0),(2,0,2),(1,3,0),(1,0,3):9\); all other multiplicities: 0. Accounting for the possible placements of the three free entries gives exactly 1, 14, 12. This proves \(F_4(t)=(36^t+14\cdot9^t)/27\).

## Verification
Run the standalone standard-library Python program `verify_flow.py` using `python3 verify_flow.py`. It checks the exact Eisenstein-integer character classification over all 27 residue triples; independently obtains total flow counts by full integer dynamic programming for \(1\le t\le10\); verifies sector-count formulas for \(1\le t\le29\); and builds the entire finite cycle-flip graph for \(a\in\{2,4\}\), \(1\le t\le4\), verifying each component, each size coefficient, the singleton counts and legality of all computed flips. These computational checks are supplementary to the unrestricted proof above.

## Relationship to prior work
Esperet and colleagues (2025) introduce the reconfiguration problem; Cranston, Li, Su, Wang and Xu (2026) study the pertinent order-three case, characterize \(\mathbb Z_3\)-flow connectivity and prove that directed-cycle reversal classes are distinguished by outdegree sequences. Their structural classification does not calculate the number, sizes or total populations of the components in these thin complete bipartite families. Goel (2026) proves an order-at-least-four group-flow connectivity theorem, highlighting the special behaviour at order three. Baggett and Yan (2026) discuss the classical binary-matrix interchange theorem in the context of a stronger interchange-graph Hamiltonicity result. The interchange theorem itself is not claimed as new. The present result supplies an exact sector and size census for every order in two natural families, including the 3-step component-count plateaus, and independent total-flow formulas. Searches did not find an equivalent published census; this is not a proof of historical priority.

## Limitations
Only the two specified left-shore sizes and the cyclic group of order three are covered. The result does not give component diameters or count shortest reconfiguration paths. Earlier results already imply some connectivity or nonconnectivity instances, so the novelty claim is the full quantitative classification, not the basic existence of multiple components. The original-priority search is necessarily nonexhaustive; no independent validation has been performed.

## References
1. L. Esperet, A. Lagoutte and M. Marseloo, *Nowhere-zero flow reconfiguration*, arXiv:2512.17342, first public version 2025-12-19, https://arxiv.org/abs/2512.17342. Later revisions have expanded author lists.
2. D. Cranston, Q. Li, B. Su, H. Wang and Y. Xu, *Reconfiguration of Nowhere-zero Flows*, arXiv:2606.24685, first public version 2026-06-23, https://arxiv.org/abs/2606.24685.
3. D. Goel, *The Cranston–Li–Su–Wang–Xu (2026) conjecture is true*, arXiv:2610.40863, first public version 2026-10-29, https://arxiv.org/abs/2610.40863.
4. D. Baggett and G. Yan, *Interchange graphs of (0,1)-matrices are maximally Hamiltonian*, arXiv:2607.13165, first public version 2026-07-14, https://arxiv.org/abs/2607.13165. The interchange connectivity theorem cited there is classical (Ryser).
