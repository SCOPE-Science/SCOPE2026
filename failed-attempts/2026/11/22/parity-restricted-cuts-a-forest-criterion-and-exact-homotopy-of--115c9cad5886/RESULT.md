# Parity-restricted cuts: a forest criterion and exact homotopy of the complete-graph shattering complex

## Finding
Let \(G=(V,E)\) be any finite simple graph on \(n\ge2\) labeled vertices. Let \(\mathcal C_G\) be the Boolean concept class on \(E\) consisting of the cut indicators \(\mathbf1_{\delta_G(S)}\) for all vertex sets \(S\subseteq V\) of even cardinality. Then an edge-query support \(F\subseteq E\) is VC-shattered by \(\mathcal C_G\) **if and only if** \((V,F)\) is a forest and has at least one connected component of odd order. In particular, writing \(c(G)\) for the number of components of \(G\),
\[
\operatorname{VCdim}(\mathcal C_G)=\operatorname{Ldim}(\mathcal C_G)
=\begin{cases}
n-c(G),&G\text{ has a component of odd order},\\
n-c(G)-1,&\text{all components of }G\text{ have even order}.
\end{cases}
\]
The shattered-support complex is the independence complex of a binary matroid; when \(n\) is even and all connected components of \(G\) have even order, its dual is the even-cut matroid associated with the graft \((G,V)\). This identification as a matroid is standard in the even-cut framework and is not claimed as a newly discovered matroid species.

For the complete graph \(K_n\), define \(t_1=1\) and \(t_j=j^{j-2}\) for \(j\ge2\). The complete polynomial enumerating shattered supports by their number of edges is
\[
\Phi_n(z)=n![x^n]\left[
\exp\!\left(\sum_{j\ge1}\frac{t_j x^j z^{j-1}}{j!}\right)-
\exp\!\left(\sum_{j\ge1}\frac{t_{2j}x^{2j}z^{2j-1}}{(2j)!}\right)
\right],\qquad n\ge2.
\]
For even \(n\ge4\), the resulting complex is homotopy equivalent over the integers to a wedge of \(b_n\) spheres of dimension \(n-3\), with
\[
 b_n=n![x^n]\left[
\exp\!\left(\sum_{j\ge1}\frac{(-1)^{j-1}t_j x^j}{j!}\right)-
\exp\!\left(-\sum_{j\ge1}\frac{t_{2j}x^{2j}}{(2j)!}\right)
\right].
\]
Its first values are \(b_4=7\), \(b_6=511\), \(b_8=98099\), and \(b_{10}=36215281\). For odd \(n\ge3\), it is the usual complete-graph graphic-matroid independence complex, of dimension \(n-2\).

## Assumptions and scope
All graphs are finite, undirected, loopless and without multiple edges; isolated vertices are allowed and count as components of order one. A cut \(\delta_G(S)\) is the set of edges with exactly one endpoint in \(S\). The shore parity means \(|S|\equiv0\pmod2\), not parity of the number of cut edges. Shattering means all \(2^{|F|}\) binary edge labels occur, including the empty pattern. Littlestone dimension refers to binary membership queries on edges, with the standard complete realizable decision-tree convention. The polynomial includes the empty support. All graph components, including isolated vertices, are counted in the forest condition.

## Proof
**1. Linear trace criterion.** Work over \(\mathbb F_2\). For a vertex indicator \(s\in\mathbb F_2^V\), the label of edge \(uv\) is \(s_u+s_v\). Allowed shores form \(H=\{s:\sum_v s_v=0\}\). The map \(H\to\mathbb F_2^F\) is linear. It is surjective exactly when its columns are linearly independent on \(H\); this is equivalent to the absence of a nonempty edge subset \(J\subseteq F\) with
\[
\sum_{e=uv\in J}(s_u+s_v)=0\quad\text{for all }s\in H.
\]
The left side equals \(\sum_v(\deg_J(v)\bmod2)s_v\). Since \(H^\perp=\langle\mathbf1_V\rangle\), a nonzero dependency occurs precisely if the degree-parity vector of \(J\) is either all zero or all one.

**2. Forest obstruction.** Any graph cycle is a nonempty all-even-degree edge subset, so a shattered support is a forest. Conversely, in a forest no nonempty edge subset has all even degrees (delete a leaf in any nonempty component). For a tree on vertex set \(W\), the mod-two degree map on its edges is a bijection onto the even-weight vectors on \(W\): injectivity follows from the leaf argument, and both spaces have dimension \(|W|-1\). Therefore a subset of forest edges can have odd degree at *every* vertex of \(V\) if and only if each component of \((V,F)\) has even order. This proves the stated if-and-only-if criterion, including the case of isolated vertices.

**3. Dimensions.** Any shattered forest has at most \(n-c(G)\) edges. If \(G\) has an odd-order component, any spanning forest of \(G\) has an odd component and attains this bound. If all components of \(G\) have even order, every spanning forest is excluded. Delete a leaf-edge in any spanning tree of any component: the resulting forest has at least one odd component and has exactly \(n-c(G)-1\) edges, attaining the reduced bound. The class \(\mathcal C_G\) is a binary linear space of edge labels. Its dimension equals the column rank, which is its VC dimension. A basis of coordinate functionals gives a fixed shattered support of that size, hence an adaptive tree of equal depth. Conversely any complete Littlestone tree of depth \(d\) has \(2^d\) distinct concept vectors, so \(d\le\log_2|\mathcal C_G|=\dim\mathcal C_G\). Thus both dimensions coincide.

**4. Exact enumeration.** For \(K_n\), the support is a labeled spanning forest (allowing singleton components). A tree on \(j\) labeled vertices has \(t_j=j^{j-2}\) choices, with \(t_1=1\). The labeled exponential formula with one factor \(z\) per edge yields the first exponential in \(\Phi_n\). The excluded forests are precisely those all of whose components have even orders; restricting tree sizes to \(2,4,6,\dots\) yields the second exponential. Their difference is exactly the shattered-support polynomial coefficient by coefficient.

**5. Integral homotopy.** The column-independence description proves that the supports form a representable matroid complex. Its rank is \(n-2\) for even \(n\) and \(n-1\) for odd \(n\), because \(K_n\) is connected. The standard shellability theorem for matroid independence complexes therefore gives a wedge of spheres in the unique top dimension \(r-1\), with torsion-free integral homology. The sphere multiplicity is \((-1)^r\Phi_n(-1)\). Here \(r\) is even for both parities of \(n\), so it is \(\Phi_n(-1)\). Substituting \(z=-1\) in the even-order formula gives the stated signed-tree exponential expression. This also identifies all lower reduced integral homology groups as zero.

## Verification
Two independent exhaustive checks were run for \(n=3,4,5,6\). The Python implementation directly enumerates allowable shore cuts and all patterns on each edge support; the C++17 implementation forms the linear restriction matrix and checks binary column rank. Both independently compare their results to the forest/odd-component criterion. The exact polynomials were independently regenerated by a species-type exponential recurrence and by a distinguished-root component recurrence, agreeing through \(n=10\). A separate simplicial-boundary computation over \(\mathbb F_2\) checked the ranks for \(n=4\) and \(6\) and produced top Betti numbers \(7\) and \(511\). The verifiers are supplied as standalone files. These finite checks corroborate, but do not replace, the proof for arbitrary \(G\) and \(n\).

Selected complete-graph face polynomials are
\[
\Phi_4(z)=1+6z+12z^2,\qquad
\Phi_6(z)=1+15z+105z^2+420z^3+840z^4,
\]
\[
\Phi_8(z)=1+28z+378z^2+3220z^3+18760z^4+73248z^5+155456z^6.
\]

## Relationship to prior work
Guenin and Pivotto's even-cut-matroid framework already identifies even shore cuts of a graft as the cycle space of a binary matroid and provides the appropriate duality vocabulary. The matroid representation is credited, not asserted as novel. Bujtás, Jendrol' and Tuza (first public February 2019) describe parity-prescribed degree forests and recall the classical \(T\)-join existence theorem; their studied objects are factors with degree restrictions, not VC traces of the even-shore cut class. Adler, Benediktsson and Macpherson (2020 preprint) study VC dimensions of graph-neighborhood relations, not edge-query traces of parity-constrained cuts. A related published research record treats *fixed-size* shores; a union over all even shore sizes does not inherit its trace characterization merely by taking a union of its shattered-support sets. Direct searches for the complete even-shore trace law, the signed forest polynomial, and the specialized homotopy multiplicities did not locate an equivalent published statement. This is a best-knowledge originality assessment, not certification of historical priority.

## Limitations
The theorem concerns binary cut labels and even shore size, not fixed shore sizes or edge-count parity of the cut. The homotopy and coefficient formulas here are complete-graph specializations; no explicit closed face polynomial or homotopy classification is asserted for arbitrary input graphs beyond their matroidality and rank. Ordinary matroid shellability and Cayley's labeled-tree formula are used as established results, not reproved. No independent audit or exhaustive survey of inaccessible literature has been completed; overlapping general matroid results could yield the formula by unrecorded specializations.

## References
1. C. Bujtás, S. Jendrol' and Z. Tuza, *On specific factors in graphs*, arXiv:1902.08689, first publicly posted 2019-02-22, especially Section 2 and Theorem 3. https://arxiv.org/abs/1902.08689
2. B. Guenin and I. Pivotto, *Stabilizer theorems for even cut matroids*, public full text dated 2016-06-10, Section 2.1 (graft/even-cut and \(T\)-join conventions). https://www.math.uwaterloo.ca/~bguenin/papers/stable.pdf
3. I. Adler, B. G. Benediktsson and D. Macpherson, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042, first posted 2020-07-31. https://arxiv.org/abs/2007.16042
4. A. Banik et al., *Cuts in Graphs with Matroid Constraints*, ESA 2024, DOI:10.4230/LIPIcs.ESA.2024.17; distinct vertex-cut optimization questions. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2024.17
5. Standard results used: Cayley's formula for labeled trees, the labeled exponential formula, and the shellability of matroid independence complexes.
