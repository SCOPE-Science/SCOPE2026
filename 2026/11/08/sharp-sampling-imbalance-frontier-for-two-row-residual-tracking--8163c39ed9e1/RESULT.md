# Sharp sampling-imbalance frontier for two-row residual-tracking Kaczmarz

## Finding

For the two-row rank-one least-squares matrix \(A=(1,1)^{\mathsf T}\), the residual-tracking VRRK-AS method with independent singleton sampling probabilities \((p,1-p)\), where \(0<p<1\), has a sharp *robust mean-square stability* step-size boundary. Put \(u=p(1-p)\) and
\[
F_u(\alpha)=(1-5u+4u^2)\alpha^3+(1-3u-u^2)\alpha^2-u^2.
\]
There is exactly one positive root \(\alpha_*(p)\) of \(F_u\), and the uniform guarantee of mean-square convergence for every right-hand side and every admissible initial iterate and residual table holds if and only if
\[
0<\alpha<\alpha_*(p).
\]
More precisely, below the boundary the full covariance evolution is exponentially stable. At the boundary an admissible initial error state exists for which mean-square convergence fails; above it an admissible initial state exists for which the mean-square error is unbounded. The sampling-optimal stability threshold is attained **only at uniform sampling**:
\[
\alpha_*(p)\le\alpha_*(1/2)=\frac{1}{\sqrt3},\qquad
\alpha_*(p)<\frac1{\sqrt3}\quad(p\ne\tfrac12).
\]
As a row becomes rarely sampled, \(\alpha_*(p)\sim\min\{p,1-p\}\). For example, the thresholds for \(p=1/10\) and \(p=1/4\) are approximately \(0.10182639437\) and \(0.27687985775\), whereas the balanced threshold is \(0.57735026919\). Nevertheless the signed mean primal error contracts for every \(0<\alpha<1\), independently of \(p\), exposing a sampling-dependent gap between signed-mean and mean-square convergence.

## Assumptions and scope

The matrix is \(A\in\mathbb R^{2\times1}\) with both rows equal to one. The data \(b_1,b_2\) are arbitrary real numbers, possibly inconsistent. The unique least-squares minimizer is \(x_\star=(b_1+b_2)/2\). At each iteration exactly one row is sampled, independently across iterations, with probabilities \(p\) and \(q=1-p\), both strictly positive. The step size \(\alpha>0\) multiplies the *unnormalized full-gradient estimator* of Algorithm 1 of Xie--Qi--Han (2026), not the averaged objective gradient. The stored residual vector may start at any real table, with the aggregate initialized consistently as its component sum. The source's prescribed zero-iterate initialization is included in this class; the sharp *necessity* assertion is for uniform stability across all such initializations, not for every particular prescribed initialization.

Set \(y=x-x_\star\), \(s_i=\bar r_i-(x_\star-b_i)\), and \(w=(y,s_1,s_2)^{\mathsf T}\). The aggregate error is \(s_1+s_2\), and, upon sampling index \(i\), the estimator is \(g=(y-s_i)/p_i+s_1+s_2\). Therefore the exact state recurrence is \(w^+=T_iw\), where
\[
T_1=\begin{pmatrix}
1-\alpha/p&\alpha q/p&-\alpha\\
1&0&0\\0&0&1
\end{pmatrix},\qquad
T_2=\begin{pmatrix}
1-\alpha/q&-\alpha&\alpha p/q\\
0&1&0\\1&0&0
\end{pmatrix}.
\]

## Proof

**Covariance reduction.** Since sampling is independent of the past, every symmetric covariance \(\Sigma_k=\mathbb E[w_kw_k^{\mathsf T}]\) satisfies the exact linear recurrence
\[
\Sigma_{k+1}=\mathcal L_{p,\alpha}(\Sigma_k),\qquad
\mathcal L_{p,\alpha}(\Sigma)=pT_1\Sigma T_1^{\mathsf T}+qT_2\Sigma T_2^{\mathsf T}.
\]
In the ordered six coordinates \((\Sigma_{00},\Sigma_{01},\Sigma_{02},\Sigma_{11},\Sigma_{12},\Sigma_{22})\), let \(M_{p,\alpha}\) denote this operator. Direct expansion of the displayed matrices, with no approximation, gives
\[
\det(I-M_{p,\alpha})=-4\alpha F_{p(1-p)}(\alpha).
\]
The standalone verifier reconstructs these six coefficients independently from the two state matrices and symbolically checks this factorization. At \(\alpha=0\) its characteristic polynomial is
\[
\chi_0(\lambda)=\lambda(\lambda-1)(\lambda-p)^2(\lambda-q)^2.
\]
Thus the eigenvalue one is simple; its right covariance eigenvector represents a common constant state \(y=s_1=s_2\), and first-order eigenvalue perturbation gives derivative \(-4\) at zero. The other eigenvalues have modulus strictly below one, so \(\rho(M_{p,\alpha})<1\) for all sufficiently small positive \(\alpha\).

**Exact stability boundary.** The covariance map preserves the closed pointed cone of positive-semidefinite \(3\times3\) real symmetric matrices. By the finite-dimensional Perron--Frobenius theorem for cone-preserving maps, its spectral radius is a real nonnegative eigenvalue. Since \(0<u\le1/4\), the coefficients \(1-5u+4u^2=(1-u)(1-4u)\) and \(1-3u-u^2\) are nonnegative, the latter strictly positive. Consequently \(F_u(0)=-u^2<0\), and \(F_u\) is strictly increasing on positive \(\alpha\), so it has precisely one positive zero.

A stable covariance operator can cross its unit spectral-radius boundary only through the eigenvalue \(+1\), due to cone positivity and continuity. The determinant factorization rules out such a crossing before \(\alpha_*(p)\); hence the spectral radius stays below one there and equals one at the root. For \(\alpha>\alpha_*(p)\), the determinant is strictly negative, which forces at least one real eigenvalue greater than one (nonreal pairs give positive contributions to the real determinant). Thus the spectral radius exceeds one there. A positive-semidefinite eigenmatrix at the spectral radius can be decomposed into finitely many rank-one covariances, proving that instability of this covariance operator is witnessed by at least one deterministic admissible initial state. In particular the full error cannot converge in mean square for all starts on or above the threshold. Exponential convergence below follows from the spectral-radius criterion.

**Sampling optimality.** Writing \(u=pq\), the implicit root decreases with increasing \(F_u\). But for every \(\alpha>0\) and \(0<u\le1/4\),
\[
\partial_uF_u(\alpha)=(-5+8u)\alpha^3+(-3-2u)\alpha^2-2u<0.
\]
Thus the positive root \(\alpha_*(u)\) is strictly increasing with \(u\), whose unique maximum occurs at \(p=q=1/2\). Here \(F_{1/4}(\alpha)=(3\alpha^2-1)/16\), giving \(1/\sqrt3\). Dividing \(F_u(\alpha)=0\) by \(u^2\) and setting \(\alpha=ut\) gives \(t\to1\) as \(u\downarrow0\), establishing \(\alpha_*(p)\sim\min\{p,q\}\). Finally \(\mathbb E[g\mid w]=2y\) yields \(\mathbb E[y_{k+1}]=(1-2\alpha)\mathbb E[y_k]\), so signed-mean convergence holds for \(0<\alpha<1\), irrespective of the covariance instability.

## Verification

Run `python verify.py` with SymPy and NumPy installed. The script constructs the two \(3\times3\) state matrices, lifts them to the exact six-dimensional covariance map, proves the determinant factorization and zero-step characteristic polynomial symbolically, checks the leading-eigenvalue derivative, and checks 45 independent one-step covariances over rational probabilities, steps, and starting vectors. It also tests representative spectral crossings numerically at probabilities \(1/10,1/4,2/5,1/2\). Numerical eigenvalue tests illustrate the exact proof rather than establish its all-parameter assertions.

## Relationship to prior work

Xie, Qi, and Han (2026) introduce the residual-tracking algorithm and give a sufficient convergence step bound for arbitrary sampling; their Proposition 3.4 identifies its JacSketch/SAGA equivalence. The result here uses that exact algorithm but calculates the **necessary and sufficient** stability boundary as a function of the *unequal sampling probabilities*. In their uniform two-row specialization, Remark 3.3 recommends \(\alpha=1/12\); the exact stability endpoint is \(1/\sqrt3\). Defazio, Bach, and Lacoste-Julien (2014), Gazagnadou, Gower, and Salmon (2019), and Morin and Giselsson (2025) study SAGA and sampling/step-size bounds but do not state the two-row cubic covariance boundary in the material inspected. The uniform-probability specialization is not separately claimed as new; the new contribution is the full nonuniform-sampling classification and its unique balance optimum.

## Limitations

The theorem applies to a rank-one two-row least-squares system with both row coefficients equal to one, iid singleton sampling, no momentum, and a constant step. It classifies robustness over all consistent initial residual-table states. It does not show that every specific initial state is unstable above threshold, does not optimize the convergence *rate* within the stable interval, and does not imply optimal sampling for heterogeneous rows, larger matrices, or different variance-reduction algorithms. As with any historical-priority assessment, unindexed analyses of specialized SAGA recurrences could contain equivalent formulas; no exhaustive uniqueness claim is made.

## References

1. J. Xie, H.-D. Qi, and D. Han, *Efficient variance reduction for randomized Kaczmarz methods via residual-tracking control variates*, arXiv:2610.39537v1 (first public 2026-10-29), Algorithm 1, Theorem 3.2, Remark 3.3, Proposition 3.4. https://arxiv.org/html/2610.39537v1
2. A. Defazio, F. Bach, and S. Lacoste-Julien, *SAGA: A Fast Incremental Gradient Method With Support for Non-Strongly Convex Composite Objectives*, arXiv:1407.0202 (2014). https://arxiv.org/abs/1407.0202
3. N. Gazagnadou, R. M. Gower, and J. Salmon, *Optimal mini-batch and step sizes for SAGA*, arXiv:1902.00071 (2019). https://arxiv.org/abs/1902.00071
4. M. Morin and P. Giselsson, *Sampling and Update Frequencies in Proximal Variance-Reduced Stochastic Gradient Methods*, Journal of Optimization Theory and Applications 205, 58 (2025). https://doi.org/10.1007/s10957-025-02671-y
5. F. Zhu, R. W. Heath Jr., and A. Mitra, *A Short and Unified Convergence Analysis of the SAG, SAGA, and IAG Algorithms*, arXiv:2602.05304 (2026). https://arxiv.org/abs/2602.05304
