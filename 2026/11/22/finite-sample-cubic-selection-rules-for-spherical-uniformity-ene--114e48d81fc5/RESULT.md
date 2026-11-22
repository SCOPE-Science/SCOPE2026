# Finite-sample cubic selection rules for spherical uniformity energies

## Finding

Let \(X_1,\ldots,X_n\) be independent uniform random points on the unit two-sphere, where \(n\ge 1\). For each integer \(\ell\ge1\), put \(d_\ell=2\ell+1\), \(K_\ell(x,y)=d_\ell P_\ell(x\cdot y)\), and
\[
T_\ell=\frac1n\sum_{i,j=1}^{n}K_\ell(X_i,X_j),
\]
where \(P_\ell\) is the Legendre polynomial with \(P_\ell(1)=1\). For any positive integer degrees \(\ell,m,k\), write
\[
G_{\ell m k}=d_\ell d_m d_k
\begin{pmatrix}\ell&m&k\\0&0&0\end{pmatrix}^{\!2}.
\]
Then the exact first, second, and joint third central cumulants are
\[
\begin{aligned}
\mathbb E T_\ell&=d_\ell,\\
\operatorname{Cov}(T_\ell,T_m)&=\mathbf 1_{\ell=m}\frac{2(n-1)d_\ell}{n},\\
\operatorname{cum}(T_\ell,T_m,T_k)&=\frac{4(n-1)}{n^2}G_{\ell m k}
+\mathbf 1_{\ell=m=k}\frac{8(n-1)(n-2)d_\ell}{n^2}.
\end{aligned}
\]
The notation \(\operatorname{cum}(T_\ell,T_m,T_k)\) denotes the expectation of the product of the three centered statistics. The Wigner coefficient can be evaluated entirely with factorials: when \(\ell+m+k\) is even and each degree is no greater than the sum of the other two, set \(s=(\ell+m+k)/2\). Then
\[
G_{\ell m k}=d_\ell d_m d_k\frac{(2s-2\ell)!(2s-2m)!(2s-2k)!}{(2s+1)!}
\left[\frac{s!}{(s-\ell)!(s-m)!(s-k)!}\right]^2.
\]
In every other case \(G_{\ell m k}=0\).

In particular, for \(n\ge2\), if the three degrees are not all equal, their joint third cumulant is strictly positive **exactly** when the even-parity and triangle conditions above hold, and otherwise it is exactly zero. Despite being pairwise uncorrelated at every \(n\), distinct harmonic energies can therefore retain third-order dependence. For example,
\[
\operatorname{cum}(T_1,T_2,T_3)=\frac{36(n-1)}{n^2},\qquad
\operatorname{Cov}((T_1-3)^2,T_2)=\frac{24(n-1)}{n^2}.
\]
More generally, for distinct positive degrees \(\ell,m\), the latter squared-deviation covariance is strictly positive precisely when \(m\) is even and \(m\le2\ell\), and is zero otherwise.

## Assumptions and scope

The sphere is \(\mathbb S^2\subset\mathbb R^3\); each observation has normalized rotation-invariant probability measure, without any density deformation or measurement noise. The sample size \(n\) is an integer at least one, and harmonic degrees are positive integers. The kernel includes the diagonal terms, so its definition and normalization are explicit. At \(n=1\), every statistic is deterministic and all centered cumulants vanish. The positive/zero selection assertion excludes the all-equal-degree case, for which the displayed complete formula applies without qualification.

With any orthonormal basis of real degree-\(\ell\) spherical harmonics in \(L^2\) of **probability** surface measure, the addition theorem gives
\[
K_\ell(x,y)=\sum_{a=1}^{d_\ell}Y_{\ell a}(x)Y_{\ell a}(y).
\]
Thus \(T_\ell\) is the natural nonnegative squared harmonic-sample-mean energy, multiplied by \(n\). The first two degrees correspond, after normalization, to the familiar dipole/Rayleigh and quadrupole/Bingham energy components.

## Proof

For every \(\ell>0\), spherical harmonic orthogonality and the addition theorem imply, for independent uniform \(X\),
\[
\mathbb E K_\ell(x,X)=0,\quad
K_\ell(x,x)=d_\ell,\quad
\mathbb E[K_\ell(x,X)K_m(X,y)]=\mathbf1_{\ell=m}K_\ell(x,y).
\]
Consequently, with \(A_\ell=T_\ell-d_\ell\),
\[
A_\ell=\frac2n\sum_{1\le i<j\le n}K_\ell(X_i,X_j).
\]
Expanding the product of two such sums, any two *different* sampled edges contain a sampled vertex appearing exactly once; integrating over that point gives zero. A repeated edge contributes \(\mathbb E K_\ell(X,Y)K_m(X,Y)=\mathbf1_{\ell=m}d_\ell\). The \(\binom n2\) repeated edges establish the covariance formula.

For a product of three centered energies, view its expansion as a multigraph of three edges on the sampled indices, including multiplicities. Integrating at a degree-one vertex annihilates its contribution. A loop is impossible because the centered energies contain only \(i<j\). The only surviving configurations are three identical edges, or the three edges of a triangle on three distinct sampled points. A repeated-edge configuration has expectation
\[
\mathbb E[K_\ell(X,Y)K_m(X,Y)K_k(X,Y)]
=\frac{d_\ell d_m d_k}{2}\int_{-1}^{1}P_\ell(t)P_m(t)P_k(t)\,dt
=G_{\ell m k}.
\]
The last equality is the classical Gaunt/Wigner \(3j\) identity for three Legendre polynomials (see the NIST DLMF reference). The Gaunt factorial expression makes its nonzero conditions and positivity explicit.

For a three-edge triangle, use the reproducing-kernel identity at successive vertices. The integral is zero unless all three degrees are equal; if equal, it is \(d_\ell\). There are \(\binom n2\) choices of a repeated edge, and \(6\binom n3\) ordered triangles. Multiplication by the expansion coefficient \((2/n)^3\) gives
\[
\mathbb E[A_\ell A_m A_k]
=\frac8{n^3}\left[\binom n2G_{\ell m k}
+6\binom n3\mathbf1_{\ell=m=k}d_\ell\right],
\]
which simplifies to the theorem. No asymptotic approximation or assumption of normality is used.

For the squared-deviation covariance, centeredness gives
\(\operatorname{Cov}(A_\ell^2,T_m)=\mathbb E[A_\ell^2 A_m]\). When \(m\ne\ell\), the Gaunt conditions for \((\ell,\ell,m)\) require that \(m\) be even and at most \(2\ell\), completing the corollary.

For each fixed finite collection of degrees, the multivariate central limit theorem applied to orthonormal harmonic coordinates yields independent Gaussian coordinate limits and, by continuous mapping, asymptotically independent chi-square energies \(\chi^2_{d_\ell}\). The finite-sample third-cumulant couplings therefore decay with \(n\), as the exact formula quantifies.

## Verification

Execute `python3 check_harmonic.py` with only Python's standard library. The checker independently builds rational Legendre polynomials, evaluates triple Legendre integrals exactly for all positive degrees one through eight, compares them to the factorial coefficient and verifies the complete triangle/parity selection rule. It then evaluates the relevant centered joint moments over all \(12^n\) samples of the regular icosahedron's twelve vertices at \(n=2,3,4\). Its spherical five-design property makes those particular low-degree integration tests exact in principle, not a Monte Carlo approximation; the actual float evaluation uses a numerical tolerance. All 1,562 assertions passed in the packaged run. These finite checks supplement, but do not replace, the general mathematical proof above.

## Relationship to prior work

The spherical-harmonic Sobolev-test framework, including Rayleigh and Bingham components and asymptotic laws, is established in García-Portugués and Verdebout (2018) and Borodavka and Ebner (first publicly posted 2023-01-09). Fernández-de-Marcos and García-Portugués (2023) give exact means and variances for new kernel-based tests, not the present cross-degree finite-sample third cumulants. Campbell's earlier analysis of finite-count angular power spectra gives exact **second-order** uncertainty and discusses higher-order source correlations; its specific estimator and variance result do not imply an explicit joint *third* cumulant for null isotropic harmonic energies. The Wigner \(3j\) coefficient and the Gaunt identity are classical; the claimed contribution is their exact finite-sample application to the complete cubic dependence pattern of these uniformity energies, not either identity alone.

## Limitations

This is an exact null-moment theorem, not a finite-sample critical-value computation, a proof of independence at finite \(n\), or a power claim against nonuniform alternatives. Only the two-sphere and the specified harmonic-energy normalization are treated. Cubic moments do not determine the full joint distribution. The closest inspected sources do not supply this particular joint law, but equivalent older results under angular power-spectrum or degenerate \(U\)-statistic terminology remain a historical-priority risk. Independent review has not been conducted.

## References

- J. Borodavka and B. Ebner, *A general maximal projection approach to uniformity testing on the hypersphere*, arXiv:2301.03482 (first posted 2023-01-09), https://arxiv.org/abs/2301.03482.
- E. García-Portugués and T. Verdebout, *An overview of uniformity tests on the hypersphere*, arXiv:1804.00286, https://arxiv.org/abs/1804.00286.
- A. Fernández-de-Marcos and E. García-Portugués, *On new omnibus tests of uniformity on the hypersphere*, arXiv:2304.04519 (first posted 2023-04-10), https://arxiv.org/abs/2304.04519.
- S. S. Campbell, *Angular Power Spectra with Finite Counts*, arXiv:1411.4031 (first posted 2014-10-24), https://arxiv.org/abs/1411.4031.
- NIST Digital Library of Mathematical Functions, §34.3 (Wigner \(3j\) and Gaunt integral formulas), https://dlmf.nist.gov/34.3.
