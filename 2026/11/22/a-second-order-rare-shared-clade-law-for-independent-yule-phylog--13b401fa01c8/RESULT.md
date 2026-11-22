# A second-order rare shared-clade law for independent Yule phylogenies

## Finding

Let \(T_n^{(1)}\) and \(T_n^{(2)}\) be independent rooted binary phylogenetic trees with the same \(n\) distinct taxon labels, each sampled from the Yule–Harding–Kingman (YHK) distribution. Let \(R_n\) count subsets of labels of sizes \(3\) through \(n-1\) that are proper clades in **both** trees. Then, as \(n\to\infty\),

\[
\Pr(R_n>0)=\frac{1}{6n}+\frac{1259}{1800n^2}+O(n^{-3}).
\]

Moreover, the probability that a shared proper clade of size at least three exists but is *not* the sole such clade, of size exactly three, is \(O(n^{-2})\). Conditional on \(R_n>0\), with probability \(1-O(n^{-1})\) the sole shared clade of size at least three is a three-taxon clade. Its three labels are exactly uniform among all three-element subsets (on this unique-triple event).

This is a second-order statement about **non-cherry** clade coincidences; it does not assert that cherries, whose count is of order one between two such trees, are absent.

## Assumptions and scope

The trees are independently generated using the YHK *rooted, leaf-labeled, binary topology* law. The label sets coincide and have size \(n\), and the root and complete taxon set are not counted as proper clades. A clade is the set of leaves below a vertex; a cherry has size two and is excluded from \(R_n\). No branch lengths, mutation process, or inference errors are modeled. All asymptotic bounds hold for integers \(n\to\infty\), with absolute implied constants.

## Proof

**Single and paired clade probabilities.** For any prescribed set \(A\) of size \(k\), the YHK clade probability (Zhu–Degnan–Steel, Lemma 4.2) is

\[
p_{n,k}=\frac{2n}{k(k+1)\binom nk},\qquad 2\le k<n.
\]

Write \(X_{n,k}\) for the number of size-\(k\) clades shared by both independent trees. Independence yields the exact mean

\[
\mathbb E X_{n,k}=\binom nk p_{n,k}^2
 =\frac{4n^2}{k^2(k+1)^2\binom nk}.
\]

For sizes three and four these are

\[
\mathbb E X_{n,3}=\frac{n}{6(n-1)(n-2)}
=\frac1{6n}+\frac1{2n^2}+O(n^{-3}),
\qquad
\mathbb E X_{n,4}=\frac{n^2}{100\binom n4}
=\frac6{25n^2}+O(n^{-3}).
\]

For \(5\le k\le n-5\), \(\binom nk\ge\binom n5\), so summing the exact means is \(O(n^{-3})\); the remaining at-most-four terminal sizes obey the same bound individually. Thus

\[
\Pr\bigl(\exists\text{ shared clade of size }\ge5\bigr)=O(n^{-3}).
\]

**Two shared triples.** Distinct clades of size three in one rooted tree are necessarily disjoint. For any two prescribed disjoint three-sets \(A,B\), the disjoint nonexhaustive case of Zhu–Degnan–Steel, Theorem 4.5, simplifies for \(n\ge7\) to

\[
q_n=\Pr(A,B\text{ both clades in one tree})
=\frac{35n-141}{35(n-1)(n-2)(n-3)(n-4)(n-5)}.
\]

Hence, for \(n\ge7\),

\[
\mathbb E\bigl[(X_{n,3})_2\bigr]
=\binom n3\binom{n-3}3q_n^2
=\frac1{36n^2}+O(n^{-3}).
\]

Here \((u)_2=u(u-1)\). Three distinct common triples have probability sum \(O(n^{-3})\), since triples in either tree are disjoint and, by exchangeability, \(\mathbb E[(X_{n,3})_3]\le (n/3)^6/[\binom n3\binom{n-3}3\binom{n-6}3]=O(n^{-3})\). [The latter inequality follows directly by writing the factorial moment as the square of the single-tree factorial moment divided by the number of ordered disjoint triples.]

**Triple–four-clade interactions.** There are two ways a size-three and size-four clade can coexist in a rooted tree: the triple lies inside the four-clade, or they are disjoint. For a prescribed three-set inside a prescribed four-set, sampling consistency implies

\[
\Pr(A,B\text{ both clades in one tree})=p_{n,4}p_{4,3}=p_{n,4}/6.
\]

Therefore the exact expected number of *ordered nested* shared three–four pairs is

\[
4\binom n4 (p_{n,4}/6)^2
=\frac{n^2}{900\binom n4}
=\frac2{75n^2}+O(n^{-3}).
\]

The expected number of disjoint shared three–four pairs is \(O(n^{-3})\): there are \(O(n^7)\) prescribed pairs and the one-tree probability is \(O(n^{-5})\) by Theorem 4.5. Distinct four-clades are disjoint, and the expected number of their shared pairs is \(O(n^{-4})\) by the same calculation.

**Bonferroni remainder.** Apply inclusion–exclusion to all possible common size-three and size-four clade events. Every triple of distinct such events has total joint-probability sum \(O(n^{-3})\). To see this, classify their compatible clade configurations: three disjoint triples; a four-clade containing one triple and a separate triple; two disjoint four-clades with a triple inside one or separate; or three disjoint four-clades. In each case the one-tree probability bound for the maximal disjoint clades is \(O(n^{-\sum_i(k_i-1)})\), with an additional bounded conditional probability for any nested triple. For the bound, condition on the last of any fixed disjoint groups of sizes \(k_1,\ldots,k_r\) being a clade, then delete its leaves. Group elimination says the remaining tree has the YHK distribution; any other disjoint group that was a clade remains one upon deletion. Iterating gives the explicit upper bound \(\prod_{i=1}^r p_{n-\sum_{j>i}k_j,k_i}=O(n^{-\sum_i(k_i-1)})\). Nested triples contribute only a bounded conditional probability inside their containing four-clade. Summing squared probabilities over the \(O(n^{\sum_i k_i})\) label choices gives \(O(n^{-3})\) or smaller. Incompatible configurations have probability zero. The preceding factorial-moment bound handles the first case independently. Thus the third Bonferroni remainder is \(O(n^{-3})\).

Combining the first two Bonferroni orders, with every pair counted once, and then restoring the negligible clades of size at least five,

\[
\begin{aligned}
\Pr(R_n>0)
&=\mathbb E X_{n,3}+\mathbb E X_{n,4}
 -\tfrac12\mathbb E[(X_{n,3})_2]
 -\mathbb E[\text{nested common three–four pairs}]+O(n^{-3})\\
&=\frac1{6n}+\left(\frac12+\frac6{25}-\frac1{72}-\frac2{75}\right)\frac1{n^2}+O(n^{-3})\\
&=\frac1{6n}+\frac{1259}{1800n^2}+O(n^{-3}).
\end{aligned}
\]

By the bounds above, the chance of any size-four-or-larger shared clade or at least two shared triples is \(O(n^{-2})\). Dividing by the leading event probability proves conditional uniqueness and size three. Label exchangeability implies exact uniformity of the unique shared three-set.

## Verification

Run `python verify.py` with standard Python. The standalone script uses exact rational arithmetic to enumerate independent pairs of YHK trees through six taxa; it checks the clade probabilities, all-common-clade expectations and factorial identities. Independent single-tree enumeration on seven taxa checks the fixed disjoint triple and nested triple–four-clade probabilities. Exact-rational Bonferroni main terms are evaluated at three larger sizes, verifying approach toward the coefficient \(1259/1800\). The script reports 136 passed assertions. These finite checks do not replace the asymptotic bounds proved above.

## Relationship to prior work

Zhu, Degnan and Steel (2011) prove single-tree marginal and multi-clade probabilities under the YHK model, used here explicitly. Steel (1988), Steel and Penny (1993), and Bryant and Steel (2008) study tree-comparison and Poisson-overlap phenomena, especially under uniform/unrooted distributions or more general comparisons. The present statement concerns the previously unisolated **second-order probability of a collision among common proper clades larger than cherries** in *two independent rooted YHK trees*: it separates common triples, common four-clades, their nesting, and double-triple coincidences. The leading and next-order constants are not asserted to be new single-tree clade probabilities or a new general Poisson limit.

## Limitations

The expansion requires independent YHK samples with the same taxon set and does not extend automatically to dependent trees, unrooted splits, nonbinary trees, or conditional trees inferred from data. The coefficient is asymptotic, not an exact finite-\(n\) event probability. Earlier work on tree-comparison metrics has overlapping subject matter; the full 1993 Steel–Penny article could not be checked line by line, leaving some historical-priority risk. The result has not undergone independent mathematical audit.

## References

1. S. Zhu, J. H. Degnan, M. Steel, *Clades, clans and reciprocal monophyly under neutral evolutionary models*, arXiv:1101.1311 (first public preprint, 2011-01-06). Lemma 4.2, Theorem 4.5 and the group-elimination property.
2. M. A. Steel, *Distribution of the symmetric difference metric on phylogenetic trees*, SIAM Journal on Discrete Mathematics 1 (1988), 541–551. DOI: 10.1137/0401050.
3. M. A. Steel and D. Penny, *Distributions of tree comparison metrics—some new results*, Systematic Biology 42 (1993), 126–141. DOI: 10.1093/sysbio/42.2.126.
4. D. Bryant and M. Steel, *Computing the distribution of a tree metric*, arXiv:0810.0868 (2008-10-06).
5. T. Wu and K. P. Choi, *On joint subtree distributions under two evolutionary models*, arXiv:1508.03139 (2015-08-13).
