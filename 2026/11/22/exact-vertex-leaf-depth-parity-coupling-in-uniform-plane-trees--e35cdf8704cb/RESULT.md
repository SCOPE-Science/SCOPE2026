# Exact vertex–leaf depth-parity coupling in uniform plane trees

## Finding
Let \(T_n\) be uniformly sampled from all rooted ordered (plane) trees with exactly \(n\ge3\) vertices. For the root-to-vertex distance \(d(v)\), let
\[
X_n=\sum_{v\in V(T_n)}(-1)^{d(v)},\qquad
Y_n=\sum_{v\in\operatorname{Leaf}(T_n)}(-1)^{d(v)}.
\]
Here a leaf has no children. The exact covariance is
\[
\boxed{\operatorname{Cov}(X_n,Y_n)=\frac n2}\qquad(n\ge3).
\]
More fully,
\[
\mathbb E X_n=0,\quad
\mathbb E Y_n=-\frac{n}{2(2n-3)},\quad
\operatorname{Var}(X_n)=\frac{n(n-2)}{2n-3},
\]
\[
\operatorname{Var}(Y_n)=\frac{5n}{8}+\frac{n}{8(2n-3)}
+\frac{n(n-1)}{4(2n-3)(2n-5)}-\frac{n^2}{4(2n-3)^2}.
\]
Consequently
\[
\lim_{n\to\infty}\operatorname{Corr}(X_n,Y_n)=\frac{2}{\sqrt5},
\qquad
\lim_{n\to\infty}\operatorname{Corr}(X_n,Y_n)^2=\frac45.
\]
Thus the best affine prediction of the signed leaf-depth imbalance from the signed all-vertex imbalance explains asymptotically four fifths of the former's variance. This is a statement about covariance and least-squares prediction, not a claimed joint central limit theorem.

## Assumptions and scope
Every plane tree shape with \(n\) vertices has probability \(1/C_{n-1}\), where \(C_j=\binom{2j}{j}/(j+1)\) is the Catalan number. The root is at depth zero, children are ordered, vertices are unlabeled, and parity signs are \(+1\) for even depth, \(-1\) for odd depth. All displayed exact claims apply to every integer \(n\ge3\). The two-vertex tree has zero all-vertex imbalance and is excluded from correlation statements. No restriction is made on degrees or height.

## Proof
Introduce the formal bivariate generating series
\[
F(z;s,t)=\sum_T z^{|T|}\exp\bigl(sX(T)+tY(T)\bigr),
\]
with the sum over all finite nonempty rooted ordered trees. Each subtree increases vertex depths by one. A one-vertex tree contributes \(ze^{s+t}\); a root with \(k\ge1\) subtrees contributes \(ze^s F(z;-s,-t)^k\). Therefore, as an identity in formal power series in \(z\) with coefficients analytic near \(s=t=0\),
\[
F(z;s,t)=ze^s\left(e^t+\frac{F(z;-s,-t)}{1-F(z;-s,-t)}\right). \tag{1}
\]
At zero marks, \(F_0=F(z;0,0)=(1-\sqrt{1-4z})/2\), with \(z=F_0(1-F_0)\). Define \(w=\sqrt{1-4z}=1-2F_0\), always the branch with constant term one.

Differentiating (1), including the negative signs from its reflected arguments, gives at \(s=t=0\)
\[
F_s=z,\qquad F_t=z(1-F_0),\qquad
F_{ss}=\frac{z(1-2z)}{w},
\]
\[
F_{st}=\frac{z}{2w}+\frac z2-z^2,\qquad
F_{tt}=\frac{z(1-F_0)+2z^3}{w}. \tag{2}
\]
These follow by solving the linear equations for each second derivative. For example, put \(a=z/(1-F_0)^2\). Since the second reflected mixed derivative has the same sign as \(F_{st}\), the mixed identity is
\[
(1-a)F_{st}=F_t+\frac{2zF_sF_t}{(1-F_0)^3},
\]
which simplifies to the fourth formula in (2). For the leaf square, the same-sign second reflected derivative gives
\[
(1-a)F_{tt}=z+\frac{2zF_t^2}{(1-F_0)^3},
\]
which gives the last formula in (2). All steps are identities of formal series, so they apply to every coefficient without an asymptotic approximation.

For every \(n\ge3\), coefficients are
\[
[z^n]F_{st}=\tfrac12\binom{2n-2}{n-1}=\tfrac n2 C_{n-1},
\]
\[
[z^n]F_{tt}=\frac5{32}\binom{2n}{n}
+\frac5{16}C_{n-1}+\frac14C_{n-2}+C_{n-3}.
\]
The second formula is obtained by writing \(F_{tt}\) as a polynomial in \(w\) and \(w^{-1}\), using \(w^2=1-4z\), and extracting coefficients. Likewise, \([z^n]F_s=0\), \([z^n]F_t=-C_{n-2}\), and \([z^n]F_{ss}=C_{n-1}n(n-2)/(2n-3)\). Dividing by \(C_{n-1}\) yields all expectations and raw moments. The Catalan ratios
\[
\frac{C_{n-2}}{C_{n-1}}=\frac{n}{2(2n-3)},\qquad
\frac{C_{n-3}}{C_{n-1}}=\frac{n(n-1)}{4(2n-3)(2n-5)}
\]
finish the stated formulas. Since \(\mathbb EX_n=0\), the mixed raw moment is already the covariance. The variances have respective leading terms \(n/2\) and \(5n/8\), giving the limiting correlation \(2/\sqrt5\).

## Verification
Run `python3 check_parity.py` from the directory containing the two files. The standalone Python program exhaustively generates all rooted ordered trees with \(3\le n\le11\), checks their Catalan counts, computes signed depths independently on every tree, and compares five rational moments with the theorem. It also checks two independent coefficient identities and numerical finite-size approach to the stated correlation limit. The execution passed 75 assertions. The analytic generating-function argument above, not that finite test, proves the all-size statements.

## Relationship to prior work
Meir and Moon (1999) analyze the bipartition-size difference of simply generated trees, including the plane-tree family. Janson (2005) gives depth-residue central limit results for conditioned Galton–Watson trees; plane trees are one of his examples. Chen, Li and Shapiro (first publicly posted 2005, published 2007) prove that the *mean* all-vertex parity imbalance vanishes and give the exact *mean* leaf-depth parity imbalance using a butterfly involution (their Corollary 4.3 and Proposition 4.4). These marginal identities are not claimed as new. The statement here concerns the previously unlocated **joint mixed moment**, complete variance of the leaf-depth sign, and their resulting nonzero limiting correlation. A separate paper by Chen, Shapiro and Yang (2005) treats parity of the *number of leaves*, not parity of their depths. The specific joint identity is not implied by the statements inspected in those works.

## Limitations
The result is confined to uniformly sampled rooted *ordered* tree shapes. It does not assert the same covariance for labeled, unordered, recursive, or full binary tree ensembles. The correlation statement is asymptotic; no joint distributional convergence or conditional independence statement is proved. Historical uniqueness is not certified: undiscovered equivalents, especially among bivariate generating-function refinements of the cited marginal results, remain possible. The independent mathematical audit has not been performed.

## References
1. A. Meir and J. W. Moon, *On the bipartition numbers of random trees, II*, Ars Combinatoria 51 (1999), 21–31. Full text: https://combinatorialpress.com/article/ars/Volume%2051/volume-51-paper-2.pdf .
2. S. Janson, *Congruence properties of depths in some random trees* (first public arXiv version 21 September 2005), https://arxiv.org/abs/math/0509471 .
3. W. Y. C. Chen, N. Y. Li and L. W. Shapiro, *The butterfly decomposition of plane trees* (first public arXiv version 2 November 2005; Discrete Applied Mathematics 155 (2007), 2187–2201), https://arxiv.org/abs/math/0511045 ; open full text: https://cfc.nankai.edu.cn/_upload/article/files/6c/0a/8a70749e40e2a1f0c7295f53f2f3/a618af21-3d6f-4af5-8b94-3feb88df9c64.pdf .
4. W. Y. C. Chen, L. W. Shapiro and L. L. M. Yang, *Parity reversing involutions on plane trees and 2-Motzkin paths* (15 March 2005), https://arxiv.org/abs/math/0503300 .
