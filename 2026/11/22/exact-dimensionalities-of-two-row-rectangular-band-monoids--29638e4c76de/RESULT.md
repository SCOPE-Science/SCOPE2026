# Exact dimensionalities of two-row rectangular-band monoids

## Finding
For every integer \(n\ge1\), let \(B_{2,n}=\{0,1\}\times[n]\) be the rectangular band with multiplication \((i,j)(k,l)=(i,l)\). Let \(M_n=B_{2,n}^{1}\) be obtained by adjoining an external identity \(1_M\). A **dimensionality** is an equivalence relation \(\sim\) with \([1_M]=\{1_M\}\), such that whenever \(ab\sim c\), there are \(a'\sim a\) and \(b'\sim b\) with \(a'b'=c\).

**Complete classification.** Every dimensionality on \(M_n\) has the singleton class \(\{1_M\}\), together with exactly one of these disjoint types on \(B_{2,n}\):

- **Separated-row type:** choose a set partition \(\pi\) of \([n]\), and use the blocks \(\{0\}\times C\) and \(\{1\}\times C\) for each \(C\in\pi\).
- **Mixed-row type:** choose a set partition \(\pi\) of \([n]\). For each \(C\in\pi\), independently choose either the single block \(\{0,1\}\times C\), or an unordered proper nonempty bipartition \(\{S,C\setminus S\}\) with \(\varnothing\ne S\subsetneq C\). For the latter choice use the two blocks
\[
X_C=(\{0\}\times S)\cup(\{1\}\times(C\setminus S)),\qquad
Y_C=(\{0\}\times(C\setminus S))\cup(\{1\}\times S).
\]
These descriptions are unique, including the choice of the column partition.

Let \(B_n\) denote the Bell number and \(\left\{\begin{smallmatrix}n\\k\end{smallmatrix}\right\}\) the Stirling number of the second kind. The **exact number of labelled dimensionalities** is
\[
\boxed{D_n=B_n+\sum_{k=1}^{n}\left\{\begin{matrix}n\\k\end{matrix}\right\}2^{n-k}}.
\]
Its exponential generating function (for positive \(n\)) is
\[
\boxed{\sum_{n\ge1}D_n\frac{z^n}{n!}
=\exp(e^z-1)+\exp\!\left(\frac{e^{2z}-1}{2}\right)-2}.
\]

**Exact rigidity boundary.** Every separated-row dimensionality is an automorphism-subgroup orbit partition. A mixed-row one is such an orbit partition **if and only if** every split column block has \(|S|=|C\setminus S|\). Thus the orbit-realizable count is
\[
\boxed{O_n=B_n+\sum_{\pi\in\Pi_n}\prod_{C\in\pi}
\left(1+\mathbf1_{2\mid |C|}\frac12\binom{|C|}{|C|/2}\right)},
\]
where \(\Pi_n\) is the set of set partitions of \([n]\). Exactly \(2B_n\) dimensionalities are ordinary monoid congruences. The first counts are

| \(n\) | \(D_n\) | \(O_n\) | \(D_n-O_n\) | Congruences |
|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 0 | 2 |
| 2 | 5 | 5 | 0 | 4 |
| 3 | 16 | 13 | 3 | 10 |
| 4 | 64 | 48 | 16 | 30 |
| 5 | 309 | 184 | 125 | 104 |

In particular, within this family, \(M_3\) (of order seven) is the smallest monoid admitting a dimensionality that is **not** an automorphism-subgroup orbit partition. One example has three classes: \(\{1_M\}\) and
\[
X=\{(0,1),(0,2),(1,3)\},\qquad
Y=\{(1,1),(1,2),(0,3)\}.
\]
The products of any two nonidentity classes equal \(B_{2,3}=X\cup Y\); nevertheless the unequal row occupancies of \(X\) rule out an automorphism-orbit realization.

## Assumptions and scope
The columns are labelled \([n]\), the two rows are fixed labelled elements, and the external identity is distinct from every rectangular-band element. The count is of actual equivalence relations, **not** isomorphism classes. Only finite monoids with exactly two rectangular-band rows and at least one column are classified. The property is the full two-sided quantified dimensionality condition of Jenča, not the ordinary congruence condition and not the coefficientwise Schur-ring condition.

## Proof
**1. Product saturation.** For a block \(A\) in a partition of the rectangular band, let \(R(A)\subseteq\{0,1\}\) and \(C(A)\subseteq[n]\) be the sets of its occupied rows and columns. Then the set of all products of elements of blocks \(A,B\) is exactly
\[
A B=R(A)\times C(B).
\]
The dimensionality condition is equivalent to requiring this product rectangle to be a union of partition blocks for every \(A,B\): given \(a\in A,b\in B\), the equality class of \(ab\) must lie in \(AB\), and conversely this inclusion supplies the required \(a',b'\). The identity class is a singleton, so all products involving it are automatically saturated.

**2. Palette criterion.** Color cells by their partition blocks. For each row \(i\) define its row palette \(\mathcal R_i\), the set of colors appearing in that row; for each column \(j\) define its column palette \(\mathcal C_j\), the set of colors appearing in that column. Product saturation is equivalent to the following: whenever \((i,j)\) and \((i',j')\) have the same color,
\[
\mathcal R_i=\mathcal R_{i'},\qquad\mathcal C_j=\mathcal C_{j'}.
\]
Indeed, choose any colors \(A\in\mathcal R_i\) and \(B\in\mathcal C_j\). Their product rectangle contains \((i,j)\), so saturation puts \((i',j')\) in the rectangle, proving both palette inclusions; reverse the cells for equality. Conversely, if a rectangle contains one cell of a given color, equality of its row and column palettes with those of every same-colored cell forces the rectangle to contain the entire color block. Thus the criterion is both necessary and sufficient.

**3. The two cases.** If \(\mathcal R_0\cap\mathcal R_1=\varnothing\), no color meets both rows. Equal column palettes along any given color imply that the partitions induced on the two rows refine one another: columns in one top-row color block have the same bottom-row color, and conversely. Hence the two column set partitions are identical, giving exactly the separated-row type.

Otherwise a color occurs in both rows, so the palette criterion forces \(\mathcal R_0=\mathcal R_1\). In particular **each color occurs in each row**. Every column palette has one or two colors. Whenever two columns share a color, their palettes coincide. Thus the column set splits uniquely into groups of columns with identical palettes, with disjoint color sets between groups. In a one-color group all cells share that color. In a two-color group every column contains one cell of each color and each of the two colors occurs in both rows. Choosing which columns put the first color in row zero gives a nonempty proper subset \(S\); interchanging the two color names replaces \(S\) with its complement. These are precisely the mixed-row types displayed above. Every construction obeys the palette criterion, and the palette groups recover its defining column partition uniquely.

**4. Counting.** In a fixed mixed-row column group of size \(s\ge1\), the monochrome choice contributes one, and an unordered nonempty proper subset pair contributes \((2^s-2)/2\), totaling \(2^{s-1}\). For a column partition into \(k\) groups the product is \(2^{n-k}\), giving \(\sum_k\left\{\begin{smallmatrix}n\\k\end{smallmatrix}\right\}2^{n-k}\). There are \(B_n\) separated-row types, and the two types are disjoint. The exponential formula on decorated set partitions gives the generating function.

**5. Automorphism orbits and congruences.** Every automorphism preserves the nonunit rectangular-band ideal and acts there as an independent row permutation and column permutation; therefore \(\operatorname{Aut}(M_n)\cong S_2\times S_n\). All separated-row forms are orbits of a subgroup preserving rows and permuting columns inside the chosen groups. Any subgroup realizing a mixed-row form must contain a row-swapping element, because every block meets both rows. Every subgroup element preserves each orbit block setwise; for a row swap preserving the two-color block \(X_C\) this forces \(|X_C\cap(\{0\}\times C)|=|X_C\cap(\{1\}\times C)|\), that is, \(|S|=|C\setminus S|\).

Conversely, when every split group is balanced, choose independent column permutations inside each half of each split group and inside each monochrome group. Adjoin one global row swap combined with a column permutation exchanging the two equal-sized halves of each split group and preserving each monochrome group. The generated subgroup has precisely the desired blocks as orbits. For each column group of size \(s\), the number of allowed mixed-row orbit patterns is one plus \(\binom{s}{s/2}/2\) when \(s\) is even, giving \(O_n\). Finally a congruence on a rectangular band must be a product of an equivalence on the row set and one on the column set: multiplying related cells on arbitrary left and right forces each coordinate equivalence throughout its respective coordinate. The row set has precisely two equivalence relations, the columns have \(B_n\), so the count is \(2B_n\). Adjoining the singleton identity does not change this classification.

## Verification
The standalone standard-library Python program `verification/verify.py` independently enumerates every set partition of the \(2n\) rectangular-band cells for \(1\le n\le5\), explicitly tests the product saturation condition, and compares against the palette/form criterion. It separately generates the subgroup-orbit partitions of \(S_2\times S_n\) by closing cycle partitions under joins; the results agree with both exact formulas. Counts are \(2,5,16,64,309\) for all dimensionalities and \(2,5,13,48,184\) for orbit realizations. The program checks the seven-element example and its coefficientwise Schur failure. The computation at \(n=5\) is also exhaustive over all labelled grid partitions. Run `python3 verification/verify.py` from the folder containing this document. These finite calculations corroborate, but do not replace, the all-\(n\) proof.

## Relationship to prior work
Jenča's *Dimensionalities on monoids* (arXiv:2611.18000v1, submitted November 13, 2026) gives the general dimensionality condition (Proposition 3.3) and proves that automorphism-subgroup orbits are dimensionalities (Theorem 3.4), while also showing they do not exhaust all dimensionalities of arbitrary monoids. It does not classify the present finite rectangular-band family. Marrow and Misseldine's *On Schur Rings Over Semigroups* (arXiv:2601.09940v1, January 14, 2026), notably Section 2.2 and its small-order tables, studies the **strictly stronger coefficientwise Schur-ring** condition and reports the \(2\)-by-\(2\) and \(2\)-by-\(3\) Schur counts.

Two publicly indexed related classifications, *All Schur partitions of two-row rectangular bands are automorphic* (October 13, 2026) and *Schur-ring classification of two-row rectangular bands* (October 26, 2026), give exactly the balanced-strip/orbit subfamily counted by \(O_n\). Those classifications and their proofs were examined; their weighted row-incidence condition excludes the **unequal** split types counted here. The explicit \(n=3\) mixed-row example has block-sum square coefficients \(2\) on row zero but \(1\) on row one, so its partition is not a Schur partition over characteristic zero. Thus the earlier Schur classifications do not imply the new all-dimensionality census \(D_n\) or its strictly positive non-orbit part. Other current-work comparisons concerning dimensionalities on finite groups do not imply this classification for non-group bands.

## Limitations
The classification is not asserted for three or more rows, rectangular groups with nontrivial maximal subgroups, general relational monoids, or non-singleton identity equivalence classes. It counts labelled partitions, not equivalence classes under isomorphism. Historical priority could be affected by older results under different terminology. The published Schur classifications were available as public research files, but a comprehensive search of all historic literature is impossible. Numerical checking stops at \(n=5\), with the infinite claim proved separately.

## References
1. G. Jenča, *Dimensionalities on monoids*, arXiv:2611.18000v1, first posted November 13, 2026, https://arxiv.org/html/2611.18000v1 .
2. J. E. Marrow and A. Misseldine, *On Schur Rings Over Semigroups*, arXiv:2601.09940v1, first posted January 14, 2026, https://arxiv.org/html/2601.09940v1 .
3. *All Schur partitions of two-row rectangular bands are automorphic*, public published-finding corpus research record dated October 13, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-all-schur-partitions-of-two-row-rectangular-bands-are-automorphi--b55d2bce611d .
4. *Schur-ring classification of two-row rectangular bands*, public published-finding corpus research record dated October 26, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-schur-ring-classification-of-two-row-rectangular-bands--898f75a97d4e .
