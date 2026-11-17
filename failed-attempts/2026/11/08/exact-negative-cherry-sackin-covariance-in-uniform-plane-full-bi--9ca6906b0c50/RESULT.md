# Exact negative cherry–Sackin covariance in uniform plane full binary trees

## Finding

Let \(H_n\) be the number of cherries, and \(S_n\) the sum of all leaf depths, in a uniformly chosen rooted ordered full binary tree with \(n\ge1\) internal vertices. Then

\[
\boxed{\operatorname{Cov}(H_n,S_n)=
-\frac{n+1}{4(2n-1)}\left((n+1)\frac{4^n}{\binom{2n}{n}}-4n\right).}
\]

This covariance vanishes exactly for \(n=1,2\), is strictly negative for every integer \(n\ge3\), and satisfies

\[
\operatorname{Cov}(H_n,S_n)\sim-\frac{\sqrt{\pi}}8 n^{3/2}
\qquad(n\to\infty).
\]

Thus a local symmetry count and a global depth cost have a strictly negative finite-sample dependence, of growing absolute magnitude, under a uniform Catalan-tree null model.

## Assumptions and scope

Trees are rooted, plane (left and right child positions are distinct), finite, and full (every internal vertex has exactly two children). The size \(n\) is the number of internal vertices; there are \(n+1\) external leaves and exactly \(C_n=\binom{2n}{n}/(n+1)\) equiprobable trees. Depth is measured in edges from the root. A cherry is an internal vertex with two leaf children. Let \(P_n\) denote the sum of depths of all internal vertices. Every such tree satisfies \(S_n=P_n+2n\), so the covariance with \(S_n\) equals that with \(P_n\). The one-leaf tree is used only as a size-zero component in decompositions and has all three statistics equal to zero.

## Proof

**1. Root decomposition.** For a nontrivial tree \(T=(L,R)\), let \(\ell\) and \(r\) denote the internal-vertex counts of its ordered subtrees. Thus \(|T|=1+\ell+r\). For the number of cherries \(H\) and internal path length \(P\),

\[
H(T)=H(L)+H(R)+\mathbf1_{\{\ell=r=0\}},\qquad
P(T)=P(L)+P(R)+\ell+r.
\]

The leaf-depth identity \(S(T)=P(T)+2|T|\) follows by induction: at the root the two subtree leaf counts sum to \(|T|+1\), and the depth shift adds one per leaf.

**2. Weighted generating functions.** Sum over all plane full binary tree shapes (including the one-leaf component) and write

\[
C(z)=\sum_Tz^{|T|},\quad U(z)=\sum_T H(T)z^{|T|},\quad
B(z)=\sum_T P(T)z^{|T|},\quad Q(z)=\sum_T H(T)P(T)z^{|T|}.
\]

Let \(s=\sqrt{1-4z}\), expanded with constant term one. The Catalan decomposition gives \(C=1+zC^2=(1-s)/(2z)\), and hence \(1-2zC=s\). Applying the preceding recurrences, with derivatives referring to \(z\), yields

\[
\begin{aligned}
U&=2zCU+z,\\
B&=2zCB+2z^2 CC',\\
Q&=2zCQ+2zUB+2z^2(CU'+UC').
\end{aligned}
\]

The term \(2zUB\) accounts for a cherry in one subtree and path length in the other. The term involving derivatives accounts for the depth shift \(\ell+r\). A root cherry has \(\ell+r=0\), so it contributes no extra mixed moment. Solving gives

\[
\begin{aligned}
U&=\frac{z}{s},\\
B&=2C-\frac3s+\frac1{s^2},\\
Q&=\frac s8-\frac14+\frac1{4s}-\frac3{8s^3}+\frac1{4s^4}.
\end{aligned}
\]

**3. Exact coefficient extraction.** For every integer \(n\ge1\), put \(c_n=\binom{2n}{n}/(n+1)\). Coefficient extraction using the standard central-binomial identities gives

\[
\begin{aligned}
[z^n]U &= \binom{2n-2}{n-1},\\
[z^n]B &= 4^n-3\binom{2n}{n}+2c_n,\\
[z^n]Q &= \frac{n+1}{4}4^n-
\frac{6n+1}{8}\binom{2n}{n}-\frac14c_{n-1}.
\end{aligned}
\]

In particular \([z^n]s=-2c_{n-1}\), \([z^n]s^{-3}=(2n+1)\binom{2n}{n}\), and \([z^n]s^{-4}=(n+1)4^n\). The uniform mean is obtained by dividing each coefficient sum by \(c_n\). Thus

\[
\operatorname{Cov}(H_n,P_n)=
\frac{[z^n]Q}{c_n}-
\frac{[z^n]U\,[z^n]B}{c_n^2}
=-\frac{n+1}{4(2n-1)}
\left((n+1)\frac{4^n}{\binom{2n}{n}}-4n\right),
\]

using only \(c_n=\binom{2n}{n}/(n+1)\) and \(c_{n-1}=\binom{2n}{n}/[2(2n-1)]\). The identity with \(S_n\) follows from the deterministic shift by \(2n\).

**4. Sign and asymptotics.** Define

\[
R_n=\frac{n+1}{4n}\frac{4^n}{\binom{2n}{n}}\quad(n\ge1).
\]

Direct calculation gives \(R_1=R_2=1\) and, for every \(n\ge2\),

\[
\frac{R_{n+1}}{R_n}=
\frac{2n(n+2)}{(n+1)(2n+1)}
=1+\frac{n-1}{(n+1)(2n+1)}>1.
\]

Therefore the bracket in the covariance formula equals \(4n(R_n-1)\), proving the two zero cases and strict negativity thereafter. Finally, the central-binomial asymptotic \(\binom{2n}{n}\sim4^n/\sqrt{\pi n}\) yields the stated \(-\sqrt{\pi}n^{3/2}/8\) leading term.

## Verification

The standalone standard-library script `verify_cherry_path.py` independently implements exact integer mixed-moment recurrences for sizes \(1\le n\le55\), and additionally explicitly enumerates all Catalan shapes through \(n=11\). It checks the three first/mixed moment formulas, the resulting rational covariance, its signs, and independent exhaustive shape totals. A fresh execution reported **82,878 passed exact comparisons**. The universal proof above, rather than these finite tests, establishes the theorem for all \(n\).

## Relationship to prior work

The uniform plane Catalan model is central in Bacher, Bodini and Jacquot (2014), whose full-text study concerns uniform generation, not the cherry–path mixed covariance. Classical Catalan path-length theory supplies marginal techniques; Norton (2025) treats the cherry and Sackin statistics separately and explicitly identifies joint distributions as future directions. Other studies of cherry and Sackin statistics frequently use nonplane leaf-labeled phylogenetic-tree laws, which are not the present probability measure. No exact all-size cherry–Sackin covariance with its sign classification was identified in the inspected sources. This is a best-knowledge literature comparison, not a uniqueness or publication-priority proof.

## Limitations

The calculation applies to the uniform **plane** Catalan model, not automatically to uniform nonplane labeled trees, Yule trees, conditioned Galton–Watson laws with a different offspring distribution, or evolutionary models. It determines a mixed second moment, not the full joint distribution or limiting joint law. Older implicit formulas or later literature may contain equivalent statements; independent mathematical and bibliographical review is outstanding.

## References

- Axel Bacher, Olivier Bodini, Alice Jacquot, *Efficient random sampling of binary and unary-binary trees via holonomic equations*, arXiv:1401.1140 (first posted 2014-01-06), https://arxiv.org/abs/1401.1140 .
- Svante Janson, *Left and Right Pathlengths in Random Binary Trees* (2005 manuscript), https://www2.math.uu.se/~svantejs/papers/sj176.pdf .
- Andy McKenzie and Mike Steel, *Distributions of cherries for two models of trees*, Mathematical Biosciences 164 (2000), 81–92, https://pubmed.ncbi.nlm.nih.gov/10704639/ .
- Charles C. Norton, *A Unified Generating Function Framework for Tree Invariants* (public manuscript, 2025), https://github.com/CharlesCNorton/unified-tree-theory .
- Tomás M. Coronado et al., *On Sackin’s original proposal: the variance of the leaves’ depths as a phylogenetic balance index*, BMC Bioinformatics 21 (2020), article 154, https://doi.org/10.1186/s12859-020-3405-1 .
