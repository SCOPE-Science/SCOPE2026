# Chromatic-cycle census and frozen minima in cyclic tensor products

## Finding
Let \(k\ge 2\) and \(q\ge 3\) be integers. In the categorical (direct/tensor) graph product \(G=C_{3k}\times K_q\), the minimum independent dominating sets are **exactly** the following: choose one of the three cyclic residues modulo \(3\), leave every cycle fiber of that residue empty, and in each pair of consecutive remaining fibers choose one vertex of the same complete-graph color. The colors on successive pairs must differ, including across the cyclic boundary.

In particular, the independent domination number (known previously) is \(i(G)=2k\), while the number of *labeled vertex sets* realizing that minimum is
\[
N_{k,q}=3\operatorname{tr}\bigl((J_q-I_q)^k\bigr)=3\bigl((q-1)^k+(-1)^k(q-1)\bigr),
\]
where \(J_q\) is the all-ones matrix and \(I_q\) the identity matrix. Moreover, **any two distinct minimum independent dominating sets differ in at least two deleted and two inserted vertices**. Therefore the token-jumping reconfiguration graph on the minimum sets, with edges joining sets related by a single vertex replacement, is edgeless. In particular, the usual token-sliding \(i\)-graph is edgeless as well.

## Assumptions and scope
All graphs are finite, simple, undirected and vertex-labeled. The vertices of \(C_{3k}\) are \(0,\ldots,3k-1\) with indices interpreted cyclically, and the complete-graph colors are \(1,\ldots,q\). The product has vertex set \(\{(j,c)\}\) and two *distinct* vertices \((j,c)\), \((j',c')\) are adjacent exactly when \(j'\equiv j\pm 1\pmod{3k}\) and \(c'\ne c\). An independent dominating set is an independent set whose closed neighborhood is every vertex, equivalently an inclusion-maximal independent set. A *minimum* one has least cardinality among such sets. The token-jumping graph has these minimum sets as vertices and an edge precisely when the two sets have symmetric difference of cardinality two; its token-sliding subgraph also requires the exchanged vertices to be adjacent in the original graph.

The results concern all integers \(k\ge2\), \(q\ge3\), **not** arbitrary cycle lengths or the case \(q=2\). The enumeration does not identify sets under graph automorphisms or color permutations.

## Proof
Write \(S_j=\{c:(j,c)\in S\}\) for the fiber of an independent dominating set \(S\). First \(|S_j|\in\{0,1,q\}\). Indeed, if a fiber contains at least two but fewer than \(q\) colors, independence forces both neighboring fibers to be empty, leaving each unselected vertex in the fiber undominated. Denote an empty fiber by \(0\), a singleton fiber by its color \(c\), and a full fiber by \(F\). Direct inspection of adjacency and domination gives the following necessary and sufficient local rules.

* A fiber labeled \(F\) has two neighboring \(0\) fibers.
* A fiber labeled \(c\) has neighbors in \(\{0,c\}\) and at least one neighbor labeled \(c\).
* A fiber labeled \(0\) either has an \(F\) neighbor or has two singleton neighbors with different colors.

These three rules are sufficient as well: every omitted color in a singleton fiber sees an equal-colored selected singleton in an adjacent fiber; every vertex in a zero fiber sees a chosen neighbor of a different color; full fibers are selected outright. The same rules ensure independence.

Let \(f,s,e\) denote the numbers of \(F\), singleton, and zero fibers. Then \(3k=f+s+e\) and \(|S|=qf+s=3k-e+(q-1)f\). Every maximal cyclic run of singleton fibers has length at least two and is monochromatic. Among the zero fibers, at most \(2f\) have an \(F\) neighbor. Every other zero fiber has singleton neighbors, and can be charged injectively to a singleton run, of which there are at most \(s/2\). Consequently
\[
e\le 2f+\frac{s}{2},\qquad e\le k+f,\qquad |S|\ge 2k+(q-2)f.\]
Since \(q\ge3\), every minimum candidate with \(|S|\le 2k\) must have \(f=0\). Now \(e\le s/2\) and \(|S|=3k-e\ge2k\). Equality requires \(e=k\), \(s=2k\), and every monochromatic singleton run to have length exactly two. Therefore the zeros occupy exactly one residue class modulo three. The local zero-fiber rule further forces the colors of the \(k\) successive two-fiber runs to form a proper cyclic \(q\)-coloring. Conversely, every such choice satisfies all local rules and has cardinality \(2k\); proper cyclic colorings exist because \(k\ge2\) and \(q\ge3\). This proves both the minimum and the exhaustive structure.

There are exactly three choices of zero residue. For each one, the colors form a length-\(k\) cyclic word with consecutive colors distinct, including the last and first. For \(k=2\), the same condition just requires the two colors to differ. The count is \(\operatorname{tr}((J_q-I_q)^k)\): the eigenvalues are \(q-1\) once and \(-1\) with multiplicity \(q-1\). Hence the stated formula follows.

Finally, two distinct choices of zero residue have disjoint zero-fiber sets of size \(k\), so each minimum set has at least \(k\ge2\) selected vertices absent from the other. With the same residue, two different solutions differ in the color of at least one *two-fiber* run; both chosen vertices in that run change. Thus distinct minima differ by at least two removals and two additions, proving there is no one-token jump and no token slide. \(\square\)

## Verification
The accompanying standalone Python program `checker.py` uses two independent methods. It enumerates cycle-fiber words and applies the three local rules for \((k,q)=(2,3),(2,4),(2,5),(3,3),(3,4),(4,3),(5,3)\), compares their optimum counts with the formula, and checks pairwise absence of token jumps. Independently, it constructs actual product-graph adjacency and exhaustively tests all vertex subsets of cardinality at most \(2k\) for \((k,q)=(2,3),(2,4),(3,3)\), confirming that no smaller independent dominating set exists and that the complete minimum-set lists agree. The tests are finite cross-checks only; the proof covers all parameters.

Reproduce with `python checker.py` using Python 3 and only the standard library.

## Relationship to prior work
Kuenzel and Rall, *On independent domination in direct products*, arXiv:2203.12397v1 (first public 2022-03-23), establish the independent domination number of \(C_m\times K_q\) and give general weak-partition conditions describing independent dominating sets of products with complete graphs. The value \(i(C_{3k}\times K_q)=2k\) and the underlying fiber-label vocabulary are **not claimed as new**. The contribution here is the equality-case rigidity for multiples of three, its complete **minimum-set multiplicity**, and the **frozen minimum-solution reconfiguration** conclusion; these are not statements supplied by that paper's scalar formula or its displayed optimum constructions.

Brewster, Mynhardt and Teshima, *The \(i\)-Graphs of Paths and Cycles*, arXiv:2303.08190v1 (2023), study the reconfiguration of minimum independent dominating sets of individual paths and cycles. Their graph family is different; the product result above is not one of their classifications. Bednarz, *On (2-d)-Kernels in the Tensor Product of Graphs*, Symmetry 13 (2021), article 230, counts independent **two-dominating** sets, a strictly stronger condition than ordinary domination. In particular the reported least two-dominating kernel size for \(C_m\times K_q\) is \(m\), not the ordinary independent domination number \(2m/3\) here.

## Limitations
This is not an enumeration of all independent dominating sets or all minimum sets when the cycle order is not divisible by three. It makes no claim about the higher-cardinality reconfiguration graph or arbitrary graph products. Literature searches and full-text comparison of the most relevant accessible work did not identify the exact cardinality census and isolation statement, but an unindexed or differently framed prior result is possible. The general fiber representation overlaps an explicitly credited published lemma.

## References
1. K. Kuenzel and D. F. Rall, *On Independent Domination in Direct Products*, arXiv:2203.12397v1 (2022-03-23), subsequently *Graphs and Combinatorics* 39, 7 (2023), DOI 10.1007/s00373-022-02600-0.
2. R. C. Brewster, C. M. Mynhardt and L. E. Teshima, *The \(i\)-Graphs of Paths and Cycles*, arXiv:2303.08190v1 (2023-03-14).
3. P. Bednarz, *On (2-d)-Kernels in the Tensor Product of Graphs*, *Symmetry* 13 (2021), article 230, DOI 10.3390/sym13020230.
