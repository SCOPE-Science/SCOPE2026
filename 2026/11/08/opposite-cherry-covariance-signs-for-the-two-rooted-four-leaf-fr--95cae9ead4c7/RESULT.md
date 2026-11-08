# Opposite cherry-covariance signs for the two rooted four-leaf fringe shapes

## Finding

Let \(T_n\) be uniformly distributed over nonplane rooted full binary phylogenetic trees with distinctly labeled leaves \(\{1,\ldots,n\}\), where \(n\ge4\). Let \(C_n\) count cherries (nodes whose descendant leaf sets have size two). Let \(B_n\) count nodes with four descendant leaves and two children each subtending two leaves (balanced four-leaf fringe subtrees). Let \(A_n\) count nodes with four descendant leaves and one child subtending exactly one leaf (asymmetric or caterpillar four-leaf fringe subtrees).

Set
\[
Q_n=(2n-9)(2n-7)(2n-5)(2n-3)^2.
\]
Then, simultaneously for every integer \(n\ge4\),
\[
\boxed{\operatorname{Cov}(C_n,B_n)=
\frac{n(n-1)(n-2)(n-3)(3n^2-19n+24)}{8Q_n}>0,}
\]
\[
\boxed{\operatorname{Cov}(C_n,A_n)=
-\frac{n(n-1)(n-2)(n-3)(n^2-5n+3)}{2Q_n}<0.}
\]
The apparent negative factor \(2n-9\) at \(n=4\) is genuine and the formulas remain valid: the respective covariances are \(4/25\) and \(-4/25\). For \(n\ge5\), the denominators and the positive-sign numerator factors have the indicated signs. In the large-tree limit,
\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(C_n,B_n)}n=\frac3{256},\qquad
\lim_{n\to\infty}\frac{\operatorname{Cov}(C_n,A_n)}n=-\frac1{64}.
\]
As a finite-size consequence, the positive-to-negative covariance magnitude ratio equals one at \(n=4\), equals \(1/3\) at \(n=5\), increases strictly for integer \(n\ge5\), and tends to \(3/4\).

## Assumptions and scope

Trees are rooted, unordered at internal children, full binary, and each of their \(n\) leaves bears a distinct label; all \((2n-3)!!\) such trees are equiprobable. No branch lengths, random edge lengths, induced quartet indices, or unrooted split counts are considered. A *fringe subtree* at a node consists of that node and all its descendants, not the restriction of the full tree to an arbitrary four-leaf subset. The entire tree can itself be a four-leaf fringe subtree when \(n=4\). Each four-leaf rooted full binary topology is either balanced (three labeled topologies on a fixed four-set) or asymmetric (twelve labeled topologies on that set).

## Proof

**Contraction lemma.** Put \(t_m=(2m-3)!!\) for \(m\ge2\), with \(t_1=1\). This is the exact number of rooted nonplane binary trees with \(m\) distinctly labeled leaves. If a particular \(k\)-subset of the labels is required to form one specified rooted fringe topology, contracting this subtree to a new marked leaf is a bijection with rooted binary trees on \(n-k+1\) distinct leaves. Therefore the probability is
\[
\frac{t_{n-k+1}}{t_n}.
\]
If two specified fringe topologies use *disjoint* leaf sets of respective cardinalities \(k\) and \(\ell\), contracting both gives the probability \(t_{n-k-\ell+2}/t_n\) whenever \(n-k-\ell+2\ge2\). Fringe leaf sets form a laminar family: two distinct fringe leaf sets are disjoint or one contains the other. This follows because their roots in a tree are either ancestor-related or in different branches.

**First moments.** By the contraction lemma, a prescribed pair of leaves is a cherry with probability \(t_{n-1}/t_n=1/(2n-3)\). Write
\[
c_n=\mathbb E C_n=\frac{\binom n2}{2n-3}.
\]
A prescribed four-set can be a fringe subtree in three balanced or twelve asymmetric labeled topologies. Hence
\[
b_n=\mathbb E B_n=3\binom n4\frac{t_{n-3}}{t_n}
=\frac{n(n-1)(n-2)(n-3)}{8(2n-3)(2n-5)(2n-7)},
\]
\[
a_n=\mathbb E A_n=4b_n.
\]

**Mixed moments.** Expand \(C_nB_n\) as a sum of ordered pairs consisting of a cherry and a balanced-four-leaf fringe node. If the pair's leaf sets are nested, each balanced four-leaf subtree contains exactly two cherry nodes. Thus these terms contribute \(2b_n\) to \(\mathbb E(C_nB_n)\). If the leaf sets are disjoint, choose the cherry pair, then a four-set avoiding it, then one of three balanced labeled topologies; the contraction lemma supplies the residual probability. Set
\[
d_n=\begin{cases}
3\binom n2\binom{n-2}4\dfrac{t_{n-4}}{t_n},&n\ge6,\\
0,&n=4,5.
\end{cases}
\]
Consequently \(\mathbb E(C_nB_n)=2b_n+d_n\). An asymmetric four-leaf fringe subtree has exactly one internal cherry, and there are four times as many labeled asymmetric topologies. The identical case split gives \(\mathbb E(C_nA_n)=a_n+4d_n\). No other overlap is possible by laminarity.

It follows that
\[
\operatorname{Cov}(C_n,B_n)=2b_n+d_n-c_nb_n,
\qquad
\operatorname{Cov}(C_n,A_n)=a_n+4d_n-c_na_n.
\]
For \(n\ge6\), substitute \(t_{n-4}/t_n=[(2n-3)(2n-5)(2n-7)(2n-9)]^{-1}\) and the first-moment formulas, then collect factors; this gives the two boxed expressions. The same expressions hold at \(n=4,5\) by setting \(d_n=0\), checked directly in the displayed first-moment identities. In particular, at \(n=4\), the covariances are \(4/25\) and \(-4/25\).

**Strict signs and limits.** For \(n\ge5\), \(Q_n>0\), while \(3n^2-19n+24>0\) and \(n^2-5n+3>0\). Therefore the covariance signs are strictly opposite. Direct computation settles \(n=4\). Leading powers give the two linear-order limits. Moreover,
\[
\frac{\operatorname{Cov}(C_n,B_n)}{-\operatorname{Cov}(C_n,A_n)}=
\frac{3n^2-19n+24}{4(n^2-5n+3)}.
\]
For integer \(n\ge5\), the next-minus-current difference equals
\[
\frac{2n^2-13n+24}{2(n^2-5n+3)(n^2-3n-1)}>0.
\]
The numerator is positive for every real \(n\), since its discriminant is negative and its leading coefficient positive; both denominator factors are positive for \(n\ge5\). This proves the ratio statement.

## Verification

The companion standalone Python 3 script `verify.py` enumerates every rooted nonplane leaf-labeled binary tree by inserting the new largest-labeled leaf into each existing edge, including the root stem. It checks the exact tree total \((2n-3)!!\), independently counts every cherry and four-leaf fringe topology, and compares all exact rational first moments and mixed covariances against both the contraction formulas and the simplified rational formulas for \(4\le n\le8\). Its last execution passed 146650 integer/rational assertions. In particular, it exhaustively enumerates 135135 rooted trees with eight leaves. This computation tests small finite instances only; the all-\(n\) result is supplied by the contraction-and-laminarity proof above. Run with `python3 verify.py` from the package directory; no third-party modules are required.

## Relationship to prior work

Chang and Fuchs (2009/2010) develop general single-fringe-pattern count asymptotics and moments under uniform and Yule tree models, but their inspected results do not state this cross-covariance between two different four-leaf types and the two-leaf type. Wu and Choi (2015/2016) obtain exact joint cherry/pitchfork distributions for rooted PDA trees, not the mixed cherry/four-leaf shape statistics. Coronado et al. (2018/2019) study a rooted quartet balance index based on *induced* trees on all four-leaf subsets, not four-leaf *fringe* nodes. Choi et al. (2024) explicitly derive the covariance matrix of cherry, pitchfork, balanced-quartet and asymmetric-quartet counts for **unrooted** PDA trees; this is the closest structural precedent. Their unrooted statistic aggregates both sides of edge cuts and is not the same as the rooted descendant statistic. In particular, appending an outgroup leaf to a rooted four-leaf tree gives a five-leaf unrooted tree with the same unlabeled unrooted shape regardless of whether the rooted tree is balanced or asymmetric, although its rooted balanced-four-leaf count differs. These comparisons delimit the claim, not certify literature-wide priority.

## Limitations

The theorem is restricted to uniformly sampled rooted **labeled** nonplane binary phylogenetic trees under the PDA law. It does not supply a full joint probability law of \((C_n,B_n,A_n)\), a central limit theorem, nor results under Yule, alpha, or unrooted models. The formulas are not claimed independent of the existing general fringe-pattern framework. A historical source could contain an implicit mixed-moment specialization; full independent literature audit has not been performed.

## References

1. H. Chang and M. Fuchs, *Limit theorems for patterns in phylogenetic trees*, Journal of Mathematical Biology 60 (2010), 481–512. First online 2009. https://doi.org/10.1007/s00285-009-0275-6 ; author manuscript: https://web.math.nccu.edu.tw/mfuchs/parameters_pt_rev.pdf
2. T. Wu and K. P. Choi, *On joint subtree distributions under two evolutionary models*, Theoretical Population Biology 108 (2016), 13–23; arXiv v1 dated 2015-08-13. https://arxiv.org/abs/1508.03139 ; accessible accepted manuscript: https://ueaeprints.uea.ac.uk/id/eprint/55603/1/Pattern_stat_TPB_final.pdf
3. T. M. Coronado, A. Mir, F. Rosselló and G. Valiente, *A balance index for phylogenetic trees based on rooted quartets*, Journal of Mathematical Biology 79 (2019), 1105–1148; arXiv 2018. https://arxiv.org/abs/1803.01651
4. K. P. Choi, G. Kaur, A. Thompson and T. Wu, *Distributions of 4-subtree patterns for uniform random unrooted phylogenetic trees*, Journal of Theoretical Biology 584 (2024), 111794. https://doi.org/10.1016/j.jtbi.2024.111794 ; accessible full text: https://ueaeprints.uea.ac.uk/94703/7/Choi_etal_2024_JTB.pdf
