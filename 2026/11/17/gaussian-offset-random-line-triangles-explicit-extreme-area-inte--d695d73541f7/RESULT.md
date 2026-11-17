# Gaussian-offset random-line triangles: explicit extreme-area intensity and marked concurrency geometry

## Finding

For each integer \(n\ge3\), take \(n\) independent oriented-normal representations of unoriented affine lines
\[
L_i=\{x\in\mathbb R^2:(\cos\Theta_i,\sin\Theta_i)\cdot x=H_i\},
\qquad \Theta_i\sim\mathrm{Uniform}(0,\pi),\quad H_i\sim N(0,1),
\]
with all angular and offset variables mutually independent. Every three lines almost surely determine a bounded Euclidean triangle. Denote its area by \(A_{ijk}\), and set
\[
N_n(t)=\sum_{1\le i<j<k\le n}\mathbf1\{n^6A_{ijk}\le t\}\qquad(t>0).
\]
Define \(s_{ij}=\sin(\Theta_j-\Theta_i)\),
\[
P=|s_{12}s_{23}s_{31}|,\qquad
S=\sqrt{s_{12}^2+s_{23}^2+s_{31}^2},\qquad W=\frac{\sqrt P}{S}\in[0,1].
\]
The constant
\[
\kappa=\frac{\mathbb E W}{3\sqrt\pi}
=\frac{1}{3\pi^2\sqrt\pi}\int_0^\pi\!\int_0^\pi
\frac{\sqrt{|\sin a\sin b\sin(a-b)|}}{\sqrt{\sin^2a+\sin^2b+\sin^2(a-b)}}\,da\,db
\approx0.0654808676436
\]
is positive and finite. For every fixed \(t>0\),
\[
 d_{\mathrm{TV}}\bigl(\mathcal L(N_n(t)),\operatorname{Poisson}(\kappa\sqrt t)\bigr)
 =O_t(n^{-1}).
\]
Consequently, writing \(A_{\min,n}=\min_{i<j<k}A_{ijk}\),
\[
\lim_{n\to\infty}\Pr(n^6 A_{\min,n}>t)=\exp(-\kappa\sqrt t).
\]
The Weibull exponent and the general Poisson mechanism for very small triangles of stationary Poisson lines have appeared previously; **the specific nonstationary Gaussian-offset model, its explicit coefficient, finite-binomial rate, and the following conditional spatial and angular marks are the proposed contribution**.

For one triple, let \(B\) be the \(3\times2\) matrix of its three unit normal row vectors, \(X=(B^{\mathsf T}B)^{-1}B^{\mathsf T}H\) its least-squares near-concurrency point, and
\[
Q_h=\frac{s_{23}H_1+s_{31}H_2+s_{12}H_3}{\sqrt{2hP}}.
\]
As \(h\downarrow0\), conditional on \(A_{123}\le h\), its three directions have a joint law with density \(W/\mathbb EW\) relative to three independent uniform normal angles. Given the directions, \(X\) is exactly (for every \(h>0\)) a centered planar Gaussian with covariance \((B^{\mathsf T}B)^{-1}\), independent of \(Q_h\); \(Q_h\) tends to \(\operatorname{Uniform}(-1,1)\), independently of these angles and \(X\). The joint convergence of the directions, \(X\), and \(Q_h\) holds in total variation. This describes both where and how the rare near-concurrency occurs.

## Assumptions and scope

The directions are independent uniform in \([0,\pi)\), while the independently sampled **signed** offsets in the selected normal convention are standard Gaussian. All lines are independent; no conditioning on meeting a fixed window, enclosing the origin, or forming actual tessellation cells is imposed. Triple areas are finite almost surely because the direction law is continuous. The asymptotic count is for a fixed positive threshold \(t\), not for thresholds growing with \(n\). The least-squares point \(X\) is defined solely for one triple of lines, with \(B^{\mathsf T}B\) invertible almost surely. Conditioned on an exceptionally small area, \(X\) is asymptotically the common location of all three pairwise intersections away from exceptional near-parallel angles. The exact conditional Gaussian law refers to the least-squares \(X\), not to a prescribed vertex.

## Proof

**1. Area identity and one-triple asymptotic.** For any three nonparallel lines, elementary elimination for their three intersection points yields
\[
 A_{123}=\frac{Z^2}{2P},\qquad Z=s_{23}H_1+s_{31}H_2+s_{12}H_3.
\]
The identity can also be checked by solving the three pairs of two-by-two linear systems and applying the shoelace determinant. Conditional on the directions, \(Z\) is centered normal with variance \(S^2\). Therefore for every \(h>0\),
\[
 \Pr(A_{123}\le h\mid\Theta_1,\Theta_2,\Theta_3)
 =\operatorname{erf}(\sqrt h\,W).
\]
Since \(2P\le S^2\) (for example, because \(2|s_{12}s_{23}|\le s_{12}^2+s_{23}^2\) and \(|s_{31}|\le1\)), \(W\le1\). The uniform Taylor expansion of the error function then gives
\[
 p(h):=\Pr(A_{123}\le h)
 =\frac2{\sqrt\pi}\mathbb EW\sqrt h+O(h^{3/2}).
\]
Global rotation allows fixing \(\Theta_1=0\), proving the stated double integral for \(\mathbb EW\). Thus
\[
 \lambda_n=\mathbb EN_n(t)=\binom n3p(t/n^6)
 =\kappa\sqrt t+O_t(n^{-1}).
\]

**2. Rare-pair estimates.** For distinct unordered triples \(I,J\), their area indicators are independent if \(I\cap J=\varnothing\). For a pair sharing exactly one line, condition on its direction, offset, and the other four directions. The remaining Gaussian offsets used in each area are independent. If the shared line is labelled 1, the conditional variance in each area numerator arising from the other two offsets is \(s_{31}^2+s_{12}^2\). Consequently, using the upper bound on a centered Gaussian density and the arithmetic–geometric mean inequality,
\[
 \Pr(A_I\le h\mid\text{shared data})
 \le\frac2{\sqrt\pi}\sqrt h\,
 \frac{\sqrt{|s_{12}s_{23}s_{31}|}}{\sqrt{s_{12}^2+s_{31}^2}}
 \le\sqrt{2h/\pi}.
\]
The conditional independence implies \(\Pr(A_I\le h,A_J\le h)\le2h/\pi\).
For pairs sharing exactly two lines, condition on the two common offsets and all directions, and integrate the two remaining independent Gaussian offsets. Each probability is bounded by
\[
 \min\left\{1,\frac{2\sqrt h}{\sqrt\pi\,\sqrt{|\sin(\Theta_1-\Theta_2)|}}\right\}.
\]
The shared angular gap is uniform modulo \(\pi\); integrating its product bound gives
\[
 \Pr(A_I\le h,A_J\le h)=O\bigl(h\log(1/h)\bigr)\quad(h\downarrow0).
\]
No assertion about independence for overlapping triples is made.

**3. Sparse dependency graph and Poisson limit.** Connect all unordered triples that have a nonempty index intersection. The standard dependency-graph Chen–Stein inequality bounds total variation from a Poisson law of the same mean by a constant times the sum of products of individual probabilities and probabilities of overlapping events (with the customary factor \(\min\{1,1/\lambda_n\}\)). There are \(O(n^5)\) ordered neighboring pairs sharing one index, \(O(n^4)\) sharing two, and \(O(n^3)\) identical pairs. At \(h=t/n^6\), these contributions are
\[
 O(n^5p(h)^2)+O(n^5h)+O(n^4h\log(1/h))
 =O_t(n^{-1}),
\]
while identical pairs are excluded from the second sum. Since \(|\lambda_n-\kappa\sqrt t|=O_t(n^{-1})\), the Poisson laws with these means differ in total variation by at most that quantity. This proves the quantitative count limit and, by the zero-count event, the minimum-area law.

**4. Exact conditional spatial decomposition and marked limit.** Set \(c=(s_{23},s_{31},s_{12})^{\mathsf T}\). Its dot product with each column of \(B\) is zero, \(\|c\|=S\), and \(\det(B^{\mathsf T}B)=S^2\). Gaussian orthogonal decomposition gives
\[
 H=BX+\frac{c}{S}V,\qquad
 V=Z/S\sim N(0,1),\qquad
 X\mid B\sim N_2(0,(B^{\mathsf T}B)^{-1}),
\]
where \(X,V\) are conditionally independent. Area is \(A_{123}=V^2/(2W^2)\). With \(Q_h=V/(\sqrt{2h}\,W)\) and \(\lvert Q_h\rvert<1\), the unnormalized joint conditional density of \((\Theta_1,\Theta_2,\Theta_3,Q_h)\), relative to uniform angles and Lebesgue measure on \((-1,1)\), is
\[
 \sqrt{h/\pi}\,W\exp(-hW^2Q_h^2).
\]
The factor for the Gaussian \(X\mid B\) is independent and exact. Dominated convergence, using \(W\le1\) and \(\mathbb EW>0\), proves total-variation convergence to the product of the \(W/\mathbb EW\) angular tilt, \(N_2(0,(B^{\mathsf T}B)^{-1})\) conditional spatial mark, and independent \(\operatorname{Uniform}(-1,1)\) defect mark. This also verifies that angular degeneracies of measure zero cause no unjustified uniform-in-angle limit.

## Verification

The standalone file `line_triangle_check.py` (Python with NumPy, SciPy and Numba) reproduces the independent geometric determinant check against Cartesian line intersections for 5,000 triples, evaluates the angle integral by nested adaptive quadrature and an independent Gaussian-Legendre mesh sequence, compares the one-triple tail against its exact normal-error-function mixture, and samples small-area triangle counts for two sample sizes. Its successful terminal marker is `LINE_TRIANGLE_CHECKS_OK`; representative calculated values are \(\mathbb EW=0.3481854480467509\) and \(\kappa=0.06548086764362844\). The stochastic trials are consistency checks only, not proofs of asymptotic independence or the claimed error rate. The proof above supplies the requisite overlap estimates.

## Relationship to prior work

Schulte and Thäle (2012), specifically Theorem 2.6 and Corollary 2.7, already prove a \(t^6\)-area scaling, a square-root Weibull law and a Poisson limit for *stationary, isotropic Poisson lines restricted to a convex window*. These features, and the general Poisson-U-statistic mechanism, are **not claimed to be new**. Their sampling process uses a stationary Crofton-intensity law rather than exactly \(n\) globally independent Gaussian-offset lines, and the cited corollary does not specify the Gaussian-offset coefficient above, its \(O_t(n^{-1})\) fixed-binomial bound, or the conditional angular, least-squares-location and signed-defect marks. Decreusefond, Schulte and Thäle (2014/2016) give abstract functional Poisson approximation; the present contribution is an explicit nonstationary line-triangle realization and its geometric calculations. Chenavier and Hemsley (2015) study extreme **inradii** of cells in the stationary Poisson-line tessellation, a distinct statistic and sampling window. Daley, Ebert and Swift (2014) consider random triangles whose side directions are uniform with one side fixed at unit length; that is neither the present offset ensemble nor the same extreme experiment. Exact priority remains provisional, particularly for older stochastic-geometry literature not fully indexed.

## Limitations

Only unit-variance Gaussian signed offsets and uniform independently sampled normal angles are covered. The location mark is the least-squares concurrency point; exact joint independence of location and defect is conditional on the directions. The convergence rate holds with \(t\) fixed and the implicit constant depending on \(t\). The result does not classify arbitrary inhomogeneous line processes, random tessellation cells inside observation windows, or general anisotropic orientation laws. The numerical quadrature is not a closed elementary expression for \(\kappa\); its integral is mathematically exact. These findings have not received independent mathematical validation, and no assertion of historical priority beyond inspected sources is made.

## References

1. M. Schulte and C. Thäle (2012), *The scaling limit of Poisson-driven order statistics with applications in geometric probability*, arXiv:1201.5282, https://arxiv.org/abs/1201.5282 (Theorem 2.6, Corollary 2.7).
2. L. Decreusefond, M. Schulte, C. Thäle (2014 preprint; 2016 journal), *Functional Poisson approximation in Kantorovich–Rubinstein distance with applications to U-statistics and stochastic geometry*, arXiv:1406.5484, https://arxiv.org/html/1406.5484.
3. N. Chenavier and R. Hemsley (2015), *Extremes for the inradius in the Poisson line tessellation*, arXiv:1502.00135, https://arxiv.org/abs/1502.00135.
4. D. J. Daley, S. Ebert, R. J. Swift (2014), *Size distributions in random triangles*, Journal of Applied Probability 51A, 283–295, https://doi.org/10.1239/jap/1417528481 (abstract and bibliographic comparison; full text not inspected).
