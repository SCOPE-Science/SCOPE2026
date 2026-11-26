# Exact anticorrelation of two Narayana statistics in a uniform plane tree

## Finding
Let \(T_n\) be uniformly distributed over the \(C_{n-1}\) rooted ordered (plane) trees with \(n\ge3\) vertices. Write \(E_n\) for the number of vertices at even graph distance from the root (including the root), and \(L_n\) for the number of vertices with no children. Each statistic has the same Narayana distribution, yet on the *same sampled tree*
\[
\operatorname{Cov}(E_n,L_n)=-\frac{n}{4(2n-3)},\qquad
\operatorname{Corr}(E_n,L_n)=-\frac1{n-2}.
\]
Both expectations are \(n/2\) and both variances are \(n(n-2)/[4(2n-3)]\). In particular the covariance is strictly negative for all \(n\ge3\), equals \(-1/8+O(n^{-1})\) as \(n\to\infty\), and the correlation tends to zero at rate \(-1/n\). For \(n=2\) both counts are identically one and their covariance is zero; correlation is undefined. For \(n=3\) the correlation is exactly \(-1\).

## Assumptions and scope
A rooted ordered tree is a finite unlabeled rooted tree with a specified ordering of the children of each vertex, up to root- and order-preserving isomorphism. All \(C_{n-1}=\binom{2n-2}{n-1}/n\) trees of size \(n\) have equal probability. Level zero is even, and a leaf is a vertex of outdegree zero, whether or not it is the root. No independent re-sampling or bijection is applied between the two statistics. The covariance statement concerns a single tree and holds for every integer \(n\ge3\), without asymptotic assumptions.

## Proof
Introduce ordinary generating functions \(F(z;x,y)\) and \(G(z;x,y)\) for plane rooted trees whose root is respectively at an even or odd global depth. The variable \(z\) records every vertex; \(x\) records even-depth vertices; \(y\) records leaves. As an empty ordered sequence of children marks a leaf and nonempty sequences do not, the unique formal power series with zero constant terms satisfy
\[
F=zx\left(y-1+\frac{1}{1-G}\right),\qquad
G=z\left(y-1+\frac{1}{1-F}\right).
\]
The desired joint probability generating polynomial at size \(n\) is \([z^n]F(z;x,y)/C_{n-1}\). At \(x=y=1\), \(F=G=T\), where \(T=z/(1-T)=(1-\sqrt{1-4z})/2\).

Setting \(y=1\) and eliminating \(G\) gives
\[
F(z;x,1)^2-(1-z+zx)F(z;x,1)+zx=0.
\]
Setting \(x=1\) forces \(F=G=Q\) and gives the *same* quadratic with \(y\) in place of \(x\). Both solutions with zero constant terms therefore agree after identifying \(x=y=q\). Their positive-degree coefficients have the Narayana expansion
\[
[z^n]F(z;q,1)=[z^n]F(z;1,q)=
\sum_{k=1}^{n-1}\frac1{n-1}\binom{n-1}{k}\binom{n-1}{k-1}q^k\quad(n\ge2).
\]
Its factorial moments, obtained by differentiation, give
\[
\mathbb E E_n=\mathbb E L_n=\frac n2,\qquad
\operatorname{Var}(E_n)=\operatorname{Var}(L_n)=\frac{n(n-2)}{4(2n-3)}.
\]

To calculate the *joint*, rather than merely marginal, moment, differentiate the two coupled functional equations once in each marking variable and solve the resulting linear equations. With \(s=\sqrt{1-4z}\), direct simplification gives the formal identity
\[
\left.\frac{\partial^2 F}{\partial x\,\partial y}\right|_{x=y=1}
=\frac{s^4-2s^3-6s^2+s+5+s^{-3}}{32}.
\]
For every \(n\ge3\), the polynomial terms \(s^4\), \(s^2\), and \(1\) contribute zero to \([z^n]\). The other three terms use the binomial expansions
\[
[z^n]s=-\frac1{2n-1}\binom{2n}{n},\quad
[z^n]s^3=\frac3{(2n-1)(2n-3)}\binom{2n}{n},\quad
[z^n]s^{-3}=(2n+1)\binom{2n}{n}.
\]
Thus
\[
[z^n]F_{xy}(z;1,1)=\frac1{32}\binom{2n}{n}
\left(2n+1-\frac1{2n-1}-\frac6{(2n-1)(2n-3)}\right).
\]
Since \(C_{n-1}=\binom{2n}{n}/[2(2n-1)]\), division by the tree count yields
\[
\mathbb E(E_nL_n)=\frac{n^2}{4}-\frac{n}{4(2n-3)}.
\]
Subtracting \(\mathbb E E_n\,\mathbb E L_n=n^2/4\) proves the covariance formula. Dividing by the identical positive variances proves the correlation formula. The two smaller cases follow by inspecting the only tree at \(n=2\), and the two trees at \(n=3\). The stated asymptotics follow directly from the rational expressions.

## Verification
The included standalone `verify_parity_leaf.py` independently enumerates all rooted ordered trees for each \(2\le n\le11\), checks Catalan totals, both Narayana histograms, exact means and variances, mixed moments, the covariance and the correlation. It also checks the coefficient extracted from \(F_{xy}\) against the enumerated integer sum. Running `python verify_parity_leaf.py` produces `PASS 113 exact assertions; exhaustive plane trees n=2..11`. Exact symbolic differentiation and binomial coefficient extraction above provide the proof for all \(n\), not this finite enumeration.

## Relationship to prior work
The common marginal Narayana distribution is classical; in particular the equivalence between leaf count and the number of even-level vertices is discussed by Chen (2019), citing Deutsch's earlier bijection. Neither equidistribution nor a bijection transferring one statistic to the other gives their covariance *on the same tree*. Chen, Li and Shapiro (2005) treat butterfly decompositions of plane trees, returns and leaf coloring rather than this same-tree mixed moment. Janson (2011) treats simply generated ordered trees and asymptotics rather than the exact mixed covariance. Mallows and Wachter (1972) give an enumerator involving black-node valencies in bichromatic plane trees, a potentially stronger enumerative framework; its full text could not be assessed here. The contribution is the exact same-tree mixed moment and its unusually simple finite-size correlation, not the classical Catalan or Narayana enumerations.

## Limitations
The theorem concerns uniformly distributed *ordered* rooted trees and these two specified counts; it does not assert the same formula for uniformly labeled, unordered, simply generated with nonconstant weights, or conditioned trees. Small-tree computation alone would not establish the all-size result; that conclusion uses the generating-function proof. Historical priority is provisional: an older, more general bicolored degree generating function might implicitly contain the formula, especially the 1972 Mallows--Wachter article, which was available only by abstract during this assessment. No independence is asserted; in particular zero limiting correlation is not exact independence.

## References
- W. Y. C. Chen, N. Y. Li, L. W. Shapiro, *The Butterfly Decomposition of Plane Trees*, arXiv:math/0511045v1, first posted 2005-11-02, https://arxiv.org/abs/math/0511045.
- S. Janson, *Simply generated trees, conditioned Galton--Watson trees, random allocations and condensation*, arXiv:1112.0510v1, first posted 2011-12-02, https://arxiv.org/abs/1112.0510.
- R. X. F. Chen, *A New Bijection Between RNA Secondary Structures and Plane Trees and its Consequences*, Electronic Journal of Combinatorics 26(4), P4.48 (2019), DOI:10.37236/8540, https://www.combinatorics.org/ojs/index.php/eljc/article/view/v26i4p48.
- C. L. Mallows, K. W. Wachter, *Valency enumeration of rooted plane trees*, Journal of the Australian Mathematical Society 13 (1972), 472--476, DOI:10.1017/S1446788700009228, https://doi.org/10.1017/S1446788700009228 (abstract accessible; full text not inspected).
