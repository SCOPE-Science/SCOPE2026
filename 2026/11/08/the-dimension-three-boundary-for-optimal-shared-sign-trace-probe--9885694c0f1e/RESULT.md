# The dimension-three boundary for optimal shared-sign trace probes

## Finding
For any real symmetric positive-definite matrix \(L\) and real scalar functions \(f,g\) both nondecreasing on its spectrum, the usual common-Rademacher-probe trace-contrast estimator
\[
T_{\rm common}=Z^{\mathsf T}f(L)Z-Z^{\mathsf T}g(L)Z
\]
has variance no larger than the estimator with two independent uniform sign vectors, but it need not have the smallest variance **among couplings preserving both full Rademacher marginals**. Dimension \(3\) is the smallest where strict suboptimality can occur; in dimension \(2\), common signs always minimize the variance.

For arbitrary real symmetric \(3\times3\) matrices \(F,G\), write their off-diagonal triples as \((a,b,c)=(F_{12},F_{13},F_{23})\) and \((d,e,f)=(G_{12},G_{13},G_{23})\). The common-probe choice \(W=Z\) minimizes
\[
\operatorname{Var}(Z^{\mathsf T}FZ-W^{\mathsf T}GW)
\]
over **all joint distributions** in which \(Z\) and \(W\) each have three independent fair sign coordinates if and only if all six quantities
\[
(a+b)(d+e),\quad(a+c)(d+f),\quad(b+c)(e+f),
\]
\[
(a-b)(d-e),\quad(a-c)(d-f),\quad(b-c)(e-f)
\]
are nonnegative. A strict negative quantity implies that common signs are strictly suboptimal. This is an exact characterization, including ties and zero off-diagonal coefficients.

As a concrete *same-matrix, increasing spectral-function* example, set
\[
L=\begin{pmatrix}4&1&2\\1&20&0\\2&0&3\end{pmatrix},
\qquad F=L,\qquad G=\frac1{12}L^2.
\]
Here \(L\) is strictly diagonally dominant and positive definite. Let \(P\) swap the second and third coordinates, and choose \(W=PZ\). This coupling is globally variance-optimal, with both full Rademacher marginals preserved and the same two matrix-function actions required per sample, yet
\[
\operatorname{Var}(Z^{\mathsf T}FZ-Z^{\mathsf T}GZ)=\frac{62}{9},
\qquad
\operatorname{Var}(Z^{\mathsf T}FZ-(PZ)^{\mathsf T}G(PZ))=\frac2{9}.
\]
The exact variance improvement is a factor of \(31\). With \(N\) independent paired samples the two variances are divided by \(N\); both estimators remain unbiased for \(\operatorname{tr}(F-G)\).

## Assumptions and scope
All matrices are real symmetric, all random sign vectors have *uniform joint Rademacher laws* (each sign coordinate independent), and any dependence **between** the two vectors is admissible. The cost comparison counts one application of each of the two prescribed matrix functions per paired sample, rather than setup costs of identifying an optimal coupling. For the nonnegative shared-probe covariance statement, \(f\) and \(g\) are real nondecreasing functions on the eigenvalues of the same symmetric \(L\). The dimension-three six-inequality criterion holds without the common-spectral-function assumption. At dimensions \(1\) and \(2\) the minimality assertion assumes the common-spectral-function monotonicity property.

## Proof
**1. Shared probes have nonnegative covariance under joint spectral monotonicity.** For a real symmetric matrix \(H\), let \(Q_H(Z)=Z^{\mathsf T}HZ\). Since Rademacher fourth moments kill unmatched off-diagonal index pairs,
\[
\operatorname{Cov}(Q_F(Z),Q_G(Z))=4\sum_{i<j}F_{ij}G_{ij}.
\]
Diagonalize \(L=U\operatorname{diag}(\lambda_k)U^{\mathsf T}\) and put \(p_{k\ell}=\sum_iU_{ik}^2U_{i\ell}^2\ge0\). The matrix \((p_{k\ell})\) is symmetric with row and column sums one. Expanding \(\operatorname{tr}(FG)-\sum_iF_{ii}G_{ii}\) and symmetrizing gives
\[
\operatorname{Cov}(Q_{f(L)}(Z),Q_{g(L)}(Z))
=2\sum_{k<\ell}p_{k\ell}
\bigl(f(\lambda_k)-f(\lambda_\ell)\bigr)
\bigl(g(\lambda_k)-g(\lambda_\ell)\bigr)\ge0.
\]
Independence makes this covariance zero, so coupling the two terms with one shared sign vector cannot increase the variance of their difference relative to independent sampling.

**2. Two coordinates are optimal.** For \(2\times2\) spectral functions, the off-diagonal entries of both \(f(L)\) and \(g(L)\) have the same sign or at least one vanishes: each equals a real common eigenvector factor times its own nonnegative spectral difference. A two-coordinate Rademacher quadratic form has exactly two equiprobable outputs (modulo the globally irrelevant sign). Because both outputs are ordered alike, the shared choice is a comonotone coupling. The rearrangement inequality maximizes the cross covariance over every coupling with fixed marginals. At dimension one the quadratic forms are constant.

**3. All joint sign couplings in three coordinates.** Modulo global sign, the eight uniform sign vectors form four equiprobable classes represented by
\[
(1,1,1),\quad(1,1,-1),\quad(1,-1,1),\quad(-1,1,1).
\]
After subtracting the common diagonal trace and dividing by two, the four values of the first quadratic form are
\[
a+b+c,\quad a-b-c,\quad -a+b-c,\quad -a-b+c.
\]
The second has the same formulas with \((d,e,f)\). Every joint coupling induces a \(4\times4\) doubly stochastic transportation matrix between these equiprobable class laws. Conversely, every such transportation matrix can be lifted to a joint distribution with uniform full sign marginals by adding independent fair global signs. By the Birkhoff--von Neumann theorem and the rearrangement inequality, maximum covariance pairs each sorted value with its sorted counterpart; the identical-class coupling is optimal exactly when there is **no inversely ordered pair of classes**. The six pairwise value differences are, up to the common factor two,
\[
b+c,\ a+c,\ a+b,\ a-b,\ a-c,\ b-c
\]
and analogously for \((d,e,f)\), proving the six necessary and sufficient inequalities. If one is negative, exchanging the two mismatched target classes strictly improves the covariance, and therefore strictly reduces contrast variance.

**4. Polynomial witness and exact values.** Direct multiplication yields
\[
L^2=\begin{pmatrix}21&24&14\\24&401&2\\14&2&13\end{pmatrix}.
\]
Its four quadratic outputs are \((33,25,29,21)\) for \(L\), and \((515,451,411,363)/12\) for \(L^2/12\). The sorted rankings disagree only by interchanging the second and third classes. The coordinate-swap permutation \(P\) realizes precisely that interchange, hence gives a globally covariance-maximizing and contrast-variance-minimizing joint sign coupling. From the uniform four-class distribution,
\[
\operatorname{Var}(Q_L)=20,\quad
\operatorname{Var}(Q_{L^2/12})=\frac{194}{9},\quad
\operatorname{Cov}(Q_L,Q_{L^2/12})=\frac{52}{3},
\]
while the coordinate swap raises covariance to \(62/3\). Substitution into the variance-of-difference identity gives \(62/9\) and \(2/9\). Strict diagonal dominance with positive diagonal makes \(L\) symmetric positive definite, and \(x\mapsto x\) and \(x\mapsto x^2/12\) are strictly increasing on its positive spectrum. This establishes the sharp dimension threshold.

## Verification
Run `python3 verify_coupling.py` in a Python standard-library environment. Its exact rational checks evaluate all \(24\) class permutations on a collection of integer edge triples, verify the six-inequality criterion including tie cases, test the exact quadratic-form distributions and the example's factor-\(31\) ratio, and test positive-definite two-dimensional polynomial instances. A recorded program output appears in `verification_output.txt`. The proof of all-coupling optimality follows from finite-dimensional transportation geometry and rearrangement, not from a finite enumeration of input matrices.

## Relationship to prior work
Frommer, Nasr Khalil and Ramirez-Hidalgo (2021, 2022) study multilevel variance reduction for Hutchinson-style matrix-function trace estimators, coupling random probes within correction differences. Hallman and Troester (2021, 2022) develop polynomial multilevel trace estimation, often with independent level probes. Cortinovis and Kressner (2020) give randomized trace error bounds; Meyer, Musco, Musco and Woodruff (2020, 2021) develop Hutch++ via low-rank variance reduction. The present result concerns the exact design of the **joint law** of two uniform sign probes for a fixed two-function trace contrast, not matrix-function approximation, allocation across levels or low-rank sketches. The rearrangement inequality and Birkhoff's theorem are classical; their use is not claimed as new.

## Limitations
The exact classification is three-dimensional. It does not provide an inexpensive optimal coupling in arbitrary dimension or account for computing a coupling. The example compares trace contrast variance, not accuracy of either marginal trace separately, and the two function evaluations in the example have unequal internal work if implemented as one versus two matrix-vector products. General coupling via sorting may be impractical for high-dimensional matrix-free computation. There may be older equivalent specializations of discrete optimal transport or sign-probe estimators; independent literature validation has not occurred.

## References
1. A. Frommer, M. Nasr Khalil, G. Ramirez-Hidalgo, *A Multilevel Approach to Variance Reduction in the Stochastic Estimation of the Trace of a Matrix*, arXiv:2108.11281v1 (25 August 2021), https://arxiv.org/abs/2108.11281.
2. E. Hallman and D. Troester, *A Multilevel Approach to Stochastic Trace Estimation*, arXiv:2103.10516v1 (18 March 2021), https://arxiv.org/abs/2103.10516.
3. A. Cortinovis and D. Kressner, *On Randomized Trace Estimates for Indefinite Matrices with an Application to Determinants*, arXiv:2005.10009, https://arxiv.org/abs/2005.10009.
4. R. Meyer, C. Musco, C. Musco and D. Woodruff, *Hutch++: Optimal Stochastic Trace Estimation*, arXiv:2010.09649, https://arxiv.org/abs/2010.09649.
5. Classical rearrangement inequality and Birkhoff--von Neumann theorem for doubly stochastic matrices (standard mathematical results).
