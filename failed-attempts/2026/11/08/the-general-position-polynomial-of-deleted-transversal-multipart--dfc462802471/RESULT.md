# The general-position polynomial of deleted-transversal multipartite graphs and a sharp four-part unimodality window

## Finding

For integers \(a,r\ge3\), let \(T^*(r,a)\) have vertex set \([a]\times[r]\), with \((i,j)\) adjacent to \((i',j')\) precisely when \(i\ne i'\) and \(j\ne j'\). Equivalently, start with a complete \(a\)-partite graph with \(r\) vertices per part and delete the edges of its \(r\) disjoint transverse \(a\)-cliques. It is the direct graph product \(K_a\times K_r\) (not the Cartesian product).

A vertex set is in general position when no three of its vertices lie on one graph geodesic. If \(\psi_{a,r}(z)=\sum_k g_k z^k\) counts its general-position sets of size \(k\), then

\[
\begin{aligned}
\psi_{a,r}(z)={}&1+ar z+\binom{ar}{2}z^2\\
&+\sum_{k\ge3}\left[a\binom{r}{k}+r\binom{a}{k}+k!\binom{a}{k}\binom{r}{k}\right]z^k\\
&+4\binom a2\binom r2 z^3+\binom a2\binom r2 z^4.
\end{aligned}
\]

Here \(\binom nk=0\) for \(k>n\). In particular, **for all integers \(r\ge3\)** the polynomial \(\psi_{4,r}\) is unimodal if and only if
\[
\boxed{3\le r\le11\quad\text{or}\quad r\ge40.}
\]
Thus \(12\le r\le39\) is exactly the finite, uninterrupted nonunimodal window for four parts.

## Assumptions and scope

All graphs are finite, simple, undirected, and labeled by the specified ordered coordinate pairs. The result concerns the full cardinality polynomial, including the empty set, and unimodality means coefficients first weakly increase and then weakly decrease. The theorem assumes both \(a\ge3\) and \(r\ge3\); it does not claim the same formula for the diameter-three boundary \(a=2\) or \(r=2\). The four-part classification means the number of parts \(a=4\), not four vertices per part.

## Proof

**1. Distance-two reduction.** Every two distinct vertices either are adjacent, or share one coordinate. In the latter case a common neighbor having both coordinates distinct from the corresponding coordinates exists because \(a,r\ge3\). Consequently \(T^*(r,a)\) has diameter exactly two. For any selected triple \(p,q,s\), a forbidden geodesic occurs precisely when \(p,s\) are nonadjacent and \(q\) is adjacent to both, or a permutation thereof. Hence a set is in general position if and only if its induced graph has no induced three-vertex path: it is a disjoint union of cliques. The more general clique-component characterization of general-position sets is known; this diameter-two reduction is included to make the current proof self-contained.

**2. Exhaustion of possible sets with at least three vertices.** View vertices as cells in an \(a\)-by-\(r\) array. A clique consists of cells with all row coordinates distinct and all column coordinates distinct. An independent set consists of cells pairwise sharing a row or a column. For size at least three, such an independent set lies entirely in a single row or a single column: if two different rows occurred, all cells must share their common column, and symmetrically for columns.

If an induced clique has size at least three, no outside cell is nonadjacent to every vertex of that clique, since a cell can share at most one row and one column with the distinct-coordinate clique. Therefore it cannot be accompanied by another component. If the largest component is an edge with endpoints \((i,p)\), \((j,q)\), its only possible vertices outside that component are the cross cells \((i,q)\) and \((j,p)\). Either one cross cell gives an edge plus an isolated vertex; choosing both gives two disjoint edges. No further cells are possible. These four forms (row/column independent sets, one clique, a three-corner rectangle, and a four-corner rectangle) are exhaustive and disjoint for sizes at least three.

**3. Exact enumeration.** A row of \(r\) cells contributes \(\binom rk\) independent \(k\)-sets, and a column of \(a\) cells contributes \(\binom ak\); this gives \(a\binom rk+r\binom ak\) for \(k\ge3\). A \(k\)-clique chooses \(k\) rows, \(k\) columns and their bijection, giving \(k!\binom ak\binom rk\). Each choice of two rows and two columns yields four three-corner sets and one four-corner set. Finally, every one- and two-vertex set is in general position, contributing \(1,ar,\binom{ar}{2}\). Adding disjoint classes proves the polynomial.

**4. The four-part coefficients.** Setting \(a=4\) gives
\[
\begin{gathered}
 b_0=1,\quad b_1=4r,\quad b_2=\binom{4r}{2},\\
 b_3=28\binom r3+24\binom r2+4r,\\
 b_4=28\binom r4+6\binom r2+r,\\
 b_k=4\binom rk\qquad(k\ge5).
\end{gathered}
\]
In particular \(b_0<b_1<b_2<b_3\) for all \(r\ge3\):
\[
 b_3-b_2=\frac{2r(7r^2-15r+5)}3>0.
\]
Also
\[
 b_4-b_3=\frac{r(7r^3-70r^2+107r-62)}6.
\]
This difference is negative for the six integers \(3\le r\le8\) and positive for every \(r\ge9\). For the latter, the cubic is positive at \(r=9\), and its derivative \(21r^2-140r+107\) is positive and increasing on \([9,\infty)\).

**5. Sharp coefficient valley.** The decisive difference is
\[
 b_5-b_4=\frac r{30}P(r),\qquad P(r)=r^4-45r^3+245r^2-525r+294.
\]
On \([12,20]\), \(P''(r)=12r^2-270r+490<0\), whereas on \([21,\infty)\) it is positive. Also \(P'(12)=-7173\), \(P'(29)=-2294\), and \(P'(30)=675\). Thus \(P\) decreases through \([12,29]\), then has its unique minimum between 29 and 30, and increases on \([30,\infty)\). Since \(P(12)=-27750\) and \(P(39)=-3450\), it is strictly negative throughout \([12,39]\); \(P(40)=51294>0\), and it is positive for all larger \(r\).

For each \(12\le r\le39\), we therefore have \(b_4>b_5\), while
\[
 b_6/b_5=(r-5)/6>1.
\]
The strict valley \(b_4>b_5<b_6\) proves nonunimodality for precisely this interval. For \(r\ge40\), the preceding formulas give \(b_0\le\cdots\le b_5\), and the remaining terms \(4\binom rk\) form a unimodal binomial tail. Hence the full polynomial is unimodal.

Finally, for \(3\le r\le8\), the finite exact inequalities \(b_3>b_4\ge b_5\ge\cdots\) hold, and for \(9\le r\le11\), \(b_4>b_5\ge b_6\ge\cdots\) hold with \(b_4>b_3\). They follow by substitution in the displayed low-degree formulas and by \(\binom r{k+1}/\binom rk=(r-k)/(k+1)\) for \(k\ge5\). Thus these nine small cases are unimodal. This completes the classification.

## Verification

The accompanying standalone `gp_tensor_verify.py` independently builds \(K_a\times K_r\), calculates all-pairs shortest-path distances, and checks every vertex subset for forbidden geodesic triples. For six labeled graphs with \((a,r)\in\{(3,3),(3,4),(4,3),(3,5),(5,3),(4,4)\}\), it examines all \(139776\) vertex subsets and obtains the exact predicted polynomial. In particular,
\[
 \psi_{3,3}(z)=1+9z+36z^2+48z^3+9z^4,
\]
\[
 \psi_{4,3}(z)=1+12z+66z^2+112z^3+21z^4.
\]
It additionally checks the four-part unimodality criterion for every integer \(3\le r\le1000\) using exact integers. These finite checks corroborate the proof but do not prove its unrestricted quantifiers.

Run from any directory after extracting the named file with `python3 gp_tensor_verify.py`; it requires only the Python standard library.

## Relationship to prior work

Tuite, Thomas and Chandran introduced the deleted-transversal multipartite construction for extremal position problems (arXiv:2106.06827, first public 2021-06-12). Their result concerns an extremal graph invariant, not the present cardinality census. Anand, Chandran, Changat, Klavžar and Thomas (arXiv:1812.08460, Theorem 3.1) characterized general-position sets abstractly using clique components and distances; the diameter-two specialization is a known premise and is not claimed as new.

Iršič, Klavžar, Rus and Tuite (arXiv:2401.05696, posted 2024-01-11; published in *Results in Mathematics* 79, article 110) studied this exact graph in Section 4, displayed a counting expression, and posed Problem 5.2 asking for its unimodality classification. The displayed expression is **not equivalent to the exact labeled enumeration** above: for \(a=r=3\), its cubic coefficient is \(66\), whereas graph-level enumeration and the present structural proof both give \(48\). The source's \(r^k\binom ak\) term counts unrestricted label assignments across different parts, including forbidden geodesic triples; the corrected count separates equal-label independent sets and injectively labeled cliques. Therefore the prior displayed formula does not imply this theorem. The present sharp four-part window is not supplied there. This is a mathematical discrepancy, not a judgment of the other results in the source.

Rather (arXiv:2603.06930, 2026) considers general-position polynomials of ordinary complete multipartite graphs and graph coronas. Those have different edges from the deleted-transversal graph here. The abstract was checked, not its full manuscript.

## Limitations

The formula is only asserted for \(a,r\ge3\); boundary cases with a coordinate set of size two can have distance three. The statement is a structural/counting theorem, not a complete resolution of Problem 5.2 for arbitrary \(a\). Exact finite enumeration cannot exclude undiscovered equivalent literature. In particular, an unindexed correction to the 2024 displayed formula or a separate enumeration for categorical products remains a publication-priority risk. An independent mathematical audit has not been performed.

## References

- J. Tuite, E. J. Thomas and U. S. V. Chandran, *On some extremal position problems for graphs*, arXiv:2106.06827 (first posted 2021-06-12). https://arxiv.org/abs/2106.06827
- V. Iršič, S. Klavžar, G. Rus and J. Tuite, *General Position Polynomials*, arXiv:2401.05696 (first posted 2024-01-11); *Results in Mathematics* 79 (2024), 110, DOI 10.1007/s00025-024-02133-3. https://link.springer.com/article/10.1007/s00025-024-02133-3
- B. S. Anand, U. S. V. Chandran, M. Changat, S. Klavžar and E. J. Thomas, *Characterization of general position sets and its applications to cographs and bipartite graphs*, arXiv:1812.08460, Theorem 3.1. https://arxiv.org/abs/1812.08460
- B. A. Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930 (2026), abstract-level relevance check only. https://arxiv.org/abs/2603.06930
