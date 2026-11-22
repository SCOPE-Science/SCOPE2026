# Seven excess individuals first permit Shannon–Simpson diversity rank reversal

## Finding

Let two biological communities have the same observed species richness \(k\ge 3\) and the same integer census \(N\), and let every observed species have a positive integer abundance. Write their Hill numbers of orders one and two as
\[
D_1(a)=\exp\!\left(-\sum_{i=1}^{k}\frac{a_i}{N}\log\frac{a_i}{N}\right),\qquad
D_2(a)=\left(\sum_{i=1}^{k}(a_i/N)^2\right)^{-1}.
\]
**The sharp universal threshold is \(N-k=7\).** For \(0\le N-k\le6\), no two such communities have opposite strict rankings under \(D_1\) and \(D_2\). For \(N=k+7\), precisely one unordered pair of abundance multisets, up to species relabeling, does:
\[
A=(1^{[k-3]},1,4,5),\qquad B=(1^{[k-3]},2,2,6),
\]
where \(1^{[m]}\) means a list of \(m\) singleton-species counts. At this first boundary, \(D_1(A)<D_1(B)\), whereas \(D_2(A)>D_2(B)\). For \(k=3\), this is the ten-individual comparison \((1,4,5)\) versus \((2,2,6)\).

## Assumptions and scope

The vectors \(a=(a_1,\ldots,a_k)\) are unlabeled abundance multisets with \(a_i\in\mathbb Z_{\ge1}\), \(\sum_i a_i=N\), fixed \(k\ge3\) and common \(N\ge k\). Diversity means plug-in Hill diversity of orders one and two, not an estimator corrected for sampling. A **strict ranking reversal** means \(D_1(A)<D_1(B)\) and \(D_2(A)>D_2(B)\), or vice versa; a tie under either metric is not a strict reversal. The theorem classifies every such pair for \(N-k\le7\), with no upper bound on \(k\).

## Proof

**Step 1 (exact order keys).** For fixed \(k,N\), set
\[
C(a)=\sum_i a_i^2,\qquad P(a)=\prod_i a_i^{a_i}.
\]
Direct algebra gives \(D_2(a)=N^2/C(a)\) and \(D_1(a)=N/P(a)^{1/N}\). Consequently, a strict reversal is equivalent to \((C(A)-C(B))(P(A)-P(B))<0\). The comparison of \(P\) is exact integer arithmetic, with no approximation of logarithms.

**Step 2 (unbounded richness becomes finite partitions).** Put \(t=N-k\) and \(e_i=a_i-1\). Every abundance multiset corresponds to a partition of \(t\) into at most \(k\) positive parts, completed by zero parts and then increased by one. For two partitions of the same \(t\), if one majorizes the other after zero padding, adding the same constant one to every coordinate preserves majorization. By the convexity of \(x\mapsto x^2\) and \(x\mapsto x\log x\) on \((0,\infty)\), majorization orders \(C\) and \(\log P\) in the same weak direction. Hence **only incomparable partitions can reverse the two Hill numbers**. This argument is uniform in arbitrary \(k\), because extra zero parts in the excess vectors merely contribute singleton counts to both communities.

**Step 3 (complete small-partition certificate).** For \(0\le t\le5\), the partitions of \(t\) are totally ordered by majorization. There are precisely two unordered incomparable partition pairs at \(t=6\), and four at \(t=7\). They are all listed below, using nondecreasing excess parts; the listed \(\Delta C\) and integer product comparison are calculated after adding one to each positive excess and are unaffected by common singleton padding.

| Excess \(t\) | Excess partition \(u\) | Excess partition \(v\) | \(C(u+1)-C(v+1)\) | \(P(u+1)\) versus \(P(v+1)\) |
|---|---|---|---:|---|
| \(6\) | \((1,1,1,3)\) | \((2,2,2)\) | \(0\) | \(16384<19683\) |
| \(6\) | \((1,1,4)\) | \((3,3)\) | \(0\) | \(50000<65536\) |
| \(7\) | \((1,1,1,1,3)\) | \((1,2,2,2)\) | \(0\) | \(65536<78732\) |
| \(7\) | \((1,1,1,4)\) | \((1,3,3)\) | \(0\) | \(200000<262144\) |
| \(7\) | \((1,1,1,4)\) | \((2,2,3)\) | \(2\) | \(200000>186624\) |
| \(7\) | \((1,1,5)\) | \((3,4)\) | \(2\) | \(746496<800000\) |

All rows except the last have either a tie in \(C\) or matching signed comparisons. The last row gives exactly the proposed reversal. Its two excess partitions have two and three positive parts, so both are admissible for every \(k\ge3\). Conversely the table exhausts all incomparable partitions through \(t=7\), proving both the lower bound and uniqueness. At the witness, \(C(A)=k+39<C(B)=k+41\), while \(P(A)=800000>746496=P(B)\); the inequalities are strict.

## Verification

The included standard-library program `verify_diversity.py` recursively enumerates each integer partition of excess \(t=0,\ldots,7\), compares cumulative descending parts to determine majorization, independently computes exact integer \(C\) and \(P\), and checks the six displayed incomparable pairs and unique reversal. It additionally enumerates complete communities for \(3\le k\le11\) as a redundant check, and confirms the exact witness values. Run `python3 verify_diversity.py` after extracting the embedded files. The uniform quantifier over all \(k\ge3\) is justified by Step 2, not by finite \(k\)-testing.

## Relationship to prior work

Hill (1973) defines the effective-species-number family and specifically connects its first and second orders to exponential Shannon entropy and inverse Simpson concentration; it does not give a sharp finite-integer census cutoff. Tóthmérész (1995) provides an explicitly discordant Shannon–Simpson example with differing species richnesses and studies diversity profiles rather than this same-richness first boundary. Jost (2006) explains the underlying index transformations; Liu et al. (published online 2006) analyze relationships among ordering methods and majorization, without this first-discordance classification in the inspected article. Related published mathematical results concern a stricter three-index reversal with twenty individuals, Berger–Parker versus Simpson reversal with eight excess individuals, Shannon versus Brillouin comparison, and Simpson-matched rarefaction. Their extra index constraints or different metrics do not imply this two-index, seven-excess threshold.

## Limitations

This is an exact classification of count vectors under fixed richness and fixed census, not a test of ecological causality, a sampling-error bound, or an estimator-selection recommendation. Continuous proportions can disagree without an integer-census cutoff. Historical priority remains qualified against unindexed small-census comparisons or finite-partition results phrased outside ecological terminology. No independent scientific audit is claimed.

## References

1. Hill, M. O. (1973). *Diversity and Evenness: A Unifying Notation and Its Consequences.* *Ecology* 54, 427–432. https://doi.org/10.2307/1934352 (first public date verified as 1973-03-01). Full text: https://ricottalab.com/wp-content/uploads/2015/10/hill-1973.pdf
2. Tóthmérész, B. (1995). *Comparison of different methods for diversity ordering.* *Journal of Vegetation Science* 6, 283–290. https://doi.org/10.2307/3236223 ; full text: https://ecoevol.ufg.br/adrimelo/div/Tothmeresz1995.pdf
3. Jost, L. (2006). *Entropy and diversity.* *Oikos* 113, 363–375. https://doi.org/10.1111/j.2006.0030-1299.14714.x
4. Liu, C., Whittaker, R. J., Ma, K., and Malcolm, J. R. (2007). *Unifying and distinguishing diversity ordering methods for comparing communities.* *Population Ecology* 49, 89–100. https://doi.org/10.1007/s10144-006-0026-0 (first public online 2006-12-15).
5. Related published mathematical comparisons: https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-the-unique-twenty-individual-double-reversal-among-three-hill-di--6710d8b3b0c9 ; https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-eight-excess-individuals-are-the-sharp-berger-parker-simpson-rev--8b2ee10f8104
