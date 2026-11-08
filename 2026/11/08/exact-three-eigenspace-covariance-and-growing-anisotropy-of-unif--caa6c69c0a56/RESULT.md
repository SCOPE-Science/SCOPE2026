# Exact three-eigenspace covariance and growing anisotropy of uniform partial-permutation vertices

## Finding
For every integer \(n\ge2\), consider the complete-bipartite matching polytope \(\mathcal D_n\subset\mathbb R^{n\times n}\): the convex hull of all zero-one matrices with at most one unit entry in each row and column. Sample a vertex \(X\) **uniformly over all vertices**, including the empty matching and matchings of every size. Equip matrix space with the Frobenius inner product and let \(\Sigma_n\) be the covariance operator of \(X\).

Set \(M_j=\sum_{k=0}^j\binom jk^2 k!=j!L_j(-1)\), with \(M_0=1\); let \(\mu=M_{n-1}/M_n\) and \(\eta=M_{n-2}/M_n\). Here \(L_j\) is the ordinary Laguerre polynomial. Define \(H=\mathbf1\mathbf1^{\mathsf T}/n\) and \(F=I-H\). The four Frobenius-orthogonal matrix projections
\[
Q_0(Y)=HYH,\quad Q_r(Y)=FYH,\quad Q_c(Y)=HYF,\quad Q_i(Y)=FYF
\]
resolve the **entire exact covariance operator** as
\[
\boxed{\Sigma_n=\lambda_0Q_0+\lambda_r(Q_r+Q_c)+\lambda_iQ_i,}
\]
where the three distinct eigenvalues and their multiplicities are
\[
\boxed{\begin{aligned}
\lambda_0&=\mu-n^2\mu^2+(n-1)^2\eta&&\text{(once)},\\
\lambda_r&=\mu-(n-1)\eta&&\text{(\(2n-2\) times)},\\
\lambda_i&=\mu+\eta&&\text{(\((n-1)^2\) times)}.
\end{aligned}}
\]
For every \(n\ge2\), these eigenvalues are **strictly ordered** \(0<\lambda_0<\lambda_r<\lambda_i\). Their scales differ sharply:
\[
\boxed{n^{3/2}\lambda_0\longrightarrow\frac12,\qquad
n^{3/2}\lambda_r\longrightarrow1,\qquad
n\lambda_i\longrightarrow1.}
\]
Consequently the intrinsic spectral condition number of the uniform-vertex covariance has the precise asymptotic
\[
\boxed{\lim_{n\to\infty}\frac{\lambda_i/\lambda_0}{\sqrt n}=2.}
\]
The scalar and row/column-sum directions become much softer than the doubly centered interaction directions. In contrast, the subspace of doubly centered matrices of dimension \((n-1)^2\) retains the largest variance.

## Assumptions and scope
The uniform distribution is on the finite **vertex set**, not on Lebesgue volume inside the polytope, and it does not condition on matching cardinality. The polytope is the full-dimensional doubly substochastic matrix polytope \(\{Y\ge0:\sum_jY_{ij}\le1,\ \sum_iY_{ij}\le1\}\); its partial-permutation vertices are identified in Heuer–Striker. \(\Sigma_n\) is covariance in the ambient Frobenius metric, so eigenvalues are variances of projections onto unit Frobenius vectors. All statements hold for integers \(n\ge2\), and the limits are through positive integers.

## Proof
**1. Count vertices and calculate two-entry probabilities.** A matching of cardinality \(k\) in the complete bipartite graph has \(\binom nk^2k!\) choices. Thus the total vertex count is \(M_n=n!L_n(-1)\). A given matrix entry is occupied exactly when the remaining positions contain a partial permutation matrix of order \(n-1\), so \(\mathbb EX_{ij}=\mu\). Two entries in the same row or column cannot both occur. Two entries in distinct rows and columns are jointly occupied with probability \(\eta\). Hence the entrywise covariance is \(\mu-\mu^2\) on the diagonal, \(-\mu^2\) on same-row or same-column off-diagonal pairs, and \(\eta-\mu^2\) on disjoint pairs.

For a test matrix \(Y\), write \(r_i=\sum_jY_{ij}\), \(c_j=\sum_iY_{ij}\), and \(s=\sum_{ij}Y_{ij}\). Summing these three entry-pair types gives the **exact identity**
\[
(\Sigma_nY)_{ij}=(\mu+\eta)Y_{ij}-\eta(r_i+c_j)+(\eta-\mu^2)s.
\]
On the mutually orthogonal subspaces \(\operatorname{range}(Q_0)\), \(\operatorname{range}(Q_r)\), \(\operatorname{range}(Q_c)\), and \(\operatorname{range}(Q_i)\), this acts by \(\lambda_0,\lambda_r,\lambda_r,\lambda_i\), respectively. Their dimensions add to \(n^2\); this proves the complete spectrum and normalization.

**2. Prove strict ordering in every dimension.** Put \(K=\sum_{ij}X_{ij}\), the random matching size, and \(D=n-K\), its deficiency. The exact formulas above yield
\[
\lambda_0=\frac{\operatorname{Var}K}{n^2},\qquad
\lambda_r=\frac{\mathbb E[K(n-K)]}{n^2(n-1)},\qquad
\lambda_i-\lambda_r=n\eta.
\]
The first two are positive because all matching sizes occur with positive probabilities; the last difference is positive since \(\eta>0\). It remains to show \(\lambda_r>\lambda_0\).

The size-generating polynomial is
\[
A_n(t)=\sum_{k=0}^n\binom nk^2k!\,t^k=n!t^nL_n(-1/t).
\]
The ordinary Laguerre polynomial has \(n\) distinct positive zeros \(x_1,\ldots,x_n\). Therefore \(A_n(t)=\prod_{a=1}^n(1+x_at)\), so \(K\) has the law of a sum of independent Bernoulli variables whose success parameters \(p_a=x_a/(1+x_a)\) are distinct and lie strictly between zero and one. Put \(p=n^{-1}\mathbb EK\). Since the success parameters are not all equal,
\[
\operatorname{Var}K=\sum_ap_a(1-p_a)
<n p(1-p),
\]
where strictness follows from the strict concavity of \(u(1-u)\). A direct substitution in the eigenvalue formulas gives
\[
\lambda_r-\lambda_0=
\frac{np(1-p)-\operatorname{Var}K}{n(n-1)}>0.
\]
This proves \(0<\lambda_0<\lambda_r<\lambda_i\) for every \(n\ge2\) without numerical approximation.

**3. Establish the sharp three-scale limits.** Reindex the matching-size distribution by deficiency \(D=n-K\). Its probability generating function is exactly
\[
\mathbb Ez^D=\frac{L_n(-z)}{L_n(-1)},\qquad
L_n(-z)=\sum_{d=0}^n\frac{(n)_d}{(d!)^2}z^d,
\]
where \((n)_d\) is a falling factorial. Perron's classical complex-domain asymptotic (Szegő, Theorem 8.22.3) gives, locally uniformly in a complex neighborhood of \(z=1\),
\[
L_n(-z)=\frac{n^{-1/4}z^{-1/4}e^{-z/2}}{2\sqrt\pi}
 e^{2\sqrt{nz}}\left(1+O(n^{-1/2})\right).
\]
The analytic remainder is locally uniform away from the Laguerre zero cut; by Cauchy's derivative estimate its first two derivatives remain \(O(n^{-1/2})\) on a smaller neighborhood. Applying \(z\,\partial_z\) once and twice to the logarithm of the generating function at \(z=1\) consequently yields
\[
\mathbb ED=\sqrt n-\frac34+O(n^{-1/2}),\qquad
\operatorname{Var}D=\frac12\sqrt n-\frac12+O(n^{-1/2}).
\]
Therefore \(\lambda_0=\operatorname{Var}D/n^2\sim (2n^{3/2})^{-1}\). Moreover,
\[
\lambda_r=\frac{n\mathbb ED-\mathbb ED^2}{n^2(n-1)}\sim n^{-3/2}.
\]
Finally \(\mu=\mathbb EK/n^2=n^{-1}+O(n^{-3/2})\) and \(\eta=\mathbb E[K(K-1)]/[n^2(n-1)^2]=O(n^{-2})\), so \(\lambda_i\sim n^{-1}\). Dividing the extreme eigenvalue asymptotics gives the stated sharp condition-number constant \(2\).

## Verification
Run `python verify.py` with Python 3, NumPy, and SciPy. For orders \(2\), \(3\), and \(4\), the checker enumerates all vertices and uses **exact rational arithmetic** to reconstruct the covariance operator and its complete four-subspace eigenbasis; the resulting three eigenvalues are all distinct and positive. It separately checks finite Laguerre zeros for orders \(2\) through \(15\) and evaluates the deficiency moments and normalized eigenvalue limits at sizes \(1000\), \(5000\), and \(10000\). The verifier reports `PARTIAL_PERMUTATION_VERTEX_COVARIANCE_CHECKS_PASSED`. None of these finite computations substitutes for the all-dimensional spectral proof or Perron asymptotic above.

## Relationship to prior work
Heuer and Striker determine the vertex and inequality descriptions of partial-permutation polytopes, including their combinatorial framework. Eisley, Matsushita, and Vindas-Meléndez investigate Gorensteinness and integer decomposition of graph matching polytopes. An independently published calculation of the John ellipsoid of this same complete-bipartite matching polytope identifies the same *symmetry subspaces*, but determines the largest **inscribed ellipsoid**, not the covariance of uniform vertices; its squared-semiaxis asymptotics are of different orders and do not imply these vertex-moment eigenvalues. The classical Laguerre real-zero theorem and Perron asymptotic supply auxiliary ingredients and are not new. The claim here is the exact uniform-vertex covariance decomposition, its all-dimensional strict ordering, and the sharp diverging anisotropy law.

## Limitations
This result does not concern uniform interior volume measure, fixed-size matchings, rectangular matching polytopes, or arbitrary graphs. It does not claim that the three-eigenspace structure alone is new: that follows from row-column symmetry. The expressions for the eigenvalues and their strict ordering concern the specifically defined **uniform vertex law**. As with any priority claim based on bounded accessible literature, an older equivalent under random rook configurations or covariance-operator terminology cannot be ruled out absolutely; an independent literature audit has not been performed.

## References
1. D. Heuer and J. Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901, first posted December 17, 2020, https://arxiv.org/abs/2012.09901; especially the partial-permutation vertex description.
2. B. Eisley, K. Matsushita, and A. R. Vindas-Meléndez, *Matching polytopes, Gorensteinness, and the integer decomposition property*, arXiv:2407.08820v1, first posted July 11, 2024, https://arxiv.org/abs/2407.08820; matching-polytope context.
3. G. Szegő, *Orthogonal Polynomials*, 4th ed., American Mathematical Society, 1975, Theorem 8.22.3, https://people.math.osu.edu/nevai.1/SZEGO/szego%3Dszego1975%3Dops%3DOCR.pdf; Perron's Laguerre formula away from the positive real axis.
4. *Exact John ellipsoid of the doubly substochastic matrix polytope*, public mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-john-ellipsoid-of-the-doubly-substochastic-matrix-polytope--12b1169a9382; same polytope, different measure/invariant.
