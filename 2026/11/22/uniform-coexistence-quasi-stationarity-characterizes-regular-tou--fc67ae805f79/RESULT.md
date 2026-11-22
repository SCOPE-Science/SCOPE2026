# Uniform coexistence quasi-stationarity characterizes regular tournament Wright–Fisher selection

## Finding

**Theorem.** Fix an integer \(d\ge2\), selection intensity \(\lambda>0\), and sampling intensity \(\gamma>0\). Let \(A\) be the skew-symmetric \(d\)-by-\(d\) tournament matrix: \(A_{ii}=0\) and \(A_{ij}\in\{-1,1\}\) for distinct indices. On the simplex \(\Delta_{d-1}\), consider the Wright–Fisher diffusion with interior generator
\[
\mathcal L f=\lambda\sum_{i=1}^d x_i(Ax)_i\partial_i f+\frac\gamma2\sum_{i,j=1}^d x_i(\delta_{ij}-x_j)\partial_{ij}f.
\]
The derivatives in this ambient expression are interpreted through smooth extensions of simplex functions; the operator is independent of the extension. Let \(\tau\) be the first time any coordinate vanishes, and let \(\nu=\operatorname{Dirichlet}(1,\dots,1)\) be the uniform probability on the simplex interior. Then \(\nu\) is quasi-stationary for the process killed at \(\tau\) **if and only if** \(A\mathbf1=0\), meaning the tournament is regular.

In that case, for every \(t\ge0\) and every measurable subset \(B\) of the open simplex,
\[
\Pr_\nu(X_t\in B,\tau>t)=e^{-\gamma\binom d2t}\nu(B).
\]
In particular the first species-loss time from uniform initial frequencies is exactly exponential, with rate \(\gamma\binom d2\), irrespective of the positive selection intensity or which regular tournament is chosen. A regular tournament has odd size.

Moreover \(h(x)=\prod_{i=1}^d x_i\) satisfies \(\mathcal Lh=-\gamma\binom d2h\), and its conservative Doob transform has drift \(\lambda x_i(Ax)_i+\gamma(1-dx_i)\) and stationary distribution \(\operatorname{Dirichlet}(2,\dots,2)\).

## Assumptions and scope

The process is the standard finite-dimensional Wright–Fisher diffusion with covariance matrix \(\gamma x_i(\delta_{ij}-x_j)\); time is not rescaled. Extinction means the **first** visit to the boundary, not eventual fixation at a vertex. Only uniform initial frequencies are asserted to have the exact selection-independent extinction law. No uniqueness of quasi-stationary distributions or convergence from arbitrary initial distributions is asserted.

The restriction \(\lambda>0\) is necessary for the converse: for \(\lambda=0\), all tournament matrices give the same neutral process and the uniform law is quasi-stationary. The condition \(A\mathbf1=0\) is equivalent to each vertex having \((d-1)/2\) wins and losses; in particular there is no such tournament when \(d\) is even.

## Proof

**1. Affine-coordinate adjoint identity.** Write \(u_i=x_i\), \(1\le i<d\), and \(x_d=1-\sum_{i<d}u_i\). Let \(m=d-1\). The affine generator has drift \(b_i=\lambda x_i(Ax)_i\), covariance \(a_{ij}=\gamma x_i(\delta_{ij}-x_j)\), for \(1\le i,j\le m\). Differentiating, using \(A_{ii}=0\) and \(A_{di}=-A_{id}\), gives
\[
\sum_{i=1}^{m}\partial_{u_i}[x_i(Ax)_i]
=\sum_{i=1}^m[(Ax)_i-x_iA_{id}]
=\sum_{i=1}^{d}(Ax)_i=\mathbf1^{\mathsf T}Ax.
\]
Likewise, each diagonal covariance term contributes \(-2\gamma\), and each ordered off-diagonal term contributes \(-\gamma\) to the double divergence; hence
\[
\sum_{i,j=1}^{m}\partial_{u_i}\partial_{u_j}a_{ij}
=-\gamma[2m+m(m-1)]=-\gamma d(d-1).
\]
The formal forward operator on constant affine density consequently obeys the **exact** identity
\[
\mathcal L^*1=-\lambda\mathbf1^{\mathsf T}Ax-\gamma\binom d2.
\tag{1}
\]

**2. Sufficiency and the absorbing boundary.** If \(A\mathbf1=0\), skew symmetry gives \(\mathbf1^{\mathsf T}A=0\), so (1) is the constant \(-\alpha\) with \(\alpha=\gamma\binom d2\). On each face, the selection drift has zero outward normal component: at \(x_i=0\) the corresponding drift vanishes, while the sum of all coordinate drifts is zero. Similarly, the covariance has vanishing normal row along each face. For instance, at \(x_d=0\), \(\sum_{i<d}a_{ij}=\gamma x_jx_d=0\).

Take a twice continuously differentiable test function vanishing on the boundary. Two integrations by parts against the constant density have no surviving boundary terms: the first boundary flux is zero by the normal degeneracy, and the remaining term contains the zero boundary value of the test function. Thus \(\int\mathcal Lf\,d\nu=-\alpha\int f\,d\nu\). The functionals \(e^{-\alpha t}\nu\) satisfy the forward weak evolution equation for the killed diffusion. Uniqueness of the killed Markov forward evolution (the standard well-posed Wright–Fisher martingale problem, stopped at the boundary) identifies them with the killed transition measures. This proves the stated identity, including exact exponential survival.

**3. Necessity.** Conversely, suppose \(\nu\) is quasi-stationary with decay rate \(\alpha'\). Differentiate the killed forward identity at time zero against arbitrary smooth test functions compactly supported in the interior. The adjoint identity (1) implies
\[
-\lambda\mathbf1^{\mathsf T}Ax-\gamma\binom d2=-\alpha'
\]
throughout the open simplex. Since \(\lambda>0\), the affine linear functional \(\mathbf1^{\mathsf T}Ax\) must be constant on the simplex. Its value at the barycenter is \(d^{-1}\mathbf1^{\mathsf T}A\mathbf1=0\) by skew symmetry, so it vanishes identically. Evaluating at the simplex vertices by continuity gives \(\mathbf1^{\mathsf T}A=0\), equivalently \(A\mathbf1=0\). This also forces \(\alpha'=\gamma\binom d2\).

**4. Positive eigenfunction and conditioned process.** For \(h=\prod_i x_i\), the selection part contributes \(\lambda h\sum_i(Ax)_i=0\) in the regular case. The second derivatives \(\partial_{ij}h=h/(x_ix_j)\) for \(i\ne j\) and zero diagonal second derivatives give \(\mathcal Lh=-\gamma\binom d2 h\). For every interior smooth test function, define
\[
\mathcal L^h f=h^{-1}\mathcal L(hf)+\gamma\binom d2 f.
\]
The gradient cross-term from the covariance is \(\sum_j a_{ij}\partial_{u_j}\log h=\gamma(1-dx_i)\) in affine coordinates. Therefore the transformed diffusion has the same covariance and drift \(\lambda x_i(Ax)_i+\gamma(1-dx_i)\). Since \(\nu\) is a left eigenmeasure and \(h\) a positive right eigenfunction for the same eigenvalue, the probability proportional to \(h\nu\) is invariant for the conservative transform. Multiplying the uniform simplex density by \(\prod_i x_i\) gives exactly \(\operatorname{Dirichlet}(2,\dots,2)\).

## Verification

The algebraic checker `checker.py` uses exact fractions and integers. It checks the balanced-tournament divergence cancellation and diversity-product cancellation at several interior rational points in dimensions \(3,5,7,9\); checks the general neutral second-divergence identity; and exhaustively enumerates all labeled tournaments in dimensions \(2\) through \(5\) to test the equivalence of balance and regularity. Its assertions corroborate, but do not replace, the symbolic proof for all dimensions. Run `python3 checker.py` with the standard Python library.

## Relationship to prior work

Angtuncio Hernández's 2026 treatment develops tournament Wright–Fisher diffusions and their multivariate Bernstein duality. It supplies the diffusion formulation and describes deterministic invariants for particular cyclic games, but the inspected statements do not imply an exact selection-independent **first-extinction** law or the above uniform quasi-stationary classification. General multitype Bernstein duality is not itself a quasi-stationary distribution formula.

The neutral two-allele uniform quasi-stationary law and the associated beta-shaped Doob process have classical precedents, including Huillet's 2011 analysis. The present claim is specifically the positive-selection regular-tournament characterization in arbitrary dimension, where nonzero circulating drift persists and uniform quasi-stationarity is not automatic.

## Limitations

The result concerns the first boundary hit from uniform initial frequencies, not the fixation time or a full quasi-stationary attraction domain. Regular tournaments exist only in odd dimensions. Existence or uniqueness of other quasi-stationary distributions under irregular tournament selection is not determined here. The available comparisons do not eliminate historical-priority risk from every older general spectral or conditioned-diffusion treatment. Independent mathematical validation has not been performed.

## References

1. O. Angtuncio Hernández, *Multivariate Bernstein duality for tournament Wright–Fisher diffusions*, arXiv:2611.13731v1 (first publicly submitted 2026-11-10), https://arxiv.org/abs/2611.13731.
2. T. E. Huillet, *Nonconservative Diffusions on [0, 1] with Killing and Branching: Applications to Wright–Fisher Models with or without Selection*, International Journal of Stochastic Analysis (2011), https://doi.org/10.1155/2011/605068.
3. S. Hummel, *Multi-type Λ-Wright–Fisher processes with polynomial drift: Bernstein duality*, arXiv:2610.14831 (background general duality framework), https://arxiv.org/abs/2610.14831.
