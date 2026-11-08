# A unique asymptotic isotropic minimizer for intersections of cubes and cross-polytopes

## Finding

Fix \(\alpha>0\) and let
\[
K_d(\alpha)=[-1,1]^d\cap\left\{x:\sum_{i=1}^{d}|x_i|\le\alpha d\right\}.
\]
For a full-dimensional convex body \(K\subset\mathbb R^d\), define the affine-invariant isotropic constant by
\[
L(K)^2=\frac{(\det \operatorname{Cov}(X))^{1/d}}{\operatorname{Vol}_d(K)^{2/d}},\qquad X\sim\operatorname{Unif}(K).
\]
The dimension-first limit \(\mathcal L(\alpha)=\lim_{d\to\infty}L(K_d(\alpha))^2\) exists for every fixed \(\alpha>0\). It equals \(1/12\) for \(\alpha\ge1/2\). For \(0<\alpha<1/2\), let \(\lambda>0\) be the unique solution of
\[
\alpha=\frac1\lambda-\frac1{e^\lambda-1}.
\]
Set
\[
Z=\frac{1-e^{-\lambda}}\lambda,\qquad
m_2=\frac{2-(\lambda^2+2\lambda+2)e^{-\lambda}}{\lambda^2(1-e^{-\lambda})},\qquad
I=-\log Z-\lambda\alpha.
\]
Then
\[
\boxed{\mathcal L(\alpha)=\frac{m_2e^{2I}}4.}
\]
This function is strictly decreasing as \(\alpha\) moves down from \(1/2\) to \(\alpha_*\), and strictly increasing as \(\alpha\) moves down from \(\alpha_*\) to zero. It has exactly one global minimizer over all \(\alpha>0\), given by
\[
\lambda_*=2.84171173823727323921\ldots,\quad
\alpha_*=0.28996223506298880477\ldots,\quad
\mathcal L(\alpha_*)=0.06227292078418549618\ldots.
\]
In particular this limit is strictly less than both \(1/12\) (cube endpoint) and \(1/(2e^2)\) (small proportional-radius endpoint).

## Assumptions and scope

All limits are taken with dimension \(d\to\infty\) and fixed radius fraction \(\alpha>0\). The set is a symmetric intersection of a cube with a dilated cross-polytope in canonical Euclidean coordinates. The isotropic constant is affine invariant and uses uniform interior volume, not uniform vertex sampling. The optimization is of the pointwise dimension-first limit, not of finite-dimensional optimal truncation parameters.

## Proof

**1. Exact volume-to-moment reduction.** Let \(U_1,\ldots,U_d\) be independent \(\operatorname{Unif}[0,1]\) variables, \(S_d=\sum U_i\), and \(P_d=\Pr(S_d\le\alpha d)\). Reflection and permutation symmetry make the covariance of uniform volume on \(K_d(\alpha)\) a scalar matrix. Its diagonal entry is \(v_d=\mathbb E[U_1^2\mid S_d\le\alpha d]\), and its volume is \(2^dP_d\). Thus
\[
L(K_d(\alpha))^2=\frac{v_d}{4P_d^{2/d}}.
\]

**2. Exponentially tilted conditional law.** When \(0<\alpha<1/2\), the function \(m_1(\lambda)=1/\lambda-1/(e^\lambda-1)\) strictly decreases from \(1/2\) to zero: it is the mean of the truncated exponential density
\[
q_\lambda(u)=\frac{e^{-\lambda u}}Z\mathbf 1_{[0,1]}(u),\qquad Z=\int_0^1e^{-\lambda u}\,du,
\]
and \(m_1'(\lambda)=-\operatorname{Var}_{q_\lambda}(U)<0\). The equation \(m_1(\lambda)=\alpha\) therefore has one solution.

Under the product tilted law \(q_\lambda^{\otimes d}\), write \(T_d=S_d-d\alpha\). Change of measure gives the exact identity
\[
P_d=Z^d e^{\lambda\alpha d}\mathbb E_{q_\lambda^{\otimes d}}\left[e^{\lambda T_d}\mathbf 1_{T_d\le0}\right].
\]
The bounded, nonlattice tilted density has positive variance \(\sigma^2\), and the ordinary uniform local central limit theorem for sums with a bounded density yields
\[
\mathbb E_{q_\lambda^{\otimes d}}\left[e^{\lambda T_d}\mathbf 1_{T_d\le0}\right]
\sim\frac1{\lambda\sigma\sqrt{2\pi d}}.
\]
The same local limit for the remaining \(d-1\) coordinates, after conditioning on \(U_1=u\in[0,1]\), and dominated convergence yield
\[
\mathbb E[U_1^2\mid S_d\le\alpha d]\longrightarrow
\mathbb E_{q_\lambda}U^2=m_2.
\]
Hence \(P_d^{1/d}\to Ze^{\lambda\alpha}=e^{-I}\), proving the displayed formula. At \(\alpha>1/2\), the law of large numbers gives \(P_d\to1\) and \(v_d\to1/3\). At \(\alpha=1/2\), symmetry gives \(P_d=1/2\); conditioning on one coordinate and applying the central limit theorem gives \(v_d\to1/3\). Therefore \(\mathcal L(\alpha)=1/12\) throughout \(\alpha\ge1/2\).

**3. Exact derivative and unique turning point.** The moments of \(q_\lambda\) are \(m_j=\mathbb E_{q_\lambda}U^j\). Since
\[
\frac{d}{d\lambda}m_2=-\operatorname{Cov}(U^2,U),\qquad
\frac{dI}{d\lambda}=\lambda\operatorname{Var}(U),
\]
the sign of \(F'(\lambda)\), where \(F(\lambda)=m_2e^{2I}/4\), is that of
\[
D(\lambda)=2\lambda\operatorname{Var}(U)m_2-\operatorname{Cov}(U^2,U).
\]
Direct substitution of the first three moments gives the exact factorization
\[
D(\lambda)=-\frac{e^{-\lambda}B(\lambda)}{\lambda^2(1-e^{-\lambda})^3},
\]
where
\[
B(\lambda)=-\lambda^2+4\lambda+2-(2\lambda^3+3\lambda^2+6\lambda+4)e^{-\lambda}+(2\lambda+2)e^{-2\lambda}.
\]
Put \(P(\lambda)=e^{2\lambda}B(\lambda)\). Write \(P(\lambda)=\sum_{n\ge0}c_n\lambda^n/n!\). Direct differentiation yields
\[
c_0=\cdots=c_4=0,\quad(c_5,c_6,c_7,c_8,c_9)=(10,46,112,132,-258),
\]
and, for every integer \(n\ge3\),
\[
c_n=2^{n-2}(-n^2+9n+8)-2n(n-1)(n-2)-3n(n-1)-6n-4.
\]
Thus \(c_n<0\) for every \(n\ge9\): check \(n=9\) directly and note \(-n^2+9n+8<0\) for \(n\ge10\). Therefore
\[
\frac{P(\lambda)}{\lambda^8}=
\frac{10}{5!\lambda^3}+\frac{46}{6!\lambda^2}+\frac{112}{7!\lambda}+\frac{132}{8!}-\sum_{n=9}^{\infty}\frac{|c_n|}{n!}\lambda^{n-8}
\]
is strictly decreasing on \((0,\infty)\), from \(+\infty\) to \(-\infty\). It vanishes at exactly one point \(\lambda_*\). The sign of \(F'\) is negative before this root and positive after it. Since \(\alpha\) decreases strictly as \(\lambda\) increases, the unique global minimizer in the nonconstant region corresponds to \(\alpha_*\). The whole function outside it is the larger constant \(1/12\).

**4. Endpoints and numerical location.** As \(\lambda\to0\), \(q_\lambda\) becomes uniform, giving \(F\to1/12\). As \(\lambda\to\infty\), the tilted law approaches an untruncated exponential on its natural \(1/\lambda\) scale, with \(m_2\sim2/\lambda^2\), \(I\sim\log\lambda-1\), and \(F\to1/(2e^2)\). The rigorous strict inequality at the minimum follows from the preceding unique sign change and its interior location. Bisection on \(B(\lambda)=0\) locates the root and quoted constants.

## Verification

The accompanying standard-library Python checker separately integrates a coordinate square against the Irwin--Hall distribution via exact rational convolution and compares it with independent inclusion--exclusion formulas for volume and the coordinate second moment. It passes 153 exact-rational parameter pairs (dimensions 2--10), checks 101 derivative coefficient signs, checks the critical derivative factorization at 12 high-precision parameters, and bounds the unique root by bisection. The analytic coefficient-sign argument, not these finite checks, proves uniqueness in all dimensions. Reproduce with `python3 CHECK.py`.

## Relationship to prior work

The Gibbs/entropy method for large-dimensional volumes is developed by Kabluchko and Prochno (2020); their article explicitly discusses cube--norm-ball intersections and volume transitions. Alonso-Gutiérrez and Prochno (2020) obtain general limiting isotropic constants for finite-valued Orlicz balls. These results give strong context for the limiting formula. The present result's distinguishing conclusion is a sharp, unique **radius optimizer** for the cube--cross-polytope intersection family, with a sign-definite exponential-polynomial proof and a strict improvement over both endpoint limiting constants. The hard coordinate bound is not itself a finite-valued Orlicz potential, so direct applicability of the published isotropic theorem should not be asserted without approximation. Frühwirth and Prochno (2024) concern deviation laws for intersections, not optimization of their isotropic constants.

## Limitations

This is not an extremal theorem for all convex bodies or all interpolations between cube and cross-polytope. It does not locate finite-dimensional minimizers or justify exchanging optimization with the high-dimensional limit. Historical priority for the uniqueness statement remains provisional pending a wider examination of equivalent probabilistic or geometric formulations; no independent mathematical audit has occurred. The numerical constants are approximations to uniquely characterized quantities, not exact rational values.

## References

- Z. Kabluchko and J. Prochno, *The maximum entropy principle and volumetric properties of Orlicz balls*, arXiv:2007.05247, first submitted 2020-07-10, https://arxiv.org/abs/2007.05247.
- D. Alonso-Gutiérrez and J. Prochno, *Thin-shell concentration for random vectors in Orlicz balls via moderate deviations and Gibbs measures*, arXiv:2011.07523, first submitted 2020-11-15, https://arxiv.org/abs/2011.07523.
- L. Frühwirth and J. Prochno, *Sharp concentration phenomena in high-dimensional Orlicz balls*, arXiv:2407.15579, first submitted 2024-07-22, https://arxiv.org/abs/2407.15579.
