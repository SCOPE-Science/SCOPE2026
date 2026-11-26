# All Schur rings on two-row rectangular bands are automorphic: classification and weighted-Bell enumeration

## Finding
For every integer \(n\ge1\), consider the rectangular-band semigroup \(S_{2,n}=\{0,1\}\times[n]\) with multiplication \((i,j)(k,l)=(i,l)\). A *Schur partition* \(\mathcal P\) of this semigroup is a partition whose block sums \(\underline X=\sum_{x\in X}x\) span a subring of the rational semigroup algebra \(\mathbb Q[S_{2,n}]\). Such a subring is called a semigroup Schur ring.

**Theorem.** Every Schur partition of \(S_{2,n}\) belongs to precisely one of two types:

1. **Separated rows:** choose a set partition \(\pi\) of \([n]\), and use exactly the blocks \(\{0\}\times T\) and \(\{1\}\times T\), for \(T\in\pi\).
2. **Balanced rows:** choose a set partition \(\pi\) of \([n]\). For every \(T\in\pi\), choose independently either (a) a single Schur block \(\{0,1\}\times T\); or (b), if \(|T|=2j\) for an integer \(j\ge1\), split \(T=T_+\sqcup T_-\) into two sets of size \(j\), with the split considered unordered, and form the two Schur blocks \((\{0\}\times T_+)\cup(\{1\}\times T_-)\) and \((\{0\}\times T_-)\cup(\{1\}\times T_+)\).

**Moreover every one of these Schur rings is automorphic:** its partition is exactly the orbit partition of a subgroup of \(\operatorname{Aut}(S_{2,n})\cong S_2\times S_n\).

Let \(B_n\) be the \(n\)-th Bell number, \(\Pi_n\) the set of set partitions of \([n]\), and
\[
 w_s=\begin{cases}1,&s\text{ odd},\\1+\frac12\binom{2j}{j},&s=2j\text{ even} \ (j\ge1).\end{cases}
\]
Then the exact number \(A_n\) of Schur partitions is
\[
 \boxed{A_n=B_n+\sum_{\pi\in\Pi_n}\prod_{T\in\pi}w_{|T|}.}
\]
The associated exponential generating function, with the empty-column case deliberately excluded, is
\[
 \boxed{\sum_{n\ge1}A_n\frac{z^n}{n!}=\exp(e^z-1)+\exp\left(e^z-1+\frac12\sum_{j\ge1}\frac{z^{2j}}{(j!)^2}\right)-2.}
\]
The first five numbers are \(2,5,13,48,184\), respectively, at \(n=1,2,3,4,5\).

## Assumptions and scope
All semigroups are finite, \(n\) is an arbitrary positive integer, and the algebra is taken over \(\mathbb Q\). There is no identity assumption on \(S_{2,n}\). The formula counts actual partitions of the fixed labeled underlying set, not isomorphism types of Schur rings and not subgroups of the automorphism group. "Automorphic" means that the partition coincides with orbits of a subgroup; different subgroups may give the same partition.

## Proof
Write \(r_X(i)=|X\cap(\{i\}\times[n])|\) and \(c_X(j)=|X\cap(\{0,1\}\times\{j\})|\). For any two Schur blocks \(X,Y\) and any semigroup element \((i,j)\), its coefficient in \(\underline X\underline Y\) equals
\[
 r_X(i)c_Y(j).
\]
Consequently the span of block sums is closed under multiplication exactly when, for every \(X,Y\), this outer-product coefficient is constant on each partition block \(Z\).

Define the **row signature** of row \(i\) to be the vector \((r_X(i))_{X\in\mathcal P}\), and the **column signature** of column \(j\) to be \((c_X(j))_{X\in\mathcal P}\). If two cells \((i,j),(i',j')\) belong to one block \(Z\), the outer-product criterion gives \(r_X(i)c_Y(j)=r_X(i')c_Y(j')\) for all \(X,Y\). Summing this identity over \(Y\) uses \(\sum_Yc_Y(j)=2\), so \(r_X(i)=r_X(i')\) for every \(X\). Summing instead over \(X\) uses \(\sum_Xr_X(i)=n\), so \(c_Y(j)=c_Y(j')\) for every \(Y\). Conversely, equality of both signatures for cells in each block makes all outer products constant. Thus a partition is Schur exactly when **each block lies entirely in a product of one row-signature class with one column-signature class**.

There are only two rows. If their signatures differ, no Schur block can contain cells from both rows. The column signature at \(j\) records the two labels of the blocks containing \((0,j)\) and \((1,j)\), each with multiplicity. If two columns lie in one first-row block, they must have the same second-row block; reversing the two rows gives the converse. Hence the induced column partitions on the rows coincide, proving type 1. Conversely every partition of type 1 satisfies the criterion.

Suppose the two row signatures coincide. Then every block \(X\) contains equally many cells in the two rows. For each column \(j\), its column signature records exactly the **unordered multiset** of its two Schur-block labels. If a label \(X\) appears in any two columns, those columns have equal column signatures because their cells of label \(X\) belong to one block. Therefore \(X\) has a unique partner label \(Y\): every column containing \(X\) has unordered label pair \(\{X,Y\}\). Different partner classes cannot overlap, so the column set decomposes uniquely into groups belonging either to an identical-label pair \(\{X,X\}\) or to two distinct labels \(\{X,Y\}\). The identical-label group is monochromatic. In the distinct-label group, every column has one cell of each label, and equal row counts for \(X\) force exactly half the columns to have \(X\) in row \(0\) and half in row \(1\). Thus the group size is even and its two orientations are balanced. This is exactly type 2. Every such partition meets both signature conditions, proving sufficiency and uniqueness.

To see automorphicity, recall every row permutation and column permutation acts as a semigroup automorphism. For type 1, let the product of symmetric groups on the chosen column blocks act on columns while fixing rows. Its orbits are the prescribed blocks. For type 2, allow arbitrary column permutations separately within each monochromatic group and within each of the two orientation halves of each two-label group. Also choose a bijection between the two halves for every two-label group, combine these bijections into a column involution \(\tau\) fixing all monochromatic columns, and use the automorphism that simultaneously swaps the two rows and applies \(\tau\). Each generator preserves every prescribed Schur block. The within-half permutations are transitive on its elements in either row, and the coupled swap connects the two halves of each label; in a monochromatic group it connects its two rows. Thus the subgroup's orbits are precisely the desired Schur blocks.

For type 1 there are \(B_n\) choices. In type 2, a column group of size \(s\) has one monochromatic decoration, and for even \(s=2j\) it has \(\binom{2j}{j}/2\) unordered balanced splits. Hence its weight is \(w_s\), yielding the weighted-Bell formula. By the exponential formula for labeled set partitions,
\[
 \sum_{n\ge0}\frac{z^n}{n!}\sum_{\pi\in\Pi_n}\prod_{T\in\pi}w_{|T|}
 =\exp\left(\sum_{s\ge1}w_s\frac{z^s}{s!}\right)
 =\exp\left(e^z-1+\frac12\sum_{j\ge1}\frac{z^{2j}}{(j!)^2}\right).
\]
Adding the ordinary Bell generating function and subtracting their two formal constant terms proves the displayed formula for positive \(n\). \(\square\)

## Verification
A standalone standard-library Python checker enumerates every set partition of the \(2n\) labeled cells for \(n=1,2,3,4,5\). For each it independently tests the original block-product closure condition via exact integer structure constants, derives the predicted weighted-Bell and Bell values, and constructs generators whose cell-orbit partition must coincide with every accepted Schur partition. It produces:

| \(n\) | separated rows | balanced rows | all Schur partitions |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 2 |
| 2 | 2 | 3 | 5 |
| 3 | 5 | 8 | 13 |
| 4 | 15 | 33 | 48 |
| 5 | 52 | 132 | 184 |

Run `python3 checker.py` from the extracted package. The checker enumerates every one of the \(115975\) set partitions of the \(10\) cells at \(n=5\); the all-\(n\) result follows from the proof, not these finite tests.

## Relationship to prior work
Marrow and Misseldine, *On Schur Rings Over Semigroups* (arXiv:2601.09940, first submitted January 14, 2026) introduce semigroup Schur rings, establish the automorphic construction, and note that rectangular bands have at least \(B_aB_b\) product Schur rings. They observe nonproduct examples and report exactly \(5\) Schur rings for a two-by-two rectangular band and \(13\) for the three-by-two case. The theorem above recovers those counts, determines every partition for the entire two-row family, proves every one is automorphic, and gives a generating function and subsequent exact counts. The product-partition lower bound alone does not imply these additional constructions or completeness. Standard enumerations of Schur rings over cyclic groups, such as Misseldine's arXiv:2112.03422, concern a different class of semigroups.

## Limitations
The theorem does not classify rectangular bands with both dimensions at least three, nor does it determine the number of isomorphism classes, the number of realizing subgroups, or all Schur rings of arbitrary rectangular groups. No independent mathematical audit has been carried out. Bibliographic search may miss equivalent results under alternative terminology or in unindexed literature.

## References
1. Joseph E. Marrow and Andrew Misseldine, *On Schur Rings Over Semigroups*, arXiv:2601.09940v1 (first submitted 2026-01-14), Sections 1, 2.2, 5, 6. https://arxiv.org/abs/2601.09940
2. Andrew Misseldine, *Enumeration Techniques on Cyclic Schur Rings*, arXiv:2112.03422 (2021), background on enumeration of classical group Schur rings. https://arxiv.org/abs/2112.03422
