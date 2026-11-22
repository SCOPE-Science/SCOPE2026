# A square-root-rank crossover in Gaussian widths of uniform hypergraph degree zonotopes

## Finding

For integers \(n\ge2\) and \(1\le k\le n-1\), let \([n]=\{1,\ldots,n\}\), \(v_S=\sum_{i\in S}e_i\) and
\[
Z_{n,k}=\sum_{\substack{S\subseteq[n]\\|S|=k}}[0,v_S]\subset\mathbb R^n.
\]
This is the convex hull of degree vectors of all simple \(k\)-uniform hypergraphs on \([n]\), including the empty hypergraph. The embedding is the unscaled standard Euclidean coordinate embedding. For \(G=(G_1,\ldots,G_n)\) with independent standard Gaussian coordinates define the directional width \(W_{n,k}(G)=h_{Z_{n,k}}(G)+h_{Z_{n,k}}(-G)\), and the normalized random width
\[
H_{n,k}=\frac{W_{n,k}(G)}{\binom nk\sqrt{k}}=\binom nk^{-1}\sum_{|S|=k}\left|k^{-1/2}\sum_{i\in S}G_i\right|.
\]
Set \(\mu=\sqrt{2/\pi}\) and
\[
C(u)=\frac2\pi\left(\sqrt{1-u^2}+u\arcsin u-1\right),\qquad0\le u\le1.
\]
**Exact finite-rank law:** \(\mathbb EH_{n,k}=\mu\) and
\[
\operatorname{Var}(H_{n,k})=\sum_{j=\max(0,2k-n)}^k
\frac{\binom kj\binom{n-k}{k-j}}{\binom nk}\,C(j/k).
\tag{1}
\]

**Square-root-rank crossover:** If \(k=k_n\to\infty\) and \(k/n\to0\), with independent standard normals \(X,Y\), then
\[
\begin{array}{ll}
\displaystyle k/\sqrt n\to c\in[0,\infty):&\displaystyle
\sqrt n(H_{n,k}-\mu)\ \Rightarrow\ \pi^{-1/2}Y+\frac{c}{\sqrt{2\pi}}(X^2-1),\\[5pt]
\displaystyle k/\sqrt n\to\infty:&\displaystyle
(n/k)(H_{n,k}-\mu)\ \Rightarrow\ (2\pi)^{-1/2}(X^2-1).
\end{array}
\tag{2}
\]
For \(c=0\), the first limit is Gaussian; for every \(c>0\) it is a convolution of a nondegenerate Gaussian and a centered chi-square, and hence non-Gaussian. The critical window is \(k\asymp\sqrt n\).

**Proportional-rank law:** If \(k/n\to\alpha\in(0,1]\), then
\[
H_{n,k}\ \Rightarrow\ f_\alpha(X),\qquad
f_\alpha(x)=\mathbb E_Y|\sqrt\alpha\,x+\sqrt{1-\alpha}\,Y|.
\tag{3}
\]
For \(0<\alpha<1\), equivalently,
\[
f_\alpha(x)=\sqrt{\frac{2(1-\alpha)}\pi}\exp\!\left(-\frac{\alpha x^2}{2(1-\alpha)}\right)
+\sqrt\alpha\,x\left[2\Phi\!\left(x\sqrt{\frac\alpha{1-\alpha}}\right)-1\right],
\]
where \(\Phi\) is the standard-normal distribution function; \(f_1(x)=|x|\). Here \(H_{n,k}-f_{k/n}(n^{-1/2}\sum_iG_i)\to0\) in \(L^2\). In particular its variance tends to \(C(\alpha)>0\): normalized Gaussian widths do not concentrate for proportional hyperedge size.

For each fixed positive integer \(k\), the separate finite-order law is
\[
\sqrt n(H_{n,k}-\mu)\ \Rightarrow\ N(0,k^2C(1/k)).
\tag{4}
\]
The differing fixed- and growing-rank variance constants make the order of limits important.

## Assumptions and scope

Only simple unlabeled-edge hypergraphs with vertices labeled by \([n]\) are used. Every hyperedge has cardinality \(k\); distinct hyperedges are selected at most once. The associated zonotope has generators \(v_S\) without any additional scaling. The Gaussian direction \(G\) is *not* normalized to the unit sphere. Equation (1) holds for every finite \(n\ge2\), \(1\le k\le n-1\). Equation (2) requires both \(k\to\infty\) and \(k/n\to0\), while (3) requires \(k/n\to\alpha>0\). No assertion of these laws for nongeneric directions, weighted hyperedge families or Haar-spherical normalization is made. The statements concern probability distributions of widths, not the uniform-volume distribution within the zonotope.

## Proof

**1. Exact width and second moment.** The support function of \([0,v]\) is \(\max\{0,\langle v,G\rangle\}\). Support functions add under Minkowski addition, so the width is the sum of the absolute support values asserted above. Each \(V_S=k^{-1/2}\sum_{i\in S}G_i\) is standard normal. For two independent uniformly selected \(k\)-sets \(S,T\), their overlap \(J=|S\cap T|\) has hypergeometric probability \(\binom kj\binom{n-k}{k-j}/\binom nk\); the pair \((V_S,V_T)\) has correlation \(J/k\). For centered unit normals with correlation \(u\), direct bivariate Gaussian integration yields
\[
\mathbb E|U||V|=\frac2\pi\bigl(\sqrt{1-u^2}+u\arcsin u\bigr).
\]
Subtracting \(\mu^2=2/\pi\), averaging over \(J\), gives (1), including overlap endpoints \(J=0,k\).

**2. Gaussian Hermite reduction.** Let \({\rm He}_r\) be the probabilists' Hermite polynomial of degree \(r\). Orthogonality in \(L^2\) of standard Gaussian measure gives
\[
|z|-\mu=a_2{\rm He}_2(z)+\sum_{r\ge2}a_{2r}{\rm He}_{2r}(z),
\qquad a_2=\frac\mu2=\frac1{\sqrt{2\pi}}.
\tag{5}
\]
All terms have even degree by symmetry. The sum of squared orthogonal component norms is \(1-2/\pi\). Define
\[
U_{n,k}=\binom nk^{-1}\sum_{|S|=k}(V_S^2-1),\qquad
R_{n,k}=H_{n,k}-\mu-a_2U_{n,k}.
\]
For correlated standard Gaussians with correlation \(u\), the expectation of equal Hermite degrees is \(r!u^r\), while distinct degrees are orthogonal. Hence the remainder covariance is nonnegative and bounded by \((1-2/\pi)u^4\) whenever \(0\le u\le1\). Averaging the covariance over all ordered subset pairs yields the rigorous error estimate
\[
\mathbb E R_{n,k}^2\le (1-2/\pi)\,\mathbb E(J/k)^4.
\tag{6}
\]
The elementary falling-factorial moment identity \(\mathbb E(J)_r=(k)_r^2/(n)_r\), together with \(J^4=(J)_1+7(J)_2+6(J)_3+(J)_4\), proves (uniformly for \(k\to\infty\), \(k/n\to0\))
\[
\mathbb E(J/k)^4=O\!\left(\frac1{nk^2}+\frac1{n^2}+\frac{k^2}{n^3}+\frac{k^4}{n^4}\right)
=o\!\left(\frac1n+\frac{k^2}{n^2}\right).
\tag{7}
\]
For small \(k\) the falling-factorial terms with \(r>k\) are zero. Thus (6) proves that \(R_{n,k}\) is negligible in \(L^2\) under either scaling in (2). This is an infinite-dimensional bound and does not rely on finite simulation.

**3. Exact quadratic decomposition.** Set
\[
A_n=\frac1n\sum_{i=1}^n(G_i^2-1),\qquad
X_n=\frac1{\sqrt n}\sum_{i=1}^nG_i,\qquad B_n=X_n^2-1.
\]
Counting inclusion of diagonal and off-diagonal terms in each subset square gives the exact identity
\[
U_{n,k}=\frac{n-k}{n-1}A_n+\frac{k-1}{n-1}B_n.
\tag{8}
\]
Write \(\sum_iG_i^2=X_n^2+Q_{n-1}\), where \(Q_{n-1}\sim\chi^2_{n-1}\) is independent of \(X_n\sim N(0,1)\), by the orthogonal decomposition of a Gaussian vector. Consequently
\[
(\sqrt n A_n,B_n)\ \Rightarrow\ (\sqrt2Y,X^2-1)
\]
with independent standard normals \(X,Y\). Insert this into (8), multiply by \(a_2\), and use the \(L^2\) estimate (7): if \(k/\sqrt n\to c\) the first line of (2) follows; if \(k/\sqrt n\to\infty\) while \(k/n\to0\), multiply by \(n/k\) to obtain its second line. The first limit is genuinely non-Gaussian for positive \(c\) because its nonzero third cumulant is inherited from \(X^2-1\).

**4. Proportional-rank reduction.** Conditional on \(X_n\), each \(V_S\) is Gaussian with conditional mean \(\sqrt{k/n}\,X_n\) and conditional variance \(1-k/n\). It follows *exactly* that
\[
\mathbb E(H_{n,k}\mid X_n)=f_{k/n}(X_n).
\tag{9}
\]
When \(k/n\to\alpha>0\), the hypergeometric overlap satisfies \(J/k\to\alpha\) in probability (for \(\alpha=1\) as well), because its mean is \(k/n\) and its variance is \((n-k)^2/[n^2(n-1)]\). Continuity and boundedness of \(C\) in (1) show \(\operatorname{Var}(H_{n,k})\to C(\alpha)\). On the other hand, two copies of \(\sqrt\alpha X+\sqrt{1-\alpha}Y\) conditionally independent given \(X\) have unconditional correlation \(\alpha\); hence \(\operatorname{Var}(f_\alpha(X))=C(\alpha)\). By (9), the conditional-variance identity gives
\[
\mathbb E\bigl(H_{n,k}-f_{k/n}(X_n)\bigr)^2
=\operatorname{Var}(H_{n,k})-\operatorname{Var}(f_{k/n}(X_n))\longrightarrow0.
\]
Since \(X_n\) is standard normal for every \(n\) and \(f_{p}(x)\) varies continuously in \(p\) in Gaussian \(L^2\), (3) follows.

**5. Fixed rank.** For fixed \(k\), \(H_{n,k}\) is an ordinary symmetric \(U\)-statistic of order \(k\), with kernel \(\left|k^{-1/2}\sum_{i=1}^kG_i\right|\). Its first Hoeffding projection, conditioning on one Gaussian, has variance \(C(1/k)\), by the same two-Gaussian absolute covariance identity with shared single coordinate. The nondegenerate first-projection central limit theorem yields (4), including \(k=1\). This completes the proof.

## Verification

The standalone Python file `check_uniform_width.py` enumerates every \(k\)-subset for \(2\le n\le11\), and checks (8) by exact rational arithmetic using seven independently chosen vectors for all 55 admissible parameter pairs (385 identities). It checks the exact hypergeometric fourth-moment formula, positivity and the Hermite-tail inequality against the analytic variance in every such pair. Additionally, 24,500 seeded Gaussian draws verify the mean and variance predictions within predeclared sampling tolerances for seven nontrivial parameter pairs. Executing `python3 check_uniform_width.py` completes with `UNIFORM_HYPERGRAPH_WIDTH_PASS`. Such computations check finite identities only; the infinite-rank and distributional statements are proved analytically above.

## Relationship to prior work

R. I. Liu's 2012 preprint (published 2013) explicitly defines the same rank-\(k\) degree-sequence zonotope and studies its integer points, lattice realization, and faces, not its Euclidean random widths. Bach, Eisenbrand and Pinchasi's May 11, 2023 preprint treats the *all-hyperedge* degree-sequence zonotope and its algorithmic and lattice properties. The present result studies its canonical uniform-rank constituents as Euclidean convex bodies and obtains the full Gaussian width variance and growing-rank stochastic transition. Classical Gaussian Hermite orthogonality and Hoeffding theory furnish proof tools, but no newly claimed theorem concerns their general statements. Existing width results for graphical zonotopes and Minkowski sums of simplices concern different generator families; one accessible summary of a closely titled hypergraphic-width result could not be checked in full and remains a priority caveat.

## Limitations

Priority is provisional; the analysis does not rule out an unpublished or unindexed equivalent formula, an implicit corollary of a broad variable-order \(U\)-statistic theorem, or a result in a not-fully-accessible hypergraphic-width paper. The theorem does not establish asymptotics for arbitrary deterministic hypergraphs or general non-Gaussian direction laws. A Haar-spherical width distribution is different from the unnormalized Gaussian width distribution here, and is not claimed. The exact error estimate assumes the stated growing-rank regime and cannot be used to infer (4) without the separate fixed-order argument.

## References

1. E. Bach, F. Eisenbrand, R. Pinchasi, *Integer points in the degree-sequence polytope*, arXiv:2305.06732v1 (first posted 2023-05-11), https://arxiv.org/html/2305.06732v1.
2. R. I. Liu, *Nonconvexity of the set of hypergraph degree sequences*, arXiv:1201.5989 (first posted 2012-01-28); *Electronic Journal of Combinatorics* 20(1) (2013), P21, https://doi.org/10.37236/2719.
3. W. Hoeffding, *A class of statistics with asymptotically normal distribution*, *Annals of Mathematical Statistics* 19 (1948), 293–325.
4. K. H. Huang, X. Liu, A. B. Duncan, A. Gandy, *A High-dimensional Convergence Theorem for U-statistics with Applications to Kernel-based Testing*, arXiv:2302.05686 (2023); distinct high-dimensional degree-two setting.
