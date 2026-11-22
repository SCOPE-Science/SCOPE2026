# Joint Poisson independence of pairwise common clades in random rooted phylogenies

## Finding

Let \(q\ge3\) be fixed. For independent uniform rooted nonplane binary phylogenetic trees \(T_1,\ldots,T_q\) with the same leaf set \([n]\), the numbers \(H_{ij}\) of shared proper nontrivial clades jointly satisfy

\[
(H_{ij})_{1\le i<j\le q}\ \xrightarrow{d}\ (Z_{ij})_{i<j},\qquad Z_{ij}\overset{\mathrm{ind}}{\sim}\operatorname{Poisson}(1/8).
\]

Let \(Y_{ij}\) be the number of shared two-leaf clades (cherries). At every \(n\ge4\), if \(i,j,k\) are distinct,

\[
\operatorname{Cov}(Y_{ij},Y_{ik})
=\frac{n(n-1)(n-2)(n-3)}{2(2n-5)(2n-3)^4}>0,
\]

which is asymptotic to \(1/(64n)\). If \(\{i,j\}\cap\{k,\ell\}=\varnothing\), the corresponding cherry overlaps are independent at every finite size. The limiting probability that **all** the trees have mutually maximum rooted Robinson–Foulds distance is \(\exp(-\binom q2/8)\).

The one-pair Poisson limit is established background; the claim here is the **joint array** and its finite positive dependence correction.

## Assumptions and scope

The PDA distribution is uniform over all \((2n-3)!!\) unordered, rooted, fully bifurcating leaf-labelled phylogenetic trees. The root is a genuine binary internal vertex, and there are no unlabelled degree-two vertices. The integer \(q\ge3\) is fixed as \(n\to\infty\). A clade is the descendant leaf set of a non-root internal vertex; a cherry is a clade of size two. Thus there are \(n-2\) proper nontrivial clades per tree. Define \(d_{ij}=2(n-2)-2H_{ij}\), the (unnormalized) rooted Robinson–Foulds symmetric-difference distance; no normalization by a union size is used.

For integer \(s\ge0\) and sufficiently large \(n\), set \(a_{n,s}=(2n-2s-3)!!/(2n-3)!!\), with \((-1)!!=1\). For a prescribed family of \(s\) mutually disjoint leaf pairs, its probability of being entirely cherries in one tree is exactly \(a_{n,s}\). Overlapping distinct leaf pairs cannot both be cherries.

## Proof

**1. Cherry contraction.** Replacing each of \(s\) disjoint, prescribed sibling leaf pairs by one new distinguished leaf is a bijection between trees containing all those cherries and the \((2(n-s)-3)!!\) rooted trees on \(n-s\) leaves. Therefore their joint probability is exactly \(a_{n,s}\), and for fixed \(s\), \(a_{n,s}\sim(2n)^{-s}\).

**2. Joint factorial moments.** Let \(r_{ij}\) be any fixed nonnegative integers, write \(R=\sum_{i<j}r_{ij}\) and \(s_i=\sum_{j\ne i}r_{\min(i,j),\max(i,j)}\), so \(\sum_i s_i=2R\). Expand \(\mathbb E\prod_{i<j}(Y_{ij})_{r_{ij}}\) by selecting ordered distinct cherries for each indicated overlap count. The terms using \(R\) **pairwise vertex-disjoint, all distinct** leaf pairs number \((n)_{2R}/2^R\). The probability that each tree contains its assigned \(s_i\) cherries is \(\prod_i a_{n,s_i}\), so these terms tend to \(2^{-R}2^{-2R}=8^{-R}\).

All remaining feasible terms contribute \(o(1)\): two different requested leaf pairs sharing a leaf cannot be cherries within one tree and, otherwise, their smaller number of free leaf labels costs a factor \(O(1/n)\) relative to the all-distinct family. If the *same* leaf pair occurs in different overlap types, the corresponding group of index edges has at least three distinct tree indices, so the probability that this pair occurs in every required tree is \(O(n^{-3})\), as opposed to \(O(n^{-2})\) for one requested pair, and there are only \(O(n^2)\) choices. A partition of all requests into repeated-label groups gives a product of these bounds; groups of a single pair and two indices are \(O(1)\), whereas each group involving three or more tree indices is \(O(n^{-1})\). The total number of such finite patterns depends only on the fixed degrees \(r_{ij}\). Hence

\[
\lim_{n\to\infty}\mathbb E\prod_{i<j}(Y_{ij})_{r_{ij}}
=(1/8)^{\sum_{i<j}r_{ij}}.
\]

These are the complete mixed factorial moments of independent Poisson variables with means \(1/8\); the latter law is moment-determinate. Consequently the full common-cherry array converges jointly to that law.

**3. Larger clades vanish.** A specified subset \(S\subset[n]\) of cardinality \(k\in\{2,\ldots,n-1\}\) forms a clade with probability

\[
p_{n,k}=\frac{(2k-3)!!(2(n-k)-1)!!}{(2n-3)!!}.
\]

The ratio \(p_{n,k+1}/p_{n,k}=(2k-1)/(2n-2k-1)\) grows with \(k\). Therefore, if \(n\ge5\), throughout \(3\le k\le n-2\) we have \(p_{n,k}\le3/[(2n-3)(2n-5)]\). Conditioning on the first tree, which has exactly \(n-2\) nontrivial clades, bounds the expected number of common clades in that size range by \(3(n-2)/[(2n-3)(2n-5)]\). For size \(n-1\), summing the probability of each possible clade occurring in both independent trees yields \(n/(2n-3)^2\). Thus the probability of any common clade of size at least three is at most

\[
\frac{3(n-2)}{(2n-3)(2n-5)}+\frac{n}{(2n-3)^2}=O(1/n).
\]

A union bound over the fixed number of tree pairs implies that \((H_{ij})\) and \((Y_{ij})\) coincide with probability tending to one. This transfers the joint Poisson limit. Since \(d_{ij}=2(n-2)-2H_{ij}\), the same holds for the whole rescaled distance-deficit matrix. In particular the event of all maximum pairwise distances has limit \(\exp(-\binom q2/8)\).

**4. Exact finite dependence.** The number \(C\) of cherries of one PDA tree has

\[
\mathbb EC=\frac{n(n-1)}{2(2n-3)},\qquad
\operatorname{Var}C=\frac{n(n-1)(n-2)(n-3)}{2(2n-5)(2n-3)^2}.
\]

The variance follows by expanding \(C^2\) over leaf pairs: a cherry has probability \(1/(2n-3)\), two disjoint prescribed cherries have probability \(1/[(2n-3)(2n-5)]\), and intersecting pairs are mutually exclusive. Given \(T_i\), overlaps with independently sampled \(T_j\) and \(T_k\) are conditionally independent, with conditional means \(C(T_i)/(2n-3)\). The law of total covariance therefore gives \(\operatorname{Cov}(Y_{ij},Y_{ik})=\operatorname{Var}C/(2n-3)^2\), the claimed formula. Disjoint index pairs are functions of independent tree pairs and hence independent.

## Verification

Run the standalone `python3 verify_phylo33.py` checker with standard Python 3. It enumerates every rooted, leaf-labelled PDA tree on three through six leaves and verifies the double-factorial count, all specified cherry-pair and clade probabilities, exact cherry mean and variance, and the shared-index covariance identity. It reports 231 exact assertions and 945 trees at six leaves. The finite checks corroborate the identities but do not replace the above factorial-moment and clade-tail arguments for arbitrary sample size.

## Relationship to prior work

Steel (1988) derives a Poisson law for the symmetric-difference distance of **two** random (unrooted) phylogenetic trees. Bryant and Steel (2008 preprint; 2009 journal) give Poisson approximations for distances from one reference tree and discuss the two-tree setting. Those are antecedents, not this paper's novelty. Zhu, Than and Wu (2014) derive PDA clade-probability structure. The new contribution is the **simultaneous dependence** of all pairwise distances among any fixed number of rooted PDA trees: the joint independent-Poisson limit, despite explicit strictly positive \(O(1/n)\) correlations of overlap counts sharing a tree. A known analogous theorem for random Cayley-tree **common edges** does not imply the different rooted PDA **common clade** statistic or its covariance formula.

## Limitations

The conclusion is for a fixed number of independent uniformly random rooted PDA trees; it does not establish a limit when their number grows, nor does it extend without proof to the Yule–Harding–Kingman distribution or to unrooted distances at finite sample size. No multivariate total-variation rate is claimed. The exact finite covariance concerns common cherries, not all shared clades. Historical equivalence in earlier tree-comparison literature is a residual priority risk; independent mathematical audit has not occurred.

## References

- M. A. Steel, “Distribution of the Symmetric Difference Metric on Phylogenetic Trees,” *SIAM Journal on Discrete Mathematics* **1** (1988), 541–551, https://doi.org/10.1137/0401050 (single-pair law; full text was not available in the inspected public source).
- D. Bryant and M. Steel, “Computing the Distribution of a Tree Metric,” first circulated 2008-10-06, https://arxiv.org/abs/0810.0868 (single-reference distance analysis and Poisson approximation).
- S. Zhu, C. Than and T. Wu, “Clades and clans: a comparison study of two evolutionary models,” first circulated 2014-07-15, https://arxiv.org/abs/1407.3880 (PDA clade probabilities and log-convexity).
- D. McKenzie and M. Steel, “Distributions of cherries for two models of trees,” *Mathematical Biosciences* **164** (2000), 81–92, https://pubmed.ncbi.nlm.nih.gov/10704639/ (one-tree cherry counts).
