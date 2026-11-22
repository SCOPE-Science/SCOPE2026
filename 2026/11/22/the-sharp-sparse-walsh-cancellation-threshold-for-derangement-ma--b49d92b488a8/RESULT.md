# The sharp sparse Walsh-cancellation threshold for derangement matchings

## Finding

For every integer \(n\ge2\), let \(\mathcal D_n\) be the set of all derangement permutations of \(\{1,\ldots,n\}\). Let \(\mathcal C_n=\{P_\pi:\pi\in\mathcal D_n\}\subseteq G_n\) be their incidence matrices in the additive Boolean matrix group \(G_n=(\mathbb Z/2\mathbb Z)^{n\times n}\). Write \(d_n=|\mathcal D_n|\). For an off-diagonal set of matrix positions \(S\), let
\[
W_n(S)=\sum_{\pi\in\mathcal D_n}(-1)^{|S\cap\{(i,\pi(i)):1\le i\le n\}|}.
\]
For every integer \(n\ge3\) and every off-diagonal \(S\) of size \(k\),
\[
\boxed{W_n(S)\ge d_n\left(1-\frac{2k}{n-1}\right).}
\]
For \(0\le k\le n-1\), the bound is sharp: the minimum is attained by selecting \(k\) permitted positions in one row or column. For \(n\ge4\), these are **all** minimizers, with the empty set and the singleton cases understood in the usual way. For \(2\le k\le n-1\), there are exactly \(2n\binom{n-1}{k}\) minimizing off-diagonal sets; for \(k=1\), there are \(n(n-1)\), and for \(k=0\), one.

Consequently, counting convolution by \(\mathbf1_{\mathcal C_n}\) is invertible on functions on \(G_n\) **if and only if \(n\) is even** (for all \(n\ge2\)). For odd \(n\ge3\), the least Hamming weight of a vanishing Fourier frequency is exactly \((n-1)/2\). At this first vanishing weight, all vanishing off-diagonal signings are stars, and their number is
\[
\boxed{\begin{cases}6,&n=3,\\2n\binom{n-1}{(n-1)/2},&n\ge5\text{ odd}.\end{cases}}
\]
(The Hamming weight is measured in the full Boolean matrix; diagonal frequencies never affect a multiplier.) In particular, every Walsh character supported on fewer than \((n-1)/2\) entries has a strictly positive multiplier when \(n\) is odd.

## Assumptions and scope

A derangement is a permutation \(\pi\) with \(\pi(i)\ne i\) for each \(i\). A permitted position \((i,j)\) has \(i\ne j\). A frequency \(A\in G_n\) has Walsh eigenvalue \(\sum_{\pi\in\mathcal D_n}(-1)^{\sum_i A_{i,\pi(i)}}\), so it depends only on the off-diagonal support \(S\). Convolution is unnormalized, \((T_nf)(x)=\sum_{y\in\mathcal C_n}f(x-y)\); Fourier normalization therefore does not enter the zero-set criterion. Here minimization is of the **signed** Walsh eigenvalue at fixed frequency weight, not its absolute value. No claim is made about the full higher-weight Fourier zero set.

## Proof

**Uniform marginal.** There are \(d_n\) derangements. By simultaneous permutation of row and column labels, each of the \(n(n-1)\) allowed edges occurs equally often; each derangement uses exactly \(n\) edges, so any allowed position belongs to exactly \(d_n/(n-1)\) derangements. Let \(X_S(\pi)\) count the selected edges in a uniformly chosen derangement. Then \(\mathbb E X_S=k/(n-1)\). For every nonnegative integer \(t\),
\[
(-1)^t\ge 1-2t,
\]
with equality if and only if \(t\in\{0,1\}\). Averaging gives the announced lower bound; equality holds precisely if **no derangement uses two distinct selected edges**.

**Extension lemma and equality geometry.** For \(n\ge4\), any two allowed positions \((i,j)\), \((i',j')\) in distinct rows and distinct columns extend to a derangement. Indeed, after imposing them, delete their two rows and columns. The residual bipartite graph has \(m=n-2\ge2\) rows and \(m\) columns, and forbids only possible diagonal pairs. Every residual row excludes at most one column, and different residual rows exclude different columns. For a single row, Hall's neighborhood has size at least \(m-1\ge1\); for any collection of at least two rows, its neighborhood is the full residual column set. Hall's criterion supplies a perfect matching, yielding the desired derangement. Thus equality in the bound forbids a pair of chosen edges in distinct rows and columns. A pairwise-intersecting set of at least two edges of a bipartite graph is necessarily a star centered on one row or one column. Conversely a star meets every permutation matching in at most one edge, so equality holds. The counting formula follows from choosing a row or column and a \(k\)-subset of its \(n-1\) allowed edges; for \(k\ge2\), two such stars cannot give the same set. For \(k=0,1\), the stated separate counts eliminate duplication. This proves the sharp fixed-weight signed minimum and classification.

**Parity and cancellation.** The classical derangement recurrence \(d_0=1\), \(d_1=0\), and \(d_n=(n-1)(d_{n-1}+d_{n-2})\) shows that \(d_n\) is odd exactly when \(n\ge2\) is even. Every Walsh multiplier is a sum of \(d_n\) signs and hence has the parity of \(d_n\). Therefore, for even \(n\), every multiplier is odd and nonzero, and Fourier diagonalization proves invertibility. For odd \(n\ge3\), the lower bound is strictly positive when \(k<(n-1)/2\). At \(k=(n-1)/2\), any \(k\)-edge star has eigenvalue zero, proving sharpness. If \(n\ge5\), the equality classification proves every first-weight zero is a star, giving the exact count. At \(n=3\) the first weight is one, and all six permitted singleton edges vanish. At \(n=2\), there is one derangement, so no multiplier vanishes. Diagonal frequency positions cannot occur in a minimum-weight zero, since deleting them retains the multiplier while reducing the weight.

## Verification

The standalone standard-library checker `check_derangement_first_zero.py` independently evaluates signed hollow permanents by subset dynamic programming and evaluates the Walsh sums by direct derangement enumeration. It exhaustively checks every sign support up to the stated weights for \(n=3,4,5,6,7\), validates the exact minimizer characterization, and checks the parity and star identities through \(n=16\). It reports `DERANGEMENT_SPARSE_WALSH_PASS; exact assertions/groups: 23518`. The proof above, not finite extrapolation, establishes the infinite-family statements.

## Relationship to prior work

The unsigned derangement recurrence and hollow permanent are classical; Feinsilver–McSorley study zeon algebras and generalized derangement permanents, but not the independently signed off-diagonal Walsh transform and sharp first-cancellation layer. Wanless studies permanents of complete signed-one matrices, rather than the hollow matrix with fixed zero diagonal and its minimum negative-entry zero set. A published exact order-five signed hollow permanent calculation gives the full absolute Walsh histogram and endpoint projection norm for the \(44\) five-letter derangements, but states neither the all-order sharp Hamming-sparse lower envelope nor the classification of its equality cases. A published sharp first-cancellation result for **complete-graph spanning trees** concerns a different support family and does not imply the derangement theorem. The contribution here is the all-order sharp signed weight envelope and extremal star geometry, not a claim of discovery of the derangement numbers or the order-five distribution.

## Limitations

This result does not classify zero characters at larger support, count all Fourier zeros, determine sharp \(\ell^1\) inverse/projection norms, or supply an absolute-value lower bound beyond the positive sparse range. The star-minimizer uniqueness statement requires \(n\ge4\), with \(n=3\) handled separately. The source priority search is bounded; an unindexed equivalent for signed permanents or rook polynomials may exist. No independent mathematical validation has been performed.

## References

1. I. M. Wanless, *Permanents of matrices of signed ones*, Linear and Multilinear Algebra 53 (2005), 427–433; DOI `10.1080/03081080500093990`. Publisher reports online publication 2006-08-06. Author open full text: `https://users.monash.edu.au/~iwanless/papers/wangconjLAMA.pdf`.
2. P. Feinsilver and J. McSorley, *Zeons, Permanents, the Johnson Scheme, and Generalized Derangements*, International Journal of Combinatorics (2011), Article ID 539030, first published 2011-06-02, DOI `10.1155/2011/539030`; full text: `https://onlinelibrary.wiley.com/doi/10.1155/2011/539030`.
3. *Exact Walsh spectrum and sharp projection norm for five-letter derangements*, 2026 published research record `2026/11/16/SCOPE-exact-walsh-spectrum-and-sharp-projection-norm-for-five-letter-d--ca7e522e4dc1`, `https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-exact-walsh-spectrum-and-sharp-projection-norm-for-five-letter-d--ca7e522e4dc1`.
4. *The sharp first Walsh cancellation threshold for complete-graph spanning trees*, 2026 published research record `2026/11/16/SCOPE-the-sharp-first-walsh-cancellation-threshold-for-complete-graph--44e28ad20e0e`, `https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-the-sharp-first-walsh-cancellation-threshold-for-complete-graph--44e28ad20e0e`.
