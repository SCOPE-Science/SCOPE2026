# An exponential occupancy law and an exact Gaussian cancellation for simplex Thales coverings

## Finding
Let \(d\ge 1\), put \(m=d+1\), and let \(P_d\) be a regular Euclidean \(d\)-simplex with centroid \(O\) and vertices \(v_1,\ldots,v_m\). Write \(D_i\) for the closed Euclidean ball having \([O,v_i]\) as a diameter. Choose \(X_d\) uniformly with respect to \(d\)-dimensional volume on \(P_d\), and define its Thales covering multiplicity by
\[
 M_d=\#\{i\in\{1,\ldots,m\}:X_d\in D_i\}.
\]
With \(p=e^{-2}\), the high-dimensional multiplicity obeys the following **sharp law of large numbers and central limit theorem**:
\[
 \boxed{\frac{M_d}{d+1}\longrightarrow p\quad\text{almost surely under the canonical exponential coupling},}
\]
\[
 \boxed{\frac{M_d-(d+1)p}{\sqrt{d+1}}\ \xrightarrow{\mathrm d}\ N\bigl(0,p(1-p)\bigr).}
\]
Thus a uniform point is typically covered by about \(13.5335 percent\) of the vertex-to-centroid diameter balls, although these balls are highly dependent. Surprisingly, the limiting fluctuation variance is **exactly the Bernoulli variance** \(p(1-p)\) of independent membership indicators with constant inclusion probability \(p\), despite the common random geometric threshold. For every dimension, \(1\le M_d\le d+1\) holds deterministically; this does not claim finite-dimensional binomiality.

## Assumptions and scope
The simplex is nondegenerate and regular, its source point is exactly its centroid, all diameter balls are closed, and \(X_d\) is uniform in the simplex's intrinsic volume. Changing the common Euclidean scale does not change membership. The almost-sure statement uses the joint construction from one infinite sequence of independent standard exponentials; without a coupling one can state convergence in probability. Dimension tends to infinity through integers. The normal limit includes the usual nonzero asymptotic variance \(e^{-2}(1-e^{-2})\). The theorem does not address arbitrary (nonregular) simplices, off-centroid source points, pointwise worst-case multiplicity, or the joint overlap volumes of prescribed subsets.

## Proof
**1. Exact geometric membership identity.** Put \(m=d+1\) and realize the simplex isometrically, up to a common scale, in the hyperplane \(H=\{y\in\mathbb R^m:\sum_i y_i=0\}\) with vertices \(v_i=e_i-\frac1m\mathbf1\) and centroid \(O=0\). A uniform point has barycentric coordinates \(\lambda=(\lambda_1,\ldots,\lambda_m)\), with \(\lambda_i\ge0\), \(\sum_i\lambda_i=1\), and \(X=\lambda-\frac1m\mathbf1\). By expanding the defining inequality for the ball of diameter \([0,v_i]\),
\[
 X\in D_i\iff\|X\|^2\le\langle X,v_i\rangle.
\]
Since \(\|X\|^2=\sum_j\lambda_j^2-1/m\) and \(\langle X,v_i\rangle=\lambda_i-1/m\), we obtain the **exact, every-dimensional identity**
\[
 \boxed{M_d=\sum_{i=1}^m\mathbf1_{\{\lambda_i\ge\sum_{j=1}^m\lambda_j^2\}}.}\tag{1}
\]
The maximum coordinate is at least the weighted average \(\sum_j\lambda_j^2=\sum_j\lambda_j\cdot\lambda_j\), proving \(M_d\ge1\). This also gives an elementary direct proof of the covering in this symmetric setting.

**2. Independent exponential representation and the strong law.** If \(E_1,E_2,\ldots\) are independent rate-one exponential random variables, then the normalized vector \((E_i/\sum_{j=1}^mE_j)_{i=1}^m\) is uniform on the barycentric simplex, i.e. has the Dirichlet distribution with all parameters one. Thus (1) becomes
\[
 M_d\overset{\rm d}=\sum_{i=1}^m\mathbf1_{\{E_i\ge T_m\}},\qquad
 T_m=\frac{\sum_{j=1}^mE_j^2}{\sum_{j=1}^mE_j}.
\tag{2}
\]
The strong law of large numbers gives \(T_m\to\mathbb E E^2/\mathbb E E=2\) almost surely. The empirical survival function \(S_m(t)=m^{-1}\sum_i\mathbf1_{\{E_i\ge t\}}\) converges uniformly almost surely to \(S(t)=e^{-t}\) for \(t\ge0\) (Glivenko–Cantelli, or monotone rational bracketing at \(t=2\)). Consequently \(M_d/m=S_m(T_m)\to e^{-2}\) almost surely.

**3. Fluctuation expansion.** Define \(U_m=m^{-1}\sum_iE_i\) and \(V_m=m^{-1}\sum_iE_i^2\). The two-dimensional central limit theorem and a first-order ratio expansion give
\[
 \sqrt m(T_m-2)=\frac1{\sqrt m}\sum_{i=1}^m(E_i^2-2E_i)+o_{\mathbb P}(1).\tag{3}
\]
The empirical-survival process is stochastically equicontinuous in a shrinking neighborhood of the fixed positive threshold \(2\); explicitly, for each fixed \(K\),
\[
 \sup_{|t-2|\le K/\sqrt m}\sqrt m\left|[S_m(t)-e^{-t}]-[S_m(2)-e^{-2}]\right|\xrightarrow{\mathbb P}0.\tag{4}
\]
One elementary proof of (4) uses a grid of mesh \(m^{-3/4}\) across this window. The number of grid points is \(O(m^{1/4})\), and each centered increment has variance at most \(O(m^{-3/2})\); Chebyshev and a union bound control the grid. Between grid points, monotonicity bounds the increment by an empirical interval count and its expected mass. Each interval has expectation \(O(m^{1/4})\) observations, and the binomial Chernoff bound gives a maximal count \(O_{\mathbb P}(m^{1/4})\) uniformly over the \(O(m^{1/4})\) intervals. After dividing by \(\sqrt m\), this is \(o_{\mathbb P}(1)\). Together with tightness of \(\sqrt m(T_m-2)\), (4) gives
\[
 \frac{M_d-mp}{\sqrt m}=\frac1{\sqrt m}\sum_{i=1}^m\left[\mathbf1_{\{E_i\ge2\}}-p-p(E_i^2-2E_i)\right]+o_{\mathbb P}(1).\tag{5}
\]
Here the coefficient \(-p\) comes from differentiating \(e^{-t}\) at \(2\).

**4. Exact variance cancellation and the Gaussian limit.** Let \(I=\mathbf1_{\{E\ge2\}}\) and \(H=E^2-2E\) for one rate-one exponential. Integration by parts and the factorial exponential moments yield
\[
 \mathbb EI=p,\quad \mathbb EH=0,\quad
 \operatorname{Var}(H)=24-4\cdot6+4\cdot2=8,
 \quad\operatorname{Cov}(I,H)=\int_2^\infty(x^2-2x)e^{-x}\,dx=4p.
\]
Therefore
\[
 \operatorname{Var}(I-p-pH)=p(1-p)+8p^2-8p^2=p(1-p).
\]
This is strictly positive. By the ordinary i.i.d. central limit theorem applied to (5), the stated Gaussian law follows. The cancellation is exact at the limiting influence-function level, not a claim that the finite-dimensional indicators are independent.

## Verification
The companion standalone Python checker `check.py` verifies (1) by two independent numerical formulations (Euclidean ball distances and the barycentric square-sum test) for multiple dimensions; tests finite-dimensional deterministic coverage; recomputes the moment identities in Step 4 exactly via factorials; and checks Monte Carlo mean and variance trends for increasing dimension with a fixed random seed. Run `python3 check.py` using Python 3 and no third-party dependencies. The finite computations illustrate the formulas and are not a proof of the almost-sure or distributional limits, which are established above by the strong law, empirical-process control, and the i.i.d. central limit theorem.

## Relationship to prior work
Pavlík [1, Section 5, Theorem 5.1 and Corollary 5.3] proves the full covering by Thales diameter balls and its power-diagram refinement for general polytopes, with no uniform-volume multiplicity law. The published regular-simplex Thales multiplicity-containment theorem [2] determines extremal radial reach, layer containment, and equality locations, not the distribution of multiplicity under uniform sampling. The classical uniform-simplex exponential representation and norm CLTs appear in Baci et al. [3, Sections 1, 3 and 5]; their \(\ell_q\)-norm asymptotics do not determine the random-threshold exceedance count in (2) or the exact variance cancellation. The published Greenwood/exceedance covariance theorem [4] gives the joint covariance of a **fixed-threshold** spacing count and quadratic concentration; its explicit one-switch law does not imply the Gaussian law for the **sample-dependent threshold** \(T_m\) without an additional empirical-process analysis. Ordinary empirical-process tools are used here, not claimed as novel. Searches for random Thales covering multiplicity and random Greenwood-threshold exceedance laws found no implication-equivalent theorem; unindexed literature remains a residual historical-priority risk.

## Limitations
Only the specific regular-simplex, centroid-source, uniform-volume asymptotic regime is proved. The fraction \(e^{-2}\) does not represent a finite-dimensional exact volume fraction and the Gaussian limit makes no finite-sample error-rate claim. This analysis does not classify higher-order joint intersections or arbitrary simplex geometries. Originality is relative to the identified inspected literature and mathematical-record comparisons, not independently certified historical priority.

## References
[1] Jan Pavlík, *Thales's theorem in higher dimensions*, arXiv:2611.14277v1, first publicly posted 10 November 2026, https://arxiv.org/html/2611.14277v1, Section 5.

[2] *Sharp multiplicity containment hierarchy for regular-simplex Thales balls*, published research note, https://github.com/published-finding corpus/2026/blob/main/2026/11/17/SCOPE-sharp-multiplicity-containment-hierarchy-for-regular-simplex-tha--d3a01e8b896a/RESULT.md.

[3] A. Baci, Z. Kabluchko, J. Prochno, M. Sonnleitner, C. Thäle, *Limit theorems for random points in a simplex*, arXiv:2005.04911v1, first publicly posted 11 May 2020, https://arxiv.org/abs/2005.04911, Sections 1, 3 and 5.

[4] *A universal one-switch covariance law for large spacings and convex spacing tests*, published research note, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-a-universal-one-switch-covariance-law-for-large-spacings-and-con--8cec2684e10a/RESULT.md.
