# Open-independent locating codes of rook graphs: a sharp modulo-three census

## Finding
For positive integers \(a,b\), let \(R_{a,b}=K_a\square K_b\), with its vertices identified with the cells \([a]\times[b]\). Two distinct cells are adjacent when they have a common row or a common column. An **open-independent open-locating-dominating set** (an \(\mathrm{OLD}_{\mathrm{oind}}\)-set) is a set \(S\) for which all signatures \(N(x)\cap S\), for \(x\in V(R_{a,b})\), are nonempty and pairwise distinct, while each vertex in \(S\) has exactly one neighbor in \(S\).

The following three cases describe **all** such sets, and they are mutually exclusive.

1. If \(a+b\equiv0\pmod3\) and \(a\le2b\), \(b\le2a\), put \(h=(2b-a)/3\) and \(v=(2a-b)/3\). The sets are precisely the collections of \(h\) horizontal two-cell dominoes and \(v\) vertical two-cell dominoes, with every row and column used exactly once as a line belonging to a domino. There are
   \[
   C_{a,b}=\frac{a!b!}{2^{h+v}h!v!}
   \]
   such sets, each of cardinality \(2(h+v)=2(a+b)/3\).
2. If \(b=2a+1\), the sets are precisely \(a\) horizontal dominoes that use each row and all but one column. There are \(C_{a,b}=b!/2^a\) sets, each of size \(2a\).
3. If \(a=2b+1\), the sets are precisely \(b\) vertical dominoes that use each column and all but one row. There are \(C_{a,b}=a!/2^b\) sets, each of size \(2b\).

For all other positive \(a,b\), there are no such sets. The dominoes are disjoint in the stronger sense that no two different dominoes use a common row or a common column. Thus every admissible rook graph has all its \(\mathrm{OLD}_{\mathrm{oind}}\)-sets of the same cardinality, and its complete size enumerator is a single monomial \(C_{a,b}z^{|S|}\). With \(C_{a,b}=0\) for absent cases, the bivariate exponential generating function is
\[
\sum_{a,b\ge1}\frac{C_{a,b}}{a!b!}X^aY^b
=\exp\left(\frac{XY^2+X^2Y}{2}\right)-1
 +X\left(\exp\left(\frac{X^2Y}{2}\right)-1\right)
 +Y\left(\exp\left(\frac{XY^2}{2}\right)-1\right).
\]
For example, \(C_{3,3}=9\), \(C_{2,5}=30\), \(C_{4,5}=180\), and \(C_{4,4}=0\). For square boards \(R_{n,n}\), such sets exist exactly when \(3\mid n\), and then their number is \((n!)^2/[2^{2n/3}((n/3)!)^2]\).

## Assumptions and scope
Graphs are finite, simple, undirected and use open (not closed) neighborhoods. A horizontal domino has two cells in one row and two distinct columns; a vertical domino has two cells in one column and two distinct rows. Different dominoes must not share a row or column. Counts treat cells as labeled and \(S\) as an unordered subset; neither domino components nor their two cells are given artificial labels. The theorem includes the degenerate one-row and one-column rectangles; \(R_{1,1}\) has no admissible set.

## Proof
**Step 1 (the only possible components).** Each selected cell has exactly one selected neighbor, so the subgraph induced by \(S\) is a disjoint union of edges. Every edge of the rook graph is a horizontal or vertical domino. Distinct dominoes cannot share a row or column, since any selected cells on the shared line would then be adjacent across components. Write \(h\) and \(v\) for the numbers of horizontal and vertical dominoes. Exactly \(h+2v\) rows and \(2h+v\) columns are used.

**Step 2 (missing-line obstruction).** Let \(u=a-h-2v\) and \(w=b-2h-v\) count unused rows and columns. If two rows were unused, the two cells where they meet any fixed used column would have identical nonempty signatures. Thus \(u\le1\); by symmetry \(w\le1\). If \(u=w=1\), their intersection would have the empty signature, so this is impossible. If \(u=1,w=0\) and there were a horizontal domino with selected cells \((r,c_1)\) and \((r,c_2)\), then the unselected cell in column \(c_1\) of the unused row would have signature \(\{(r,c_1)\}\), identical to that of the selected cell \((r,c_2)\). Thus \(h=0\), which forces \(v=b\) and \(a=2b+1\). The transposed argument for \(u=0,w=1\) forces \(v=0\), \(h=a\), and \(b=2a+1\). Finally \(u=w=0\) gives the linear system \(h+2v=a\), \(2h+v=b\), hence the formulas for \(h,v\) in case 1 and its arithmetic conditions. These are all possibilities.

**Step 3 (the full-coverage converse).** Fix any nonoverlapping domino collection using every row and column. For a row \(r\), let \(A_r\) be its nonempty set of selected cells, and for a column \(c\), let \(B_c\) be its nonempty set of selected cells. A selected cell has signature consisting solely of its unique selected partner; these singletons are distinct. For an unselected cell \((r,c)\), the signature is the disjoint union \(A_r\cup B_c\), so it has at least two elements and cannot equal a selected-cell signature.

Suppose two different unselected cells \((r,c)\) and \((r',c')\) have equal signatures. If their rows agree, their distinct column sets are disjoint and nonempty, a contradiction; similarly if their columns agree. Otherwise \(r\ne r'\) and \(c\ne c'\). Sets belonging to distinct rows or to distinct columns are disjoint. Equality \(A_r\cup B_c=A_{r'}\cup B_{c'}\) therefore implies \(A_r=B_{c'}\) and \(A_{r'}=B_c\), with all four sets nonempty. But the same nonempty set of selected cells cannot consist of the selected cells of both a row and a column: it would have to be the singleton at their intersection, whereas every selected cell belongs to a domino and has two selected cells on one of its two lines. This contradiction proves all signatures distinct and nonempty.

**Step 4 (single unused-line converse).** If exactly one row is unused and every domino is vertical, selected-cell signatures are distinct singletons, cells in the unused row have distinct two-element signatures (the complete selected pairs in their columns), and all remaining unselected cells have three-element signatures: the two selected cells of their column together with the unique selected cell of their row. These triples determine their row and column uniquely. Therefore all signatures are nonempty and distinct. The case of one unused column and all horizontal dominoes is symmetric.

**Step 5 (exact counting).** In case 1, partition the \(a\) labeled rows into \(h\) singleton horizontal-row blocks and \(v\) unordered pairs for vertical dominoes; independently partition the \(b\) labeled columns into \(h\) unordered pairs for horizontal dominoes and \(v\) singleton vertical-column blocks. Match the corresponding horizontal blocks bijectively and likewise the vertical blocks. The count is
\[
\frac{a!}{h!2^vv!}\,\frac{b!}{2^hh!v!}\,h!v!
=\frac{a!b!}{2^{h+v}h!v!}.
\]
If one column is unused, choose that column, then partition the other \(2a\) labeled columns into pairs attached to the \(a\) rows. This gives \((2a+1)!/2^a=b!/2^a\); the transposed case is identical. The size enumerators follow from the number of dominoes in each case.

Finally, a horizontal domino carries one row label and an unordered pair of column labels, contributing \(XY^2/2\) in labeled exponential enumeration; a vertical domino contributes \(X^2Y/2\). An unordered collection of such components contributes the first exponential term. One distinguished unused row can coexist only with vertical dominoes, and one distinguished unused column only with horizontal ones; these give the remaining two exponential terms. Subtracting the empty structures yields the displayed generating function.

## Verification
The standalone script `check.py` enumerates every subset, directly from rook-graph adjacency matrices, for twenty labeled rectangles through size \(4\times5\), including \(3\times6\). It tests open independence, nonempty signatures and injectivity independently of the structural formulas; `check_output.txt` records the exact observed size distributions. The direct counts agree in all tested instances, including positive mixed-domino cases \((3,3)\) and \((4,5)\), a single-unused-line case \((2,5)\), and absent cases \((4,4)\) and \((3,5)\). The proof, not the finite enumeration, establishes the infinite statements.

## Relationship to prior work
Seo and Slater introduced the open-independent open-locating-dominating parameter and proved structural and complexity statements for other graph families [1]. Cappelle, Coelho, Foulds and Longo investigated the problem for planar graphs, \(P_4\)-tidy graphs and complementary prisms of cographs [2]. Studer, Haynes and Lawson examined the weaker induced-paired domination condition, which requires induced matching components but does not require distinct open signatures [3]. An existing rectangular rook-graph dissociation-polynomial classification also counts collections of line-disjoint dominoes together with isolated selected cells; its profile weights yield the same factorial factors once one knows which domino profiles satisfy the stronger open-locating condition. What is not implied by that dissociation statement is the open-signature criterion: only the full-line-coverage profiles and the two sharply restricted single-unused-line profiles work. The present theorem proves that additional necessity-and-sufficiency statement and its arithmetic consequences. The inspected primary literature does not supply the complete open-independent locating classification. Ordinary Cartesian grid graphs \(P_a\square P_b\) appearing in related detection work are not the rook graphs \(K_a\square K_b\).

## Limitations
These statements concern only Cartesian products of two complete graphs with the stated open-neighborhood and induced-matching conditions; they do not solve the general open-independent locating problem. Published-priority uncertainty remains for unindexed work or differently named rook-graph coding results. The verification script supplies finite regression evidence, not a computer proof of the general theorem. Independent external audit has not been performed.

## References
[1] S. J. Seo and P. J. Slater, “Open-independent, open-locating-dominating sets,” *Electronic Journal of Graph Theory and Applications* 5(2) (2017), 179–193. DOI: https://doi.org/10.5614/ejgta.2017.5.2.2. Full text: https://www.ejgta.org/index.php/ejgta/article/download/210/pdf_47.

[2] M. R. Cappelle, E. Coelho, L. R. Foulds and H. J. Longo, “Open-independent, open-locating-dominating sets: structural aspects of some classes of graphs,” *Discrete Mathematics & Theoretical Computer Science* 24(1) (2022). First public preprint, March 14, 2021: https://arxiv.org/abs/2103.07972. DOI: https://doi.org/10.46298/dmtcs.8440.

[3] D. S. Studer, T. W. Haynes and L. M. Lawson, “Induced-Paired Domination in Graphs,” *Ars Combinatoria* 57 (2000), 111–128. https://combinatorialpress.com/ars-articles/volume-057-ars-articles/induced-paired-domination-in-graphs/.
