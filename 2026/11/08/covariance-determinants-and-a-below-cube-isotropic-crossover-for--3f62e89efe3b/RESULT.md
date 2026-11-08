# An exact isotropic determinant and a below-cube limit for layered chain polytopes

## Finding
For any \(k\ge1\) and positive integers \(m_1,\ldots,m_k\), let \(d=\sum_i m_i\), and let \(P\) be the ordinal sum of \(k\) antichains of respective sizes \(m_i\). Its standard-coordinate chain polytope is
\[
 C(\mathbf m)=\left\{x\in\mathbb R_{\ge0}^{d}:\sum_{i=1}^k\max_{1\le j\le m_i}x_{ij}\le1\right\}.
\]
Write \(X\) for a uniformly volume-distributed point of \(C(\mathbf m)\), \(\Sigma=\operatorname{Cov}(X)\), and \(D=(d+1)(d+2)\). Define
\[
 \lambda_i=\frac{(m_i+1)(m_i+2)}{12D},\qquad
 a_i=\frac{(m_i+1)(2m_i+1)}{6D},\qquad
 R=1-\frac3{2(d+1)}\sum_{i=1}^k\frac{m_i(m_i+1)}{2m_i+1}.
\]
Then \(R>0\), \(\operatorname{vol}_d C=\prod_i m_i!/d!\), and the **full covariance determinant** is
\[
 \boxed{\det\Sigma=R\prod_{i=1}^k a_i\lambda_i^{m_i-1}.}
\]
The coordinate means are \(\mathbb E X_{ij}=(m_i+1)/(2(d+1))\). In each layer the \((m_i-1)\)-dimensional coordinate-sum-zero space is an eigenspace of \(\Sigma\) with eigenvalue \(\lambda_i\); the remaining \(k\)-dimensional block-mean matrix is explicitly \(\operatorname{diag}(a_1,\ldots,a_k)-hh^{\mathsf T}\), with \(h_i=\sqrt{m_i}(m_i+1)/(2(d+1)\sqrt{d+2})\).

With the squared affine-invariant isotropic constant defined by
\[
 L(C)^2=\frac{(\det\Sigma)^{1/d}}{\operatorname{vol}_d(C)^{2/d}},
\]
let \(k\ge2\) be fixed and let all \(m_i\) grow, with \(m_i/d\) bounded away from zero. Then
\[
 \boxed{\log\bigl(12L(C(\mathbf m))^2\bigr)
 =-\frac{(k-1)\log d}{d}+O_k(1/d),}
\]
where the implicit constant is uniform when the layer proportions have a common positive lower bound. Consequently the isotropic constants approach the cube value \(L^2=1/12\) **from below**, independently of the limiting positive layer proportions. Finite members can lie above the cube value: the two-singleton case has \(L^2=1/(6\sqrt3)>1/12\), while \(C(30,30)\) already has \(L^2<1/12\). The case \(k=1\) is exactly a cube and has \(L^2=1/12\).

## Assumptions and scope
The integers \(k,m_i\) are arbitrary subject to \(k\ge1,m_i\ge1\). Coordinates use the standard Euclidean inner product and volume refers to ordinary \(d\)-dimensional Lebesgue volume. The asymptotic estimate assumes fixed \(k\), \(d\to\infty\), and \(\min_i(m_i/d)\ge\varepsilon>0\); it makes no assertion for growing \(k\) or vanishing layer proportions. The constant is affine-invariant but is computed in this canonical embedding.

## Proof
A maximal chain meets each layer once. Therefore its chain inequality, maximized over the choices of one element per layer, is precisely \(\sum_i\max_j x_{ij}\le1\), in addition to nonnegativity.

For every layer independently, choose one of its \(m_i!\) coordinate orderings. In the corresponding chamber, take successive nonnegative gaps \(g_{i,1},\ldots,g_{i,m_i}\) between ordered coordinates (including the gap from zero). The maximum of layer \(i\) is the sum of its gaps, so the chamber is affinely identified, by a determinant-one triangular transformation, with the standard simplex \(g\ge0,\sum_{i,r}g_{i,r}\le1\). The interiors of these \(\prod_i m_i!\) chambers are disjoint and equiprobable, giving \(\operatorname{vol}_d C=\prod_i m_i!/d!\).

Within each chamber the \(d\) gaps, together with their residual \(1-\sum g\), have the uniform Dirichlet law with \(d+1\) unit parameters. Thus every gap has mean \(1/(d+1)\) and
\[
 \mathbb E[g_sg_t]=\frac{1+\mathbf1_{s=t}}{(d+1)(d+2)}.
\]
For a labeled coordinate in layer \(i\), its ordering rank \(U\) is uniform on \(\{1,\ldots,m_i\}\), independently of the Dirichlet gaps. That coordinate is the sum of the first \(U\) gaps. If two coordinates share the layer, their distinct ranks are uniform ordered distinct elements of the same rank set; across layers the ranks are independent. Directly summing the Dirichlet second moments yields, for a coordinate \(a\) in layer \(i\) and \(b\) in layer \(j\),
\[
\begin{aligned}
 \mathbb E X_a&=\frac{m_i+1}{2(d+1)},\\
 \mathbb E X_a^2&=\frac{(m_i+1)(m_i+2)}{3D},\\
 \mathbb E(X_aX_b)&=\frac{(m_i+1)(m_i+2)}{4D}\quad(a\ne b,\ i=j),\\
 \mathbb E(X_aX_b)&=\frac{(m_i+1)(m_j+1)}{4D}\quad(i\ne j).
\end{aligned}
\]
Subtract products of the means. Each layer-contrast space then has eigenvalue \(\lambda_i\). For the normalized block-mean vectors \(\mathbf1_{m_i}/\sqrt{m_i}\), the remaining covariance matrix is \(A-hh^{\mathsf T}\), where \(A=\operatorname{diag}(a_i)\) and \(h_i\) has the displayed value. The matrix determinant lemma gives
\[
 \det(A-hh^{\mathsf T})=\left(\prod_i a_i\right)
 \left(1-\sum_i\frac{h_i^2}{a_i}\right)
 =\left(\prod_i a_i\right)R,
\]
which proves the determinant identity. Positivity also follows since \((m_i+1)/(2m_i+1)\le2/3\), hence \(R\ge1/(d+1)>0\).

For the asymptotic statement, put \(p_i=m_i/d\). The condition \(p_i\ge\varepsilon\) and fixed \(k\) imply uniformly
\[
 \log\det\Sigma
 =d\left(-\log12+2\sum_i p_i\log p_i\right)+O_{k,\varepsilon}(1).
\]
Indeed \(\lambda_i=p_i^2/12\,[1+O(1/d)]\), the \(k\) mean-block eigenvalues remain bounded above and below away from zero, and \(R\to1/4\). Stirling's formula yields
\[
 \log\operatorname{vol}_d C=d\sum_i p_i\log p_i
 +\frac{k-1}{2}\log d+O_{k,\varepsilon}(1).
\]
Combining these exact determinant and volume asymptotics in the definition of \(L(C)^2\) gives the stated logarithmic expansion, so its leading negative term dominates for fixed \(k\ge2\). For \(k=2,m_1=m_2=1\), direct substitution gives \(L^2=1/(6\sqrt3)\); for \((m_1,m_2)=(30,30)\), the strict inequality \(12^{60}\det\Sigma<\operatorname{vol}_{60}(C)^2\) follows by exact rational multiplication and is independently reproducible in the attached checker.

## Verification
The standalone Python 3 program `checker.py` uses only standard-library rational arithmetic. It separately reconstructs second moments from the gap-simplex chamber model and from closed formulas, computes determinants by exact rational elimination, and verifies the determinant expression for 15 different layer vectors (including three-layer and four-layer cases). It also checks both strict cube comparisons using integer inequalities, not floating-point estimates. The asymptotic expansion is proved analytically above; finite checks do not substitute for its proof.

## Relationship to prior work
Stanley introduced order and chain polytopes and their common volume interpretation via linear extensions. Ahmad, Fourier, and Joswig introduced the maximal-ranked-poset framework and obtained face-number comparisons for their chain-order interpolants, but not the covariance determinant or isotropic asymptotics here. Freij-Hollanti and Lundström treated face-vector behavior under ordinal sums, not these metric-volume invariants. A related earlier centroidal-inertia comparison of ordinal-sum order and chain polytopes gives a **trace difference** and a low-rank covariance difference, but neither determines either covariance determinant or yields the below-cube isotropic asymptotic. A published bound for centrally symmetric Hanner polytopes does not cover these generally noncentrally symmetric positive-coordinate chain polytopes.

## Limitations
The result does not establish a finite-dimensional monotonicity law for \(L(C(\mathbf m))\). In fact, sample values need not vary monotonically toward \(1/12\), and the asymptotic sign conclusion assumes fixed layer count and nonvanishing proportions. Historical novelty remains subject to discovery of earlier equivalent random-coordinate or determinantal formulations. The mathematical result has not been independently audited.

## References
1. R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry **1** (1986), 9–23. DOI: 10.1007/BF02187680.
2. I. Ahmad, G. Fourier, M. Joswig, *Order and chain polytopes of maximal ranked posets*, arXiv:2309.01626, first posted 2023-09-04. https://arxiv.org/abs/2309.01626.
3. R. Freij-Hollanti, T. Lundström, *\(f\)-vector inequalities for order and chain polytopes*, arXiv:2312.13890, first posted 2023-12-21. https://arxiv.org/abs/2312.13890.
4. *Unconditional Reflexive Polytopes*, Discrete & Computational Geometry (2020), section on chain polytopes and unimodular triangulations, DOI: 10.1007/s00454-020-00199-8.
