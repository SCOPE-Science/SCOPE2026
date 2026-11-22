# Exact finite-sample calibration and a sharp positive lower edge for the one-dimensional uniform Euler-characteristic goodness-of-fit test

## Finding
Let \(n\ge2\) independent observations have the \(\operatorname{Uniform}(0,1)\) distribution, and write \(\Delta_n\) for the one-dimensional, *exactly null-centered* Euler-characteristic supremum goodness-of-fit statistic for the Čech filtration of the unscaled observations, with radius range \([0,T]\), \(T\ge1/2\). Put \(Z_n=\sqrt n\,\Delta_n\). Then \(Z_n\) admits the explicit finite inclusion-exclusion CDF in the proof below, supported on \([1/2,n-1]\). The nonzero minimum \(1/2\) is a sharp deterministic jump-size barrier, not an asymptotic claim.

Moreover, a nontrivial interval extending rightward from the lower endpoint has an exact product CDF. Write \(m=n-1\). For \(n\ge3\), let \(\beta_n\in(1/2,1)\) be the unique solution of
\[
\sum_{k=1}^{m}\left[1-\left(\frac{k-\beta_n}{m}\right)^{1/n}\right]=1.
\]
Set \(\beta_2=1\). For \(1/2\le z\le\beta_n\), put
\[
L_k(z)=\left(\frac{k-z}{m}\right)^{1/n},\qquad
V_k(z)=\left(\frac{k-1+z}{m}\right)^{1/n}.
\]
Then
\[
\boxed{\Pr(Z_n\le z)=n!m!\prod_{k=1}^{m}\bigl(V_k(z)-L_k(z)\bigr)
\left(1-m+\tfrac12\sum_{k=1}^{m}\bigl(V_k(z)+L_k(z)\bigr)\right).}
\]
In particular, if \(q_k=(k-1/2)/m\) and \(S_n=1-m+\sum_{k=1}^{m}q_k^{1/n}>0\), then
\[
\boxed{\Pr\bigl(Z_n\le 1/2+\varepsilon\bigr)
\sim C_n\varepsilon^{n-1},\quad
C_n=n!m!S_n\left(\frac{2}{nm}\right)^m
\prod_{k=1}^{m}q_k^{1/n-1}>0.}
\]
For \(n=2\), the entire CDF is \(\Pr(Z_2\le z)=2z-1\) on \([1/2,1]\).

## Assumptions and scope
The null is fully specified \(\operatorname{Uniform}(0,1)\), with distinct iid observations almost surely, known unit interval, exact population centering, and all radii needed to join every sample point; the Čech complexes are built using Euclidean balls of radius \(r\). The result does not assert the same finite distribution for a bounded shorter radius range, an estimated null, empirical Monte Carlo centering, a different ambient dimension, or a thermodynamic normalization without a corresponding rescaling of the radius range. Empty endpoint gaps must not be treated as additional bridges between observations. All formulas hold for each integer \(n\ge2\); convergence in the displayed small-ball formula is at fixed \(n\).

## Proof
**1. Reduction to sorted internal gaps.** Let \(U_{(1)}<\cdots<U_{(n)}\) be the sample order statistics, and \(G_i=U_{(i+1)}-U_{(i)}\), \(1\le i\le m\). In one dimension the Euler characteristic of the Čech complex counts connected components of the union of radius-\(r\) intervals. Hence
\[
\chi(r)=1+\sum_{i=1}^{m}\mathbf 1\{G_i>2r\},\qquad
\mathbb E\chi(r)=1+m(1-2r)_+^n.
\]
The second identity uses \(\Pr(G_i>x)=(1-x)^n\), \(0\le x\le1\), from uniform order statistics. Write \(H_1>\cdots>H_m\) for the descending arrangement of the internal gaps and \(p_k=(1-H_k)^n\). Immediately before and after its \(k\)-th largest-gap jump the centered component counts are respectively \(k-mp_k\) and \(k-1-mp_k\), up to sign. Between jumps the centering is monotone, and before the first and after the last jumps the endpoint deviations cannot exceed the corresponding one-sided jump values. Therefore the supremum over the full radius range is exactly
\[
Z_n=\max_{1\le k\le m}\max\{|k-mp_k|,|k-1-mp_k|\}.
\]
For every sample this maximum is at least \(1/2\). For fixed \(z\), the event \(Z_n\le z\) is equivalent to all the simultaneous rank restrictions
\[
\ell_k(z)=\max\{0,(k-z)/m\}\le p_k\le
u_k(z)=\min\{1,(k-1+z)/m\}.
\]
Thus \(A_k(z)=1-\nu_k(z)^{1/n}\le H_k\le B_k(z)=1-\ell_k(z)^{1/n}\).

**2. Finite CDF formula for arbitrary \(z\).** For \(z<1/2\) the probability vanishes, and for \(z\ge m\) it equals one. For \(1/2\le z<m\), form the strictly increasing distinct endpoints \(0=t_0<t_1<\cdots<t_J=1\) from \(0,1,A_1,\ldots,A_m,B_1,\ldots,B_m\). For a nonnegative integer vector \(c=(c_1,\ldots,c_J)\) with \(\sum_jc_j=m\), assign \(c_j\) internal gaps to the half-open cell \([t_{j-1},t_j]\). List its cell indices \(j_k(c)\) in *descending* order, repeating \(j\) precisely \(c_j\) times. Call \(c\) admissible if \([t_{j_k(c)-1},t_{j_k(c)}]\subseteq[A_k,B_k]\) for every \(1\le k\le m\). Define \(x_+=\max(x,0)\) and
\[
P_c=\frac{m!}{\prod_{j=1}^Jc_j!}
\sum_{h_1=0}^{c_1}\cdots\sum_{h_J=0}^{c_J}
(-1)^{\sum_jh_j}\prod_{j=1}^J{c_j\choose h_j}
\left(1-\sum_{j=1}^{J}c_jt_{j-1}-\sum_{j=1}^{J}h_j(t_j-t_{j-1})\right)_+^n.
\]
Then the exact **finite-sample null law**, for all \(1/2\le z<m\), is
\[
\boxed{\Pr(Z_n\le z)=\sum_{c\text{ admissible}}P_c.}
\]
Indeed, the vector consisting of \(m\) internal gaps and the two endpoint gaps has the \(\operatorname{Dirichlet}(1,\ldots,1)\) distribution with \(n+1\) coordinates. For any chosen internal coordinates and nonnegative thresholds \(s_i\), its joint survivor is \((1-\sum s_i)_+^n\). Inclusion-exclusion over the upper edges of each cell gives precisely the summand in \(P_c\); multiplying by \(m!/\prod c_j!\) counts which labeled gaps fall in each cell. Cells have probability-zero boundaries. An admissible allocation is exactly the intersection of the sorted-rank restrictions. This establishes the formula without asymptotics or simulation.

**3. Product region, support and sharp edge.** At \(z=1/2\), each rank interval collapses to the single proposed gap \(h_k^*=1-q_k^{1/n}\). Since \(x\mapsto x^{1/n}\) is strictly concave, midpoint integration gives \(\sum_kq_k^{1/n}>m\int_0^1x^{1/n}\,dx=mn/(n+1)\). Consequently
\[
S_n=1-m+\sum_kq_k^{1/n}>1-\frac{m}{n+1}=\frac{2}{n+1}>0.
\]
The gaps \(h_k^*\) are strictly decreasing and have sum less than one. They therefore define a permissible sample configuration (choose positive endpoint gaps to absorb the slack), proving that the deterministic lower bound \(1/2\) is sharp. The upper support endpoint \(m\) is approached by clustering all observations arbitrarily closely.

For \(1/2\le z<1\), the rank intervals in gap space are strictly ordered and have boundaries \(a_k(z)=1-V_k(z)\) and \(b_k(z)=1-L_k(z)\). Their largest possible total gap is \(\sum_kb_k(z)\), increasing continuously from a number below one to a number above one at \(z=1\) for \(n\ge3\). It equals one uniquely at \(z=\beta_n\). Hence, for \(z\le\beta_n\), *every point* of the rank-ordered rectangular box is in the internal-gap simplex. The internal-gap density there, after integrating the two endpoint gaps, is \(n!(1-\sum_kh_k)\); ordering multiplies it by \(m!\). Direct integration over the box gives \(n!m!\prod_k(b_k-a_k)\,[1-\tfrac12\sum_k(a_k+b_k)]\), exactly the displayed product formula. The case \(n=2\) is a direct one-gap integration.

Finally, setting \(z=1/2+\varepsilon\) yields \(V_k-L_k=(2/(nm))q_k^{1/n-1}\varepsilon+O(\varepsilon^2)\) and the bracket tends to \(S_n\). Multiplying all \(m\) factors proves the sharp \(\varepsilon^{n-1}\) law and its positive coefficient.

## Verification
The standalone `check.py` implements the exact finite inclusion-exclusion CDF, the product-region formula and its transition point, the endpoint coefficient and the directly evaluated gap statistic. Running `python check.py` with Python 3.10+ and `mpmath` 1.3+ reports 53 passing checks, including independent agreement between both exact formulas, small-deviation coefficient convergence and ancillary seeded simulations. Representative CDF values are \(\Pr(Z_3\le0.7)=0.0884815993675377351\) and \(\Pr(Z_4\le1.3)=0.615278908664878501\); \(C_3=2.19183094800470891\), \(\beta_3=0.983523951793910068\). Numerical checks supplement the exact proof and do not certify all sample sizes.

## Relationship to prior work
Dłotko, Hellmer, Stettner and Topolnicki introduced the Euler-characteristic-based goodness-of-fit test and studied its general-dimensional formulation, large-sample behavior and practical simulation-based calibration. The present result concerns its exactly centered, fully filtered, one-dimensional uniform specialization: a sharp finite-sample CDF, exact support barrier and nontrivial endpoint asymptotics. Its derivation relies on classical uniform-spacing Dirichlet identities and finite inclusion-exclusion; neither technique is itself new. Earlier works of Durbin and Koziol on Kolmogorov–Smirnov and other tests based on *spacing empirical processes* are plausible overlapping background but operate with differently defined empirical spacing statistics; the full older texts were not available for decisive article-wide priority assessment. These distinctions are mathematical scope boundaries, not a proof of literature uniqueness.

## Limitations
The finite formula is computationally combinatorial and not optimized for large \(n\). No improved critical-value algorithm, asymptotic Gaussian limit, power comparison, composite-null calibration, or higher-dimensional extension is claimed. The exact null-centered statistic is not identical to a Monte Carlo-centered implementation. Earlier classical spacing-process results may provide overlapping general techniques or stronger coverage, and a specialist independent priority assessment remains appropriate.

## References
1. Dłotko, P., Hellmer, N., Stettner, D., and Topolnicki, B., *Topology-Driven Goodness-of-Fit Tests in Arbitrary Dimensions*, arXiv:2210.14965v1, first submitted 2022-10-25, https://arxiv.org/abs/2210.14965 ; journal DOI https://doi.org/10.1007/s11222-023-10333-0.
2. Durbin, J., *Kolmogorov-Smirnov tests when parameters are estimated with applications to tests of exponentiality and tests on spacings*, Biometrika (1975), DOI https://doi.org/10.1093/biomet/62.1.5.
3. Koziol, J. A., *On Goodness of Fit Tests Based on the Empirical Distribution Function for Uniform Spacings*, Journal of the Royal Statistical Society B (1977), DOI https://doi.org/10.1111/j.2517-6161.1977.tb01631.x.
