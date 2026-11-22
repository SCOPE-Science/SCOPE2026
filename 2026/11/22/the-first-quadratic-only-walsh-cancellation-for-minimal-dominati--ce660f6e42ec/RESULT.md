# The first quadratic-only Walsh cancellation for minimal domination of paths

## Finding
Let \(P_n\) be the labelled path on vertices \(1,\ldots,n\). Write \(\mathcal D_n\) for **all inclusion-minimal** dominating vertex subsets (not merely minimum-cardinality dominating sets), and let \(f_n:\mathbb F_2^n\to\{0,1\}\) be the indicator of their binary vertex-incidence vectors. Define the unnormalized Walsh multipliers
\[
W_n(S)=\sum_{D\in\mathcal D_n}(-1)^{|D\cap S|},\qquad S\subseteq\{1,\ldots,n\}.
\]
Then \(n=17\) is the **least** positive path order for which any Walsh multiplier vanishes but every singleton multiplier remains nonzero. At that order there are exactly \(268\) minimal dominating sets, \(19{,}516\) vanishing Walsh multipliers among \(2^{17}=131{,}072\), and exactly \(15\) vanishing multipliers of support size two; there are no vanishing multipliers of support less than two. Consequently convolution by \(f_{17}\) has rank \(111{,}556\), sharp least nonzero absolute multiplier \(2\), and positive-spectrum condition number \(134\).

For \(G=\mathbb F_2^{17}\), let \(\mathcal R\) be the convolution range in \(\ell^p(G)\). Among **all** real or complex linear projections onto \(\mathcal R\), the sharp minimum operator norm is
\[
\min_{Q^2=Q,\ \mathrm{ran}(Q)=\mathcal R}\|Q\|_{\ell^1\to\ell^1}
=\min_{Q^2=Q,\ \mathrm{ran}(Q)=\mathcal R}\|Q\|_{\ell^\infty\to\ell^\infty}
=\frac{417721}{16384}.
\]
The complete list of zero-pair supports (with vertices numbered from one) is
\[
\begin{gathered}
\{1,16\},\{1,17\},\{2,16\},\{2,17\},\{3,5\},\\
\{3,7\},\{3,8\},\{3,11\},\{3,12\},\{4,14\},\\
\{6,15\},\{7,15\},\{10,15\},\{11,15\},\{13,15\}.
\end{gathered}
\]

## Assumptions and scope
All groups and Fourier characters are over \(\mathbb F_2\), with unnormalized Fourier transform \(\widehat f(S)=\sum_x f(x)(-1)^{\langle S,x\rangle}\). Domination uses the **closed** neighborhood: \(D\subseteq[n]\) dominates \(P_n\) if each vertex is in \(D\) or adjacent to an element of \(D\). Minimal means inclusion-minimal, not minimum size. A character's degree is \(|S|\). The stated minimality of path order is only for \(1\le n\le17\); no classification of all later orders is asserted.

## Proof
**Finite classification.** Put \(N[j]=\{j-1,j,j+1\}\cap[n]\). The following exact criterion holds: \(D\) is an inclusion-minimal dominating set if and only if (a) \(D\cap N[j]\ne\varnothing\) for every \(j\), and (b) for every \(i\in D\), there is a \(j\in N[i]\) with \(D\cap N[j]=\{i\}\). Indeed, (a) is domination, and the \(j\) from (b) is a private neighbor lost if \(i\) is deleted. Conversely, if no such \(j\) exists, deleting \(i\) leaves a dominating set. Therefore a complete scan of \(2^n\) incidence masks and these local tests enumerates **all** required sets without sampling or omissions.

The accompanying executable certificate evaluates this criterion for every \(n=1,\ldots,17\). It independently computes the same families using incremental enumeration of inclusion-minimal transversals of the closed-neighborhood hypergraph; equality of the two sorted set lists is asserted at each order. For every order it applies a full exact-integer fast Walsh–Hadamard transform of length \(2^n\). The verified tuples (order, minimal-set count, zero-character count, zero-singleton count) are:

| \(n\) | \(|\mathcal D_n|\) | Zeros | Zero singletons |
|---:|---:|---:|---:|
|1|1|0|0|
|2|2|2|2|
|3|2|4|3|
|4|4|12|4|
|5|4|12|4|
|6|7|0|0|
|7|9|0|0|
|8|13|0|0|
|9|18|152|6|
|10|25|0|0|
|11|36|952|4|
|12|49|0|0|
|13|70|1848|2|
|14|97|0|0|
|15|137|0|0|
|16|191|0|0|
|17|268|19516|0|

The \(n=17\) zero characters have the degree distribution \((2:15),(3:88),(4:372),(5:1034),(6:2210),(7:3564),(8:4205),(9:3746),(10:2497),(11:1212),(12:425),(13:120),(14:24),(15:4)\); no other degrees occur. Direct character sums independently identify precisely the fifteen degree-two zeros listed above. Every singleton multiplier is nonzero. The largest multiplier is \(268\), and a surviving multiplier has magnitude \(2\), establishing the condition number.

**Optimal endpoint projection.** The convolution range is the span of precisely those Walsh characters with nonzero \(W_{17}(S)\). The canonical Fourier projection \(P\) onto that range is convolution with
\[
q(x)=2^{-17}\sum_{S:W_{17}(S)\ne0}(-1)^{\langle S,x\rangle}.
\]
Its \(\ell^1\) and \(\ell^\infty\) operator norms both equal \(\sum_x|q(x)|\). The exact second integer Walsh transform in the certificate gives
\[
\sum_{x\in G}\left|\sum_{S:W_{17}(S)\ne0}(-1)^{\langle S,x\rangle}\right|=3{,}341{,}768,
\]
so \(\|P\|=3{,}341{,}768/131{,}072=417{,}721/16{,}384\). If \(Q\) is any projection onto this range, average its conjugates by all \(2^{17}\) translations. The averaged operator is a projection onto the same translation-invariant range, commutes with all translations, and has operator norm at most \(\|Q\|\) on either endpoint space. Such a translation-commuting projection must have Fourier multiplier one on the range and zero on its complement, hence is \(P\). This proves unrestricted optimality over both scalar fields.

## Verification
The file `verify.py` is a standalone Python 3 integer-only certificate. Run `python3 verify.py` in this directory. It requires no third-party packages and asserts equality of two independent finite enumerators at all 17 orders, verifies the complete first-occurrence table, the degree-two support list, rank, exact positive spectral gap, and the projection norm. Both signed transforms have exact integer arithmetic, with no numerical tolerances or floating point. The sorted \(268\)-mask census has SHA-256 `e828ca5d8b975f47f7df6f69973d352d88e95403acffc7bf27c5c65674d4ad68` when masks are joined as decimal integers by commas, without a trailing newline.

## Relationship to prior work
Alikhani and Peng (2009) treat domination **polynomials of all dominating sets** on paths, not the incidence Fourier spectrum of inclusion-minimal families. Kanté, Limouzy, Mary, Nourine and Uno (2013) give algorithms and counts of minimal dominating sets in interval graphs, including paths. Kanté, Limouzy, Mary and Nourine (2014), and Kanté et al. (2014), develop minimal-dominating-set enumerators for graph classes, including chordal graphs, and provide the private-neighbor criterion used here; their mathematical conclusions concern enumeration algorithms and hypergraph transversals, not signed character cancellation. Related results on maximal independent sets of paths concern a strictly smaller family, since many minimal dominating sets contain adjacent vertices. These results therefore do not imply the specific first quadratic-only cancellation, the 17-vertex rank, or the optimal projection constant.

## Limitations
This is an exact **finite boundary theorem**, not a general closed formula in the path order. The independent certificate establishes finite enumeration; it does not certify unseen higher orders. Neither the all-order Walsh zero set nor convergence or asymptotics of endpoint projection norms is asserted. Literature comparisons are bounded: an unindexed equivalent signed enumeration remains possible, and independent mathematical audit has not been performed.

## References
1. S. Alikhani and Y.-H. Peng, *Dominating Sets and Domination Polynomials of Paths*, International Journal of Mathematics and Mathematical Sciences (2009), DOI: https://doi.org/10.1155/2009/542040 (first published 2009-05-05).
2. M. M. Kanté, V. Limouzy, A. Mary and L. Nourine, *On the Enumeration of Minimal Dominating Sets and Related Notions*, arXiv:1407.2053 (first public version 2014-07-08), https://arxiv.org/abs/1407.2053.
3. M. M. Kanté, V. Limouzy, A. Mary, L. Nourine and T. Uno, *A Polynomial Delay Algorithm for Enumerating Minimal Dominating Sets in Chordal Graphs*, arXiv:1407.2036 (first public version 2014-07-08), https://arxiv.org/abs/1407.2036.
4. M. M. Kanté, V. Limouzy, A. Mary, L. Nourine and T. Uno, *On the Enumeration and Counting of Minimal Dominating Sets in Interval and Permutation Graphs* (2013), author-hosted full text, https://perso.isima.fr/~makante/articles/kanteLMNU13.pdf.
