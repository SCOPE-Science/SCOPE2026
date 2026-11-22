# Mixed-dimensional sphere wedges for ordinary four-cut complexes of three-row rook graphs

## Finding
For every integer \(n\ge4\), let \(G_n=K_3\square K_n\) be the rook graph with vertex set \(V=[3]\times[n]\), adjacent when exactly one coordinate agrees. Let \(\Delta_4(G_n)\) be the **ordinary** four-cut complex, whose facets are complements of disconnected induced four-vertex sets, and let \(X_n=\Delta_4(G_n)^\vee\) be its combinatorial Alexander dual on the full \(3n\)-element ground set. Then
\[
X_n\simeq\bigvee^{n(n-1)(n-2)} S^2\ \vee\ 
\bigvee^{(n-1)(n-2)^2/2}S^3.
\]
Consequently the complete reduced **integral** homology of the original four-cut complex is
\[
\widetilde H_i(\Delta_4(G_n);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{(n-1)(n-2)^2/2},&i=3n-6,\\
\mathbb Z^{n(n-1)(n-2)},&i=3n-5,\\
0,&\text{otherwise}.
\end{cases}
\]
The original cut complex is pure of dimension \(3n-5\) and is not shellable over any coefficient field. The sphere-wedge statement is about the **dual**, not the original cut complex.

## Assumptions and scope
The graph is the Cartesian product of complete graphs, not the ordinary square-lattice path grid. Label rows \(0,1,2\) and columns \(0,\ldots,n-1\). A face of \(X_n\) is exactly a vertex set every four-element subset of which induces a connected subgraph; all sets of at most three cells are faces. Every homotopy equivalence refers to geometric realizations, with integral coefficients in all homology assertions. The range begins with \(n=4\); the nine-vertex \(n=3\) base instance is used only in the proof and consistency checks, not claimed as an additional new case.

## Proof
**1. Exact Alexander dual and rectangular decomposition.** By the definition of Alexander dual, \(A\subseteq V\) belongs to \(X_n\) if and only if it contains no disconnected induced four-set. A rook graph is the line graph of the complete bipartite row–column incidence graph: a selected set of board cells is connected in the rook graph precisely when its corresponding incidence edges form one edge-bearing component. A set of at least four cells meeting at least two rows cannot occupy four distinct columns, because four chosen incidence edges meeting both rows and four columns cannot connect all used incidence vertices. Similarly, a set of at least four cells meeting all three rows and at least three columns contains a four-set whose incidence edges meet all three rows and three columns; four edges cannot connect six incidence vertices. Thus every face of size at least four is contained either in one entire row, a two-row/three-column rectangle, or a three-row/two-column rectangle. Conversely, every subset of each of those rectangles has all its four-subsets connected: for a two-by-three rectangle two nonempty disconnected groups would require four disjoint column appearances, and for a three-by-two rectangle they would require four disjoint row appearances. A three-cell face not contained in these rectangular families necessarily occupies one cell in each row and three distinct columns. It cannot extend to any allowed four-face.

Let \(Y_n\) denote the union of the full simplices on (a) each whole row, (b) every two-row/three-column rectangle, and (c) every three-row/two-column rectangle. Let \(T_n\) be the set of three-cell transversals with distinct columns. We have the **exact simplicial decomposition**
\[
X_n=Y_n\cup\bigcup_{\tau\in T_n}\tau,
\qquad |T_n|=3!\binom n3=n(n-1)(n-2),
\]
where each \(\tau\) is an additional two-simplex whose entire boundary already lies in \(Y_n\), and no additional face contains it. This characterization has no asymptotic or generic-position qualifications.

**2. All-parameter acyclic matching of the rectangular core.** Order the cells first by row, then by column: \((0,0),\ldots,(0,n-1),(1,0),\ldots,(2,n-1)\). On the face poset of \(Y_n\), perform successive *vertex-toggle element matchings*: at the current cell \(v\), pair every still-unmatched face \(F\) avoiding \(v\) with \(F\cup\{v\}\) whenever both are still unmatched; remove these pairs before processing the next cell. Pair the empty face with \(\{(0,0)\}\) in the augmented poset, or equivalently retain this vertex as the single critical zero-cell in the nonempty face poset. These pairs are disjoint, and the sequential element-matching lemma proves acyclicity: in a hypothetical closed gradient path, choose the earliest pivot of a matched upward step. All earlier toggles were exhausted; removal of that pivot at a later downward step would force an earlier matched pivot in the path, contradicting minimality. The same argument rules out cycles entirely within one pivot stage.

For completeness, the following gives the **uniform critical-cell calculation**, rather than an extrapolation from small numerical examples. Apply the stated toggle rule to the three types of rectangular faces. Its terminal unmatched nonempty faces, apart from the chosen zero-cell, are exactly these four-element sets:

* \(\{(r,0),(r,a),(r,b),(r,c)\}\), where \(r\in\{1,2\}\) and \(1\le a<b<c<n\);
* \(\{(1,a),(2,a),(2,b),(2,c)\}\), where \(0\le a<b<c<n\).

Here is an inductive case audit of that calculation. For the three-column base case, the second family has the sole representative \(\{(1,0),(2,0),(2,1),(2,2)\}\), while no first-family face exists. Append a new last column indexed \(n\) and reapply the same row-major toggle rule. Faces meeting only one row contribute new unmatched faces only for rows \(1,2\), in which case their four columns are \(0,n\) and two of \(1,\ldots,n-1\): precisely \(2\binom{n-1}{2}\) faces. Faces meeting two rows contribute an unmatched face only when row \(1\) occupies the minimum of three used columns and row \(2\) occupies all three, with the new column included: precisely \(\binom n2\) faces. Faces meeting three rows contribute none. Faces not using the new column retain exactly their old terminal status. To check these three rows of the audit directly, use that a multirow face with at least four cells has at most three occupied columns, split according to one, two or three cells in the new column, and in each case toggle the first row-major available cell; if both the deletion and insertion faces remain, they are paired immediately. The only configurations in which that toggle is unavailable are the two displayed families. The single-row case reduces to toggling column zero or the smallest remaining column and gives the four-cell condition above. This is an induction over all column counts, not an experiment over a finite interval.

Thus the only positive-dimensional critical cells of \(Y_n\) are in dimension three, numbering
\[
2\binom{n-1}{3}+\binom n3=\frac{(n-1)(n-2)^2}{2}.
\]
Ordinary discrete Morse theory produces a CW complex with one zero-cell, that many three-cells, and no cells of any other positive dimension. Since their attaching maps go to a point, \(Y_n\simeq\bigvee^{(n-1)(n-2)^2/2}S^3\). In particular \(Y_n\) is simply connected.

**3. Independent two-sphere attachments.** Every boundary \(\partial\tau\cong S^1\) of a transversal triangle lies in the simply connected \(Y_n\), so its attaching map is nullhomotopic. Adding all the distinct triangular two-cells, none of which is a face of another added cell, is homotopy equivalent to wedging one \(S^2\) for each transversal. This gives the first claimed homotopy equivalence integrally, including the absence of torsion or additional higher homology.

**4. Duality and shellability.** Combinatorial Alexander duality on \(N=3n\) vertices gives \(\widetilde H_i(\Delta_4(G_n);\mathbb Z)\cong\widetilde H^{N-i-3}(X_n;\mathbb Z)\). The computed dual homology is free, so the universal coefficient theorem yields exactly the displayed degrees and ranks. Every cut facet is the complement of a disconnected four-set, hence has size \(N-4\) and dimension \(N-5\). As the rank in degree \(N-6\) is positive, a pure shellable or Cohen–Macaulay complex is impossible.

## Verification
The self-contained `evidence/verify.py` is executable with standard Python 3. It independently constructs the Alexander dual directly from **all** vertex subsets and the original connected-four-set predicate for \(n=3,4,5,6\), and compares it with the rectangular decomposition. For \(n=3,\ldots,8\), it regenerates the complete row-major element matching on both \(X_n\) and \(Y_n\), compares every critical face with closed-form critical sets, checks the complete Hasse-diagram orientation for acyclicity at \(n\le7\), and independently computes ordinary mod-two boundary ranks for \(n\le6\). An additional check of the rectangular-core critical pattern at \(n=9,10,12\) was also performed during verification. These finite checks corroborate, but do not replace, the all-parameter rectangle classification and matching induction in the proof. The stored successful execution output is `evidence/verification-output.txt`.

## Relationship to prior work
Bayer–Denker–Jelić Milutinović–Rowlands–Sundaram–Xue introduce ordinary cut complexes and analyze trees, cycles, multipartite graphs and clique prisms, including \(K_2\square K_n\), but not this \(K_3\square K_n\) four-cut family [1]. Their sequel's grid graphs are \(P_m\square P_n\), with path rather than complete-graph factors [2]. Previously indexed rook-graph work determines the three-cut homology for arbitrary board sizes [3], and the four-cut integral homology of \(K_4\square K_4\) [4]. Neither statement implies the present three-row four-cut formula. The nine-vertex \(K_3\square K_3\) special case was already determined separately and is not claimed as original; the present contribution is the all-length formula starting at four columns and its uniform Morse mechanism. No analogous full theorem was found in the inspected indexed literature, but this cannot establish priority against unindexed sources.

## Limitations
This theorem determines the dual's homotopy type and the original cut complex's additive integral homology, not the original complex's homotopy type, the full symmetry representation, or cut sizes other than four. The matching induction is the essential nonstandard mathematical step; finite enumerations cannot independently establish its all-parameter validity. Independent external validation is not asserted. Bibliographic incompleteness, especially unindexed equivalent formulations using four-uniform hypergraph independence complexes, remains a risk.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first posted 26 April 2023, especially Sections 1 and 7.3, https://arxiv.org/abs/2304.13675.
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first posted 11 July 2024, Section 5, https://arxiv.org/abs/2407.08158.
3. *Integral and equivariant homology of three-cut complexes of rook graphs*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-integral-and-equivariant-homology-of-three-cut-complexes-of-rook--bd50464fc17f.
4. *Integral four-cut homology separates the Shrikhande and rook graphs*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-integral-four-cut-homology-separates-the-shrikhande-and-rook-gra--de2f98e55b1f.
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
